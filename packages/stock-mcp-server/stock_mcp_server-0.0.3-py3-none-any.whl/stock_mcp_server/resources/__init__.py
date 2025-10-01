"""MCP Resources for Stock MCP Server.

This module provides read-only resource endpoints via URI access pattern.
Resources are pre-aggregated, cached data optimized for direct fetching.
"""

from stock_mcp_server.resources.market_resources import (
    get_daily_briefing,
    get_macro_calendar,
    get_market_indicators,
    get_market_summary,
    get_money_flow_report,
    get_news_digest,
    get_risk_report,
    get_sector_heatmap,
    get_sentiment_report,
    get_technical_analysis,
    list_resources,
    read_resource,
)

__all__ = [
    "list_resources",
    "read_resource",
    "get_market_summary",
    "get_technical_analysis",
    "get_sentiment_report",
    "get_daily_briefing",
    "get_news_digest",
    "get_money_flow_report",
    "get_sector_heatmap",
    "get_market_indicators",
    "get_risk_report",
    "get_macro_calendar",
]
