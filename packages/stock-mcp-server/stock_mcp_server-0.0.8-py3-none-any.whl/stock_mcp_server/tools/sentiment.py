"""Sentiment analysis MCP tool implementation.

Implements get_sentiment_analysis tool according to contract specification.
"""

from typing import Any
from datetime import datetime

from loguru import logger

from stock_mcp_server.services.sentiment_service import get_sentiment_service
from stock_mcp_server.services.akshare_service import get_akshare_service
from stock_mcp_server.utils.validators import validate_date
from stock_mcp_server.utils.json_utils import sanitize_for_json


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
        
        # Fetch market data needed for sentiment calculation
        try:
            index_data = akshare_service.get_index_spot("000001")
            breadth = akshare_service.get_market_breadth(date)
            capital_flow = akshare_service.get_capital_flow(date)
            
            if not index_data or not breadth or not capital_flow:
                return {
                    "success": False,
                    "metadata": {
                        "query_time": query_time,
                        "data_source": "none"
                    },
                    "error": {
                        "code": "INSUFFICIENT_DATA",
                        "message": "Insufficient data for sentiment calculation",
                        "details": "Need market data including index, breadth, and capital flow"
                    }
                }
            
            # Prepare market data for sentiment calculation
            market_data = {
                "volume_ratio": float(getattr(index_data, "volume_ratio", 1.0)),
                "advancing": breadth.advancing,
                "declining": breadth.declining,
                "total_stocks": breadth.total_stocks,
                "change_pct": float(getattr(index_data, "change_pct", 0.0)),
                "amplitude": float(getattr(index_data, "amplitude", 1.0)),
                "north_net": capital_flow.north_net or 0,
                "main_net": capital_flow.main_net or 0,
            }
            
        except Exception as e:
            logger.warning(f"Failed to fetch market data for sentiment: {e}")
            return {
                "success": False,
                "metadata": {
                    "query_time": query_time,
                    "data_source": "none"
                },
                "error": {
                    "code": "DATA_UNAVAILABLE",
                    "message": "Unable to fetch required market data",
                    "details": str(e)
                }
            }
        
        # Calculate sentiment
        sentiment_data = sentiment_service.calculate_market_sentiment(
            market_data=market_data,
            news_articles=None,  # Optional, can be added later
            weights=None  # Use default weights
        )
        
        if not sentiment_data:
            return {
                "success": False,
                "metadata": {
                    "query_time": query_time,
                    "data_source": "none"
                },
                "error": {
                    "code": "CALCULATION_ERROR",
                    "message": "Failed to calculate sentiment",
                    "details": "Sentiment calculation returned None"
                }
            }
        
        logger.info(f"get_sentiment_analysis executed: dimension={dimension}, cache_hit={cache_hit}")
        
        response = {
            "success": True,
            "sentiment": sentiment_data.model_dump(),
            "metadata": {
                "query_time": query_time,
                "data_source": "calculated",
                "cache_hit": cache_hit
            }
        }
        
        # Sanitize for JSON serialization (convert Decimal to float)
        return sanitize_for_json(response)
        
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
