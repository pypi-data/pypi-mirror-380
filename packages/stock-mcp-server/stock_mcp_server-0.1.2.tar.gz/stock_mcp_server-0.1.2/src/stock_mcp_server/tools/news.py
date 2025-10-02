"""News analysis MCP tool implementation.

Implements get_news tool according to contract specification.
"""

from typing import Any
from datetime import datetime

from loguru import logger

from stock_mcp_server.services.news_service import get_news_service
from stock_mcp_server.services.sentiment_service import get_sentiment_service
from stock_mcp_server.utils.json_utils import sanitize_for_json


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
    news_articles = []
    data_source = "none"
    sources_tried = []
    cache_hit = False
    
    try:
        news_service = get_news_service()
        sentiment_service = get_sentiment_service()
        
        # Source 1: Try primary news service
        try:
            logger.info("Attempting to fetch from primary news service...")
            sources_tried.append("primary")
            news_articles = news_service.fetch_latest_news(
                limit=limit,
                category=category if category != "all" else None
            )
            if news_articles:
                data_source = "primary_scraper"
        except Exception as e:
            logger.warning(f"Primary news source failed: {e}")
            sources_tried.append("primary_failed")
        
        # Source 2: If primary failed, try akshare news
        if not news_articles:
            try:
                logger.info("Attempting to fetch from akshare...")
                sources_tried.append("akshare")
                from stock_mcp_server.services.akshare_service import get_akshare_service
                akshare = get_akshare_service()
                news_articles = akshare.get_news(limit=limit)
                if news_articles:
                    data_source = "akshare"
            except Exception as e:
                logger.warning(f"AKShare news source failed: {e}")
                sources_tried.append("akshare_failed")
        
        # Source 3: If both failed, try alternative news API
        if not news_articles:
            try:
                logger.info("Attempting to fetch from alternative source...")
                sources_tried.append("alternative")
                news_articles = _fetch_from_alternative_source(limit, category)
                if news_articles:
                    data_source = "alternative"
            except Exception as e:
                logger.warning(f"Alternative news source failed: {e}")
                sources_tried.append("alternative_failed")
        
        if not news_articles:
            return {
                "success": False,
                "metadata": {
                    "query_time": query_time,
                    "data_source": "none",
                    "sources_tried": sources_tried
                },
                "error": {
                    "code": "ALL_SOURCES_FAILED",
                    "message": "Failed to fetch news from all available sources",
                    "details": f"Tried {len(sources_tried)} sources: {', '.join(sources_tried)}"
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
        
        response = {
            "success": True,
            "news": news_list,
            "hot_topics": hot_topics if include_hot_topics else None,
            "overall_sentiment": overall_sentiment if include_sentiment else None,
            "metadata": {
                "query_time": query_time,
                "data_source": data_source,
                "sources_tried": sources_tried,
                "cache_hit": cache_hit
            }
        }
        
        # Sanitize for JSON serialization (convert Decimal to float)
        return sanitize_for_json(response)
        
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


def _fetch_from_alternative_source(limit: int, category: str | None) -> list:
    """Fetch news from alternative sources - 24/7 available sources.
    
    These sources work reliably in non-trading hours (evenings/weekends).
    Uses only verified akshare APIs that exist.
    
    Args:
        limit: Number of articles to fetch
        category: Category filter
        
    Returns:
        List of NewsArticle objects
    """
    from stock_mcp_server.models.news import NewsArticle, NewsCategory
    
    articles = []
    
    try:
        import akshare as ak
        
        # Source 1: 东方财富新闻 (24/7 available, most reliable)
        try:
            logger.info("Trying Eastmoney News (stock_news_em)...")
            df = ak.stock_news_em()
            if df is not None and not df.empty:
                for idx, row in df.head(limit).iterrows():
                    try:
                        article = NewsArticle(
                            title=str(row.get("新闻标题", "")),
                            url=str(row.get("新闻链接", "")),
                            source="东方财富",
                            published_at=datetime.now(),
                            category=NewsCategory.MARKET,
                            summary=str(row.get("新闻内容", ""))[:200] if "新闻内容" in row else None,
                            importance=6.0,
                            scraped_at=datetime.now()
                        )
                        articles.append(article)
                    except Exception as e:
                        logger.debug(f"Skip one news item: {e}")
                        continue
        except Exception as e:
            logger.warning(f"Failed to fetch from Eastmoney: {e}")
        
        # Source 2: 央视新闻 (CCTV - reliable in evenings)
        if len(articles) < limit:
            try:
                logger.info("Trying CCTV Finance (news_cctv)...")
                df = ak.news_cctv()
                if df is not None and not df.empty:
                    remaining = limit - len(articles)
                    for idx, row in df.head(remaining).iterrows():
                        try:
                            article = NewsArticle(
                                title=str(row.get("title", "")),
                                url="https://tv.cctv.com/lm/jjxx/",
                                source="央视财经",
                                published_at=datetime.now(),
                                category=NewsCategory.MARKET,
                                summary=str(row.get("content", ""))[:200] if "content" in row else None,
                                importance=7.0,
                                scraped_at=datetime.now()
                            )
                            articles.append(article)
                        except Exception as e:
                            logger.debug(f"Skip one news item: {e}")
                            continue
            except Exception as e:
                logger.warning(f"Failed to fetch from CCTV news: {e}")
        
        # Source 3: 财新网新闻 (Caixin - professional, 16k+ articles!)
        if len(articles) < limit:
            try:
                logger.info("Trying Caixin News (stock_news_main_cx)...")
                df = ak.stock_news_main_cx()
                if df is not None and not df.empty:
                    remaining = limit - len(articles)
                    for idx, row in df.head(remaining).iterrows():
                        try:
                            # Caixin uses 'summary' as title and 'tag' for category
                            summary = str(row.get("summary", ""))
                            url = str(row.get("url", "https://www.caixin.com"))
                            tag = str(row.get("tag", ""))
                            
                            if summary:  # Only add if we have a summary
                                article = NewsArticle(
                                    title=summary[:100] if len(summary) > 100 else summary,
                                    url=url,
                                    source="财新网",
                                    published_at=datetime.now(),
                                    category=NewsCategory.MARKET,
                                    summary=summary[:200],
                                    importance=8.0,
                                    tags=[tag] if tag else None,
                                    scraped_at=datetime.now()
                                )
                                articles.append(article)
                        except Exception as e:
                            logger.debug(f"Skip one Caixin news item: {e}")
                            continue
            except Exception as e:
                logger.warning(f"Failed to fetch from Caixin: {e}")
                
    except Exception as e:
        logger.error(f"Failed to fetch from alternative sources: {e}")
    
    logger.info(f"Alternative sources fetched {len(articles)} articles")
    return articles
