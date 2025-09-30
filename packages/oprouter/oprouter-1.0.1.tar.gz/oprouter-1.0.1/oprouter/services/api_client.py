"""Advanced OpenRouter API client with robust retry logic and rate limiting."""

import asyncio
import json
import random
import time
import logging
from typing import List, Dict, Any, Optional, AsyncGenerator
from dataclasses import dataclass
from datetime import datetime, timedelta

import aiohttp
from asyncio_throttle import Throttler
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential_jitter,
    retry_if_exception_type,
    before_sleep_log,
    after_log
)

from ..core.config import get_config
from ..core.logger import logger


@dataclass
class APIResponse:
    """Structured API response."""
    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    status_code: Optional[int] = None
    headers: Optional[Dict[str, str]] = None
    usage: Optional[Dict[str, Any]] = None


class RateLimitError(Exception):
    """Custom exception for rate limit errors."""
    def __init__(self, message: str, retry_after: Optional[int] = None):
        super().__init__(message)
        self.retry_after = retry_after


class OpenRouterClient:
    """Advanced OpenRouter API client with comprehensive error handling and retry logic."""
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        self.config = get_config()
        self.api_key = api_key or self.config.openrouter_api_key
        self.model = model or self.config.default_model
        self.base_url = self.config.base_url
        
        # Rate limiting
        self.throttler = Throttler(
            rate_limit=self.config.max_requests_per_minute,
            period=60
        )
        self.semaphore = asyncio.Semaphore(self.config.max_concurrent_requests)
        
        # Session management
        self._session: Optional[aiohttp.ClientSession] = None
        
        logger.info(f"Initialized OpenRouter client with model: {self.model}")
    
    async def __aenter__(self):
        """Async context manager entry."""
        await self._ensure_session()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()
    
    async def _ensure_session(self):
        """Ensure aiohttp session is created."""
        if self._session is None or self._session.closed:
            timeout = aiohttp.ClientTimeout(total=300, connect=30)
            self._session = aiohttp.ClientSession(
                timeout=timeout,
                connector=aiohttp.TCPConnector(limit=100, limit_per_host=30)
            )
    
    async def close(self):
        """Close the aiohttp session."""
        if self._session and not self._session.closed:
            await self._session.close()
            self._session = None
    
    def _get_headers(self, extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """Get request headers."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "X-Title": "OpRouter Advanced Chat Client",
            "User-Agent": "OpRouter/1.0"
        }
        if extra_headers:
            headers.update(extra_headers)
        return headers
    
    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential_jitter(initial=1, max=60, jitter=5),
        retry=retry_if_exception_type((RateLimitError, aiohttp.ClientError, asyncio.TimeoutError)),
        before_sleep=before_sleep_log(logger, logging.WARNING),
        after=after_log(logger, logging.INFO)
    )
    async def _make_request(
        self, 
        method: str, 
        endpoint: str, 
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> APIResponse:
        """Make HTTP request with comprehensive error handling."""
        await self._ensure_session()
        
        async with self.semaphore:  # Limit concurrent requests
            async with self.throttler:  # Rate limiting
                url = f"{self.base_url}/{endpoint.lstrip('/')}"
                request_headers = self._get_headers(headers)
                
                logger.debug(f"Making {method} request to {url}")
                
                try:
                    async with self._session.request(
                        method=method,
                        url=url,
                        json=data,
                        headers=request_headers
                    ) as response:
                        response_headers = dict(response.headers)
                        response_text = await response.text()
                        
                        # Handle rate limiting
                        if response.status == 429:
                            retry_after = int(response_headers.get('Retry-After', 60))
                            logger.warning(f"Rate limited. Retry after {retry_after} seconds")
                            raise RateLimitError(
                                f"Rate limit exceeded. Retry after {retry_after} seconds",
                                retry_after=retry_after
                            )
                        
                        # Handle other client errors
                        if 400 <= response.status < 500:
                            error_msg = f"Client error {response.status}: {response_text}"
                            logger.error(error_msg)
                            return APIResponse(
                                success=False,
                                error=error_msg,
                                status_code=response.status,
                                headers=response_headers
                            )
                        
                        # Handle server errors
                        if response.status >= 500:
                            error_msg = f"Server error {response.status}: {response_text}"
                            logger.error(error_msg)
                            raise aiohttp.ClientError(error_msg)
                        
                        # Success response
                        if response.status == 200:
                            try:
                                response_data = json.loads(response_text)
                                usage = response_data.get('usage', {})
                                
                                logger.info(f"Request successful. Tokens used: {usage.get('total_tokens', 0)}")
                                
                                return APIResponse(
                                    success=True,
                                    data=response_data,
                                    status_code=response.status,
                                    headers=response_headers,
                                    usage=usage
                                )
                            except json.JSONDecodeError as e:
                                error_msg = f"Invalid JSON response: {e}"
                                logger.error(error_msg)
                                return APIResponse(
                                    success=False,
                                    error=error_msg,
                                    status_code=response.status
                                )
                        
                        # Unexpected status code
                        error_msg = f"Unexpected status code {response.status}: {response_text}"
                        logger.warning(error_msg)
                        return APIResponse(
                            success=False,
                            error=error_msg,
                            status_code=response.status,
                            headers=response_headers
                        )
                
                except asyncio.TimeoutError:
                    error_msg = "Request timeout"
                    logger.error(error_msg)
                    raise
                except aiohttp.ClientError as e:
                    error_msg = f"Client error: {e}"
                    logger.error(error_msg)
                    raise
                except Exception as e:
                    error_msg = f"Unexpected error: {e}"
                    logger.error(error_msg)
                    return APIResponse(success=False, error=error_msg)

    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        stream: bool = False,
        **kwargs
    ) -> APIResponse:
        """Send a chat completion request."""
        payload = {
            "model": model or self.model,
            "messages": messages,
            "temperature": temperature,
            **kwargs
        }

        if max_tokens:
            payload["max_tokens"] = max_tokens

        if stream:
            payload["stream"] = True

        logger.info(f"Sending chat completion request with {len(messages)} messages")

        return await self._make_request("POST", "/chat/completions", data=payload)

    async def chat_completion_stream(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> AsyncGenerator[str, None]:
        """Stream chat completion response."""
        payload = {
            "model": model or self.model,
            "messages": messages,
            "temperature": temperature,
            "stream": True,
            **kwargs
        }

        if max_tokens:
            payload["max_tokens"] = max_tokens

        await self._ensure_session()

        async with self.semaphore:
            async with self.throttler:
                url = f"{self.base_url}/chat/completions"
                headers = self._get_headers()

                try:
                    async with self._session.post(
                        url=url,
                        json=payload,
                        headers=headers
                    ) as response:
                        if response.status != 200:
                            error_text = await response.text()
                            raise Exception(f"Stream request failed: {response.status} - {error_text}")

                        async for line in response.content:
                            line = line.decode('utf-8').strip()
                            if line.startswith('data: '):
                                data = line[6:]
                                if data == '[DONE]':
                                    break
                                try:
                                    chunk = json.loads(data)
                                    if 'choices' in chunk and chunk['choices']:
                                        delta = chunk['choices'][0].get('delta', {})
                                        if 'content' in delta:
                                            yield delta['content']
                                except json.JSONDecodeError:
                                    continue

                except Exception as e:
                    logger.error(f"Streaming error: {e}")
                    raise

    async def get_models(self) -> APIResponse:
        """Get available models."""
        return await self._make_request("GET", "/models")

    async def health_check(self) -> bool:
        """Check if the API is accessible."""
        try:
            response = await self.get_models()
            return response.success
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return False
