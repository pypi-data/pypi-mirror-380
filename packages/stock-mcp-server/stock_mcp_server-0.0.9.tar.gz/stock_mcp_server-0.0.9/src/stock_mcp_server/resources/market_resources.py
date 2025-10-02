"""MCP Resource implementations for market data.

This module implements all 10 MCP resources as read-only data endpoints.
Resources are accessed via URIs (e.g., market://summary/latest) and return
pre-aggregated, cached data optimized for quick retrieval.
"""

import re
from datetime import datetime
from typing import Any
from urllib.parse import parse_qs, urlparse

from loguru import logger

from stock_mcp_server.services.akshare_service import AKShareService
from stock_mcp_server.services.cache_service import CacheService
from stock_mcp_server.services.indicator_service import IndicatorService
from stock_mcp_server.services.news_service import NewsService
from stock_mcp_server.services.sentiment_service import SentimentService
from stock_mcp_server.tools.advice import generate_advice
from stock_mcp_server.tools.indicators import calculate_indicators
from stock_mcp_server.tools.market_data import get_market_data
from stock_mcp_server.tools.money_flow import get_money_flow
from stock_mcp_server.tools.news import get_news
from stock_mcp_server.tools.sector import get_sector_data
from stock_mcp_server.tools.sentiment import get_sentiment_analysis
from stock_mcp_server.utils.date_utils import get_latest_trading_date, parse_date


# Initialize services (singleton pattern)
_akshare_service = AKShareService()
_cache_service = CacheService()
_indicator_service = IndicatorService()
_news_service = NewsService()
_sentiment_service = SentimentService()


def list_resources() -> list[dict[str, Any]]:
    """List all available MCP resources.
    
    Returns:
        List of resource definitions with URI templates and descriptions
    """
    return [
        {
            "uri": "market://summary/{date}",
            "name": "market-summary",
            "description": "Market summary with index quotes, breadth, and key statistics",
            "mimeType": "application/json",
        },
        {
            "uri": "market://analysis/technical/{date}",
            "name": "technical-analysis",
            "description": "Technical analysis report with indicators and signals",
            "mimeType": "application/json",
        },
        {
            "uri": "market://sentiment/{date}",
            "name": "sentiment-report",
            "description": "Market sentiment analysis report",
            "mimeType": "application/json",
        },
        {
            "uri": "market://briefing/{date}",
            "name": "daily-briefing",
            "description": "Comprehensive daily market briefing",
            "mimeType": "application/json",
        },
        {
            "uri": "market://news/{date}",
            "name": "news-digest",
            "description": "Curated news digest with sentiment analysis",
            "mimeType": "application/json",
        },
        {
            "uri": "market://moneyflow/{date}",
            "name": "money-flow-report",
            "description": "Capital flow analysis report",
            "mimeType": "application/json",
        },
        {
            "uri": "market://sectors/heatmap/{date}",
            "name": "sector-heatmap",
            "description": "Sector performance heatmap data",
            "mimeType": "application/json",
        },
        {
            "uri": "market://indicators/all/{date}",
            "name": "market-indicators",
            "description": "All market indicators aggregated",
            "mimeType": "application/json",
        },
        {
            "uri": "market://risk/{date}",
            "name": "risk-report",
            "description": "Market risk assessment report",
            "mimeType": "application/json",
        },
        {
            "uri": "market://macro/calendar",
            "name": "macro-calendar",
            "description": "Economic calendar with upcoming data releases",
            "mimeType": "application/json",
        },
    ]


def read_resource(uri: str) -> dict[str, Any]:
    """Read a resource by URI.
    
    Args:
        uri: Resource URI (e.g., "market://summary/latest")
        
    Returns:
        Resource data with metadata
        
    Raises:
        ValueError: If URI is invalid or resource not found
    """
    try:
        # Ensure uri is a string (convert from AnyUrl if needed)
        uri_str = str(uri) if not isinstance(uri, str) else uri
        logger.info(f"Reading resource: {uri_str}")
        
        # Parse URI
        parsed = urlparse(uri_str)
        # Combine netloc and path, remove leading slash
        if parsed.netloc:
            path = (parsed.netloc + parsed.path).lstrip('/')
        else:
            path = parsed.path.lstrip('/')
        query_params = parse_qs(parsed.query)
        
        logger.debug(f"Parsed URI - scheme: {parsed.scheme}, netloc: {parsed.netloc}, path: {parsed.path}, combined: {path}")
        
        # Route to appropriate resource handler
        if path.startswith("summary/"):
            date_param = path.split("/")[1]
            return get_market_summary(date_param, query_params)
            
        elif path.startswith("analysis/technical/"):
            date_param = path.split("/")[2]
            return get_technical_analysis(date_param, query_params)
            
        elif path.startswith("sentiment/"):
            date_param = path.split("/")[1]
            return get_sentiment_report(date_param, query_params)
            
        elif path.startswith("briefing/"):
            date_param = path.split("/")[1]
            return get_daily_briefing(date_param, query_params)
            
        elif path.startswith("news/"):
            date_param = path.split("/")[1]
            return get_news_digest(date_param, query_params)
            
        elif path.startswith("moneyflow/"):
            date_param = path.split("/")[1]
            return get_money_flow_report(date_param, query_params)
            
        elif path.startswith("sectors/heatmap/"):
            date_param = path.split("/")[2]
            return get_sector_heatmap(date_param, query_params)
            
        elif path.startswith("indicators/all/"):
            date_param = path.split("/")[2]
            return get_market_indicators(date_param, query_params)
            
        elif path.startswith("risk/"):
            date_param = path.split("/")[1]
            return get_risk_report(date_param, query_params)
            
        elif path.startswith("macro/calendar"):
            return get_macro_calendar(query_params)
            
        else:
            raise ValueError(f"Unknown resource URI: {uri_str}")
            
    except Exception as e:
        # Use uri_str if available, otherwise convert uri to string
        uri_display = uri_str if 'uri_str' in locals() else str(uri)
        logger.error(f"Error reading resource {uri_display}: {e}")
        return {
            "uri": uri_display,
            "error": {
                "code": "RESOURCE_ERROR",
                "message": str(e),
                "details": f"Failed to read resource: {uri_display}",
            },
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "data_source": "error",
                "cache_age_seconds": None,
            },
        }


def _resolve_date(date_param: str) -> str:
    """Resolve date parameter to actual date.
    
    Args:
        date_param: Date parameter (latest/today/YYYY-MM-DD)
        
    Returns:
        Resolved date in YYYY-MM-DD format
    """
    if date_param in ("latest", "today"):
        return get_latest_trading_date()
    
    # Validate date format
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_param):
        raise ValueError(f"Invalid date format: {date_param}")
    
    return date_param


def _get_query_param(params: dict[str, list[str]], key: str, default: Any = None) -> Any:
    """Get query parameter value.
    
    Args:
        params: Query parameters dict
        key: Parameter key
        default: Default value if not found
        
    Returns:
        Parameter value or default
    """
    if key in params and params[key]:
        value = params[key][0]
        # Convert boolean strings
        if value.lower() in ("true", "false"):
            return value.lower() == "true"
        return value
    return default


# Resource 1: Market Summary
def get_market_summary(date_param: str, query_params: dict[str, list[str]]) -> dict[str, Any]:
    """Get market summary resource.
    
    URI: market://summary/{date}
    Query params: include_breadth, include_valuation
    
    Args:
        date_param: Date parameter (latest/YYYY-MM-DD)
        query_params: Query parameters
        
    Returns:
        Market summary data
    """
    try:
        date = _resolve_date(date_param)
        include_breadth = _get_query_param(query_params, "include_breadth", True)
        include_valuation = _get_query_param(query_params, "include_valuation", False)
        
        # Get market data
        market_data = get_market_data({
            "data_type": "all",
            "index_code": "000001",
            "date": date,
        })
        
        # Build response
        response = {
            "uri": f"market://summary/{date}",
            "date": date,
            "index": market_data.get("realtime", {}),
            "breadth": market_data.get("breadth", {}) if include_breadth else None,
            "valuation": market_data.get("valuation", {}) if include_valuation else None,
            "summary_text": _generate_summary_text(market_data, date),
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "data_source": "akshare",
                "cache_age_seconds": 300,
            },
        }
        
        return response
        
    except Exception as e:
        logger.error(f"Error generating market summary: {e}")
        raise


def _generate_summary_text(market_data: dict, date: str) -> str:
    """Generate Chinese summary text."""
    index = market_data.get("realtime", {})
    breadth = market_data.get("breadth", {})
    
    close = index.get("close", 0)
    change_pct = index.get("change_pct", 0)
    amount = index.get("amount", 0) / 100000000  # Convert to billions
    
    direction = "上涨" if change_pct > 0 else "下跌"
    adv = breadth.get("advancing", 0)
    dec = breadth.get("declining", 0)
    adv_pct = breadth.get("advance_pct", 0)
    dec_pct = breadth.get("decline_pct", 0)
    limit_up = breadth.get("limit_up", 0)
    
    summary = (
        f"{date}，上证指数收于{close:.2f}点，{direction}{abs(change_pct):.2f}%。"
        f"市场{'活跃' if adv > dec else '偏弱'}，涨跌家数比{adv_pct:.0f}:{dec_pct:.0f}，"
        f"涨停{limit_up}家。成交额{amount:.0f}亿元。"
    )
    
    return summary


# Resource 2: Technical Analysis
def get_technical_analysis(date_param: str, query_params: dict[str, list[str]]) -> dict[str, Any]:
    """Get technical analysis resource.
    
    URI: market://analysis/technical/{date}
    
    Args:
        date_param: Date parameter
        query_params: Query parameters
        
    Returns:
        Technical analysis report
    """
    try:
        date = _resolve_date(date_param)
        
        # Calculate indicators
        indicators_data = calculate_indicators({
            "symbol": "000001",
            "indicators": ["MA", "MACD", "RSI", "KDJ", "BOLL"],
            "date": date,
        })
        
        response = {
            "uri": f"market://analysis/technical/{date}",
            "date": date,
            "indicators": indicators_data.get("indicators", []),
            "overall_signal": indicators_data.get("overall_signal", "NEUTRAL"),
            "support_levels": _calculate_support_levels(indicators_data),
            "resistance_levels": _calculate_resistance_levels(indicators_data),
            "trend_analysis": _generate_trend_analysis(indicators_data),
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "data_source": "calculated",
                "cache_age_seconds": 1800,
            },
        }
        
        return response
        
    except Exception as e:
        logger.error(f"Error generating technical analysis: {e}")
        raise


def _calculate_support_levels(indicators_data: dict) -> list[float]:
    """Calculate support levels from indicators."""
    # Simplified: use MA values as support
    levels = []
    for indicator in indicators_data.get("indicators", []):
        if indicator.get("name") == "MA":
            values = indicator.get("values", {})
            levels.extend([
                float(values.get("ma20", 0)),
                float(values.get("ma60", 0)),
            ])
    return sorted(set(levels))[:3]  # Top 3 support levels


def _calculate_resistance_levels(indicators_data: dict) -> list[float]:
    """Calculate resistance levels from indicators."""
    # Simplified: use Bollinger upper band
    levels = []
    for indicator in indicators_data.get("indicators", []):
        if indicator.get("name") == "BOLL":
            values = indicator.get("values", {})
            levels.append(float(values.get("upper", 0)))
    return sorted(set(levels), reverse=True)[:3]


def _generate_trend_analysis(indicators_data: dict) -> str:
    """Generate trend analysis text."""
    signals = [ind.get("signal", "NEUTRAL") for ind in indicators_data.get("indicators", [])]
    buy_count = signals.count("BUY") + signals.count("STRONG_BUY")
    sell_count = signals.count("SELL") + signals.count("STRONG_SELL")
    
    if buy_count > sell_count:
        return "技术面偏多，多数指标显示买入信号"
    elif sell_count > buy_count:
        return "技术面偏空，多数指标显示卖出信号"
    else:
        return "技术面中性，多空力量均衡"


# Resource 3: Sentiment Report
def get_sentiment_report(date_param: str, query_params: dict[str, list[str]]) -> dict[str, Any]:
    """Get sentiment report resource.
    
    URI: market://sentiment/{date}
    
    Args:
        date_param: Date parameter
        query_params: Query parameters
        
    Returns:
        Sentiment analysis report
    """
    try:
        date = _resolve_date(date_param)
        
        # Get sentiment analysis
        sentiment_data = get_sentiment_analysis({"date": date})
        
        response = {
            "uri": f"market://sentiment/{date}",
            "date": date,
            "sentiment_index": sentiment_data.get("sentiment_index", 50.0),
            "sentiment_level": sentiment_data.get("sentiment_level", "neutral"),
            "components": sentiment_data.get("components", {}),
            "trend": sentiment_data.get("trend", "stable"),
            "interpretation": sentiment_data.get("interpretation", ""),
            "risk_level": sentiment_data.get("risk_level", "medium"),
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "data_source": "calculated",
                "cache_age_seconds": 3600,
            },
        }
        
        return response
        
    except Exception as e:
        logger.error(f"Error generating sentiment report: {e}")
        raise


# Resource 4: Daily Briefing
def get_daily_briefing(date_param: str, query_params: dict[str, list[str]]) -> dict[str, Any]:
    """Get daily briefing resource.
    
    URI: market://briefing/{date}
    
    Args:
        date_param: Date parameter
        query_params: Query parameters
        
    Returns:
        Daily market briefing
    """
    try:
        date = _resolve_date(date_param)
        
        # Aggregate data from multiple sources
        market_data = get_market_data({"data_type": "all", "date": date})
        news_data = get_news({"limit": 5, "date": date})
        sentiment_data = get_sentiment_analysis({"date": date})
        indicators_data = calculate_indicators({
            "symbol": "000001",
            "indicators": ["MA", "MACD", "RSI"],
            "date": date,
        })
        
        # Generate investment suggestion
        advice_data = generate_advice({"analysis_depth": "simple"})
        
        response = {
            "uri": f"market://briefing/{date}",
            "date": date,
            "market_summary": _generate_summary_text(market_data, date),
            "key_news": news_data.get("news", [])[:5],
            "technical_summary": _generate_trend_analysis(indicators_data),
            "sentiment_overview": sentiment_data.get("interpretation", ""),
            "investment_suggestion": advice_data.get("operational_strategy", ""),
            "tomorrow_outlook": _generate_tomorrow_outlook(market_data, sentiment_data),
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "data_source": "aggregated",
                "cache_age_seconds": 3600,
            },
        }
        
        return response
        
    except Exception as e:
        logger.error(f"Error generating daily briefing: {e}")
        raise


def _generate_tomorrow_outlook(market_data: dict, sentiment_data: dict) -> str:
    """Generate tomorrow's market outlook."""
    sentiment = sentiment_data.get("sentiment_level", "neutral")
    
    if sentiment == "optimistic":
        return "预计明日市场延续强势，关注量能变化"
    elif sentiment == "panic":
        return "市场情绪偏弱，明日关注是否止跌企稳"
    else:
        return "市场处于震荡整理阶段，明日方向尚不明确"


# Resource 5: News Digest
def get_news_digest(date_param: str, query_params: dict[str, list[str]]) -> dict[str, Any]:
    """Get news digest resource.
    
    URI: market://news/{date}
    
    Args:
        date_param: Date parameter
        query_params: Query parameters (category, importance)
        
    Returns:
        News digest with sentiment
    """
    try:
        date = _resolve_date(date_param)
        category = _get_query_param(query_params, "category", None)
        importance = _get_query_param(query_params, "importance", 0)
        
        # Get news
        news_data = get_news({
            "limit": 20,
            "category": category,
            "importance": int(importance) if importance else 0,
            "include_hot_topics": True,
            "date": date,
        })
        
        response = {
            "uri": f"market://news/{date}",
            "date": date,
            "news_list": news_data.get("news", []),
            "overall_sentiment": news_data.get("overall_sentiment", "neutral"),
            "hot_topics": news_data.get("hot_topics", []),
            "market_impact": _assess_news_impact(news_data),
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "data_source": "scraped",
                "cache_age_seconds": 1800,
            },
        }
        
        return response
        
    except Exception as e:
        logger.error(f"Error generating news digest: {e}")
        raise


def _assess_news_impact(news_data: dict) -> str:
    """Assess overall market impact of news."""
    sentiment = news_data.get("overall_sentiment", "neutral")
    
    if sentiment == "positive":
        return "消息面偏利好，对市场有正面提振作用"
    elif sentiment == "negative":
        return "消息面偏利空，市场面临一定压力"
    else:
        return "消息面影响中性，对市场影响有限"


# Resource 6: Money Flow Report
def get_money_flow_report(date_param: str, query_params: dict[str, list[str]]) -> dict[str, Any]:
    """Get money flow report resource.
    
    URI: market://moneyflow/{date}
    
    Args:
        date_param: Date parameter
        query_params: Query parameters
        
    Returns:
        Capital flow analysis
    """
    try:
        date = _resolve_date(date_param)
        
        # Get money flow data
        flow_data = get_money_flow({
            "flow_type": "all",
            "date": date,
        })
        
        response = {
            "uri": f"market://moneyflow/{date}",
            "date": date,
            "north_capital": flow_data.get("north_capital", {}),
            "margin_trading": flow_data.get("margin_trading", {}),
            "main_capital": flow_data.get("main_capital", {}),
            "five_day_trend": _calculate_five_day_trend(flow_data),
            "interpretation": _interpret_capital_flow(flow_data),
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "data_source": "akshare",
                "cache_age_seconds": 1800,
            },
        }
        
        return response
        
    except Exception as e:
        logger.error(f"Error generating money flow report: {e}")
        raise


def _calculate_five_day_trend(flow_data: dict) -> list[dict]:
    """Calculate 5-day capital flow trend."""
    # Simplified: return current day data
    # In real implementation, fetch 5 days of data
    return [
        {
            "date": flow_data.get("date", ""),
            "north_net": flow_data.get("north_capital", {}).get("net", 0),
            "main_net": flow_data.get("main_capital", {}).get("net", 0),
        }
    ]


def _interpret_capital_flow(flow_data: dict) -> str:
    """Interpret capital flow data."""
    north_net = flow_data.get("north_capital", {}).get("net", 0)
    main_net = flow_data.get("main_capital", {}).get("net", 0)
    
    if north_net > 0 and main_net > 0:
        return "北向资金和主力资金同步流入，市场资金面积极"
    elif north_net < 0 and main_net < 0:
        return "北向资金和主力资金同步流出，市场资金面承压"
    else:
        return "资金流向分歧，市场观望情绪浓厚"


# Resource 7: Sector Heatmap
def get_sector_heatmap(date_param: str, query_params: dict[str, list[str]]) -> dict[str, Any]:
    """Get sector heatmap resource.
    
    URI: market://sectors/heatmap/{date}
    
    Args:
        date_param: Date parameter
        query_params: Query parameters (type)
        
    Returns:
        Sector heatmap data
    """
    try:
        date = _resolve_date(date_param)
        sector_type = _get_query_param(query_params, "type", "industry")
        
        # Get sector data
        sector_data = get_sector_data({
            "sector_type": sector_type,
            "sort_by": "change_pct",
            "limit": 50,
            "date": date,
        })
        
        response = {
            "uri": f"market://sectors/heatmap/{date}",
            "date": date,
            "sectors": sector_data.get("sectors", []),
            "heatmap_data": _generate_heatmap_data(sector_data),
            "top_gainers": sector_data.get("sectors", [])[:5],
            "top_losers": sector_data.get("sectors", [])[-5:],
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "data_source": "akshare",
                "cache_age_seconds": 900,
            },
        }
        
        return response
        
    except Exception as e:
        logger.error(f"Error generating sector heatmap: {e}")
        raise


def _generate_heatmap_data(sector_data: dict) -> list[dict]:
    """Generate heatmap visualization data."""
    heatmap = []
    for sector in sector_data.get("sectors", []):
        heatmap.append({
            "name": sector.get("name", ""),
            "value": sector.get("change_pct", 0),
            "color": _get_heatmap_color(sector.get("change_pct", 0)),
        })
    return heatmap


def _get_heatmap_color(change_pct: float) -> str:
    """Get color for heatmap based on change percentage."""
    if change_pct > 2:
        return "dark_red"
    elif change_pct > 0:
        return "red"
    elif change_pct > -2:
        return "green"
    else:
        return "dark_green"


# Resource 8: Market Indicators
def get_market_indicators(date_param: str, query_params: dict[str, list[str]]) -> dict[str, Any]:
    """Get all market indicators resource.
    
    URI: market://indicators/all/{date}
    
    Args:
        date_param: Date parameter
        query_params: Query parameters
        
    Returns:
        All market indicators aggregated
    """
    try:
        date = _resolve_date(date_param)
        
        # Get various indicators
        technical = calculate_indicators({
            "symbol": "000001",
            "indicators": ["MA", "MACD", "RSI", "KDJ", "BOLL"],
            "date": date,
        })
        
        market_data = get_market_data({"data_type": "all", "date": date})
        sentiment = get_sentiment_analysis({"date": date})
        
        response = {
            "uri": f"market://indicators/all/{date}",
            "date": date,
            "technical_indicators": technical.get("indicators", []),
            "breadth_indicators": market_data.get("breadth", {}),
            "sentiment_indicators": sentiment.get("components", {}),
            "valuation_indicators": market_data.get("valuation", {}),
            "composite_signal": _calculate_composite_signal(technical, market_data, sentiment),
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "data_source": "aggregated",
                "cache_age_seconds": 1800,
            },
        }
        
        return response
        
    except Exception as e:
        logger.error(f"Error generating market indicators: {e}")
        raise


def _calculate_composite_signal(technical: dict, market_data: dict, sentiment: dict) -> str:
    """Calculate composite signal from all indicators."""
    # Simplified composite logic
    tech_signal = technical.get("overall_signal", "NEUTRAL")
    breadth = market_data.get("breadth", {})
    sentiment_level = sentiment.get("sentiment_level", "neutral")
    
    advance_pct = breadth.get("advance_pct", 50)
    
    bullish_count = 0
    if tech_signal in ("BUY", "STRONG_BUY"):
        bullish_count += 1
    if advance_pct > 55:
        bullish_count += 1
    if sentiment_level in ("optimistic", "extreme_optimism"):
        bullish_count += 1
    
    if bullish_count >= 2:
        return "BUY"
    elif bullish_count == 0:
        return "SELL"
    else:
        return "NEUTRAL"


# Resource 9: Risk Report
def get_risk_report(date_param: str, query_params: dict[str, list[str]]) -> dict[str, Any]:
    """Get risk assessment report resource.
    
    URI: market://risk/{date}
    
    Args:
        date_param: Date parameter
        query_params: Query parameters
        
    Returns:
        Risk assessment report
    """
    try:
        date = _resolve_date(date_param)
        
        # Get data for risk assessment
        market_data = get_market_data({"data_type": "all", "date": date})
        sentiment = get_sentiment_analysis({"date": date})
        
        risk_level = _assess_risk_level(market_data, sentiment)
        
        response = {
            "uri": f"market://risk/{date}",
            "date": date,
            "risk_level": risk_level,
            "risk_factors": _identify_risk_factors(market_data, sentiment),
            "market_extremes": _detect_market_extremes(market_data),
            "volatility_index": _calculate_volatility_index(market_data),
            "risk_warnings": _generate_risk_warnings(risk_level, market_data),
            "hedging_strategies": _suggest_hedging_strategies(risk_level),
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "data_source": "calculated",
                "cache_age_seconds": 3600,
            },
        }
        
        return response
        
    except Exception as e:
        logger.error(f"Error generating risk report: {e}")
        raise


def _assess_risk_level(market_data: dict, sentiment: dict) -> str:
    """Assess overall market risk level."""
    sentiment_level = sentiment.get("sentiment_level", "neutral")
    breadth = market_data.get("breadth", {})
    
    limit_down = breadth.get("limit_down", 0)
    decline_pct = breadth.get("decline_pct", 50)
    
    if sentiment_level == "extreme_panic" or limit_down > 50:
        return "extreme"
    elif sentiment_level == "panic" or decline_pct > 60:
        return "high"
    elif sentiment_level == "extreme_optimism":
        return "high"  # Overheating risk
    elif decline_pct > 55 or decline_pct < 45:
        return "medium"
    else:
        return "low"


def _identify_risk_factors(market_data: dict, sentiment: dict) -> list[str]:
    """Identify current market risk factors."""
    factors = []
    
    breadth = market_data.get("breadth", {})
    sentiment_index = sentiment.get("sentiment_index", 50)
    
    if breadth.get("decline_pct", 0) > 60:
        factors.append("市场宽度较差，下跌股票占比过高")
    
    if sentiment_index < 30:
        factors.append("市场情绪恐慌，投资者信心不足")
    elif sentiment_index > 80:
        factors.append("市场情绪过热，存在回调风险")
    
    if breadth.get("limit_down", 0) > 30:
        factors.append("跌停股票较多，市场抛压较大")
    
    return factors if factors else ["当前无明显风险因素"]


def _detect_market_extremes(market_data: dict) -> dict[str, Any]:
    """Detect market extremes (panic selling, euphoria)."""
    breadth = market_data.get("breadth", {})
    
    return {
        "panic_selling": breadth.get("limit_down", 0) > 50,
        "euphoria": breadth.get("limit_up", 0) > 100,
        "oversold": breadth.get("decline_pct", 0) > 70,
        "overbought": breadth.get("advance_pct", 0) > 70,
    }


def _calculate_volatility_index(market_data: dict) -> float:
    """Calculate volatility index."""
    index = market_data.get("realtime", {})
    amplitude = abs(index.get("amplitude", 0))
    
    # Simplified VIX-style calculation
    volatility = amplitude * 10  # Scale to 0-100
    
    return min(volatility, 100.0)


def _generate_risk_warnings(risk_level: str, market_data: dict) -> list[str]:
    """Generate risk warnings based on risk level."""
    warnings = []
    
    if risk_level == "extreme":
        warnings.append("⚠️ 市场风险极高，建议空仓观望")
        warnings.append("⚠️ 避免盲目抄底，等待市场企稳信号")
    elif risk_level == "high":
        warnings.append("⚠️ 市场风险较高，控制仓位至30%以下")
        warnings.append("⚠️ 严格止损，避免重仓操作")
    elif risk_level == "medium":
        warnings.append("⚠️ 市场波动加大，建议半仓操作")
    else:
        warnings.append("✓ 市场风险可控，可适当参与")
    
    return warnings


def _suggest_hedging_strategies(risk_level: str) -> list[str]:
    """Suggest hedging strategies based on risk level."""
    if risk_level in ("extreme", "high"):
        return [
            "降低股票仓位至30%以下",
            "增加债券类资产配置",
            "考虑持有现金等待机会",
            "分散投资，避免集中持仓",
        ]
    elif risk_level == "medium":
        return [
            "维持适中仓位（40-60%）",
            "设置止损点位",
            "关注防御性板块（银行、公用事业）",
        ]
    else:
        return [
            "可适当提高仓位至70%",
            "关注成长性板块机会",
            "保持合理风险敞口",
        ]


# Resource 10: Macro Calendar
def get_macro_calendar(query_params: dict[str, list[str]]) -> dict[str, Any]:
    """Get macro economic calendar resource.
    
    URI: market://macro/calendar
    
    Args:
        query_params: Query parameters (start_date, end_date, importance)
        
    Returns:
        Economic calendar data
    """
    try:
        start_date = _get_query_param(query_params, "start_date", None)
        end_date = _get_query_param(query_params, "end_date", None)
        importance = _get_query_param(query_params, "importance", None)
        
        # Get macro calendar data
        # For now, return mock data - real implementation would fetch from data source
        calendar_data = _fetch_macro_calendar(start_date, end_date, importance)
        
        response = {
            "uri": "market://macro/calendar",
            "calendar_range": {
                "start_date": start_date or datetime.now().strftime("%Y-%m-%d"),
                "end_date": end_date or "",
            },
            "upcoming_events": calendar_data.get("events", []),
            "central_bank_meetings": calendar_data.get("cb_meetings", []),
            "policy_announcements": calendar_data.get("policy", []),
            "expected_impacts": calendar_data.get("impacts", []),
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "data_source": "calendar",
                "cache_age_seconds": 86400,
            },
        }
        
        return response
        
    except Exception as e:
        logger.error(f"Error generating macro calendar: {e}")
        raise


def _fetch_macro_calendar(
    start_date: str | None,
    end_date: str | None,
    importance: str | None,
) -> dict[str, Any]:
    """Fetch macro economic calendar data.
    
    This is a placeholder - real implementation would fetch from data source.
    """
    # Mock data for now
    return {
        "events": [
            {
                "date": "2025-10-15",
                "time": "09:30",
                "event": "9月CPI数据发布",
                "importance": "high",
                "expected_value": "102.5%",
                "previous_value": "102.3%",
                "impact": "通胀数据超预期，可能影响货币政策",
            },
            {
                "date": "2025-10-18",
                "event": "三季度GDP数据",
                "importance": "high",
                "expected_value": "5.0%",
                "impact": "关注经济增长动能",
            },
        ],
        "cb_meetings": [
            {
                "date": "2025-10-20",
                "organization": "中国人民银行",
                "event": "第三季度货币政策委员会例会",
                "importance": "high",
            }
        ],
        "policy": [
            {
                "date": "2025-10-10",
                "event": "国常会讨论稳增长政策",
                "importance": "medium",
            }
        ],
        "impacts": [
            "10月中旬关注通胀数据对货币政策影响",
            "GDP数据将影响市场对四季度经济预期",
        ],
    }
