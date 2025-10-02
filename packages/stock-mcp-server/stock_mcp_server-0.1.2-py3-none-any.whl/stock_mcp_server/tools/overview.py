"""Market overview MCP tool implementation.

Implements get_market_overview tool according to contract specification.
"""

from typing import Any
from datetime import datetime

from loguru import logger

from stock_mcp_server.services.akshare_service import get_akshare_service
from stock_mcp_server.services.sentiment_service import get_sentiment_service
from stock_mcp_server.services.news_service import get_news_service
from stock_mcp_server.utils.validators import validate_date
from stock_mcp_server.utils.json_utils import sanitize_for_json


def get_market_overview(
    date: str | None = None,
    include_details: bool = False,
) -> dict[str, Any]:
    """
    Get comprehensive market snapshot combining all data types.
    
    Args:
        date: Query date (optional, defaults to today)
        include_details: Include detailed breakdowns
        
    Returns:
        Comprehensive market overview
    """
    query_time = datetime.now().isoformat()
    
    try:
        # Validate date if provided
        if date:
            try:
                validate_date(date)
            except ValueError as e:
                return {
                    "success": False,
                    "metadata": {
                        "query_time": query_time,
                        "data_source": "none"
                    },
                    "error": {
                        "code": "INVALID_DATE",
                        "message": "Invalid date format",
                        "details": str(e)
                    }
                }
        
        akshare_service = get_akshare_service()
        sentiment_service = get_sentiment_service()
        news_service = get_news_service()
        cache_hit = False
        
        overview = {}
        
        # 1. Index quotes summary
        try:
            index_data = akshare_service.get_index_spot("000001")
            if index_data:
                overview["index_quotes"] = {
                    "000001": {
                        "name": index_data.name,
                        "close": float(index_data.close) if index_data.close else float(index_data.current),
                        "change_pct": float(index_data.change_pct)
                    }
                }
            else:
                overview["index_quotes"] = {}
        except Exception as e:
            logger.warning(f"Failed to fetch index data: {e}")
            overview["index_quotes"] = {}
        
        # 2. Market breadth summary
        try:
            breadth = akshare_service.get_market_breadth(date)
            if breadth:
                overview["breadth_summary"] = {
                    "advancing": breadth.advancing,
                    "declining": breadth.declining,
                    "advance_pct": float(breadth.advance_pct)
                }
            else:
                overview["breadth_summary"] = {
                    "advancing": 0,
                    "declining": 0,
                    "advance_pct": 0.0
                }
        except Exception as e:
            logger.warning(f"Failed to fetch breadth data: {e}")
            overview["breadth_summary"] = {
                "advancing": 0,
                "declining": 0,
                "advance_pct": 0.0
            }
        
        # 3. Capital flow summary
        try:
            flow = akshare_service.get_capital_flow(date)
            if flow:
                overview["capital_summary"] = {
                    "north_net": float(flow.north_net) if flow.north_net else 0,
                    "main_net": float(flow.main_net) if flow.main_net else 0
                }
            else:
                overview["capital_summary"] = {
                    "north_net": 0,
                    "main_net": 0
                }
        except Exception as e:
            logger.warning(f"Failed to fetch capital flow: {e}")
            overview["capital_summary"] = {
                "north_net": 0,
                "main_net": 0
            }
        
        # 4. Sentiment
        try:
            sentiment_data = sentiment_service.calculate_market_sentiment(date)
            if sentiment_data:
                overview["sentiment_index"] = float(sentiment_data.sentiment_index)
                overview["sentiment_level"] = sentiment_data.sentiment_level
            else:
                overview["sentiment_index"] = 50.0
                overview["sentiment_level"] = "neutral"
        except Exception as e:
            logger.warning(f"Failed to calculate sentiment: {e}")
            overview["sentiment_index"] = 50.0
            overview["sentiment_level"] = "neutral"
        
        # 5. Top sectors (placeholder)
        overview["top_sectors_by_gain"] = []
        overview["top_sectors_by_loss"] = []
        
        # 6. Top news
        try:
            if include_details:
                news_articles = news_service.fetch_latest_news(limit=5)
                if news_articles:
                    overview["top_news"] = [
                        {
                            "title": article.title,
                            "importance": float(article.importance),
                            "sentiment": article.sentiment or "neutral"
                        }
                        for article in news_articles[:5]
                    ]
                else:
                    overview["top_news"] = []
            else:
                overview["top_news"] = []
        except Exception as e:
            logger.warning(f"Failed to fetch news: {e}")
            overview["top_news"] = []
        
        # 7. Core insight
        overview["core_insight"] = _generate_core_insight(overview)
        
        # 8. Metadata
        overview["date"] = date or datetime.now().strftime("%Y-%m-%d")
        overview["generated_at"] = query_time
        
        logger.info(f"get_market_overview executed: include_details={include_details}")
        
        response = {
            "success": True,
            "overview": overview,
            "metadata": {
                "query_time": query_time,
                "data_source": "aggregated",
                "cache_hit": cache_hit
            }
        }
        
        # Sanitize for JSON serialization (convert Decimal to float)
        return sanitize_for_json(response)
        
    except Exception as e:
        logger.error(f"Error in get_market_overview: {e}", exc_info=True)
        return {
            "success": False,
            "metadata": {
                "query_time": query_time,
                "data_source": "none"
            },
            "error": {
                "code": "DATA_UNAVAILABLE",
                "message": "Cannot generate market overview",
                "details": str(e)
            }
        }


def _generate_core_insight(overview: dict[str, Any]) -> str:
    """Generate core market insight from overview data."""
    # Simple logic to generate insight
    sentiment_index = overview.get("sentiment_index", 50)
    advance_pct = overview["breadth_summary"].get("advance_pct", 0)
    north_net = overview["capital_summary"].get("north_net", 0)
    
    insights = []
    
    # Sentiment insight
    if sentiment_index > 60:
        insights.append("市场情绪偏乐观")
    elif sentiment_index < 40:
        insights.append("市场情绪偏谨慎")
    else:
        insights.append("市场情绪中性")
    
    # Breadth insight
    if advance_pct > 55:
        insights.append("市场宽度良好")
    elif advance_pct < 45:
        insights.append("市场偏弱")
    
    # Capital insight
    if north_net > 1000000000:  # > 10亿
        insights.append("北向资金大幅流入")
    elif north_net < -1000000000:
        insights.append("北向资金流出")
    
    if insights:
        return "，".join(insights) + "。"
    else:
        return "市场整体平稳。"
