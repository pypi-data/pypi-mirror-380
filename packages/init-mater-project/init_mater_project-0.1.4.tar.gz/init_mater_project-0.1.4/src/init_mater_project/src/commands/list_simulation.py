"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

import json
from pathlib import Path
from typing import Dict, List

import click

from src.settings import MaterConfig


def list_simulation_variables(config: MaterConfig) -> None:
    """
    # List variables and their associated dimensions from configured file

    ## Arguments
    - `config` (MaterConfig): Configuration object containing variable dimension file path

    ## Returns
    - `None`: Displays variables summary to console or error messages
    """
    try:
        with open(config.paths.variables_dimensions_path, "r", encoding="utf-8") as f:
            var_dim_data = json.load(f)

        var_dimensions = {}
        for item in var_dim_data:
            variable = item.get("variable")
            dimension = item.get("dimension")
            if variable and dimension:
                if variable not in var_dimensions:
                    var_dimensions[variable] = []
                if dimension not in var_dimensions[variable]:
                    var_dimensions[variable].append(dimension)

        click.echo("📋 Variables and their associated dimensions:\n")

        for var in sorted(var_dimensions.keys()):
            dimensions = ", ".join(sorted(var_dimensions[var]))
            click.echo(f"  • {var} ({dimensions})")

        click.echo(f"\nTotal: {len(var_dimensions)} variables")

    except FileNotFoundError:
        click.echo(
            f"❌ Variable dimension file not found: {config.paths.variables_dimensions_path}"
        )
    except json.JSONDecodeError as e:
        click.echo(f"❌ Invalid JSON in variable dimension file: {e}")
    except Exception as e:
        click.echo(f"❌ Error loading variables: {e}")


def list_simulation_dimensions(config: MaterConfig) -> None:
    """
    # List dimensions and their values from hierarchy file

    ## Arguments
    - `config` (MaterConfig): Configuration object containing hierarchy file path

    ## Returns
    - `None`: Displays dimensions summary to console or error messages
    """
    try:
        with open(config.paths.dimensions_hierarchy_file, "r", encoding="utf-8") as f:
            hierarchy_data = json.load(f)

        dimension_values = {}
        for entry in hierarchy_data:
            name = entry.get("name")
            value = entry.get("value")
            if name and value:
                if name not in dimension_values:
                    dimension_values[name] = []
                if value not in dimension_values[name]:
                    dimension_values[name].append(value)

        click.echo("📊 Dimensions and their values:\n")

        for dim in sorted(dimension_values.keys()):
            values = ", ".join(sorted(dimension_values[dim]))
            click.echo(f"  • {dim} ({values})")

        click.echo(f"\nTotal: {len(dimension_values)} dimensions")

    except FileNotFoundError:
        click.echo(
            f"❌ Dimensions hierarchy file not found: {config.paths.dimensions_hierarchy_file}"
        )
    except json.JSONDecodeError as e:
        click.echo(f"❌ Invalid JSON in dimensions hierarchy file: {e}")
    except Exception as e:
        click.echo(f"❌ Error loading dimensions: {e}")


def load_all_input_records(input_path: Path) -> List[Dict]:
    """
    # Load all records from input data files

    ## Arguments
    - `input_path` (Path): Path to input data directory or file

    ## Returns
    - `List[Dict]`: All input records combined
    """
    all_records = []

    if input_path.is_file():
        records = load_records_from_file(input_path)
        all_records.extend(records)
    elif input_path.is_dir():
        json_files = list(input_path.rglob("*.json"))

        for json_file in json_files:
            try:
                records = load_records_from_file(json_file)
                all_records.extend(records)
            except Exception:
                continue  # Skip invalid files silently for units listing

    return all_records


def load_records_from_file(file_path: Path) -> List[Dict]:
    """
    # Load input_data records from single MATER input file

    ## Arguments
    - `file_path` (Path): Path to MATER input JSON file

    ## Returns
    - `List[Dict]`: List of input_data records
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict) and "input_data" in data:
        return data["input_data"]

    return []
