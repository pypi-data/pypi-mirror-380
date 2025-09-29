"""Caching layer for news data"""

import asyncio
import json
import logging
import hashlib
from typing import Any, Optional, Dict, Union, List
from datetime import datetime, timedelta
import os
import tempfile

logger = logging.getLogger(__name__)

class NewsDataCache:
    """Simple file-based cache for news data with TTL support"""

    def __init__(self, cache_dir: Optional[str] = None, default_ttl: int = 1800):
        """
        Initialize cache

        Args:
            cache_dir: Directory for cache files (default: temp dir)
            default_ttl: Default TTL in seconds (default: 30 minutes)
        """
        self.cache_dir = cache_dir or os.path.join(tempfile.gettempdir(), "news_mcp_cache")
        self.default_ttl = default_ttl
        self._ensure_cache_dir()

    def _ensure_cache_dir(self):
        """Ensure cache directory exists"""
        try:
            os.makedirs(self.cache_dir, exist_ok=True)
        except Exception as e:
            logger.warning(f"Could not create cache directory: {e}")
            self.cache_dir = tempfile.gettempdir()

    def _get_cache_key(self, key: str) -> str:
        """Generate a safe cache key"""
        # Create a hash of the key to avoid filesystem issues
        key_hash = hashlib.md5(key.encode()).hexdigest()
        return f"news_cache_{key_hash}.json"

    def _get_cache_path(self, key: str) -> str:
        """Get full path for cache file"""
        return os.path.join(self.cache_dir, self._get_cache_key(key))

    async def get(self, key: str) -> Optional[Any]:
        """
        Get cached data

        Args:
            key: Cache key

        Returns:
            Cached data or None if not found/expired
        """
        try:
            cache_path = self._get_cache_path(key)

            if not os.path.exists(cache_path):
                return None

            # Read cache file
            with open(cache_path, 'r', encoding='utf-8') as f:
                cache_data = json.load(f)

            # Check expiration
            cached_at = datetime.fromisoformat(cache_data['cached_at'])
            ttl = cache_data.get('ttl', self.default_ttl)

            if datetime.now() > cached_at + timedelta(seconds=ttl):
                # Expired, remove file
                try:
                    os.remove(cache_path)
                except:
                    pass
                return None

            logger.debug(f"Cache hit for key: {key}")
            return cache_data['data']

        except Exception as e:
            logger.debug(f"Cache read error for key {key}: {e}")
            return None

    async def set(self, key: str, data: Any, ttl: Optional[int] = None) -> bool:
        """
        Set cached data

        Args:
            key: Cache key
            data: Data to cache
            ttl: TTL in seconds (default: use default_ttl)

        Returns:
            True if cached successfully
        """
        try:
            cache_path = self._get_cache_path(key)

            cache_data = {
                'data': data,
                'cached_at': datetime.now().isoformat(),
                'ttl': ttl or self.default_ttl,
                'key': key  # Store original key for debugging
            }

            # Write to temp file first, then rename (atomic operation)
            temp_path = cache_path + '.tmp'
            with open(temp_path, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, ensure_ascii=False, indent=2)

            os.rename(temp_path, cache_path)
            logger.debug(f"Cache set for key: {key}")
            return True

        except Exception as e:
            logger.debug(f"Cache write error for key {key}: {e}")
            return False

    async def delete(self, key: str) -> bool:
        """
        Delete cached data

        Args:
            key: Cache key

        Returns:
            True if deleted successfully
        """
        try:
            cache_path = self._get_cache_path(key)
            if os.path.exists(cache_path):
                os.remove(cache_path)
                logger.debug(f"Cache deleted for key: {key}")
                return True
            return False
        except Exception as e:
            logger.debug(f"Cache delete error for key {key}: {e}")
            return False

    async def clear(self) -> int:
        """
        Clear all cached data

        Returns:
            Number of files deleted
        """
        deleted_count = 0
        try:
            for filename in os.listdir(self.cache_dir):
                if filename.startswith("news_cache_") and filename.endswith(".json"):
                    file_path = os.path.join(self.cache_dir, filename)
                    try:
                        os.remove(file_path)
                        deleted_count += 1
                    except:
                        pass
            logger.info(f"Cache cleared: {deleted_count} files deleted")
        except Exception as e:
            logger.error(f"Cache clear error: {e}")

        return deleted_count

    async def cleanup_expired(self) -> int:
        """
        Clean up expired cache entries

        Returns:
            Number of expired files deleted
        """
        deleted_count = 0
        try:
            for filename in os.listdir(self.cache_dir):
                if filename.startswith("news_cache_") and filename.endswith(".json"):
                    file_path = os.path.join(self.cache_dir, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            cache_data = json.load(f)

                        cached_at = datetime.fromisoformat(cache_data['cached_at'])
                        ttl = cache_data.get('ttl', self.default_ttl)

                        if datetime.now() > cached_at + timedelta(seconds=ttl):
                            os.remove(file_path)
                            deleted_count += 1
                    except:
                        # If we can't read the file, it's probably corrupted, delete it
                        try:
                            os.remove(file_path)
                            deleted_count += 1
                        except:
                            pass

            if deleted_count > 0:
                logger.info(f"Cache cleanup: {deleted_count} expired files deleted")

        except Exception as e:
            logger.error(f"Cache cleanup error: {e}")

        return deleted_count

    async def get_stats(self) -> Dict[str, Any]:
        """
        Get cache statistics

        Returns:
            Dictionary with cache stats
        """
        stats = {
            'total_files': 0,
            'total_size_bytes': 0,
            'expired_files': 0,
            'valid_files': 0,
            'oldest_entry': None,
            'newest_entry': None,
            'cache_dir': self.cache_dir
        }

        try:
            oldest_time = None
            newest_time = None

            for filename in os.listdir(self.cache_dir):
                if filename.startswith("news_cache_") and filename.endswith(".json"):
                    file_path = os.path.join(self.cache_dir, filename)
                    stats['total_files'] += 1

                    try:
                        # Get file size
                        stats['total_size_bytes'] += os.path.getsize(file_path)

                        # Read cache data
                        with open(file_path, 'r', encoding='utf-8') as f:
                            cache_data = json.load(f)

                        cached_at = datetime.fromisoformat(cache_data['cached_at'])
                        ttl = cache_data.get('ttl', self.default_ttl)

                        # Track oldest/newest
                        if oldest_time is None or cached_at < oldest_time:
                            oldest_time = cached_at
                        if newest_time is None or cached_at > newest_time:
                            newest_time = cached_at

                        # Check if expired
                        if datetime.now() > cached_at + timedelta(seconds=ttl):
                            stats['expired_files'] += 1
                        else:
                            stats['valid_files'] += 1

                    except:
                        # Corrupted file
                        stats['expired_files'] += 1

            if oldest_time:
                stats['oldest_entry'] = oldest_time.isoformat()
            if newest_time:
                stats['newest_entry'] = newest_time.isoformat()

        except Exception as e:
            logger.error(f"Cache stats error: {e}")

        return stats

    def create_cache_key(self, base_key: str, **params) -> str:
        """
        Create a cache key from base key and parameters

        Args:
            base_key: Base cache key
            **params: Additional parameters to include in key

        Returns:
            Generated cache key
        """
        # Sort params for consistent keys
        param_str = "&".join(f"{k}={v}" for k, v in sorted(params.items()) if v is not None)

        if param_str:
            return f"{base_key}?{param_str}"
        else:
            return base_key

    async def get_or_set(self, key: str, fetch_func, ttl: Optional[int] = None) -> Any:
        """
        Get cached data or fetch and cache if not found

        Args:
            key: Cache key
            fetch_func: Async function to fetch data if not cached
            ttl: TTL for cached data

        Returns:
            Cached or freshly fetched data
        """
        # Try to get from cache first
        cached_data = await self.get(key)
        if cached_data is not None:
            return cached_data

        # Fetch fresh data
        try:
            fresh_data = await fetch_func()

            # Cache the result
            await self.set(key, fresh_data, ttl)

            return fresh_data

        except Exception as e:
            logger.error(f"Error fetching data for cache key {key}: {e}")
            raise

    async def warm_cache(self, keys_and_fetchers: List[tuple]) -> Dict[str, bool]:
        """
        Warm cache with multiple keys

        Args:
            keys_and_fetchers: List of (key, fetch_func, ttl) tuples

        Returns:
            Dictionary mapping keys to success status
        """
        results = {}

        # Process in parallel
        tasks = []
        for item in keys_and_fetchers:
            if len(item) == 2:
                key, fetch_func = item
                ttl = None
            else:
                key, fetch_func, ttl = item

            tasks.append(self._warm_single_key(key, fetch_func, ttl))

        task_results = await asyncio.gather(*tasks, return_exceptions=True)

        for i, result in enumerate(task_results):
            key = keys_and_fetchers[i][0]
            results[key] = not isinstance(result, Exception)

            if isinstance(result, Exception):
                logger.error(f"Cache warming failed for key {key}: {result}")

        return results

    async def _warm_single_key(self, key: str, fetch_func, ttl: Optional[int] = None):
        """Warm a single cache key"""
        try:
            # Check if already cached and not expired
            cached = await self.get(key)
            if cached is not None:
                return True

            # Fetch and cache
            data = await fetch_func()
            await self.set(key, data, ttl)
            return True

        except Exception as e:
            logger.debug(f"Cache warming error for key {key}: {e}")
            raise