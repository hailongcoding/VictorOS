from __future__ import annotations

from pathlib import Path
import tomllib
from typing import Any


class ConfigManager:
    """Loads and provides access to JarvisOS configuration."""

    def __init__(self, config_path: str | Path):
        self._path = Path(config_path)
        self._config: dict[str, Any] = {}

    def load(self) -> None:
        """Load the TOML configuration file."""

        if not self._path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self._path}"
            )

        with self._path.open("rb") as file:
            self._config = tomllib.load(file)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Read values using dot notation.

        Example:
            config.get("brain.default_model")
        """

        current: Any = self._config

        for part in key.split("."):
            if not isinstance(current, dict):
                return default

            if part not in current:
                return default

            current = current[part]

        return current

    @property
    def data(self) -> dict[str, Any]:
        """Return the entire configuration."""
        return self._config