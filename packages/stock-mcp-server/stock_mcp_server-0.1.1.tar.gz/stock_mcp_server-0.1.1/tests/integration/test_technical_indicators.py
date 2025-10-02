"""Integration test: Technical indicators (Scenario 2).

Tests the complete flow of calculating technical indicators,
including MA, MACD, RSI, and signal generation.
"""

# Removed pytest import
from datetime import datetime, timedelta

from stock_mcp_server.tools.indicators import calculate_indicators



def test_calculate_ma_indicators():
    """Test MA (Moving Average) indicator calculation."""
    result = calculate_indicators(
        indicators=["ma"],
        period="d",
        start_date=(datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d"),
        end_date=datetime.now().strftime("%Y-%m-%d")
    )
    
    # Verify response structure
    assert result["success"] is True, "MA calculation should succeed"
    assert "data" in result
    assert "indicators" in result["data"]
    
    indicators = result["data"]["indicators"]
    assert len(indicators) > 0, "Should return at least one indicator"
    
    # Find MA indicator
    ma_indicator = None
    for ind in indicators:
        if ind["name"].upper() == "MA":
            ma_indicator = ind
            break
    
    assert ma_indicator is not None, "Should return MA indicator"
    
    # Verify MA structure
    assert "values" in ma_indicator, "MA should have values"
    assert "category" in ma_indicator, "MA should have category"
    assert ma_indicator["category"] == "trend", "MA should be trend indicator"
    
    # Verify MA values
    values = ma_indicator["values"]
    assert isinstance(values, dict), "Values should be dict"
    # Should have multiple MA periods (5, 10, 20, 60, etc.)
    assert len(values) > 0, "Should have at least one MA value"



def test_calculate_macd_indicators():
    """Test MACD indicator calculation and signal generation."""
    result = calculate_indicators(
        indicators=["macd"],
        period="d",
        start_date=(datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d"),
        end_date=datetime.now().strftime("%Y-%m-%d")
    )
    
    assert result["success"] is True, "MACD calculation should succeed"
    
    indicators = result["data"]["indicators"]
    macd_indicator = None
    for ind in indicators:
        if ind["name"].upper() == "MACD":
            macd_indicator = ind
            break
    
    assert macd_indicator is not None, "Should return MACD indicator"
    
    # Verify MACD structure
    assert "values" in macd_indicator
    assert "signal" in macd_indicator, "MACD should have signal"
    assert "interpretation" in macd_indicator, "MACD should have interpretation"
    
    # Verify MACD values (should have DIF, DEA, MACD)
    values = macd_indicator["values"]
    # MACD typically has these components
    assert len(values) > 0, "Should have MACD values"
    
    # Verify signal is valid
    valid_signals = ["strong_buy", "buy", "neutral", "sell", "strong_sell"]
    if macd_indicator["signal"]:
        assert macd_indicator["signal"] in valid_signals, \
            f"Signal should be valid: {macd_indicator['signal']}"
    
    # Verify interpretation is in Chinese
    if macd_indicator["interpretation"]:
        interpretation = macd_indicator["interpretation"]
        assert isinstance(interpretation, str), "Interpretation should be string"
        # Check for Chinese characters
        assert any('\u4e00' <= c <= '\u9fff' for c in interpretation), \
            "Interpretation should contain Chinese characters"



def test_calculate_rsi_indicators():
    """Test RSI indicator calculation."""
    result = calculate_indicators(
        indicators=["rsi"],
        period="d",
        start_date=(datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d"),
        end_date=datetime.now().strftime("%Y-%m-%d")
    )
    
    assert result["success"] is True, "RSI calculation should succeed"
    
    indicators = result["data"]["indicators"]
    rsi_indicator = None
    for ind in indicators:
        if ind["name"].upper() == "RSI":
            rsi_indicator = ind
            break
    
    assert rsi_indicator is not None, "Should return RSI indicator"
    
    # Verify RSI values are in valid range (0-100)
    values = rsi_indicator["values"]
    for key, value in values.items():
        if isinstance(value, (int, float)):
            assert 0 <= value <= 100, f"RSI value should be 0-100: {key}={value}"
        elif isinstance(value, list):
            for v in value:
                if isinstance(v, (int, float)):
                    assert 0 <= v <= 100, f"RSI value should be 0-100: {v}"



def test_multiple_indicator_categories():
    """Test requesting multiple indicator categories."""
    result = calculate_indicators(
        indicators=["ma", "rsi", "macd", "boll"],
        period="d",
        start_date=(datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d"),
        end_date=datetime.now().strftime("%Y-%m-%d")
    )
    
    assert result["success"] is True, "Multiple indicators should succeed"
    
    indicators = result["data"]["indicators"]
    assert len(indicators) >= 3, "Should return at least 3 indicators"
    
    # Verify different categories are present
    categories = set()
    for ind in indicators:
        if "category" in ind:
            categories.add(ind["category"])
    
    # Should have multiple categories
    assert len(categories) >= 2, f"Should have multiple categories: {categories}"



def test_indicator_signals():
    """Test that indicators generate appropriate trading signals."""
    result = calculate_indicators(
        indicators=["ma", "macd", "rsi"],
        period="d",
        start_date=(datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d"),
        end_date=datetime.now().strftime("%Y-%m-%d")
    )
    
    assert result["success"] is True
    
    indicators = result["data"]["indicators"]
    
    # Count indicators with signals
    signals_count = 0
    valid_signals = ["strong_buy", "buy", "neutral", "sell", "strong_sell"]
    
    for ind in indicators:
        if "signal" in ind and ind["signal"]:
            signals_count += 1
            assert ind["signal"] in valid_signals, \
                f"Invalid signal: {ind['signal']} for {ind['name']}"
    
    # At least some indicators should have signals
    assert signals_count > 0, "At least one indicator should have a signal"



def test_indicator_chinese_interpretation():
    """Test that indicators provide Chinese interpretations."""
    result = calculate_indicators(
        indicators=["ma", "macd"],
        period="d",
        start_date=(datetime.now() - timedelta(days=60)).strftime("%Y-%m-%d"),
        end_date=datetime.now().strftime("%Y-%m-%d")
    )
    
    assert result["success"] is True
    
    indicators = result["data"]["indicators"]
    
    # Check for Chinese interpretations
    chinese_count = 0
    for ind in indicators:
        if "interpretation" in ind and ind["interpretation"]:
            interpretation = ind["interpretation"]
            # Check for Chinese characters
            if any('\u4e00' <= c <= '\u9fff' for c in interpretation):
                chinese_count += 1
    
    # At least some indicators should have Chinese interpretations
    assert chinese_count > 0, "Should have Chinese interpretations"



def test_indicator_by_category():
    """Test requesting indicators by category."""
    result = calculate_indicators(
        category="trend",
        period="d",
        start_date=(datetime.now() - timedelta(days=60)).strftime("%Y-%m-%d"),
        end_date=datetime.now().strftime("%Y-%m-%d")
    )
    
    # Should succeed even if specific indicators not requested
    # (category should filter/select appropriate indicators)
    assert "success" in result
    assert "data" in result



def test_indicator_with_custom_params():
    """Test indicators with custom parameters."""
    result = calculate_indicators(
        indicators=["ma"],
        params={
            "ma_periods": [5, 10, 20, 60]
        },
        period="d",
        start_date=(datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d"),
        end_date=datetime.now().strftime("%Y-%m-%d")
    )
    
    assert result["success"] is True, "Custom params should work"
    
    indicators = result["data"]["indicators"]
    assert len(indicators) > 0, "Should return indicators with custom params"



def test_comprehensive_analysis_summary():
    """Test that comprehensive analysis summary is provided."""
    result = calculate_indicators(
        indicators=["ma", "macd", "rsi", "kdj"],
        period="d",
        start_date=(datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d"),
        end_date=datetime.now().strftime("%Y-%m-%d")
    )
    
    assert result["success"] is True
    
    # Check if summary/overall signal is provided
    data = result["data"]
    if "summary" in data:
        summary = data["summary"]
        # Summary should provide overall assessment
        assert isinstance(summary, (str, dict)), "Summary should be string or dict"

