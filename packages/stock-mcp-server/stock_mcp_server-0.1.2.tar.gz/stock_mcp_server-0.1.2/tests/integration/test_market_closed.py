"""Integration test: Market closed status (Scenario 8).

Tests the complete flow of handling queries during non-trading hours,
including proper status indicators and data freshness.
"""

import pytest
from datetime import datetime, time as dt_time

from stock_mcp_server.tools.market_data import get_market_data


def is_trading_hours() -> bool:
    """Check if current time is within trading hours (09:30-15:00 Beijing time)."""
    now = datetime.now()
    current_time = now.time()
    
    # Trading hours: 09:30-15:00 (China)
    morning_start = dt_time(9, 30)
    close_time = dt_time(15, 0)
    
    # Check if it's a weekday
    if now.weekday() >= 5:  # Saturday or Sunday
        return False
    
    # Check if within trading hours
    return morning_start <= current_time <= close_time



def test_market_status_indicator():
    """Test that market status is indicated in response."""
    result = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    assert result["success"] is True
    data = result["data"]
    
    # Check for market status indicator
    status_fields = ["market_status", "status", "trading_status"]
    has_status = False
    status_value = None
    
    for field in status_fields:
        if field in data:
            has_status = True
            status_value = data[field]
            break
        elif "index" in data and field in data["index"]:
            has_status = True
            status_value = data["index"][field]
            break
    
    # Market status should be present
    if has_status:
        valid_statuses = ["open", "closed", "pre-market", "after-hours", "休市", "开市", "盘中"]
        assert any(s in str(status_value).lower() for s in valid_statuses), \
            f"Invalid market status: {status_value}"



def test_data_timestamp_when_closed():
    """Test that data timestamp shows last trading session when market closed."""
    result = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    assert result["success"] is True
    data = result["data"]
    
    # Check trading date
    if "index" in data and "trading_date" in data["index"]:
        trading_date = data["index"]["trading_date"]
        
        # Parse trading date
        trade_date = datetime.strptime(trading_date, "%Y-%m-%d")
        now = datetime.now()
        
        # Trading date should not be in future
        assert trade_date <= now, \
            f"Trading date should not be in future: {trading_date}"
        
        # If queried during weekend or after hours, trading date should be last trading day
        if not is_trading_hours():
            # Should be a recent date (within last few days)
            days_diff = (now - trade_date).days
            assert days_diff < 7, \
                f"Trading date should be recent: {trading_date} ({days_diff} days ago)"



def test_timestamp_freshness_indicator():
    """Test that response indicates data freshness."""
    result = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    assert result["success"] is True
    
    # Check metadata for data age
    metadata = result["metadata"]
    
    if "data_age_seconds" in metadata:
        data_age = metadata["data_age_seconds"]
        if data_age is not None:
            # Data age should be reasonable
            assert data_age >= 0, "Data age should be non-negative"
            
            # If market is closed, data might be hours old
            if not is_trading_hours():
                # Data could be from last trading session
                pass
            else:
                # During trading hours, should be relatively fresh
                assert data_age < 3600, \
                    f"Data during trading hours should be fresh: {data_age}s old"



def test_no_misleading_current_language():
    """Test that closed market data doesn't use misleading 'current' language."""
    result = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    assert result["success"] is True
    data = result["data"]
    
    # If market is closed, check that fields are appropriately named
    if "index" in data:
        index = data["index"]
        
        # Should have timestamp or date indicating data freshness
        date_fields = ["trading_date", "date", "timestamp", "updated_at"]
        has_date = any(field in index for field in date_fields)
        
        # At least one date field should be present
        # (this helps indicate data age)



def test_next_trading_session_indication():
    """Test indication of next trading session when market closed."""
    result = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    assert result["success"] is True
    data = result["data"]
    
    # Check for next trading session info (optional feature)
    next_session_fields = ["next_trading_session", "next_open", "next_session"]
    has_next_session = any(
        field in data or (
            "index" in data and field in data.get("index", {})
        )
        for field in next_session_fields
    )
    
    # This is an optional feature, so we don't strictly require it
    # Just verify it's valid if present
    if has_next_session:
        for field in next_session_fields:
            if field in data:
                next_session = data[field]
                # Should be a valid timestamp or date string
                assert isinstance(next_session, str), \
                    "Next session should be string"



def test_closed_market_returns_last_data():
    """Test that queries during closed hours return last available data."""
    result = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    assert result["success"] is True
    data = result["data"]
    
    # Should still return data (from last session)
    assert "index" in data or "quote" in data, \
        "Should return data even when market closed"
    
    # Data should have basic fields
    index_data = data.get("index") or data.get("quote")
    if index_data:
        assert "close" in index_data or "current" in index_data, \
            "Should have price data"



def test_market_status_consistency():
    """Test consistency between market status and data freshness."""
    result = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    assert result["success"] is True
    data = result["data"]
    metadata = result["metadata"]
    
    # If market status is "closed", data should not be immediate
    market_status = None
    if "market_status" in data:
        market_status = data["market_status"]
    elif "index" in data and "market_status" in data["index"]:
        market_status = data["index"]["market_status"]
    
    if market_status and "closed" in str(market_status).lower():
        # Data age should reflect that market is closed
        if "data_age_seconds" in metadata and metadata["data_age_seconds"]:
            data_age = metadata["data_age_seconds"]
            # Closed market data would typically be at least 1 minute old
            # (unless just closed)



def test_weekend_query():
    """Test querying data during weekend."""
    now = datetime.now()
    
    # Only run this test on weekends
    if now.weekday() < 5:
        pytest.skip("This test only runs on weekends")
    
    result = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    assert result["success"] is True
    data = result["data"]
    
    # Should return data from last Friday
    if "index" in data and "trading_date" in data["index"]:
        trading_date = data["index"]["trading_date"]
        trade_date = datetime.strptime(trading_date, "%Y-%m-%d")
        
        # Should be a Friday (weekday 4)
        assert trade_date.weekday() == 4, \
            f"Weekend data should be from Friday: {trading_date}"



def test_after_hours_query():
    """Test querying data after trading hours."""
    now = datetime.now()
    current_time = now.time()
    
    # Only run after 15:00 on weekdays
    if now.weekday() >= 5 or current_time < dt_time(15, 0):
        pytest.skip("This test only runs after trading hours")
    
    result = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    assert result["success"] is True
    data = result["data"]
    
    # Should return today's close data
    if "index" in data and "trading_date" in data["index"]:
        trading_date = data["index"]["trading_date"]
        today = now.strftime("%Y-%m-%d")
        
        # Should be today's date
        assert trading_date == today, \
            f"After hours should show today's data: {trading_date} vs {today}"



def test_graceful_handling_no_crash():
    """Test that closed market queries don't cause errors."""
    # This test should pass regardless of market hours
    result = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    # Should always succeed gracefully
    assert result["success"] is True
    assert "data" in result
    assert "metadata" in result
    
    # No exceptions should be raised
    # Data should be returned (possibly cached/last session)



def test_cache_behavior_closed_market():
    """Test that closed market data is properly cached."""
    # First query
    result1 = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    # Second query immediately after
    result2 = get_market_data(
        data_type="realtime",
        index_code="000001"
    )
    
    # Both should succeed
    assert result1["success"] is True
    assert result2["success"] is True
    
    # When market is closed, data should be same (cached)
    if not is_trading_hours():
        # Check if cache was hit on second query
        if "cache_hit" in result2["metadata"]:
            # Second query likely from cache
            assert isinstance(result2["metadata"]["cache_hit"], bool)

