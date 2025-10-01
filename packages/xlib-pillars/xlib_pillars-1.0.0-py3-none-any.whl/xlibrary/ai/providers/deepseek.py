"""
DeepSeek Provider - DeepSeek API implementation.

Production-ready provider with full DeepSeek feature support including MoE architecture,
reasoning models (R1), cost-effective performance, and unified reasoning interface.
"""

import logging
from typing import List, Dict, Iterator, Optional, Any
from datetime import datetime
import re

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


class DeepSeekProvider(BaseAIProvider):
    """
    DeepSeek provider with full feature support.

    Supports DeepSeek MoE models with advanced capabilities:
    - 671B total parameters, 37B active per token (efficient MoE architecture)
    - Cost-effective performance: 20-100x cheaper than GPT-4
    - 128K context windows
    - Reasoning models with chain-of-thought (deepseek-reasoner/R1)
    - OpenAI-compatible API interface
    """

    # Complete DeepSeek model catalog
    DEEPSEEK_MODELS = {
        # Universal aliases mapping to DeepSeek models
        "latest": "deepseek-chat",           # V3 flagship model
        "current": "deepseek-chat",          # Current high-performance
        "fast": "deepseek-chat",             # Same model (already very fast)
        "reasoning": "deepseek-reasoner",    # R1 reasoning model

        # Direct model access - current production models
        "deepseek-chat": "deepseek-chat",
        "deepseek-reasoner": "deepseek-reasoner",

        # Convenient aliases
        "chat": "deepseek-chat",
        "reasoner": "deepseek-reasoner",
        "r1": "deepseek-reasoner"
    }

    def __init__(self, model: str = "current", api_key: Optional[str] = None, **kwargs):
        """Initialize DeepSeek provider with API key validation."""
        super().__init__(model, api_key, **kwargs)

        if not api_key:
            raise ConfigurationError("DeepSeek API key is required")

        self.api_key = api_key
        self._validate_api_key()

        # Initialize OpenAI-compatible client when needed
        self._client = None

        # Configuration from kwargs
        self.max_tokens_default = kwargs.get('max_tokens') or 4096

        logger.info(f"DeepSeek provider initialized with model {model}")

    @property
    def client(self):
        """Lazy initialization of DeepSeek client (OpenAI-compatible)."""
        if self._client is None:
            try:
                import openai
                # DeepSeek uses OpenAI-compatible API with custom base URL
                self._client = openai.OpenAI(
                    api_key=self.api_key,
                    base_url="https://api.deepseek.com"
                )
            except ImportError:
                raise ConfigurationError(
                    "openai package required for DeepSeek provider. "
                    "Install with: pip install openai"
                )
        return self._client

    def _validate_api_key(self):
        """Validate DeepSeek API key format."""
        if not isinstance(self.api_key, str):
            raise ConfigurationError("API key must be a string")

        if len(self.api_key) < 20:
            raise ConfigurationError("DeepSeek API key too short")

        if not self.api_key.startswith('sk-'):
            raise ConfigurationError(
                "Invalid DeepSeek API key format. Must start with 'sk-'"
            )

    def complete(self, messages: List[Message], enable_reasoning: bool = False, **kwargs) -> AIResponse:
        """Generate a complete response using DeepSeek."""
        try:
            # Prepare request parameters
            model = self._resolve_model(kwargs.get('model', self.model))
            max_tokens = kwargs.get('max_tokens', self.max_tokens_default)
            temperature = kwargs.get('temperature', 0.7)

            # For reasoning, switch to deepseek-reasoner if not already
            if enable_reasoning and model == "deepseek-chat":
                model = "deepseek-reasoner"

            # Prepare messages for DeepSeek API (OpenAI-compatible)
            deepseek_messages = self._prepare_messages(messages)

            # Build request
            request_params = {
                "model": model,
                "messages": deepseek_messages,
                "temperature": temperature,
                "max_tokens": max_tokens
            }

            # Add tools if provided (DeepSeek supports function calling)
            tools = kwargs.get('tools')
            if tools:
                request_params["tools"] = tools
                request_params["tool_choice"] = kwargs.get('tool_choice', 'auto')

            # Add structured output if provided
            response_format = kwargs.get('response_format')
            if response_format:
                request_params["response_format"] = response_format

            # Add stop sequences if provided
            stop = kwargs.get('stop')
            if stop:
                request_params["stop"] = stop

            # Make API call
            start_time = datetime.now()
            response = self.client.chat.completions.create(**request_params)

            # Parse and return response
            ai_response = self._parse_response(response, model, enable_reasoning)
            ai_response.latency_ms = (datetime.now() - start_time).total_seconds() * 1000

            return ai_response

        except Exception as e:
            # Import here to avoid circular imports
            import openai
            if isinstance(e, openai.APIError):
                raise self._map_deepseek_error(e)
            else:
                logger.error(f"Unexpected error in DeepSeek complete: {e}")
                raise ProviderError(f"DeepSeek provider error: {e}")

    def stream(self, messages: List[Message], **kwargs) -> Iterator[AIResponse]:
        """Stream response tokens as they are generated."""
        try:
            # Prepare request (similar to complete)
            model = self._resolve_model(kwargs.get('model', self.model))
            max_tokens = kwargs.get('max_tokens', self.max_tokens_default)
            temperature = kwargs.get('temperature', 0.7)

            deepseek_messages = self._prepare_messages(messages)

            request_params = {
                "model": model,
                "messages": deepseek_messages,
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
                            provider='deepseek',
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
                    provider='deepseek',
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
                raise self._map_deepseek_error(e)
            else:
                logger.error(f"Unexpected error in DeepSeek stream: {e}")
                raise ProviderError(f"DeepSeek streaming error: {e}")

    def count_tokens(self, text: str) -> int:
        """
        Count tokens for DeepSeek models.

        Note: Uses tiktoken approximation since DeepSeek doesn't provide
        a direct token counting API. DeepSeek uses similar tokenization to GPT models.
        """
        try:
            import tiktoken
            # Use cl100k_base as it's compatible with most models
            encoding = tiktoken.get_encoding("cl100k_base")
            return len(encoding.encode(text))
        except ImportError:
            # Fallback to approximation if tiktoken not available
            logger.warning("tiktoken not available, using approximation")
            return max(1, len(text) // 4)

    def get_models(self, real: bool = True, aliases: bool = True) -> Dict[str, str]:
        """Get available DeepSeek models."""
        result = {}

        if aliases:
            alias_keys = ["latest", "current", "fast", "reasoning"]
            result.update({
                k: f"Alias for {self.DEEPSEEK_MODELS[k]}"
                for k in alias_keys if k in self.DEEPSEEK_MODELS
            })

        if real:
            result.update({
                k: f"DeepSeek {k.replace('deepseek-', '').title()}" for k, v in self.DEEPSEEK_MODELS.items()
                if k.startswith("deepseek-")
            })

        return result

    def validate_model(self, model: str) -> bool:
        """Validate if model is available."""
        return model in self.DEEPSEEK_MODELS

    def estimate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """Estimate cost for DeepSeek API usage using centralized pricing."""
        return get_cost_estimate("deepseek", input_tokens, output_tokens)

    def get_capabilities(self) -> Dict[str, Any]:
        """Get DeepSeek provider capabilities using centralized feature matrix."""
        return get_provider_features("deepseek")

    def _resolve_model(self, model: str) -> str:
        """Resolve model alias to actual DeepSeek model name."""
        if model in self.DEEPSEEK_MODELS:
            return self.DEEPSEEK_MODELS[model]
        else:
            raise ModelUnavailableError(
                f"Model '{model}' not available for DeepSeek provider",
                suggested_replacement="current"
            )

    def _is_reasoning_model(self, model: str) -> bool:
        """Check if the model supports reasoning/chain-of-thought."""
        reasoning_models = {"deepseek-reasoner"}
        return model in reasoning_models

    def _prepare_messages(self, messages: List[Message]) -> List[Dict]:
        """
        Prepare messages for DeepSeek API format (OpenAI-compatible).

        DeepSeek accepts:
        - System, user, assistant messages
        - Content as string or structured format
        """
        deepseek_messages = []

        for message in messages:
            deepseek_message = {
                "role": message.role,
                "content": message.content
            }

            # Add name if present
            if hasattr(message, 'name') and message.name:
                deepseek_message["name"] = message.name

            deepseek_messages.append(deepseek_message)

        return deepseek_messages

    def _parse_response(self, response, model: str, enable_reasoning: bool = False) -> AIResponse:
        """Parse DeepSeek API response into our AIResponse format."""
        # Extract text content
        content = ""
        thinking_trace = None

        if hasattr(response, 'choices') and response.choices:
            choice = response.choices[0]
            if hasattr(choice, 'message') and choice.message:
                content = choice.message.content or ""

                # For deepseek-reasoner, extract thinking trace if available
                if model == "deepseek-reasoner" and enable_reasoning:
                    # DeepSeek reasoner may provide reasoning in special format
                    # Check if the response contains reasoning markers
                    if "<think>" in content and "</think>" in content:
                        think_match = re.search(r'<think>(.*?)</think>', content, re.DOTALL)
                        if think_match:
                            thinking_trace = think_match.group(1).strip()
                            # Remove thinking section from main content
                            content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()

        # Extract token usage
        input_tokens = 0
        output_tokens = 0

        if hasattr(response, 'usage'):
            input_tokens = getattr(response.usage, 'prompt_tokens', 0)
            output_tokens = getattr(response.usage, 'completion_tokens', 0)

        # Calculate cost estimate
        cost_estimate = self.estimate_cost(input_tokens, output_tokens)

        # Get finish reason
        finish_reason = 'stop'
        if hasattr(response, 'choices') and response.choices:
            choice = response.choices[0]
            finish_reason = getattr(choice, 'finish_reason', 'stop')

        return AIResponse(
            content=content,
            provider='deepseek',
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            tokens_used=input_tokens + output_tokens,
            cost_estimate=cost_estimate,
            thinking_trace=thinking_trace,
            finish_reason=finish_reason,
            metadata={
                'api_version': 'deepseek_v1',
                'supports_reasoning': self._is_reasoning_model(model),
                'moe_architecture': True,      # DeepSeek uses MoE
                'active_parameters': '37B',    # 37B active out of 671B total
                'total_parameters': '671B',
                'cost_effective': True
            }
        )

    def _map_deepseek_error(self, error) -> ProviderError:
        """Map DeepSeek API errors to our exception hierarchy."""
        import openai

        error_message = str(error)

        if hasattr(error, 'status_code'):
            status_code = error.status_code

            if status_code == 401:
                return AuthenticationError("Invalid DeepSeek API key")
            elif status_code == 429:
                retry_after = None
                if hasattr(error, 'response') and error.response:
                    retry_after = error.response.headers.get('retry-after')
                    if retry_after:
                        retry_after = int(retry_after)
                return RateLimitError("DeepSeek rate limit exceeded", retry_after)
            elif status_code == 400:
                if "maximum context length" in error_message.lower():
                    return TokenLimitExceededError("DeepSeek context length exceeded")
                elif "model" in error_message.lower() or "does not exist" in error_message.lower():
                    return ModelUnavailableError(
                        f"DeepSeek model error: {error_message}",
                        suggested_replacement="current"
                    )

        # Generic API error
        return ProviderError(f"DeepSeek API error: {error_message}")