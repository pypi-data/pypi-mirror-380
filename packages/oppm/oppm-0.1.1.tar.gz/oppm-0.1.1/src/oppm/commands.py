"""Command implementations for OPPM."""

import platform
import shutil
from pathlib import Path

from .config import OPPMConfig, save_config, update_config
from .exceptions import (
    AppNotFoundError,
    InstallError,
    InvalidInputError,
    MigrationError,
)
from .metadata import (
    add_app_to_metadata,
    load_metadata,
    remove_app_from_metadata,
    save_metadata,
)
from .shims import create_shim, list_shims, remove_shims_for_app

# Supported archive formats
UNARY_ARCHIVE_TYPES = {".zip", ".tar", ".tgz", ".tbz2", ".txz"}
BINARY_ARCHIVE_TYPES = {".tar.gz", ".tar.bz2", ".tar.xz"}


def extract_app_name(input_path: Path) -> str:
    """Extract the application name from the input path.

    Args:
        input_path: Path to the input (file or directory).

    Returns:
        str: Extracted application name.

    Raises:
        InvalidInputError: If the input type is not supported.
    """
    if input_path.is_dir():
        return input_path.name
    elif input_path.is_file():
        if input_path.suffix == ".exe":
            return input_path.stem
        elif input_path.suffix in UNARY_ARCHIVE_TYPES:
            return input_path.stem
        elif any(str(input_path).endswith(s) for s in BINARY_ARCHIVE_TYPES):
            return Path(input_path.stem).stem
        else:
            raise InvalidInputError(
                f"Unsupported file type: {input_path.suffix}. "
                f"Supported types: .exe, {', '.join(UNARY_ARCHIVE_TYPES | BINARY_ARCHIVE_TYPES)}"
            )
    else:
        raise InvalidInputError(f"Input path does not exist or is not a file/directory: {input_path}")


def install_app(input_path: Path, config: OPPMConfig, custom_name: str | None = None) -> None:
    """Install an application.

    Args:
        input_path: Path to the application (file or directory).
        config: OPPM configuration.
        custom_name: Optional custom name for the application.

    Raises:
        InvalidInputError: If input path doesn't exist or type is not supported.
        InstallError: If installation fails.
    """
    if not input_path.exists():
        raise InvalidInputError(f"Input file or directory does not exist: {input_path}")

    app_name = extract_app_name(input_path)
    if custom_name:
        app_name = custom_name
    app_dir = config.apps_dir / app_name

    # Remove old version if exists
    if app_dir.exists():
        print(f"Application '{app_name}' already exists. Removing old version...")
        shutil.rmtree(app_dir)

    try:
        if input_path.is_dir():
            shutil.copytree(input_path, app_dir)
        elif input_path.is_file():
            app_dir.mkdir(parents=True, exist_ok=True)
            if input_path.suffix == ".exe":
                shutil.copy(input_path, app_dir)
            else:
                # It's an archive file (validated in extract_app_name)
                shutil.unpack_archive(input_path, app_dir)
        else:
            raise InvalidInputError(f"Unsupported input type: {input_path}")
    except InvalidInputError:
        # Re-raise our custom exceptions
        raise
    except Exception as e:
        # Clean up on failure
        if app_dir.exists():
            shutil.rmtree(app_dir)
        raise InstallError(f"Failed to install '{app_name}': {e}") from e

    add_app_to_metadata(app_name, app_dir, config.meta_file)
    print(f"Successfully installed {app_name}")


def list_apps(config: OPPMConfig) -> None:
    """List all installed applications.

    Args:
        config: OPPM configuration.
    """
    meta = load_metadata(config.meta_file)
    if not meta["apps"]:
        print("No applications installed.")
        return

    print("Installed applications:")
    for app in sorted(meta["apps"], key=lambda x: x["name"]):
        print(f"  - {app['name']}")


def remove_app(app_name: str, config: OPPMConfig) -> None:
    """Remove a specified application.

    Args:
        app_name: Name of the application to remove.
        config: OPPM configuration.

    Raises:
        AppNotFoundError: If application is not found.
    """
    # Remove from metadata
    removed = remove_app_from_metadata(app_name, config.meta_file)

    if not removed:
        raise AppNotFoundError(
            f"Application '{app_name}' not found in metadata. "
            "Maybe you can call 'oppm update' to update the metadata first."
        )

    # Remove shims
    app_dir = config.apps_dir / app_name
    remove_shims_for_app(app_dir, config.shims_dir)

    # Remove directory
    if app_dir.exists():
        shutil.rmtree(app_dir)
        print(f"Successfully removed application directory: {app_dir}")
    else:
        print(f"Warning: Application directory '{app_dir}' does not exist, may have been manually deleted.")

    print(f"Successfully removed {app_name}")


def update_metadata(config: OPPMConfig) -> None:
    """Synchronize metadata with actual installed apps.

    Args:
        config: OPPM configuration.
    """
    if not config.apps_dir.exists():
        print("Application directory does not exist, cannot update.")
        return

    try:
        # Get actual apps from filesystem
        actual_apps = {app.name for app in config.apps_dir.iterdir() if app.is_dir()}

        # Get apps from metadata
        meta = load_metadata(config.meta_file)
        meta_apps = {app["name"] for app in meta["apps"]}
    except FileNotFoundError:
        print("Metadata file does not exist, cannot update.")
        return

    # Find differences
    apps_to_add = actual_apps - meta_apps
    apps_to_remove = meta_apps - actual_apps

    if apps_to_add:
        print(f"Found {len(apps_to_add)} apps to add: {apps_to_add}")
        for app_name in apps_to_add:
            meta["apps"].append({"name": app_name, "path": str(config.apps_dir / app_name)})

    if apps_to_remove:
        print(f"Found {len(apps_to_remove)} apps to remove: {apps_to_remove}")
        meta["apps"] = [app for app in meta["apps"] if app["name"] not in apps_to_remove]

    if not apps_to_add and not apps_to_remove:
        print("No changes found.")
        return

    save_metadata(config.meta_file, meta)
    print("Update complete")


def clean_all(config: OPPMConfig) -> None:
    """Remove all installed applications.

    Args:
        config: OPPM configuration.
    """
    if config.apps_dir.exists():
        for item in config.apps_dir.iterdir():
            print(f"Removing {item.name} ...")
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()

    save_metadata(config.meta_file, {"apps": []})
    print("Cleaning complete")


def initialize(root_dir: Path) -> None:
    """Initialize OPPM directories and configuration.

    Args:
        root_dir: Root directory for OPPM.

    Raises:
        ConfigError: If configuration save fails.
        MetaFileError: If metadata file creation fails.
    """
    apps_dir = root_dir / "apps"
    meta_file = root_dir / "meta.json"
    shims_dir = root_dir / "shims"

    # Create directories
    root_dir.mkdir(parents=True, exist_ok=True)
    apps_dir.mkdir(exist_ok=True)
    shims_dir.mkdir(exist_ok=True)

    # Create metadata file
    if not meta_file.exists():
        print("Creating meta.json ...")
        save_metadata(meta_file, {"apps": []})

    # Save configuration
    config = OPPMConfig(root_dir=root_dir, apps_dir=apps_dir, meta_file=meta_file)
    save_config(config)

    print("Initialization complete")
    _print_path_instructions(shims_dir)


def migrate_root(old_root_dir: Path, new_root_dir: Path) -> None:
    """Migrate OPPM to a new root directory.

    Args:
        old_root_dir: Current root directory.
        new_root_dir: New root directory.

    Raises:
        MigrationError: If old root doesn't exist, new root is not empty, or migration fails.
    """
    if not old_root_dir.exists():
        raise MigrationError(f"Old root directory does not exist: {old_root_dir}")

    old_root_resolved = old_root_dir.resolve()
    new_root_resolved = new_root_dir.resolve()

    if old_root_resolved == new_root_resolved:
        print("Source and destination are the same. Nothing to do.")
        return

    if new_root_dir.exists():
        if any(new_root_dir.iterdir()):
            raise MigrationError(f"Target directory '{new_root_dir}' exists and is not empty. Please remove it first.")
        shutil.rmtree(new_root_dir)

    print(f"Migrating from '{old_root_dir}' to '{new_root_dir}' ...")

    try:
        shutil.move(str(old_root_dir), str(new_root_dir))
    except Exception as e:
        raise MigrationError(f"Failed to move directory: {e}") from e

    # Update paths in metadata
    new_meta_file = new_root_dir / "meta.json"
    new_apps_dir = new_root_dir / "apps"

    try:
        meta = load_metadata(new_meta_file)
        for app in meta["apps"]:
            app["path"] = str(new_apps_dir / app["name"])
        save_metadata(new_meta_file, meta)
        print("Updated paths in meta.json.")
    except Exception as e:
        print(f"Warning: Could not update meta.json. You may need to run 'oppm update'. Reason: {e}")

    # Update configuration file
    new_config = OPPMConfig(
        root_dir=new_root_dir,
        apps_dir=new_apps_dir,
        meta_file=new_meta_file,
    )
    update_config(new_config)
    print("Updated configuration file")

    print("Migration complete!")
    _print_path_instructions(new_root_dir / "shims")


def add_executable(exe_path: Path, exe_name: str | None, config: OPPMConfig) -> None:
    """Add an executable to the shims directory.

    Args:
        exe_path: Path to the executable.
        exe_name: Optional custom name for the shim.
        config: OPPM configuration.

    Raises:
        InvalidInputError: If executable doesn't exist.
        ShimError: If shim creation fails.
    """
    if not exe_path.exists():
        raise InvalidInputError(f"Executable not found: {exe_path}")

    shim_name = exe_name if exe_name else exe_path.name

    print("Creating shim...")
    create_shim(exe_path, shim_name, config.shims_dir)
    print(f"Successfully added {shim_name}")


def delete_executable(exe_path: Path, config: OPPMConfig) -> None:
    """Remove shims for an executable.

    Args:
        exe_path: Path to the executable.
        config: OPPM configuration.

    Raises:
        InvalidInputError: If executable doesn't exist.
    """
    if not exe_path.exists():
        raise InvalidInputError(f"Executable not found: {exe_path}")

    # Remove shims that point to this executable
    remove_shims_for_app(exe_path.parent, config.shims_dir)
    print(f"Successfully deleted shims for {exe_path.name}")


def show_shims(config: OPPMConfig) -> None:
    """Display all shims in the shims directory.

    Args:
        config: OPPM configuration.
    """
    shims = list_shims(config.shims_dir)

    if not shims:
        print("No shims found.")
        return

    print("Installed shims:")
    for shim_name, target in shims:
        print(f"  - {shim_name} -> {target}")


def _print_path_instructions(shims_dir: Path) -> None:
    """Print instructions for adding shims directory to PATH.

    Args:
        shims_dir: Path to the shims directory.
    """
    print("\n--- IMPORTANT NEXT STEP ---")
    print("To complete the setup, you need to add the shims directory to your system's PATH.")
    print(
        "Please add the following line to your shell's configuration file "
        "(e.g., .zshrc, .bashrc, or PowerShell profile):\n"
    )

    current_os = platform.system()

    if current_os == "Windows":
        print(f'  $env:PATH += ";{shims_dir.resolve()}"')
        print("\nThen, restart your terminal for the changes to take effect.")
    elif current_os in ["Linux", "Darwin"]:  # Darwin is macOS
        print(f'  export PATH="{shims_dir.resolve()}:$PATH"')
        print("\nThen, run 'source ~/.your_shell_rc_file' or restart your terminal.")
    else:
        print(f"Your OS ({current_os}) is not automatically detected. Please add this path to your PATH manually:")
        print(f"  {shims_dir.resolve()}")
