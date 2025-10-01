"""Configuration management for OPPM."""

from pathlib import Path
from typing import TYPE_CHECKING, NamedTuple, cast

import tomlkit
from tomlkit import document, table

from .exceptions import ConfigError

if TYPE_CHECKING:
    from tomlkit.items import Table


CONFIG_FILE = Path.home() / ".oppmconfig"


class OPPMConfig(NamedTuple):
    """OPPM configuration data."""

    root_dir: Path
    apps_dir: Path
    meta_file: Path

    @property
    def shims_dir(self) -> Path:
        """Get the shims directory path."""
        return self.root_dir / "shims"


def load_config() -> OPPMConfig:
    """Load configuration from the config file.

    Returns:
        OPPMConfig: The loaded configuration.

    Raises:
        ConfigError: If config file doesn't exist or is invalid.
    """
    if not CONFIG_FILE.exists():
        raise ConfigError(f"Configuration file does not exist: {CONFIG_FILE}. Please run 'oppm init' first.")

    try:
        with CONFIG_FILE.open("r", encoding="utf-8") as f:
            config_doc: tomlkit.TOMLDocument = tomlkit.load(f)
            config_table = cast("Table", config_doc["config"])

            return OPPMConfig(
                root_dir=Path(str(config_table["root_dir"])).resolve(),
                apps_dir=Path(str(config_table["apps_dir"])).resolve(),
                meta_file=Path(str(config_table["meta_file"])).resolve(),
            )
    except (FileNotFoundError, KeyError, OSError) as e:
        raise ConfigError(f"Failed to load configuration: {e}. You may need to run 'oppm init' again.") from e


def save_config(config: OPPMConfig) -> None:
    """Save configuration to the config file.

    Args:
        config: The configuration to save.

    Raises:
        ConfigError: If saving fails.
    """
    try:
        doc = document()
        config_table = table()
        config_table.add("root_dir", str(config.root_dir))
        config_table.add("apps_dir", str(config.apps_dir))
        config_table.add("meta_file", str(config.meta_file))
        doc.add("config", config_table)

        CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with CONFIG_FILE.open("w", encoding="utf-8") as f:
            tomlkit.dump(doc, f)
    except (OSError, Exception) as e:
        raise ConfigError(f"Failed to save configuration: {e}") from e


def update_config(config: OPPMConfig) -> None:
    """Update existing configuration file.

    Args:
        config: The new configuration values.

    Raises:
        ConfigError: If update fails.
    """
    try:
        with CONFIG_FILE.open("r+", encoding="utf-8") as f:
            config_doc: tomlkit.TOMLDocument = tomlkit.load(f)
            config_table = cast("Table", config_doc["config"])

            config_table["root_dir"] = str(config.root_dir)
            config_table["apps_dir"] = str(config.apps_dir)
            config_table["meta_file"] = str(config.meta_file)

            f.seek(0)
            f.truncate()
            tomlkit.dump(config_doc, f)
    except (FileNotFoundError, KeyError, OSError) as e:
        raise ConfigError(
            f"Failed to update configuration file '{CONFIG_FILE}'. Please manually update it. Error: {e}"
        ) from e
