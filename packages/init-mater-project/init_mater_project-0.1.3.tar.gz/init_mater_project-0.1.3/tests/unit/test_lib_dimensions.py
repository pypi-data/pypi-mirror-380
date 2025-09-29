"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

import pytest
from unittest.mock import patch, mock_open
import json
from pathlib import Path

from src.init_mater_project.src.lib.dimensions import (
    create_dimensions_mapping,
    resolve_single_mapping_entry,
    create_reference_indexes,
    find_dimension_in_reference,
    build_complete_hierarchy_from_mapping,
    resolve_parent_from_reference,
    find_and_create_missing_parents,
    create_parent_entry,
    build_hierarchy_tree,
    build_subtree,
    get_parent_value,
    get_parent_value_from_hierarchy,
    load_reference_dimensions_data,
)


class TestCreateDimensionsMapping:
    """Test create_dimensions_mapping function"""

    def test_successful_mapping_with_matches(
        self, sample_input_dimensions, sample_reference_dimensions
    ):
        """Test successful mapping when references are found"""
        result = create_dimensions_mapping(
            sample_input_dimensions, sample_reference_dimensions
        )

        assert len(result) == 2
        france_entry = next(entry for entry in result if entry["value"] == "france")
        assert france_entry["reference_equivalence"] == {"iso_alpha2": "FR"}
        assert france_entry["parent_hierarchy"]["default"] == "world"

    def test_mapping_with_empty_reference(self, sample_input_dimensions):
        """Test mapping when no reference data available"""
        result = create_dimensions_mapping(sample_input_dimensions, [])

        assert len(result) == 2
        for entry in result:
            assert "TODO" in entry["reference_equivalence"]
            assert "TODO" in entry["parent_hierarchy"]

    def test_partial_matches(
        self, sample_input_dimensions, sample_reference_dimensions
    ):
        """Test mapping with partial matches - some found, some not"""
        partial_reference = [sample_reference_dimensions[0]]
        result = create_dimensions_mapping(sample_input_dimensions, partial_reference)

        assert len(result) == 2
        matched_entries = [
            e for e in result if "TODO" not in e["reference_equivalence"]
        ]
        todo_entries = [e for e in result if "TODO" in e["reference_equivalence"]]

        assert len(matched_entries) == 1
        assert len(todo_entries) == 1

    def test_empty_source_dimensions(self, sample_reference_dimensions):
        """Test mapping with empty source dimensions"""
        result = create_dimensions_mapping([], sample_reference_dimensions)

        assert result == []


class TestResolveSingleMappingEntry:
    """Test resolve_single_mapping_entry function"""

    def test_complete_resolution(
        self, sample_reference_dimensions, sample_input_dimensions
    ):
        """Test complete resolution with reference and valid parent"""
        sample_reference_index = create_reference_indexes(sample_reference_dimensions)
        entry = {
            "name": "location",
            "value": "france",
            "reference_equivalence": {"iso_alpha2": "FR"},
            "parent_hierarchy": {"default": "world"},
        }

        resolved, errors, auto_resolved = resolve_single_mapping_entry(
            entry, sample_reference_index, sample_input_dimensions
        )

        assert errors == []
        assert not auto_resolved
        assert resolved["parent_hierarchy"]["default"] == "world"

    def test_auto_resolution_from_reference(
        self, sample_reference_dimensions, sample_input_dimensions
    ):
        """Test parent auto-resolution from reference"""
        sample_reference_index = create_reference_indexes(sample_reference_dimensions)
        entry = {
            "name": "location",
            "value": "france",
            "reference_equivalence": {"iso_alpha2": "FR"},
            "parent_hierarchy": {},
        }

        resolved, errors, auto_resolved = resolve_single_mapping_entry(
            entry, sample_reference_index, sample_input_dimensions
        )

        assert errors == []
        assert auto_resolved
        assert resolved["parent_hierarchy"]["default"] == "world"

    def test_todo_entries_error(
        self, sample_reference_dimensions, sample_input_dimensions
    ):
        """Test entries with TODO keys generate errors"""
        sample_reference_index = create_reference_indexes(sample_reference_dimensions)
        entry = {
            "name": "location",
            "value": "france",
            "reference_equivalence": {"TODO": "check reference"},
            "parent_hierarchy": {"default": "world"},
        }

        resolved, errors, auto_resolved = resolve_single_mapping_entry(
            entry, sample_reference_index, sample_input_dimensions
        )

        assert len(errors) == 1
        assert "TODO keys" in errors[0]
        assert not auto_resolved

    def test_invalid_parent_error(self, sample_reference_dimensions):
        """Test invalid parent generates error"""
        sample_reference_index = create_reference_indexes(sample_reference_dimensions)
        entry = {
            "name": "location",
            "value": "france",
            "reference_equivalence": {},
            "parent_hierarchy": {"default": "invalid_parent"},
        }

        resolved, errors, auto_resolved = resolve_single_mapping_entry(
            entry, sample_reference_index, []
        )

        assert len(errors) == 1
        assert "parent 'invalid_parent' not found" in errors[0]

    def test_multiple_hierarchy_keys_error(
        self, sample_reference_dimensions, sample_input_dimensions
    ):
        """Test multiple hierarchy keys generate error"""
        sample_reference_index = create_reference_indexes(sample_reference_dimensions)
        entry = {
            "name": "location",
            "value": "france",
            "reference_equivalence": {},
            "parent_hierarchy": {"default": "world", "other": "top-level"},
        }

        resolved, errors, auto_resolved = resolve_single_mapping_entry(
            entry, sample_reference_index, sample_input_dimensions
        )

        assert len(errors) == 1
        assert "must contain only one value" in errors[0]


class TestCreateReferenceIndexes:
    """Test create_reference_indexes function"""

    def test_complete_indexing(self, sample_reference_dimensions):
        """Test complete indexing with direct and equivalence entries"""
        result = create_reference_indexes(sample_reference_dimensions)

        assert "direct" in result
        assert "equivalence" in result

        assert ("location", "france") in result["direct"]
        assert ("location", "FRANCE") not in result["direct"]
        assert ("location", "fr") in result["equivalence"]

    def test_empty_reference(self):
        """Test indexing with empty reference"""
        result = create_reference_indexes([])

        assert result["direct"] == {}
        assert result["equivalence"] == {}

    def test_case_insensitive_indexing(self):
        """Test case-insensitive indexing"""
        reference = [
            {"name": "location", "value": "FRANCE", "equivalence": {"iso": "FR"}}
        ]

        result = create_reference_indexes(reference)

        assert ("location", "france") in result["direct"]
        assert ("location", "fr") in result["equivalence"]

    def test_malformed_entries_skipped(self):
        """Test malformed entries are skipped"""
        reference = [
            {"name": "location"},
            {"value": "france"},
            {"name": "location", "value": "france"},
        ]

        result = create_reference_indexes(reference)

        assert len(result["direct"]) == 1
        assert ("location", "france") in result["direct"]


class TestFindDimensionInReference:
    """Test find_dimension_in_reference function"""

    def test_direct_match_found(self, sample_reference_dimensions):
        """Test direct match is found"""
        sample_reference_index = create_reference_indexes(sample_reference_dimensions)
        result = find_dimension_in_reference(
            "location", "france", sample_reference_index
        )

        assert result is not None
        assert result["value"] == "france"

    def test_equivalence_match_found(self, sample_reference_dimensions):
        """Test equivalence match is found"""
        sample_reference_index = create_reference_indexes(sample_reference_dimensions)
        result = find_dimension_in_reference("location", "FR", sample_reference_index)

        assert result is not None
        assert result["value"] == "france"

    def test_case_insensitive_matching(self, sample_reference_dimensions):
        """Test case-insensitive matching works"""
        sample_reference_index = create_reference_indexes(sample_reference_dimensions)
        result = find_dimension_in_reference(
            "location", "FRANCE", sample_reference_index
        )

        assert result is not None
        assert result["value"] == "france"

    def test_not_found(self, sample_reference_dimensions):
        """Test dimension not found"""
        sample_reference_index = create_reference_indexes(sample_reference_dimensions)
        result = find_dimension_in_reference(
            "location", "unknown", sample_reference_index
        )

        assert result is None

    def test_empty_index(self):
        """Test search with empty index"""
        empty_index = {"direct": {}, "equivalence": {}}
        result = find_dimension_in_reference("location", "france", empty_index)

        assert result is None


class TestBuildCompleteHierarchyFromMapping:
    """Test build_complete_hierarchy_from_mapping function"""

    @patch("src.init_mater_project.src.lib.dimensions.load_reference_dimensions_data")
    @patch("pathlib.Path.exists")
    def test_complete_hierarchy_with_missing_parents(
        self, mock_exists, mock_load_ref, complete_mapping
    ):
        """Test complete hierarchy creation with missing parents"""
        mock_exists.return_value = True
        mock_load_ref.return_value = []

        result = build_complete_hierarchy_from_mapping(complete_mapping)

        assert len(result) >= len(complete_mapping)

        parent_values = [entry["value"] for entry in result]
        assert "world" in parent_values

    @patch("src.init_mater_project.src.lib.dimensions.load_reference_dimensions_data")
    @patch("pathlib.Path.exists")
    def test_hierarchy_without_reference(
        self, mock_exists, mock_load_ref, complete_mapping
    ):
        """Test hierarchy creation without reference file"""
        mock_exists.return_value = False

        result = build_complete_hierarchy_from_mapping(complete_mapping)

        assert len(result) >= len(complete_mapping)

    def test_todo_entries_raise_error(self, incomplete_mapping):
        """Test entries with TODO keys raise error"""
        with pytest.raises(ValueError, match="Cannot build entry with TODO keys"):
            build_complete_hierarchy_from_mapping(incomplete_mapping)


class TestResolveParentFromReference:
    """Test resolve_parent_from_reference function"""

    def test_use_reference_parent_when_empty(
        self, sample_reference_dimensions, mapping_with_empty_parent
    ):
        """Test using reference parent when parent_hierarchy is empty"""
        sample_reference_index = create_reference_indexes(sample_reference_dimensions)

        result = resolve_parent_from_reference(
            mapping_with_empty_parent, sample_reference_index
        )

        assert result["parent_hierarchy"]["default"] == "world"

    def test_keep_provided_parent_override(
        self, sample_reference_dimensions, mapping_with_custom_parent
    ):
        """Test keeping provided parent when user overrides"""
        sample_reference_index = create_reference_indexes(sample_reference_dimensions)

        result = resolve_parent_from_reference(
            mapping_with_custom_parent, sample_reference_index
        )

        assert result["parent_hierarchy"]["default"] == "custom_parent"

    def test_default_to_top_level_when_no_parent(
        self, sample_reference_dimensions, mapping_completely_empty
    ):
        """Test defaulting to top-level when no parent available"""
        sample_reference_index = create_reference_indexes(sample_reference_dimensions)

        result = resolve_parent_from_reference(
            mapping_completely_empty, sample_reference_index
        )

        assert result["parent_hierarchy"]["default"] == "top-level"

    def test_todo_entries_raise_error(self, incomplete_mapping):
        """Test entries with TODO keys raise error"""
        mapping_entry = incomplete_mapping[1]

        with pytest.raises(ValueError, match="Cannot build entry with TODO keys"):
            resolve_parent_from_reference(mapping_entry, {})


class TestFindAndCreateMissingParents:
    """Test find_and_create_missing_parents function"""

    def test_create_single_missing_parent(
        self, sample_reference_dimensions, complete_mapping
    ):
        """Test creating single missing parent"""
        sample_reference_index = create_reference_indexes(sample_reference_dimensions)
        hierarchy_entries = [complete_mapping[0]]

        result = find_and_create_missing_parents(
            hierarchy_entries, sample_reference_index
        )

        assert len(result) == 1
        assert result[0]["value"] == "world"

    def test_create_cascading_missing_parents(self, cascading_hierarchy_entries):
        """Test creating parents recursively"""
        result = find_and_create_missing_parents(cascading_hierarchy_entries, {})

        assert len(result) >= 1
        europe_entry = next(entry for entry in result if entry["value"] == "europe")
        assert europe_entry["parent_hierarchy"]["default"] == "top-level"

    def test_no_missing_parents(self):
        """Test when no parents are missing"""
        hierarchy_entries = [
            {
                "name": "location",
                "value": "world",
                "reference_equivalence": {},
                "parent_hierarchy": {"default": "top-level"},
            }
        ]

        result = find_and_create_missing_parents(hierarchy_entries, {})

        assert result == []


class TestCreateParentEntry:
    """Test create_parent_entry function"""

    def test_create_from_reference(self, sample_reference_dimensions):
        """Test creating parent entry from reference data"""
        sample_reference_index = create_reference_indexes(sample_reference_dimensions)

        result = create_parent_entry("location", "world", sample_reference_index)

        assert result["name"] == "location"
        assert result["value"] == "world"
        assert result["reference_equivalence"] == {}
        assert result["parent_hierarchy"]["default"] == "top-level"

    def test_create_basic_parent(self):
        """Test creating basic parent entry when no reference"""
        result = create_parent_entry("location", "unknown", {})

        assert result["name"] == "location"
        assert result["value"] == "unknown"
        assert result["reference_equivalence"] == {}
        assert result["parent_hierarchy"]["default"] == "top-level"


class TestBuildHierarchyTree:
    """Test build_hierarchy_tree function"""

    def test_simple_tree_structure(self, simple_hierarchy_entries):
        """Test building simple tree structure"""
        result = build_hierarchy_tree(simple_hierarchy_entries)

        assert "world" in result
        assert "children" in result["world"]
        assert "france" in result["world"]["children"]

    def test_multilevel_hierarchy(self, multilevel_hierarchy_entries):
        """Test deep hierarchy tree"""
        result = build_hierarchy_tree(multilevel_hierarchy_entries)

        assert "world" in result
        assert "vehicule" in result

        world_children = result["world"]["children"]
        assert "france" in world_children

        vehicule_children = result["vehicule"]["children"]
        assert "car" in vehicule_children

    def test_multiple_roots(self, multiple_roots_entries):
        """Test multiple top-level entries"""
        result = build_hierarchy_tree(multiple_roots_entries)

        assert len(result) == 2
        assert "world" in result
        assert "other_root" in result

    def test_empty_entries(self):
        """Test empty entries list"""
        result = build_hierarchy_tree([])

        assert result == {}


class TestBuildSubtree:
    """Test build_subtree function"""

    def test_build_subtree_with_children(self, subtree_entries_with_children):
        """Test building subtree with children"""
        result = build_subtree("world", subtree_entries_with_children)

        assert "entry" in result
        assert "children" in result
        assert "france" in result["children"]

    def test_build_subtree_no_children(self, subtree_entries_no_children):
        """Test building subtree with no children"""
        result = build_subtree("france", subtree_entries_no_children)

        assert "entry" in result
        assert "children" in result
        assert len(result["children"]) == 0

    def test_build_nested_subtree(self, nested_subtree_entries):
        """Test building nested subtree recursively"""
        result = build_subtree("world", nested_subtree_entries)

        assert "france" in result["children"]
        france_subtree = result["children"]["france"]
        assert "paris" in france_subtree["children"]


class TestUtilityFunctions:
    """Test utility functions"""

    def test_get_parent_value_success(self):
        """Test getting parent value from reference entry"""
        entry = {"parents_values": {"default": "world"}}
        result = get_parent_value(entry)
        assert result == "world"

    def test_get_parent_value_missing(self):
        """Test getting parent value when missing"""
        entry = {"parents_values": {}}
        result = get_parent_value(entry)
        assert result is None

    def test_get_parent_value_from_hierarchy_success(self):
        """Test getting parent value from hierarchy entry"""
        entry = {"parent_hierarchy": {"default": "world"}}
        result = get_parent_value_from_hierarchy(entry)
        assert result == "world"

    def test_get_parent_value_from_hierarchy_missing(self):
        """Test getting parent value from hierarchy when missing"""
        entry = {"parent_hierarchy": {}}
        result = get_parent_value_from_hierarchy(entry)
        assert result is None


class TestLoadReferenceDimensionsData:
    """Test load_reference_dimensions_data function"""

    def test_successful_load(self):
        """Test successful loading of reference data"""
        test_data = [{"name": "location", "value": "france"}]
        mock_file_content = json.dumps(test_data)

        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("builtins.open", mock_open(read_data=mock_file_content)),
        ):
            result = load_reference_dimensions_data(Path("test.json"))

        assert result == test_data

    def test_file_not_exists(self):
        """Test loading when file doesn't exist"""
        with patch("pathlib.Path.exists", return_value=False):
            result = load_reference_dimensions_data(Path("nonexistent.json"))

        assert result == []

    def test_invalid_json(self):
        """Test loading with invalid JSON"""
        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("builtins.open", mock_open(read_data="invalid json")),
        ):
            result = load_reference_dimensions_data(Path("test.json"))

        assert result == []

    def test_non_list_data(self):
        """Test loading when data is not a list"""
        mock_file_content = json.dumps({"not": "a list"})

        with (
            patch("pathlib.Path.exists", return_value=True),
            patch("builtins.open", mock_open(read_data=mock_file_content)),
        ):
            result = load_reference_dimensions_data(Path("test.json"))

        assert result == []
