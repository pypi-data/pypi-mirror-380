"""Communication pillar exceptions."""

from typing import Optional, Any, Dict


class CommunicationError(Exception):
    """Base exception for all communication errors."""

    def __init__(self, message: str, error_code: Optional[str] = None, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.error_code = error_code
        self.details = details or {}


class AuthenticationError(CommunicationError):
    """Authentication related errors."""

    def __init__(self, message: str = "Authentication failed", provider: Optional[str] = None, **kwargs):
        super().__init__(message, error_code="AUTH_FAILED", **kwargs)
        self.provider = provider


class MessageError(CommunicationError):
    """Message handling errors."""

    def __init__(self, message: str, message_id: Optional[str] = None, **kwargs):
        super().__init__(message, error_code="MESSAGE_ERROR", **kwargs)
        self.message_id = message_id


class AttachmentError(CommunicationError):
    """Attachment handling errors."""

    def __init__(self, message: str, file_path: Optional[str] = None, **kwargs):
        super().__init__(message, error_code="ATTACHMENT_ERROR", **kwargs)
        self.file_path = file_path


class ProviderError(CommunicationError):
    """Provider-specific errors."""

    def __init__(self, message: str, provider: str, operation: Optional[str] = None, **kwargs):
        super().__init__(message, error_code="PROVIDER_ERROR", **kwargs)
        self.provider = provider
        self.operation = operation


class RateLimitError(CommunicationError):
    """Rate limiting errors."""

    def __init__(self, message: str = "Rate limit exceeded", retry_after: Optional[int] = None, **kwargs):
        super().__init__(message, error_code="RATE_LIMIT", **kwargs)
        self.retry_after = retry_after


class NetworkError(CommunicationError):
    """Network connectivity errors."""

    def __init__(self, message: str, status_code: Optional[int] = None, **kwargs):
        super().__init__(message, error_code="NETWORK_ERROR", **kwargs)
        self.status_code = status_code


class ValidationError(CommunicationError):
    """Input validation errors."""

    def __init__(self, message: str, field: Optional[str] = None, **kwargs):
        super().__init__(message, error_code="VALIDATION_ERROR", **kwargs)
        self.field = field