"""
OpenAI Provider - OpenAI API implementation.

Production-ready provider with full OpenAI feature support including GPT-4o,
reasoning models (o1, o1-mini), structured outputs, and function calling.
"""

import logging
from typing import List, Dict, Iterator, Optional, Any
from datetime import datetime

from ..core.base import BaseAIProvider
from ..core.models import Message, AIResponse
from ..core.exceptions import (
    ConfigurationError,
    RateLimitError,
    TokenLimitExceededError,
    ModelUnavailableError,
    ProviderError,
    AuthenticationError
)
from ..features import get_provider_features, get_cost_estimate

logger = logging.getLogger(__name__)


class OpenAIProvider(BaseAIProvider):
    """
    OpenAI provider with full feature support.

    Supports GPT-4o family and reasoning models with advanced capabilities:
    - Extended context (128K tokens for GPT-4o)
    - Reasoning models with chain-of-thought (o1, o1-mini)
    - Structured outputs with JSON schema validation
    - Function calling and tool use
    - Vision capabilities (GPT-4o)
    """

    # Complete OpenAI model catalog - all current production models
    OPENAI_MODELS = {
        # Universal aliases mapping to current flagship models
        "latest": "gpt-4o",                    # Current flagship
        "current": "gpt-4o",                   # High-performance
        "fast": "gpt-4o-mini",                 # Fast processing
        "reasoning": "o1-mini",                # Reasoning model

        # Direct model access - GPT-4o family (mapping to themselves for consistency)
        "gpt-4o": "gpt-4o",
        "gpt-4o-mini": "gpt-4o-mini",
        "gpt-4-turbo": "gpt-4-turbo",
        "gpt-4": "gpt-4",

        # Reasoning models
        "o1": "o1",
        "o1-mini": "o1-mini",

        # Legacy models
        "gpt-3.5-turbo": "gpt-3.5-turbo",

        # Convenient aliases
        "4o": "gpt-4o",
        "4o-mini": "gpt-4o-mini",
        "turbo": "gpt-4-turbo"
    }

    def __init__(self, model: str = "current", api_key: Optional[str] = None, **kwargs):
        """Initialize OpenAI provider with API key validation."""
        super().__init__(model, api_key, **kwargs)

        if not api_key:
            raise ConfigurationError("OpenAI API key is required")

        self.api_key = api_key
        self._validate_api_key()

        # Initialize OpenAI client when needed
        self._client = None

        # Configuration from kwargs
        self.max_tokens_default = kwargs.get('max_tokens') or 4096
        self.use_json_mode = kwargs.get('use_json_mode', True)

        logger.info(f"OpenAI provider initialized with model {model}")

    @property
    def client(self):
        """Lazy initialization of OpenAI client."""
        if self._client is None:
            try:
                import openai
                self._client = openai.OpenAI(api_key=self.api_key)
            except ImportError:
                raise ConfigurationError(
                    "openai package required for OpenAI provider. "
                    "Install with: pip install openai"
                )
        return self._client

    def _validate_api_key(self):
        """Validate OpenAI API key format."""
        if not isinstance(self.api_key, str):
            raise ConfigurationError("API key must be a string")

        if len(self.api_key) < 20:
            raise ConfigurationError("OpenAI API key too short")

        if not self.api_key.startswith(('sk-', 'sk-proj-')):
            raise ConfigurationError(
                "Invalid OpenAI API key format. Must start with 'sk-' or 'sk-proj-'"
            )

    def complete(self, messages: List[Message], enable_reasoning: bool = False, **kwargs) -> AIResponse:
        """Generate a complete response using OpenAI."""
        try:
            # Prepare request parameters
            model = self._resolve_model(kwargs.get('model', self.model))
            max_tokens = kwargs.get('max_tokens', self.max_tokens_default)
            temperature = kwargs.get('temperature', 0.7)

            # Check if we should use reasoning mode
            is_reasoning_model = self._is_reasoning_model(model)
            if enable_reasoning and not is_reasoning_model:
                # For non-reasoning models, add reasoning instruction
                messages = self._add_reasoning_instruction(messages)

            # Prepare messages for OpenAI's format
            openai_messages = self._prepare_messages(messages)

            # Build request
            request_params = {
                "model": model,
                "messages": openai_messages,
                "temperature": temperature
            }

            # Add max_tokens for non-reasoning models (reasoning models don't support it)
            if not is_reasoning_model:
                request_params["max_tokens"] = max_tokens

            # Add tools if provided
            tools = kwargs.get('tools')
            if tools and not is_reasoning_model:  # Reasoning models don't support tools yet
                request_params["tools"] = tools
                request_params["tool_choice"] = kwargs.get('tool_choice', 'auto')

            # Add structured output if provided
            response_format = kwargs.get('response_format')
            if response_format and self.use_json_mode and not is_reasoning_model:
                request_params["response_format"] = response_format

            # Add stop sequences if provided
            stop = kwargs.get('stop')
            if stop and not is_reasoning_model:
                request_params["stop"] = stop

            # Make API call
            start_time = datetime.now()
            response = self.client.chat.completions.create(**request_params)

            # Parse and return response
            ai_response = self._parse_response(response, model, is_reasoning_model)
            ai_response.latency_ms = (datetime.now() - start_time).total_seconds() * 1000

            return ai_response

        except Exception as e:
            # Import here to avoid circular imports
            import openai
            if isinstance(e, openai.APIError):
                raise self._map_openai_error(e)
            else:
                logger.error(f"Unexpected error in OpenAI complete: {e}")
                raise ProviderError(f"OpenAI provider error: {e}")

    def stream(self, messages: List[Message], **kwargs) -> Iterator[AIResponse]:
        """Stream response tokens as they are generated."""
        try:
            # Prepare request (similar to complete)
            model = self._resolve_model(kwargs.get('model', self.model))
            max_tokens = kwargs.get('max_tokens', self.max_tokens_default)
            temperature = kwargs.get('temperature', 0.7)

            # Reasoning models don't support streaming
            if self._is_reasoning_model(model):
                raise ConfigurationError(f"Model {model} does not support streaming")

            openai_messages = self._prepare_messages(messages)

            request_params = {
                "model": model,
                "messages": openai_messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "stream": True
            }

            # Stream the response
            accumulated_content = ""
            chunk_index = 0

            stream = self.client.chat.completions.create(**request_params)

            for chunk in stream:
                if hasattr(chunk, 'choices') and chunk.choices:
                    delta = chunk.choices[0].delta
                    if hasattr(delta, 'content') and delta.content:
                        chunk_text = delta.content
                        accumulated_content += chunk_text

                        # Create streaming response chunk
                        yield AIResponse(
                            content=accumulated_content,
                            provider='openai',
                            model=model,
                            is_streaming=True,
                            chunk_index=chunk_index,
                            is_final_chunk=False,
                            input_tokens=0,  # Not available during streaming
                            output_tokens=chunk_index + 1,
                            tokens_used=chunk_index + 1
                        )

                        chunk_index += 1

            # Send final chunk
            if accumulated_content:
                yield AIResponse(
                    content=accumulated_content,
                    provider='openai',
                    model=model,
                    is_streaming=True,
                    chunk_index=chunk_index,
                    is_final_chunk=True,
                    output_tokens=chunk_index,
                    tokens_used=chunk_index,
                    finish_reason="stop"
                )

        except Exception as e:
            import openai
            if isinstance(e, openai.APIError):
                raise self._map_openai_error(e)
            else:
                logger.error(f"Unexpected error in OpenAI stream: {e}")
                raise ProviderError(f"OpenAI streaming error: {e}")

    def count_tokens(self, text: str) -> int:
        """
        Count tokens using tiktoken for OpenAI models.

        Note: Uses cl100k_base encoding which is appropriate for most OpenAI models.
        """
        try:
            import tiktoken
            encoding = tiktoken.get_encoding("cl100k_base")
            return len(encoding.encode(text))
        except ImportError:
            # Fallback to approximation if tiktoken not available
            logger.warning("tiktoken not available, using approximation")
            return max(1, len(text) // 4)

    def get_models(self, real: bool = True, aliases: bool = True) -> Dict[str, str]:
        """Get available OpenAI models."""
        result = {}

        if aliases:
            alias_keys = ["latest", "current", "fast", "reasoning"]
            result.update({
                k: f"Alias for {self.OPENAI_MODELS[k]}"
                for k in alias_keys if k in self.OPENAI_MODELS
            })

        if real:
            result.update({
                k: f"OpenAI {k.upper()}" for k, v in self.OPENAI_MODELS.items()
                if k.startswith(("gpt-", "o1"))
            })

        return result

    def validate_model(self, model: str) -> bool:
        """Validate if model is available."""
        return model in self.OPENAI_MODELS

    def estimate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """Estimate cost for OpenAI API usage using centralized pricing."""
        return get_cost_estimate("openai", input_tokens, output_tokens)

    def get_capabilities(self) -> Dict[str, Any]:
        """Get OpenAI provider capabilities using centralized feature matrix."""
        return get_provider_features("openai")

    def _resolve_model(self, model: str) -> str:
        """Resolve model alias to actual OpenAI model name."""
        if model in self.OPENAI_MODELS:
            return self.OPENAI_MODELS[model]
        else:
            raise ModelUnavailableError(
                f"Model '{model}' not available for OpenAI provider",
                suggested_replacement="current"
            )

    def _is_reasoning_model(self, model: str) -> bool:
        """Check if the model is a reasoning model (o1, o1-mini)."""
        reasoning_models = {"o1", "o1-mini"}
        return model in reasoning_models

    def _add_reasoning_instruction(self, messages: List[Message]) -> List[Message]:
        """Add reasoning instruction for non-reasoning models."""
        # Add a system message encouraging step-by-step thinking
        reasoning_msg = Message(
            role="system",
            content="Think step by step and show your reasoning process."
        )
        return [reasoning_msg] + messages

    def _prepare_messages(self, messages: List[Message]) -> List[Dict]:
        """
        Prepare messages for OpenAI's API format.

        OpenAI accepts:
        - System, user, assistant messages
        - Content as string or structured format
        """
        openai_messages = []

        for message in messages:
            openai_message = {
                "role": message.role,
                "content": message.content
            }

            # Add name if present
            if hasattr(message, 'name') and message.name:
                openai_message["name"] = message.name

            openai_messages.append(openai_message)

        return openai_messages

    def _parse_response(self, response, model: str, is_reasoning_model: bool = False) -> AIResponse:
        """Parse OpenAI API response into our AIResponse format."""
        # Extract text content
        content = ""
        thinking_trace = None

        if hasattr(response, 'choices') and response.choices:
            choice = response.choices[0]
            if hasattr(choice, 'message') and choice.message:
                content = choice.message.content or ""

                # For reasoning models, extract thinking trace if available
                if is_reasoning_model and hasattr(choice.message, 'reasoning'):
                    thinking_trace = choice.message.reasoning

        # Extract token usage
        input_tokens = 0
        output_tokens = 0
        reasoning_tokens = 0

        if hasattr(response, 'usage'):
            input_tokens = getattr(response.usage, 'prompt_tokens', 0)
            output_tokens = getattr(response.usage, 'completion_tokens', 0)

            # Reasoning models may have additional reasoning tokens
            if is_reasoning_model:
                reasoning_tokens = getattr(response.usage, 'reasoning_tokens', 0)

        # Calculate cost estimate
        cost_estimate = self.estimate_cost(input_tokens, output_tokens)

        # Get finish reason
        finish_reason = 'stop'
        if hasattr(response, 'choices') and response.choices:
            choice = response.choices[0]
            finish_reason = getattr(choice, 'finish_reason', 'stop')

        return AIResponse(
            content=content,
            provider='openai',
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            reasoning_tokens=reasoning_tokens,
            tokens_used=input_tokens + output_tokens + reasoning_tokens,
            cost_estimate=cost_estimate,
            thinking_trace=thinking_trace,
            finish_reason=finish_reason,
            metadata={
                'api_version': 'chat_completions',
                'is_reasoning_model': is_reasoning_model,
                'supports_streaming': not is_reasoning_model
            }
        )

    def _map_openai_error(self, error) -> ProviderError:
        """Map OpenAI API errors to our exception hierarchy."""
        import openai

        error_message = str(error)

        if hasattr(error, 'status_code'):
            status_code = error.status_code

            if status_code == 401:
                return AuthenticationError("Invalid OpenAI API key")
            elif status_code == 429:
                retry_after = None
                if hasattr(error, 'response') and error.response:
                    retry_after = error.response.headers.get('retry-after')
                    if retry_after:
                        retry_after = int(retry_after)
                return RateLimitError("OpenAI rate limit exceeded", retry_after)
            elif status_code == 400:
                if "maximum context length" in error_message.lower():
                    return TokenLimitExceededError("OpenAI context length exceeded")
                elif "model" in error_message.lower() or "does not exist" in error_message.lower():
                    return ModelUnavailableError(
                        f"OpenAI model error: {error_message}",
                        suggested_replacement="current"
                    )

        # Generic API error
        return ProviderError(f"OpenAI API error: {error_message}")