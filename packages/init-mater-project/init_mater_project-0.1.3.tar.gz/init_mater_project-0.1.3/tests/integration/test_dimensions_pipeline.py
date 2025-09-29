"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

import json
import subprocess
from pathlib import Path

from click.testing import CliRunner

from src.init_mater_project.main import main


def test_dimensions_map_to_build_pipeline_full_workflow(tmp_path):
    """Test complete dimensions workflow: generate project → input data → map → build hierarchy"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["dimensions-test"])
        assert result_init.exit_code == 0
        assert "✅ MATER project 'dimensions-test' initialized!" in result_init.output

        project_dir = Path("dimensions-test").resolve()

        # Step 2: Setup input data (copy minimal example from generated project)
        src_input = project_dir / "examples" / "minimal_example.json"
        dst_input = project_dir / "data" / "input" / "minimal_example.json"
        dst_input.write_text(src_input.read_text())

        # Step 3: Map dimensions
        result_map = subprocess.run(
            ["uv", "run", "mater-cli", "dimensions", "map"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_map.returncode == 0
        assert "Generated dimensions mapping" in result_map.stdout

        # Verify mapping file was created
        mapping_file = (
            project_dir / "data" / "dimensions_hierarchy" / "dimensions_mapping.json"
        )
        assert mapping_file.exists()

        # Step 4: Check mapping content and simulate user editing (remove TODOs)
        mapping_data = json.loads(mapping_file.read_text())
        assert len(mapping_data) > 0

        # Simulate user completing TODOs by copying complete mapping from examples
        src_complete_mapping = (
            project_dir / "examples" / "minimal_dimensions_hierarchy.json"
        )
        if src_complete_mapping.exists():
            mapping_file.write_text(src_complete_mapping.read_text())

        # Step 5: Build dimensions hierarchy
        result_build = subprocess.run(
            ["uv", "run", "mater-cli", "dimensions", "build"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_build.returncode == 0
        assert "Generated dimensions hierarchy" in result_build.stdout

        # Step 6: Verify hierarchy file was created
        hierarchy_file = (
            project_dir / "data" / "dimensions_hierarchy" / "dimensions_hierarchy.json"
        )
        assert hierarchy_file.exists()

        # Validate hierarchy structure
        hierarchy_data = json.loads(hierarchy_file.read_text())
        assert len(hierarchy_data) > 0

        for entry in hierarchy_data:
            assert "name" in entry
            assert "value" in entry
            assert "reference_equivalence" in entry
            assert "parent_hierarchy" in entry


def test_dimensions_pipeline_with_example_workflow(tmp_path):
    """Test dimensions pipeline using --example flag in generated project"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["dimensions-example-project"])
        assert result_init.exit_code == 0

        project_dir = Path("dimensions-example-project").resolve()

        # Step 2: Test dimensions map with example data
        result_map = subprocess.run(
            ["uv", "run", "mater-cli", "dimensions", "map", "--example"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_map.returncode == 0
        assert "Example data" in result_map.stdout

        # Step 3: Test dimensions build with example data
        result_build = subprocess.run(
            ["uv", "run", "mater-cli", "dimensions", "build", "--example"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_build.returncode == 0
        assert "Example data" in result_build.stdout


def test_dimensions_incremental_workflow(tmp_path):
    """Test dimensions incremental mapping workflow"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["incremental-test"])
        assert result_init.exit_code == 0

        project_dir = Path("incremental-test").resolve()

        # Step 2: Setup initial input data
        src_input = project_dir / "examples" / "minimal_example.json"
        dst_input = project_dir / "data" / "input" / "minimal_example.json"
        dst_input.write_text(src_input.read_text())

        # Step 3: Create initial mapping
        result_map_initial = subprocess.run(
            ["uv", "run", "mater-cli", "dimensions", "map"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_map_initial.returncode == 0

        # Step 4: Add more input data (simulate new data)
        additional_data = {
            "input_data": [
                {
                    "time": 2020,
                    "value": 5000,
                    "scenario": "historical",
                    "unit": "number of objects",
                    "variable": "exogenous_stock",
                    "dimensions_values": {"location": "france", "object": "truck"},
                }
            ],
            "provider": {
                "first_name": "Test",
                "last_name": "User",
                "email_address": "test@example.com",
            },
            "metadata": {
                "source": "Additional Test Data",
                "link": "https://example.com",
                "project": "Test Project",
            },
        }

        additional_file = project_dir / "data" / "input" / "additional_data.json"
        additional_file.write_text(json.dumps(additional_data, indent=2))

        # Step 5: Run incremental mapping
        result_map_incremental = subprocess.run(
            ["uv", "run", "mater-cli", "dimensions", "map", "-m", "incremental"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_map_incremental.returncode == 0
        assert "new dimensions added" in result_map_incremental.stdout


def test_dimensions_resolve_workflow(tmp_path):
    """Test dimensions resolve workflow for validating mapping"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["resolve-test"])
        assert result_init.exit_code == 0

        project_dir = Path("resolve-test").resolve()

        # Step 2: Setup input data
        src_input = project_dir / "examples" / "minimal_example.json"
        dst_input = project_dir / "data" / "input" / "minimal_example.json"
        dst_input.write_text(src_input.read_text())

        # Step 3: Create initial mapping
        result_map = subprocess.run(
            ["uv", "run", "mater-cli", "dimensions", "map"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_map.returncode == 0

        # Step 4: Simulate user editing mapping (copy from examples)
        src_complete_mapping = (
            project_dir / "examples" / "minimal_dimensions_hierarchy.json"
        )
        mapping_file = (
            project_dir / "data" / "dimensions_hierarchy" / "dimensions_mapping.json"
        )
        if src_complete_mapping.exists():
            mapping_file.write_text(src_complete_mapping.read_text())

        # Step 5: Run resolve to validate mapping
        result_resolve = subprocess.run(
            ["uv", "run", "mater-cli", "dimensions", "map", "-m", "resolve"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_resolve.returncode == 0
        assert "validated successfully" in result_resolve.stdout


def test_dimensions_mapping_with_missing_input_data(tmp_path):
    """Test dimensions map when no input data is available"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["no-input-test"])
        assert result_init.exit_code == 0

        project_dir = Path("no-input-test").resolve()

        # Step 2: Try to map dimensions without input data
        result = subprocess.run(
            ["uv", "run", "mater-cli", "dimensions", "map"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "No input data available" in result.stdout


def test_dimensions_build_without_mapping(tmp_path):
    """Test dimensions build when no mapping file exists"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["no-mapping-test"])
        assert result_init.exit_code == 0

        project_dir = Path("no-mapping-test").resolve()

        # Step 2: Try to build without mapping file
        result = subprocess.run(
            ["uv", "run", "mater-cli", "dimensions", "build"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "Mapping file not found" in result.stdout
