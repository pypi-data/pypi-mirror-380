"""
Provider-specific rate limiting configurations.

Defines default rate limits for different AI providers based on their
published API limits and best practices.
"""

import logging
from dataclasses import dataclass
from typing import Dict, Optional


logger = logging.getLogger(__name__)


@dataclass
class ProviderLimits:
    """Rate limits for a specific provider tier."""
    requests_per_minute: int
    tokens_per_minute: int
    concurrent_requests: int
    burst_allowance: int = 10

    # Token-specific limits
    max_tokens_per_request: int = 8192
    daily_token_limit: Optional[int] = None

    # Specialized limits
    streaming_requests_per_minute: Optional[int] = None
    reasoning_requests_per_minute: Optional[int] = None


# Provider rate limits based on published API limits
# Note: These are conservative defaults - users should configure based on their actual tiers

PROVIDER_LIMITS: Dict[str, Dict[str, ProviderLimits]] = {
    "claude": {
        "free": ProviderLimits(
            requests_per_minute=5,
            tokens_per_minute=1_000,
            concurrent_requests=1,
            burst_allowance=2,
            max_tokens_per_request=4096,
            daily_token_limit=10_000
        ),
        "pro": ProviderLimits(
            requests_per_minute=50,
            tokens_per_minute=40_000,
            concurrent_requests=5,
            burst_allowance=10,
            max_tokens_per_request=8192,
            daily_token_limit=1_000_000
        ),
        "team": ProviderLimits(
            requests_per_minute=100,
            tokens_per_minute=100_000,
            concurrent_requests=10,
            burst_allowance=20,
            max_tokens_per_request=8192
        ),
        "enterprise": ProviderLimits(
            requests_per_minute=1000,
            tokens_per_minute=2_000_000,
            concurrent_requests=50,
            burst_allowance=100,
            max_tokens_per_request=8192
        )
    },

    "openai": {
        "free": ProviderLimits(
            requests_per_minute=3,
            tokens_per_minute=200,
            concurrent_requests=1,
            burst_allowance=1,
            max_tokens_per_request=4096,
            daily_token_limit=1_000
        ),
        "tier1": ProviderLimits(
            requests_per_minute=500,
            tokens_per_minute=30_000,
            concurrent_requests=10,
            burst_allowance=20,
            max_tokens_per_request=8192
        ),
        "tier2": ProviderLimits(
            requests_per_minute=3_000,
            tokens_per_minute=450_000,
            concurrent_requests=25,
            burst_allowance=50,
            max_tokens_per_request=8192
        ),
        "tier3": ProviderLimits(
            requests_per_minute=5_000,
            tokens_per_minute=800_000,
            concurrent_requests=50,
            burst_allowance=100,
            max_tokens_per_request=8192
        ),
        "tier4": ProviderLimits(
            requests_per_minute=10_000,
            tokens_per_minute=2_000_000,
            concurrent_requests=100,
            burst_allowance=200,
            max_tokens_per_request=8192
        ),
        "tier5": ProviderLimits(
            requests_per_minute=30_000,
            tokens_per_minute=5_000_000,
            concurrent_requests=200,
            burst_allowance=500,
            max_tokens_per_request=8192
        )
    },

    "deepseek": {
        "free": ProviderLimits(
            requests_per_minute=10,
            tokens_per_minute=2_000,
            concurrent_requests=2,
            burst_allowance=3,
            max_tokens_per_request=4096
        ),
        "pro": ProviderLimits(
            requests_per_minute=100,
            tokens_per_minute=50_000,
            concurrent_requests=10,
            burst_allowance=20,
            max_tokens_per_request=8192
        ),
        "enterprise": ProviderLimits(
            requests_per_minute=1000,
            tokens_per_minute=500_000,
            concurrent_requests=25,
            burst_allowance=50,
            max_tokens_per_request=8192
        )
    },

    "mock": {
        "default": ProviderLimits(
            requests_per_minute=1000,
            tokens_per_minute=1_000_000,
            concurrent_requests=100,
            burst_allowance=500,
            max_tokens_per_request=8192
        )
    }
}


def get_provider_limits(
    provider: str,
    tier: Optional[str] = None,
    fallback_to_default: bool = True
) -> Optional[ProviderLimits]:
    """
    Get rate limits for a specific provider and tier.

    Args:
        provider: Provider name (claude, openai, deepseek, mock)
        tier: Provider tier (free, pro, team, enterprise, etc.)
        fallback_to_default: Whether to fallback to default tier if specified tier not found

    Returns:
        ProviderLimits: Rate limits for the provider/tier, or None if not found
    """
    if provider not in PROVIDER_LIMITS:
        logger.warning(f"No rate limits defined for provider: {provider}")
        return None

    provider_tiers = PROVIDER_LIMITS[provider]

    # If tier specified, try to get it
    if tier and tier in provider_tiers:
        logger.debug(f"Using rate limits for {provider}/{tier}")
        return provider_tiers[tier]

    # If tier not found or not specified, try fallbacks
    if fallback_to_default:
        # Try common tier names in order of preference
        fallback_tiers = ["default", "pro", "team", "tier1", "enterprise", "free"]

        for fallback_tier in fallback_tiers:
            if fallback_tier in provider_tiers:
                if tier and tier != fallback_tier:
                    logger.info(f"Tier '{tier}' not found for {provider}, using '{fallback_tier}'")
                return provider_tiers[fallback_tier]

    logger.warning(f"No suitable rate limits found for {provider}/{tier}")
    return None


def get_all_provider_limits() -> Dict[str, Dict[str, ProviderLimits]]:
    """Get all provider limits for inspection."""
    return PROVIDER_LIMITS.copy()


def register_provider_limits(
    provider: str,
    tier: str,
    limits: ProviderLimits
):
    """
    Register custom rate limits for a provider/tier.

    Args:
        provider: Provider name
        tier: Tier name
        limits: Rate limit configuration
    """
    if provider not in PROVIDER_LIMITS:
        PROVIDER_LIMITS[provider] = {}

    PROVIDER_LIMITS[provider][tier] = limits
    logger.info(f"Registered custom rate limits for {provider}/{tier}")


def estimate_cost_limits(
    provider: str,
    input_cost_per_1k: float,
    output_cost_per_1k: float,
    daily_budget: float
) -> ProviderLimits:
    """
    Estimate rate limits based on cost constraints.

    Args:
        provider: Provider name
        input_cost_per_1k: Cost per 1k input tokens
        output_cost_per_1k: Cost per 1k output tokens
        daily_budget: Daily budget in USD

    Returns:
        ProviderLimits: Estimated limits based on budget
    """
    # Conservative assumptions for estimation
    avg_tokens_per_request = 2000  # 1000 input + 1000 output
    avg_cost_per_request = (
        (1000 * input_cost_per_1k / 1000) +  # Input cost
        (1000 * output_cost_per_1k / 1000)   # Output cost
    )

    # Calculate daily request limit from budget
    daily_requests = int(daily_budget / avg_cost_per_request) if avg_cost_per_request > 0 else 10000

    # Convert to per-minute limits (assuming 16 active hours per day)
    requests_per_minute = max(1, daily_requests // (16 * 60))
    tokens_per_minute = requests_per_minute * avg_tokens_per_request

    limits = ProviderLimits(
        requests_per_minute=requests_per_minute,
        tokens_per_minute=tokens_per_minute,
        concurrent_requests=max(1, requests_per_minute // 10),
        burst_allowance=max(2, requests_per_minute // 5),
        max_tokens_per_request=8192,
        daily_token_limit=daily_requests * avg_tokens_per_request
    )

    logger.info(f"Estimated rate limits for {provider} with ${daily_budget}/day budget: "
               f"{requests_per_minute} req/min, {tokens_per_minute} tokens/min")

    return limits