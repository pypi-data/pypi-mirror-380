"""
AI Pillar - Multi-provider AI abstraction layer

Provides unified interface for:
- Claude (Anthropic)
- OpenAI (GPT models)
- DeepSeek
- Mock provider (for testing)

Features:
- Stateless and stateful conversations
- Streaming support
- Reasoning mode support
- File attachments
- Cost tracking and token management
"""

from .manager import AIManager
from .core.models import Message, AIResponse, Artifact, ArtifactType, AIErrorCodes
from .core.config import AIConfig
from .core.base import BaseAIProvider
from .core.exceptions import (
    AIError,
    ConfigurationError,
    InvalidProviderError,
    InvalidModelError,
    MissingCredentialsError,
    ProviderError,
    AuthenticationError,
    RateLimitError,
    ModelUnavailableError,
    RequestError,
    ValidationError,
    TimeoutError,
    ConversationError,
    FileError
)
from .session.conversation import Conversation, ChainableRequest

__version__ = "1.0.0"
__all__ = [
    # Main classes
    "AIManager",
    "AIConfig",
    "Conversation",
    "ChainableRequest",

    # Core models
    "Message",
    "AIResponse",
    "Artifact",
    "ArtifactType",
    "AIErrorCodes",

    # Base classes
    "BaseAIProvider",

    # Exceptions
    "AIError",
    "ConfigurationError",
    "InvalidProviderError",
    "InvalidModelError",
    "MissingCredentialsError",
    "ProviderError",
    "AuthenticationError",
    "RateLimitError",
    "ModelUnavailableError",
    "RequestError",
    "ValidationError",
    "TimeoutError",
    "ConversationError",
    "FileError"
]