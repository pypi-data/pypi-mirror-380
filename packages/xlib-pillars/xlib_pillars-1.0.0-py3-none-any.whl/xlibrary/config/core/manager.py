"""Configuration manager implementation."""

import os
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List, Optional, Type, Union
from datetime import datetime

from .schema import Schema, ValidationResult
from .exceptions import (
    ConfigError,
    ValidationError,
    FileNotFoundError as ConfigFileNotFoundError,
    InterpolationError
)
from ..loaders import ConfigLoader, TomlLoader, LoadResult
from ..interpolation import (
    InterpolationEngine,
    EnvironmentResolver,
    ConfigResolver,
    ChainResolver
)
from ..encryption import ConfigEncryption


class ConfigManager:
    """
    Configuration manager with TOML support, interpolation, and validation.

    Provides hierarchical configuration loading, environment variable interpolation,
    and schema validation following the xlibrary design patterns.
    """

    def __init__(
        self,
        sources: Union[str, List[str], Path, List[Path], None] = None,
        schema: Optional[Schema] = None,
        environment: Optional[str] = None,
        auto_reload: bool = False,
        interpolation: bool = True,
        encoding: str = "utf-8",
        encryption_key: Optional[str] = None
    ):
        """
        Initialize configuration manager.

        Args:
            sources: Configuration file path(s) or None for empty config
            schema: Schema for validation
            environment: Environment-specific configuration section
            auto_reload: Automatically reload configuration when files change
            interpolation: Enable variable interpolation
            encoding: File encoding
            encryption_key: Optional encryption key for sensitive values
        """
        self._sources = self._normalize_sources(sources)
        self._schema = schema
        self._environment = environment
        self._auto_reload = auto_reload
        self._interpolation_enabled = interpolation
        self._encoding = encoding
        self._encryption_key = encryption_key

        # Internal state
        self._data: Dict[str, Any] = {}
        self._metadata: Dict[str, Any] = {}
        self._loaders: List[ConfigLoader] = [TomlLoader()]
        self._file_timestamps: Dict[str, float] = {}

        # Encryption system
        self._encryption = None
        if encryption_key:
            try:
                self._encryption = ConfigEncryption(encryption_key)
                # Test encryption is working
                if not self._encryption.test_encryption():
                    raise ConfigError("Encryption test failed - invalid encryption key")
            except Exception as e:
                raise ConfigError(f"Failed to initialize encryption: {e}")

        # Interpolation system
        self._interpolation_engine = InterpolationEngine()
        if interpolation:
            self._setup_interpolation()

        # Load initial configuration
        if self._sources:
            self._load_all_sources()

    def _normalize_sources(self, sources: Union[str, List[str], Path, List[Path], None]) -> List[Path]:
        """Normalize sources to list of Path objects."""
        if sources is None:
            return []

        if isinstance(sources, (str, Path)):
            sources = [sources]

        return [Path(source) for source in sources]

    def _setup_interpolation(self) -> None:
        """Set up interpolation resolvers."""
        # Environment variables resolver (highest priority)
        env_resolver = EnvironmentResolver()

        # Configuration resolver (lower priority)
        config_resolver = ConfigResolver(self._data)

        # Chain resolvers with priority order
        chain_resolver = ChainResolver([env_resolver, config_resolver])
        self._interpolation_engine.add_resolver(chain_resolver)

    def _load_all_sources(self) -> None:
        """Load configuration from all sources."""
        all_data = {}
        load_metadata = []

        for source_path in self._sources:
            if not source_path.exists():
                if len(self._sources) == 1:
                    # Only raise error if there's a single source file
                    raise ConfigFileNotFoundError(str(source_path))
                continue

            # Find appropriate loader
            loader = self._find_loader(source_path)
            if not loader:
                continue

            # Load configuration
            result = loader.load(source_path)
            load_metadata.append(result)

            if result.success:
                # Store file timestamp for auto-reload
                if self._auto_reload:
                    self._file_timestamps[str(source_path)] = source_path.stat().st_mtime

                # Merge data (later sources override earlier ones)
                all_data = self._merge_config(all_data, result.data)

        # Apply environment-specific overrides
        if self._environment and self._environment in all_data:
            env_config = all_data[self._environment]
            if isinstance(env_config, dict):
                all_data = self._merge_config(all_data, env_config)

        # Store metadata
        self._metadata = {
            'load_results': load_metadata,
            'load_time': datetime.now(),
            'sources': [str(p) for p in self._sources],
            'environment': self._environment
        }

        # Apply interpolation
        if self._interpolation_enabled:
            try:
                # Update config resolver with new data
                for resolver in self._interpolation_engine.resolvers:
                    if hasattr(resolver, 'resolvers'):  # ChainResolver
                        for sub_resolver in resolver.resolvers:
                            if isinstance(sub_resolver, ConfigResolver):
                                sub_resolver.update_config(all_data)
                    elif isinstance(resolver, ConfigResolver):
                        resolver.update_config(all_data)

                all_data = self._interpolation_engine.interpolate(all_data)
            except InterpolationError:
                raise
            except Exception as e:
                raise InterpolationError(f"Interpolation failed: {e}")

        # Validate against schema
        if self._schema:
            validation_result = self._schema.validate(all_data)
            if not validation_result.is_valid:
                raise ValidationError(
                    "Configuration validation failed",
                    errors=validation_result.errors
                )

        self._data = all_data

    def _find_loader(self, path: Path) -> Optional[ConfigLoader]:
        """Find appropriate loader for file."""
        for loader in self._loaders:
            if loader.can_load(path):
                return loader
        return None

    def _merge_config(self, base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        """Merge configuration dictionaries."""
        result = deepcopy(base)

        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                # Recursively merge nested dictionaries
                result[key] = self._merge_config(result[key], value)
            else:
                # Override value
                result[key] = deepcopy(value)

        return result

    def get(self, key: str, default: Any = None, type: Optional[Type] = None) -> Any:
        """
        Get configuration value with optional type conversion.

        Args:
            key: Configuration key (supports dot notation for nested access)
            default: Default value if key not found
            type: Type to convert value to

        Returns:
            Configuration value or default
        """
        # Check for file changes if auto-reload is enabled
        if self._auto_reload:
            self._check_reload()

        # Navigate nested keys
        keys = key.split('.')
        current = self._data

        try:
            for k in keys:
                if isinstance(current, dict) and k in current:
                    current = current[k]
                else:
                    return default

            # Handle decryption if needed
            if isinstance(current, str) and self._encryption and self._encryption.is_encrypted_value(current):
                try:
                    current = self._encryption.unwrap_and_decrypt(current)
                except Exception as e:
                    # If decryption fails, log error but return default
                    # This prevents crashes from corrupted encrypted values
                    return default

            # Apply type conversion if requested
            if type is not None and current is not None:
                if isinstance(current, type):
                    return current
                try:
                    # Common type conversions
                    if type == bool:
                        if isinstance(current, str):
                            return current.lower() in ('true', '1', 'yes', 'on')
                        return bool(current)
                    elif type in (int, float, str):
                        return type(current)
                    else:
                        return type(current)
                except (ValueError, TypeError):
                    return default

            return current

        except (KeyError, TypeError):
            return default

    def set(self, key: str, value: Any, encrypt: bool = False) -> None:
        """
        Set configuration value with optional encryption.

        Args:
            key: Configuration key (supports dot notation for nested setting)
            value: Value to set
            encrypt: Whether to encrypt the value (requires encryption_key)
        """
        # Handle encryption if requested
        if encrypt:
            if not self._encryption:
                raise ConfigError("Encryption requested but no encryption key provided")
            try:
                value = self._encryption.encrypt_and_wrap(str(value))
            except Exception as e:
                raise ConfigError(f"Failed to encrypt value: {e}")

        keys = key.split('.')
        current = self._data

        # Navigate to parent of target key
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            elif not isinstance(current[k], dict):
                current[k] = {}
            current = current[k]

        # Set the value
        current[keys[-1]] = value

        # Update interpolation engine if enabled
        if self._interpolation_enabled:
            for resolver in self._interpolation_engine.resolvers:
                if hasattr(resolver, 'resolvers'):  # ChainResolver
                    for sub_resolver in resolver.resolvers:
                        if isinstance(sub_resolver, ConfigResolver):
                            sub_resolver.update_config(self._data)
                elif isinstance(resolver, ConfigResolver):
                    resolver.update_config(self._data)

    def update(self, updates: Dict[str, Any]) -> None:
        """
        Update multiple configuration values.

        Args:
            updates: Dictionary of key-value pairs to update
        """
        for key, value in updates.items():
            self.set(key, value)

    def set_encrypted(self, key: str, value: Any) -> None:
        """
        Set an encrypted configuration value.

        Convenience method equivalent to set(key, value, encrypt=True).

        Args:
            key: Configuration key (supports dot notation for nested setting)
            value: Value to encrypt and set

        Raises:
            ConfigError: If no encryption key was provided during initialization
        """
        self.set(key, value, encrypt=True)

    def has(self, key: str) -> bool:
        """
        Check if configuration key exists.

        Args:
            key: Configuration key to check

        Returns:
            True if key exists
        """
        return self.get(key) is not None

    def keys(self, prefix: str = "") -> List[str]:
        """
        List all configuration keys with optional prefix.

        Args:
            prefix: Key prefix to filter by

        Returns:
            List of matching keys
        """
        def _collect_keys(data: Dict[str, Any], current_prefix: str = "") -> List[str]:
            keys = []
            for key, value in data.items():
                full_key = f"{current_prefix}.{key}" if current_prefix else key
                keys.append(full_key)

                if isinstance(value, dict):
                    keys.extend(_collect_keys(value, full_key))

            return keys

        all_keys = _collect_keys(self._data)

        if prefix:
            return [key for key in all_keys if key.startswith(prefix)]

        return all_keys

    def to_dict(self) -> Dict[str, Any]:
        """Export configuration as dictionary."""
        return deepcopy(self._data)

    def save(self, path: Optional[Union[str, Path]] = None) -> None:
        """
        Save configuration to file.

        Args:
            path: Path to save to (uses first source if not specified)
        """
        if path is None:
            if not self._sources:
                raise ConfigError("No save path specified and no sources configured")
            path = self._sources[0]

        path_obj = Path(path)
        loader = self._find_loader(path_obj)

        if not loader:
            # Default to TOML loader
            loader = TomlLoader()

        success = loader.save(self._data, path_obj)
        if not success:
            raise ConfigError(f"Failed to save configuration to {path_obj}")

    def reload(self) -> None:
        """Reload configuration from sources."""
        if self._sources:
            self._load_all_sources()

    def _check_reload(self) -> None:
        """Check if any source files have changed and reload if needed."""
        if not self._auto_reload or not self._sources:
            return

        reload_needed = False

        for source_path in self._sources:
            if not source_path.exists():
                continue

            current_mtime = source_path.stat().st_mtime
            stored_mtime = self._file_timestamps.get(str(source_path), 0)

            if current_mtime > stored_mtime:
                reload_needed = True
                break

        if reload_needed:
            self.reload()

    def validate(self, schema: Optional[Schema] = None) -> List[str]:
        """
        Validate configuration against schema.

        Args:
            schema: Schema to validate against (uses instance schema if not provided)

        Returns:
            List of validation errors (empty if valid)
        """
        validation_schema = schema or self._schema

        if not validation_schema:
            return []

        result = validation_schema.validate(self._data)
        return result.errors

    def get_metadata(self) -> Dict[str, Any]:
        """Get configuration metadata."""
        return deepcopy(self._metadata)

    def clear(self) -> None:
        """Clear all configuration data."""
        self._data = {}
        self._metadata = {}
        self._file_timestamps = {}

    def add_loader(self, loader: ConfigLoader) -> None:
        """Add a configuration loader."""
        self._loaders.append(loader)

    def set_schema(self, schema: Schema) -> None:
        """Set configuration schema."""
        self._schema = schema

    def enable_interpolation(self, enabled: bool = True) -> None:
        """Enable or disable variable interpolation."""
        self._interpolation_enabled = enabled
        if enabled and not self._interpolation_engine.resolvers:
            self._setup_interpolation()

    def add_resolver(self, resolver) -> None:
        """Add a variable resolver to the interpolation engine."""
        self._interpolation_engine.add_resolver(resolver)

    def __contains__(self, key: str) -> bool:
        """Support 'in' operator for key checking."""
        return self.has(key)

    def __getitem__(self, key: str) -> Any:
        """Support dictionary-style access."""
        value = self.get(key)
        if value is None and key not in self._data:
            # Use dot notation navigation to check if key truly exists
            keys = key.split('.')
            current = self._data
            for k in keys:
                if isinstance(current, dict) and k in current:
                    current = current[k]
                else:
                    raise KeyError(key)
            return current
        return value

    def __setitem__(self, key: str, value: Any) -> None:
        """Support dictionary-style assignment."""
        self.set(key, value)

    def __repr__(self) -> str:
        """String representation of ConfigManager."""
        source_info = f"{len(self._sources)} sources" if self._sources else "no sources"
        return f"ConfigManager({source_info}, {len(self._data)} keys)"