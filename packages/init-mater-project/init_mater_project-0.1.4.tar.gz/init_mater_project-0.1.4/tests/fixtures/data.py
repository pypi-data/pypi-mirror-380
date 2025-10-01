"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

import pytest


@pytest.fixture
def sample_input_data():
    """Sample input data"""
    return {
        "input_data": [
            {
                "time": 2000,
                "value": 100,
                "variable": "stock",
                "dimensions_values": {"location": "france", "object": "car"},
            }
        ],
        "provider": {
            "first_name": "Test",
            "last_name": "User",
            "email_address": "test.user@example.com",
        },
        "metadata": {
            "source": "Test Dataset Source",
            "link": "https://example.com/dataset",
            "project": "Test Project",
        },
    }


@pytest.fixture
def sample_input_data_multiple():
    """Sample input data with multiple entries"""
    return {
        "input_data": [
            {
                "time": 2000,
                "value": 100,
                "variable": "stock",
                "dimensions_values": {"location": "france", "object": "car"},
            },
            {
                "time": 2015,
                "value": 200,
                "variable": "stock",
                "dimensions_values": {"location": "france", "object": "car"},
            },
        ],
        "provider": {
            "first_name": "Test",
            "last_name": "User",
            "email_address": "test.user@example.com",
        },
        "metadata": {
            "source": "Test Dataset Source",
            "link": "https://example.com/dataset",
            "project": "Test Project",
        },
    }


@pytest.fixture
def sample_variables_dimensions():
    """Sample variables-dimensions"""
    return [
        {"variable": "stock", "dimension": "location", "property": "extensive"},
        {"variable": "stock", "dimension": "object", "property": "extensive"},
    ]


@pytest.fixture
def sample_input_dimensions():
    """Input data dimensions"""
    return [{"name": "location", "value": "france"}, {"name": "object", "value": "car"}]


@pytest.fixture
def sample_reference_dimensions():
    """Reference dimensions"""
    return [
        {
            "name": "location",
            "value": "france",
            "equivalence": {"iso_alpha2": "FR"},
            "parents_values": {"default": "world"},
        },
        {
            "name": "location",
            "value": "world",
            "equivalence": {},
            "parents_values": {"default": "top-level"},
        },
        {
            "name": "object",
            "value": "car",
            "equivalence": {"auto": "auto"},
            "parents_values": {"default": "vehicule"},
        },
        {
            "name": "object",
            "value": "vehicule",
            "equivalence": {},
            "parents_values": {"default": "top-level"},
        },
    ]


@pytest.fixture
def complete_mapping():
    """Complete mapping without TODOs"""
    return [
        {
            "name": "location",
            "value": "france",
            "reference_equivalence": {"iso_alpha2": "FR"},
            "parent_hierarchy": {"default": "world"},
        },
        {
            "name": "object",
            "value": "car",
            "reference_equivalence": {"auto": "auto"},
            "parent_hierarchy": {"default": "vehicule"},
        },
    ]


@pytest.fixture
def incomplete_mapping():
    """Mapping with some TODOs"""
    return [
        {
            "name": "location",
            "value": "france",
            "reference_equivalence": {"iso_alpha2": "FR"},
            "parent_hierarchy": {"default": "world"},
        },
        {
            "name": "object",
            "value": "car",
            "reference_equivalence": {"TODO": "check reference"},
            "parent_hierarchy": {"default": "vehicule"},
        },
    ]


@pytest.fixture
def all_todo_mapping():
    """Mapping where all entries have TODOs"""
    return [
        {
            "name": "location",
            "value": "france",
            "reference_equivalence": {"TODO": "check reference"},
            "parent_hierarchy": {"default": "world"},
        },
        {
            "name": "object",
            "value": "car",
            "reference_equivalence": {"auto": "auto"},
            "parent_hierarchy": {"TODO": ["check parent"]},
        },
    ]


@pytest.fixture
def empty_entries_mapping():
    """Mapping with empty reference and parent data"""
    return [
        {
            "name": "location",
            "value": "unknown",
            "reference_equivalence": {},
            "parent_hierarchy": {},
        },
        {
            "name": "object",
            "value": "mystery",
            "reference_equivalence": {},
            "parent_hierarchy": {},
        },
    ]


@pytest.fixture
def mapping_with_empty_parent():
    """Mapping with empty parent_hierarchy"""
    return {
        "name": "location",
        "value": "france",
        "reference_equivalence": {"iso_alpha2": "FR"},
        "parent_hierarchy": {},
    }


@pytest.fixture
def mapping_with_custom_parent():
    """Mapping with custom parent override"""
    return {
        "name": "location",
        "value": "france",
        "reference_equivalence": {"iso_alpha2": "FR"},
        "parent_hierarchy": {"default": "custom_parent"},
    }


@pytest.fixture
def mapping_completely_empty():
    """Mapping with empty reference_equivalence and parent_hierarchy"""
    return {
        "name": "location",
        "value": "france",
        "reference_equivalence": {},
        "parent_hierarchy": {},
    }


@pytest.fixture
def reference_todo_only_mapping():
    """Mapping with TODO only in reference_equivalence"""
    return [
        {
            "name": "location",
            "value": "france",
            "reference_equivalence": {"TODO": "check reference"},
            "parent_hierarchy": {"default": "world"},
        }
    ]


@pytest.fixture
def parent_todo_only_mapping():
    """Mapping with TODO only in parent_hierarchy"""
    return [
        {
            "name": "location",
            "value": "france",
            "reference_equivalence": {"iso_alpha2": "FR"},
            "parent_hierarchy": {"TODO": ["check parent"]},
        }
    ]


@pytest.fixture
def simple_hierarchy_entries():
    """Simple hierarchy for tree building"""
    return [
        {
            "name": "location",
            "value": "world",
            "parent_hierarchy": {"default": "top-level"},
        },
        {
            "name": "location",
            "value": "france",
            "parent_hierarchy": {"default": "world"},
        },
    ]


@pytest.fixture
def multilevel_hierarchy_entries():
    """Multi-level hierarchy"""
    return [
        {
            "name": "location",
            "value": "world",
            "parent_hierarchy": {"default": "top-level"},
        },
        {
            "name": "location",
            "value": "france",
            "parent_hierarchy": {"default": "world"},
        },
        {
            "name": "object",
            "value": "vehicule",
            "parent_hierarchy": {"default": "top-level"},
        },
        {"name": "object", "value": "car", "parent_hierarchy": {"default": "vehicule"}},
    ]


@pytest.fixture
def multiple_roots_entries():
    """Hierarchy entries with multiple top-level roots"""
    return [
        {
            "name": "location",
            "value": "world",
            "parent_hierarchy": {"default": "top-level"},
        },
        {
            "name": "location",
            "value": "other_root",
            "parent_hierarchy": {"default": "top-level"},
        },
    ]


@pytest.fixture
def cascading_hierarchy_entries():
    """Hierarchy entries requiring cascading parent creation"""
    return [
        {
            "name": "location",
            "value": "france",
            "reference_equivalence": {},
            "parent_hierarchy": {"default": "europe"},
        }
    ]


@pytest.fixture
def subtree_entries_with_children():
    """Entries structure for testing subtree with children"""
    return {
        "world": {
            "name": "location",
            "value": "world",
            "parent_hierarchy": {"default": "top-level"},
        },
        "france": {
            "name": "location",
            "value": "france",
            "parent_hierarchy": {"default": "world"},
        },
    }


@pytest.fixture
def subtree_entries_no_children():
    """Entries structure for testing subtree with no children"""
    return {
        "france": {
            "name": "location",
            "value": "france",
            "parent_hierarchy": {"default": "world"},
        }
    }


@pytest.fixture
def nested_subtree_entries():
    """Entries structure for testing deep nested subtree"""
    return {
        "world": {
            "name": "location",
            "value": "world",
            "parent_hierarchy": {"default": "top-level"},
        },
        "france": {
            "name": "location",
            "value": "france",
            "parent_hierarchy": {"default": "world"},
        },
        "paris": {
            "name": "location",
            "value": "paris",
            "parent_hierarchy": {"default": "france"},
        },
    }


@pytest.fixture
def sample_csv_data():
    """Sample CSV data for transformation testing"""
    return """year,location,object,value,unit
2000,france,car,100,number
2010,france,car,150,number
2020,france,car,200,number"""


@pytest.fixture
def malformed_json():
    """Malformed JSON string"""
    return "{ invalid json"


@pytest.fixture
def missing_input_data_json():
    """JSON missing input_data section"""
    return {
        "provider": {
            "first_name": "Test",
            "last_name": "User",
            "email_address": "test.user@example.com",
        },
        "metadata": {
            "source": "Test Dataset Source",
            "link": "https://example.com/dataset",
            "project": "Test Project",
        },
    }


@pytest.fixture
def input_data_not_list_json():
    """JSON with input_data as dict instead of list"""
    return {
        "input_data": {"not": "a list"},
        "provider": {
            "first_name": "Test",
            "last_name": "User",
            "email_address": "test.user@example.com",
        },
        "metadata": {
            "source": "Test Dataset Source",
            "link": "https://example.com/dataset",
            "project": "Test Project",
        },
    }


@pytest.fixture
def not_array_json():
    """JSON that is not an array"""
    return {"not": "an array"}


@pytest.fixture
def empty_json():
    """Empty JSON object"""
    return {}
