"""Abstract base class for AI providers."""

from abc import ABC, abstractmethod
from typing import List, Dict, Iterator, Optional, Any
from .models import Message, AIResponse


class BaseAIProvider(ABC):
    """Abstract base class that all AI providers must implement."""

    def __init__(self, model: str, api_key: str, **kwargs):
        """Initialize the provider with a model and required API key configuration."""
        self.model = model
        self.api_key = api_key
        self.config = kwargs

    @abstractmethod
    def complete(self, messages: List[Message], enable_reasoning: bool = False, **kwargs) -> AIResponse:
        """
        Generate a complete response to the given messages.

        Args:
            messages: List of conversation messages
            enable_reasoning: If True, populate thinking_trace when available
            **kwargs: Provider-specific options like temperature, max_tokens, etc.

        Returns:
            AIResponse containing the generated content and metadata
        """
        pass

    @abstractmethod
    def stream(self, messages: List[Message], **kwargs) -> Iterator[AIResponse]:
        """
        Stream response tokens as they are generated.

        Args:
            messages: List of conversation messages
            **kwargs: Provider-specific options

        Yields:
            AIResponse: Response chunks with incremental content
        """
        pass

    @abstractmethod
    def count_tokens(self, text: str) -> int:
        """
        Count tokens in the given text.

        Args:
            text: Text to count tokens for

        Returns:
            int: Number of tokens
        """
        pass

    @abstractmethod
    def get_models(self, real: bool = True, aliases: bool = True) -> Dict[str, str]:
        """
        Get available models for this provider.

        Args:
            real: Include real/concrete model names
            aliases: Include universal aliases (latest, current, fast, reasoning)

        Returns:
            Dict mapping model names to their descriptions or actual model IDs
        """
        pass

    @abstractmethod
    def validate_model(self, model: str) -> bool:
        """
        Validate if a model is available for this provider.

        Args:
            model: Model name to validate

        Returns:
            bool: True if model is valid
        """
        pass

    def estimate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """
        Estimate cost for a request with given token counts.

        Args:
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens

        Returns:
            float: Estimated cost in USD
        """
        # Default implementation - providers should override with real pricing
        return 0.0

    @abstractmethod
    def get_capabilities(self) -> Dict[str, Any]:
        """
        Get capabilities supported by this provider.

        Each provider must implement this to return their specific capabilities
        using standardized capability names for cross-provider compatibility.

        Returns:
            Dict containing capability flags and limits
        """
        pass

    def __repr__(self) -> str:
        """String representation of the provider."""
        return f"{self.__class__.__name__}(model={self.model})"