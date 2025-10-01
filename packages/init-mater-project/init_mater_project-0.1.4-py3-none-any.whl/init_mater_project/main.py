"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

import click
import shutil
from pathlib import Path
from importlib import resources
from jinja2 import Environment, PackageLoader


@click.command()
@click.argument("project_name")
def main(project_name: str):
    """Initialize a new MATER project"""
    create_project(project_name)

    click.echo(f"\n✅ MATER project '{project_name}' initialized!")
    click.echo("\n🚀 Next steps:")
    click.secho(f"   cd {project_name}", fg="bright_blue", bold=True)
    click.secho("   uv sync", fg="bright_blue", bold=True)
    click.echo("\n🎮 Run your first MATER simulation:")
    click.secho(
        "   uv run mater-cli simulation run --example", fg="bright_blue", bold=True
    )


def create_project(project_name: str) -> None:
    """Create MATER project structure"""
    project_path = Path(project_name)

    if project_path.exists():
        click.echo(f"❌ Project '{project_name}' already exists!")
        return

    project_path.mkdir()

    generate_files_from_templates(project_path, project_name)
    copy_static_files(project_path)
    copy_src_package(project_path)
    copy_project_directories(project_path)

    display_project_structure(project_path)


def generate_files_from_templates(project_path: Path, project_name: str) -> None:
    """Generate project files from templates"""
    templates_path = resources.files("init_mater_project") / "templates"

    if not templates_path.is_dir():
        click.echo("⚠ Templates directory not found")
        return

    click.echo("\n...generating project files from templates")

    env = Environment(loader=PackageLoader("init_mater_project", "templates"))

    files_to_generate = [
        ("pyproject.toml.j2", "pyproject.toml"),
        ("README.md.j2", "README.md"),
    ]

    for _, destination in files_to_generate:
        output_file = project_path / destination
        output_file.parent.mkdir(parents=True, exist_ok=True)

    for template_name, destination in files_to_generate:
        template = env.get_template(template_name)
        content = template.render(project_name=project_name)
        (project_path / destination).write_text(content, encoding="utf-8")


def copy_static_files(project_path: Path) -> None:
    """Copy static files directly to project root"""
    static_files_path = resources.files("init_mater_project") / "static_files"

    if not static_files_path.is_dir():
        click.echo("⚠ Static files directory not found")
        return

    click.echo("...copying static files to project root")

    for item in static_files_path.iterdir():
        destination = project_path / item.name

        try:
            if item.is_file():
                destination.write_bytes(item.read_bytes())
            elif item.is_dir():
                shutil.copytree(item, destination, dirs_exist_ok=True)
        except Exception as e:
            click.echo(f"⚠ Error copying {item.name}: {e}")


def copy_src_package(project_path: Path) -> None:
    """Copy commands package directly to project"""
    commands_path = resources.files("init_mater_project") / "src"

    if not commands_path.is_dir():
        click.echo("⚠ Commands directory not found")
        return

    click.echo("...copying commands package")

    destination = project_path / "src"

    try:
        shutil.copytree(commands_path, destination, dirs_exist_ok=True)
    except Exception as e:
        click.echo(f"⚠ Error copying commands: {e}")


def copy_project_directories(project_path: Path) -> None:
    """Copy project directories"""
    directories_to_copy = ["data", "transforms", "outputs", "examples"]

    click.echo("...setting up project directory structure")

    for directory in directories_to_copy:
        source_path = resources.files("init_mater_project") / directory

        if source_path.is_dir():
            destination = project_path / directory
            try:
                shutil.copytree(source_path, destination, dirs_exist_ok=True)
            except Exception as e:
                click.echo(f"⚠ Error copying {directory}: {e}")
        else:
            click.echo(f"⚠ Directory {directory} not found in package")


def display_project_structure(project_path: Path) -> None:
    """Display the complete project structure"""
    _display_directory_tree(project_path, project_path.name)


def _display_directory_tree(path: Path, name: str, prefix: str = "") -> None:
    """Recursively display directory tree"""
    click.echo(f"\n{prefix}{name}/")

    items = [
        item
        for item in path.iterdir()
        if not (item.is_file() and item.name == ".gitkeep")
    ]
    items = sorted(items, key=lambda x: (x.is_file(), x.name))

    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        current_prefix = prefix + ("└── " if is_last else "├── ")
        next_prefix = prefix + ("    " if is_last else "│   ")

        if item.is_dir():
            if item.name in ["__pycache__", ".git"]:
                continue
            click.echo(f"{current_prefix}{item.name}/")
            _display_directory_contents(item, next_prefix)
        else:
            click.echo(f"{current_prefix}{item.name}")


def _display_directory_contents(path: Path, prefix: str) -> None:
    """Display contents of a directory"""
    items = [
        item
        for item in path.iterdir()
        if not (item.is_file() and item.name == ".gitkeep")
    ]
    items = sorted(items, key=lambda x: (x.is_file(), x.name))

    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        current_prefix = prefix + ("└── " if is_last else "├── ")
        next_prefix = prefix + ("    " if is_last else "│   ")

        if item.is_dir():
            click.echo(f"{current_prefix}{item.name}/")
            _display_directory_contents(item, next_prefix)
        else:
            click.echo(f"{current_prefix}{item.name}")


if __name__ == "__main__":
    main()
