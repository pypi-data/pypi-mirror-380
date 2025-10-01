"""
xlibrary.encryption - Enterprise-grade cryptography utilities

This module provides comprehensive cryptography capabilities including:
- Symmetric encryption (AES-256-GCM, ChaCha20-Poly1305, Fernet)
- Asymmetric encryption (RSA, ECDSA, Ed25519)
- PKI operations with digital signatures
- Secure hashing (SHA256/512, BLAKE2b, Argon2)
- Token generation and key management
- File encryption with streaming support

Key Features:
- Multiple algorithm support with secure defaults
- Persistent key storage with encryption
- Batch operations for efficiency
- Memory-safe operations
- Enterprise-grade security practices

Usage:
    from xlibrary.encryption import EncryptionManager

    em = EncryptionManager()

    # String encryption
    encrypted = em.encrypt_string("secret data", "password")
    decrypted = em.decrypt_string(encrypted, "password")

    # Key pair generation
    key_pair = em.generate_key_pair("rsa_2048", "my_key")
    signature = em.sign_data("document", "my_key")

    # Token generation
    api_key = em.generate_api_key("sk", 48)
"""

from .core.manager import EncryptionManager
from .core.types import (
    SymmetricAlgorithm,
    AsymmetricAlgorithm,
    HashAlgorithm,
    KeyPair,
    EncryptedData,
    HashData,
    EncryptionResult,
    EncryptionError
)

__version__ = "1.0.0"
__all__ = [
    # Main class
    "EncryptionManager",

    # Algorithm enums
    "SymmetricAlgorithm",
    "AsymmetricAlgorithm",
    "HashAlgorithm",

    # Data types
    "KeyPair",
    "EncryptedData",
    "HashData",
    "EncryptionResult",

    # Exceptions
    "EncryptionError"
]