import json
import sys
from pathlib import Path
from typing import Any

# TOML: prefer stdlib tomllib on 3.11+, fall back to tomli for parsing.
try:
    import tomllib  # Python 3.11+
    _TOML_LOAD = tomllib.load
except Exception:
    import tomli as tomllib  # type: ignore
    _TOML_LOAD = tomllib.load

# For dumping TOML we rely on the third-party tomli_w package.
try:
    import tomli_w

    def _toml_dump(data: dict[str, Any], fp) -> None:
        """Dump TOML data to a text or binary file-like object using tomli-w.

        This wrapper prefers the `dumps()` API (returns str) and writes text.
        If `dumps` isn't available, it falls back to `dump()` which on some
        tomli-w versions writes bytes to a binary file object.
        """
        if hasattr(tomli_w, "dumps"):
            text = tomli_w.dumps(data)
            # fp is expected to be a text file here
            fp.write(text)
        else:
            # Older tomli_w versions might write bytes; caller should open binary
            tomli_w.dump(data, fp)

    _HAS_TOMLI_W = True
except Exception:
    _toml_dump = None  # type: ignore
    _HAS_TOMLI_W = False


class ConfigSerializer:
    """Base class for config serializers."""

    def load(self, path: Path) -> dict[str, Any]:
        raise NotImplementedError

    def dump(self, data: dict[str, Any], path: Path) -> None:
        raise NotImplementedError

    def extension(self) -> str:
        raise NotImplementedError


class TOMLSerializer(ConfigSerializer):
    """Serializer for TOML configuration files."""

    def load(self, path: Path) -> dict[str, Any]:
        """Load TOML data from a file path."""
        with open(path, "rb") as f:
            return _TOML_LOAD(f)

    def dump(self, data: dict[str, Any], path: Path) -> None:
        """Write TOML data to a file path. Requires tomli-w to be installed."""
        if not _HAS_TOMLI_W:
            raise RuntimeError(
                "Writing TOML requires `tomli-w`. Install it to save TOML files."
            )
        path.parent.mkdir(parents=True, exist_ok=True)
        # Some tomli_w versions expose `dumps()` (returns str); others only
        # provide `dump()` which writes bytes to a binary file. Handle both.
        try:
            if hasattr(tomli_w, "dumps"):
                text = tomli_w.dumps(data)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(text)
            else:
                with open(path, "wb") as f:
                    tomli_w.dump(data, f)
        except Exception:
            # Re-raise with a clearer message
            raise

    def extension(self) -> str:
        """Return the file extension used for this serializer."""
        return "toml"


class JSONSerializer(ConfigSerializer):
    """Serializer for JSON configuration files."""

    def load(self, path: Path) -> dict[str, Any]:
        """Load JSON data from a file path."""
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def dump(self, data: dict[str, Any], path: Path) -> None:
        """Write JSON data to a file path."""
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def extension(self) -> str:
        """Return the file extension used for this serializer."""
        return "json"


class Config:
    """A flexible configuration container.

    Attributes
    ----------
    strict : bool
        When True, attribute access for missing keys raises AttributeError. When
        False, missing keys return None.
    """

    def __init__(self, *args, name: str, use_home: bool = True, strict: bool = False, **kwargs):
        """Create a Config.

        Parameters
        ----------
        name : str
            Application/config namespace used for default config directory.
        use_home : bool
            Whether to use the user's config directory (True) or platform-specific
            application directories (False).
        strict : bool
            If True, accessing missing keys as attributes raises AttributeError.
        """
        # Internal state use leading underscore names
        super().__setattr__("_use_home", use_home)
        super().__setattr__("_name", name or "mtb")
        super().__setattr__("_serializer", JSONSerializer())
        super().__setattr__("_strict", bool(strict))
        # Underlying data store for public config keys
        super().__setattr__("_data", dict(*args, **kwargs))

    # Attribute access -------------------------------------------------
    def __getattr__(self, name: str) -> Any:
        """Return stored value for attribute-style access or handle missing.

        If the config is strict, missing attributes raise AttributeError. In
        non-strict mode, missing attributes return None (backwards compatible).
        """
        if name in self._data:
            return self._data[name]
        if self._strict:
            raise AttributeError(f"Config has no key: {name}")
        return None

    def set_strict(self, strict: bool) -> None:
        """Toggle strict mode for attribute access."""
        super().__setattr__("_strict", bool(strict))

    def get(self, name: str, default: Any = None) -> Any:
        """Return the named configuration value or default if missing."""
        return self._data.get(name, default)

    def delete_key(self, name: str) -> None:
        """Remove a key from configuration if present."""
        self._data.pop(name, None)

    def set(self, name: str, value: Any) -> None:
        """Set a configuration value (use underscore-prefixed names for internals)."""
        if name.startswith("_"):
            super().__setattr__(name, value)
            return
        self._data[name] = value

    def __setattr__(self, name: str, value: Any) -> None:
        """Assign configuration values: public keys go into the config map.

        Internal attributes must begin with an underscore and are set on the
        instance directly.
        """
        self.set(name, value)

    def _to_serializable(self, obj: Any) -> Any:
        """Recursively convert objects to JSON/TOML serializable equivalents."""
        if isinstance(obj, Config):
            return obj.to_dict()
        if isinstance(obj, Path):
            return obj.as_posix()
        if isinstance(obj, dict):
            return {k: self._to_serializable(v) for k, v in obj.items()}
        if isinstance(obj, (list, tuple)):
            return [self._to_serializable(v) for v in obj]
        return obj

    def to_dict(self) -> dict[str, Any]:
        """Return a serializable copy of the config data."""
        return self._to_serializable(self._data)

    def set_serializer(self, serializer: ConfigSerializer) -> None:
        """Override the serializer used by save/load operations."""
        super().__setattr__("_serializer", serializer)

    # Save/load -------------------------------------------------------
    def _serializer_from_kind(self, kind: str) -> ConfigSerializer:
        k = (kind or "").lower().lstrip(".")
        if k == "toml":
            return TOMLSerializer()
        elif k == "json":
            return JSONSerializer()
        raise ValueError(f"Unknown config kind: {kind}")

    def save(self, path: Path | None = None, *, kind: str = "toml") -> Path:
        """Save the configuration to disk and return the path written.

        If `path` is omitted the file will be chosen under the app config
        directory (e.g. ~/.config/<app>/config.<ext>)
        """
        if path is None:
            serializer = self._serializer_from_kind(kind)
            config_dir = self.config_dir
            # Prefer existing config file if one exists
            found = None
            for f in config_dir.glob("config.*"):
                found = f
                break
            if found is None:
                path = config_dir / f"config.{serializer.extension()}"
            else:
                path = found
        else:
            serializer = self._serializer_from_kind(path.suffix[1:])

        serializable = self.to_dict()
        serializer.dump(serializable, path)
        return path

    def load(self, path: Path | None = None, kind: str = "toml") -> None:
        """Load configuration from disk into this Config instance."""
        if path is None:
            serializer = self._serializer_from_kind(kind)
            config_dir = self.config_dir
            found = None
            for f in config_dir.glob("config.*"):
                found = f
                break
            if found is None:
                path = config_dir / f"config.{serializer.extension()}"
            else:
                path = found
        else:
            serializer = self._serializer_from_kind(path.suffix[1:])

        if path.exists():
            data = serializer.load(path)
            # Update internal data but do not overwrite internal underscored attributes
            for k, v in data.items():
                self._data[k] = v

    # Convenience / path handling ------------------------------------
    @property
    def config_dir(self) -> Path:
        """Determine the config directory for this app and ensure it exists."""
        if self._use_home:
            base = Path.home() / ".config"
        else:
            if sys.platform == "darwin":
                base = Path.home() / "Library/Application Support"
            elif sys.platform == "win32":
                base = Path.home() / "AppData/Roaming"
            else:
                base = Path.home() / ".config"

        cfg = base / self._name
        cfg.mkdir(parents=True, exist_ok=True)
        return cfg


if __name__ == "__main__":
    config = Config(name="myApp")
    config.allow_xxx = True
    config.debug_mode = False
    print(config)

    p = config.save(Path("./myApp.json"))
    print("Saved:", p)

    print(config.config_dir)

    config2 = Config(name="myApp")
    config2.load(Path("./myApp.json"))
    print(config2)

    config.save(Path("./myApp.toml"))

    config4 = Config(name="myApp")
    config4.load(Path("./myApp.toml"))
    print(config4)
