"""Integration test: Market overview (Scenario 7).

Tests the complete flow of comprehensive market overview,
combining all data types into a single snapshot.
"""

# Removed pytest import

from stock_mcp_server.tools.overview import get_market_overview



def test_basic_market_overview():
    """Test basic market overview retrieval."""
    result = get_market_overview(
        include_details=False
    )
    
    # Verify response structure
    assert result["success"] is True, "Market overview should succeed"
    assert "data" in result
    assert "overview" in result["data"]
    
    overview = result["data"]["overview"]
    
    # Verify required sections
    assert "index_quotes" in overview or "indices" in overview, \
        "Should have index quotes"
    assert "breadth_summary" in overview or "breadth" in overview, \
        "Should have market breadth"
    assert "capital_summary" in overview or "capital" in overview, \
        "Should have capital flows"
    assert "sentiment_index" in overview or "sentiment" in overview, \
        "Should have sentiment"



def test_overview_index_quotes():
    """Test index quotes in overview."""
    result = get_market_overview(
        include_details=False
    )
    
    assert result["success"] is True
    overview = result["data"]["overview"]
    
    index_key = "index_quotes" if "index_quotes" in overview else "indices"
    indices = overview[index_key]
    
    assert isinstance(indices, dict) or isinstance(indices, list), \
        "Indices should be dict or list"
    
    # Should have at least Shanghai Composite
    if isinstance(indices, dict):
        assert len(indices) > 0, "Should have at least one index"
        # Check first index
        first_index = list(indices.values())[0] if indices else {}
        if first_index:
            assert "name" in first_index or "close" in first_index or "current" in first_index, \
                "Index should have basic info"



def test_overview_breadth_summary():
    """Test market breadth summary in overview."""
    result = get_market_overview(
        include_details=False
    )
    
    assert result["success"] is True
    overview = result["data"]["overview"]
    
    breadth_key = "breadth_summary" if "breadth_summary" in overview else "breadth"
    breadth = overview[breadth_key]
    
    assert isinstance(breadth, dict), "Breadth should be dict"
    
    # Should have key breadth metrics
    breadth_fields = ["advancing", "declining", "total_stocks", "advance_pct"]
    has_breadth_data = any(field in breadth for field in breadth_fields)
    assert has_breadth_data, "Should have breadth data"



def test_overview_capital_summary():
    """Test capital flow summary in overview."""
    result = get_market_overview(
        include_details=False
    )
    
    assert result["success"] is True
    overview = result["data"]["overview"]
    
    capital_key = "capital_summary" if "capital_summary" in overview else "capital"
    capital = overview[capital_key]
    
    assert isinstance(capital, dict), "Capital should be dict"
    
    # Should have capital flow data
    capital_fields = ["north_net", "main_net", "north", "main"]
    has_capital_data = any(field in capital for field in capital_fields)



def test_overview_sentiment():
    """Test sentiment in overview."""
    result = get_market_overview(
        include_details=False
    )
    
    assert result["success"] is True
    overview = result["data"]["overview"]
    
    # Check for sentiment data
    if "sentiment_index" in overview:
        sentiment_index = float(overview["sentiment_index"])
        assert 0 <= sentiment_index <= 100, \
            f"Sentiment index should be 0-100: {sentiment_index}"
    
    if "sentiment_level" in overview:
        valid_levels = ["extreme_panic", "panic", "neutral", "optimistic", "extreme_optimism"]
        assert overview["sentiment_level"] in valid_levels, \
            f"Invalid sentiment level: {overview['sentiment_level']}"



def test_overview_top_sectors():
    """Test top sectors in overview."""
    result = get_market_overview(
        include_details=False
    )
    
    assert result["success"] is True
    overview = result["data"]["overview"]
    
    # Check for sector information
    sector_fields = ["top_sectors", "sectors", "top_sectors_by_gain"]
    has_sectors = any(field in overview for field in sector_fields)
    
    if has_sectors:
        for field in sector_fields:
            if field in overview:
                sectors = overview[field]
                if isinstance(sectors, list) and len(sectors) > 0:
                    sector = sectors[0]
                    if isinstance(sector, dict):
                        assert "name" in sector or "change_pct" in sector, \
                            "Sector should have basic info"



def test_overview_top_news():
    """Test top news in overview."""
    result = get_market_overview(
        include_details=True
    )
    
    assert result["success"] is True
    overview = result["data"]["overview"]
    
    # Check for news
    news_fields = ["top_news", "news"]
    has_news = any(field in overview for field in news_fields)
    
    if has_news:
        for field in news_fields:
            if field in overview:
                news = overview[field]
                if isinstance(news, list):
                    # Should have limited number of news (5 max as per spec)
                    assert len(news) <= 5, "Should have max 5 news items in overview"



def test_overview_core_insight():
    """Test core market insight in overview."""
    result = get_market_overview(
        include_details=False
    )
    
    assert result["success"] is True
    overview = result["data"]["overview"]
    
    # Check for core insight
    insight_fields = ["core_insight", "insight", "summary"]
    has_insight = any(field in overview for field in insight_fields)
    
    if has_insight:
        for field in insight_fields:
            if field in overview:
                insight = overview[field]
                assert isinstance(insight, str), "Insight should be string"
                # Should contain Chinese
                assert any('\u4e00' <= c <= '\u9fff' for c in insight), \
                    "Insight should contain Chinese"



def test_overview_with_details():
    """Test overview with detailed data."""
    result = get_market_overview(
        include_details=True
    )
    
    assert result["success"] is True
    overview = result["data"]["overview"]
    
    # With details, should have more comprehensive data
    # Count how many sections are present
    sections = [
        "index_quotes", "indices",
        "breadth_summary", "breadth",
        "capital_summary", "capital",
        "sentiment_index", "sentiment",
        "top_sectors", "sectors",
        "top_news", "news"
    ]
    
    present_sections = sum(1 for s in sections if s in overview)
    # Should have multiple sections
    assert present_sections >= 3, \
        f"Should have at least 3 data sections: {present_sections}"



def test_overview_without_details():
    """Test overview without detailed data."""
    result = get_market_overview(
        include_details=False
    )
    
    assert result["success"] is True
    # Should still succeed with basic overview
    assert "data" in result
    assert "overview" in result["data"]



def test_overview_consistency():
    """Test consistency across overview sections."""
    result = get_market_overview(
        include_details=True
    )
    
    assert result["success"] is True
    overview = result["data"]["overview"]
    
    # If both sentiment_index and sentiment_level present, they should be consistent
    if "sentiment_index" in overview and "sentiment_level" in overview:
        sentiment_index = float(overview["sentiment_index"])
        sentiment_level = overview["sentiment_level"]
        
        # Verify consistency
        if sentiment_index <= 20:
            assert "panic" in sentiment_level.lower() or sentiment_level == "extreme_panic"
        elif sentiment_index >= 80:
            assert "optimis" in sentiment_level.lower() or sentiment_level == "extreme_optimism"



def test_overview_metadata():
    """Test overview metadata."""
    result = get_market_overview(
        include_details=False
    )
    
    assert result["success"] is True
    assert "metadata" in result
    
    metadata = result["metadata"]
    assert "query_time" in metadata
    assert "data_source" in metadata



def test_overview_date_parameter():
    """Test overview with specific date."""
    from datetime import datetime
    
    result = get_market_overview(
        date=datetime.now().strftime("%Y-%m-%d"),
        include_details=False
    )
    
    assert result["success"] is True
    # Should return overview for specified date
    assert "data" in result



def test_overview_performance():
    """Test that overview meets performance target (<3s)."""
    import time
    
    start_time = time.time()
    
    result = get_market_overview(
        include_details=True
    )
    
    elapsed = time.time() - start_time
    
    assert result["success"] is True
    # Should complete within 3 seconds
    assert elapsed < 3.0, f"Market overview took too long: {elapsed}s"



def test_overview_comprehensive_snapshot():
    """Test that overview provides comprehensive market snapshot."""
    result = get_market_overview(
        include_details=True
    )
    
    assert result["success"] is True
    overview = result["data"]["overview"]
    
    # Count data sections
    required_sections = [
        ("index_quotes", "indices"),
        ("breadth_summary", "breadth"),
        ("capital_summary", "capital"),
        ("sentiment_index", "sentiment")
    ]
    
    sections_present = 0
    for section_pair in required_sections:
        if any(s in overview for s in section_pair):
            sections_present += 1
    
    # Should have most required sections
    assert sections_present >= 3, \
        f"Overview should have comprehensive data: {sections_present}/4 sections"

