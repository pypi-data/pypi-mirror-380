"""AI provider implementations."""

from typing import Type
from ..core.base import BaseAIProvider
from ..core.exceptions import InvalidProviderError


def get_provider_class(provider_name: str) -> Type[BaseAIProvider]:
    """
    Get provider class by name.

    Args:
        provider_name: Name of the provider ("mock", "claude", "openai", "deepseek")

    Returns:
        Provider class

    Raises:
        InvalidProviderError: If provider is not supported
    """
    if provider_name == "mock":
        from .mock import MockProvider
        return MockProvider
    elif provider_name == "claude":
        from .claude import ClaudeProvider
        return ClaudeProvider
    elif provider_name == "openai":
        from .openai import OpenAIProvider
        return OpenAIProvider
    elif provider_name == "deepseek":
        from .deepseek import DeepSeekProvider
        return DeepSeekProvider
    else:
        raise InvalidProviderError(f"Unknown provider: {provider_name}")


__all__ = [
    "get_provider_class",
]