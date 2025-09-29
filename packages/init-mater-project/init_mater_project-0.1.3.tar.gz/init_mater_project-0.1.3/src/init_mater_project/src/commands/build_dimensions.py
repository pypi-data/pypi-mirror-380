"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

import json
from pathlib import Path
from typing import List, Dict

import click

from src.settings import MaterConfig
from src.lib.dimensions import (
    build_complete_hierarchy_from_mapping,
    build_hierarchy_tree,
)
from src.lib.validation import (
    validate_mapping_completeness,
)


def build_dimensions_hierarchy(config: MaterConfig, example: bool = False) -> None:
    """
    # Build final dimensions hierarchy from mapping file

    ## Arguments
    - `config` (MaterConfig): Configuration object containing paths and simulation parameters
    - `example` (bool): Whether using example data

    ## Returns
    - `None`: Creates final hierarchy file but doesn't return a value
    """

    try:
        dimensions_mapping = load_mapping_file(config.paths.dimensions_mapping_file)

        validation_result = validate_mapping_completeness(dimensions_mapping)
        display_mapping_validation(validation_result)

        if not validation_result["can_proceed"]:
            return

        complete_hierarchy = build_complete_hierarchy_from_mapping(dimensions_mapping)

        save_hierarchy_file(complete_hierarchy, config.paths.dimensions_hierarchy_file)

        click.echo(
            f"📊 Built hierarchy with {len(complete_hierarchy)} dimension values"
        )
        click.echo("🎯 Complete hierarchy generated!")
        display_elegant_hierarchy(complete_hierarchy)

    except FileNotFoundError as e:
        click.echo(f"⚠️  File not found: {e}")
        if "dimensions_mapping" in str(e):
            click.echo("💡 Create the mapping first:")
            if example:
                click.secho(
                    "   uv run mater-cli dimensions map --example",
                    fg="bright_blue",
                    bold=True,
                )
            else:
                click.secho(
                    "   uv run mater-cli dimensions map", fg="bright_blue", bold=True
                )
    except json.JSONDecodeError as e:
        click.echo(f"⚠️  Invalid JSON format: {e}")
    except PermissionError:
        click.echo("⚠️  Permission denied")
    except Exception as e:
        click.echo(f"⚠️  Error building dimensions hierarchy: {e}")


def display_mapping_validation(validation_result: Dict) -> None:
    """
    # Display mapping validation status and guidance

    ## Arguments
    - `validation_result` (Dict): Validation result from validate_mapping_completeness

    ## Returns
    - `None`: Displays validation status but doesn't return a value
    """
    mapped = validation_result["mapped"]
    todo = validation_result["todo"]
    completion_rate = validation_result["completion_rate"]

    click.echo("📋 Mapping validation:")
    click.echo(f"   ✅ {mapped} dimensions mapped ({completion_rate:.1f}%)")

    if todo > 0:
        click.echo(f"   ❌ {todo} dimensions with TODOs")
        click.echo("\n⚠️  Cannot build hierarchy with incomplete mapping!")
        click.echo("💡 Complete TODOs in mapping file:")
        click.echo("      - Remove TODO keys and fill with real data")
        click.echo(
            "      - Check out existing dimensions values: data/references/dimensions.json"
        )
    else:
        click.echo("   🎯 Mapping complete! Building hierarchy...")


def display_elegant_hierarchy(complete_hierarchy: List[Dict]) -> None:
    """
    # Display complete hierarchy in elegant tree format

    ## Arguments
    - `complete_hierarchy` (List[Dict]): Complete validated hierarchy

    ## Returns
    - `None`: Displays hierarchy but doesn't return a value
    """
    dimensions_by_name = {}
    for entry in complete_hierarchy:
        name = entry.get("name", "unknown")
        if name not in dimensions_by_name:
            dimensions_by_name[name] = []
        dimensions_by_name[name].append(entry)

    click.echo("\n🌳 Complete Hierarchy:")

    for dim_name, entries in dimensions_by_name.items():
        click.echo(f"\n📁 {dim_name.capitalize()}:")

        tree_structure = build_hierarchy_tree(entries)
        if tree_structure:
            display_tree_structure(tree_structure, "   ")
        else:
            click.echo("   (No hierarchical structure found)")


def display_tree_structure(tree: Dict, indent: str = "") -> None:
    """
    # Display tree structure with elegant formatting

    ## Arguments
    - `tree` (Dict): Tree structure to display
    - `indent` (str): Current indentation level

    ## Returns
    - `None`: Displays tree but doesn't return a value
    """
    if not tree:
        return

    items = list(tree.items())

    for i, (value, subtree) in enumerate(items):
        is_last = i == len(items) - 1
        current_prefix = indent + ("└── " if is_last else "├── ")
        next_indent = indent + ("    " if is_last else "│   ")

        click.echo(f"{current_prefix}{value}")

        if subtree.get("children"):
            display_tree_structure(subtree["children"], next_indent)


def load_mapping_file(mapping_file: Path) -> List[Dict]:
    """
    # Load dimensions mapping from JSON file

    ## Arguments
    - `mapping_file` (Path): Path to mapping JSON file

    ## Returns
    - `List[Dict]`: Dimensions mapping data
    """
    if not mapping_file.exists():
        raise FileNotFoundError(f"Mapping file not found: {mapping_file}")

    try:
        with open(mapping_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError(f"Mapping file must contain an array, got: {type(data)}")

        click.echo(f"📁 Loaded mapping: {mapping_file} ({len(data)} entries)")
        return data

    except json.JSONDecodeError as e:
        click.echo(f"❌ Invalid JSON in mapping file: {mapping_file}")
        click.echo(f"   Error: {e.msg} at line {e.lineno}, column {e.colno}")
        raise json.JSONDecodeError(
            f"Invalid JSON in mapping file {mapping_file}", e.doc, e.pos
        )


def save_hierarchy_file(complete_hierarchy: List[Dict], output_file: Path) -> None:
    """
    # Save complete hierarchy to JSON file with user confirmation if exists

    ## Arguments
    - `complete_hierarchy` (List[Dict]): Complete dimension hierarchy data
    - `output_file` (Path): Output file path

    ## Returns
    - `None`: Saves file but doesn't return a value
    """
    if output_file.exists():
        response = input(f"File '{output_file}' already exists. Overwrite? (y/N): ")
        if response.lower() not in ["y", "yes"]:
            click.echo(f"Skipped: {output_file}")
            return

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(complete_hierarchy, f, indent=2, ensure_ascii=False)

    click.echo(f"✅ Generated dimensions hierarchy: {output_file}")


def load_reference_dimensions(reference_path: Path) -> List[Dict]:
    """
    # Load reference dimensions from JSON file

    ## Arguments
    - `reference_path` (Path): Path to reference dimensions JSON file

    ## Returns
    - `List[Dict]`: Reference dimensions data
    """
    if not reference_path.exists():
        return []

    try:
        with open(reference_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            return []

        return data

    except json.JSONDecodeError:
        return []
