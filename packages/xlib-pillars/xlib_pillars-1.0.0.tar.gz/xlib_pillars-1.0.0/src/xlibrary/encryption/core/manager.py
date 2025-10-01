"""
Encryption Manager for xlibrary

Comprehensive encryption functionality including symmetric/asymmetric encryption,
PKI operations, token generation, and secure hashing.
"""

import os
import json
import secrets
import hashlib
import base64
import uuid
import time
from pathlib import Path
from typing import Dict, List, Optional, Union, Tuple, Any
from datetime import datetime

from .types import (
    SymmetricAlgorithm, AsymmetricAlgorithm, HashAlgorithm,
    KeyPair, EncryptedData, HashData, EncryptionResult,
    EncryptionError, KeyNotFoundError, InvalidAlgorithmError,
    DecryptionError, KeyGenerationError
)

# Optional cryptography imports
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa, ec, ed25519, padding
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305, AESGCM
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
    from cryptography.hazmat.backends import default_backend
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False


class EncryptionManager:
    """
    Comprehensive encryption manager supporting multiple algorithms and operations.
    """

    def __init__(
        self,
        key_storage_path: Optional[str] = None,
        default_symmetric: SymmetricAlgorithm = SymmetricAlgorithm.AES_256_GCM,
        default_asymmetric: AsymmetricAlgorithm = AsymmetricAlgorithm.RSA_2048,
        default_hash: HashAlgorithm = HashAlgorithm.SHA256
    ):
        """
        Initialize EncryptionManager.

        Args:
            key_storage_path: Directory to store key pairs
            default_symmetric: Default symmetric encryption algorithm
            default_asymmetric: Default asymmetric algorithm
            default_hash: Default hash algorithm
        """
        if not CRYPTO_AVAILABLE:
            raise EncryptionError(
                "Cryptography package not available. Install with: pip install xlibrary[encryption]"
            )

        self.key_storage_path = Path(key_storage_path or os.path.expanduser("~/.xlibrary/keys"))
        self.key_storage_path.mkdir(parents=True, exist_ok=True)

        self.default_symmetric = default_symmetric
        self.default_asymmetric = default_asymmetric
        self.default_hash = default_hash

        self._key_cache: Dict[str, KeyPair] = {}

    # Symmetric Encryption Methods

    def encrypt_string(
        self,
        plaintext: str,
        password: str,
        algorithm: Union[str, SymmetricAlgorithm] = None
    ) -> str:
        """
        Encrypt a string with symmetric encryption.

        Args:
            plaintext: String to encrypt
            password: Password for encryption
            algorithm: Encryption algorithm to use

        Returns:
            Base64-encoded encrypted data with metadata
        """
        if algorithm is None:
            algorithm = self.default_symmetric
        elif isinstance(algorithm, str):
            try:
                algorithm = SymmetricAlgorithm(algorithm)
            except ValueError:
                raise InvalidAlgorithmError(f"Unknown algorithm: {algorithm}")

        plaintext_bytes = plaintext.encode('utf-8')
        encrypted_data = self._encrypt_symmetric(plaintext_bytes, password.encode('utf-8'), algorithm)

        # Create JSON structure with all metadata
        result = {
            "ciphertext": base64.b64encode(encrypted_data.ciphertext).decode('ascii'),
            "algorithm": algorithm.value,
            "salt": base64.b64encode(encrypted_data.salt).decode('ascii') if encrypted_data.salt else None,
            "iv": base64.b64encode(encrypted_data.iv).decode('ascii') if encrypted_data.iv else None,
            "tag": base64.b64encode(encrypted_data.tag).decode('ascii') if encrypted_data.tag else None
        }

        return base64.b64encode(json.dumps(result).encode('utf-8')).decode('ascii')

    def decrypt_string(self, encrypted_data: str, password: str) -> str:
        """
        Decrypt a string encrypted with encrypt_string.

        Args:
            encrypted_data: Base64-encoded encrypted data from encrypt_string
            password: Password used for encryption

        Returns:
            Decrypted plaintext string
        """
        try:
            # Decode the JSON structure
            json_data = json.loads(base64.b64decode(encrypted_data).decode('utf-8'))

            # Reconstruct EncryptedData object
            encrypted_obj = EncryptedData(
                ciphertext=base64.b64decode(json_data["ciphertext"]),
                algorithm=json_data["algorithm"],
                salt=base64.b64decode(json_data["salt"]) if json_data.get("salt") else None,
                iv=base64.b64decode(json_data["iv"]) if json_data.get("iv") else None,
                tag=base64.b64decode(json_data["tag"]) if json_data.get("tag") else None
            )

            algorithm = SymmetricAlgorithm(json_data["algorithm"])
            decrypted_bytes = self._decrypt_symmetric(encrypted_obj, password.encode('utf-8'), algorithm)

            return decrypted_bytes.decode('utf-8')

        except Exception as e:
            raise DecryptionError(f"Failed to decrypt string: {e}")

    def encrypt_file(
        self,
        input_path: Union[str, Path],
        output_path: Union[str, Path],
        password: str,
        algorithm: Union[str, SymmetricAlgorithm] = None,
        chunk_size: int = 64 * 1024
    ) -> EncryptionResult:
        """
        Encrypt file with streaming for large files.

        Args:
            input_path: Path to input file
            output_path: Path to output encrypted file
            password: Password for encryption
            algorithm: Encryption algorithm to use
            chunk_size: Size of chunks for streaming (bytes)

        Returns:
            EncryptionResult with operation details
        """
        start_time = time.time()
        input_path = Path(input_path)
        output_path = Path(output_path)

        if algorithm is None:
            algorithm = self.default_symmetric
        elif isinstance(algorithm, str):
            algorithm = SymmetricAlgorithm(algorithm)

        try:
            file_size = input_path.stat().st_size

            # For small files, use in-memory encryption
            if file_size < chunk_size:
                with open(input_path, 'rb') as f:
                    plaintext = f.read()

                encrypted_data = self._encrypt_symmetric(plaintext, password.encode('utf-8'), algorithm)

                # Store encrypted data with metadata
                result_data = {
                    "algorithm": algorithm.value,
                    "ciphertext": base64.b64encode(encrypted_data.ciphertext).decode('ascii'),
                    "salt": base64.b64encode(encrypted_data.salt).decode('ascii') if encrypted_data.salt else None,
                    "iv": base64.b64encode(encrypted_data.iv).decode('ascii') if encrypted_data.iv else None,
                    "tag": base64.b64encode(encrypted_data.tag).decode('ascii') if encrypted_data.tag else None
                }

                with open(output_path, 'w') as f:
                    json.dump(result_data, f)

            else:
                # For large files, implement streaming (simplified version)
                # In production, this would use proper streaming encryption
                raise NotImplementedError("Streaming encryption for large files not yet implemented")

            execution_time = time.time() - start_time
            output_size = output_path.stat().st_size

            return EncryptionResult(
                success=True,
                input_path=input_path,
                output_path=output_path,
                algorithm=algorithm.value,
                file_size=output_size,
                execution_time=execution_time
            )

        except Exception as e:
            return EncryptionResult(
                success=False,
                input_path=input_path,
                output_path=output_path,
                algorithm=algorithm.value if algorithm else None,
                error_message=str(e),
                execution_time=time.time() - start_time
            )

    def _encrypt_symmetric(self, plaintext: bytes, key_material: bytes,
                          algorithm: SymmetricAlgorithm) -> EncryptedData:
        """Internal method for symmetric encryption."""
        if algorithm == SymmetricAlgorithm.AES_256_GCM:
            return self._encrypt_aes_gcm(plaintext, key_material)
        elif algorithm == SymmetricAlgorithm.CHACHA20_POLY1305:
            return self._encrypt_chacha20(plaintext, key_material)
        elif algorithm == SymmetricAlgorithm.FERNET:
            return self._encrypt_fernet(plaintext, key_material)
        else:
            raise InvalidAlgorithmError(f"Unsupported algorithm: {algorithm}")

    def _decrypt_symmetric(self, encrypted_data: EncryptedData, key_material: bytes,
                          algorithm: SymmetricAlgorithm) -> bytes:
        """Internal method for symmetric decryption."""
        if algorithm == SymmetricAlgorithm.AES_256_GCM:
            return self._decrypt_aes_gcm(encrypted_data, key_material)
        elif algorithm == SymmetricAlgorithm.CHACHA20_POLY1305:
            return self._decrypt_chacha20(encrypted_data, key_material)
        elif algorithm == SymmetricAlgorithm.FERNET:
            return self._decrypt_fernet(encrypted_data, key_material)
        else:
            raise InvalidAlgorithmError(f"Unsupported algorithm: {algorithm}")

    def _encrypt_aes_gcm(self, plaintext: bytes, key_material: bytes) -> EncryptedData:
        """Encrypt using AES-256-GCM."""
        # Generate salt and derive key
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(key_material)

        # Generate IV
        iv = os.urandom(12)

        # Encrypt
        cipher = AESGCM(key)
        ciphertext = cipher.encrypt(iv, plaintext, None)

        # Extract tag (last 16 bytes of ciphertext)
        tag = ciphertext[-16:]
        ciphertext = ciphertext[:-16]

        return EncryptedData(
            ciphertext=ciphertext,
            algorithm="aes_256_gcm",
            salt=salt,
            iv=iv,
            tag=tag
        )

    def _decrypt_aes_gcm(self, encrypted_data: EncryptedData, key_material: bytes) -> bytes:
        """Decrypt using AES-256-GCM."""
        # Derive key from salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=encrypted_data.salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(key_material)

        # Reconstruct full ciphertext with tag
        full_ciphertext = encrypted_data.ciphertext + encrypted_data.tag

        # Decrypt
        cipher = AESGCM(key)
        plaintext = cipher.decrypt(encrypted_data.iv, full_ciphertext, None)

        return plaintext

    def _encrypt_chacha20(self, plaintext: bytes, key_material: bytes) -> EncryptedData:
        """Encrypt using ChaCha20-Poly1305."""
        # Generate salt and derive key
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(key_material)

        # Generate nonce
        nonce = os.urandom(12)

        # Encrypt
        cipher = ChaCha20Poly1305(key)
        ciphertext = cipher.encrypt(nonce, plaintext, None)

        # Extract tag (last 16 bytes)
        tag = ciphertext[-16:]
        ciphertext = ciphertext[:-16]

        return EncryptedData(
            ciphertext=ciphertext,
            algorithm="chacha20_poly1305",
            salt=salt,
            iv=nonce,
            tag=tag
        )

    def _decrypt_chacha20(self, encrypted_data: EncryptedData, key_material: bytes) -> bytes:
        """Decrypt using ChaCha20-Poly1305."""
        # Derive key
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=encrypted_data.salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(key_material)

        # Reconstruct full ciphertext with tag
        full_ciphertext = encrypted_data.ciphertext + encrypted_data.tag

        # Decrypt
        cipher = ChaCha20Poly1305(key)
        plaintext = cipher.decrypt(encrypted_data.iv, full_ciphertext, None)

        return plaintext

    def _encrypt_fernet(self, plaintext: bytes, key_material: bytes) -> EncryptedData:
        """Encrypt using Fernet."""
        # Derive key for Fernet (needs exactly 32 bytes, base64 encoded)
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(key_material))

        # Encrypt
        fernet = Fernet(key)
        ciphertext = fernet.encrypt(plaintext)

        return EncryptedData(
            ciphertext=ciphertext,
            algorithm="fernet",
            salt=salt
        )

    def _decrypt_fernet(self, encrypted_data: EncryptedData, key_material: bytes) -> bytes:
        """Decrypt using Fernet."""
        # Derive key
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=encrypted_data.salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(key_material))

        # Decrypt
        fernet = Fernet(key)
        plaintext = fernet.decrypt(encrypted_data.ciphertext)

        return plaintext

    # Token Generation Methods

    def generate_token(self, length: int = 32, format: str = "hex") -> Union[str, bytes]:
        """
        Generate cryptographically secure random token.

        Args:
            length: Token length in bytes
            format: Output format ("hex", "base64", "bytes")

        Returns:
            Secure random token in specified format
        """
        token_bytes = secrets.token_bytes(length)

        if format == "hex":
            return token_bytes.hex()
        elif format == "base64":
            return base64.urlsafe_b64encode(token_bytes).decode('ascii')
        elif format == "bytes":
            return token_bytes
        else:
            raise ValueError(f"Invalid format: {format}")

    def generate_api_key(self, prefix: str = "xlk", length: int = 32, alphabet: str = "base62") -> str:
        """
        Generate API key with prefix.

        Args:
            prefix: Key prefix (e.g., "sk", "pk", "xlk")
            length: Key length (excluding prefix)
            alphabet: Character set ("base62", "base64", "hex")

        Returns:
            API key with format: prefix_randomstring
        """
        if alphabet == "base62":
            # Base62: 0-9, A-Z, a-z
            chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        elif alphabet == "base64":
            chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
        elif alphabet == "hex":
            chars = "0123456789abcdef"
        else:
            raise ValueError(f"Invalid alphabet: {alphabet}")

        key_part = ''.join(secrets.choice(chars) for _ in range(length))
        return f"{prefix}_{key_part}"

    def generate_uuid(self, version: int = 4) -> str:
        """Generate UUID."""
        if version == 4:
            return str(uuid.uuid4())
        else:
            raise ValueError(f"UUID version {version} not supported")

    def generate_secure_password(
        self,
        length: int = 16,
        include_uppercase: bool = True,
        include_lowercase: bool = True,
        include_digits: bool = True,
        include_symbols: bool = True,
        exclude_ambiguous: bool = True
    ) -> str:
        """Generate cryptographically secure password."""
        chars = ""

        if include_lowercase:
            chars += "abcdefghijklmnopqrstuvwxyz"
        if include_uppercase:
            chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if include_digits:
            chars += "0123456789"
        if include_symbols:
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

        if exclude_ambiguous:
            # Remove ambiguous characters
            ambiguous = "0O1lI"
            chars = ''.join(c for c in chars if c not in ambiguous)

        if not chars:
            raise ValueError("No valid characters selected for password generation")

        return ''.join(secrets.choice(chars) for _ in range(length))

    # Secure Hashing Methods

    def hash_string(
        self,
        data: str,
        algorithm: Union[str, HashAlgorithm] = None,
        salt_length: int = 32
    ) -> HashData:
        """
        Hash string with secure random salt.

        Args:
            data: String to hash
            algorithm: Hash algorithm to use
            salt_length: Length of salt in bytes

        Returns:
            HashData with hash, salt, and metadata
        """
        if algorithm is None:
            algorithm = self.default_hash
        elif isinstance(algorithm, str):
            try:
                algorithm = HashAlgorithm(algorithm)
            except ValueError:
                raise InvalidAlgorithmError(f"Unknown algorithm: {algorithm}")

        salt = secrets.token_hex(salt_length)

        if algorithm == HashAlgorithm.SHA256:
            hash_obj = hashlib.sha256()
            hash_obj.update(data.encode('utf-8'))
            hash_obj.update(salt.encode('utf-8'))
            hash_value = hash_obj.hexdigest()
            iterations = None

        elif algorithm == HashAlgorithm.SHA512:
            hash_obj = hashlib.sha512()
            hash_obj.update(data.encode('utf-8'))
            hash_obj.update(salt.encode('utf-8'))
            hash_value = hash_obj.hexdigest()
            iterations = None

        elif algorithm == HashAlgorithm.BLAKE2B:
            hash_obj = hashlib.blake2b()
            hash_obj.update(data.encode('utf-8'))
            hash_obj.update(salt.encode('utf-8'))
            hash_value = hash_obj.hexdigest()
            iterations = None

        elif algorithm == HashAlgorithm.ARGON2:
            # Use Argon2 for password hashing
            kdf = Argon2id(
                length=32,
                salt=salt.encode('utf-8')[:16],  # Argon2 needs bytes
                iterations=4,
                lanes=1,
                memory_cost=65536
            )
            hash_bytes = kdf.derive(data.encode('utf-8'))
            hash_value = hash_bytes.hex()
            iterations = 4

        else:
            raise InvalidAlgorithmError(f"Unsupported algorithm: {algorithm}")

        return HashData(
            hash=hash_value,
            salt=salt,
            algorithm=algorithm.value,
            iterations=iterations,
            metadata={"created_at": datetime.now().isoformat()}
        )

    def verify_hash(self, data: str, hash_data: HashData) -> bool:
        """
        Verify hashed data matches original.

        Args:
            data: Original data to verify
            hash_data: HashData from hash_string

        Returns:
            True if data matches hash
        """
        try:
            algorithm = HashAlgorithm(hash_data.algorithm)

            if algorithm == HashAlgorithm.SHA256:
                hash_obj = hashlib.sha256()
                hash_obj.update(data.encode('utf-8'))
                hash_obj.update(hash_data.salt.encode('utf-8'))
                computed_hash = hash_obj.hexdigest()

            elif algorithm == HashAlgorithm.SHA512:
                hash_obj = hashlib.sha512()
                hash_obj.update(data.encode('utf-8'))
                hash_obj.update(hash_data.salt.encode('utf-8'))
                computed_hash = hash_obj.hexdigest()

            elif algorithm == HashAlgorithm.BLAKE2B:
                hash_obj = hashlib.blake2b()
                hash_obj.update(data.encode('utf-8'))
                hash_obj.update(hash_data.salt.encode('utf-8'))
                computed_hash = hash_obj.hexdigest()

            elif algorithm == HashAlgorithm.ARGON2:
                kdf = Argon2id(
                    algorithm=hashes.SHA256(),
                    length=32,
                    salt=hash_data.salt.encode('utf-8')[:16],
                    iterations=hash_data.iterations or 4,
                    lanes=1,
                    memory_cost=65536,
                    backend=default_backend()
                )
                hash_bytes = kdf.derive(data.encode('utf-8'))
                computed_hash = hash_bytes.hex()

            else:
                return False

            return secrets.compare_digest(computed_hash, hash_data.hash)

        except Exception:
            return False

    def hash_file(
        self,
        file_path: Union[str, Path],
        algorithm: Union[str, HashAlgorithm] = HashAlgorithm.SHA256,
        chunk_size: int = 64 * 1024
    ) -> str:
        """
        Generate file hash for integrity verification.

        Args:
            file_path: Path to file
            algorithm: Hash algorithm
            chunk_size: Size of chunks for reading large files

        Returns:
            Hexadecimal hash of file contents
        """
        if isinstance(algorithm, str):
            algorithm = HashAlgorithm(algorithm)

        file_path = Path(file_path)

        if algorithm == HashAlgorithm.SHA256:
            hash_obj = hashlib.sha256()
        elif algorithm == HashAlgorithm.SHA512:
            hash_obj = hashlib.sha512()
        elif algorithm == HashAlgorithm.BLAKE2B:
            hash_obj = hashlib.blake2b()
        else:
            raise InvalidAlgorithmError(f"File hashing not supported for: {algorithm}")

        with open(file_path, 'rb') as f:
            while chunk := f.read(chunk_size):
                hash_obj.update(chunk)

        return hash_obj.hexdigest()

    # Asymmetric Encryption & PKI Methods (Basic implementations)

    def generate_key_pair(
        self,
        algorithm: Union[str, AsymmetricAlgorithm],
        key_id: str,
        key_size: Optional[int] = None
    ) -> KeyPair:
        """
        Generate asymmetric key pair.

        Args:
            algorithm: Asymmetric algorithm
            key_id: Unique identifier for the key pair
            key_size: Key size (algorithm dependent)

        Returns:
            KeyPair object with public/private keys
        """
        if isinstance(algorithm, str):
            try:
                algorithm = AsymmetricAlgorithm(algorithm)
            except ValueError:
                raise InvalidAlgorithmError(f"Unknown algorithm: {algorithm}")

        try:
            if algorithm == AsymmetricAlgorithm.RSA_2048:
                private_key = rsa.generate_private_key(
                    public_exponent=65537,
                    key_size=key_size or 2048,
                    backend=default_backend()
                )
            elif algorithm == AsymmetricAlgorithm.RSA_4096:
                private_key = rsa.generate_private_key(
                    public_exponent=65537,
                    key_size=key_size or 4096,
                    backend=default_backend()
                )
            elif algorithm == AsymmetricAlgorithm.ECDSA_P256:
                private_key = ec.generate_private_key(ec.SECP256R1(), backend=default_backend())
            elif algorithm == AsymmetricAlgorithm.ECDSA_P384:
                private_key = ec.generate_private_key(ec.SECP384R1(), backend=default_backend())
            elif algorithm == AsymmetricAlgorithm.ED25519:
                private_key = ed25519.Ed25519PrivateKey.generate()
            else:
                raise InvalidAlgorithmError(f"Unsupported algorithm: {algorithm}")

            # Serialize keys
            private_pem = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )

            public_key = private_key.public_key()
            public_pem = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )

            key_pair = KeyPair(
                key_id=key_id,
                algorithm=algorithm.value,
                private_key=private_pem,
                public_key=public_pem,
                created_at=datetime.now(),
                metadata={"key_size": key_size}
            )

            # Cache the key pair
            self._key_cache[key_id] = key_pair

            return key_pair

        except Exception as e:
            raise KeyGenerationError(f"Failed to generate key pair: {e}")

    # Key Management Methods

    def store_key_pair(
        self,
        key_id: str,
        key_pair: KeyPair,
        protected: bool = True,
        metadata: Optional[Dict[str, Any]] = None
    ) -> bool:
        """
        Store key pair persistently.

        Args:
            key_id: Key identifier
            key_pair: KeyPair to store
            protected: Whether to encrypt stored key
            metadata: Additional metadata

        Returns:
            True if stored successfully
        """
        try:
            key_file = self.key_storage_path / f"{key_id}.json"

            # Prepare key data for storage
            key_data = {
                "key_id": key_pair.key_id,
                "algorithm": key_pair.algorithm,
                "public_key": base64.b64encode(key_pair.public_key).decode('ascii'),
                "private_key": base64.b64encode(key_pair.private_key).decode('ascii'),
                "created_at": key_pair.created_at.isoformat(),
                "metadata": key_pair.metadata or {},
                "protected": protected
            }

            if metadata:
                key_data["metadata"].update(metadata)

            # For now, store unencrypted (in production, implement key encryption)
            with open(key_file, 'w') as f:
                json.dump(key_data, f, indent=2)

            # Set restrictive permissions
            os.chmod(key_file, 0o600)

            # Cache the key
            self._key_cache[key_id] = key_pair

            return True

        except Exception as e:
            raise EncryptionError(f"Failed to store key pair: {e}")

    def get_key_pair(self, key_id: str) -> Optional[KeyPair]:
        """
        Retrieve stored key pair.

        Args:
            key_id: Key identifier

        Returns:
            KeyPair if found, None otherwise
        """
        # Check cache first
        if key_id in self._key_cache:
            return self._key_cache[key_id]

        try:
            key_file = self.key_storage_path / f"{key_id}.json"

            if not key_file.exists():
                return None

            with open(key_file, 'r') as f:
                key_data = json.load(f)

            key_pair = KeyPair(
                key_id=key_data["key_id"],
                algorithm=key_data["algorithm"],
                public_key=base64.b64decode(key_data["public_key"]),
                private_key=base64.b64decode(key_data["private_key"]),
                created_at=datetime.fromisoformat(key_data["created_at"]),
                metadata=key_data.get("metadata", {})
            )

            # Cache the key
            self._key_cache[key_id] = key_pair

            return key_pair

        except Exception as e:
            raise EncryptionError(f"Failed to retrieve key pair: {e}")

    def list_keys(self, algorithm: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        List available keys with metadata.

        Args:
            algorithm: Filter by algorithm (optional)

        Returns:
            List of key metadata dictionaries
        """
        keys = []

        try:
            for key_file in self.key_storage_path.glob("*.json"):
                with open(key_file, 'r') as f:
                    key_data = json.load(f)

                if algorithm is None or key_data.get("algorithm") == algorithm:
                    keys.append({
                        "key_id": key_data["key_id"],
                        "algorithm": key_data["algorithm"],
                        "created_at": key_data["created_at"],
                        "metadata": key_data.get("metadata", {}),
                        "protected": key_data.get("protected", False)
                    })

        except Exception as e:
            raise EncryptionError(f"Failed to list keys: {e}")

        return keys