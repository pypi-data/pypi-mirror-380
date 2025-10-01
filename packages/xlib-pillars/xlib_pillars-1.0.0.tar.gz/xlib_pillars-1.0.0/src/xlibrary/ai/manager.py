"""
AIManager - Main interface for AI provider abstraction system.

Provides clean constructor-first configuration with intelligent cascading updates.
"""

import logging
from typing import Dict, Optional, Any, List, Iterator, Union
from datetime import datetime

from .core.base import BaseAIProvider
from .core.config import AIConfig
from .core.models import Message, AIResponse
from .core.exceptions import (
    ConfigurationError,
    InvalidProviderError,
    InvalidModelError,
    MissingCredentialsError
)
from .session.conversation import Conversation
from .providers import get_provider_class
from .testing.manager_interface import TestingInterface
from .metrics import AIMetrics
from .health import HealthChecker
from .limits import RateLimiter, RateLimitConfig, RateLimitResult
from .logging import AILogger, LogConfig
from .features import (
    PROVIDER_FEATURES, check_feature_support, get_provider_features,
    get_model_capabilities, validate_provider_config, get_quality_assessment
)


logger = logging.getLogger(__name__)


class AIManager:
    """
    Main interface for AI provider interactions.

    Provides constructor-first configuration with intelligent property management
    and cascading updates when provider/model/key changes.
    """

    # Provider defaults for when switching providers
    PROVIDER_DEFAULTS = {
        "mock": "latest",
        "claude": "current",
        "openai": "current",
        "deepseek": "latest"
    }

    # Universal model aliases that work across all providers
    UNIVERSAL_ALIASES = {
        "latest": "Flagship model",
        "current": "High-performance model",
        "fast": "Efficient model",
        "reasoning": "Thinking-enabled model"
    }

    def __init__(
        self,
        api_key: str,
        provider: str = "claude",
        model: str = "latest",
        config: Optional[AIConfig] = None,
        metrics: Optional[AIMetrics] = None,
        enable_metrics: bool = False,
        health_checker: Optional[HealthChecker] = None,
        enable_health_checks: bool = False,
        rate_limiter: Optional[RateLimiter] = None,
        enable_rate_limiting: bool = False,
        rate_limit_config: Optional[RateLimitConfig] = None,
        provider_tier: Optional[str] = None,
        ai_logger: Optional[AILogger] = None,
        enable_logging: bool = False,
        log_config: Optional[LogConfig] = None,
        **kwargs
    ):
        """
        Initialize AIManager with credentials, provider, and configuration.

        Args:
            api_key: API key for the provider (required)
            provider: Provider name ("claude", "openai", "deepseek", "mock") - defaults to "claude"
            model: Model to use - defaults to "latest"
            config: AIConfig instance for advanced configuration
            metrics: AIMetrics instance for usage tracking (optional)
            enable_metrics: Create default metrics instance if True
            health_checker: HealthChecker instance for provider monitoring (optional)
            enable_health_checks: Create default health checker if True
            rate_limiter: RateLimiter instance for request throttling (optional)
            enable_rate_limiting: Create default rate limiter if True
            rate_limit_config: Rate limiting configuration (optional)
            provider_tier: Provider tier for rate limiting (free, pro, team, etc.)
            ai_logger: AILogger instance for structured logging (optional)
            enable_logging: Create default logger if True
            log_config: Logging configuration (optional)
            **kwargs: Additional configuration options
        """
        # Store immutable provider
        self._provider = provider
        self._validate_provider(provider)

        # Validate required API key
        if not api_key or not isinstance(api_key, str) or len(api_key.strip()) == 0:
            raise ConfigurationError("API key is required and must be a non-empty string")

        # Set up configuration
        self.config = config or AIConfig()
        if kwargs:
            # Merge any additional config from kwargs
            extra_config = AIConfig(**kwargs)
            self.config = self.config.merge_with(extra_config)

        # Set up mutable properties
        self._api_key = api_key
        self._model = model

        # Initialize provider instance
        self._provider_instance: Optional[BaseAIProvider] = None
        self._initialize_provider()

        # Active conversations tracking
        self._conversations: Dict[str, Conversation] = {}

        # Testing interface
        self.testing = TestingInterface(self._provider_instance)

        # Metrics system (optional)
        if metrics is not None:
            self.metrics = metrics
        elif enable_metrics:
            self.metrics = AIMetrics(backend="memory")
        else:
            self.metrics = None

        # Health checking system (optional)
        if health_checker is not None:
            self.health = health_checker
            # Register this provider with the health checker
            self.health.register_provider(self._provider, self._provider_instance)
        elif enable_health_checks:
            self.health = HealthChecker(
                providers=[self._provider],
                check_interval_seconds=60,  # Check every minute
                timeout_seconds=10
            )
            self.health.register_provider(self._provider, self._provider_instance)
        else:
            self.health = None

        # Rate limiting system (optional)
        if rate_limiter is not None:
            self.rate_limiter = rate_limiter
        elif enable_rate_limiting:
            self.rate_limiter = RateLimiter(
                provider=self._provider,
                config=rate_limit_config or RateLimitConfig(),
                provider_tier=provider_tier,
                metrics=self.metrics,
                health_checker=self.health
            )
        else:
            self.rate_limiter = None

        # Advanced logging system (optional)
        if ai_logger is not None:
            self.logging = ai_logger
        elif enable_logging:
            self.logging = AILogger.get_logger(
                name="manager",
                config=log_config or LogConfig(enabled=True)
            )
        else:
            self.logging = None

        logger.info(f"AIManager initialized: {provider} with model {self._model}")

    def _validate_provider(self, provider: str):
        """Validate provider is supported."""
        supported_providers = ["mock", "claude", "openai", "deepseek"]
        if provider not in supported_providers:
            raise InvalidProviderError(
                f"Provider '{provider}' not supported. "
                f"Supported providers: {supported_providers}"
            )

    def _initialize_provider(self):
        """Initialize the provider instance."""
        try:
            provider_class = get_provider_class(self._provider)
            self._provider_instance = provider_class(
                model=self._model,
                api_key=self._api_key,
                **self.config.__dict__
            )
        except Exception as e:
            logger.error(f"Failed to initialize {self._provider} provider: {e}")
            raise ConfigurationError(f"Could not initialize {self._provider} provider: {e}")

    @property
    def provider(self) -> str:
        """Get current provider (immutable after construction)."""
        return self._provider

    @property
    def model(self) -> str:
        """Get current model."""
        return self._model

    @model.setter
    def model(self, value: str):
        """Set model (validates against current provider)."""
        if not self._provider_instance.validate_model(value):
            raise InvalidModelError(f"Model '{value}' not valid for provider '{self._provider}'")

        self._model = value
        self._provider_instance.model = value
        logger.info(f"Model changed to: {value}")

    @property
    def api_key(self) -> Optional[str]:
        """Get current API key (masked for security)."""
        if self._api_key:
            return f"sk-...{self._api_key[-4:]}"
        return None

    @api_key.setter
    def api_key(self, value: str):
        """Set API key."""
        if not value or not isinstance(value, str) or len(value.strip()) == 0:
            raise ConfigurationError("API key must be a non-empty string")
        self._api_key = value
        if self._provider_instance:
            self._provider_instance.api_key = value
        logger.info("API key updated")

    def get_models(self, real: bool = True, aliases: bool = True) -> Dict[str, str]:
        """
        Get available models for current provider.

        Args:
            real: Include concrete model names
            aliases: Include universal aliases

        Returns:
            Dict mapping model names to descriptions
        """
        if not self._provider_instance:
            return {}

        return self._provider_instance.get_models(real=real, aliases=aliases)

    def models(self, real: bool = True, aliases: bool = True) -> Dict[str, str]:
        """
        Alias for get_models() for design document compatibility.

        Args:
            real: Include concrete model names
            aliases: Include universal aliases

        Returns:
            Dict mapping model names to descriptions
        """
        return self.get_models(real=real, aliases=aliases)

    def validate_model(self, model: str) -> bool:
        """
        Validate if a model is available for current provider.

        Args:
            model: Model name to validate

        Returns:
            bool: True if model is valid
        """
        if not self._provider_instance:
            return False

        return self._provider_instance.validate_model(model)

    def request(
        self,
        prompt: str,
        enable_reasoning: bool = False,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        top_p: Optional[float] = None,
        **kwargs
    ) -> AIResponse:
        """
        Make a stateless request to the AI provider.

        Args:
            prompt: The input prompt
            enable_reasoning: Enable thinking trace if supported
            temperature: Override default temperature
            max_tokens: Override default max tokens
            top_p: Override default top_p
            **kwargs: Additional provider-specific parameters

        Returns:
            AIResponse with the generated content and metadata
        """
        if not self._provider_instance:
            raise ConfigurationError("Provider not initialized")

        # Build request parameters first, preferring method args over config defaults
        request_params = {}
        if temperature is not None:
            request_params['temperature'] = temperature
        elif self.config.temperature is not None:
            request_params['temperature'] = self.config.temperature

        if max_tokens is not None:
            request_params['max_tokens'] = max_tokens
        elif self.config.max_tokens is not None:
            request_params['max_tokens'] = self.config.max_tokens

        if top_p is not None:
            request_params['top_p'] = top_p
        elif self.config.top_p is not None:
            request_params['top_p'] = self.config.top_p

        # Add any additional kwargs
        request_params.update(kwargs)

        # Generate request ID and estimate tokens
        request_id = f"{self._provider}_{int(datetime.now().timestamp() * 1000)}"
        tokens_estimate = self.count_tokens(prompt) if hasattr(self, 'count_tokens') else len(prompt) // 4

        # Log request start if logging enabled
        if self.logging:
            self.logging.log_ai_request(
                provider=self._provider,
                model=self._model,
                prompt=prompt,
                enable_reasoning=enable_reasoning,
                request_id=request_id,
                estimated_tokens=tokens_estimate,
                **request_params
            )

        # Rate limiting check

        if self.rate_limiter:
            rate_limit_result = self.rate_limiter.check_rate_limit(request_id, tokens_estimate)

            if rate_limit_result == RateLimitResult.REJECTED:
                from .core.exceptions import RateLimitError
                raise RateLimitError("Request rejected due to rate limiting")
            elif rate_limit_result == RateLimitResult.BACKOFF:
                from .core.exceptions import RateLimitError
                backoff_delay = self.rate_limiter.get_backoff_delay()
                raise RateLimitError(f"Request requires backoff: {backoff_delay:.1f}s",
                                   backoff_delay=backoff_delay)
            elif rate_limit_result == RateLimitResult.QUEUED:
                from .core.exceptions import RateLimitError
                raise RateLimitError("Request has been queued due to rate limiting")

            # Consume tokens if allowed
            if not self.rate_limiter.consume_tokens(request_id, tokens_estimate):
                from .core.exceptions import RateLimitError
                raise RateLimitError("Failed to consume rate limit tokens")

        # Create messages and make request
        messages = [Message(role="user", content=prompt)]

        start_time = datetime.now()

        # Use logging operation context if available
        if self.logging:
            with self.logging.operation("ai_request",
                                      provider=self._provider,
                                      model=self._model,
                                      request_id=request_id) as operation_id:
                try:
                    response = self._provider_instance.complete(
                        messages=messages,
                        enable_reasoning=enable_reasoning,
                        **request_params
                    )
                    success = True
                    error_type = None
                except Exception as e:
                    success = False
                    error_type = type(e).__name__

                    # Log the error
                    self.logging.log_ai_error(
                        provider=self._provider,
                        model=self._model,
                        error=e,
                        request_id=request_id,
                        operation_id=operation_id
                    )
                    raise
        else:
            try:
                response = self._provider_instance.complete(
                    messages=messages,
                    enable_reasoning=enable_reasoning,
                    **request_params
                )
                success = True
                error_type = None
            except Exception as e:
                # Re-raise the exception after recording metrics
                success = False
                error_type = type(e).__name__
                # Record error metrics before re-raising
                if self.metrics:
                    duration_seconds = (datetime.now() - start_time).total_seconds()
                    self.metrics.record_request(
                        provider=self._provider,
                        model=self._model,
                        duration_seconds=duration_seconds,
                        success=False,
                        error_type=error_type
                    )

                # Release rate limiter on failure
                if self.rate_limiter:
                    self.rate_limiter.release_request(request_id, success=False)

                raise

        end_time = datetime.now()

        # Add timing information
        response.latency_ms = (end_time - start_time).total_seconds() * 1000
        duration_seconds = response.latency_ms / 1000

        # Extract artifacts if enabled
        if self.config.auto_extract_artifacts:
            response.extract_artifacts()

        # Record metrics if enabled
        if self.metrics:
            self.metrics.record_request(
                provider=self._provider,
                model=self._model,
                duration_seconds=duration_seconds,
                tokens_used=response.tokens_used,
                cost_estimate=response.cost_estimate,
                success=success,
                error_type=error_type
            )

        # Release rate limiter on success
        if self.rate_limiter:
            self.rate_limiter.release_request(request_id, success=True)

        # Log successful response
        if self.logging:
            self.logging.log_ai_response(
                provider=self._provider,
                model=self._model,
                response_length=len(response.content),
                tokens_used=response.tokens_used,
                cost=response.cost_estimate or 0.0,
                latency_ms=response.latency_ms,
                request_id=request_id,
                reasoning_enabled=enable_reasoning,
                artifacts_count=len(response.artifacts) if hasattr(response, 'artifacts') and response.artifacts else 0
            )

        logger.info(f"Request completed: {len(response.content)} chars, "
                   f"{response.tokens_used} tokens, {response.latency_ms:.1f}ms")

        return response

    def request_stream(
        self,
        prompt: str,
        enable_reasoning: bool = False,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        top_p: Optional[float] = None,
        stop_sequences: Optional[List[str]] = None,
        stream_chunk_size: int = 1024,
        include_usage_in_chunks: bool = False,
        timeout: Optional[float] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Iterator[AIResponse]:
        """
        Make a streaming request to the AI provider.

        Args:
            prompt: The input prompt
            enable_reasoning: Enable reasoning mode if supported
            temperature: Override default temperature
            max_tokens: Override default max tokens
            top_p: Nucleus sampling parameter
            stop_sequences: List of sequences where generation should stop
            stream_chunk_size: Target size of each chunk (characters)
            include_usage_in_chunks: Include token usage info in each chunk
            timeout: Request timeout in seconds
            metadata: Additional metadata for the request
            **kwargs: Additional provider-specific parameters

        Yields:
            AIResponse chunks as they are generated
        """
        if not self._provider_instance:
            raise ConfigurationError("Provider not initialized")

        # Build comprehensive request parameters matching design document
        request_params = {}

        # Core parameters
        if temperature is not None:
            request_params['temperature'] = temperature
        elif self.config.temperature is not None:
            request_params['temperature'] = self.config.temperature

        if max_tokens is not None:
            request_params['max_tokens'] = max_tokens
        elif self.config.max_tokens is not None:
            request_params['max_tokens'] = self.config.max_tokens

        # Advanced parameters from design document
        if top_p is not None:
            request_params['top_p'] = top_p

        if stop_sequences is not None:
            request_params['stop'] = stop_sequences

        if enable_reasoning:
            request_params['enable_reasoning'] = enable_reasoning

        if timeout is not None:
            request_params['timeout'] = timeout

        # Streaming-specific parameters
        request_params['stream_chunk_size'] = stream_chunk_size
        request_params['include_usage_in_chunks'] = include_usage_in_chunks

        # Metadata
        if metadata is not None:
            request_params['metadata'] = metadata

        # Add additional parameters
        request_params.update(kwargs)

        # Create messages and stream
        messages = [Message(role="user", content=prompt)]
        if metadata:
            messages[0].metadata.update(metadata)

        logger.info(f"Streaming request: {len(prompt)} chars, reasoning={enable_reasoning}")

        start_time = datetime.now()
        chunk_count = 0
        total_tokens = 0
        total_cost = 0.0

        try:
            for chunk in self._provider_instance.stream(messages=messages, **request_params):
                chunk_count += 1

                # Track tokens and cost from chunks
                if hasattr(chunk, 'tokens_used') and chunk.tokens_used:
                    total_tokens += chunk.tokens_used
                if hasattr(chunk, 'cost_estimate') and chunk.cost_estimate:
                    total_cost += chunk.cost_estimate

                # Enhance chunk with streaming metadata if requested
                if include_usage_in_chunks:
                    chunk.metadata = chunk.metadata or {}
                    chunk.metadata['streaming'] = {
                        'chunk_size_target': stream_chunk_size,
                        'include_usage': include_usage_in_chunks
                    }

                yield chunk

            # Record streaming metrics after completion
            if self.metrics:
                duration_seconds = (datetime.now() - start_time).total_seconds()
                self.metrics.record_request(
                    provider=self._provider,
                    model=self._model,
                    duration_seconds=duration_seconds,
                    tokens_used=total_tokens,
                    cost_estimate=total_cost,
                    success=True
                )
                self.metrics.record_streaming(
                    provider=self._provider,
                    model=self._model,
                    chunks_count=chunk_count
                )

        except Exception as e:
            # Record error metrics for streaming
            if self.metrics:
                duration_seconds = (datetime.now() - start_time).total_seconds()
                self.metrics.record_request(
                    provider=self._provider,
                    model=self._model,
                    duration_seconds=duration_seconds,
                    tokens_used=total_tokens,
                    cost_estimate=total_cost,
                    success=False,
                    error_type=type(e).__name__
                )
            raise

    def start_conversation(
        self,
        conversation_id: Optional[str] = None,
        system_message: Optional[str] = None,
        **kwargs
    ) -> Conversation:
        """
        Start a new stateful conversation.

        Args:
            conversation_id: Optional unique ID for the conversation
            system_message: Optional system message to set context
            **kwargs: Additional conversation parameters

        Returns:
            Conversation instance for stateful interactions
        """
        if not self._provider_instance:
            raise ConfigurationError("Provider not initialized")

        conversation = Conversation(
            provider=self._provider_instance,
            config=self.config,
            conversation_id=conversation_id,
            system_message=system_message,
            **kwargs
        )

        # Track active conversation
        self._conversations[conversation.conversation_id] = conversation

        # Update conversation metrics
        if self.metrics:
            self.metrics.record_conversation(self._provider, len(self._conversations))

        logger.info(f"Started conversation: {conversation.conversation_id}")
        return conversation

    def get_capabilities(self) -> Dict[str, Any]:
        """
        Get comprehensive capabilities of the current provider.

        Returns:
            Dict with all provider capabilities from the feature matrix
        """
        return get_provider_features(self._provider)

    def check_feature_support(self, feature: str) -> bool:
        """
        Check if the current provider supports a specific feature.

        Args:
            feature: Feature name to check (e.g., 'reasoning_mode', 'streaming', 'json_mode')

        Returns:
            bool: True if the feature is supported, False otherwise

        Example:
            if ai.check_feature_support('reasoning_mode'):
                response = ai.request(prompt, enable_reasoning=True)
            else:
                response = ai.request(f"Think step by step: {prompt}")
        """
        return check_feature_support(self._provider, feature)

    def get_model_capabilities(self, model: Optional[str] = None) -> Dict[str, Any]:
        """
        Get model-specific capabilities for the current provider.

        Args:
            model: Specific model name (uses current model if None)

        Returns:
            Dict with model capabilities including context limits and features
        """
        model_to_check = model or self._model
        return get_model_capabilities(self._provider, model_to_check)

    def get_feature_matrix(self) -> Dict[str, Any]:
        """
        Get the complete feature matrix for the current provider.

        Returns:
            Dict with all features and their support status
        """
        return PROVIDER_FEATURES.get(self._provider, {}).copy()

    def validate_configuration(self) -> List[str]:
        """
        Validate current configuration against provider capabilities.

        Returns:
            List of validation warnings/errors
        """
        config_dict = {
            'max_tokens': self.config.max_tokens,
            'temperature': self.config.temperature,
            'top_p': self.config.top_p,
            # Add other relevant config parameters
        }

        return validate_provider_config(self._provider, config_dict)

    def get_supported_models(self) -> List[str]:
        """
        Get list of models supported by the current provider.

        Returns:
            List of available model names
        """
        features = PROVIDER_FEATURES.get(self._provider, {})
        return features.get('available_models', [])

    def supports_reasoning(self, model: Optional[str] = None) -> bool:
        """
        Check if reasoning mode is supported for the specified model.

        Args:
            model: Model to check (uses current model if None)

        Returns:
            bool: True if reasoning is supported for this model
        """
        model_to_check = model or self._model
        features = PROVIDER_FEATURES.get(self._provider, {})
        reasoning_models = features.get('reasoning_models', [])

        return (
            features.get('reasoning_mode', False) and
            (not reasoning_models or model_to_check in reasoning_models)
        )

    def supports_vision(self, model: Optional[str] = None) -> bool:
        """
        Check if vision/image input is supported for the specified model.

        Args:
            model: Model to check (uses current model if None)

        Returns:
            bool: True if vision is supported for this model
        """
        model_to_check = model or self._model
        features = PROVIDER_FEATURES.get(self._provider, {})
        vision_models = features.get('vision_models', [])

        return (
            features.get('image_input', False) and
            (not vision_models or model_to_check in vision_models)
        )

    def supports_streaming(self) -> bool:
        """
        Check if the current provider supports streaming responses.

        Returns:
            bool: True if streaming is supported
        """
        return check_feature_support(self._provider, 'streaming')

    def get_rate_limits(self) -> Dict[str, Union[int, float]]:
        """
        Get rate limiting information for the current provider.

        Returns:
            Dict with rate limiting parameters
        """
        features = PROVIDER_FEATURES.get(self._provider, {})
        return {
            'requests_per_minute': features.get('requests_per_minute', 0),
            'tokens_per_minute': features.get('tokens_per_minute', 0),
            'concurrent_requests': features.get('concurrent_requests', 0)
        }

    def get_quality_metrics(self) -> Dict[str, str]:
        """
        Get quality assessment for the current provider.

        Returns:
            Dict with quality metrics
        """
        return get_quality_assessment(self._provider)

    def get_context_limits(self) -> Dict[str, int]:
        """
        Get context window and output limits for the current provider.

        Returns:
            Dict with token limits
        """
        features = PROVIDER_FEATURES.get(self._provider, {})
        return {
            'max_context_tokens': features.get('max_context_tokens', 0),
            'max_output_tokens': features.get('max_output_tokens', 0)
        }

    def estimate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """
        Estimate cost for a request with given token counts.

        Args:
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens

        Returns:
            Estimated cost in USD
        """
        from .features import get_cost_estimate
        return get_cost_estimate(self._provider, input_tokens, output_tokens)

    def count_tokens(self, text: str) -> int:
        """Count tokens in text using provider's tokenizer."""
        if not self._provider_instance:
            # Rough estimate: ~4 characters per token
            return len(text) // 4
        return self._provider_instance.count_tokens(text)

    def get_active_conversations(self) -> List[str]:
        """Get IDs of all active conversations."""
        return list(self._conversations.keys())

    def get_conversation(self, conversation_id: str) -> Optional[Conversation]:
        """Get a specific conversation by ID."""
        return self._conversations.get(conversation_id)

    def close_conversation(self, conversation_id: str):
        """Close and remove a conversation."""
        if conversation_id in self._conversations:
            del self._conversations[conversation_id]

            # Update conversation metrics
            if self.metrics:
                self.metrics.record_conversation(self._provider, len(self._conversations))

            logger.info(f"Closed conversation: {conversation_id}")

    def test(self, **kwargs):
        """
        Backward compatibility shortcut for ai.testing.perform().

        Args:
            **kwargs: All arguments passed to ai.testing.perform()

        Returns:
            TestSuiteResults with complete test outcomes

        Example:
            results = ai.test()  # Same as ai.testing.perform()
        """
        return self.testing.perform(**kwargs)

    def __repr__(self) -> str:
        """String representation of AIManager."""
        return f"AIManager(provider={self._provider}, model={self._model})"