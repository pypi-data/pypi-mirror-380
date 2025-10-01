"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

from pathlib import Path
from typing import List, Dict, Optional, Tuple


def create_dimensions_mapping(
    source_dimensions: List[Dict], reference_dimensions: List[Dict]
) -> List[Dict]:
    """
    # Create mapping by matching source dimensions with reference data

    ## Arguments
    - `source_dimensions` (List[Dict]): Unique dimensions from input data
    - `reference_dimensions` (List[Dict]): Reference dimensions with hierarchies

    ## Returns
    - `List[Dict]`: Mapping with matched and TODO entries
    """
    reference_index = create_reference_indexes(reference_dimensions)
    mapping = []

    for dimension in source_dimensions:
        name, value = dimension["name"], dimension["value"]

        reference_entry = find_dimension_in_reference(name, value, reference_index)

        if reference_entry:
            mapping_entry = {
                "name": reference_entry.get("name", ""),
                "value": reference_entry.get("value", ""),
                "reference_equivalence": reference_entry.get("equivalence", {}),
                "parent_hierarchy": {
                    "default": get_parent_value(reference_entry) or "top-level"
                },
            }
        else:
            mapping_entry = {
                "name": name,
                "value": value,
                "reference_equivalence": {
                    "TODO": "check in 'data/references/dimensions.json' if this value exists under another name in reference"
                },
                "parent_hierarchy": {
                    "default": "parent_value",
                    "TODO": [
                        "if you found a reference equivalence, leave parent_hierarchy empty '{}' to use the equivalence parent value",
                        "or choose a parent value from input data or reference using 'data/references/dimensions.json'",
                    ],
                },
            }

        mapping.append(mapping_entry)

    return mapping


def resolve_single_mapping_entry(
    entry: Dict, reference_index: Dict, all_input_dimensions: List[Dict]
) -> Tuple[Dict, List[str], bool]:
    """
    # Resolve single mapping entry references and validate

    ## Arguments
    - `entry` (Dict): Single mapping entry to resolve
    - `reference_index` (Dict): Reference lookup indexes
    - `all_input_dimensions` (List[Dict]): All available input dimensions

    ## Returns
    - `Tuple[Dict, List[str], bool]`: (resolved_entry, errors, was_auto_resolved)
    """
    name = entry["name"]
    value = entry["value"]
    reference_equivalence = entry.get("reference_equivalence", {})
    parent_hierarchy = entry.get("parent_hierarchy", {})
    errors = []
    auto_resolved = False

    resolved_entry = entry.copy()

    if "TODO" in reference_equivalence or "TODO" in parent_hierarchy:
        errors.append(f"{name}={value}: Contains TODO keys, manual completion required")
        return resolved_entry, errors, auto_resolved

    hierarchy_keys = list(parent_hierarchy.keys())
    if len(hierarchy_keys) > 1:
        errors.append(
            f"{name}={value}: parent_hierarchy must contain only one value, got: {hierarchy_keys}"
        )
        return resolved_entry, errors, auto_resolved

    parent_value = next(iter(parent_hierarchy.values())) if parent_hierarchy else None

    if reference_equivalence:
        ref_value = (
            list(reference_equivalence.values())[0] if reference_equivalence else None
        )
        if ref_value:
            ref_entry = find_dimension_in_reference(name, ref_value, reference_index)
            if not ref_entry:
                errors.append(
                    f"{name}={value}: reference_equivalence '{ref_value}' not found in reference"
                )
            else:
                if not parent_hierarchy:
                    ref_parent = get_parent_value(ref_entry)
                    if ref_parent:
                        resolved_entry["parent_hierarchy"] = {"default": ref_parent}
                        auto_resolved = True
                        parent_value = ref_parent

    if parent_value and parent_value != "top-level":
        parent_exists = find_dimension_in_reference(
            name, parent_value, reference_index
        ) is not None or any(
            dim["name"] == name and dim["value"] == parent_value
            for dim in all_input_dimensions
        )

        if not parent_exists:
            errors.append(
                f"{name}={value}: parent '{parent_value}' not found in reference or input data"
            )

    return resolved_entry, errors, auto_resolved


def create_reference_indexes(reference_dimensions: List[Dict]) -> Dict:
    """
    # Create lookup indexes for reference dimensions (direct + equivalence, case-insensitive)

    ## Arguments
    - `reference_dimensions` (List[Dict]): Reference dimensions data

    ## Returns
    - `Dict`: Dictionary with 'direct' and 'equivalence' indexes
    """
    direct_index = {}
    equivalence_index = {}

    for entry in reference_dimensions:
        name = entry.get("name")
        value = entry.get("value")

        if not name or not value:
            continue

        # Direct index (lowercase for case-insensitive matching)
        direct_index[(name, value.lower())] = entry

        # Equivalence index (lowercase for case-insensitive matching)
        equivalences = entry.get("equivalence", {})
        for equiv_key, equiv_value in equivalences.items():
            if isinstance(equiv_value, str):
                equivalence_index[(name, equiv_value.lower())] = entry

    return {"direct": direct_index, "equivalence": equivalence_index}


def find_dimension_in_reference(
    name: str, value: str, reference_index: Dict
) -> Optional[Dict]:
    """
    # Find dimension in reference by exact match or equivalence lookup (case-insensitive)

    ## Arguments
    - `name` (str): Dimension name to search
    - `value` (str): Dimension value to search
    - `reference_index` (Dict): Pre-built reference indexes

    ## Returns
    - `Optional[Dict]`: Reference entry if found, None otherwise
    """
    if not reference_index:
        return None

    direct_index, equivalence_index = (
        reference_index["direct"],
        reference_index["equivalence"],
    )
    value_lower = value.lower()

    if (name, value_lower) in direct_index:
        return direct_index[(name, value_lower)]

    if (name, value_lower) in equivalence_index:
        return equivalence_index[(name, value_lower)]

    return None


def get_parent_value(entry: Dict) -> Optional[str]:
    """
    # Get parent value from reference entry using 'parents_values' field

    ## Arguments
    - `entry` (Dict): Reference entry with parents_values

    ## Returns
    - `Optional[str]`: Parent value if found, None otherwise
    """
    parents_values = entry.get("parents_values", {})
    return parents_values.get("default")


def build_complete_hierarchy_from_mapping(mapping: List[Dict]) -> List[Dict]:
    """
    # Build complete hierarchy by resolving parents and creating missing parents

    ## Arguments
    - `mapping` (List[Dict]): Dimensions mapping with parent relationships

    ## Returns
    - `List[Dict]`: Complete hierarchy with resolved parents and missing parents
    """
    complete_hierarchy = []
    processed_combinations = set()
    reference_dimensions = []
    reference_index = {}

    reference_path = Path("data/references/dimensions.json")
    if reference_path.exists():
        reference_dimensions = load_reference_dimensions_data(reference_path)
        reference_index = create_reference_indexes(reference_dimensions)

    for entry in mapping:
        name, value = entry["name"], entry["value"]
        combination = (name, value)

        if combination in processed_combinations:
            continue

        resolved_entry = resolve_parent_from_reference(entry, reference_index)
        complete_hierarchy.append(resolved_entry)
        processed_combinations.add(combination)

    missing_parents = find_and_create_missing_parents(
        complete_hierarchy, reference_index
    )
    for parent_entry in missing_parents:
        parent_combination = (parent_entry["name"], parent_entry["value"])
        if parent_combination not in processed_combinations:
            complete_hierarchy.append(parent_entry)
            processed_combinations.add(parent_combination)

    return complete_hierarchy


def resolve_parent_from_reference(mapping_entry: Dict, reference_index: Dict) -> Dict:
    """
    # Resolve parent hierarchy using reference_equivalence logic

    ## Arguments
    - `mapping_entry` (Dict): Entry from mapping file
    - `reference_index` (Dict): Reference lookup indexes

    ## Returns
    - `Dict`: Entry with resolved parent hierarchy
    """
    name = mapping_entry["name"]
    value = mapping_entry["value"]
    reference_equivalence = mapping_entry.get("reference_equivalence", {})
    parent_hierarchy = mapping_entry.get("parent_hierarchy", {})

    if "TODO" in reference_equivalence or "TODO" in parent_hierarchy:
        raise ValueError(f"Cannot build entry with TODO keys: {name}={value}")

    resolved_entry = {
        "name": name,
        "value": value,
        "reference_equivalence": reference_equivalence.copy(),
        "parent_hierarchy": parent_hierarchy.copy(),
    }

    if reference_equivalence:
        ref_value = (
            list(reference_equivalence.values())[0] if reference_equivalence else None
        )
        if ref_value:
            ref_entry = find_dimension_in_reference(name, ref_value, reference_index)
            if ref_entry:
                if not parent_hierarchy or not parent_hierarchy.get("default"):
                    ref_parent = get_parent_value(ref_entry)
                    if ref_parent:
                        resolved_entry["parent_hierarchy"] = {"default": ref_parent}

    if not resolved_entry["parent_hierarchy"].get("default"):
        resolved_entry["parent_hierarchy"]["default"] = "top-level"

    return resolved_entry


def find_and_create_missing_parents(
    hierarchy_entries: List[Dict], reference_index: Dict
) -> List[Dict]:
    """
    # Find and create missing parent entries recursively

    ## Arguments
    - `hierarchy_entries` (List[Dict]): Current hierarchy entries
    - `reference_index` (Dict): Reference lookup indexes

    ## Returns
    - `List[Dict]`: Missing parent entries to add
    """
    existing_values_by_name = {}
    missing_parents = []
    parents_to_process = []

    for entry in hierarchy_entries:
        name = entry["name"]
        value = entry["value"]
        if name not in existing_values_by_name:
            existing_values_by_name[name] = set()
        existing_values_by_name[name].add(value)

    for entry in hierarchy_entries:
        name = entry["name"]
        parent_value = entry.get("parent_hierarchy", {}).get("default")
        if parent_value and parent_value != "top-level":
            if (
                name not in existing_values_by_name
                or parent_value not in existing_values_by_name[name]
            ):
                parents_to_process.append((name, parent_value))

    while parents_to_process:
        name, parent_value = parents_to_process.pop(0)

        if (
            name in existing_values_by_name
            and parent_value in existing_values_by_name[name]
        ):
            continue

        parent_entry = create_parent_entry(name, parent_value, reference_index)
        missing_parents.append(parent_entry)

        if name not in existing_values_by_name:
            existing_values_by_name[name] = set()
        existing_values_by_name[name].add(parent_value)

        grandparent_value = parent_entry.get("parent_hierarchy", {}).get("default")
        if grandparent_value and grandparent_value != "top-level":
            if (
                name not in existing_values_by_name
                or grandparent_value not in existing_values_by_name[name]
            ):
                parents_to_process.append((name, grandparent_value))

    return missing_parents


def create_parent_entry(name: str, value: str, reference_index: Dict) -> Dict:
    """
    # Create parent entry, using reference if available

    ## Arguments
    - `name` (str): Dimension name
    - `value` (str): Dimension value
    - `reference_index` (Dict): Reference lookup indexes

    ## Returns
    - `Dict`: Parent entry with proper format
    """
    ref_entry = find_dimension_in_reference(name, value, reference_index)

    if ref_entry:
        ref_parent = get_parent_value(ref_entry)
        return {
            "name": name,
            "value": value,
            "reference_equivalence": ref_entry.get("equivalence", {}),
            "parent_hierarchy": {"default": ref_parent or "top-level"},
        }
    else:
        return {
            "name": name,
            "value": value,
            "reference_equivalence": {},
            "parent_hierarchy": {"default": "top-level"},
        }


def build_hierarchy_tree(entries: List[Dict]) -> Dict:
    """
    # Build tree structure from flat dimension entries

    ## Arguments
    - `entries` (List[Dict]): Dimension entries for same dimension name

    ## Returns
    - `Dict`: Tree structure with parent-child relationships
    """
    entries_by_value = {entry["value"]: entry for entry in entries}

    root_nodes = []
    for entry in entries:
        parent = get_parent_value_from_hierarchy(entry)
        if not parent or parent == "top-level":
            root_nodes.append(entry["value"])

    tree = {}
    for root in root_nodes:
        if root in entries_by_value:
            tree[root] = build_subtree(root, entries_by_value)

    return tree


def build_subtree(parent_value: str, entries_by_value: Dict) -> Dict:
    """
    # Recursively build subtree for a parent node

    ## Arguments
    - `parent_value` (str): Parent node value
    - `entries_by_value` (Dict): Lookup dictionary of all entries

    ## Returns
    - `Dict`: Subtree structure
    """
    subtree = {"entry": entries_by_value.get(parent_value, {}), "children": {}}

    for value, entry in entries_by_value.items():
        entry_parent = get_parent_value_from_hierarchy(entry)
        if entry_parent == parent_value:
            subtree["children"][value] = build_subtree(value, entries_by_value)

    return subtree


def get_parent_value_from_hierarchy(entry: Dict) -> Optional[str]:
    """
    # Get parent value from hierarchy entry using 'parent_hierarchy' field

    ## Arguments
    - `entry` (Dict): Dimension entry from hierarchy file

    ## Returns
    - `Optional[str]`: Parent value if found, None otherwise
    """
    parent_hierarchy = entry.get("parent_hierarchy", {})
    return parent_hierarchy.get("default")


def load_reference_dimensions_data(reference_path: Path) -> List[Dict]:
    """
    # Load reference dimensions from JSON file (internal utility)

    ## Arguments
    - `reference_path` (Path): Path to reference dimensions JSON file

    ## Returns
    - `List[Dict]`: Reference dimensions data
    """
    import json

    if not reference_path.exists():
        return []

    try:
        with open(reference_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            return []

        return data

    except json.JSONDecodeError:
        return []
