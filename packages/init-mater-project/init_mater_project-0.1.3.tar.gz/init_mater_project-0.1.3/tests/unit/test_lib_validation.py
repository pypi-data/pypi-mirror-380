"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

import pytest

from src.init_mater_project.src.lib.validation import (
    validate_mapping_completeness,
    count_mapping_statistics,
)


class TestValidateMappingCompleteness:
    """Test validate_mapping_completeness function"""

    def test_complete_mapping_validation(self, complete_mapping):
        """Test validation of complete mapping without TODOs"""
        result = validate_mapping_completeness(complete_mapping)

        assert result["total"] == 2
        assert result["mapped"] == 2
        assert result["todo"] == 0
        assert result["completion_rate"] == 100.0
        assert result["can_proceed"] is True
        assert len(result["todo_entries"]) == 0

    def test_incomplete_mapping_validation(self, incomplete_mapping):
        """Test validation of incomplete mapping with TODOs"""
        result = validate_mapping_completeness(incomplete_mapping)

        assert result["total"] == 2
        assert result["mapped"] == 1
        assert result["todo"] == 1
        assert result["completion_rate"] == 50.0
        assert result["can_proceed"] is False
        assert len(result["todo_entries"]) == 1

    def test_all_todo_mapping(self, all_todo_mapping):
        """Test validation when all entries have TODOs"""
        result = validate_mapping_completeness(all_todo_mapping)

        assert result["total"] == 2
        assert result["mapped"] == 0
        assert result["todo"] == 2
        assert result["completion_rate"] == 0.0
        assert result["can_proceed"] is False
        assert len(result["todo_entries"]) == 2

    def test_empty_mapping_validation(self):
        """Test validation of empty mapping"""
        result = validate_mapping_completeness([])

        assert result["total"] == 0
        assert result["mapped"] == 0
        assert result["todo"] == 0
        assert result["completion_rate"] == 0.0
        assert result["can_proceed"] is True
        assert len(result["todo_entries"]) == 0

    def test_todo_entries_identification(self, all_todo_mapping):
        """Test correct identification of TODO entries"""
        result = validate_mapping_completeness(all_todo_mapping)

        todo_entries = result["todo_entries"]
        assert len(todo_entries) == 2

        todo_values = [entry["value"] for entry in todo_entries]
        assert "france" in todo_values
        assert "car" in todo_values

    def test_reference_todo_detection(self, reference_todo_only_mapping):
        """Test detection of TODO in reference_equivalence"""
        result = validate_mapping_completeness(reference_todo_only_mapping)

        assert result["todo"] == 1
        assert result["can_proceed"] is False

    def test_parent_todo_detection(self, parent_todo_only_mapping):
        """Test detection of TODO in parent_hierarchy"""
        result = validate_mapping_completeness(parent_todo_only_mapping)

        assert result["todo"] == 1
        assert result["can_proceed"] is False


class TestCountMappingStatistics:
    """Test count_mapping_statistics function"""

    def test_accurate_counting_complete(self, complete_mapping):
        """Test accurate counting for complete mapping"""
        mapped, todo = count_mapping_statistics(complete_mapping)

        assert mapped == 2
        assert todo == 0

    def test_accurate_counting_incomplete(self, incomplete_mapping):
        """Test accurate counting for incomplete mapping"""
        mapped, todo = count_mapping_statistics(incomplete_mapping)

        assert mapped == 1
        assert todo == 1

    def test_all_mapped_counting(self, complete_mapping):
        """Test counting when all entries are mapped"""
        mapped, todo = count_mapping_statistics(complete_mapping)

        assert mapped == 2
        assert todo == 0

    def test_all_todo_counting(self, all_todo_mapping):
        """Test counting when all entries have TODOs"""
        mapped, todo = count_mapping_statistics(all_todo_mapping)

        assert mapped == 0
        assert todo == 2

    def test_empty_entries_counting(self, empty_entries_mapping):
        """Test counting entries without reference or parent data"""
        mapped, todo = count_mapping_statistics(empty_entries_mapping)

        assert mapped == 0
        assert todo == 0

    def test_mixed_mapping_counting(self, incomplete_mapping):
        """Test counting with mixed complete and TODO entries"""
        mapped, todo = count_mapping_statistics(incomplete_mapping)

        assert mapped == 1
        assert todo == 1

    def test_reference_todo_only_counting(self, reference_todo_only_mapping):
        """Test counting entries with TODO only in reference_equivalence"""
        mapped, todo = count_mapping_statistics(reference_todo_only_mapping)

        assert mapped == 0
        assert todo == 1

    def test_parent_todo_only_counting(self, parent_todo_only_mapping):
        """Test counting entries with TODO only in parent_hierarchy"""
        mapped, todo = count_mapping_statistics(parent_todo_only_mapping)

        assert mapped == 0
        assert todo == 1

    @pytest.mark.parametrize(
        "has_ref_todo,has_parent_todo,expected_mapped,expected_todo",
        [
            (False, False, 1, 0),
            (True, False, 0, 1),
            (False, True, 0, 1),
            (True, True, 0, 1),
        ],
    )
    def test_todo_combinations(
        self, has_ref_todo, has_parent_todo, expected_mapped, expected_todo
    ):
        """Test different combinations of TODO presence"""
        ref_equiv = {"TODO": "check"} if has_ref_todo else {"iso_alpha2": "FR"}
        parent_hier = {"TODO": ["check"]} if has_parent_todo else {"default": "world"}

        mapping = [
            {
                "name": "location",
                "value": "france",
                "reference_equivalence": ref_equiv,
                "parent_hierarchy": parent_hier,
            }
        ]

        mapped, todo = count_mapping_statistics(mapping)

        assert mapped == expected_mapped
        assert todo == expected_todo

    def test_empty_mapping_counting(self):
        """Test counting with empty mapping"""
        mapped, todo = count_mapping_statistics([])

        assert mapped == 0
        assert todo == 0
