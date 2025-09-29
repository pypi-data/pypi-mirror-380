"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

from typing import List, Dict, Tuple


def validate_mapping_completeness(mapping: List[Dict]) -> Dict:
    """
    # Validate mapping completeness by detecting TODO keys

    ## Arguments
    - `mapping` (List[Dict]): Dimensions mapping to validate

    ## Returns
    - `Dict`: Validation result with completion status and statistics
    """
    mapped_count, todo_count = count_mapping_statistics(mapping)
    total_count = len(mapping)
    completion_rate = (mapped_count / total_count * 100) if total_count > 0 else 0

    todo_entries = []
    for entry in mapping:
        reference_equivalence = entry.get("reference_equivalence", {})
        parent_hierarchy = entry.get("parent_hierarchy", {})

        if "TODO" in reference_equivalence or "TODO" in parent_hierarchy:
            todo_entries.append(entry)

    return {
        "total": total_count,
        "mapped": mapped_count,
        "todo": todo_count,
        "completion_rate": completion_rate,
        "todo_entries": todo_entries,
        "can_proceed": todo_count == 0,
    }


def count_mapping_statistics(mapping: List[Dict]) -> Tuple[int, int]:
    """
    # Count mapped vs TODO entries in mapping by detecting TODO keys

    ## Arguments
    - `mapping` (List[Dict]): Mapping data

    ## Returns
    - `Tuple[int, int]`: (mapped_count, todo_count)
    """
    mapped_count = 0
    todo_count = 0

    for entry in mapping:
        reference_equivalence = entry.get("reference_equivalence", {})
        parent_hierarchy = entry.get("parent_hierarchy", {})

        has_ref_todo = "TODO" in reference_equivalence
        has_parent_todo = "TODO" in parent_hierarchy

        if has_ref_todo or has_parent_todo:
            todo_count += 1
        else:
            if reference_equivalence or parent_hierarchy:
                mapped_count += 1

    return mapped_count, todo_count
