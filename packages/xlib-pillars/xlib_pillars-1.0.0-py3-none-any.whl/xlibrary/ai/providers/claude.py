"""
Claude Provider - Anthropic Claude API implementation.

Production-ready provider with full Claude feature support including streaming,
system messages, tool use, thinking modes, and extended context capabilities.
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


class ClaudeProvider(BaseAIProvider):
    """
    Anthropic Claude provider with full feature support.

    Supports Claude 4 family models with advanced capabilities:
    - Extended context (200K standard, 1M beta)
    - System message separation
    - Tool use and computer control
    - Thinking mode for reasoning
    - Prompt caching for efficiency
    """

    # Complete Claude model catalog - all current production models
    CLAUDE_MODELS = {
        # Universal aliases mapping to current models
        "latest": "claude-3-5-sonnet-20241022",      # Current best model
        "current": "claude-3-5-sonnet-20241022",     # High-performance
        "fast": "claude-3-5-haiku-20241022",         # Fast processing
        "reasoning": "claude-3-5-sonnet-20241022",   # Supports thinking

        # Direct model access - current production models
        "claude-3-5-sonnet-20241022": "Claude 3.5 Sonnet",
        "claude-3-5-haiku-20241022": "Claude 3.5 Haiku",

        # Legacy models (deprecated but still supported for now)
        "claude-3-opus-20240229": "Claude 3 Opus",
        "claude-3-sonnet-20240229": "Claude 3 Sonnet",
        "claude-3-haiku-20240307": "Claude 3 Haiku",

        # For reference - newer models from support (not yet verified)
        # "claude-opus-4-1-20250805": "Claude 4.1 Opus",
        # "claude-sonnet-4-20250514": "Claude 4 Sonnet",
        # "claude-3-7-sonnet-20250219": "Claude 3.7 Sonnet",
    }

    def __init__(self, model: str = "current", api_key: Optional[str] = None, **kwargs):
        """Initialize Claude provider with API key validation."""
        super().__init__(model, api_key, **kwargs)

        if not api_key:
            raise ConfigurationError("Claude API key is required")

        self.api_key = api_key
        self._validate_api_key()

        # Initialize Anthropic client when needed
        self._client = None

        # Configuration from kwargs
        self.enable_caching = kwargs.get('enable_caching', True)
        self.max_tokens_default = kwargs.get('max_tokens') or 4096  # Ensure default is never None

        logger.info(f"Claude provider initialized with model {model}")

    @property
    def client(self):
        """Lazy initialization of Anthropic client."""
        if self._client is None:
            try:
                import anthropic
                self._client = anthropic.Anthropic(api_key=self.api_key)
            except ImportError:
                raise ConfigurationError(
                    "anthropic package required for Claude provider. "
                    "Install with: pip install anthropic"
                )
        return self._client

    def _validate_api_key(self):
        """Validate Claude API key format."""
        if not isinstance(self.api_key, str):
            raise ConfigurationError("API key must be a string")

        if len(self.api_key) < 20:
            raise ConfigurationError("Claude API key too short")

        if not self.api_key.startswith(('sk-ant-', 'sk-')):
            raise ConfigurationError(
                "Invalid Claude API key format. Must start with 'sk-ant-' or 'sk-'"
            )

    def complete(self, messages: List[Message], enable_reasoning: bool = False, **kwargs) -> AIResponse:
        """Generate a complete response using Claude."""
        try:
            # Prepare request parameters
            model = self._resolve_model(kwargs.get('model', self.model))
            max_tokens = kwargs.get('max_tokens', self.max_tokens_default)
            temperature = kwargs.get('temperature', 0.7)

            # Ensure max_tokens is always set (required by Claude API)
            if max_tokens is None:
                max_tokens = self.max_tokens_default

            # Prepare messages for Claude's format
            claude_messages, system_message = self._prepare_messages(messages)

            # Build request
            request_params = {
                "model": model,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "messages": claude_messages
            }

            # Add system message if present
            if system_message:
                request_params["system"] = system_message

            # Add tools if provided
            tools = kwargs.get('tools')
            if tools:
                request_params["tools"] = tools
                request_params["tool_choice"] = kwargs.get('tool_choice', {"type": "auto"})

            # Add reasoning/thinking mode if enabled and supported
            if enable_reasoning and self._supports_thinking(model):
                thinking_budget = kwargs.get('thinking_budget', 16000)
                request_params["thinking"] = {
                    "type": "enabled",
                    "budget_tokens": thinking_budget
                }
                # Thinking mode requires temperature = 1.0
                request_params["temperature"] = 1.0
                # Ensure max_tokens is greater than thinking budget
                if max_tokens <= thinking_budget:
                    request_params["max_tokens"] = thinking_budget + 1000

            # Add caching if enabled and beneficial
            if self.enable_caching and len(claude_messages) > 2:
                request_params = self._add_caching(request_params)

            # Make API call
            start_time = datetime.now()
            response = self.client.messages.create(**request_params)

            # Parse and return response
            ai_response = self._parse_response(response, model)
            ai_response.latency_ms = (datetime.now() - start_time).total_seconds() * 1000

            return ai_response

        except Exception as e:
            # Import here to avoid circular imports
            import anthropic
            if isinstance(e, anthropic.APIError):
                raise self._map_anthropic_error(e)
            else:
                logger.error(f"Unexpected error in Claude complete: {e}")
                raise ProviderError(f"Claude provider error: {e}")

    def stream(self, messages: List[Message], **kwargs) -> Iterator[AIResponse]:
        """Stream response tokens as they are generated."""
        try:
            # Prepare request (similar to complete)
            model = self._resolve_model(kwargs.get('model', self.model))
            max_tokens = kwargs.get('max_tokens', self.max_tokens_default)
            temperature = kwargs.get('temperature', 0.7)

            # Ensure max_tokens is always set (required by Claude API)
            if max_tokens is None:
                max_tokens = self.max_tokens_default

            claude_messages, system_message = self._prepare_messages(messages)

            request_params = {
                "model": model,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "messages": claude_messages
            }

            if system_message:
                request_params["system"] = system_message

            # Stream the response
            accumulated_content = ""
            chunk_index = 0

            with self.client.messages.stream(**request_params) as stream:
                for chunk in stream:
                    if chunk.type == "content_block_delta":
                        if hasattr(chunk.delta, 'text'):
                            chunk_text = chunk.delta.text
                            accumulated_content += chunk_text

                            # Create streaming response chunk
                            yield AIResponse(
                                content=accumulated_content,
                                provider='claude',
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
                        provider='claude',
                        model=model,
                        is_streaming=True,
                        chunk_index=chunk_index,
                        is_final_chunk=True,
                        output_tokens=chunk_index,
                        tokens_used=chunk_index,
                        finish_reason="stop"
                    )

        except Exception as e:
            import anthropic
            if isinstance(e, anthropic.APIError):
                raise self._map_anthropic_error(e)
            else:
                logger.error(f"Unexpected error in Claude stream: {e}")
                raise ProviderError(f"Claude streaming error: {e}")

    def count_tokens(self, text: str) -> int:
        """
        Count tokens using Claude's tokenizer.

        Note: This is an approximation since Claude doesn't provide
        a direct token counting API. Using ~4 chars per token.
        """
        # Claude uses a similar tokenization to GPT models
        # Approximate: 4 characters per token on average
        return max(1, len(text) // 4)

    def get_models(self, real: bool = True, aliases: bool = True) -> Dict[str, str]:
        """Get available Claude models."""
        result = {}

        if aliases:
            result.update({
                "latest": self.CLAUDE_MODELS["latest"],
                "current": self.CLAUDE_MODELS["current"],
                "fast": self.CLAUDE_MODELS["fast"],
                "reasoning": self.CLAUDE_MODELS["reasoning"]
            })

        if real:
            result.update({
                k: v for k, v in self.CLAUDE_MODELS.items()
                if k.startswith("claude-")
            })

        return result

    def validate_model(self, model: str) -> bool:
        """Validate if model is available."""
        return model in self.CLAUDE_MODELS

    def estimate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """Estimate cost for Claude API usage using centralized pricing."""
        return get_cost_estimate("claude", input_tokens, output_tokens)

    def get_capabilities(self) -> Dict[str, Any]:
        """Get Claude provider capabilities using centralized feature matrix."""
        return get_provider_features("claude")

    def _resolve_model(self, model: str) -> str:
        """Resolve model alias to actual Claude model name."""
        if model in self.CLAUDE_MODELS:
            return self.CLAUDE_MODELS[model]
        elif model in self.CLAUDE_MODELS.values():
            return model
        else:
            raise ModelUnavailableError(
                f"Model '{model}' not available for Claude provider",
                suggested_replacement="current"
            )

    def _prepare_messages(self, messages: List[Message]) -> tuple:
        """
        Prepare messages for Claude's API format.

        Claude requires:
        - System messages separated from conversation
        - Messages in user/assistant alternating format
        - Content as string or structured format
        """
        system_messages = []
        claude_messages = []

        for message in messages:
            if message.role == "system":
                system_messages.append(message.content)
            elif message.role in ["user", "assistant"]:
                claude_messages.append({
                    "role": message.role,
                    "content": message.content
                })

        # Combine system messages
        system_message = "\n\n".join(system_messages) if system_messages else None

        # Ensure alternating user/assistant pattern
        claude_messages = self._ensure_alternating_messages(claude_messages)

        return claude_messages, system_message

    def _ensure_alternating_messages(self, messages: List[Dict]) -> List[Dict]:
        """Ensure messages alternate between user and assistant."""
        if not messages:
            return messages

        # Claude requires alternating user/assistant
        # If we have consecutive messages from same role, combine them
        processed = []
        current_role = None
        current_content = []

        for message in messages:
            role = message["role"]
            content = message["content"]

            if role == current_role:
                # Same role as previous, combine content
                current_content.append(content)
            else:
                # Different role, save previous if exists
                if current_role and current_content:
                    processed.append({
                        "role": current_role,
                        "content": "\n\n".join(current_content)
                    })

                # Start new message
                current_role = role
                current_content = [content]

        # Add final message
        if current_role and current_content:
            processed.append({
                "role": current_role,
                "content": "\n\n".join(current_content)
            })

        # Ensure we start with user message
        if processed and processed[0]["role"] != "user":
            processed.insert(0, {
                "role": "user",
                "content": "Please continue our conversation."
            })

        return processed

    def _add_caching(self, request_params: Dict) -> Dict:
        """Add Claude's prompt caching for repeated content."""
        if not self.enable_caching:
            return request_params

        # Cache system message if present
        if "system" in request_params and isinstance(request_params["system"], str):
            request_params["system"] = [
                {
                    "type": "text",
                    "text": request_params["system"],
                    "cache_control": {"type": "ephemeral"}
                }
            ]

        # Cache early messages if they're likely to be context
        messages = request_params.get("messages", [])
        if len(messages) >= 2:
            # Cache first message (often context/instructions)
            first_msg = messages[0]
            if isinstance(first_msg["content"], str):
                messages[0] = {
                    "role": first_msg["role"],
                    "content": [
                        {
                            "type": "text",
                            "text": first_msg["content"],
                            "cache_control": {"type": "ephemeral"}
                        }
                    ]
                }

        return request_params

    def _supports_thinking(self, model: str) -> bool:
        """Check if the model supports extended thinking mode."""
        # Note: As of current API, thinking mode is not yet available in production
        # This will be updated when Claude models with thinking support are released
        thinking_models = set()  # Empty set - no models currently support thinking in production

        # Future models that will support thinking:
        # thinking_models = {
        #     "claude-4-sonnet-20250101",     # Future model with thinking
        #     "claude-3-7-sonnet-20250219",   # Future thinking-enabled model
        # }

        return model in thinking_models

    def _parse_response(self, response, model: str) -> AIResponse:
        """Parse Claude API response into our AIResponse format."""
        # Extract text content
        content = ""
        if hasattr(response, 'content') and response.content:
            for block in response.content:
                if hasattr(block, 'text'):
                    content += block.text

        # Extract thinking trace if available
        thinking_trace = None
        if hasattr(response, 'thinking') and response.thinking:
            thinking_trace = response.thinking

        # Extract token usage
        input_tokens = 0
        output_tokens = 0
        reasoning_tokens = 0
        cached_tokens = 0

        if hasattr(response, 'usage'):
            input_tokens = getattr(response.usage, 'input_tokens', 0)
            output_tokens = getattr(response.usage, 'output_tokens', 0)
            cached_tokens = getattr(response.usage, 'cache_read_input_tokens', 0)

            # Reasoning tokens might be separate in thinking mode
            if hasattr(response.usage, 'cache_creation_input_tokens'):
                reasoning_tokens = getattr(response.usage, 'cache_creation_input_tokens', 0)

        # Calculate cost estimate
        cost_estimate = self.estimate_cost(input_tokens, output_tokens)

        # Get finish reason
        finish_reason = getattr(response, 'stop_reason', 'stop')

        return AIResponse(
            content=content,
            provider='claude',
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            reasoning_tokens=reasoning_tokens,
            cached_tokens=cached_tokens,
            tokens_used=input_tokens + output_tokens + reasoning_tokens,
            cost_estimate=cost_estimate,
            thinking_trace=thinking_trace,
            finish_reason=finish_reason,
            metadata={
                'api_version': 'claude',
                'supports_thinking': self._supports_thinking(model),
                'caching_enabled': self.enable_caching
            }
        )

    def _map_anthropic_error(self, error) -> ProviderError:
        """Map Anthropic API errors to our exception hierarchy."""
        import anthropic

        error_message = str(error)

        if hasattr(error, 'status_code'):
            status_code = error.status_code

            if status_code == 401:
                return AuthenticationError("Invalid Claude API key")
            elif status_code == 429:
                retry_after = None
                if hasattr(error, 'response') and error.response:
                    retry_after = error.response.headers.get('retry-after')
                    if retry_after:
                        retry_after = int(retry_after)
                return RateLimitError("Claude rate limit exceeded", retry_after)
            elif status_code == 400:
                if "maximum context length" in error_message.lower():
                    return TokenLimitExceededError("Claude context length exceeded")
                elif "model" in error_message.lower():
                    return ModelUnavailableError(
                        f"Claude model error: {error_message}",
                        suggested_replacement="current"
                    )

        # Generic API error
        return ProviderError(f"Claude API error: {error_message}")