"""Configuration encryption implementation."""

import hashlib
import platform
import uuid
from typing import Optional
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64


def derive_app_key(app_name: str, version: str, machine_id: Optional[str] = None) -> str:
    """
    Derive a deterministic encryption key from app metadata.

    This creates a consistent key that's unique per application and machine,
    providing reasonable security for config file encryption.

    Args:
        app_name: Application name
        version: Application version
        machine_id: Optional machine identifier (auto-detected if not provided)

    Returns:
        Derived key string suitable for encryption

    Example:
        encryption_key = derive_app_key("myapp", "1.0.0")
        config = ConfigManager("config.toml", encryption_key=encryption_key)
    """
    if machine_id is None:
        # Generate a machine-specific identifier
        try:
            # Try to get MAC address as machine identifier
            machine_id = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                                  for elements in range(0, 2*6, 2)][::-1])
        except Exception:
            # Fallback to platform info
            machine_id = f"{platform.system()}-{platform.node()}"

    # Combine app metadata
    key_material = f"{app_name}-{version}-{machine_id}"

    # Hash to create deterministic key
    key_hash = hashlib.sha256(key_material.encode()).hexdigest()
    return key_hash


def derive_fernet_key(password: str, salt: bytes = None) -> bytes:
    """
    Derive a Fernet-compatible key from password.

    Args:
        password: Password string
        salt: Optional salt bytes (auto-generated if not provided)

    Returns:
        32-byte key suitable for Fernet encryption
    """
    if salt is None:
        # Use a fixed salt derived from password for deterministic keys
        salt = hashlib.sha256(password.encode()).digest()[:16]

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )

    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key


class ConfigEncryption:
    """Handles encryption and decryption of configuration values."""

    def __init__(self, encryption_key: str):
        """
        Initialize encryption with a key.

        Args:
            encryption_key: Key string for encryption/decryption
        """
        self.encryption_key = encryption_key
        self._fernet = None
        self._setup_encryption()

    def _setup_encryption(self) -> None:
        """Set up Fernet encryption cipher."""
        try:
            # Derive Fernet-compatible key from our key string
            fernet_key = derive_fernet_key(self.encryption_key)
            self._fernet = Fernet(fernet_key)
        except Exception as e:
            raise ValueError(f"Failed to setup encryption: {e}")

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt a string value.

        Args:
            plaintext: String to encrypt

        Returns:
            Base64-encoded encrypted string
        """
        if not self._fernet:
            raise ValueError("Encryption not initialized")

        try:
            # Convert to bytes, encrypt, then encode as base64 string
            plaintext_bytes = plaintext.encode('utf-8')
            encrypted_bytes = self._fernet.encrypt(plaintext_bytes)
            encrypted_string = base64.urlsafe_b64encode(encrypted_bytes).decode('utf-8')
            return encrypted_string
        except Exception as e:
            raise ValueError(f"Encryption failed: {e}")

    def decrypt(self, encrypted_text: str) -> str:
        """
        Decrypt an encrypted string value.

        Args:
            encrypted_text: Base64-encoded encrypted string

        Returns:
            Decrypted plaintext string
        """
        if not self._fernet:
            raise ValueError("Encryption not initialized")

        try:
            # Decode from base64, decrypt, then decode as string
            encrypted_bytes = base64.urlsafe_b64decode(encrypted_text.encode('utf-8'))
            plaintext_bytes = self._fernet.decrypt(encrypted_bytes)
            plaintext = plaintext_bytes.decode('utf-8')
            return plaintext
        except Exception as e:
            raise ValueError(f"Decryption failed: {e}")

    def is_encrypted_value(self, value: str) -> bool:
        """
        Check if a string value appears to be encrypted.

        Args:
            value: String value to check

        Returns:
            True if value looks like an encrypted value
        """
        if not isinstance(value, str):
            return False

        return value.startswith("encrypted:")

    def wrap_encrypted_value(self, encrypted_text: str) -> str:
        """
        Wrap encrypted text with prefix marker.

        Args:
            encrypted_text: Base64 encrypted string

        Returns:
            Wrapped encrypted value with "encrypted:" prefix
        """
        return f"encrypted:{encrypted_text}"

    def unwrap_encrypted_value(self, wrapped_value: str) -> str:
        """
        Remove encryption prefix wrapper.

        Args:
            wrapped_value: Value with "encrypted:" prefix

        Returns:
            Raw encrypted string without prefix
        """
        if wrapped_value.startswith("encrypted:"):
            return wrapped_value[10:]  # Remove "encrypted:" prefix
        return wrapped_value

    def encrypt_and_wrap(self, plaintext: str) -> str:
        """
        Encrypt plaintext and wrap with prefix.

        Args:
            plaintext: String to encrypt

        Returns:
            Wrapped encrypted value ready for storage
        """
        encrypted = self.encrypt(plaintext)
        return self.wrap_encrypted_value(encrypted)

    def unwrap_and_decrypt(self, wrapped_value: str) -> str:
        """
        Unwrap and decrypt a stored encrypted value.

        Args:
            wrapped_value: Stored encrypted value with prefix

        Returns:
            Decrypted plaintext string
        """
        encrypted_text = self.unwrap_encrypted_value(wrapped_value)
        return self.decrypt(encrypted_text)

    def test_encryption(self) -> bool:
        """
        Test that encryption/decryption is working correctly.

        Returns:
            True if encryption is working properly
        """
        try:
            test_text = "test-encryption-12345"
            encrypted = self.encrypt(test_text)
            decrypted = self.decrypt(encrypted)
            return decrypted == test_text
        except Exception:
            return False