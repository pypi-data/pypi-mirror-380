"""Integration test: Market sentiment (Scenario 3).

Tests the complete flow of market sentiment analysis,
including sentiment index, component breakdown, and trend analysis.
"""

# Removed pytest import
from datetime import datetime

from stock_mcp_server.tools.sentiment import get_sentiment_analysis



def test_basic_sentiment_analysis():
    """Test basic market sentiment analysis."""
    result = get_sentiment_analysis(
        dimension="all"
    )
    
    # Verify response structure
    assert result["success"] is True, "Sentiment analysis should succeed"
    assert "data" in result
    assert "sentiment" in result["data"]
    
    sentiment = result["data"]["sentiment"]
    
    # Verify required fields
    assert "sentiment_index" in sentiment, "Should have sentiment index"
    assert "sentiment_level" in sentiment, "Should have sentiment level"
    
    # Verify sentiment index is in valid range (0-100)
    sentiment_index = float(sentiment["sentiment_index"])
    assert 0 <= sentiment_index <= 100, \
        f"Sentiment index should be 0-100: {sentiment_index}"
    
    # Verify sentiment level is valid
    valid_levels = ["extreme_panic", "panic", "neutral", "optimistic", "extreme_optimism"]
    assert sentiment["sentiment_level"] in valid_levels, \
        f"Invalid sentiment level: {sentiment['sentiment_level']}"



def test_sentiment_component_breakdown():
    """Test sentiment component breakdown."""
    result = get_sentiment_analysis(
        dimension="all",
        include_trend=True
    )
    
    assert result["success"] is True
    sentiment = result["data"]["sentiment"]
    
    # Verify component scores
    assert "volume_sentiment" in sentiment, "Should have volume sentiment"
    assert "price_sentiment" in sentiment, "Should have price sentiment"
    assert "volatility_sentiment" in sentiment, "Should have volatility sentiment"
    assert "capital_sentiment" in sentiment, "Should have capital sentiment"
    
    # Verify all components are in valid range (0-100)
    components = [
        "volume_sentiment",
        "price_sentiment", 
        "volatility_sentiment",
        "capital_sentiment"
    ]
    
    for component in components:
        if component in sentiment:
            value = float(sentiment[component])
            assert 0 <= value <= 100, \
                f"{component} should be 0-100: {value}"



def test_sentiment_trend_analysis():
    """Test sentiment trend analysis."""
    result = get_sentiment_analysis(
        dimension="all",
        include_trend=True,
        days=30
    )
    
    assert result["success"] is True
    sentiment = result["data"]["sentiment"]
    
    # Check for trend information
    if "sentiment_trend" in sentiment:
        trend = sentiment["sentiment_trend"]
        valid_trends = ["improving", "deteriorating", "stable"]
        assert trend in valid_trends, f"Invalid trend: {trend}"
    
    # Check for previous sentiment comparison
    if "previous_sentiment" in sentiment:
        prev_sentiment = float(sentiment["previous_sentiment"])
        assert 0 <= prev_sentiment <= 100, "Previous sentiment should be valid"
    
    if "sentiment_change" in sentiment:
        change = float(sentiment["sentiment_change"])
        assert -100 <= change <= 100, "Sentiment change should be valid range"



def test_sentiment_chinese_interpretation():
    """Test Chinese interpretation of sentiment."""
    result = get_sentiment_analysis(
        dimension="all"
    )
    
    assert result["success"] is True
    sentiment = result["data"]["sentiment"]
    
    # Check for Chinese interpretation
    assert "interpretation" in sentiment, "Should have interpretation"
    interpretation = sentiment["interpretation"]
    
    assert isinstance(interpretation, str), "Interpretation should be string"
    assert len(interpretation) > 0, "Interpretation should not be empty"
    
    # Check for Chinese characters
    assert any('\u4e00' <= c <= '\u9fff' for c in interpretation), \
        "Interpretation should contain Chinese characters"



def test_sentiment_risk_level():
    """Test risk level assessment."""
    result = get_sentiment_analysis(
        dimension="all"
    )
    
    assert result["success"] is True
    sentiment = result["data"]["sentiment"]
    
    # Check for risk level
    if "risk_level" in sentiment:
        risk_level = sentiment["risk_level"]
        valid_risks = ["low", "medium", "high", "extreme", "低风险", "中等风险", "高风险", "极高风险"]
        # Risk level should be one of the valid values
        assert any(risk in risk_level.lower() for risk in ["low", "medium", "high", "extreme", "低", "中", "高"]), \
            f"Invalid risk level: {risk_level}"



def test_sentiment_by_dimension_volume():
    """Test sentiment analysis for volume dimension only."""
    result = get_sentiment_analysis(
        dimension="volume"
    )
    
    assert result["success"] is True
    sentiment = result["data"]["sentiment"]
    
    # Should have volume sentiment
    assert "volume_sentiment" in sentiment, "Should have volume sentiment"
    volume_sentiment = float(sentiment["volume_sentiment"])
    assert 0 <= volume_sentiment <= 100, "Volume sentiment should be valid"



def test_sentiment_by_dimension_price():
    """Test sentiment analysis for price dimension only."""
    result = get_sentiment_analysis(
        dimension="price"
    )
    
    assert result["success"] is True
    sentiment = result["data"]["sentiment"]
    
    # Should have price sentiment
    assert "price_sentiment" in sentiment, "Should have price sentiment"
    price_sentiment = float(sentiment["price_sentiment"])
    assert 0 <= price_sentiment <= 100, "Price sentiment should be valid"



def test_sentiment_by_dimension_capital():
    """Test sentiment analysis for capital dimension only."""
    result = get_sentiment_analysis(
        dimension="capital"
    )
    
    assert result["success"] is True
    sentiment = result["data"]["sentiment"]
    
    # Should have capital sentiment
    assert "capital_sentiment" in sentiment, "Should have capital sentiment"
    capital_sentiment = float(sentiment["capital_sentiment"])
    assert 0 <= capital_sentiment <= 100, "Capital sentiment should be valid"



def test_sentiment_with_specific_date():
    """Test sentiment analysis for specific date."""
    # Query for a specific date
    result = get_sentiment_analysis(
        date=(datetime.now().strftime("%Y-%m-%d")),
        dimension="all"
    )
    
    assert result["success"] is True
    
    # Check date in response
    sentiment = result["data"]["sentiment"]
    if "date" in sentiment:
        assert sentiment["date"] is not None



def test_sentiment_weights():
    """Test that sentiment calculation uses proper weights."""
    result = get_sentiment_analysis(
        dimension="all"
    )
    
    assert result["success"] is True
    sentiment = result["data"]["sentiment"]
    
    # Check if weights are provided
    if "weights" in sentiment:
        weights = sentiment["weights"]
        assert isinstance(weights, dict), "Weights should be dict"
        
        # Verify weights sum to 1.0 (or close to it)
        if weights:
            total_weight = sum(float(w) for w in weights.values())
            assert 0.9 <= total_weight <= 1.1, \
                f"Weights should sum to ~1.0: {total_weight}"



def test_sentiment_consistency():
    """Test that sentiment values are consistent with classification."""
    result = get_sentiment_analysis(
        dimension="all"
    )
    
    assert result["success"] is True
    sentiment = result["data"]["sentiment"]
    
    sentiment_index = float(sentiment["sentiment_index"])
    sentiment_level = sentiment["sentiment_level"]
    
    # Verify consistency between index and level
    if sentiment_index <= 20:
        assert sentiment_level == "extreme_panic", \
            f"Index {sentiment_index} should be extreme_panic"
    elif sentiment_index <= 40:
        assert sentiment_level == "panic", \
            f"Index {sentiment_index} should be panic"
    elif sentiment_index <= 60:
        assert sentiment_level == "neutral", \
            f"Index {sentiment_index} should be neutral"
    elif sentiment_index <= 80:
        assert sentiment_level == "optimistic", \
            f"Index {sentiment_index} should be optimistic"
    else:
        assert sentiment_level == "extreme_optimism", \
            f"Index {sentiment_index} should be extreme_optimism"



def test_sentiment_metadata():
    """Test sentiment analysis metadata."""
    result = get_sentiment_analysis(
        dimension="all"
    )
    
    assert result["success"] is True
    
    # Check metadata
    assert "metadata" in result
    metadata = result["metadata"]
    assert "query_time" in metadata
    assert "data_source" in metadata

