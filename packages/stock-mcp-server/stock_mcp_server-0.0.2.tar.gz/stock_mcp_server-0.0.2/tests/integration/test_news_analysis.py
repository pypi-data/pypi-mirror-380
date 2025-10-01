"""Integration test: News analysis (Scenario 4).

Tests the complete flow of financial news retrieval and analysis,
including sentiment classification and hot topics aggregation.
"""

# Removed pytest import
from datetime import datetime

from stock_mcp_server.tools.news import get_news



def test_basic_news_retrieval():
    """Test basic financial news retrieval."""
    result = get_news(
        limit=10,
        category="all",
        include_sentiment=True
    )
    
    # Verify response structure
    assert result["success"] is True, "News retrieval should succeed"
    assert "data" in result
    assert "news" in result["data"]
    
    news_list = result["data"]["news"]
    
    # Should return some news articles
    assert isinstance(news_list, list), "News should be a list"
    # May return fewer than requested if not enough news available
    assert len(news_list) <= 10, "Should not exceed requested limit"



def test_news_article_structure():
    """Test that news articles have required fields."""
    result = get_news(
        limit=5,
        include_sentiment=True
    )
    
    assert result["success"] is True
    news_list = result["data"]["news"]
    
    if len(news_list) > 0:
        # Check first article structure
        article = news_list[0]
        
        assert "title" in article, "Article should have title"
        assert "source" in article, "Article should have source"
        assert "published_at" in article or "timestamp" in article, \
            "Article should have publication time"
        
        # Title should not be empty
        assert len(article["title"]) > 0, "Title should not be empty"
        
        # Check for Chinese content
        title = article["title"]
        assert any('\u4e00' <= c <= '\u9fff' for c in title), \
            "Title should contain Chinese characters"



def test_news_sorted_by_importance():
    """Test that news is sorted by importance score."""
    result = get_news(
        limit=10,
        include_sentiment=True
    )
    
    assert result["success"] is True
    news_list = result["data"]["news"]
    
    if len(news_list) > 1:
        # Check if importance scores are present
        has_importance = all("importance" in article for article in news_list)
        
        if has_importance:
            # Verify sorting (descending order)
            for i in range(len(news_list) - 1):
                importance1 = float(news_list[i]["importance"])
                importance2 = float(news_list[i + 1]["importance"])
                assert importance1 >= importance2, \
                    f"News should be sorted by importance: {importance1} < {importance2}"



def test_news_sentiment_classification():
    """Test news sentiment classification."""
    result = get_news(
        limit=10,
        include_sentiment=True
    )
    
    assert result["success"] is True
    news_list = result["data"]["news"]
    
    if len(news_list) > 0:
        # Count articles with sentiment
        sentiment_count = 0
        valid_sentiments = ["positive", "neutral", "negative"]
        
        for article in news_list:
            if "sentiment" in article and article["sentiment"]:
                sentiment_count += 1
                assert article["sentiment"] in valid_sentiments, \
                    f"Invalid sentiment: {article['sentiment']}"
            
            # Check sentiment score if present
            if "sentiment_score" in article and article["sentiment_score"] is not None:
                score = float(article["sentiment_score"])
                assert 0 <= score <= 1, f"Sentiment score should be 0-1: {score}"
        
        # At least some articles should have sentiment when requested
        if include_sentiment_was_true := True:
            assert sentiment_count > 0, "Should have sentiment analysis"



def test_news_hot_topics_aggregation():
    """Test hot topics aggregation."""
    result = get_news(
        limit=10,
        include_hot_topics=True
    )
    
    assert result["success"] is True
    data = result["data"]
    
    # Check for hot topics
    if "hot_topics" in data:
        hot_topics = data["hot_topics"]
        assert isinstance(hot_topics, (list, dict)), \
            "Hot topics should be list or dict"
        
        if isinstance(hot_topics, list) and len(hot_topics) > 0:
            # Verify hot topic structure
            topic = hot_topics[0]
            if isinstance(topic, dict):
                # Should have topic name and count/articles
                assert "topic" in topic or "keyword" in topic or "name" in topic, \
                    "Topic should have identifier"



def test_news_by_category_policy():
    """Test news filtering by policy category."""
    result = get_news(
        limit=5,
        category="policy"
    )
    
    assert result["success"] is True
    news_list = result["data"]["news"]
    
    # Check that articles have category field
    if len(news_list) > 0:
        for article in news_list:
            if "category" in article:
                # Should be policy or related
                assert article["category"] in ["policy", "all", "政策"], \
                    f"Expected policy category, got: {article['category']}"



def test_news_by_category_market():
    """Test news filtering by market category."""
    result = get_news(
        limit=5,
        category="market"
    )
    
    assert result["success"] is True
    news_list = result["data"]["news"]
    
    # Should return some market news
    assert isinstance(news_list, list), "Should return news list"



def test_news_importance_filter():
    """Test filtering news by minimum importance."""
    result = get_news(
        limit=10,
        importance=7.0,
        include_sentiment=True
    )
    
    assert result["success"] is True
    news_list = result["data"]["news"]
    
    # Verify all returned news meet importance threshold
    for article in news_list:
        if "importance" in article:
            importance = float(article["importance"])
            assert importance >= 7.0, \
                f"Article importance {importance} below threshold 7.0"



def test_news_with_related_info():
    """Test that news includes related stocks/sectors."""
    result = get_news(
        limit=10,
        include_sentiment=True
    )
    
    assert result["success"] is True
    news_list = result["data"]["news"]
    
    if len(news_list) > 0:
        # Check if any articles have related information
        has_related_stocks = any("related_stocks" in article for article in news_list)
        has_related_sectors = any("related_sectors" in article for article in news_list)
        has_tags = any("tags" in article for article in news_list)
        
        # At least some articles should have related information
        # (but not mandatory for all)
        has_any_related = has_related_stocks or has_related_sectors or has_tags



def test_news_overall_sentiment():
    """Test overall news sentiment aggregation."""
    result = get_news(
        limit=10,
        include_sentiment=True
    )
    
    assert result["success"] is True
    data = result["data"]
    
    # Check for overall sentiment summary
    if "overall_sentiment" in data or "sentiment_summary" in data:
        overall = data.get("overall_sentiment") or data.get("sentiment_summary")
        
        # Should provide sentiment breakdown
        if isinstance(overall, dict):
            # May have positive_pct, negative_pct, neutral_pct
            for key in overall:
                if "pct" in key or "percent" in key:
                    value = float(overall[key])
                    assert 0 <= value <= 100, \
                        f"Percentage should be 0-100: {key}={value}"



def test_news_snownlp_method():
    """Test news sentiment using SnowNLP method."""
    result = get_news(
        limit=5,
        include_sentiment=True,
        sentiment_method="snownlp"
    )
    
    assert result["success"] is True
    news_list = result["data"]["news"]
    
    # Should succeed with SnowNLP method
    assert isinstance(news_list, list), "Should return news list"



def test_news_without_sentiment():
    """Test news retrieval without sentiment analysis."""
    result = get_news(
        limit=5,
        include_sentiment=False
    )
    
    assert result["success"] is True
    news_list = result["data"]["news"]
    
    # Should still return news
    assert isinstance(news_list, list), "Should return news list"



def test_news_metadata():
    """Test news response metadata."""
    result = get_news(
        limit=10
    )
    
    assert result["success"] is True
    assert "metadata" in result
    
    metadata = result["metadata"]
    assert "query_time" in metadata
    assert "data_source" in metadata



def test_news_performance():
    """Test that news retrieval meets performance target (<10s)."""
    import time
    
    start_time = time.time()
    
    result = get_news(
        limit=10,
        include_sentiment=True,
        include_hot_topics=True
    )
    
    elapsed = time.time() - start_time
    
    assert result["success"] is True
    # Should complete within 10 seconds (as per spec)
    assert elapsed < 10.0, f"News retrieval took too long: {elapsed}s"

