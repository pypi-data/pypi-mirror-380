"""News analysis MCP tool implementation.

Implements get_news tool according to contract specification.
"""

from typing import Any
from datetime import datetime

from loguru import logger

from stock_mcp_server.services.news_service import get_news_service
from stock_mcp_server.services.sentiment_service import get_sentiment_service


def get_news(
    limit: int = 10,
    category: str = "all",
    importance: float | None = None,
    include_sentiment: bool = True,
    include_hot_topics: bool = False,
    sentiment_method: str = "snownlp",
) -> dict[str, Any]:
    """
    Retrieve and analyze financial news with sentiment scoring.
    
    Args:
        limit: Number of news items (default: 10)
        category: Filter by category (policy/market/company/industry/international/all)
        importance: Minimum importance score (0-10)
        include_sentiment: Perform sentiment analysis
        include_hot_topics: Include hot topics aggregation
        sentiment_method: Sentiment analysis method (snownlp/llm)
        
    Returns:
        News articles with sentiment analysis
    """
    query_time = datetime.now().isoformat()
    
    try:
        news_service = get_news_service()
        sentiment_service = get_sentiment_service()
        cache_hit = False
        
        # Fetch news articles
        news_articles = news_service.fetch_latest_news(
            limit=limit,
            category=category if category != "all" else None
        )
        
        if not news_articles:
            return {
                "success": False,
                "metadata": {
                    "query_time": query_time,
                    "data_source": "cache"
                },
                "error": {
                    "code": "PARSE_ERROR",
                    "message": "Failed to scrape news from all sources",
                    "details": "All news sources unavailable or blocked"
                }
            }
        
        # Filter by importance if specified
        if importance is not None:
            news_articles = [
                article for article in news_articles
                if article.importance >= importance
            ]
        
        # Add sentiment if requested
        if include_sentiment:
            for article in news_articles:
                if not article.sentiment_score:
                    try:
                        sentiment_score = sentiment_service.analyze_text_sentiment(
                            article.title + " " + (article.summary or "")
                        )
                        article.sentiment_score = sentiment_score
                        # Classify sentiment
                        if sentiment_score >= 0.7:
                            article.sentiment = "positive"
                        elif sentiment_score >= 0.4:
                            article.sentiment = "neutral"
                        else:
                            article.sentiment = "negative"
                    except Exception as e:
                        logger.warning(f"Failed to analyze sentiment for article: {e}")
        
        # Calculate hot topics if requested
        hot_topics = []
        overall_sentiment = {
            "positive": 0,
            "neutral": 0,
            "negative": 0
        }
        
        if include_hot_topics:
            # Aggregate tags/keywords
            topic_counts: dict[str, int] = {}
            for article in news_articles:
                if article.tags:
                    for tag in article.tags:
                        topic_counts[tag] = topic_counts.get(tag, 0) + 1
            
            # Get top topics
            sorted_topics = sorted(topic_counts.items(), key=lambda x: x[1], reverse=True)
            hot_topics = [
                {"topic": topic, "count": count, "avg_sentiment": 0.5}
                for topic, count in sorted_topics[:5]
            ]
        
        # Calculate overall sentiment distribution
        for article in news_articles:
            if article.sentiment == "positive":
                overall_sentiment["positive"] += 1
            elif article.sentiment == "negative":
                overall_sentiment["negative"] += 1
            else:
                overall_sentiment["neutral"] += 1
        
        # Convert to percentages
        total = len(news_articles)
        if total > 0:
            overall_sentiment = {
                "positive": round(overall_sentiment["positive"] / total * 100, 1),
                "neutral": round(overall_sentiment["neutral"] / total * 100, 1),
                "negative": round(overall_sentiment["negative"] / total * 100, 1)
            }
        
        logger.info(f"get_news executed: {len(news_articles)} articles fetched")
        
        # Convert to dict
        news_list = [article.model_dump() for article in news_articles]
        
        return {
            "success": True,
            "news": news_list,
            "hot_topics": hot_topics if include_hot_topics else None,
            "overall_sentiment": overall_sentiment if include_sentiment else None,
            "metadata": {
                "query_time": query_time,
                "data_source": "scraped",
                "sources_count": 2,  # Dongfang Fortune, Sina Finance
                "cache_hit": cache_hit
            }
        }
        
    except Exception as e:
        logger.error(f"Error in get_news: {e}", exc_info=True)
        return {
            "success": False,
            "metadata": {
                "query_time": query_time,
                "data_source": "none"
            },
            "error": {
                "code": "PARSE_ERROR",
                "message": "Failed to fetch news",
                "details": str(e)
            }
        }
