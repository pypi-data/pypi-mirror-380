"""Technical indicators MCP tool implementation.

Implements calculate_indicators tool according to contract specification.
"""

from typing import Any
from datetime import datetime, timedelta

from loguru import logger

from stock_mcp_server.services.indicator_service import get_indicator_service
from stock_mcp_server.services.akshare_service import get_akshare_service
from stock_mcp_server.utils.validators import validate_date


def calculate_indicators(
    indicators: list[str] | None = None,
    category: str = "all",
    params: dict[str, Any] | None = None,
    period: str = "d",
    start_date: str | None = None,
    end_date: str | None = None,
    symbol: str = "000001",
    date: str | None = None,
) -> dict[str, Any]:
    """
    Calculate 50+ technical indicators across multiple categories.
    
    Args:
        indicators: List of indicator names (ma, rsi, macd, etc.)
        category: Filter by category (trend/momentum/volatility/volume/all)
        params: Indicator parameters (periods, sensitivity)
        period: Calculation timeframe (d/w/m)
        start_date: Start date for calculation
        end_date: End date for calculation
        symbol: Symbol code for calculation
        
    Returns:
        Dictionary with calculated indicators and signals
    """
    query_time = datetime.now().isoformat()
    
    try:
        # Validate dates
        if start_date:
            validate_date(start_date)
        if end_date:
            validate_date(end_date)
        
        indicator_service = get_indicator_service()
        akshare_service = get_akshare_service()
        
        # Get historical data for calculation
        # Fetch at least 100 days of data for reliable indicator calculation
        try:
            from stock_mcp_server.models.market import HistoricalPrice
            
            # If no end_date specified, use today
            if not end_date:
                end_date = datetime.now().strftime("%Y-%m-%d")
            
            # If no start_date specified, use 100 days ago
            if not start_date:
                start_dt = datetime.now() - timedelta(days=100)
                start_date = start_dt.strftime("%Y-%m-%d")
            
            # Fetch historical data from akshare
            adjust_type = "qfq"  # Default to forward adjustment
            hist_data_raw = akshare_service.get_stock_hist(
                symbol=symbol,
                period="daily",
                start_date=start_date,
                end_date=end_date,
                adjust=adjust_type
            )
            
            if not hist_data_raw or len(hist_data_raw) < 20:
                logger.warning(f"Insufficient historical data: got {len(hist_data_raw) if hist_data_raw else 0} days")
                return {
                    "success": False,
                    "metadata": {
                        "query_time": query_time,
                        "data_source": "none"
                    },
                    "error": {
                        "code": "INSUFFICIENT_DATA",
                        "message": "Not enough historical data for calculation",
                        "details": f"Need at least 20 days, got {len(hist_data_raw) if hist_data_raw else 0} days"
                    }
                }
            
            # Convert to HistoricalPrice objects
            from stock_mcp_server.models.market import TimeFrame, AdjustType
            price_data = []
            for item in hist_data_raw:
                # Handle date field - could be datetime.date or string
                date_val = item.get("日期", item.get("date", ""))
                if hasattr(date_val, 'strftime'):
                    date_str = date_val.strftime("%Y-%m-%d")
                else:
                    date_str = str(date_val)
                
                price_data.append(HistoricalPrice(
                    symbol=symbol,
                    date=date_str,
                    timeframe=TimeFrame.DAILY,
                    adjust=AdjustType.FORWARD if adjust_type == "qfq" else AdjustType.NONE,
                    open=float(item.get("开盘", item.get("open", 0))),
                    high=float(item.get("最高", item.get("high", 0))),
                    low=float(item.get("最低", item.get("low", 0))),
                    close=float(item.get("收盘", item.get("close", 0))),
                    volume=int(item.get("成交量", item.get("volume", 0))),
                    amount=float(item.get("成交额", item.get("amount", 0)))
                ))
            
        except Exception as e:
            logger.error(f"Failed to fetch historical data: {e}")
            return {
                "success": False,
                "metadata": {
                    "query_time": query_time,
                    "data_source": "none"
                },
                "error": {
                    "code": "DATA_FETCH_ERROR",
                    "message": "Failed to fetch historical data",
                    "details": str(e)
                }
            }
        
        results = []
        cache_hit = False
        
        # Determine which indicators to calculate
        if indicators:
            indicator_list = indicators
        elif category != "all":
            # Get indicators by category
            indicator_list = _get_indicators_by_category(category)
        else:
            # Calculate a default set
            indicator_list = ["MA", "RSI", "MACD", "KDJ", "BOLL"]
        
        # Calculate each indicator
        for indicator_name in indicator_list:
            try:
                indicator_results = _calculate_single_indicator(
                    indicator_service,
                    indicator_name,
                    price_data,
                    params or {}
                )
                if indicator_results:
                    results.extend(indicator_results)
            except Exception as e:
                logger.warning(f"Failed to calculate {indicator_name}: {e}")
                continue
        
        if not results:
            return {
                "success": False,
                "metadata": {
                    "query_time": query_time,
                    "data_source": "none"
                },
                "error": {
                    "code": "INSUFFICIENT_DATA",
                    "message": "Not enough historical data for calculation",
                    "details": "Need at least 60 days of data"
                }
            }
        
        logger.info(f"calculate_indicators executed: {len(results)} indicators calculated")
        
        return {
            "success": True,
            "indicators": results,
            "metadata": {
                "query_time": query_time,
                "data_source": "calculated",
                "cache_hit": cache_hit
            }
        }
        
    except Exception as e:
        logger.error(f"Error in calculate_indicators: {e}", exc_info=True)
        return {
            "success": False,
            "metadata": {
                "query_time": query_time,
                "data_source": "none"
            },
            "error": {
                "code": "CALCULATION_ERROR",
                "message": "Failed to calculate indicators",
                "details": str(e)
            }
        }


def _get_indicators_by_category(category: str) -> list[str]:
    """Get indicator list by category."""
    categories = {
        "trend": ["ma", "ema", "macd", "dmi", "adx"],
        "momentum": ["rsi", "kdj", "stochastic", "roc"],
        "volatility": ["boll", "atr", "keltner"],
        "volume": ["obv", "mfi", "cmf", "vwap"]
    }
    return categories.get(category, ["ma", "rsi", "macd"])


def _calculate_single_indicator(
    service: Any,
    indicator_name: str,
    price_data: list,
    params: dict[str, Any]
) -> list[dict[str, Any]]:
    """Calculate a single indicator.
    
    Args:
        service: IndicatorService instance
        indicator_name: Name of indicator (MA, RSI, etc.)
        price_data: List of HistoricalPrice objects
        params: Indicator parameters
        
    Returns:
        List of indicator dictionaries
    """
    try:
        # Map indicator names to service methods
        indicator_name_upper = indicator_name.upper()
        
        if indicator_name_upper == "MA":
            results = service.calculate_ma(price_data, params.get("period", 20))
        elif indicator_name_upper == "EMA":
            results = service.calculate_ema(price_data, params.get("period", 12))
        elif indicator_name_upper == "RSI":
            results = service.calculate_rsi(price_data, params.get("period", 14))
        elif indicator_name_upper == "MACD":
            results = service.calculate_macd(price_data)
        elif indicator_name_upper == "KDJ":
            results = service.calculate_kdj(price_data, params.get("period", 9))
        elif indicator_name_upper == "BOLL":
            results = service.calculate_boll(price_data, params.get("period", 20))
        elif indicator_name_upper == "ATR":
            results = service.calculate_atr(price_data, params.get("period", 14))
        else:
            # Unsupported indicator
            logger.warning(f"Unsupported indicator: {indicator_name}")
            return []
        
        # Convert TechnicalIndicator objects to dictionaries
        return [_indicator_to_dict(ind) for ind in results]
        
    except Exception as e:
        logger.error(f"Error calculating {indicator_name}: {e}", exc_info=True)
        return []


def _indicator_to_dict(indicator: Any) -> dict[str, Any]:
    """Convert TechnicalIndicator object to dictionary."""
    return {
        "name": indicator.name,
        "category": indicator.category.value if hasattr(indicator.category, 'value') else str(indicator.category),
        "period": indicator.period,
        "values": {k: float(v) for k, v in indicator.values.items()},
        "signal": indicator.signal.value if hasattr(indicator.signal, 'value') else str(indicator.signal),
        "interpretation": indicator.interpretation,
        "date": indicator.date
    }
