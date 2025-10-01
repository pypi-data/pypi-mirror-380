"""Configuration classes for AI provider system."""

from dataclasses import dataclass, field
from typing import Dict, Any, Optional
import logging


@dataclass
class AIConfig:
    """Configuration for AI provider behavior."""

    # Core provider parameters
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None

    # Feature flags
    educational_mode: bool = False
    verbose_logging: bool = False
    conversation_logging: bool = True
    auto_extract_artifacts: bool = True

    # Logging configuration
    log_level: str = "INFO"
    log_format: Optional[str] = None

    # Rate limiting and resource management
    rate_limit_requests: Optional[int] = None
    max_history_length: int = 100
    max_concurrent_requests: int = 5

    # Provider-specific settings
    provider_config: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        """Set up logging based on configuration."""
        self._setup_logging()

    def _setup_logging(self):
        """Configure logging based on settings."""
        log_format = self.log_format or (
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            if self.verbose_logging else
            "%(levelname)s: %(message)s"
        )

        # Configure logging level
        numeric_level = getattr(logging, self.log_level.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError(f'Invalid log level: {self.log_level}')

        # Only set up if not already configured
        if not logging.getLogger().handlers:
            logging.basicConfig(
                level=numeric_level,
                format=log_format
            )

    def get_provider_setting(self, provider: str, setting: str, default: Any = None) -> Any:
        """Get provider-specific configuration setting."""
        return self.provider_config.get(provider, {}).get(setting, default)

    def set_provider_setting(self, provider: str, setting: str, value: Any):
        """Set provider-specific configuration setting."""
        if provider not in self.provider_config:
            self.provider_config[provider] = {}
        self.provider_config[provider][setting] = value

    def merge_with(self, other: 'AIConfig') -> 'AIConfig':
        """Merge this config with another, with other taking precedence."""
        # For merge, other config overrides base config
        new_provider_config = {**self.provider_config}
        for provider, settings in other.provider_config.items():
            if provider in new_provider_config:
                new_provider_config[provider].update(settings)
            else:
                new_provider_config[provider] = settings

        return AIConfig(
            temperature=other.temperature if other.temperature is not None else self.temperature,
            max_tokens=other.max_tokens if other.max_tokens is not None else self.max_tokens,
            top_p=other.top_p if other.top_p is not None else self.top_p,
            educational_mode=other.educational_mode,  # Boolean fields take other's value
            verbose_logging=other.verbose_logging,    # Boolean fields take other's value
            conversation_logging=other.conversation_logging,
            auto_extract_artifacts=other.auto_extract_artifacts,
            log_level=other.log_level if other.log_level != "INFO" else self.log_level,
            log_format=other.log_format or self.log_format,
            rate_limit_requests=other.rate_limit_requests if other.rate_limit_requests is not None else self.rate_limit_requests,
            max_history_length=other.max_history_length,
            max_concurrent_requests=other.max_concurrent_requests,
            provider_config=new_provider_config,
        )