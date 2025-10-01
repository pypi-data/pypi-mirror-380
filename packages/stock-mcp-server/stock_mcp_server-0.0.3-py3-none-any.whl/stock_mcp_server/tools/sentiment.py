"""Sentiment analysis MCP tool implementation.

Implements get_sentiment_analysis tool according to contract specification.
"""

from typing import Any
from datetime import datetime

from loguru import logger

from stock_mcp_server.services.sentiment_service import get_sentiment_service
from stock_mcp_server.services.akshare_service import get_akshare_service
from stock_mcp_server.utils.validators import validate_date


def get_sentiment_analysis(
    dimension: str = "all",
    date: str | None = None,
    days: int = 30,
    include_trend: bool = False,
) -> dict[str, Any]:
    """
    Calculate multi-dimensional market sentiment index.
    
    Args:
        dimension: Dimension to analyze (all/volume/price/volatility/capital/news)
        date: Analysis date (optional, defaults to today)
        days: Historical trend period (default: 30)
        include_trend: Include trend analysis (true/false)
        
    Returns:
        Sentiment analysis dictionary
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
        
        sentiment_service = get_sentiment_service()
        akshare_service = get_akshare_service()
        cache_hit = False
        
        # Calculate sentiment
        sentiment_data = sentiment_service.calculate_market_sentiment(
            date=date,
            include_trend=include_trend,
            trend_days=days
        )
        
        if not sentiment_data:
            return {
                "success": False,
                "metadata": {
                    "query_time": query_time,
                    "data_source": "none"
                },
                "error": {
                    "code": "INSUFFICIENT_DATA",
                    "message": "Insufficient data for sentiment calculation",
                    "details": "Need at least 1 day of market data"
                }
            }
        
        logger.info(f"get_sentiment_analysis executed: dimension={dimension}, cache_hit={cache_hit}")
        
        return {
            "success": True,
            "sentiment": sentiment_data.model_dump(),
            "metadata": {
                "query_time": query_time,
                "data_source": "calculated",
                "cache_hit": cache_hit
            }
        }
        
    except Exception as e:
        logger.error(f"Error in get_sentiment_analysis: {e}", exc_info=True)
        return {
            "success": False,
            "metadata": {
                "query_time": query_time,
                "data_source": "none"
            },
            "error": {
                "code": "CALCULATION_ERROR",
                "message": "Failed to calculate sentiment",
                "details": str(e)
            }
        }
