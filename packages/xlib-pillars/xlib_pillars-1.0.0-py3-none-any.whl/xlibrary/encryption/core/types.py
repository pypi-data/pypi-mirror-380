"""
Type definitions for encryption operations.
"""

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional, Dict, Any, Union
from datetime import datetime


class SymmetricAlgorithm(Enum):
    """Supported symmetric encryption algorithms."""
    AES_256_GCM = "aes_256_gcm"
    CHACHA20_POLY1305 = "chacha20_poly1305"
    FERNET = "fernet"


class AsymmetricAlgorithm(Enum):
    """Supported asymmetric encryption/signing algorithms."""
    RSA_2048 = "rsa_2048"
    RSA_4096 = "rsa_4096"
    ECDSA_P256 = "ecdsa_p256"
    ECDSA_P384 = "ecdsa_p384"
    ED25519 = "ed25519"


class HashAlgorithm(Enum):
    """Supported hash algorithms."""
    SHA256 = "sha256"
    SHA512 = "sha512"
    BLAKE2B = "blake2b"
    ARGON2 = "argon2"


@dataclass
class KeyPair:
    """Represents an asymmetric key pair."""
    key_id: str
    algorithm: str
    public_key: bytes
    private_key: bytes
    created_at: datetime
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


@dataclass
class EncryptedData:
    """Represents encrypted data with metadata."""
    ciphertext: bytes
    algorithm: str
    salt: Optional[bytes] = None
    iv: Optional[bytes] = None
    tag: Optional[bytes] = None
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


@dataclass
class HashData:
    """Represents hashed data with salt and metadata."""
    hash: str
    salt: str
    algorithm: str
    iterations: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


@dataclass
class EncryptionResult:
    """Result of encryption/decryption operations."""
    success: bool
    input_path: Optional[Path] = None
    output_path: Optional[Path] = None
    algorithm: Optional[str] = None
    file_size: Optional[int] = None
    execution_time: Optional[float] = None
    error_message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


class EncryptionError(Exception):
    """Base exception for encryption operations."""
    pass


class KeyNotFoundError(EncryptionError):
    """Exception raised when a key is not found."""
    pass


class InvalidAlgorithmError(EncryptionError):
    """Exception raised for invalid algorithm selection."""
    pass


class DecryptionError(EncryptionError):
    """Exception raised during decryption operations."""
    pass


class KeyGenerationError(EncryptionError):
    """Exception raised during key generation."""
    pass