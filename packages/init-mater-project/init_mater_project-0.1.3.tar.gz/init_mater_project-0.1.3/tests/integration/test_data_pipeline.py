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


def test_project_generation_creates_proper_structure(tmp_path):
    """Test that project generation creates all necessary directories and files"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Generate new MATER project
        result = runner.invoke(main, ["structure-test"])
        assert result.exit_code == 0
        assert "MATER project 'structure-test' initialized!" in result.output

        project_dir = Path("structure-test")

        # Verify essential files exist
        assert (project_dir / "config.toml").exists()
        assert (project_dir / "README.md").exists()

        # Verify directory structure
        assert (project_dir / "data" / "raw").is_dir()
        assert (project_dir / "data" / "input").is_dir()
        assert (project_dir / "data" / "references").is_dir()
        assert (project_dir / "data" / "dimensions_hierarchy").is_dir()
        assert (project_dir / "transforms" / "datasets").is_dir()
        assert (project_dir / "outputs").is_dir()
        assert (project_dir / "src").is_dir()
        assert (project_dir / "examples").is_dir()

        # Verify config.toml has valid content
        config_content = (project_dir / "config.toml").read_text()
        assert "[simulation]" in config_content
        assert "[paths]" in config_content
        assert "[provider]" in config_content
        assert "[metadata]" in config_content


def test_data_generate_to_build_pipeline_full_workflow(tmp_path):
    """Test complete workflow: generate project → generate script → build data → validate output"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["test-project"])
        assert result_init.exit_code == 0
        assert "✅ MATER project 'test-project' initialized!" in result_init.output

        project_dir = Path("test-project").resolve()

        # Verify project structure was created
        assert project_dir.exists()
        assert (project_dir / "config.toml").exists()
        assert (project_dir / "data" / "raw").exists()

        # Setup: copy minimal example CSV from generated project examples to raw
        src_csv = project_dir / "examples" / "minimal_raw_example.csv"
        dst_csv = project_dir / "data" / "raw" / "minimal_raw_example.csv"
        dst_csv.write_text(src_csv.read_text())

        # Step 2: Generate transformation script using subprocess
        result_generate = subprocess.run(
            ["uv", "run", "mater-cli", "data", "generate"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_generate.returncode == 0
        assert "Generated" in result_generate.stdout

        # Verify script was created
        script_path = project_dir / "transforms" / "datasets" / "minimal_raw_example.py"
        assert script_path.exists()

        # Step 3: Build input data from script using subprocess
        result_build = subprocess.run(
            ["uv", "run", "mater-cli", "data", "build"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_build.returncode == 0
        assert "All scripts executed successfully!" in result_build.stdout

        # Step 4: Validate generated JSON output
        json_files = list((project_dir / "data/input").glob("*.json"))
        assert len(json_files) == 1

        json_data = json.loads(json_files[0].read_text())
        assert "input_data" in json_data
        assert "provider" in json_data
        assert "metadata" in json_data
        assert len(json_data["input_data"]) > 0


def test_data_pipeline_with_example_workflow(tmp_path):
    """Test data pipeline using --example flag in generated project"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["example-project"])
        assert result_init.exit_code == 0

        project_dir = Path("example-project").resolve()

        # Step 2: Test data generate with example data using subprocess
        result_generate = subprocess.run(
            ["uv", "run", "mater-cli", "data", "generate", "--example"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_generate.returncode == 0
        assert "Example data" in result_generate.stdout

        # Step 3: Test data build with example data using subprocess
        result_build = subprocess.run(
            ["uv", "run", "mater-cli", "data", "build", "--example"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_build.returncode == 0
        assert "Example data" in result_build.stdout


def test_data_build_with_multiple_scripts_in_generated_project(tmp_path):
    """Test data build with multiple transformation scripts in generated project"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["multi-script-project"])
        assert result_init.exit_code == 0

        project_dir = Path("multi-script-project").resolve()

        # Step 2: Create multiple raw files
        (project_dir / "data/raw/dataset1.csv").write_text(
            "time,location,object,value,unit,variable,scenario\n"
            "2000,france,car,100,number,exogenous_stock,historical\n"
        )
        (project_dir / "data/raw/dataset2.csv").write_text(
            "time,location,object,value,unit,variable,scenario\n"
            "2000,spain,car,200,number,exogenous_stock,historical\n"
        )

        # Step 3: Generate multiple scripts using subprocess
        result_generate = subprocess.run(
            ["uv", "run", "mater-cli", "data", "generate"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_generate.returncode == 0
        assert "2 script(s) successfully" in result_generate.stdout

        # Step 4: Build input data from all scripts using subprocess
        result_build = subprocess.run(
            ["uv", "run", "mater-cli", "data", "build"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_build.returncode == 0

        # Step 5: Verify multiple JSON files were created
        json_files = list((project_dir / "data/input").glob("*.json"))
        assert len(json_files) == 2

        # Verify each file has correct structure
        for json_file in json_files:
            json_data = json.loads(json_file.read_text())
            assert "input_data" in json_data
            assert len(json_data["input_data"]) > 0


def test_data_build_error_handling_in_generated_project(tmp_path):
    """Test data build with failing script in generated project → proper error handling"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["error-test-project"])
        assert result_init.exit_code == 0

        project_dir = Path("error-test-project").resolve()

        # Step 2: Create a script that will fail
        transforms_dir = project_dir / "transforms/datasets"

        failing_script = transforms_dir / "failing_script.py"
        failing_script.write_text("""
import sys
print("This script will fail")
sys.exit(1)
""")

        working_script = transforms_dir / "working_script.py"
        working_script.write_text("""
import json
from pathlib import Path
from src.settings import MaterConfig

def main():
    config = MaterConfig()
    output_dir = Path(config.paths.input_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    final_data = {
        "input_data": [{
            "time": 2000,
            "value": 100,
            "scenario": "historical",
            "unit": "number",
            "variable": "exogenous_stock",
            "dimensions_values": {"location": "france", "object": "car"}
        }],
        "provider": {
            "first_name": "Test",
            "last_name": "User",
            "email_address": "test@example.com"
        },
        "metadata": {
            "source": "Test Source",
            "link": "https://example.com",
            "project": "Test Project"
        }
    }

    output_path = output_dir / "working_script.json"
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(final_data, file, indent=2, ensure_ascii=False)

    print(f"Generated 1 MATER records")

if __name__ == "__main__":
    main()
""")

        # Step 3: Build input data with mixed success/failure using subprocess
        result_build = subprocess.run(
            ["uv", "run", "mater-cli", "data", "build"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result_build.returncode == 0  # Command should not crash
        assert "✅ 1 successful, ❌ 1 failed" in result_build.stdout

        # Step 4: Verify working script still produced output
        json_files = list((project_dir / "data/input").glob("*.json"))
        assert len(json_files) == 1

        json_data = json.loads(json_files[0].read_text())
        assert "input_data" in json_data


def test_data_generate_in_empty_raw_directory(tmp_path):
    """Test data generate when raw directory is empty"""
    runner = CliRunner()

    with runner.isolated_filesystem(temp_dir=tmp_path):
        # Step 1: Generate new MATER project
        result_init = runner.invoke(main, ["empty-raw-test"])
        assert result_init.exit_code == 0

        project_dir = Path("empty-raw-test").resolve()

        # Step 2: Try to generate scripts with empty raw directory using subprocess
        result = subprocess.run(
            ["uv", "run", "mater-cli", "data", "generate"],
            cwd=project_dir,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "No supported dataset files found" in result.stdout
