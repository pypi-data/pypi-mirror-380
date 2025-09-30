"""API client interfaces for OpRouter."""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, AsyncGenerator
from dataclasses import dataclass


@dataclass
class APIResponse:
    """Structured API response."""
    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    status_code: Optional[int] = None
    headers: Optional[Dict[str, str]] = None
    usage: Optional[Dict[str, Any]] = None


class APIClientInterface(ABC):
    """Interface for API clients."""

    @abstractmethod
    async def health_check(self) -> bool:
        """Check if the API is accessible."""
        pass

    @abstractmethod
    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        stream: bool = False,
        **kwargs
    ) -> APIResponse:
        """Get chat completion from the API."""
        pass

    @abstractmethod
    async def stream_chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        **kwargs
    ) -> AsyncGenerator[str, None]:
        """Stream chat completion from the API."""
        pass

    @abstractmethod
    async def get_models(self) -> APIResponse:
        """Get available models."""
        pass