"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

import subprocess
import sys
from pathlib import Path
from typing import List

import click

from src.settings import MaterConfig


def build_input_data(config: MaterConfig) -> None:
    """
    # Execute transformation scripts to build MATER input data

    ## Arguments
    - `config` (MaterConfig): Configuration object containing scripts and output paths

    ## Returns
    - `None`: Executes scripts and displays results to console
    """

    try:
        scripts = get_scripts(config.paths.transforms_script_path)
        if not scripts:
            click.echo(
                f"⚠️  No Python scripts found in {config.paths.transforms_script_path}"
            )
            return

        default_config = MaterConfig()
        script_output_dir = default_config.paths.input_path
        if script_output_dir.is_file():
            script_output_dir = script_output_dir.parent

        files_to_generate = []
        existing_files_to_override = []

        for script in scripts:
            expected_file = script_output_dir / f"{script.stem}.json"
            files_to_generate.append(expected_file)
            if expected_file.exists():
                existing_files_to_override.append(expected_file)

        if existing_files_to_override:
            click.echo(
                f"⚠️  Found {len(existing_files_to_override)} existing file(s) that will be overwritten:"
            )
            for file_path in existing_files_to_override:
                click.echo(f"   - {file_path.name}")

            response = input("\nOverride existing files? (y/N): ")
            if response.lower() not in ["y", "yes"]:
                click.echo("Build cancelled by user")
                return

        click.echo(f"🚀 Executing {len(scripts)} transformation script(s)...")

        generated_files = []
        success_count = 0

        for script in scripts:
            click.echo(f"   ⚙️  Executing {script.name}...")

            if execute_script(script):
                expected_file = script_output_dir / f"{script.stem}.json"
                if expected_file.exists():
                    click.echo(f"   ✅ {script.name} completed successfully")
                    generated_files.append(expected_file)
                    success_count += 1
                else:
                    click.echo(
                        f"   ⚠️  {script.name} executed but no output file found: {expected_file}"
                    )
                    click.echo(
                        "       Script may have failed silently or saved to wrong location"
                    )
            else:
                click.echo(f"   ❌ {script.name} failed")

        failed_count = len(scripts) - success_count
        click.echo(
            f"\n📊 Summary: ✅ {success_count} successful, ❌ {failed_count} failed"
        )

        if failed_count == 0:
            click.echo("🎯 All scripts executed successfully!")
            if generated_files:
                click.echo(
                    f"\n📄 Generated {len(generated_files)} file(s) in: {script_output_dir}"
                )
                for file_path in generated_files:
                    click.echo(f"   - {file_path.name}")

    except Exception as e:
        click.echo(f"❌ Error: {e}")


def get_scripts(script_path: Path) -> List[Path]:
    """
    # Discover Python scripts to execute from specified path

    ## Arguments
    - `script_path` (Path): Path to script file or directory containing scripts

    ## Returns
    - `List[Path]`: List of Python script paths ready for execution
    """
    if not script_path.exists():
        raise FileNotFoundError(f"Script path not found: {script_path}")

    if script_path.is_file():
        if script_path.suffix != ".py":
            raise ValueError(f"File must be a Python script (.py): {script_path}")
        click.echo(f"📁 Found script file: {script_path}")
        return [script_path]

    scripts = sorted(script_path.glob("*.py"))
    click.echo(f"📁 Found {len(scripts)} Python script(s) in: {script_path}")
    for script in scripts:
        click.echo(f"   - {script.name}")

    return scripts


def execute_script(script_path: Path) -> bool:
    """
    # Execute a single transformation script and return success status

    ## Arguments
    - `script_path` (Path): Path to Python script to execute

    ## Returns
    - `bool`: True if script executed successfully, False if failed or timeout
    """
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=300,
        )
        return result.returncode == 0

    except subprocess.TimeoutExpired:
        click.echo(f"   ⏰ {script_path.name} timed out")
        return False
    except Exception as e:
        click.echo(f"   ❌ {script_path.name} error: {e}")
        return False
