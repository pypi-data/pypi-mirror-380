"""Validation utilities for OpRouter."""


def validate_api_key(api_key: str) -> bool:
    """Validate API key format."""
    if not api_key:
        return False

    # OpenRouter API keys typically start with "sk-or-v1-"
    if api_key.startswith("sk-or-v1-") and len(api_key) > 20:
        return True

    # Also accept other formats for flexibility
    if len(api_key) > 10:
        return True

    return False