"""Advanced attachment handling system for email communications."""

import os
import mimetypes
import hashlib
from pathlib import Path
from typing import List, Optional, Dict, Any, Union, BinaryIO, Iterator
import tempfile
import shutil
from dataclasses import dataclass, field

from ...core.message import Attachment
from ...core.exceptions import AttachmentError


@dataclass
class AttachmentInfo:
    """Extended attachment information."""
    attachment: Attachment
    hash_md5: Optional[str] = None
    hash_sha256: Optional[str] = None
    is_safe: Optional[bool] = None
    scan_results: Dict[str, Any] = field(default_factory=dict)


class AttachmentManager:
    """Advanced attachment management with security and validation."""

    # Dangerous file extensions (security)
    DANGEROUS_EXTENSIONS = {
        '.exe', '.bat', '.cmd', '.com', '.scr', '.pif', '.vbs', '.js',
        '.jar', '.app', '.deb', '.dmg', '.iso', '.msi', '.pkg',
        '.ps1', '.sh', '.bash', '.zsh'
    }

    # Common safe extensions
    SAFE_EXTENSIONS = {
        '.txt', '.pdf', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg',
        '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.csv',
        '.zip', '.rar', '.7z', '.tar', '.gz', '.mp3', '.mp4', '.avi',
        '.mov', '.mkv', '.json', '.xml', '.html', '.css'
    }

    def __init__(self, temp_dir: Optional[str] = None, max_file_size: int = 25 * 1024 * 1024):
        """Initialize attachment manager.

        Args:
            temp_dir: Temporary directory for file operations
            max_file_size: Maximum file size in bytes (default 25MB for Gmail)
        """
        self.temp_dir = temp_dir or tempfile.gettempdir()
        self.max_file_size = max_file_size
        self._temp_files = []

    def create_attachment(
        self,
        file_path: Union[str, Path],
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
        validate: bool = True
    ) -> AttachmentInfo:
        """Create attachment from file path with validation.

        Args:
            file_path: Path to file
            filename: Override filename
            content_type: Override content type
            validate: Whether to validate file safety

        Returns:
            AttachmentInfo object

        Raises:
            AttachmentError: If attachment creation fails
        """
        file_path = Path(file_path)

        if not file_path.exists():
            raise AttachmentError(f"Attachment file not found: {file_path}", file_path=str(file_path))

        if not file_path.is_file():
            raise AttachmentError(f"Path is not a file: {file_path}", file_path=str(file_path))

        # Check file size
        file_size = file_path.stat().st_size
        if file_size > self.max_file_size:
            raise AttachmentError(
                f"File too large: {file_size} bytes (max: {self.max_file_size})",
                file_path=str(file_path)
            )

        # Determine content type
        if not content_type:
            content_type, _ = mimetypes.guess_type(str(file_path))
            content_type = content_type or 'application/octet-stream'

        # Create attachment
        attachment = Attachment(
            filename=filename or file_path.name,
            content_type=content_type,
            size=file_size,
            file_path=str(file_path.absolute())
        )

        # Create attachment info
        info = AttachmentInfo(attachment=attachment)

        # Validate if requested
        if validate:
            info = self.validate_attachment(info)

        return info

    def create_attachment_from_data(
        self,
        data: bytes,
        filename: str,
        content_type: Optional[str] = None,
        validate: bool = True
    ) -> AttachmentInfo:
        """Create attachment from binary data.

        Args:
            data: Binary data
            filename: Filename for attachment
            content_type: MIME content type
            validate: Whether to validate data safety

        Returns:
            AttachmentInfo object

        Raises:
            AttachmentError: If attachment creation fails
        """
        if len(data) > self.max_file_size:
            raise AttachmentError(
                f"Data too large: {len(data)} bytes (max: {self.max_file_size})",
                file_path=filename
            )

        # Determine content type
        if not content_type:
            content_type, _ = mimetypes.guess_type(filename)
            content_type = content_type or 'application/octet-stream'

        # Create attachment
        attachment = Attachment(
            filename=filename,
            content_type=content_type,
            size=len(data),
            content=data
        )

        # Create attachment info
        info = AttachmentInfo(attachment=attachment)

        # Validate if requested
        if validate:
            info = self.validate_attachment(info)

        return info

    def validate_attachment(self, info: AttachmentInfo) -> AttachmentInfo:
        """Validate attachment for security and integrity.

        Args:
            info: AttachmentInfo object to validate

        Returns:
            Updated AttachmentInfo with validation results
        """
        attachment = info.attachment

        # Check file extension
        file_ext = Path(attachment.filename).suffix.lower()
        info.is_safe = file_ext not in self.DANGEROUS_EXTENSIONS

        # Calculate hashes
        try:
            content = attachment.load_content()
            info.hash_md5 = hashlib.md5(content).hexdigest()
            info.hash_sha256 = hashlib.sha256(content).hexdigest()
        except Exception as e:
            info.scan_results['hash_error'] = str(e)

        # Basic content validation
        try:
            # Check for null bytes (potential binary in text file)
            if attachment.content_type.startswith('text/'):
                if b'\x00' in content:
                    info.scan_results['suspicious'] = 'Null bytes in text file'

            # Check file header matches extension
            if self._validate_file_header(content, file_ext):
                info.scan_results['header_match'] = True
            else:
                info.scan_results['header_match'] = False
                info.scan_results['warning'] = 'File header does not match extension'

        except Exception as e:
            info.scan_results['validation_error'] = str(e)

        return info

    def _validate_file_header(self, content: bytes, file_ext: str) -> bool:
        """Validate file header matches extension.

        Args:
            content: File content bytes
            file_ext: File extension

        Returns:
            True if header matches extension
        """
        if len(content) < 4:
            return False

        # Common file signatures
        signatures = {
            '.pdf': [b'%PDF'],
            '.jpg': [b'\xFF\xD8\xFF'],
            '.jpeg': [b'\xFF\xD8\xFF'],
            '.png': [b'\x89PNG\r\n\x1A\n'],
            '.gif': [b'GIF87a', b'GIF89a'],
            '.zip': [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
            '.docx': [b'PK\x03\x04'],  # DOCX is ZIP-based
            '.xlsx': [b'PK\x03\x04'],  # XLSX is ZIP-based
            '.exe': [b'MZ'],
            '.mp3': [b'ID3', b'\xFF\xFB', b'\xFF\xF3', b'\xFF\xF2'],
            '.mp4': [b'\x00\x00\x00\x20ftypmp4', b'\x00\x00\x00\x18ftyp'],
        }

        expected_sigs = signatures.get(file_ext, [])
        if not expected_sigs:
            return True  # Unknown extension, assume valid

        for sig in expected_sigs:
            if content.startswith(sig):
                return True

        return False

    def batch_create_attachments(
        self,
        file_paths: List[Union[str, Path]],
        validate: bool = True
    ) -> List[AttachmentInfo]:
        """Create multiple attachments from file paths.

        Args:
            file_paths: List of file paths
            validate: Whether to validate attachments

        Returns:
            List of AttachmentInfo objects

        Raises:
            AttachmentError: If any attachment creation fails
        """
        attachments = []
        errors = []

        for file_path in file_paths:
            try:
                info = self.create_attachment(file_path, validate=validate)
                attachments.append(info)
            except AttachmentError as e:
                errors.append(f"{file_path}: {e}")

        if errors:
            raise AttachmentError(f"Failed to create attachments: {'; '.join(errors)}")

        return attachments

    def save_attachment(
        self,
        attachment: Attachment,
        output_dir: Union[str, Path],
        filename: Optional[str] = None,
        overwrite: bool = False
    ) -> Path:
        """Save attachment to directory.

        Args:
            attachment: Attachment to save
            output_dir: Output directory
            filename: Override filename
            overwrite: Whether to overwrite existing files

        Returns:
            Path to saved file

        Raises:
            AttachmentError: If save fails
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        output_filename = filename or attachment.filename
        output_path = output_dir / output_filename

        # Check for existing file
        if output_path.exists() and not overwrite:
            # Generate unique filename
            base = output_path.stem
            suffix = output_path.suffix
            counter = 1
            while output_path.exists():
                output_path = output_dir / f"{base}_{counter}{suffix}"
                counter += 1

        try:
            content = attachment.load_content()
            with open(output_path, 'wb') as f:
                f.write(content)

            return output_path

        except Exception as e:
            raise AttachmentError(f"Failed to save attachment: {e}", file_path=str(output_path)) from e

    def batch_save_attachments(
        self,
        attachments: List[Attachment],
        output_dir: Union[str, Path],
        overwrite: bool = False
    ) -> List[Path]:
        """Save multiple attachments to directory.

        Args:
            attachments: List of attachments to save
            output_dir: Output directory
            overwrite: Whether to overwrite existing files

        Returns:
            List of paths to saved files

        Raises:
            AttachmentError: If any save fails
        """
        saved_paths = []
        errors = []

        for attachment in attachments:
            try:
                path = self.save_attachment(attachment, output_dir, overwrite=overwrite)
                saved_paths.append(path)
            except AttachmentError as e:
                errors.append(f"{attachment.filename}: {e}")

        if errors:
            raise AttachmentError(f"Failed to save attachments: {'; '.join(errors)}")

        return saved_paths

    def create_temp_file(self, data: bytes, filename: str) -> str:
        """Create temporary file with data.

        Args:
            data: Binary data
            filename: Filename

        Returns:
            Path to temporary file
        """
        # Extract extension for temp file
        suffix = Path(filename).suffix or '.tmp'

        # Create temp file
        temp_fd, temp_path = tempfile.mkstemp(suffix=suffix, dir=self.temp_dir)
        try:
            with os.fdopen(temp_fd, 'wb') as f:
                f.write(data)
        except:
            os.close(temp_fd)
            if os.path.exists(temp_path):
                os.unlink(temp_path)
            raise

        # Track for cleanup
        self._temp_files.append(temp_path)
        return temp_path

    def get_attachment_preview(self, attachment: Attachment, max_preview_size: int = 1024) -> str:
        """Get text preview of attachment content.

        Args:
            attachment: Attachment to preview
            max_preview_size: Maximum preview size in characters

        Returns:
            Text preview of attachment
        """
        try:
            if attachment.content_type.startswith('text/'):
                content = attachment.load_content()
                text = content.decode('utf-8', errors='replace')
                if len(text) > max_preview_size:
                    text = text[:max_preview_size] + '...'
                return text
            else:
                return f"Binary file ({attachment.content_type}), {attachment.size} bytes"
        except Exception as e:
            return f"Preview unavailable: {e}"

    def calculate_total_size(self, attachments: List[Attachment]) -> int:
        """Calculate total size of attachments.

        Args:
            attachments: List of attachments

        Returns:
            Total size in bytes
        """
        return sum(att.size for att in attachments)

    def filter_by_type(self, attachments: List[Attachment], content_types: List[str]) -> List[Attachment]:
        """Filter attachments by content type.

        Args:
            attachments: List of attachments
            content_types: List of content types to include

        Returns:
            Filtered list of attachments
        """
        return [att for att in attachments if any(att.content_type.startswith(ct) for ct in content_types)]

    def filter_by_extension(self, attachments: List[Attachment], extensions: List[str]) -> List[Attachment]:
        """Filter attachments by file extension.

        Args:
            attachments: List of attachments
            extensions: List of extensions to include (with or without dots)

        Returns:
            Filtered list of attachments
        """
        # Normalize extensions
        normalized_exts = []
        for ext in extensions:
            if not ext.startswith('.'):
                ext = f'.{ext}'
            normalized_exts.append(ext.lower())

        return [
            att for att in attachments
            if Path(att.filename).suffix.lower() in normalized_exts
        ]

    def cleanup_temp_files(self) -> None:
        """Clean up temporary files created by this manager."""
        for temp_path in self._temp_files:
            try:
                if os.path.exists(temp_path):
                    os.unlink(temp_path)
            except Exception:
                pass  # Ignore cleanup errors
        self._temp_files.clear()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit with cleanup."""
        self.cleanup_temp_files()