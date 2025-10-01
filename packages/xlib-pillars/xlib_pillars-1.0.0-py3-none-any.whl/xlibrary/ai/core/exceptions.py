"""
Comprehensive exception hierarchy for AI provider system.

Follows the complete design document specification with detailed error categories,
specialized exception types, and rich metadata for error handling.
"""

from typing import Optional
from datetime import datetime


# =============================================================================
# BASE EXCEPTION
# =============================================================================

class AIError(Exception):
    """Base exception for all AI-related errors."""

    def __init__(self, message: str, metadata: Optional[dict] = None):
        super().__init__(message)
        self.metadata = metadata or {}
        self.timestamp = datetime.now()


# =============================================================================
# CONFIGURATION ERRORS
# =============================================================================

class ConfigurationError(AIError):
    """Raised when there's an issue with configuration."""
    pass


class InvalidProviderError(ConfigurationError):
    """Raised when an invalid provider is specified."""

    def __init__(self, message: str, provider: str = None, available_providers: list = None):
        super().__init__(message)
        self.provider = provider
        self.available_providers = available_providers or []


class InvalidModelError(ConfigurationError):
    """Raised when an invalid model is specified for a provider."""

    def __init__(self, message: str, model: str = None, available_models: list = None):
        super().__init__(message)
        self.model = model
        self.available_models = available_models or []


class MissingCredentialsError(ConfigurationError):
    """Raised when required credentials are missing."""

    def __init__(self, message: str, required_credential: str = None):
        super().__init__(message)
        self.required_credential = required_credential


class InvalidConfigurationError(ConfigurationError):
    """Raised when configuration parameters are invalid."""

    def __init__(self, message: str, invalid_params: list = None):
        super().__init__(message)
        self.invalid_params = invalid_params or []


# =============================================================================
# PROVIDER ERRORS
# =============================================================================

class ProviderError(AIError):
    """Base class for provider-specific errors."""

    def __init__(self, message: str, provider: str = None, **kwargs):
        super().__init__(message, **kwargs)
        self.provider = provider


class AuthenticationError(ProviderError):
    """Raised when authentication with a provider fails."""
    pass


class InvalidAPIKeyError(AuthenticationError):
    """Raised when the API key is invalid."""
    pass


class ExpiredAPIKeyError(AuthenticationError):
    """Raised when the API key has expired."""

    def __init__(self, message: str, expiry_date: datetime = None, **kwargs):
        super().__init__(message, **kwargs)
        self.expiry_date = expiry_date


class InsufficientPermissionsError(AuthenticationError):
    """Raised when API key lacks required permissions."""

    def __init__(self, message: str, required_permissions: list = None, **kwargs):
        super().__init__(message, **kwargs)
        self.required_permissions = required_permissions or []


class RateLimitError(ProviderError):
    """Raised when rate limits are exceeded."""

    def __init__(self, message: str, retry_after_seconds: int = None, **kwargs):
        super().__init__(message, **kwargs)
        self.retry_after_seconds = retry_after_seconds


class RequestRateLimitError(RateLimitError):
    """Raised when request rate limit is exceeded."""

    def __init__(self, message: str, requests_remaining: int = None, **kwargs):
        super().__init__(message, **kwargs)
        self.requests_remaining = requests_remaining


class TokenRateLimitError(RateLimitError):
    """Raised when token rate limit is exceeded."""

    def __init__(self, message: str, tokens_remaining: int = None, **kwargs):
        super().__init__(message, **kwargs)
        self.tokens_remaining = tokens_remaining


class DailyQuotaExceededError(RateLimitError):
    """Raised when daily quota is exceeded."""

    def __init__(self, message: str, quota_reset_time: datetime = None, **kwargs):
        super().__init__(message, **kwargs)
        self.quota_reset_time = quota_reset_time


class ModelUnavailableError(ProviderError):
    """Raised when a model is unavailable."""

    def __init__(self, message: str, model: str = None, suggested_replacement: str = None, **kwargs):
        super().__init__(message, **kwargs)
        self.model = model
        self.suggested_replacement = suggested_replacement


class ModelNotFoundError(ModelUnavailableError):
    """Raised when a model cannot be found."""
    pass


class ModelDeprecatedError(ModelUnavailableError):
    """Raised when a model has been deprecated."""

    def __init__(self, message: str, deprecation_date: datetime = None, **kwargs):
        super().__init__(message, **kwargs)
        self.deprecation_date = deprecation_date


class ModelMaintenanceError(ModelUnavailableError):
    """Raised when a model is under maintenance."""

    def __init__(self, message: str, maintenance_end_time: datetime = None, **kwargs):
        super().__init__(message, **kwargs)
        self.maintenance_end_time = maintenance_end_time


class ProviderServiceError(ProviderError):
    """Base class for provider service errors."""
    pass


class ProviderTimeoutError(ProviderServiceError):
    """Raised when provider service times out."""

    def __init__(self, message: str, timeout_duration: float = None, **kwargs):
        super().__init__(message, **kwargs)
        self.timeout_duration = timeout_duration


class ProviderOverloadedError(ProviderServiceError):
    """Raised when provider service is overloaded."""
    pass


class ProviderMaintenanceError(ProviderServiceError):
    """Raised when provider service is under maintenance."""

    def __init__(self, message: str, maintenance_end_time: datetime = None, **kwargs):
        super().__init__(message, **kwargs)
        self.maintenance_end_time = maintenance_end_time


# =============================================================================
# REQUEST ERRORS
# =============================================================================

class RequestError(AIError):
    """Base class for request-related errors."""

    def __init__(self, message: str, request_id: str = None, **kwargs):
        super().__init__(message, **kwargs)
        self.request_id = request_id


class ValidationError(RequestError):
    """Raised when request validation fails."""
    pass


class InvalidPromptError(ValidationError):
    """Raised when prompt is invalid."""

    def __init__(self, message: str, prompt_length: int = None, **kwargs):
        super().__init__(message, **kwargs)
        self.prompt_length = prompt_length


class TokenLimitExceededError(ValidationError):
    """Raised when token limits are exceeded."""

    def __init__(self, message: str, token_count: int = None, token_limit: int = None, **kwargs):
        super().__init__(message, **kwargs)
        self.token_count = token_count
        self.token_limit = token_limit


class InvalidParameterError(ValidationError):
    """Raised when request parameters are invalid."""

    def __init__(self, message: str, invalid_parameter: str = None, valid_range: str = None, **kwargs):
        super().__init__(message, **kwargs)
        self.invalid_parameter = invalid_parameter
        self.valid_range = valid_range


class UnsupportedFeatureError(ValidationError):
    """Raised when a feature is not supported by the provider."""

    def __init__(self, message: str, feature: str = None, **kwargs):
        super().__init__(message, **kwargs)
        self.feature = feature


class TimeoutError(RequestError):
    """Base class for timeout errors."""

    def __init__(self, message: str, timeout_duration: float = None, **kwargs):
        super().__init__(message, **kwargs)
        self.timeout_duration = timeout_duration


class RequestTimeoutError(TimeoutError):
    """Raised when request times out."""
    pass


class StreamingTimeoutError(TimeoutError):
    """Raised when streaming times out."""
    pass


class ResponseTimeoutError(TimeoutError):
    """Raised when response times out."""
    pass


class ContentFilterError(RequestError):
    """Base class for content filtering errors."""

    def __init__(self, message: str, filter_category: str = None, **kwargs):
        super().__init__(message, **kwargs)
        self.filter_category = filter_category


class InputFilteredError(ContentFilterError):
    """Raised when input content is filtered."""
    pass


class OutputFilteredError(ContentFilterError):
    """Raised when output content is filtered."""
    pass


class SafetyFilterError(ContentFilterError):
    """Raised when content triggers safety filters."""

    def __init__(self, message: str, safety_category: str = None, confidence_score: float = None, **kwargs):
        super().__init__(message, **kwargs)
        self.safety_category = safety_category
        self.confidence_score = confidence_score


# =============================================================================
# CONVERSATION ERRORS
# =============================================================================

class ConversationError(AIError):
    """Base class for conversation-related errors."""

    def __init__(self, message: str, conversation_id: str = None, **kwargs):
        super().__init__(message, **kwargs)
        self.conversation_id = conversation_id


class ConversationNotFoundError(ConversationError):
    """Raised when a conversation cannot be found."""
    pass


class ConversationLimitExceededError(ConversationError):
    """Raised when conversation limits are exceeded."""

    def __init__(self, message: str, current_count: int = None, limit: int = None, **kwargs):
        super().__init__(message, **kwargs)
        self.current_count = current_count
        self.limit = limit


class ContextWindowExceededError(ConversationError):
    """Raised when conversation context window is exceeded."""

    def __init__(self, message: str, context_length: int = None, max_length: int = None, **kwargs):
        super().__init__(message, **kwargs)
        self.context_length = context_length
        self.max_length = max_length


class InvalidConversationStateError(ConversationError):
    """Raised when conversation is in an invalid state."""

    def __init__(self, message: str, current_state: str = None, expected_state: str = None, **kwargs):
        super().__init__(message, **kwargs)
        self.current_state = current_state
        self.expected_state = expected_state


# =============================================================================
# FILE ERRORS
# =============================================================================

class FileError(AIError):
    """Base class for file-related errors."""

    def __init__(self, message: str, file_path: str = None, **kwargs):
        super().__init__(message, **kwargs)
        self.file_path = file_path


class FileNotFoundError(FileError):
    """Raised when a file cannot be found."""
    pass


class FileSizeLimitError(FileError):
    """Raised when file size exceeds limits."""

    def __init__(self, message: str, file_size: int = None, size_limit: int = None, **kwargs):
        super().__init__(message, **kwargs)
        self.file_size = file_size
        self.size_limit = size_limit


class UnsupportedFileTypeError(FileError):
    """Raised when a file type is not supported."""

    def __init__(self, message: str, file_type: str = None, supported_types: list = None, **kwargs):
        super().__init__(message, **kwargs)
        self.file_type = file_type
        self.supported_types = supported_types or []


class FileEncodingError(FileError):
    """Raised when file encoding is invalid."""

    def __init__(self, message: str, encoding: str = None, **kwargs):
        super().__init__(message, **kwargs)
        self.encoding = encoding


class FilePermissionError(FileError):
    """Raised when file permissions are insufficient."""
    pass