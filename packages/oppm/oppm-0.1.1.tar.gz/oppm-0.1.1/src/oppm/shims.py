"""Shim management for OPPM."""

import sys
from pathlib import Path

from .exceptions import ShimError


def create_shim(execute_path: Path, shim_name: str, shims_dir: Path) -> None:
    """Create a shim for an executable.

    Args:
        execute_path: Path to the executable.
        shim_name: Name of the shim to create.
        shims_dir: Directory where shims are stored.

    Raises:
        ShimError: If shim creation fails.
    """
    shims_dir.mkdir(parents=True, exist_ok=True)
    shim_path = shims_dir / shim_name

    if shim_path.exists():
        raise ShimError(f"Shim '{shim_name}' already exists at {shim_path}")

    try:
        # Fixed: Correct symlink parameter order
        shim_path.symlink_to(execute_path.resolve())
        print(f"  Created shim: {shim_path} -> {execute_path}")
    except (OSError, AttributeError) as e:
        raise ShimError(
            f"Failed to create shim for {execute_path}: {e}\n"
            "  On Windows, you may need to run this as an Administrator or enable Developer Mode."
        ) from e


def remove_shims_for_app(app_dir: Path, shims_dir: Path) -> None:
    """Remove all shims associated with a given application.

    Args:
        app_dir: Directory of the application.
        shims_dir: Directory where shims are stored.
    """
    if not shims_dir.exists():
        return

    print("Removing shims...")
    app_dir_resolved = app_dir.resolve()

    for shim_path in shims_dir.iterdir():
        if not shim_path.is_symlink():
            continue

        try:
            target = shim_path.resolve()
            if target.is_relative_to(app_dir_resolved):
                shim_path.unlink()
                print(f"  Removed shim: {shim_path.name}")
        except (OSError, ValueError) as e:
            print(f"  Error removing shim {shim_path.name}: {e}", file=sys.stderr)


def list_shims(shims_dir: Path) -> list[tuple[str, Path]]:
    """List all shims in the shims directory.

    Args:
        shims_dir: Directory where shims are stored.

    Returns:
        List of tuples containing (shim_name, target_path).
    """
    if not shims_dir.exists():
        return []

    shims = []
    for shim_path in shims_dir.iterdir():
        if shim_path.is_symlink():
            try:
                target = shim_path.resolve()
                shims.append((shim_path.name, target))
            except OSError:
                # Skip broken symlinks
                continue

    return sorted(shims, key=lambda x: x[0])
