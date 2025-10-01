"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

import subprocess
from pathlib import Path

from click.testing import CliRunner

from src.init_mater_project.main import main


def test_simulation_full_workflow(tmp_path):
    """Test complete simulation workflow: generate project → setup data → setup dimensions → run simulation"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["simulation-test"])
        assert result_init.exit_code == 0
        assert "✅ MATER project 'simulation-test' initialized!" in result_init.output

        project_dir = Path("simulation-test").resolve()

        # Step 2: Setup input data (copy minimal example from generated project)
        src_input = project_dir / "examples" / "minimal_example.json"
        dst_input = project_dir / "data" / "input" / "minimal_example.json"
        dst_input.write_text(src_input.read_text())

        # Step 3: Setup dimensions hierarchy (copy from examples)
        src_dimensions = project_dir / "examples" / "minimal_dimensions_hierarchy.json"
        dst_dimensions = (
            project_dir / "data" / "dimensions_hierarchy" / "dimensions_hierarchy.json"
        )
        dst_dimensions.write_text(src_dimensions.read_text())

        # Step 4: Setup variables dimensions (copy from examples)
        src_variables = project_dir / "examples" / "minimal_variables_dimensions.json"
        dst_variables = (
            project_dir / "data" / "references" / "variables_dimensions.json"
        )
        dst_variables.write_text(src_variables.read_text())

        # Step 5: Run simulation using subprocess
        result_simulation = subprocess.run(
            ["uv", "run", "mater-cli", "simulation", "run"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_simulation.returncode == 0
        assert "Simulation completed successfully!" in result_simulation.stdout

        # Step 6: Verify simulation outputs were created
        output_dir = project_dir / "outputs" / "simulation_outputs"
        assert output_dir.exists()

        # Check for typical MATER output files
        output_files = list(output_dir.glob("*"))
        assert len(output_files) > 0


def test_simulation_with_example_workflow(tmp_path):
    """Test simulation pipeline using --example flag in generated project"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["simulation-example-project"])
        assert result_init.exit_code == 0

        project_dir = Path("simulation-example-project").resolve()

        # Step 2: Run simulation with example data
        result_simulation = subprocess.run(
            ["uv", "run", "mater-cli", "simulation", "run", "--example"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_simulation.returncode == 0
        assert "Example data" in result_simulation.stdout
        assert "Simulation completed successfully!" in result_simulation.stdout

        # Step 3: Verify example outputs were created
        example_output_dir = project_dir / "examples" / "example_outputs"
        assert example_output_dir.exists()


def test_simulation_with_custom_parameters(tmp_path):
    """Test simulation with custom start time, end time, and scenario"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["custom-simulation-test"])
        assert result_init.exit_code == 0

        project_dir = Path("custom-simulation-test").resolve()

        # Step 2: Setup data from examples
        src_input = project_dir / "examples" / "minimal_example.json"
        dst_input = project_dir / "data" / "input" / "minimal_example.json"
        dst_input.write_text(src_input.read_text())

        src_dimensions = project_dir / "examples" / "minimal_dimensions_hierarchy.json"
        dst_dimensions = (
            project_dir / "data" / "dimensions_hierarchy" / "dimensions_hierarchy.json"
        )
        dst_dimensions.write_text(src_dimensions.read_text())

        src_variables = project_dir / "examples" / "minimal_variables_dimensions.json"
        dst_variables = (
            project_dir / "data" / "references" / "variables_dimensions.json"
        )
        dst_variables.write_text(src_variables.read_text())

        # Step 3: Run simulation with custom parameters
        result_simulation = subprocess.run(
            [
                "uv",
                "run",
                "mater-cli",
                "simulation",
                "run",
                "--start-time",
                "1950",
                "--end-time",
                "2050",
                "--scenario",
                "test_scenario",
                "--name",
                "custom_test_outputs",
            ],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )

        assert result_simulation.returncode == 0
        assert "1950 - 2050" in result_simulation.stdout
        assert "test_scenario" in result_simulation.stdout
        assert "custom_test_outputs" in result_simulation.stdout

        # Step 4: Verify custom output directory was created
        custom_output_dir = project_dir / "outputs" / "custom_test_outputs"
        assert custom_output_dir.exists()


def test_simulation_list_variables(tmp_path):
    """Test listing variables and dimensions for simulation"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["list-test"])
        assert result_init.exit_code == 0

        project_dir = Path("list-test").resolve()

        # Step 2: List variables using subprocess
        result_list_vars = subprocess.run(
            ["uv", "run", "mater-cli", "simulation", "list-variables"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_list_vars.returncode == 0
        assert "Variables and their associated dimensions:" in result_list_vars.stdout

        # Step 3: List variables with example data
        result_list_vars_example = subprocess.run(
            ["uv", "run", "mater-cli", "simulation", "list-variables", "--example"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_list_vars_example.returncode == 0
        assert "Example data" in result_list_vars_example.stdout


def test_simulation_list_dimensions(tmp_path):
    """Test listing dimensions for simulation"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["dimensions-list-test"])
        assert result_init.exit_code == 0

        project_dir = Path("dimensions-list-test").resolve()

        # Step 2: Setup dimensions hierarchy from examples
        src_dimensions = project_dir / "examples" / "minimal_dimensions_hierarchy.json"
        dst_dimensions = (
            project_dir / "data" / "dimensions_hierarchy" / "dimensions_hierarchy.json"
        )
        dst_dimensions.write_text(src_dimensions.read_text())

        # Step 3: List dimensions using subprocess
        result_list_dims = subprocess.run(
            ["uv", "run", "mater-cli", "simulation", "list-dimensions"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_list_dims.returncode == 0
        assert "Dimensions and their values:" in result_list_dims.stdout

        # Step 4: List dimensions with example data
        result_list_dims_example = subprocess.run(
            ["uv", "run", "mater-cli", "simulation", "list-dimensions", "--example"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_list_dims_example.returncode == 0
        assert "Example data" in result_list_dims_example.stdout


def test_simulation_with_missing_data(tmp_path):
    """Test simulation when required data files are missing"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["missing-data-test"])
        assert result_init.exit_code == 0

        project_dir = Path("missing-data-test").resolve()

        # Step 2: Try to run simulation without setting up data
        result_simulation = subprocess.run(
            ["uv", "run", "mater-cli", "simulation", "run"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_simulation.returncode == 0
        assert "No valid input JSON files found" in result_simulation.stdout


def test_simulation_with_invalid_config(tmp_path):
    """Test simulation with invalid configuration parameters"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["invalid-config-test"])
        assert result_init.exit_code == 0

        project_dir = Path("invalid-config-test").resolve()

        # Step 2: Try to run simulation with invalid time range
        result_simulation = subprocess.run(
            [
                "uv",
                "run",
                "mater-cli",
                "simulation",
                "run",
                "--start-time",
                "2100",
                "--end-time",
                "1900",  # End before start
            ],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )

        assert result_simulation.returncode == 0
        assert "2100 - 1900" in result_simulation.stdout
        assert "No valid input JSON files found" in result_simulation.stdout
