"""Command-line interface for OPPM (One-file Package Manager)."""

import argparse
import sys
from pathlib import Path

from . import commands
from .config import load_config
from .exceptions import OPPMError


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser.

    Returns:
        argparse.ArgumentParser: Configured parser.
    """
    parser = argparse.ArgumentParser(
        prog="oppm",
        description="OPPM - One-file Package Manager for managing portable applications",
    )

    subparsers = parser.add_subparsers(dest="mode", required=True, help="Command to run")

    # init command
    parser_init = subparsers.add_parser("init", help="Initialize OPPM directories and configuration")
    parser_init.add_argument(
        "-r",
        "--root_dir",
        default=Path.home() / ".oppm",
        type=Path,
        help="Root directory for OPPM (default: ~/.oppm)",
    )

    # list command
    subparsers.add_parser("list", help="List all installed applications")

    # install command
    parser_install = subparsers.add_parser("install", help="Install an application")
    parser_install.add_argument("input_path", type=Path, help="Path to the application to install")
    parser_install.add_argument("-n", "--name", type=str, help="Custom name for the application")

    # remove command
    parser_remove = subparsers.add_parser("remove", help="Remove an application")
    parser_remove.add_argument("app_name", type=str, help="Name of the application to remove")

    # update command
    subparsers.add_parser("update", help="Synchronize metadata with installed applications")

    # clean command
    subparsers.add_parser("clean", help="Remove all installed applications")

    # migrate command
    parser_migrate = subparsers.add_parser("migrate", help="Migrate OPPM to a new root directory")
    parser_migrate.add_argument("new_root_dir", type=Path, help="New root directory for OPPM")

    # exe command group
    parser_exe = subparsers.add_parser("exe", help="Manage executable shims")
    parser_exe_children = parser_exe.add_subparsers(
        dest="exe_mode", required=True, help="Executable management command"
    )

    # exe add
    exe_add_parser = parser_exe_children.add_parser("add", help="Add an executable to the shims directory")
    exe_add_parser.add_argument("exe_path", type=Path, help="Path to the executable")
    exe_add_parser.add_argument("-e", "--exe_name", type=str, help="Custom name for the shim")

    # exe delete
    exe_delete_parser = parser_exe_children.add_parser("delete", help="Remove shims for an executable")
    exe_delete_parser.add_argument("exe_path", type=Path, help="Path to the executable")

    # exe show
    parser_exe_children.add_parser("show", help="Show all shims in the shims directory")

    return parser


def main() -> None:
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args()

    try:
        # Handle init command separately (doesn't require config)
        if args.mode == "init":
            args.root_dir.mkdir(parents=True, exist_ok=True)
            commands.initialize(args.root_dir)
            return

        # Load configuration for all other commands
        config = load_config()

        # Execute commands
        if args.mode == "list":
            commands.list_apps(config)

        elif args.mode == "install":
            commands.install_app(args.input_path, config, args.name)

        elif args.mode == "remove":
            commands.remove_app(args.app_name, config)

        elif args.mode == "update":
            commands.update_metadata(config)

        elif args.mode == "clean":
            commands.clean_all(config)

        elif args.mode == "migrate":
            commands.migrate_root(config.root_dir, args.new_root_dir.resolve())

        elif args.mode == "exe":
            if args.exe_mode == "add":
                commands.add_executable(args.exe_path, args.exe_name, config)
            elif args.exe_mode == "delete":
                commands.delete_executable(args.exe_path, config)
            elif args.exe_mode == "show":
                commands.show_shims(config)

    except OPPMError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
