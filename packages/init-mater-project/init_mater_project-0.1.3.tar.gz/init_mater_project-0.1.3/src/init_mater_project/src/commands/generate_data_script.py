"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

from pathlib import Path
from typing import List, Optional

import click
from jinja2 import Environment, FileSystemLoader

from src.settings import MaterConfig


def generate_data_script(config: MaterConfig) -> None:
    """
    # Create script(s) to transform dataset file(s) in MATER-formatted data with provided configuration

    ## Arguments
    - `config` (MaterConfig): Configuration object containing paths and simulation parameters

    ## Returns
    - `None`: Creates Python scripts in transforms_script_path directory but doesn't return a value
    """

    try:
        dataset_files = load_dataset_files(config.paths.raw_path)

        if not dataset_files:
            click.echo(
                f"❌ Error: No supported dataset files found in {config.paths.raw_path}"
            )
            click.echo(
                "Supported formats: json, csv, xlsx, parquet, pickle, tsv, yaml, xml"
            )
            return

        scripts_created = 0
        for dataset_file in dataset_files:
            file_format = detect_file_format(dataset_file)
            if not file_format:
                click.echo(f"Skipping unsupported format: {dataset_file}")
                continue

            script_name = dataset_file.stem

            loading_imports = get_required_imports(file_format)
            transform_imports = get_transform_imports()
            all_imports = organize_imports(loading_imports + transform_imports)

            provider_info = config.provider_info
            metadata_info = config.metadata_info

            script_content = f'''"""
Data processing script for dataset: {script_name}
Generated automatically - customize the transformation logic as needed
Source file: {dataset_file}
"""

{all_imports}

{get_transform_template(provider_info, metadata_info).replace("# PLACEHOLDER_LOADING_CODE", get_loading_template(file_format, str(dataset_file)))}
'''

            script_file = config.paths.transforms_script_path / f"{script_name}.py"

            if script_file.exists():
                response = input(
                    f"Script '{script_file}' already exists. Overwrite? (y/N): "
                )
                if response.lower() not in ["y", "yes"]:
                    click.echo(f"Skipped: {script_file}")
                    continue

            script_file.write_text(script_content, encoding="utf-8")
            scripts_created += 1
            click.echo(f"Generated script: {script_file}")

        if scripts_created > 0:
            click.echo(f"\n✅ Generated {scripts_created} script(s) successfully")
            click.echo("\n💡 Remember to:")
            click.echo("   - Adjust data loading logic in main()")
            click.echo(
                "   - Customize transformation logic in transform_to_mater_format()"
            )
            click.echo(
                "   - Provider and metadata info are pre-filled from your config"
            )

    except FileNotFoundError as e:
        if "Templates directory not found" in str(e):
            click.echo("❌ Error: Templates directory not found")
        elif "template not found" in str(e):
            click.echo("❌ Error: Required template file missing")
        else:
            click.echo(f"❌ Error: File not found - {e}")
    except PermissionError:
        click.echo("❌ Error: Permission denied")
    except Exception as e:
        click.echo(f"❌ Error creating scripts: {e}")


def load_dataset_files(path: Path) -> List[Path]:
    """
    # Find all supported dataset files in specified path (file or directory)

    ## Arguments
    - `path` (Path): File path or directory path to search for dataset files

    ## Returns
    - `List[Path]`: List of Path objects for supported dataset files found
    """
    supported_extensions = {
        ".json",
        ".csv",
        ".xlsx",
        ".xls",
        ".parquet",
        ".pickle",
        ".pkl",
        ".tsv",
        ".yaml",
        ".yml",
        ".xml",
    }

    if path.is_file():
        if path.suffix.lower() in supported_extensions:
            click.echo(f"Found dataset file: {path}")
            return [path]
        else:
            return []

    elif path.is_dir():
        dataset_files = [
            f for f in path.rglob("*") if f.suffix.lower() in supported_extensions
        ]

        if dataset_files:
            click.echo(f"Found dataset files in folder: {path}")
            for file_path in dataset_files:
                relative_path = file_path.relative_to(path)
                click.echo(f"  - {relative_path}")

        return dataset_files

    else:
        return []


def detect_file_format(file_path: Path) -> Optional[str]:
    """
    # Detect file format based on extension and validate file existence

    ## Arguments
    - `file_path` (Path): Path to the file to analyze

    ## Returns
    - `Optional[str]`: String identifier for the file format, or None if unsupported/missing
    """
    if not file_path.exists():
        return None

    suffix = file_path.suffix.lower()
    match suffix:
        case ".json":
            return "json"
        case ".csv":
            return "csv"
        case ".xlsx" | ".xls":
            return "excel"
        case ".parquet":
            return "parquet"
        case ".pickle" | ".pkl":
            return "pickle"
        case ".tsv":
            return "tsv"
        case ".yaml" | ".yml":
            return "yaml"
        case ".xml":
            return "xml"
        case _:
            return None


def get_required_imports(file_format: str) -> List[str]:
    """
    # Get required import statements for specific file format processing

    ## Arguments
    - `file_format` (str): File format identifier (json, csv, excel, etc.)

    ## Returns
    - `List[str]`: List of import statements needed for the file format
    """
    import_map = {
        "json": ["import json", "import pandas as pd"],
        "csv": ["import pandas as pd"],
        "excel": ["import pandas as pd"],
        "parquet": ["import pandas as pd"],
        "pickle": ["import pandas as pd", "import pickle"],
        "tsv": ["import pandas as pd"],
        "yaml": ["import yaml", "import pandas as pd"],
        "xml": ["import pandas as pd", "import xml.etree.ElementTree as ET"],
    }
    return import_map.get(file_format, ["import pandas as pd"])


def get_transform_imports() -> List[str]:
    """
    # Get required import statements for data transformation functionality

    ## Arguments
    - None

    ## Returns
    - `List[str]`: List of import statements needed for transformation operations
    """
    return [
        "import json",
        "from pathlib import Path",
        "from src.settings import MaterConfig",
    ]


def organize_imports(import_list: List[str]) -> str:
    """
    # Organize import statements according to PEP8 standards (stdlib, third-party, local)

    ## Arguments
    - `import_list` (List[str]): List of import statements to organize

    ## Returns
    - `str`: Formatted import section with proper PEP8 grouping and spacing
    """

    unique_imports = []
    seen = set()
    for imp in import_list:
        if imp not in seen:
            unique_imports.append(imp)
            seen.add(imp)

    stdlib = []
    third_party = []
    local = []

    for imp in unique_imports:
        if any(lib in imp for lib in ["json", "pathlib", "pickle", "xml"]):
            stdlib.append(imp)
        elif "from settings" in imp:
            local.append(imp)
        else:
            third_party.append(imp)

    sections = []
    if stdlib:
        stdlib_sorted = sorted(stdlib, key=lambda x: (0 if "pathlib" in x else 1, x))
        sections.append("\n".join(stdlib_sorted))
    if third_party:
        sections.append("\n".join(sorted(third_party)))
    if local:
        sections.append("\n".join(sorted(local)))

    return "\n\n".join(sections)


def get_loading_template(file_format: str, dataset_path: str) -> str:
    """
    # Generate loading code template based on file format

    ## Arguments
    - `file_format` (str): File format identifier for template selection
    - `dataset_path` (str): Path to dataset file for template rendering

    ## Returns
    - `str`: Generated loading code specific to the file format
    """
    template_dir = Path("transforms/templates")

    if not template_dir.exists():
        raise FileNotFoundError(f"Templates directory not found: {template_dir}")

    env = Environment(loader=FileSystemLoader(template_dir))

    try:
        template = env.get_template(f"load_{file_format}.py.j2")
        return template.render(dataset_path=dataset_path)
    except Exception as e:
        raise FileNotFoundError(
            f"Loading template not found: {template_dir}/load_{file_format}.py.j2"
        ) from e


def get_transform_template(provider_info: dict, metadata_info: dict) -> str:
    """
    # Generate MATER transformation code template

    ## Arguments
    - provider_info (dict): Provider information from config
    - metadata_info (dict): Metadata information from config

    ## Returns
    - `str`: Generated transformation code template with placeholder for loading code
    """
    template_dir = Path("transforms/templates")

    if not template_dir.exists():
        raise FileNotFoundError(f"Templates directory not found: {template_dir}")

    env = Environment(loader=FileSystemLoader(template_dir))

    try:
        template = env.get_template("transform_data.py.j2")
        return template.render(provider=provider_info, metadata=metadata_info)
    except Exception as e:
        raise FileNotFoundError(
            f"Transform template not found: {template_dir}/transform_data.py.j2"
        ) from e
