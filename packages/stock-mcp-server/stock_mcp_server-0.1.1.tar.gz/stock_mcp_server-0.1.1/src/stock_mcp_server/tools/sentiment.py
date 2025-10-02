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
        # Use fault-tolerant approach: gather what we can
        try:
            # Try to get index data
            index_data = None
            try:
                index_data = akshare_service.get_index_spot("000001")
            except Exception as e:
                logger.warning(f"Failed to fetch index data: {e}")
            
            # Try to get market breadth
            breadth = None
            try:
                breadth = akshare_service.get_market_breadth(date)
            except Exception as e:
                logger.warning(f"Failed to fetch market breadth: {e}")
            
            # Try to get capital flow
            capital_flow = None
            try:
                capital_flow = akshare_service.get_capital_flow(date)
            except Exception as e:
                logger.warning(f"Failed to fetch capital flow: {e}")
            
            # Check if we have at least some data
            if not any([index_data, breadth, capital_flow]):
                return {
                    "success": False,
                    "metadata": {
                        "query_time": query_time,
                        "data_source": "none"
                    },
                    "error": {
                        "code": "INSUFFICIENT_DATA",
                        "message": "Unable to fetch any market data",
                        "details": "All data sources failed"
                    }
                }
            
            # Prepare market data with fallback values and safe float conversion
            def safe_float(value, default=0.0):
                """Safely convert to float with fallback"""
                try:
                    if value is None:
                        return default
                    return float(value)
                except (TypeError, ValueError):
                    return default
            
            market_data = {
                "volume_ratio": safe_float(getattr(index_data, "volume_ratio", None), 1.0) if index_data else 1.0,
                "advancing": breadth.advancing if (breadth and breadth.advancing) else 2000,
                "declining": breadth.declining if (breadth and breadth.declining) else 2000,
                "total_stocks": breadth.total_stocks if (breadth and breadth.total_stocks) else 4000,
                "change_pct": safe_float(getattr(index_data, "change_pct", None), 0.0) if index_data else 0.0,
                "amplitude": safe_float(getattr(index_data, "amplitude", None), 1.0) if index_data else 1.0,
                "north_net": safe_float(capital_flow.north_net if capital_flow else None, 0),
                "main_net": safe_float(capital_flow.main_net if capital_flow else None, 0),
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
