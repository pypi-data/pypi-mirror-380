import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import TYPE_CHECKING, cast

import tomlkit
from tomlkit import document, table

if TYPE_CHECKING:
    from tomlkit.items import Table

TopLevelDir = Path.home() / ".oppmconfig"


class MetaFileError(Exception):
    """Error related to meta.json file operations."""

    pass


class AppNotFoundError(Exception):
    """Raised when the specified application is not found."""

    pass


def _load_meta(meta_file: Path) -> dict[str, list[dict[str, str]]]:
    """Load and return metadata."""
    if not meta_file.exists():
        raise MetaFileError(f"Metadata file does not exist: {meta_file}")
    try:
        with meta_file.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        raise MetaFileError(f"Failed to read or parse metadata file: {e}") from e


def _save_meta(meta_file: Path, meta: dict[str, list[dict[str, str]]]) -> None:
    """Save metadata to file."""
    try:
        with meta_file.open("w", encoding="utf-8") as f:
            json.dump(meta, f, indent=4, ensure_ascii=False)
    except OSError as e:
        raise MetaFileError(f"Failed to write to metadata file: {e}") from e


def _add_app_to_meta(app_name: str, app_dir: Path, meta_file: Path):
    """Add an application entry to metadata."""
    meta = _load_meta(meta_file)
    # Remove any existing entries with the same name to avoid duplicates
    meta["apps"] = [app for app in meta["apps"] if app["name"] != app_name]
    meta["apps"].append({"name": app_name, "path": str(app_dir)})
    _save_meta(meta_file, meta)
    print(f"Successfully installed {app_name}")


UnaryArchiveTypeSet = {".zip", ".tar", ".tgz", ".tbz2", ".txz"}

BinaryArchiveTypeSet = {".tar.gz", ".tar.bz2", ".tar.xz"}


def _extract_app_name(input_path: Path) -> str:
    """Extract the application name from the input path."""
    if input_path.is_dir():
        return input_path.name
    elif input_path.is_file():
        if input_path.suffix == ".exe":
            return input_path.stem
        elif input_path.suffix in UnaryArchiveTypeSet:
            return input_path.stem
        elif any(s for s in BinaryArchiveTypeSet if str(input_path).endswith(s)):
            return Path(input_path.stem).stem
        else:
            raise ValueError(f"Unsupported input type: {input_path}")
    else:
        raise ValueError(f"Unsupported input type: {input_path}")


# --- Core Functions ---
def install(input_path: Path, apps_dir: Path, meta_file: Path, name: str | None):
    """Install an application."""
    if not input_path.exists():
        raise FileNotFoundError(f"Input file or directory does not exist: {input_path}")
    # [NOTE] Why first call this function?
    # Now, explicitly check the input path style rather than assume it's a supported archive file.
    app_name = _extract_app_name(input_path)
    if name is not None:
        app_name = name
    app_dir = apps_dir / app_name

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
                # Assume it's an archive file, because we check it in _extract_app_name.
                shutil.unpack_archive(input_path, app_dir)
        else:
            raise ValueError(f"Unsupported input type: {input_path}")
    except Exception as e:
        # If installation fails, clean up the created directory
        if app_dir.exists():
            shutil.rmtree(app_dir)
        raise OSError(f"Failed to install '{app_name}': {e}") from e

    _add_app_to_meta(app_name, app_dir, meta_file)


def list_apps(meta_file: Path):
    """List all installed applications."""
    meta = _load_meta(meta_file)
    if not meta["apps"]:
        print("No applications installed.")
        return
    print("Installed applications:")
    for app in sorted(meta["apps"], key=lambda x: x["name"]):
        print(f"- {app['name']}")


def remove(app_name: str, apps_dir: Path, meta_file: Path):
    """Remove a specified application."""
    meta = _load_meta(meta_file)
    apps_to_keep = [app for app in meta["apps"] if app["name"] != app_name]

    if len(apps_to_keep) == len(meta["apps"]):
        print(
            "Warning: Application '{app_name}' not found in metadata. Maybe you can call 'oppm update' to update the metadata first."
        )
        raise AppNotFoundError(f"Application '{app_name}' not found in metadata.")

    meta["apps"] = apps_to_keep
    _save_meta(meta_file, meta)

    app_dir = apps_dir / app_name
    if app_dir.exists():
        shutil.rmtree(app_dir)
        print(f"Successfully removed application directory: {app_dir}")
    else:
        print(f"Warning: Application directory '{app_dir}' does not exist, may have been manually deleted.")

    print(f"Successfully removed {app_name}")


def update(apps_dir: Path, meta_file: Path):
    try:
        truth_apps_set = {app.name for app in apps_dir.iterdir() if app.is_dir()}
        meta = _load_meta(meta_file)
        meta_apps_set = {app["name"] for app in meta["apps"]}
    except FileNotFoundError:
        print("Application directory or metadata file does not exist, cannot update.")
        return

    apps_to_add = truth_apps_set - meta_apps_set
    if apps_to_add:
        print(f"Found {len(apps_to_add)} apps need to be added:  {apps_to_add}")
        for app_name in apps_to_add:
            meta["apps"].append({"name": app_name, "path": str(apps_dir / app_name)})

    apps_to_remove = meta_apps_set - truth_apps_set
    if apps_to_remove:
        print(f"Found {len(apps_to_remove)} apps need to be removed:  {apps_to_remove}")
        meta["apps"] = [app for app in meta["apps"] if app["name"] not in apps_to_remove]

    if not apps_to_add and not apps_to_remove:
        print("No changes found.")
        return

    _save_meta(meta_file, meta)
    print("Update complete")


def clean(apps_dir: Path, meta_file: Path):
    if apps_dir.exists():
        for item in apps_dir.iterdir():
            print(f"Removing {item.name} ...")
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
    _save_meta(meta_file, {"apps": []})
    print("Cleaning complete")


def init(root_dir: Path, apps_dir: Path, meta_file: Path):
    root_dir.mkdir(exist_ok=True)
    apps_dir.mkdir(exist_ok=True)
    if not meta_file.exists():
        print("Creating meta.json ...")
        _save_meta(meta_file, {"apps": []})
    doc = document()
    config = table()
    config.add("root_dir", str(root_dir))
    config.add("apps_dir", str(apps_dir))
    config.add("meta_file", str(meta_file))
    doc.add("config", config)
    with TopLevelDir.open("w", encoding="utf-8") as f:
        tomlkit.dump(doc, f)
    print("Initialization complete")


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="mode", required=True, help="Mode to run OPPM")

    subparsers.add_parser("list", help="List all installed apps")

    parser_install = subparsers.add_parser("install", help="Install an app")
    parser_install.add_argument("input_path", type=Path, help="Path to the app to install")
    parser_install.add_argument("-n", "--name", type=str, help="Name of the app")

    parser_remove = subparsers.add_parser("remove", help="Remove an app")
    parser_remove.add_argument("app_name", type=str, help="Name of the app to remove")

    subparsers.add_parser("update", help="Update apps dir and meta.json")

    parser_init = subparsers.add_parser("init", help="Initialize OPPM dir and meta.json")
    parser_init.add_argument(
        "-r",
        "--root_dir",
        default=Path.home() / ".oppm",
        type=Path,
        help="Root directory for OPPM. (Default: ~/.oppm)",
    )

    subparsers.add_parser("clean", help="Clean apps dir and meta.json")

    args = parser.parse_args()

    if args.mode == "init":
        try:
            args.root_dir.mkdir(parents=True, exist_ok=True)
            init(args.root_dir, args.root_dir / "apps", args.root_dir / "meta.json")
        except OSError as e:
            print(f"Error during initialization: {e}", file=sys.stderr)
            sys.exit(1)
        return

    try:
        if not TopLevelDir.exists():
            print("Error: OPPM is not initialized. Please run 'oppm init' first.", file=sys.stderr)
            sys.exit(1)

        with TopLevelDir.open("r", encoding="utf-8") as f:
            config: tomlkit.TOMLDocument = tomlkit.load(f)

            config_table = cast("Table", config["config"])
            apps_dir = Path(str(config_table["apps_dir"])).resolve()
            meta_file = Path(str(config_table["meta_file"])).resolve()
    except (FileNotFoundError, KeyError, OSError) as e:
        print(f"Error loading configuration: {e}. You may need to run 'oppm init' again.", file=sys.stderr)
        sys.exit(1)

    try:
        if args.mode == "list":
            list_apps(meta_file)
        elif args.mode == "install":
            install(args.input_path, apps_dir, meta_file, args.name)
        elif args.mode == "remove":
            remove(args.app_name, apps_dir, meta_file)
        elif args.mode == "update":
            update(apps_dir, meta_file)
        elif args.mode == "clean":
            clean(apps_dir, meta_file)
    except (
        MetaFileError,
        AppNotFoundError,
        FileNotFoundError,
        ValueError,
        OSError,
    ) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
