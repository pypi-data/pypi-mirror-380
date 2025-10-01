"""Path mapping and validation for CVAT annotations.

This module provides functions for mapping different types of paths (reading order, merge, group, etc.)
to elements and validating their relationships.
"""

import logging
from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple

from .models import CVATAnnotationPath, CVATElement
from .tree import TreeNode, closest_common_ancestor, find_node_by_element_id
from .utils import (
    DEFAULT_PROXIMITY_THRESHOLD,
    get_deepest_element_at_point,
    is_caption_element,
    is_container_element,
    is_footnote_element,
)

logger = logging.getLogger(__name__)


@dataclass
class PathMappings:
    """Container for all path-to-element mappings."""

    reading_order: Dict[int, List[int]]  # path_id -> [element_id, ...]
    merge: Dict[int, List[int]]  # path_id -> [element_id, ...]
    group: Dict[int, List[int]]  # path_id -> [element_id, ...]
    to_caption: Dict[int, Tuple[int, int]]  # path_id -> (container_id, caption_id)
    to_footnote: Dict[int, Tuple[int, int]]  # path_id -> (container_id, footnote_id)
    to_value: Dict[int, Tuple[int, int]]  # path_id -> (key_id, value_id)


def map_path_points_to_elements(
    paths: List[CVATAnnotationPath],
    elements: List[CVATElement],
    proximity_thresh: float = DEFAULT_PROXIMITY_THRESHOLD,
) -> PathMappings:
    """Map all path types to their connected elements.

    Args:
        paths: List of CVAT annotation paths
        elements: List of elements to map paths to
        proximity_thresh: Distance threshold for point-to-element mapping

    Returns:
        PathMappings object containing all path-to-element mappings
    """
    reading_order: Dict[int, List[int]] = {}
    merge: Dict[int, List[int]] = {}
    group: Dict[int, List[int]] = {}
    to_caption: Dict[int, Tuple[int, int]] = {}
    to_footnote: Dict[int, Tuple[int, int]] = {}
    to_value: Dict[int, Tuple[int, int]] = {}

    for path in paths:
        touched_elements: List[int] = []
        for pt in path.points:
            deepest = get_deepest_element_at_point(pt, elements, proximity_thresh)
            if deepest:
                eid = deepest.id
                # Only add if not a duplicate in sequence
                if not touched_elements or touched_elements[-1] != eid:
                    touched_elements.append(eid)

        if not touched_elements:
            continue

        # Map based on path label
        if path.label.startswith("reading_order"):
            reading_order[path.id] = touched_elements
        elif path.label == "merge":
            merge[path.id] = touched_elements
        elif path.label == "group":
            group[path.id] = touched_elements
        elif path.label == "to_caption" and len(touched_elements) == 2:
            # First element should be container, second should be caption
            container_id, caption_id = touched_elements[0], touched_elements[1]

            # Get elements to check their types
            container_el = next((el for el in elements if el.id == container_id), None)
            caption_el = next((el for el in elements if el.id == caption_id), None)

            # Check if the relationship is backwards and auto-correct with warning
            if (
                container_el
                and caption_el
                and is_caption_element(container_el)
                and is_container_element(caption_el)
            ):
                logger.warning(
                    f"Caption path {path.id}: Backwards annotation detected, auto-correcting"
                )
                container_id, caption_id = caption_id, container_id

            to_caption[path.id] = (container_id, caption_id)
        elif path.label == "to_footnote" and len(touched_elements) == 2:
            # First element should be container, second should be footnote
            container_id, footnote_id = touched_elements[0], touched_elements[1]

            # Get elements to check their types
            container_el = next((el for el in elements if el.id == container_id), None)
            footnote_el = next((el for el in elements if el.id == footnote_id), None)

            # Check if the relationship is backwards and auto-correct with warning
            if (
                container_el
                and footnote_el
                and is_footnote_element(container_el)
                and is_container_element(footnote_el)
            ):
                logger.warning(
                    f"Footnote path {path.id}: Backwards annotation detected, auto-correcting"
                )
                container_id, footnote_id = footnote_id, container_id

            to_footnote[path.id] = (container_id, footnote_id)
        elif path.label == "to_value" and len(touched_elements) == 2:
            # First element should be key, second should be value
            to_value[path.id] = (touched_elements[0], touched_elements[1])

    # Resolve reading order conflicts before returning
    reading_order = _resolve_reading_order_conflicts(reading_order, paths, elements)

    return PathMappings(
        reading_order=reading_order,
        merge=merge,
        group=group,
        to_caption=to_caption,
        to_footnote=to_footnote,
        to_value=to_value,
    )


def _find_container_for_conflicted_path(
    path: CVATAnnotationPath, lost_elements: List[int], elements: List[CVATElement]
) -> Optional[CVATElement]:
    """Find container element for reading order path using existing spatial utilities."""
    from .tree import contains
    from .utils import is_container_element

    # Find containers that contain any of the lost elements, but path isn't fully inside
    container_candidates = []
    for element in elements:
        if is_container_element(element):
            # Skip if path is fully contained (violates constraint)
            if all(
                element.bbox.l <= x <= element.bbox.r
                and element.bbox.t <= y <= element.bbox.b
                for x, y in path.points
            ):
                continue

            # Check if container holds any lost elements
            for lost_id in lost_elements:
                lost_el = next((el for el in elements if el.id == lost_id), None)
                if lost_el and contains(element, lost_el):
                    container_candidates.append(element)
                    break

    return (
        min(container_candidates, key=lambda e: e.bbox.area())
        if container_candidates
        else None
    )


def _resolve_reading_order_conflicts(
    reading_order: Dict[int, List[int]],
    paths: List[CVATAnnotationPath],
    elements: List[CVATElement],
) -> Dict[int, List[int]]:
    """Resolve conflicts where elements appear in multiple reading order paths."""
    # Build path mappings (reuse existing pattern from associate_paths_to_containers)
    path_levels = {
        p.id: p.level or 1 for p in paths if p.label.startswith("reading_order")
    }
    path_by_id = {p.id: p for p in paths if p.label.startswith("reading_order")}

    # Find element conflicts
    element_to_paths: Dict[int, List[Tuple[int, int]]] = {}
    for path_id, element_ids in reading_order.items():
        level = path_levels.get(path_id, 1)
        for element_id in element_ids:
            element_to_paths.setdefault(element_id, []).append((path_id, level))

    conflicts = {
        eid: paths for eid, paths in element_to_paths.items() if len(paths) > 1
    }
    if conflicts:
        logger.info(f"Resolving {len(conflicts)} reading order conflicts")

    # Resolve conflicts: assign to deepest level, find containers for emptied paths
    emptied_paths: Dict[int, List[int]] = {}
    for element_id, path_level_pairs in conflicts.items():
        keep_path_id = max(path_level_pairs, key=lambda x: x[1])[0]
        for path_id, _ in path_level_pairs:
            if path_id != keep_path_id:
                reading_order[path_id].remove(element_id)
                emptied_paths.setdefault(path_id, []).append(element_id)

    # Add containers for paths that lost elements
    for path_id, lost_elements in emptied_paths.items():
        path = path_by_id.get(path_id)
        if path:
            container = _find_container_for_conflicted_path(
                path, lost_elements, elements
            )
            if container and container.id not in reading_order[path_id]:
                reading_order[path_id].append(container.id)
                logger.info(
                    f"Added container element {container.id} ({container.label}) to reading order path {path_id}"
                )

    return reading_order


def associate_paths_to_containers(
    mappings: PathMappings,
    tree_roots: List[TreeNode],
    paths: List[CVATAnnotationPath],
) -> Tuple[PathMappings, Dict[int, TreeNode]]:
    """Associate paths to their closest parent containers.

    Args:
        mappings: PathMappings object containing path-to-element mappings
        tree_roots: List of root nodes in the containment tree
        paths: List of all paths to check levels

    Returns:
        Tuple of (PathMappings, Dict[int, TreeNode]) where the dict maps path_id to container node
    """
    path_to_container: Dict[int, TreeNode] = {}

    # Create a mapping of path_id to path level for reading order paths
    path_levels = {p.id: p.level for p in paths if p.label.startswith("reading_order")}

    # Helper function to find common ancestor
    def find_common_ancestor(element_ids: List[int]) -> Optional[TreeNode]:
        touched_nodes: List[TreeNode] = [
            n
            for n in [find_node_by_element_id(tree_roots, eid) for eid in element_ids]
            if n is not None
        ]
        if not touched_nodes:
            return None
        return closest_common_ancestor(touched_nodes)

    # Associate reading order paths
    for path_id, el_ids in mappings.reading_order.items():
        # Skip level 1 reading order paths - they don't need containers
        if path_id in path_levels and (
            path_levels[path_id] == 1 or path_levels[path_id] is None
        ):
            continue

        ancestor = find_common_ancestor(el_ids)
        if ancestor is not None:
            path_to_container[path_id] = ancestor
        else:
            # fallback: parent of first touched element
            node = find_node_by_element_id(tree_roots, el_ids[0])
            if node and node.parent:
                path_to_container[path_id] = node.parent

    # Associate merge paths
    for path_id, el_ids in mappings.merge.items():
        ancestor = find_common_ancestor(el_ids)
        if ancestor is not None:
            path_to_container[path_id] = ancestor

    # Associate group paths
    for path_id, el_ids in mappings.group.items():
        ancestor = find_common_ancestor(el_ids)
        if ancestor is not None:
            path_to_container[path_id] = ancestor

    # Associate to_caption and to_footnote paths
    for path_id, (container_id, _) in mappings.to_caption.items():
        node = find_node_by_element_id(tree_roots, container_id)
        if node:
            path_to_container[path_id] = node

    for path_id, (container_id, _) in mappings.to_footnote.items():
        node = find_node_by_element_id(tree_roots, container_id)
        if node:
            path_to_container[path_id] = node

    # Associate to_value paths
    for path_id, (key_id, _) in mappings.to_value.items():
        node = find_node_by_element_id(tree_roots, key_id)
        if node:
            path_to_container[path_id] = node

    return mappings, path_to_container


def validate_caption_footnote_paths(
    elements: List[CVATElement],
    to_caption: Dict[int, Tuple[int, int]],
    to_footnote: Dict[int, Tuple[int, int]],
) -> List[str]:
    """Validate caption and footnote paths.

    Rules:
    1. Starting point of to_caption and to_footnote paths must be on a container element
    2. End point must be on a caption or footnote element, respectively
    3. If container elements are connected by a group path, only one member container of the group must have a to_caption or to_footnote path

    Returns:
        List of validation error messages
    """
    errors = []
    id_to_element = {el.id: el for el in elements}

    # Validate to_caption paths
    for path_id, (container_id, caption_id) in to_caption.items():
        container = id_to_element.get(container_id)
        caption = id_to_element.get(caption_id)

        if not container or not is_container_element(container):
            errors.append(
                f"Caption path {path_id}: Starting point is not a container element"
            )
        if not caption or not is_caption_element(caption):
            errors.append(f"Caption path {path_id}: End point is not a caption element")

    # Validate to_footnote paths
    for path_id, (container_id, footnote_id) in to_footnote.items():
        container = id_to_element.get(container_id)
        footnote = id_to_element.get(footnote_id)

        if not container or not is_container_element(container):
            errors.append(
                f"Footnote path {path_id}: Starting point is not a container element"
            )
        if not footnote or not is_footnote_element(footnote):
            errors.append(
                f"Footnote path {path_id}: End point is not a footnote element"
            )

    return errors
