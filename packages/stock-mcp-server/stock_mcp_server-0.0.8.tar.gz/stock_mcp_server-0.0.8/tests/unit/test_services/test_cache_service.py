"""Unit tests for cache service."""

import pytest
from decimal import Decimal
from datetime import datetime

from stock_mcp_server.services.cache_service import CacheService
from stock_mcp_server.models.market import MarketIndex


class TestCacheService:
    """Tests for CacheService."""

    @pytest.fixture
    def cache_service(self, tmp_path):
        """Create a cache service with temporary database."""
        from stock_mcp_server.config import Config
        
        # Create config with temp path
        config = Config()
        config.cache_db_path = tmp_path / "test_cache.db"
        
        from stock_mcp_server import services
        # Reset global cache
        services.cache_service._cache_service = None
        
        cache = CacheService()
        yield cache
        
        # Cleanup
        services.cache_service._cache_service = None

    def test_cache_set_and_get(self, cache_service):
        """Test setting and getting cache values."""
        # Set a value
        cache_service.set("test_category", {"data": "value"}, key="test_key")
        
        # Get the value
        result = cache_service.get("test_category", key="test_key")
        assert result == {"data": "value"}

    def test_cache_miss(self, cache_service):
        """Test cache miss returns default."""
        result = cache_service.get("test_category", default="default_value", key="nonexistent")
        assert result == "default_value"

    def test_cache_with_model(self, cache_service):
        """Test caching Pydantic models."""
        index = MarketIndex(
            code="000001",
            name="上证指数",
            current=Decimal("3245.67"),
            open=Decimal("3230.50"),
            high=Decimal("3250.00"),
            low=Decimal("3228.00"),
            pre_close=Decimal("3235.00"),
            change=Decimal("10.67"),
            change_pct=Decimal("0.33"),
            amplitude=Decimal("0.68"),
            volume=28500000,
            amount=Decimal("345000000000"),
            timestamp=datetime.now(),
            trading_date="2025-09-30",
            market_status="closed",
        )
        
        # Cache the model
        cache_service.set("market_data", index, index_code="000001")
        
        # Retrieve it
        cached = cache_service.get("market_data", index_code="000001")
        assert cached is not None
        assert cached.code == "000001"

    def test_cache_ttl(self, cache_service):
        """Test cache with custom TTL."""
        cache_service.set("test_category", "value", ttl_seconds=1, key="ttl_test")
        
        # Should exist immediately
        result = cache_service.get("test_category", key="ttl_test")
        assert result == "value"

    def test_cache_delete(self, cache_service):
        """Test deleting cache entry."""
        cache_service.set("test_category", "value", key="delete_test")
        
        # Verify it exists
        assert cache_service.get("test_category", key="delete_test") == "value"
        
        # Delete it
        cache_service.delete("test_category", key="delete_test")
        
        # Verify it's gone
        assert cache_service.get("test_category", key="delete_test") is None

    def test_clear_category(self, cache_service):
        """Test clearing all entries in a category."""
        cache_service.set("test_category", "value1", key="key1")
        cache_service.set("test_category", "value2", key="key2")
        cache_service.set("other_category", "value3", key="key3")
        
        # Clear test_category
        cache_service.clear_category("test_category")
        
        # test_category should be cleared
        assert cache_service.get("test_category", key="key1") is None
        assert cache_service.get("test_category", key="key2") is None
        
        # other_category should still exist
        assert cache_service.get("other_category", key="key3") == "value3"

    def test_generate_key_consistency(self, cache_service):
        """Test that same parameters generate same key."""
        key1 = cache_service._generate_key("category", param1="a", param2="b")
        key2 = cache_service._generate_key("category", param1="a", param2="b")
        key3 = cache_service._generate_key("category", param2="b", param1="a")  # Different order
        
        assert key1 == key2
        assert key1 == key3  # Order shouldn't matter

    def test_memory_cache_hit(self, cache_service):
        """Test that memory cache is checked first."""
        # Set a value
        cache_service.set("test_category", "value", key="memory_test")
        
        # Get it twice - second should be from memory cache
        result1 = cache_service.get("test_category", key="memory_test")
        result2 = cache_service.get("test_category", key="memory_test")
        
        assert result1 == "value"
        assert result2 == "value"
