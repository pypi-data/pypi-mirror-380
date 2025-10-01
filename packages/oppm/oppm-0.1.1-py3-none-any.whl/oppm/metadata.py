"""Metadata management for OPPM."""

import json
from pathlib import Path
from typing import TypedDict

from .exceptions import MetaFileError


class AppEntry(TypedDict):
    """Application entry in metadata."""

    name: str
    path: str


class Metadata(TypedDict):
    """Metadata structure."""

    apps: list[AppEntry]


def load_metadata(meta_file: Path) -> Metadata:
    """Load and return metadata.

    Args:
        meta_file: Path to the metadata file.

    Returns:
        Metadata: The loaded metadata.

    Raises:
        MetaFileError: If loading fails.
    """
    if not meta_file.exists():
        raise MetaFileError(f"Metadata file does not exist: {meta_file}")

    try:
        with meta_file.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        raise MetaFileError(f"Failed to read or parse metadata file: {e}") from e


def save_metadata(meta_file: Path, meta: Metadata) -> None:
    """Save metadata to file.

    Args:
        meta_file: Path to the metadata file.
        meta: Metadata to save.

    Raises:
        MetaFileError: If saving fails.
    """
    try:
        meta_file.parent.mkdir(parents=True, exist_ok=True)
        with meta_file.open("w", encoding="utf-8") as f:
            json.dump(meta, f, indent=4, ensure_ascii=False)
    except OSError as e:
        raise MetaFileError(f"Failed to write to metadata file: {e}") from e


def add_app_to_metadata(app_name: str, app_dir: Path, meta_file: Path) -> None:
    """Add an application entry to metadata.

    Args:
        app_name: Name of the application.
        app_dir: Directory where the app is installed.
        meta_file: Path to the metadata file.

    Raises:
        MetaFileError: If operation fails.
    """
    meta = load_metadata(meta_file)
    # Remove any existing entries with the same name to avoid duplicates
    meta["apps"] = [app for app in meta["apps"] if app["name"] != app_name]
    meta["apps"].append({"name": app_name, "path": str(app_dir)})
    save_metadata(meta_file, meta)


def remove_app_from_metadata(app_name: str, meta_file: Path) -> bool:
    """Remove an application entry from metadata.

    Args:
        app_name: Name of the application to remove.
        meta_file: Path to the metadata file.

    Returns:
        bool: True if app was found and removed, False otherwise.

    Raises:
        MetaFileError: If operation fails.
    """
    meta = load_metadata(meta_file)
    original_count = len(meta["apps"])
    meta["apps"] = [app for app in meta["apps"] if app["name"] != app_name]

    if len(meta["apps"]) == original_count:
        return False

    save_metadata(meta_file, meta)
    return True
