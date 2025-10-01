"""
Config Pillar - Configuration management with TOML support

Features:
- TOML configuration file support
- Environment variable interpolation
- Configuration validation
- Hierarchical configuration merging
"""

from .core.manager import ConfigManager
from .core.schema import (
    Schema,
    ValidationResult,
    TypeValidator,
    RangeValidator,
    PatternValidator,
    ChoiceValidator,
    required,
    optional,
    range_check,
    pattern,
    choice
)
from .core.exceptions import (
    ConfigError,
    ValidationError,
    FileNotFoundError,
    InterpolationError,
    InvalidFormatError,
    CircularReferenceError
)
from .loaders import ConfigLoader, TomlLoader
from .interpolation import (
    InterpolationEngine,
    VariableResolver,
    EnvironmentResolver,
    ConfigResolver,
    ChainResolver
)
from .encryption import ConfigEncryption, derive_app_key
from .helpers import APIKeyManager, ConfigProfiles

__version__ = "1.0.0"
__all__ = [
    # Main classes
    "ConfigManager",
    "Schema",

    # Schema components
    "ValidationResult",
    "TypeValidator",
    "RangeValidator",
    "PatternValidator",
    "ChoiceValidator",

    # Schema convenience functions
    "required",
    "optional",
    "range_check",
    "pattern",
    "choice",

    # Exceptions
    "ConfigError",
    "ValidationError",
    "FileNotFoundError",
    "InterpolationError",
    "InvalidFormatError",
    "CircularReferenceError",

    # Loaders
    "ConfigLoader",
    "TomlLoader",

    # Interpolation
    "InterpolationEngine",
    "VariableResolver",
    "EnvironmentResolver",
    "ConfigResolver",
    "ChainResolver",

    # Encryption
    "ConfigEncryption",
    "derive_app_key",

    # Optional Helpers
    "APIKeyManager",
    "ConfigProfiles"
]