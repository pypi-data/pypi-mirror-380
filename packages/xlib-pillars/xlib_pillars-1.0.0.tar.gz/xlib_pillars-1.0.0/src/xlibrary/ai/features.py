"""
Provider Feature Matrix for AI Capabilities.

Comprehensive feature support matrix across all providers for runtime
capability checking and feature availability detection.
"""

from typing import Dict, Any, Union, List, Optional


# Complete feature support matrix across all providers
PROVIDER_FEATURES: Dict[str, Dict[str, Any]] = {
    "claude": {
        # Core features
        "stateless_requests": True,
        "stateful_conversations": True,
        "streaming": True,
        "reasoning_mode": True,         # Claude supports thinking trace
        "function_calling": True,       # Tool use capability

        # Content types
        "text_input": True,
        "image_input": True,           # Vision models
        "file_attachments": True,
        "pdf_processing": True,
        "document_parsing": True,

        # Advanced features
        "system_messages": True,
        "message_caching": True,       # Prompt caching
        "artifact_generation": True,
        "code_execution": False,       # No native code execution
        "web_search": False,          # No built-in web search

        # Model capabilities
        "max_context_tokens": 200_000,  # Context window size
        "max_output_tokens": 4_096,     # Maximum output length
        "supports_json_mode": False,    # No native JSON mode
        "supports_stop_sequences": True,

        # Rate limiting
        "requests_per_minute": 1000,   # API limits
        "tokens_per_minute": 80_000,   # Token limits
        "concurrent_requests": 5,      # Concurrent request limit

        # Model-specific features
        "available_models": [
            "claude-3-5-sonnet-20241022",  # Current flagship
            "claude-3-5-haiku-20241022",   # Fast model
            "claude-3-opus-20240229",      # Legacy flagship
            "claude-3-sonnet-20240229",    # Legacy balanced
            "claude-3-haiku-20240307"      # Legacy fast
        ],

        # Provider-specific features
        "thinking_trace": True,         # Reasoning mode with thinking steps
        "tool_use": True,              # Native tool/function calling
        "vision_models": ["claude-3-5-sonnet-20241022"],
        "reasoning_models": ["claude-3-5-sonnet-20241022"],

        # Cost information (per 1M tokens)
        "input_cost_per_1m": 3.00,    # USD per 1M input tokens
        "output_cost_per_1m": 15.00,  # USD per 1M output tokens

        # Quality metrics
        "quality_tier": "premium",     # premium, standard, basic
        "response_quality": "excellent",
        "coding_capability": "excellent",
        "reasoning_capability": "excellent"
    },

    "openai": {
        # Core features
        "stateless_requests": True,
        "stateful_conversations": True,
        "streaming": True,
        "reasoning_mode": True,        # o1-mini, o1 reasoning models
        "function_calling": True,      # Native function calling

        # Content types
        "text_input": True,
        "image_input": True,          # GPT-4V, GPT-4o
        "file_attachments": True,
        "pdf_processing": False,      # Limited native PDF support
        "document_parsing": True,

        # Advanced features
        "system_messages": True,
        "message_caching": False,     # No prompt caching
        "artifact_generation": True,
        "code_execution": True,       # Code interpreter
        "web_search": True,           # SearchGPT integration

        # Model capabilities
        "max_context_tokens": 128_000,  # Most models
        "max_output_tokens": 4_096,     # Standard limit
        "supports_json_mode": True,     # Native JSON mode
        "supports_stop_sequences": True,

        # Rate limiting
        "requests_per_minute": 3500,   # Higher API limits
        "tokens_per_minute": 200_000,  # Higher token limits
        "concurrent_requests": 20,     # Higher concurrency

        # Model-specific features
        "available_models": [
            "gpt-4o",                   # Current flagship
            "gpt-4o-mini",             # Fast model
            "gpt-4-turbo",             # Previous flagship
            "gpt-4",                   # Legacy flagship
            "gpt-3.5-turbo",          # Legacy fast
            "o1-preview",              # Reasoning model
            "o1-mini"                  # Fast reasoning
        ],

        # Provider-specific features
        "reasoning_models": ["o1-preview", "o1-mini"],
        "vision_models": ["gpt-4o", "gpt-4-turbo", "gpt-4"],
        "json_mode_models": ["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"],
        "function_calling_models": ["gpt-4o", "gpt-4-turbo", "gpt-4", "gpt-3.5-turbo"],

        # Cost information (per 1M tokens)
        "input_cost_per_1m": 2.50,    # USD per 1M input tokens (GPT-4o)
        "output_cost_per_1m": 10.00,  # USD per 1M output tokens (GPT-4o)

        # Quality metrics
        "quality_tier": "premium",
        "response_quality": "excellent",
        "coding_capability": "excellent",
        "reasoning_capability": "excellent"
    },

    "deepseek": {
        # Core features
        "stateless_requests": True,
        "stateful_conversations": True,
        "streaming": True,
        "reasoning_mode": True,        # DeepSeek R1 reasoning
        "function_calling": True,      # Function calling support

        # Content types
        "text_input": True,
        "image_input": False,         # No vision models yet
        "file_attachments": True,
        "pdf_processing": False,      # Limited document support
        "document_parsing": False,

        # Advanced features
        "system_messages": True,
        "message_caching": False,     # No caching
        "artifact_generation": True,
        "code_execution": False,      # No code execution
        "web_search": False,          # No web search

        # Model capabilities
        "max_context_tokens": 64_000,   # Context window
        "max_output_tokens": 8_192,     # Larger output
        "supports_json_mode": True,     # JSON mode support
        "supports_stop_sequences": True,

        # Rate limiting
        "requests_per_minute": 600,    # Moderate limits
        "tokens_per_minute": 100_000,  # Token limits
        "concurrent_requests": 10,     # Concurrency limit

        # Model-specific features
        "available_models": [
            "deepseek-r1",              # Reasoning model
            "deepseek-chat",           # Chat model
            "deepseek-coder",          # Code-specialized
            "deepseek-math"            # Math-specialized
        ],

        # Provider-specific features
        "reasoning_models": ["deepseek-r1"],
        "vision_models": [],           # No vision support yet
        "specialized_models": ["deepseek-coder", "deepseek-math"],

        # Cost information (per 1M tokens)
        "input_cost_per_1m": 0.14,    # Very cost-effective
        "output_cost_per_1m": 0.28,   # Very cost-effective

        # Quality metrics
        "quality_tier": "standard",
        "response_quality": "very_good",
        "coding_capability": "excellent",
        "reasoning_capability": "very_good"
    },

    "mock": {
        # Core features (all supported for testing)
        "stateless_requests": True,
        "stateful_conversations": True,
        "streaming": True,
        "reasoning_mode": True,        # Simulated reasoning
        "function_calling": True,      # Simulated function calls

        # Content types
        "text_input": True,
        "image_input": True,          # Simulated vision
        "file_attachments": True,
        "pdf_processing": True,       # Simulated processing
        "document_parsing": True,

        # Advanced features
        "system_messages": True,
        "message_caching": True,      # Simulated caching
        "artifact_generation": True,
        "code_execution": True,       # Simulated execution
        "web_search": True,           # Simulated search

        # Model capabilities (configurable)
        "max_context_tokens": 200_000,  # Configurable
        "max_output_tokens": 8_192,     # Configurable
        "supports_json_mode": True,
        "supports_stop_sequences": True,

        # Rate limiting (no real limits)
        "requests_per_minute": float('inf'),
        "tokens_per_minute": float('inf'),
        "concurrent_requests": float('inf'),

        # Model-specific features
        "available_models": [
            "latest",                   # Universal alias
            "current",                 # Universal alias
            "fast",                    # Universal alias
            "reasoning"                # Universal alias
        ],

        # Provider-specific features
        "reasoning_models": ["latest", "current", "reasoning"],
        "vision_models": ["latest", "current"],
        "all_features_simulated": True,

        # Cost information (testing - no cost)
        "input_cost_per_1m": 0.0,
        "output_cost_per_1m": 0.0,

        # Quality metrics
        "quality_tier": "testing",
        "response_quality": "simulated",
        "coding_capability": "simulated",
        "reasoning_capability": "simulated"
    }
}


# Feature categories for organized access
FEATURE_CATEGORIES = {
    "core": [
        "stateless_requests",
        "stateful_conversations",
        "streaming",
        "reasoning_mode",
        "function_calling"
    ],
    "content_types": [
        "text_input",
        "image_input",
        "file_attachments",
        "pdf_processing",
        "document_parsing"
    ],
    "advanced": [
        "system_messages",
        "message_caching",
        "artifact_generation",
        "code_execution",
        "web_search"
    ],
    "model_capabilities": [
        "max_context_tokens",
        "max_output_tokens",
        "supports_json_mode",
        "supports_stop_sequences"
    ],
    "rate_limiting": [
        "requests_per_minute",
        "tokens_per_minute",
        "concurrent_requests"
    ]
}


def check_feature_support(provider: str, feature: str) -> bool:
    """
    Check if a provider supports a specific feature.

    Args:
        provider: Provider name (claude, openai, deepseek, mock)
        feature: Feature name to check

    Returns:
        bool: True if the feature is supported, False otherwise

    Example:
        if check_feature_support("claude", "reasoning_mode"):
            response = ai.request("Complex problem", enable_reasoning=True)
        else:
            print("Reasoning mode not available for this provider")
    """
    return PROVIDER_FEATURES.get(provider, {}).get(feature, False)


def get_provider_features(provider: str) -> Dict[str, Any]:
    """
    Get all features for a specific provider.

    Args:
        provider: Provider name

    Returns:
        Dict of all features and their values for the provider
    """
    return PROVIDER_FEATURES.get(provider, {}).copy()


def get_feature_comparison(feature: str) -> Dict[str, Any]:
    """
    Compare a specific feature across all providers.

    Args:
        feature: Feature name to compare

    Returns:
        Dict mapping provider names to feature values
    """
    return {
        provider: features.get(feature, False)
        for provider, features in PROVIDER_FEATURES.items()
    }


def get_providers_with_feature(feature: str, value: Any = True) -> List[str]:
    """
    Get list of providers that support a specific feature.

    Args:
        feature: Feature name to check
        value: Expected feature value (default: True)

    Returns:
        List of provider names that support the feature
    """
    return [
        provider for provider, features in PROVIDER_FEATURES.items()
        if features.get(feature) == value
    ]


def get_feature_matrix(category: Optional[str] = None) -> Dict[str, Dict[str, Any]]:
    """
    Get feature matrix for all providers, optionally filtered by category.

    Args:
        category: Feature category to filter by (core, content_types, advanced, etc.)

    Returns:
        Dict of providers with their feature support
    """
    if category and category in FEATURE_CATEGORIES:
        features_to_include = FEATURE_CATEGORIES[category]
        return {
            provider: {
                feature: features.get(feature, False)
                for feature in features_to_include
            }
            for provider, features in PROVIDER_FEATURES.items()
        }

    return PROVIDER_FEATURES.copy()


def get_model_capabilities(provider: str, model: Optional[str] = None) -> Dict[str, Any]:
    """
    Get model-specific capabilities for a provider.

    Args:
        provider: Provider name
        model: Specific model name (optional)

    Returns:
        Dict of model capabilities
    """
    provider_features = PROVIDER_FEATURES.get(provider, {})

    capabilities = {
        "max_context_tokens": provider_features.get("max_context_tokens"),
        "max_output_tokens": provider_features.get("max_output_tokens"),
        "supports_json_mode": provider_features.get("supports_json_mode"),
        "supports_stop_sequences": provider_features.get("supports_stop_sequences"),
        "available_models": provider_features.get("available_models", [])
    }

    # Add model-specific features if model is specified
    if model:
        reasoning_models = provider_features.get("reasoning_models", [])
        vision_models = provider_features.get("vision_models", [])

        capabilities.update({
            "supports_reasoning": model in reasoning_models,
            "supports_vision": model in vision_models,
            "model_specific": True
        })

    return {k: v for k, v in capabilities.items() if v is not None}


def get_cost_estimate(provider: str, input_tokens: int, output_tokens: int) -> float:
    """
    Estimate cost for a request based on provider pricing.

    Args:
        provider: Provider name
        input_tokens: Number of input tokens
        output_tokens: Number of output tokens

    Returns:
        Estimated cost in USD
    """
    provider_features = PROVIDER_FEATURES.get(provider, {})

    input_cost_per_1m = provider_features.get("input_cost_per_1m", 0.0)
    output_cost_per_1m = provider_features.get("output_cost_per_1m", 0.0)

    input_cost = (input_tokens / 1_000_000) * input_cost_per_1m
    output_cost = (output_tokens / 1_000_000) * output_cost_per_1m

    return input_cost + output_cost


def get_quality_assessment(provider: str) -> Dict[str, str]:
    """
    Get quality assessment for a provider.

    Args:
        provider: Provider name

    Returns:
        Dict with quality metrics
    """
    provider_features = PROVIDER_FEATURES.get(provider, {})

    return {
        "quality_tier": provider_features.get("quality_tier", "unknown"),
        "response_quality": provider_features.get("response_quality", "unknown"),
        "coding_capability": provider_features.get("coding_capability", "unknown"),
        "reasoning_capability": provider_features.get("reasoning_capability", "unknown")
    }


def validate_provider_config(provider: str, config: Dict[str, Any]) -> List[str]:
    """
    Validate configuration against provider capabilities.

    Args:
        provider: Provider name
        config: Configuration to validate

    Returns:
        List of validation warnings/errors
    """
    warnings = []
    provider_features = PROVIDER_FEATURES.get(provider, {})

    if not provider_features:
        return [f"Unknown provider: {provider}"]

    # Check token limits
    max_tokens = config.get("max_tokens")
    if max_tokens:
        max_output = provider_features.get("max_output_tokens")
        if max_output and max_tokens > max_output:
            warnings.append(f"max_tokens ({max_tokens}) exceeds provider limit ({max_output})")

    # Check JSON mode support
    if config.get("json_mode") and not provider_features.get("supports_json_mode"):
        warnings.append("JSON mode requested but not supported by provider")

    # Check reasoning mode
    if config.get("enable_reasoning") and not provider_features.get("reasoning_mode"):
        warnings.append("Reasoning mode requested but not supported by provider")

    # Check function calling
    if config.get("functions") and not provider_features.get("function_calling"):
        warnings.append("Function calling requested but not supported by provider")

    return warnings


def get_recommended_provider(requirements: Dict[str, Any]) -> Optional[str]:
    """
    Recommend a provider based on requirements.

    Args:
        requirements: Dict of required features and preferences

    Returns:
        Recommended provider name or None if no match
    """
    scored_providers = []

    for provider, features in PROVIDER_FEATURES.items():
        if provider == "mock":  # Skip mock provider for real recommendations
            continue

        score = 0

        # Check required features
        required_features = requirements.get("required_features", [])
        for feature in required_features:
            if not features.get(feature, False):
                score = -1  # Disqualified
                break
            score += 10  # Bonus for required feature

        if score < 0:
            continue  # Skip disqualified providers

        # Check preferred features
        preferred_features = requirements.get("preferred_features", [])
        for feature in preferred_features:
            if features.get(feature, False):
                score += 5

        # Quality preference
        quality_preference = requirements.get("quality_tier")
        if quality_preference == features.get("quality_tier"):
            score += 15

        # Cost preference
        cost_preference = requirements.get("cost_preference", "balanced")
        input_cost = features.get("input_cost_per_1m", 0)
        if cost_preference == "low_cost" and input_cost < 1.0:
            score += 10
        elif cost_preference == "premium" and input_cost > 2.0:
            score += 5

        scored_providers.append((provider, score))

    if not scored_providers:
        return None

    # Return highest scoring provider
    scored_providers.sort(key=lambda x: x[1], reverse=True)
    return scored_providers[0][0]