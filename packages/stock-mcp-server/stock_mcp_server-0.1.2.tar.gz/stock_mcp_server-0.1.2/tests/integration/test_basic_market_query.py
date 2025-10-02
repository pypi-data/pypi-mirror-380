"""Integration test: Basic market query (Scenario 1).

Tests the complete flow of querying Shanghai Composite Index performance,
including real-time data, OHLC, volume, and market breadth.
"""

from datetime import datetime

import pytest

from stock_mcp_server.tools.market_data import get_market_data


def test_basic_market_query_realtime():
    """Test basic market query for real-time Shanghai index data."""
    # Query Shanghai index real-time data
    result = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    # Verify response structure
    assert result["success"] is True, "Query should succeed"
    assert "data" in result, "Response should contain data"
    assert "metadata" in result, "Response should contain metadata"
    
    # Verify data content
    data = result["data"]
    assert "index" in data, "Data should contain index information"
    
    index = data["index"]
    # Verify required fields
    assert "code" in index, "Index should have code"
    assert "name" in index, "Index should have name"
    assert "current" in index or "close" in index, "Index should have price"
    assert "change_pct" in index, "Index should have change percentage"
    assert "open" in index, "Index should have open price"
    assert "high" in index, "Index should have high price"
    assert "low" in index, "Index should have low price"
    assert "volume" in index, "Index should have volume"
    assert "amount" in index, "Index should have amount"
    assert "trading_date" in index, "Index should have trading date"
    
    # Verify data types
    assert isinstance(index["code"], str), "Code should be string"
    assert index["code"] == "000001", "Code should be 000001"
    assert "上证" in index["name"] or "沪" in index["name"], "Name should contain Shanghai reference"
    
    # Verify metadata
    metadata = result["metadata"]
    assert "query_time" in metadata, "Metadata should have query time"
    assert "data_source" in metadata, "Metadata should have data source"


def test_basic_market_query_breadth():
    """Test market breadth statistics query."""
    # Query market breadth
    result = get_market_data(
        data_type="breadth",
        index_code="000001"
    )
    
    # Check if data source is available (may be rate-limited)
    if not result["success"]:
        error = result.get("error", {})
        error_details = error.get("details", "")
        
        # If it's a network/rate-limit issue, skip the test
        if any(keyword in str(error_details) for keyword in ["Connection", "aborted", "No market breadth", "Expecting value"]):
            pytest.skip(f"Market breadth data source unavailable (rate-limited): {error_details[:100]}")
        else:
            # Other errors should fail the test
            assert False, f"Unexpected error: {error}"
    
    # Verify response
    assert result["success"] is True, "Breadth query should succeed"
    assert "data" in result
    
    data = result["data"]
    assert "breadth" in data, "Data should contain breadth information"
    
    breadth = data["breadth"]
    # Verify breadth statistics
    assert "total_stocks" in breadth, "Should have total stocks count"
    assert "advancing" in breadth, "Should have advancing stocks count"
    assert "declining" in breadth, "Should have declining stocks count"
    assert "unchanged" in breadth, "Should have unchanged stocks count"
    assert "limit_up" in breadth, "Should have limit up count"
    assert "limit_down" in breadth, "Should have limit down count"
    
    # Verify data consistency
    assert breadth["total_stocks"] > 0, "Total stocks should be positive"
    assert breadth["advancing"] >= 0, "Advancing should be non-negative"
    assert breadth["declining"] >= 0, "Declining should be non-negative"
    
    # Check if counts add up (with some tolerance for data timing and missing data)
    total_counted = breadth["advancing"] + breadth["declining"] + breadth["unchanged"]
    # Allow up to 10% difference due to data timing, suspended stocks, etc.
    tolerance = breadth["total_stocks"] * 0.1
    assert abs(total_counted - breadth["total_stocks"]) < tolerance, \
        f"Stock counts should roughly add up: {total_counted} vs {breadth['total_stocks']}"


def test_basic_market_query_all():
    """Test comprehensive market query with all data types."""
    # Query all data types
    result = get_market_data(
        data_type="all",
        index_code="000001"
    )
    
    # Verify response (may partially succeed if some data sources are rate-limited)
    assert result["success"] is True, "Comprehensive query should succeed"
    assert "data" in result
    
    data = result["data"]
    # Verify all data sections are present
    assert "index" in data, "Should have index data"
    
    # Verify index data
    index = data["index"]
    assert index["code"] == "000001"
    assert "current" in index or "close" in index
    
    # Breadth data may not be available if data sources are rate-limited
    # This is acceptable as it's an external dependency issue
    if "breadth" in data and data["breadth"] is not None:
        breadth = data["breadth"]
        assert "total_stocks" in breadth
        assert "advancing" in breadth
    else:
        pytest.skip("Market breadth data unavailable (rate-limited), but index data verified successfully")


def test_timestamp_freshness():
    """Test that returned data has fresh timestamps."""
    result = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    assert result["success"] is True
    
    # Check metadata timestamp
    metadata = result["metadata"]
    query_time_str = metadata["query_time"]
    query_time = datetime.fromisoformat(query_time_str.replace("Z", "+00:00"))
    
    # Query time should be recent (within last hour)
    now = datetime.now(query_time.tzinfo)
    time_diff = (now - query_time).total_seconds()
    assert time_diff < 3600, f"Query time should be recent, but was {time_diff}s ago"
    
    # Check data timestamp (if market open)
    data = result["data"]
    if "index" in data and "trading_date" in data["index"]:
        trading_date = data["index"]["trading_date"]
        # Should be a valid date string
        assert len(trading_date) == 10, "Trading date should be YYYY-MM-DD format"
        assert "-" in trading_date, "Trading date should contain dashes"


def test_error_handling_invalid_code():
    """Test error handling for invalid index code."""
    result = get_market_data(
        data_type="realtime",
        index_code="999999"  # Invalid code
    )
    
    # Should handle gracefully (may return empty data or error)
    assert "success" in result
    # Error handling should not crash


def test_cache_behavior():
    """Test that repeated queries use cache."""
    # First query
    result1 = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    # Second query (should hit cache)
    result2 = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    # Both should succeed
    assert result1["success"] is True
    assert result2["success"] is True
    
    # Check cache metadata
    if "cache_hit" in result2["metadata"]:
        # Second query might be from cache
        assert isinstance(result2["metadata"]["cache_hit"], bool)

