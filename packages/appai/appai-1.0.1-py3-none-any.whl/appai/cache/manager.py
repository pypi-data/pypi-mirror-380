"""Cache manager with in-memory caching strategy."""

import logging
from typing import Optional, Dict, Any
from collections import OrderedDict

logger = logging.getLogger(__name__)


class CacheManager:
    """
    In-memory LRU cache for AIApp.

    Simple caching without external dependencies.
    Useful for caching task results and patterns during execution.
    """

    def __init__(self, max_size: int = 1000):
        """
        Initialize in-memory cache.

        Args:
            max_size: Maximum number of items to cache (LRU eviction)
        """
        self._cache: OrderedDict = OrderedDict()
        self.max_size = max_size
        self.hits = 0
        self.misses = 0
        logger.info(f"📦 In-memory cache initialized (max_size={max_size})")

    def get(self, key: str) -> Optional[Dict[str, Any]]:
        """Get cached item."""
        if key in self._cache:
            self.hits += 1
            # Move to end (most recently used)
            self._cache.move_to_end(key)
            return self._cache[key]

        self.misses += 1
        return None

    def set(self, key: str, value: Dict[str, Any]):
        """Cache item with LRU eviction."""
        if key in self._cache:
            # Update existing
            self._cache.move_to_end(key)
        else:
            # Add new
            if len(self._cache) >= self.max_size:
                # Evict least recently used
                self._cache.popitem(last=False)

        self._cache[key] = value

    def get_cached_result(self, task_id: str) -> Optional[Dict[str, Any]]:
        """Get cached task result."""
        return self.get(f"result:{task_id}")

    def cache_result(self, task_id: str, result: Dict[str, Any]):
        """Cache task result."""
        self.set(f"result:{task_id}", result)

    def get_cached_pattern(self, pattern_id: str) -> Optional[Dict[str, Any]]:
        """Get cached pattern."""
        return self.get(f"pattern:{pattern_id}")

    def cache_pattern(self, pattern_id: str, pattern: Dict[str, Any]):
        """Cache pattern."""
        self.set(f"pattern:{pattern_id}", pattern)

    def clear_cache(self):
        """Clear all caches."""
        self._cache.clear()
        self.hits = 0
        self.misses = 0
        logger.info("✅ Cache cleared")

    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0

        return {
            "size": len(self._cache),
            "max_size": self.max_size,
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": f"{hit_rate:.1f}%"
        }
