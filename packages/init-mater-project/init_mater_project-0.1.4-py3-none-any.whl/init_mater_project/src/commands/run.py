"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

import json
import pandas as pd
from pathlib import Path

import click
from pydantic import ValidationError
from mater import Mater

from src.settings import MaterConfig


def run_simulation(config: MaterConfig):
    """
    # Run a MATER simulation with provided configuration

    ## Arguments
    - `config` (MaterConfig): Configuration object containing simulation parameters and  file paths

    ## Returns
    - `None`: This function performs the simulation and outputs results but doesn't return a value
    """

    try:
        data_df, dimension_df, variable_dimension_df = load_simulation_data(config)

        model = Mater()

        click.echo("\n⚙️  Building simulation parameters...")
        params = model.parameter_from_df(
            config.output_path,
            config.simulation.start_time,
            config.simulation.end_time,
            config.simulation.frequency,
            config.simulation.scenario,
            dimension_df,
            variable_dimension_df,
            data_df,
        )
        click.echo(
            f"Simulation parameters built successfully ({config.simulation.start_time}-{config.simulation.end_time}, {config.simulation.frequency})"
        )

        click.echo("\n🚀 Running simulation...")
        model.run(params[0])

        click.echo("✅ Simulation completed successfully!")
        click.echo(f"\n📁 See outputs in folder: '{config.output_path}'")

    except FileNotFoundError as e:
        click.echo(f"❌ File not found: {e}")
    except json.JSONDecodeError as e:
        click.echo(f"❌ Invalid JSON format: {e}")
    except ValidationError as e:
        click.echo("❌ Configuration validation error:")
        for error in e.errors():
            field = " -> ".join(str(x) for x in error["loc"])
            click.echo(f"  {field}: {error['msg']}")
    except ValueError as e:
        click.echo(f"❌ Invalid data format: {e}")
    except PermissionError as e:
        click.echo(f"❌ Permission denied: {e}")
    except Exception as e:
        click.echo(f"❌ Simulation error: {e}")


def load_simulation_data(config: MaterConfig):
    """
    # Load data required for simulation

    ## Arguments
    - `config` (MaterConfig): Configuration object containing file paths

    ## Returns
    - `tuple`: (data_df, dimension_df, variable_dimension_df)
    """
    click.echo("\n📥 Loading simulation data...")

    data_df = input_json_to_dataframe(config.paths.input_path)
    click.echo(f"Input data loaded ({len(data_df)} rows)")

    dimension_df = dimension_json_to_dataframe(config.paths.dimensions_hierarchy_file)
    click.echo(f"Dimensions values loaded ({len(dimension_df)} unique combinations)")

    variable_dimension_df = variables_dimensions_json_to_dataframe(
        config.paths.variables_dimensions_path
    )
    click.echo(
        f"Variable-dimension associations loaded ({len(variable_dimension_df)} associations)"
    )

    click.echo("🎯 All simulation data loaded successfully")
    return data_df, dimension_df, variable_dimension_df


def input_json_to_dataframe(path: Path) -> pd.DataFrame:
    """
    Load input data JSON (with sections: input_data, provider, metadata)

    Args:
        path: Path to input JSON file or directory

    Returns:
        DataFrame from input_data section
    """
    path = Path(path)

    if path.is_file():
        data = _json_to_dataframe(path, "input data file")

        if not isinstance(data, dict) or "input_data" not in data:
            raise ValueError(
                f"Input JSON must contain 'input_data' section, got: {list(data.keys()) if isinstance(data, dict) else type(data)}"
            )

        return pd.DataFrame(data["input_data"])

    elif path.is_dir():
        dataframes = []
        processed_files = []

        json_files = [
            f for f in path.rglob("*.json") if f.stem not in {"metadata", "provider"}
        ]

        for json_file in json_files:
            try:
                data = _json_to_dataframe(json_file, "input data file")

                if isinstance(data, dict) and "input_data" in data:
                    df = pd.DataFrame(data["input_data"]).reset_index(drop=True)
                    dataframes.append(df)
                    processed_files.append(str(json_file.relative_to(path)))
                else:
                    click.echo(f"Skipping {json_file}: missing 'input_data' section")
                    continue

            except Exception as e:
                click.echo(f"Skipping {json_file}: {e}")
                continue

        if not dataframes:
            raise ValueError(f"No valid input JSON files found in: {path}")

        click.echo(f"Processed files in folder: {path}")
        for file_path in processed_files:
            click.echo(f"  - {file_path}")

        return pd.concat(dataframes, ignore_index=True, sort=False)

    else:
        raise ValueError(f"Path must be file or directory: {path}")


def dimension_json_to_dataframe(path: Path) -> pd.DataFrame:
    """
    Load dimension data JSON (array of dimension objects)
    Expected format: [{"name": "location", "value": "france", "equivalence": {...}, "parents_values": {...}}, ...]

    Args:
        path: Path to dimensions JSON file

    Returns:
        DataFrame with dimension data
    """
    data = _json_to_dataframe(path, "dimension data file")

    if not isinstance(data, list):
        raise ValueError(f"Dimension JSON must be an array, got: {type(data)}")

    return pd.DataFrame(data)


def variables_dimensions_json_to_dataframe(path: Path) -> pd.DataFrame:
    """
    Load variables-dimensions JSON (array of variable-dimension associations)
    Expected format: [{"variable": "exogenous_stock", "dimension": "location", "property": "extensive"}, ...]

    Args:
        path: Path to variables-dimensions JSON file

    Returns:
        DataFrame with variable-dimension associations
    """
    data = _json_to_dataframe(path, "variables-dimensions file")

    if not isinstance(data, list):
        raise ValueError(
            f"Variables-dimensions JSON must be an array, got: {type(data)}"
        )

    return pd.DataFrame(data)


def _json_to_dataframe(path: Path, description: str = "file") -> dict | list:
    """
    Internal: Load and parse JSON file

    Args:
        path: Path to JSON file
        description: Description for logging

    Returns:
        Parsed JSON data (dict or list)
    """
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")

    if path.suffix.lower() != ".json":
        raise ValueError(f"File must be a JSON file, got: {path.suffix}")

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        click.echo(f"Processed {description}: {path}")
        return data
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in {path}: {e.msg}", e.doc, e.pos)


if __name__ == "__main__":
    run_simulation()
