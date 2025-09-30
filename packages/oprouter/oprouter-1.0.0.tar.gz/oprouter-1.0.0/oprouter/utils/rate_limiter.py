"""Rate limiting utilities for OpRouter."""

from typing import List, Dict, Any
from datetime import datetime, timedelta


class RateLimitTracker:
    """Track rate limits and usage."""

    def __init__(self, max_requests: int = 60, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests: List[datetime] = []

    def can_make_request(self) -> bool:
        """Check if a request can be made without hitting rate limits."""
        now = datetime.now()
        cutoff = now - timedelta(seconds=self.window_seconds)

        # Remove old requests
        self.requests = [req_time for req_time in self.requests if req_time > cutoff]

        return len(self.requests) < self.max_requests

    def record_request(self):
        """Record a new request."""
        self.requests.append(datetime.now())

    def time_until_next_request(self) -> float:
        """Get seconds until next request can be made."""
        if self.can_make_request():
            return 0.0

        # Find the oldest request that's still in the window
        now = datetime.now()
        cutoff = now - timedelta(seconds=self.window_seconds)

        valid_requests = [req_time for req_time in self.requests if req_time > cutoff]
        if not valid_requests:
            return 0.0

        oldest_request = min(valid_requests)
        next_available = oldest_request + timedelta(seconds=self.window_seconds)

        return max(0.0, (next_available - now).total_seconds())

    def get_usage_stats(self) -> Dict[str, Any]:
        """Get current usage statistics."""
        now = datetime.now()
        cutoff = now - timedelta(seconds=self.window_seconds)

        # Remove old requests
        self.requests = [req_time for req_time in self.requests if req_time > cutoff]

        return {
            "current_requests": len(self.requests),
            "max_requests": self.max_requests,
            "window_seconds": self.window_seconds,
            "usage_percentage": (len(self.requests) / self.max_requests) * 100,
            "time_until_reset": self.time_until_next_request()
        }