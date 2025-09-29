"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

from tests.fixtures.config import (
    mock_config,
    mock_config_example,
    mock_config_custom_paths,
)

from tests.fixtures.data import (
    sample_input_data,
    sample_input_data_multiple,
    sample_variables_dimensions,
    sample_input_dimensions,
    sample_reference_dimensions,
    complete_mapping,
    incomplete_mapping,
    all_todo_mapping,
    empty_entries_mapping,
    mapping_with_empty_parent,
    mapping_with_custom_parent,
    mapping_completely_empty,
    reference_todo_only_mapping,
    parent_todo_only_mapping,
    simple_hierarchy_entries,
    multilevel_hierarchy_entries,
    multiple_roots_entries,
    cascading_hierarchy_entries,
    subtree_entries_with_children,
    subtree_entries_no_children,
    nested_subtree_entries,
    sample_csv_data,
    malformed_json,
    missing_input_data_json,
    input_data_not_list_json,
    not_array_json,
    empty_json,
)
