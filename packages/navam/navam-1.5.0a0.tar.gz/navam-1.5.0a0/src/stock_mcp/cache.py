"""Caching layer for API responses."""

import asyncio
from typing import Dict, Any, Optional
from datetime import datetime, timedelta
import json


class StockDataCache:
    """Simple in-memory cache for stock data."""

    def __init__(self, ttl_minutes: int = 15):
        """Initialize cache with TTL in minutes."""
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.ttl = timedelta(minutes=ttl_minutes)
        self._cleanup_task = None

    def _is_expired(self, timestamp: datetime) -> bool:
        """Check if cache entry is expired."""
        return datetime.now() - timestamp > self.ttl

    def get(self, key: str) -> Optional[Any]:
        """Get value from cache if not expired."""
        if key in self.cache:
            entry = self.cache[key]
            if not self._is_expired(entry['timestamp']):
                return entry['value']
            else:
                del self.cache[key]
        return None

    def set(self, key: str, value: Any) -> None:
        """Set value in cache with current timestamp."""
        self.cache[key] = {
            'value': value,
            'timestamp': datetime.now()
        }

    def clear(self) -> None:
        """Clear all cache entries."""
        self.cache.clear()

    async def cleanup(self) -> None:
        """Clean up expired entries periodically."""
        while True:
            await asyncio.sleep(60)
            expired_keys = [
                key for key, entry in self.cache.items()
                if self._is_expired(entry['timestamp'])
            ]
            for key in expired_keys:
                del self.cache[key]

    def start_cleanup(self) -> None:
        """Start background cleanup task."""
        if not self._cleanup_task:
            self._cleanup_task = asyncio.create_task(self.cleanup())

    def stop_cleanup(self) -> None:
        """Stop background cleanup task."""
        if self._cleanup_task:
            self._cleanup_task.cancel()
            self._cleanup_task = None