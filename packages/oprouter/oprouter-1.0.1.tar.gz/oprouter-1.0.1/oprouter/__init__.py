"""OpRouter - A Python library for chatting with AI models through OpenRouter. Simple to use, reliable, and feature-rich."""

from .ui.cli import OpRouterCLI, main as cli_main
from .services.api_client import OpenRouterClient, APIResponse
from .services.api_client import RateLimitError

__all__ = [
    'OpRouterCLI',
    'cli_main',
    'OpenRouterClient',
    'APIResponse',
    'RateLimitError'
]