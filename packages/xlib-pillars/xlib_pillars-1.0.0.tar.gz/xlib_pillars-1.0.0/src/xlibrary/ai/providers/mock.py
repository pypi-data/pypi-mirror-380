"""Mock AI provider for testing and development."""

import time
from typing import List, Dict, Iterator, Optional, Any
from ..core.base import BaseAIProvider
from ..core.models import Message, AIResponse
from ..features import get_provider_features, get_cost_estimate


class MockProvider(BaseAIProvider):
    """Mock provider that simulates AI responses for testing."""

    def __init__(self, model: str = "latest", api_key: Optional[str] = None, **kwargs):
        """Initialize mock provider."""
        super().__init__(model=model, api_key=api_key, **kwargs)

        # Mock model mappings
        self._models = {
            "latest": "mock-flagship-v1",
            "current": "mock-performance-v1",
            "fast": "mock-efficient-v1",
            "reasoning": "mock-reasoning-v1",
            "mock-flagship-v1": "Mock Flagship Model",
            "mock-performance-v1": "Mock High-Performance Model",
            "mock-efficient-v1": "Mock Efficient Model",
            "mock-reasoning-v1": "Mock Reasoning Model"
        }

    def complete(self, messages: List[Message], enable_reasoning: bool = False, **kwargs) -> AIResponse:
        """Generate a mock response."""
        # Simulate processing time
        time.sleep(0.1)

        # Generate mock response based on last message
        last_message = messages[-1] if messages else None
        prompt = last_message.content if last_message else ""

        # Simple mock response generation
        if "respond with exactly: 'test successful'" in prompt.lower():
            content = "Test successful"
        elif "remember this number: 42" in prompt.lower():
            content = "I'll remember the number 42."
        elif "what number did i ask you to remember" in prompt.lower():
            content = "You asked me to remember the number 42."
        elif "hello" in prompt.lower():
            content = "Hello! I'm a mock AI provider. How can I help you today?"
        elif "capital" in prompt.lower() and "france" in prompt.lower():
            content = "The capital of France is Paris."
        elif "test" in prompt.lower():
            content = "This is a mock response for testing purposes."
        elif len(prompt) > 100:
            content = "Thank you for your detailed message. This is a mock response simulating how I would process longer inputs."
        else:
            content = f"Mock response to: {prompt[:50]}{'...' if len(prompt) > 50 else ''}"

        # Add reasoning trace if requested
        thinking_trace = None
        reasoning_tokens = 0
        if enable_reasoning:
            thinking_trace = f"<thinking>\nThe user asked: {prompt}\nI should provide a helpful mock response.\n</thinking>"
            reasoning_tokens = 20

        # Mock token usage
        input_tokens = len(prompt.split()) * 2  # Rough approximation
        output_tokens = len(content.split()) * 2
        total_tokens = input_tokens + output_tokens + reasoning_tokens

        return AIResponse(
            content=content,
            provider="mock",
            model=self._models.get(self.model, self.model),
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            reasoning_tokens=reasoning_tokens,
            tokens_used=total_tokens,
            cost_estimate=total_tokens * 0.00001,  # Mock pricing
            latency_ms=100.0,
            thinking_trace=thinking_trace,
            finish_reason="stop",
            metadata={"mock": True, "test_mode": True}
        )

    def stream(self, messages: List[Message], **kwargs) -> Iterator[AIResponse]:
        """Generate mock streaming response."""
        response = self.complete(messages, **kwargs)

        # Split response into chunks
        words = response.content.split()
        accumulated_content = ""

        for i, word in enumerate(words):
            accumulated_content += word + " "

            # Simulate streaming delay
            time.sleep(0.05)

            chunk_response = AIResponse(
                content=accumulated_content.strip(),
                provider="mock",
                model=response.model,
                input_tokens=response.input_tokens,
                output_tokens=len(accumulated_content.split()) * 2,
                tokens_used=response.input_tokens + len(accumulated_content.split()) * 2,
                cost_estimate=response.cost_estimate,
                is_streaming=True,
                chunk_index=i,
                is_final_chunk=(i == len(words) - 1),
                metadata={"mock": True, "streaming": True}
            )

            yield chunk_response

    def count_tokens(self, text: str) -> int:
        """Mock token counting (approximate)."""
        return len(text.split()) * 2

    def get_models(self, real: bool = True, aliases: bool = True) -> Dict[str, str]:
        """Get available mock models."""
        result = {}

        if aliases:
            result.update({
                "latest": self._models["latest"],
                "current": self._models["current"],
                "fast": self._models["fast"],
                "reasoning": self._models["reasoning"]
            })

        if real:
            result.update({
                "mock-flagship-v1": self._models["mock-flagship-v1"],
                "mock-performance-v1": self._models["mock-performance-v1"],
                "mock-efficient-v1": self._models["mock-efficient-v1"],
                "mock-reasoning-v1": self._models["mock-reasoning-v1"]
            })

        return result

    def validate_model(self, model: str) -> bool:
        """Validate if model is available."""
        return model in self._models

    def estimate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """Estimate cost using centralized pricing (mock provider is free)."""
        return get_cost_estimate("mock", input_tokens, output_tokens)

    def get_capabilities(self) -> Dict[str, Any]:
        """Get mock provider capabilities using centralized feature matrix."""
        return get_provider_features("mock")