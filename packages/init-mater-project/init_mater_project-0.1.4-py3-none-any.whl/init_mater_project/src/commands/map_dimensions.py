"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

import json
from pathlib import Path
from typing import List, Dict
from enum import Enum

import click

from src.settings import MaterConfig
from src.lib.dimensions import (
    create_dimensions_mapping,
    resolve_single_mapping_entry,
    create_reference_indexes,
)


class MappingMode(Enum):
    """Dimensions mapping operation modes"""

    INITIAL = "initial"
    INCREMENTAL = "incremental"
    FORCE = "force"
    RESOLVE = "resolve"


def map_dimensions(config: MaterConfig, mode: MappingMode) -> None:
    """
    # Map input dimensions to reference into a mapping file

    ## Arguments
    - `config` (MaterConfig): Configuration object containing paths and simulation parameters
    - `mode` (MappingMode): Mapping operation mode

    ## Returns
    - `None`: Creates or updates mapping file but doesn't return a value
    """

    try:
        has_input_data = False
        input_path = config.paths.input_path
        if input_path.is_file() and input_path.suffix.lower() == ".json":
            has_input_data = True
        elif input_path.is_dir():
            json_files = list(input_path.rglob("*.json"))
            has_input_data = True if len(json_files) > 0 else False

        if not has_input_data:
            click.echo("⚠️  No input data available for dimension mapping")
            click.echo(f"    Expected: {config.paths.input_path}")
            click.echo("💡 Add MATER-formatted JSON files to input directory first")
            return

        mapping_file = config.paths.dimensions_mapping_file
        mapping_exists = mapping_file.exists()

        if not mapping_exists and mode in [
            MappingMode.RESOLVE,
            MappingMode.INCREMENTAL,
        ]:
            click.echo("❌ No mapping file found for this operation")
            click.echo("💡 Create the initial mapping:")
            click.secho(
                "   uv run mater-cli dimensions map", fg="bright_blue", bold=True
            )
            return

        if mapping_exists and mode == MappingMode.INITIAL:
            click.echo(f"⚠️  Mapping file already exists: {mapping_file}")
            click.echo("💡 Options:")
            click.echo("   -m incremental : Add new dimensions only")
            click.echo("   -m force       : Override existing mapping")
            click.echo("   -m resolve     : Validate and resolve references")
            return

        if mode == MappingMode.RESOLVE:
            resolve_mapping_references(config)

        elif mode == MappingMode.FORCE:
            if mapping_exists:
                click.echo(f"⚠️  This will override existing mapping: {mapping_file}")
                response = input("Continue? (y/N): ")
                if response.lower() not in ["y", "yes"]:
                    click.echo("Operation cancelled")
                    return
            create_initial_mapping(config)

        elif mode == MappingMode.INCREMENTAL:
            update_mapping_incremental(config)

        elif mode == MappingMode.INITIAL:
            create_initial_mapping(config)

    except FileNotFoundError as e:
        click.echo(f"⚠️  File not found: {e}")
    except json.JSONDecodeError as e:
        click.echo(f"⚠️  Invalid JSON format: {e}")
    except PermissionError:
        click.echo("⚠️  Permission denied")
    except Exception as e:
        click.echo(f"⚠️  Error creating dimensions mapping: {e}")


def create_initial_mapping(config: MaterConfig) -> None:
    """
    # Create initial mapping from input data

    ## Arguments
    - `config` (MaterConfig): Configuration object

    ## Returns
    - `None`: Creates mapping file
    """
    source_dimensions = load_dimensions_from_input_data(config.paths.input_path)
    reference_dimensions = load_dimensions_values(config.paths.dimensions_values_path)

    dimensions_mapping = create_dimensions_mapping(
        source_dimensions, reference_dimensions
    )

    with open(config.paths.dimensions_mapping_file, "w", encoding="utf-8") as f:
        json.dump(dimensions_mapping, f, indent=2, ensure_ascii=False)
    click.echo(
        f"✅ Generated dimensions mapping: {config.paths.dimensions_mapping_file}"
    )

    mapped_count = 0
    todo_count = 0
    for entry in dimensions_mapping:
        reference_equivalence = entry.get("reference_equivalence", {})
        parent_hierarchy = entry.get("parent_hierarchy", {})

        has_ref_todo = "TODO" in reference_equivalence
        has_parent_todo = "TODO" in parent_hierarchy

        if has_ref_todo or has_parent_todo:
            todo_count += 1
        else:
            mapped_count += 1

    click.echo(
        f"📊 Mapped {len(dimensions_mapping)} unique dimension values from {len(source_dimensions)} source values"
    )

    if mapped_count > 0:
        click.echo(f"✅ {mapped_count} dimensions successfully mapped to reference")

    if todo_count > 0:
        click.echo(f"⚠️  {todo_count} dimensions need manual completion")
        click.echo("\n💡 Next steps:")
        click.echo(f"   1. Edit mapping file: {config.paths.dimensions_mapping_file}")
        click.echo("      - Remove TODO keys and fill with real data")
        click.echo(
            "      - Check out existing dimensions values: data/references/dimensions.json"
        )
        click.echo("   2. Resolve references and validate:")
        click.secho(
            "      uv run mater-cli dimensions map -m resolve",
            fg="bright_blue",
            bold=True,
        )
    else:
        click.echo("🎯 All dimensions successfully mapped!")
        click.echo("💡 Build your dimensions hierarchy:")
        click.secho("   uv run mater-cli dimensions build", fg="bright_blue", bold=True)


def update_mapping_incremental(config: MaterConfig) -> None:
    """
    # Update existing mapping by adding new dimensions while preserving user edits

    ## Arguments
    - `config` (MaterConfig): Configuration object

    ## Returns
    - `None`: Updates mapping file
    """
    existing_mapping = load_mapping_file(config.paths.dimensions_mapping_file)
    current_dimensions = load_dimensions_from_input_data(config.paths.input_path)
    reference_dimensions = load_dimensions_values(config.paths.dimensions_values_path)

    existing_combinations = {
        (entry["name"], entry["value"]) for entry in existing_mapping
    }
    new_dimensions = [
        dim
        for dim in current_dimensions
        if (dim["name"], dim["value"]) not in existing_combinations
    ]

    if not new_dimensions:
        click.echo("ℹ️  No new dimensions found")
        click.echo(f"   Current mapping: {len(existing_mapping)} dimensions")
        click.echo(f"   Input data: {len(current_dimensions)} dimensions")
        return

    new_mapping_entries = create_dimensions_mapping(
        new_dimensions, reference_dimensions
    )
    updated_mapping = existing_mapping + new_mapping_entries

    with open(config.paths.dimensions_mapping_file, "w", encoding="utf-8") as f:
        json.dump(updated_mapping, f, indent=2, ensure_ascii=False)
    click.echo(f"✅ Updated dimensions mapping: {config.paths.dimensions_mapping_file}")

    click.echo("📊 Incremental mapping completed:")
    click.echo(f"   📌 {len(existing_mapping)} existing dimensions preserved")
    click.echo(f"   🆕 {len(new_mapping_entries)} new dimensions added")

    if len(new_mapping_entries) > 0:
        click.echo("\n💡 Next steps:")
        click.echo(f"   1. Edit mapping file: {config.paths.dimensions_mapping_file}")
        click.echo("      - Remove TODO keys and fill with real data")
        click.echo(
            "      - Check out existing dimensions values: data/references/dimensions.json"
        )
        click.echo("   2. Resolve references and validate:")
        click.secho(
            "      uv run mater-cli dimensions map -m resolve",
            fg="bright_blue",
            bold=True,
        )


def resolve_mapping_references(config: MaterConfig) -> None:
    """
    # Validate and resolve references in user-edited mapping

    ## Arguments
    - `config` (MaterConfig): Configuration object

    ## Returns
    - `None`: Updates mapping with resolved references and validation
    """
    mapping = load_mapping_file(config.paths.dimensions_mapping_file)
    reference_dimensions = load_dimensions_values(config.paths.dimensions_values_path)
    reference_index = create_reference_indexes(reference_dimensions)
    all_input_dimensions = load_dimensions_from_input_data(config.paths.input_path)

    resolved_mapping = []
    errors = []
    auto_resolved = 0

    for entry in mapping:
        resolved_entry, entry_errors, was_auto_resolved = resolve_single_mapping_entry(
            entry, reference_index, all_input_dimensions
        )
        resolved_mapping.append(resolved_entry)
        errors.extend(entry_errors)
        if was_auto_resolved:
            auto_resolved += 1

    success_count = len(mapping) - len(errors)

    click.echo("📊 Resolution completed:")
    click.echo(f"   ✅ {success_count} entries validated successfully")
    if auto_resolved > 0:
        click.echo(f"   🔧 {auto_resolved} parent hierarchies auto-resolved")

    if errors:
        click.echo(f"   ❌ {len(errors)} errors found:")
        for error in errors:
            click.echo(f"      • {error}")

    if not errors:
        with open(config.paths.dimensions_mapping_file, "w", encoding="utf-8") as f:
            json.dump(resolved_mapping, f, indent=2, ensure_ascii=False)
        click.echo(
            f"✅ Resolved dimensions mapping: {config.paths.dimensions_mapping_file}"
        )
        click.echo("💡 Build your dimensions hierarchy:")
        click.secho("   uv run mater-cli dimensions build", fg="bright_blue", bold=True)
    else:
        click.echo("❌ Fix errors before proceeding to build")


def load_mapping_file(mapping_file: Path) -> List[Dict]:
    """
    # Load existing dimensions mapping from JSON file

    ## Arguments
    - `mapping_file` (Path): Path to mapping JSON file

    ## Returns
    - `List[Dict]`: Existing dimensions mapping data
    """
    if not mapping_file.exists():
        raise FileNotFoundError(f"Mapping file not found: {mapping_file}")

    try:
        with open(mapping_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError(f"Mapping file must contain an array, got: {type(data)}")

        click.echo(f"📁 Loaded existing mapping: {mapping_file} ({len(data)} entries)")
        return data

    except json.JSONDecodeError as e:
        click.echo(f"❌ Invalid JSON in mapping file: {mapping_file}")
        click.echo(f"   Error: {e.msg} at line {e.lineno}, column {e.colno}")
        raise json.JSONDecodeError(
            f"Invalid JSON in mapping file {mapping_file}", e.doc, e.pos
        )


def load_dimensions_from_input_data(input_path: Path) -> List[Dict]:
    """
    # Load dimensions from MATER input data files

    ## Arguments
    - `input_path` (Path): Path to input data directory or file

    ## Returns
    - `List[Dict]`: List of unique dimension value combinations
    """
    records = []
    processed_files = []

    if input_path.is_file():
        records = load_records_from_file(input_path)
        records.extend(records)
        processed_files.append(input_path.name)
    elif input_path.is_dir():
        json_files = list(input_path.rglob("*.json"))

        if not json_files:
            click.echo(f"⚠️  No JSON files found in {input_path}")
            return []

        for json_file in json_files:
            try:
                records = load_records_from_file(json_file)
                records.extend(records)
                processed_files.append(str(json_file.relative_to(input_path)))
            except Exception as e:
                click.echo(f"⚠️  Skipping {json_file}: {e}")
                continue
    else:
        raise ValueError(f"Input path must be file or directory: {input_path}")

    unique_dimensions = []
    seen_combinations = set()
    for record in records:
        dimensions_values = record.get("dimensions_values", {})
        if isinstance(dimensions_values, dict):
            for name, value in dimensions_values.items():
                combination = (name, value)
                if combination not in seen_combinations:
                    seen_combinations.add(combination)
                    unique_dimensions.append({"name": name, "value": value})

    click.echo("📁 Processed input file(s):")
    for file_path in processed_files:
        click.echo(f"   - {file_path}")

    return unique_dimensions


def load_dimensions_values(dimensions_values_path: Path) -> List[Dict]:
    """
    # Load dimensions values used as reference from JSON file or directory

    ## Arguments
    - `dimensions_values_path` (Path): Path to reference dimensions JSON file or directory

    ## Returns
    - `List[Dict]`: Reference dimensions data
    """
    if not dimensions_values_path.exists():
        click.echo(f"⚠️  Dimensions values path not found: {dimensions_values_path}")
        click.echo("Using empty reference (all dimensions will have TODO entries)")
        return []

    all_dimensions = []
    processed_files = []

    if dimensions_values_path.is_file():
        with open(dimensions_values_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError(f"File must contain an array, got: {type(data)}")

        all_dimensions.extend(data)
        processed_files.append(dimensions_values_path.name)
    elif dimensions_values_path.is_dir():
        json_files = list(dimensions_values_path.rglob("*.json"))

        if not json_files:
            click.echo(f"⚠️  No JSON files found in {dimensions_values_path}")
            return []

        for json_file in json_files:
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)

                if not isinstance(data, list):
                    raise ValueError(f"File must contain an array, got: {type(data)}")

                all_dimensions.extend(data)
                processed_files.append(
                    str(json_file.relative_to(dimensions_values_path))
                )
            except Exception as e:
                click.echo(f"⚠️  Skipping {json_file}: {e}")
                continue
    else:
        raise ValueError(
            f"Dimensions values path must be file or directory: {dimensions_values_path}"
        )

    click.echo("📚 Processed dimensions file(s):")
    for file_path in processed_files:
        click.echo(f"   - {file_path}")

    return all_dimensions


def check_input_data_availability(input_path: Path) -> bool:
    """
    # Check if input data is available in the specified path

    ## Arguments
    - `input_path` (Path): Path to check for input data

    ## Returns
    - `bool`: True if input data is available, False otherwise
    """
    if input_path.is_file() and input_path.suffix.lower() == ".json":
        return True
    elif input_path.is_dir():
        json_files = list(input_path.rglob("*.json"))
        return len(json_files) > 0

    return False


def load_records_from_file(file_path: Path) -> List[Dict]:
    """
    # Load input_data records from a single MATER input file

    ## Arguments
    - `file_path` (Path): Path to MATER input JSON file

    ## Returns
    - `List[Dict]`: List of input_data records
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict) or "input_data" not in data:
        raise ValueError(f"File must contain 'input_data' section: {file_path}")

    input_data = data["input_data"]
    if not isinstance(input_data, list):
        raise ValueError(f"'input_data' must be a list: {file_path}")

    return input_data
