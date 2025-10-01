"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

import pytest
from pathlib import Path
from unittest.mock import Mock


@pytest.fixture
def mock_config():
    """Mock MaterConfig for testing commands"""
    config = Mock()

    config.paths.input_path = Path("data/input")
    config.paths.dimensions_hierarchy_file = Path(
        "data/dimensions_hierarchy/dimensions_hierarchy.json"
    )
    config.paths.variables_dimensions_path = Path(
        "data/references/variables_dimensions.json"
    )
    config.paths.raw_path = Path("data/raw")
    config.paths.transforms_script_path = Path("transforms/datasets")
    config.paths.dimensions_mapping_file = Path(
        "data/dimensions_hierarchy/dimensions_mapping.json"
    )
    config.paths.dimensions_values_path = Path("data/references/dimensions.json")
    config.paths.output_folder = Path("outputs")

    config.simulation.name = "test_simulation"
    config.simulation.start_time = 1900
    config.simulation.end_time = 2100
    config.simulation.frequency = "YS"
    config.simulation.scenario = "historical"

    config.output_path = Path("outputs/test_simulation")

    config.provider_info = {
        "first_name": "Test",
        "last_name": "User",
        "email_address": "test.user@example.com",
    }

    config.metadata_info = {
        "source": "Test Dataset Source",
        "link": "https://example.com/dataset",
        "project": "Test Project",
    }

    return config


@pytest.fixture
def mock_config_example():
    """Mock MaterConfig with example settings for testing"""
    config = Mock()

    config.paths.input_path = Path("examples/minimal_example.json")
    config.paths.dimensions_hierarchy_file = Path(
        "examples/minimal_dimensions_hierarchy.json"
    )
    config.paths.variables_dimensions_path = Path(
        "examples/minimal_variables_dimensions.json"
    )
    config.paths.raw_path = Path("examples/minimal_raw_example.csv")
    config.paths.transforms_script_path = Path("examples")
    config.paths.dimensions_mapping_file = Path(
        "examples/minimal_dimensions_mapping.json"
    )
    config.paths.dimensions_values_path = Path("examples/minimal_dimensions.json")
    config.paths.output_folder = Path("examples")

    config.simulation.name = "example_outputs"
    config.simulation.start_time = 1900
    config.simulation.end_time = 2100
    config.simulation.frequency = "YS"
    config.simulation.scenario = "example"

    config.output_path = Path("examples/example_outputs")

    config.provider_info = {
        "first_name": "Lauranne",
        "last_name": "Sarribouette",
        "email_address": "lauranne.sarribouette@univ-grenoble-alpes.fr",
    }

    config.metadata_info = {
        "source": "Example Dataset Source",
        "link": "https://example.org/dataset",
        "project": "Example MATER Project",
    }

    return config


@pytest.fixture
def mock_config_custom_paths():
    """Mock MaterConfig with custom paths for testing path overrides"""
    config = Mock()

    config.paths.input_path = Path("custom/input")
    config.paths.dimensions_hierarchy_file = Path("custom/dimensions_hierarchy.json")
    config.paths.variables_dimensions_path = Path("custom/variables_dimensions.json")
    config.paths.raw_path = Path("custom/raw")
    config.paths.transforms_script_path = Path("custom/transforms")
    config.paths.dimensions_mapping_file = Path("custom/dimensions_mapping.json")
    config.paths.dimensions_values_path = Path("custom/dimensions.json")
    config.paths.output_folder = Path("custom/outputs")

    config.simulation.name = "custom_simulation"
    config.simulation.start_time = 2000
    config.simulation.end_time = 2050
    config.simulation.frequency = "MS"
    config.simulation.scenario = "custom"

    config.output_path = Path("custom/outputs/custom_simulation")

    return config
