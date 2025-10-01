"""OPPM - One-file Package Manager for managing portable applications."""

from .cli import main
from .exceptions import (
    AppNotFoundError,
    ConfigError,
    InstallError,
    InvalidInputError,
    MetaFileError,
    MigrationError,
    OPPMError,
    ShimError,
)

__version__ = "0.1.1"

__all__ = [
    "main",
    "OPPMError",
    "MetaFileError",
    "AppNotFoundError",
    "ConfigError",
    "ShimError",
    "InstallError",
    "InvalidInputError",
    "MigrationError",
]
