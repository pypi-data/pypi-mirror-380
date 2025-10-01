"""Money flow MCP tool implementation.

Implements get_money_flow tool according to contract specification.
"""

from typing import Any
from datetime import datetime

from loguru import logger

from stock_mcp_server.services.akshare_service import get_akshare_service
from stock_mcp_server.utils.validators import validate_date


def get_money_flow(
    flow_type: str = "all",
    date: str | None = None,
) -> dict[str, Any]:
    """
    Track capital flows across different categories.
    
    Args:
        flow_type: Type of flow (north/margin/main/all)
        date: Query date in YYYY-MM-DD format (optional)
        
    Returns:
        Capital flow data dictionary
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
                    "flow_type": flow_type,
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
        
        # Get capital flow data
        flow_data = service.get_capital_flow(date)
        
        if not flow_data:
            return {
                "success": False,
                "flow_type": flow_type,
                "metadata": {
                    "query_time": query_time,
                    "data_source": "none"
                },
                "error": {
                    "code": "DATA_UNAVAILABLE",
                    "message": "Money flow data temporarily unavailable",
                    "details": "Unable to fetch capital flow data"
                }
            }
        
        # Filter data based on flow_type
        data = flow_data.model_dump()
        
        if flow_type == "north":
            # Return only north capital data
            filtered_data = {
                "north_inflow": data.get("north_inflow"),
                "north_outflow": data.get("north_outflow"),
                "north_net": data.get("north_net"),
                "north_total_holdings": data.get("north_total_holdings"),
                "north_holdings_pct": data.get("north_holdings_pct"),
                "date": data.get("date"),
                "timestamp": data.get("timestamp")
            }
        elif flow_type == "margin":
            # Return only margin trading data
            filtered_data = {
                "margin_balance": data.get("margin_balance"),
                "margin_buy": data.get("margin_buy"),
                "margin_repay": data.get("margin_repay"),
                "short_balance": data.get("short_balance"),
                "short_sell": data.get("short_sell"),
                "short_cover": data.get("short_cover"),
                "margin_total": data.get("margin_total"),
                "date": data.get("date"),
                "timestamp": data.get("timestamp")
            }
        elif flow_type == "main":
            # Return only main capital flow data
            filtered_data = {
                "super_large_net": data.get("super_large_net"),
                "large_net": data.get("large_net"),
                "medium_net": data.get("medium_net"),
                "small_net": data.get("small_net"),
                "main_net": data.get("main_net"),
                "date": data.get("date"),
                "timestamp": data.get("timestamp")
            }
        else:  # all
            filtered_data = data
        
        logger.info(f"get_money_flow executed: flow_type={flow_type}, cache_hit={cache_hit}")
        
        return {
            "success": True,
            "flow_type": flow_type,
            "data": filtered_data,
            "metadata": {
                "query_time": query_time,
                "data_source": "akshare",
                "cache_hit": cache_hit
            }
        }
        
    except Exception as e:
        logger.error(f"Error in get_money_flow: {e}", exc_info=True)
        return {
            "success": False,
            "flow_type": flow_type,
            "metadata": {
                "query_time": query_time,
                "data_source": "none"
            },
            "error": {
                "code": "DATA_UNAVAILABLE",
                "message": "Unable to fetch money flow data",
                "details": str(e)
            }
        }
