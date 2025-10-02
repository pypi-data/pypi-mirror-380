"""Market data MCP tool implementation.

Implements get_market_data tool according to contract specification.
"""

from typing import Any
from datetime import datetime

from loguru import logger

from stock_mcp_server.services.akshare_service import get_akshare_service
from stock_mcp_server.utils.validators import validate_date
from stock_mcp_server.utils.json_utils import sanitize_for_json


def get_market_data(
    data_type: str = "realtime",
    index_code: str = "000001",
    date: str | None = None,
    period: str = "1day",
    adjust: str = "none",
    start_date: str | None = None,
    end_date: str | None = None,
) -> dict[str, Any]:
    """
    Get comprehensive market data for Shanghai Composite Index.
    
    Args:
        data_type: Type of data (realtime/history/breadth/valuation/turnover/all)
        index_code: Index code (default: '000001' for Shanghai Composite)
        date: Query date in YYYY-MM-DD format (optional)
        period: K-line timeframe (only for history)
        adjust: Price adjustment method (none/qfq/hfq)
        start_date: Start date for historical data
        end_date: End date for historical data
        
    Returns:
        Market data dictionary with success status and data/error
    """
    query_time = datetime.now().isoformat()
    
    try:
        # Validate inputs
        if date:
            try:
                validate_date(date)
            except ValueError as e:
                return {
                    "success": False,
                    "data_type": data_type,
                    "metadata": {
                        "query_time": query_time,
                        "data_source": "none"
                    },
                    "error": {
                        "code": "INVALID_DATE",
                        "message": "Invalid date format. Expected YYYY-MM-DD",
                        "details": str(e)
                    }
                }
        
        if start_date:
            validate_date(start_date)
        if end_date:
            validate_date(end_date)
        
        service = get_akshare_service()
        cache_hit = False
        
        # Handle different data types
        if data_type == "realtime":
            result = _get_realtime_data(service, index_code, date)
            cache_hit = result.get("_cache_hit", False)
            
        elif data_type == "history":
            result = _get_historical_data(
                service, index_code, period, adjust, start_date, end_date
            )
            cache_hit = result.get("_cache_hit", False)
            
        elif data_type == "breadth":
            result = _get_breadth_data(service, date)
            cache_hit = result.get("_cache_hit", False)
            
        elif data_type == "valuation":
            result = _get_valuation_data(service, index_code, date)
            cache_hit = result.get("_cache_hit", False)
            
        elif data_type == "turnover":
            result = _get_turnover_data(service, date)
            cache_hit = result.get("_cache_hit", False)
            
        elif data_type == "all":
            result = _get_all_data(service, index_code, date)
            cache_hit = result.get("_cache_hit", False)
            
        else:
            return {
                "success": False,
                "data_type": data_type,
                "metadata": {
                    "query_time": query_time,
                    "data_source": "none"
                },
                "error": {
                    "code": "INVALID_PARAMETER",
                    "message": f"Invalid data_type: {data_type}",
                    "details": "Must be one of: realtime, history, breadth, valuation, turnover, all"
                }
            }
        
        # Remove internal cache flag
        if "_cache_hit" in result:
            del result["_cache_hit"]
        
        # Add standard response fields
        result["success"] = True
        result["data_type"] = data_type
        result["metadata"] = {
            "query_time": query_time,
            "data_source": "akshare",
            "cache_hit": cache_hit
        }
        
        logger.info(f"get_market_data executed: type={data_type}, code={index_code}, cache_hit={cache_hit}")
        
        # Sanitize for JSON serialization (convert Decimal to float)
        return sanitize_for_json(result)
        
    except Exception as e:
        logger.error(f"Error in get_market_data: {e}", exc_info=True)
        return {
            "success": False,
            "data_type": data_type,
            "metadata": {
                "query_time": query_time,
                "data_source": "none"
            },
            "error": {
                "code": "DATA_UNAVAILABLE",
                "message": "Unable to fetch market data",
                "details": str(e)
            }
        }


def _get_realtime_data(service: Any, index_code: str, date: str | None) -> dict[str, Any]:
    """Get real-time index data."""
    # Note: date parameter is not used for real-time data (always gets latest)
    # If a specific date is needed, use historical data instead
    index_data = service.get_index_spot(index_code)
    
    if not index_data:
        raise ValueError(f"No data available for index {index_code}")
    
    return {
        "data": {
            "index": index_data.model_dump()
        },
        "_cache_hit": False  # Track internally
    }


def _get_historical_data(
    service: Any,
    symbol: str,
    timeframe: str,
    adjust: str,
    start_date: str | None,
    end_date: str | None
) -> dict[str, Any]:
    """Get historical K-line data."""
    # For now, return a placeholder - full implementation would use akshare
    # historical data methods
    records = []
    
    # This would be implemented with actual akshare historical data fetch
    # For now, return empty structure that matches contract
    
    return {
        "data": {
            "symbol": symbol,
            "timeframe": timeframe,
            "adjust": adjust,
            "records": records,
            "count": len(records)
        },
        "_cache_hit": False
    }


def _get_breadth_data(service: Any, date: str | None) -> dict[str, Any]:
    """Get market breadth statistics."""
    breadth = service.get_market_breadth(date)
    
    if not breadth:
        raise ValueError("No market breadth data available")
    
    return {
        "data": {
            "breadth": breadth.model_dump()
        },
        "_cache_hit": False
    }


def _get_valuation_data(service: Any, index_code: str, date: str | None) -> dict[str, Any]:
    """Get market valuation metrics."""
    # Placeholder for valuation data
    # Would fetch PE, PB ratios, market cap, etc.
    return {
        "data": {
            "valuation": {
                "index_code": index_code,
                "date": date or datetime.now().strftime("%Y-%m-%d"),
                "pe_ratio": None,
                "pb_ratio": None,
                "market_cap": None
            }
        },
        "_cache_hit": False
    }


def _get_turnover_data(service: Any, date: str | None) -> dict[str, Any]:
    """Get turnover analysis."""
    # Placeholder for turnover data
    return {
        "data": {
            "turnover": {
                "date": date or datetime.now().strftime("%Y-%m-%d"),
                "total_turnover": None,
                "by_size": {}
            }
        },
        "_cache_hit": False
    }


def _get_all_data(service: Any, index_code: str, date: str | None) -> dict[str, Any]:
    """Get comprehensive market data."""
    result = {"data": {}}
    
    # Get real-time index (date parameter not used for real-time data)
    try:
        index_data = service.get_index_spot(index_code)
        if index_data:
            result["data"]["index"] = index_data.model_dump()
    except Exception as e:
        logger.warning(f"Failed to fetch index data: {e}")
        result["data"]["index"] = None
    
    # Get market breadth
    try:
        breadth = service.get_market_breadth(date)
        if breadth:
            result["data"]["breadth"] = breadth.model_dump()
    except Exception as e:
        logger.warning(f"Failed to fetch breadth data: {e}")
        result["data"]["breadth"] = None
    
    # Get capital flow
    try:
        flow = service.get_capital_flow(date)
        if flow:
            result["data"]["capital_flow"] = flow.model_dump()
    except Exception as e:
        logger.warning(f"Failed to fetch capital flow: {e}")
        result["data"]["capital_flow"] = None
    
    result["_cache_hit"] = False
    return result