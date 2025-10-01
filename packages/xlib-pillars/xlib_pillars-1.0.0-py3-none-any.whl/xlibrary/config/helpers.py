"""
Optional helper utilities for common configuration patterns.

These are convenience layers on top of the core ConfigManager,
providing structured approaches for common use cases while
maintaining all the security and flexibility of the base system.
"""

from typing import Dict, List, Optional, Tuple
from .core.manager import ConfigManager


class APIKeyManager:
    """
    Optional helper for managing multiple API keys with encryption.

    Provides a structured approach to organizing API keys while
    maintaining full encryption and the flexibility to use your
    own organization if preferred.

    Usage:
        config = ConfigManager(encryption_key=key)
        api_keys = APIKeyManager(config)

        # Add keys with automatic encryption
        api_keys.add_key('openai', 'document_editing', 'sk-key1', 'For doc editing')
        api_keys.add_key('openai', 'chat_support', 'sk-key2', 'For chat features')

        # Set default key
        api_keys.set_default('openai', 'document_editing')

        # Retrieve keys (automatically decrypted)
        key = api_keys.get_key('openai')  # Gets default
        key = api_keys.get_key('openai', 'chat_support')  # Gets specific key
    """

    def __init__(self, config_manager: ConfigManager, base_path: str = "api_keys"):
        """
        Initialize API key manager.

        Args:
            config_manager: ConfigManager instance (should have encryption enabled)
            base_path: Base path in config for API keys (default: "api_keys")
        """
        self.config = config_manager
        self.base_path = base_path

        # Warn if encryption is not enabled
        if not self.config._encryption:
            import warnings
            warnings.warn(
                "APIKeyManager is being used without encryption enabled. "
                "API keys will be stored in plain text. "
                "Consider initializing ConfigManager with encryption_key parameter.",
                UserWarning
            )

    def add_key(self, provider: str, name: str, key: str,
                description: str = "", set_as_default: bool = False) -> None:
        """
        Add or update an API key with automatic encryption.

        Args:
            provider: Provider name ('openai', 'anthropic', etc.)
            name: Key identifier ('primary', 'backup', 'document_editing', etc.)
            key: The actual API key
            description: Optional description
            set_as_default: Whether to set this as the default key for this provider
        """
        # Store the key with encryption (if enabled)
        key_path = f"{self.base_path}.{provider}.keys.{name}"
        if self.config._encryption:
            self.config.set(key_path, key, encrypt=True)
        else:
            self.config.set(key_path, key)

        # Store metadata (not encrypted)
        if description:
            desc_path = f"{self.base_path}.{provider}.descriptions.{name}"
            self.config.set(desc_path, description)

        # Set as default if requested or if this is the first key for this provider
        if set_as_default or not self.get_default_key_name(provider):
            self.set_default(provider, name)

    def get_key(self, provider: str, name: Optional[str] = None) -> Optional[str]:
        """
        Get an API key with automatic decryption.

        Args:
            provider: Provider name
            name: Key name, or None to get the default key

        Returns:
            API key string or None if not found
        """
        if name is None:
            name = self.get_default_key_name(provider)
            if not name:
                return None

        key_path = f"{self.base_path}.{provider}.keys.{name}"
        return self.config.get(key_path)

    def set_default(self, provider: str, name: str) -> None:
        """Set the default key for a provider."""
        default_path = f"{self.base_path}.{provider}.default_key"
        self.config.set(default_path, name)

    def get_default_key_name(self, provider: str) -> Optional[str]:
        """Get the name of the default key for a provider."""
        default_path = f"{self.base_path}.{provider}.default_key"
        return self.config.get(default_path)

    def list_keys(self, provider: str) -> List[Tuple[str, Optional[str]]]:
        """
        List all keys for a provider with their descriptions.

        Returns:
            List of (key_name, description) tuples
        """
        keys_path = f"{self.base_path}.{provider}.keys"
        keys = self.config.get(keys_path, {})

        if not isinstance(keys, dict):
            return []

        result = []
        for key_name in keys.keys():
            desc_path = f"{self.base_path}.{provider}.descriptions.{key_name}"
            description = self.config.get(desc_path)
            result.append((key_name, description))

        return result

    def list_providers(self) -> List[str]:
        """List all configured providers."""
        api_keys = self.config.get(self.base_path, {})
        if not isinstance(api_keys, dict):
            return []
        return list(api_keys.keys())

    def remove_key(self, provider: str, name: str) -> bool:
        """
        Remove an API key.

        Returns:
            True if key was removed, False if it didn't exist
        """
        key_path = f"{self.base_path}.{provider}.keys.{name}"
        desc_path = f"{self.base_path}.{provider}.descriptions.{name}"

        # Check if key exists
        if self.config.get(key_path) is None:
            return False

        # Remove key and description
        # Note: This is a limitation - ConfigManager doesn't have a delete method
        # For now, we'll set them to None (could be enhanced later)
        self.config.set(key_path, None)
        self.config.set(desc_path, None)

        # If this was the default key, clear the default
        if self.get_default_key_name(provider) == name:
            default_path = f"{self.base_path}.{provider}.default_key"
            self.config.set(default_path, None)

        return True

    def get_key_info(self, provider: str, name: str) -> Optional[Dict[str, str]]:
        """
        Get information about a specific key.

        Returns:
            Dictionary with 'name', 'description', 'is_default' keys, or None if not found
        """
        key_path = f"{self.base_path}.{provider}.keys.{name}"
        key = self.config.get(key_path)

        if key is None:
            return None

        desc_path = f"{self.base_path}.{provider}.descriptions.{name}"
        description = self.config.get(desc_path, "")

        is_default = self.get_default_key_name(provider) == name

        return {
            'name': name,
            'description': description,
            'is_default': is_default,
            'key_preview': key[:10] + '...' if len(key) > 10 else key
        }


class ConfigProfiles:
    """
    Optional helper for managing configuration profiles (dev/staging/prod).

    Provides environment-specific configuration management while
    maintaining encryption and flexibility.

    Usage:
        config = ConfigManager(encryption_key=key)
        profiles = ConfigProfiles(config)

        profiles.set_profile_value('dev', 'database.host', 'localhost')
        profiles.set_profile_value('prod', 'database.host', 'prod.db.com')
        profiles.activate_profile('dev')

        host = config.get('database.host')  # Gets dev value
    """

    def __init__(self, config_manager: ConfigManager, base_path: str = "profiles"):
        """
        Initialize configuration profiles.

        Args:
            config_manager: ConfigManager instance
            base_path: Base path for profiles (default: "profiles")
        """
        self.config = config_manager
        self.base_path = base_path
        self.active_profile = None

    def set_profile_value(self, profile: str, key: str, value: any, encrypt: bool = False) -> None:
        """Set a value for a specific profile."""
        profile_path = f"{self.base_path}.{profile}.{key}"
        self.config.set(profile_path, value, encrypt=encrypt)

    def activate_profile(self, profile: str) -> None:
        """
        Activate a profile by copying its values to the root level.

        Args:
            profile: Profile name to activate
        """
        profile_data = self.config.get(f"{self.base_path}.{profile}", {})

        if isinstance(profile_data, dict):
            # Copy all profile values to root level
            for key, value in profile_data.items():
                self.config.set(key, value)

            # Track active profile
            self.config.set('active_profile', profile)
            self.active_profile = profile

    def get_active_profile(self) -> Optional[str]:
        """Get the currently active profile."""
        if self.active_profile:
            return self.active_profile
        return self.config.get('active_profile')

    def list_profiles(self) -> List[str]:
        """List available profiles."""
        profiles = self.config.get(self.base_path, {})
        if isinstance(profiles, dict):
            return list(profiles.keys())
        return []