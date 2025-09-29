"""
init-mater-project

Copyright (C) 2025 [Lauranne Sarribouette] <lauranne.sarribouette@univ-grenoble-alpes.fr>

SPDX-License-Identifier: LGPL-3.0-or-later
"""

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
    TomlConfigSettingsSource,
    PydanticBaseSettingsSource,
)
from pydantic import Field, field_validator, EmailStr, BaseModel
from pathlib import Path
from typing import Literal, Tuple, Type


class Simulation(BaseModel):
    """Simulation configuration"""

    name: str = Field(
        default="simulation_outputs",
        description="Simulation outputs folder name",
        min_length=1,
    )
    start_time: int = Field(
        default=1900,
        description="Simulation start time (year or timestamp)",
        ge=1000,
        le=3000,
    )
    end_time: int = Field(
        default=2100,
        description="Simulation end time (year or timestamp)",
        ge=1000,
        le=3000,
    )
    frequency: Literal["YS", "MS", "QS", "D"] = Field(
        default="YS", description="Time frequency for simulation"
    )
    scenario: str = Field(
        default="historical", description="Simulation scenario type", min_length=1
    )

    @field_validator("end_time")
    @classmethod
    def validate_time_range(cls, v, info):
        """Ensure end_time is after start_time"""
        if "start_time" in info.data and v <= info.data["start_time"]:
            raise ValueError("end_time must be greater than start_time")
        return v


class Paths(BaseModel):
    """Paths configuration"""

    dimensions_hierarchy_file: Path = Field(
        default=Path("data/dimensions_hierarchy/dimensions_hierarchy.json"),
        description="File that contains the user dimensions hierarchy",
    )
    dimensions_mapping_file: Path = Field(
        default=Path("data/dimensions_hierarchy/dimensions_mapping.json"),
        description="File that contains the user dimensions mapping",
    )
    dimensions_values_path: Path = Field(
        default=Path("data/references/variables_dimensions.json"),
        description="Path to the file or folder that contains the dimensions values used as reference in the simulations",
    )
    input_path: Path = Field(
        default=Path("data/input"),
        description="Path to the file or folder that contains the MATER-formatted input data",
    )
    output_folder: Path = Field(
        default=Path("outputs"),
        description="Path to the folder that contains the simulation outputs",
    )
    raw_path: Path = Field(
        default=Path("data/raw"),
        description="Path to the file or folder that contains the user raw data",
    )
    transforms_script_path: Path = Field(
        default=Path("transforms/datasets"),
        description="Path to the file or folder that contains the transforming scripts for datasets",
    )
    variables_dimensions_path: Path = Field(
        default=Path("data/references/variables_dimensions.json"),
        description="Path to the file or folder that contains the variable-dimensions associations used as reference in the simulations",
    )

    @field_validator("dimensions_hierarchy_file", "dimensions_mapping_file")
    @classmethod
    def validate_json_file(cls, v):
        """Ensure path is JSON file"""
        if v.is_file():
            if v.suffix.lower() != ".json":
                raise ValueError(f"File must be a .json file, got: {v}")
        return v

    @field_validator(
        "dimensions_values_path", "input_path", "raw_path", "variables_dimensions_path"
    )
    @classmethod
    def validate_json_or_folder(cls, v):
        """Ensure path is either a JSON file or a directory"""
        if v.is_file():
            if v.suffix.lower() != ".json":
                raise ValueError(f"File must be a .json file, got: {v}")
        elif not v.is_dir():
            raise ValueError(
                f"Path must be either a JSON file or a directory, got: {v}"
            )
        return v

    @field_validator("transforms_script_path")
    @classmethod
    def validate_python_or_folder(cls, v):
        """Ensure path is either a Python file or a directory"""
        if v.is_file():
            if v.suffix.lower() != ".py":
                raise ValueError(f"File must be a .py file, got: {v}")
        elif not v.is_dir():
            raise ValueError(
                f"Path must be either a Python file or a directory, got: {v}"
            )
        return v

    @field_validator("output_folder")
    @classmethod
    def validate_is_folder(cls, v):
        """Ensure path is an existing directory"""
        if not v.is_dir():
            raise ValueError(f"Path must be an existing directory, got: {v}")
        return v


class Provider(BaseModel):
    """Provider information model"""

    first_name: str = Field(
        default="John", description="Provider first name", min_length=1
    )
    last_name: str = Field(
        default="Doe", description="Provider last name", min_length=1
    )
    email: EmailStr = Field(
        default="john.doe@example.com",
        description="Provider email",
    )


class Metadata(BaseModel):
    """Metadata information model"""

    source: str = Field(
        default="Default Source", description="Source of the dataset(s)", min_length=1
    )
    link: str = Field(
        default="https://example.com/source",
        description="Link to the dataset",
    )
    project: str = Field(
        default="MATER Project", description="Project name", min_length=1
    )

    @field_validator("link")
    @classmethod
    def validate_url_format(cls, v: str) -> str:
        """Basic URL format validation"""
        if not v.startswith(("http://", "https://", "ftp://")):
            raise ValueError(
                "Link must be a valid URL starting with http://, https://, or ftp://"
            )
        return v


class MaterConfig(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        toml_file="config.toml",
        validate_assignment=True,
        validate_default=True,
    )

    simulation: Simulation = Field(default_factory=Simulation)
    paths: Paths = Field(default_factory=Paths)
    provider: Provider = Field(default_factory=Provider)
    metadata: Metadata = Field(default_factory=Metadata)

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        """Configure settings sources priority: Init > TOML > ENV"""
        return (
            init_settings,
            TomlConfigSettingsSource(settings_cls),
            env_settings,
        )

    @property
    def output_path(self) -> Path:
        """Complete output path"""
        return self.paths.output_folder / self.simulation.name

    @property
    def provider_info(self) -> dict:
        """Provider information as dictionary"""
        return {
            "first_name": self.provider.first_name,
            "last_name": self.provider.last_name,
            "email_address": str(self.provider.email),
        }

    @property
    def metadata_info(self) -> dict:
        """Metadata information as dictionary"""
        return {
            "source": self.metadata.source,
            "link": self.metadata.link,
            "project": self.metadata.project,
        }

    def use_example_settings(self, context: str = "default") -> None:
        """Override settings for --example"""
        self.simulation.name = "example_outputs"
        self.simulation.scenario = "example"

        self.paths.dimensions_hierarchy_file = Path(
            "examples/minimal_dimensions_hierarchy.json"
        )
        self.paths.dimensions_mapping_file = Path(
            "examples/minimal_dimensions_mapping.json"
        )
        self.paths.dimensions_values_path = Path("examples/minimal_dimensions.json")
        self.paths.input_path = Path("examples/minimal_example.json")
        self.paths.output_folder = Path("examples")
        self.paths.raw_path = Path("examples/minimal_raw_example.csv")

        if context == "data build":
            self.paths.transforms_script_path = Path(
                "examples/minimal_raw_after_example.py"
            )
        else:
            self.paths.transforms_script_path = Path("examples")

        self.paths.variables_dimensions_path = Path(
            "examples/minimal_variables_dimensions.json"
        )

        self.provider.first_name = "Lauranne"
        self.provider.last_name = "Sarribouette"
        self.provider.email = "lauranne.sarribouette@univ-grenoble-alpes.fr"

        self.metadata.source = "Example Dataset Source"
        self.metadata.link = "https://example.org/dataset"
        self.metadata.project = "Example MATER Project"
