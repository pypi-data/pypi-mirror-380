"""Token counting utilities for OpRouter."""

import tiktoken
from typing import List, Dict
from ..core.logger import logger


class TokenCounter:
    """Token counting utilities."""

    def __init__(self, model: str = "gpt-3.5-turbo"):
        try:
            self.encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            # Fallback to cl100k_base for unknown models
            self.encoding = tiktoken.get_encoding("cl100k_base")
            logger.warning(f"Unknown model {model}, using cl100k_base encoding")

    def count_tokens(self, text: str) -> int:
        """Count tokens in text."""
        return len(self.encoding.encode(text))

    def count_message_tokens(self, messages: List[Dict[str, str]]) -> int:
        """Count tokens in a list of messages."""
        total_tokens = 0

        for message in messages:
            # Add tokens for message structure
            total_tokens += 4  # Every message has role, content, name, and function_call

            for key, value in message.items():
                total_tokens += self.count_tokens(str(value))
                if key == "name":  # If there's a name, the role is omitted
                    total_tokens -= 1

        total_tokens += 2  # Every reply is primed with assistant
        return total_tokens

    def estimate_cost(self, prompt_tokens: int, completion_tokens: int, model: str) -> float:
        """Estimate cost based on token usage."""
        # Simplified pricing - in reality, you'd fetch this from the API or config
        pricing = {
            "gpt-3.5-turbo": {"prompt": 0.0015, "completion": 0.002},
            "gpt-4": {"prompt": 0.03, "completion": 0.06},
            "x-ai/grok-4-fast:free": {"prompt": 0.0, "completion": 0.0},
        }

        model_pricing = pricing.get(model, {"prompt": 0.001, "completion": 0.002})

        prompt_cost = (prompt_tokens / 1000) * model_pricing["prompt"]
        completion_cost = (completion_tokens / 1000) * model_pricing["completion"]

        return prompt_cost + completion_cost