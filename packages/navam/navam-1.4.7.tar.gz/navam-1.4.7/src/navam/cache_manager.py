"""
Session-level caching for MCP tool calls to eliminate redundant API requests.

This module provides a lightweight, in-memory cache that persists for the duration
of a chat session, preventing duplicate tool calls when multiple agents request
the same data.
"""

import json
import time
from typing import Any, Dict, Optional
from dataclasses import dataclass
from hashlib import md5


@dataclass
class CacheEntry:
    """Represents a cached tool result with metadata"""
    result: Any
    timestamp: float
    tool_name: str
    hit_count: int = 0


class SessionCache:
    """
    Session-level cache for MCP tool calls.

    Features:
    - TTL-based expiration (default 5 minutes)
    - LRU eviction when max size reached
    - Per-tool namespace to avoid collisions
    - Cache statistics for monitoring
    """

    def __init__(self, ttl_seconds: int = 300, max_entries: int = 100):
        """
        Initialize session cache.

        Args:
            ttl_seconds: Time-to-live for cache entries (default 5 minutes)
            max_entries: Maximum number of cached entries (LRU eviction)
        """
        self.ttl_seconds = ttl_seconds
        self.max_entries = max_entries
        self.cache: Dict[str, CacheEntry] = {}

        # Statistics
        self.stats = {
            'hits': 0,
            'misses': 0,
            'evictions': 0,
            'total_calls': 0
        }

    def _make_key(self, tool_name: str, args: dict) -> str:
        """
        Generate cache key from tool name and arguments.

        Uses MD5 hash of sorted JSON to ensure consistent keys regardless
        of argument order.
        """
        args_str = json.dumps(args, sort_keys=True)
        hash_suffix = md5(args_str.encode()).hexdigest()[:8]
        return f"{tool_name}:{hash_suffix}"

    def get(self, tool_name: str, args: dict) -> Optional[Any]:
        """
        Retrieve cached result if available and not expired.

        Args:
            tool_name: Name of the MCP tool
            args: Tool arguments as dictionary

        Returns:
            Cached result if found and valid, None otherwise
        """
        self.stats['total_calls'] += 1
        key = self._make_key(tool_name, args)

        # Check if key exists
        if key not in self.cache:
            self.stats['misses'] += 1
            return None

        entry = self.cache[key]

        # Check if expired
        age = time.time() - entry.timestamp
        if age > self.ttl_seconds:
            # Expired - remove and count as miss
            del self.cache[key]
            self.stats['misses'] += 1
            return None

        # Valid cache hit
        entry.hit_count += 1
        self.stats['hits'] += 1
        return entry.result

    def set(self, tool_name: str, args: dict, result: Any):
        """
        Store tool result in cache.

        Args:
            tool_name: Name of the MCP tool
            args: Tool arguments as dictionary
            result: Tool result to cache
        """
        # Evict if at capacity
        if len(self.cache) >= self.max_entries:
            self._evict_lru()

        key = self._make_key(tool_name, args)
        self.cache[key] = CacheEntry(
            result=result,
            timestamp=time.time(),
            tool_name=tool_name,
            hit_count=0
        )

    def _evict_lru(self):
        """Evict least recently used entry (oldest with lowest hit count)"""
        if not self.cache:
            return

        # Find entry with lowest hit count, breaking ties by age
        lru_key = min(
            self.cache.keys(),
            key=lambda k: (
                self.cache[k].hit_count,
                -self.cache[k].timestamp  # Negative for oldest first
            )
        )

        del self.cache[lru_key]
        self.stats['evictions'] += 1

    def clear(self):
        """Clear all cache entries"""
        self.cache.clear()

    def get_stats(self) -> dict:
        """
        Get cache performance statistics.

        Returns:
            Dictionary with hit rate, miss rate, and other metrics
        """
        total = self.stats['total_calls']
        if total == 0:
            hit_rate = 0.0
        else:
            hit_rate = (self.stats['hits'] / total) * 100

        return {
            'total_calls': total,
            'hits': self.stats['hits'],
            'misses': self.stats['misses'],
            'hit_rate': f"{hit_rate:.1f}%",
            'evictions': self.stats['evictions'],
            'cache_size': len(self.cache),
            'max_size': self.max_entries
        }

    def get_cached_tools(self) -> list:
        """
        Get list of currently cached tool calls.

        Returns:
            List of tool names and ages
        """
        now = time.time()
        return [
            {
                'tool': entry.tool_name,
                'age_seconds': int(now - entry.timestamp),
                'hit_count': entry.hit_count
            }
            for entry in self.cache.values()
        ]


class CachedToolExecutor:
    """
    Wrapper for MCP tool execution with automatic caching.

    Usage:
        executor = CachedToolExecutor(cache)
        result = await executor.execute('get_company_profile', {'symbol': 'NVDA'})
    """

    def __init__(self, cache: SessionCache, execute_fn):
        """
        Initialize cached executor.

        Args:
            cache: SessionCache instance
            execute_fn: Async function to execute tools (tool_name, args) -> result
        """
        self.cache = cache
        self.execute_fn = execute_fn

    async def execute(self, tool_name: str, args: dict) -> Any:
        """
        Execute tool with caching.

        Checks cache first, executes and caches on miss.

        Args:
            tool_name: Name of the MCP tool
            args: Tool arguments

        Returns:
            Tool result (from cache or fresh execution)
        """
        # Try cache first
        cached_result = self.cache.get(tool_name, args)
        if cached_result is not None:
            return cached_result

        # Cache miss - execute tool
        result = await self.execute_fn(tool_name, args)

        # Cache the result
        self.cache.set(tool_name, args, result)

        return result


# Example usage in chat.py:
"""
class InteractiveChat:
    def __init__(self):
        # Initialize session cache
        self.session_cache = SessionCache(ttl_seconds=300)

        # Wrap tool executor
        self.cached_executor = CachedToolExecutor(
            cache=self.session_cache,
            execute_fn=self._execute_mcp_tool
        )

    async def _execute_tool_with_caching(self, tool_name: str, args: dict):
        '''Execute MCP tool with session-level caching'''
        return await self.cached_executor.execute(tool_name, args)

    def print_cache_stats(self):
        '''Display cache performance statistics'''
        stats = self.session_cache.get_stats()
        self.console.print(f"[cyan]📊 Cache Performance:[/cyan]")
        self.console.print(f"  Hit rate: [green]{stats['hit_rate']}[/green]")
        self.console.print(f"  Total calls: {stats['total_calls']}")
        self.console.print(f"  Cache size: {stats['cache_size']}/{stats['max_size']}")
"""
