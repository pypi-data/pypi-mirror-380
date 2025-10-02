"""Cache service with two-tier caching (in-memory + SQLite)."""

import hashlib
import json
import pickle
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from cachetools import TTLCache
from loguru import logger
from sqlalchemy import Column, DateTime, Integer, LargeBinary, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from stock_mcp_server.config import get_config

Base = declarative_base()


class CacheEntry(Base):
    """SQLite cache entry model."""

    __tablename__ = "cache_entries"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True, nullable=False)
    value = Column(LargeBinary, nullable=False)  # Pickled data
    category = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    expires_at = Column(DateTime, index=True, nullable=False)


class CacheService:
    """Two-tier cache service (in-memory + SQLite)."""

    def __init__(self) -> None:
        """Initialize cache service."""
        config = get_config()
        self.config = config

        # In-memory cache (TTL cache)
        self.memory_cache: TTLCache[str, Any] = TTLCache(
            maxsize=config.cache.in_memory_max_items,
            ttl=300,  # Default 5 minutes
        )

        # SQLite cache
        db_path = config.cache_db_path
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.engine = create_engine(f"sqlite:///{db_path}", echo=False)
        Base.metadata.create_all(self.engine)
        self.SessionLocal = sessionmaker(bind=self.engine)

        logger.info(f"Cache service initialized: db={db_path}")

    def _generate_key(self, category: str, **params: Any) -> str:
        """Generate cache key from category and parameters."""
        param_str = json.dumps(params, sort_keys=True, default=str)
        hash_str = hashlib.md5(param_str.encode()).hexdigest()
        return f"{category}:{hash_str}"

    def get(
        self, category: str, default: Any = None, **params: Any
    ) -> Any:
        """
        Get value from cache.
        
        Args:
            category: Cache category (e.g., "market_data", "news")
            default: Default value if not found
            **params: Parameters to identify the cached item
            
        Returns:
            Cached value or default
        """
        key = self._generate_key(category, **params)

        # Try in-memory cache first
        if key in self.memory_cache:
            logger.debug(f"Cache HIT (memory): {key}")
            return self.memory_cache[key]

        # Try SQLite cache
        try:
            with self.SessionLocal() as session:
                entry = (
                    session.query(CacheEntry)
                    .filter(
                        CacheEntry.key == key, CacheEntry.expires_at > datetime.now()
                    )
                    .first()
                )

                if entry:
                    value = pickle.loads(entry.value)
                    # Populate memory cache for next access
                    self.memory_cache[key] = value
                    logger.debug(f"Cache HIT (sqlite): {key}")
                    return value

        except Exception as e:
            logger.error(f"Cache read error: {e}")

        logger.debug(f"Cache MISS: {key}")
        return default

    def set(
        self, category: str, value: Any, ttl_seconds: int | None = None, **params: Any
    ) -> None:
        """
        Set value in cache.
        
        Args:
            category: Cache category
            value: Value to cache
            ttl_seconds: Time-to-live in seconds (None = use default)
            **params: Parameters to identify the cached item
        """
        key = self._generate_key(category, **params)

        # Use category-specific TTL if not provided
        if ttl_seconds is None:
            ttl_seconds = self._get_default_ttl(category)

        # Set in memory cache
        self.memory_cache[key] = value

        # Set in SQLite cache
        try:
            with self.SessionLocal() as session:
                expires_at = datetime.now() + timedelta(seconds=ttl_seconds)
                
                # Delete existing entry if present
                session.query(CacheEntry).filter(CacheEntry.key == key).delete()
                
                # Insert new entry
                entry = CacheEntry(
                    key=key,
                    value=pickle.dumps(value),
                    category=category,
                    expires_at=expires_at,
                )
                session.add(entry)
                session.commit()
                logger.debug(f"Cache SET: {key} (ttl={ttl_seconds}s)")

        except Exception as e:
            logger.error(f"Cache write error: {e}")

    def delete(self, category: str, **params: Any) -> None:
        """Delete specific cache entry."""
        key = self._generate_key(category, **params)

        # Delete from memory
        self.memory_cache.pop(key, None)

        # Delete from SQLite
        try:
            with self.SessionLocal() as session:
                session.query(CacheEntry).filter(CacheEntry.key == key).delete()
                session.commit()
                logger.debug(f"Cache DELETE: {key}")
        except Exception as e:
            logger.error(f"Cache delete error: {e}")

    def clear_category(self, category: str) -> None:
        """Clear all entries in a category."""
        try:
            with self.SessionLocal() as session:
                deleted = (
                    session.query(CacheEntry)
                    .filter(CacheEntry.category == category)
                    .delete()
                )
                session.commit()
                logger.info(f"Cache cleared: category={category}, deleted={deleted}")
        except Exception as e:
            logger.error(f"Cache clear error: {e}")

        # Clear memory cache (can't selectively clear by category)
        self.memory_cache.clear()

    def cleanup_expired(self) -> None:
        """Remove expired entries from SQLite cache."""
        try:
            with self.SessionLocal() as session:
                deleted = (
                    session.query(CacheEntry)
                    .filter(CacheEntry.expires_at < datetime.now())
                    .delete()
                )
                session.commit()
                logger.info(f"Cache cleanup: removed {deleted} expired entries")
        except Exception as e:
            logger.error(f"Cache cleanup error: {e}")

    def _get_default_ttl(self, category: str) -> int:
        """Get default TTL for a category."""
        config = self.config
        ttl_map = {
            "market_data": config.refresh_intervals.realtime,
            "news": config.refresh_intervals.news,
            "historical": config.refresh_intervals.historical,
            "indicators": config.refresh_intervals.indicators,
            "sentiment": config.refresh_intervals.sentiment,
        }
        return ttl_map.get(category, 300)  # Default 5 minutes


# Global cache instance
_cache_service: CacheService | None = None


def get_cache() -> CacheService:
    """Get global cache service instance."""
    global _cache_service
    if _cache_service is None:
        _cache_service = CacheService()
    return _cache_service

