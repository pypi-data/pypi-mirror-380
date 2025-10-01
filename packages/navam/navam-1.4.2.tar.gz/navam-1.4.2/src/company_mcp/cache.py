"""Cache implementation for company data with rate limiting"""

import json
import time
from typing import Dict, Any, Optional
import logging
import asyncio
from collections import defaultdict

logger = logging.getLogger(__name__)

class CompanyDataCache:
    """Enhanced in-memory cache for company research data with rate limiting"""

    def __init__(self):
        self._cache: Dict[str, Dict[str, Any]] = {}
        self._default_ttl = 3600  # 1 hour default TTL

        # Rate limiting configuration
        self._rate_limits = {
            'profile': {'ttl': 3600, 'max_requests': 100},  # 1 hour cache, 100 requests/hour
            'financials': {'ttl': 7200, 'max_requests': 50},  # 2 hour cache, 50 requests/hour
            'ratings': {'ttl': 3600, 'max_requests': 50},  # 1 hour cache
            'insider': {'ttl': 86400, 'max_requests': 20},  # 24 hour cache, less frequent updates
            'filings': {'ttl': 86400, 'max_requests': 30},  # 24 hour cache
            'search': {'ttl': 1800, 'max_requests': 100},  # 30 minute cache
        }

        # Track API call counts for rate limiting
        self._api_calls = defaultdict(lambda: defaultdict(list))
        self._rate_limit_window = 3600  # 1 hour window for rate limits

    async def get(self, key: str) -> Optional[Dict[str, Any]]:
        """Get value from cache if not expired"""
        if key in self._cache:
            entry = self._cache[key]
            if time.time() < entry["expires_at"]:
                logger.debug(f"Cache hit for key: {key}")
                return entry["value"]
            else:
                # Remove expired entry
                del self._cache[key]
                logger.debug(f"Cache expired for key: {key}")

        logger.debug(f"Cache miss for key: {key}")
        return None

    async def set(self, key: str, value: Dict[str, Any], ttl: Optional[int] = None) -> None:
        """Set value in cache with TTL"""
        # Determine TTL based on key type
        key_type = key.split('_')[0] if '_' in key else 'default'
        if key_type in self._rate_limits:
            ttl = ttl or self._rate_limits[key_type]['ttl']
        else:
            ttl = ttl or self._default_ttl

        expires_at = time.time() + ttl

        self._cache[key] = {
            "value": value,
            "expires_at": expires_at
        }

        logger.debug(f"Cache set for key: {key}, TTL: {ttl}s")

    def clear(self) -> None:
        """Clear all cache entries"""
        self._cache.clear()
        self._api_calls.clear()
        logger.info("Cache cleared")

    def cleanup_expired(self) -> None:
        """Remove expired entries from cache"""
        current_time = time.time()
        expired_keys = [
            key for key, entry in self._cache.items()
            if current_time >= entry["expires_at"]
        ]

        for key in expired_keys:
            del self._cache[key]

        if expired_keys:
            logger.info(f"Cleaned up {len(expired_keys)} expired cache entries")

    async def check_rate_limit(self, api_type: str, identifier: str = 'default') -> bool:
        """Check if API call is within rate limits"""
        if api_type not in self._rate_limits:
            return True  # No rate limit configured

        current_time = time.time()
        window_start = current_time - self._rate_limit_window

        # Clean old entries
        self._api_calls[api_type][identifier] = [
            t for t in self._api_calls[api_type][identifier]
            if t > window_start
        ]

        # Check if within limit
        max_requests = self._rate_limits[api_type]['max_requests']
        current_count = len(self._api_calls[api_type][identifier])

        if current_count >= max_requests:
            logger.warning(f"Rate limit reached for {api_type}/{identifier}: {current_count}/{max_requests}")
            return False

        # Record this request
        self._api_calls[api_type][identifier].append(current_time)
        return True

    def get_ttl_for_type(self, cache_type: str) -> int:
        """Get TTL for specific cache type"""
        if cache_type in self._rate_limits:
            return self._rate_limits[cache_type]['ttl']
        return self._default_ttl