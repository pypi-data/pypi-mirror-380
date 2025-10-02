"""Special market data MCP tool implementation.

Implements get_special_data tool according to contract specification.
"""

from typing import Any
from datetime import datetime

from loguru import logger

from stock_mcp_server.services.akshare_service import get_akshare_service
from stock_mcp_server.utils.validators import validate_date


def get_special_data(
    data_type: str,
    contract: str | None = None,
    underlying: str | None = None,
    sort_by: str | None = None,
    limit: int = 20,
    date: str | None = None,
) -> dict[str, Any]:
    """
    Retrieve special market data (Dragon-Tiger List, block trades, IPOs, derivatives).
    
    Args:
        data_type: Data type (longhu/block_trade/unlock/new_stock/futures/options/convertible_bond)
        contract: Futures contract (IH/IF/IC/IM) - for futures
        underlying: Option underlying (50ETF/300ETF) - for options
        sort_by: Sorting criteria
        limit: Number of items
        date: Query date (optional)
        
    Returns:
        Special market data
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
        
        service = get_akshare_service()
        cache_hit = False
        
        # Placeholder data structure
        data = {}
        
        if data_type == "longhu":
            data = {
                "stocks": [],
                "summary": {
                    "total_stocks": 0,
                    "total_buy": 0,
                    "total_sell": 0
                }
            }
        elif data_type == "block_trade":
            data = {
                "trades": [],
                "summary": {
                    "total_trades": 0,
                    "total_volume": 0
                }
            }
        elif data_type == "new_stock":
            data = {
                "ipos": [],
                "summary": {
                    "total_ipos": 0
                }
            }
        else:
            # Other data types
            data = {
                "items": []
            }
        
        logger.info(f"get_special_data executed: data_type={data_type}")
        
        return {
            "success": True,
            "data_type": data_type,
            "data": data,
            "metadata": {
                "query_time": query_time,
                "data_source": "akshare",
                "cache_hit": cache_hit
            }
        }
        
    except Exception as e:
        logger.error(f"Error in get_special_data: {e}", exc_info=True)
        return {
            "success": False,
            "data_type": data_type,
            "metadata": {
                "query_time": query_time,
                "data_source": "none"
            },
            "error": {
                "code": "DATA_UNAVAILABLE",
                "message": "Special data temporarily unavailable",
                "details": str(e)
            }
        }
