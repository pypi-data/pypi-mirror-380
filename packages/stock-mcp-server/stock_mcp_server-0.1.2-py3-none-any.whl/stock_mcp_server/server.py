"""MCP server entry point for Stock MCP Server."""

import asyncio
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, Resource
from loguru import logger

from stock_mcp_server.config import get_config
from stock_mcp_server.resources import list_resources, read_resource
from stock_mcp_server.tools import (
    get_market_data,
    calculate_indicators,
    get_money_flow,
    get_sentiment_analysis,
    get_news,
    get_sector_data,
    get_macro_data,
    get_special_data,
    generate_advice,
    get_market_overview,
)
from stock_mcp_server.utils.logger import setup_logging


def create_server() -> Server:
    """Create and configure the MCP server.
    
    Returns:
        Server: Configured MCP server with all tools and resources.
    """
    config = get_config()
    
    # Create server with metadata
    server = Server(
        name=config.server_name,
    )

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        """List available MCP tools."""
        return [
            Tool(
                name="get_market_data",
                description="获取市场数据（实时行情/历史数据/市场宽度/估值指标/成交分布）",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "data_type": {
                            "type": "string",
                            "enum": ["realtime", "history", "breadth", "valuation", "turnover", "all"],
                            "description": "数据类型：realtime(实时行情), history(历史数据), breadth(市场宽度), valuation(估值指标), turnover(成交分布), all(全部)",
                            "default": "realtime",
                        },
                        "index_code": {
                            "type": "string",
                            "description": "指数代码，默认 000001（上证指数）",
                            "default": "000001",
                        },
                        "date": {
                            "type": "string",
                            "description": "交易日期（YYYY-MM-DD格式），可选，默认最新交易日",
                        },
                        "period": {
                            "type": "string",
                            "description": "K线周期（仅history类型）：1min/5min/15min/30min/60min/1day/1week/1month",
                        },
                        "adjust": {
                            "type": "string",
                            "enum": ["none", "qfq", "hfq"],
                            "description": "复权方式（仅history类型）：none(不复权), qfq(前复权), hfq(后复权)",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "开始日期（YYYY-MM-DD格式，仅history类型）",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "结束日期（YYYY-MM-DD格式，仅history类型）",
                        },
                    },
                },
            ),
            Tool(
                name="calculate_indicators",
                description="计算技术指标（MA/RSI/MACD/KDJ/BOLL等50+指标）",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "indicators": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "指标列表：ma, ema, rsi, macd, kdj, boll, atr, obv, cci等",
                        },
                        "category": {
                            "type": "string",
                            "enum": ["trend", "momentum", "volatility", "volume", "all"],
                            "description": "指标类型：trend(趋势), momentum(动量), volatility(波动), volume(成交量), all(全部)",
                        },
                        "params": {
                            "type": "object",
                            "description": "指标参数（如周期、敏感度等）",
                        },
                        "period": {
                            "type": "string",
                            "enum": ["d", "w", "m"],
                            "description": "计算周期：d(日), w(周), m(月)",
                            "default": "d",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "开始日期（YYYY-MM-DD格式）",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "结束日期（YYYY-MM-DD格式）",
                        },
                    },
                },
            ),
            Tool(
                name="get_money_flow",
                description="获取资金流向数据（北向资金/融资融券/主力资金）",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "查询日期（YYYY-MM-DD格式），可选",
                        },
                        "flow_type": {
                            "type": "string",
                            "enum": ["north", "margin", "main", "all"],
                            "description": "资金类型：north(北向资金), margin(融资融券), main(主力资金), all(全部)",
                            "default": "all",
                        },
                    },
                },
            ),
            Tool(
                name="get_sentiment_analysis",
                description="获取市场情绪分析（综合情绪指数/成分得分/趋势分析）",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "分析日期（YYYY-MM-DD格式），可选",
                        },
                        "dimension": {
                            "type": "string",
                            "enum": ["all", "volume", "price", "volatility", "capital", "news"],
                            "description": "情绪维度：all(全部), volume(成交量), price(价格), volatility(波动), capital(资金), news(消息)",
                            "default": "all",
                        },
                        "days": {
                            "type": "integer",
                            "description": "历史趋势周期（天数），默认30",
                            "default": 30,
                        },
                        "include_trend": {
                            "type": "boolean",
                            "description": "是否包含趋势分析",
                            "default": True,
                        },
                    },
                },
            ),
            Tool(
                name="get_news",
                description="获取财经新闻并进行情绪分析（东方财富/新浪财经/证券时报等）",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "limit": {
                            "type": "integer",
                            "description": "返回新闻数量，默认10",
                            "default": 10,
                        },
                        "category": {
                            "type": "string",
                            "enum": ["policy", "market", "company", "industry", "international", "all"],
                            "description": "新闻类型：policy(政策), market(市场), company(公司), industry(行业), international(国际), all(全部)",
                            "default": "all",
                        },
                        "importance": {
                            "type": "number",
                            "description": "最低重要性评分（0-10），默认0",
                            "default": 0,
                        },
                        "include_sentiment": {
                            "type": "boolean",
                            "description": "是否包含情绪分析",
                            "default": True,
                        },
                        "include_hot_topics": {
                            "type": "boolean",
                            "description": "是否包含热点话题汇总",
                            "default": True,
                        },
                        "sentiment_method": {
                            "type": "string",
                            "enum": ["snownlp", "llm"],
                            "description": "情绪分析方法：snownlp(快速), llm(准确但慢)",
                            "default": "snownlp",
                        },
                    },
                },
            ),
            Tool(
                name="get_sector_data",
                description="获取板块数据（行业板块/概念板块/地域板块/风格板块）",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "sector_type": {
                            "type": "string",
                            "enum": ["industry", "concept", "region", "style", "all"],
                            "description": "板块类型：industry(行业), concept(概念), region(地域), style(风格), all(全部)",
                            "default": "industry",
                        },
                        "sort_by": {
                            "type": "string",
                            "enum": ["change", "turnover", "money_flow"],
                            "description": "排序方式：change(涨跌幅), turnover(成交额), money_flow(资金流向)",
                            "default": "change",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "返回板块数量",
                            "default": 10,
                        },
                        "include_rotation": {
                            "type": "boolean",
                            "description": "是否包含板块轮动分析",
                            "default": False,
                        },
                        "include_leaders": {
                            "type": "boolean",
                            "description": "是否包含龙头股信息",
                            "default": True,
                        },
                        "rotation_days": {
                            "type": "integer",
                            "description": "板块轮动分析周期（天数），默认30",
                            "default": 30,
                        },
                    },
                },
            ),
            Tool(
                name="get_macro_data",
                description="获取宏观经济数据（GDP/CPI/PMI/M2等国内外宏观指标）",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "data_type": {
                            "type": "string",
                            "enum": ["macro", "global", "all"],
                            "description": "数据类型：macro(国内宏观), global(全球市场), all(全部)",
                            "default": "macro",
                        },
                        "indicators": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "指标列表：gdp, cpi, pmi, m2等",
                        },
                        "markets": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "市场列表（仅global类型）：us_stock, commodity, forex等",
                        },
                        "period": {
                            "type": "string",
                            "enum": ["monthly", "quarterly", "yearly"],
                            "description": "数据周期：monthly(月度), quarterly(季度), yearly(年度)",
                        },
                        "include_impact": {
                            "type": "boolean",
                            "description": "是否包含对A股的影响分析",
                            "default": False,
                        },
                    },
                },
            ),
            Tool(
                name="get_special_data",
                description="获取特色数据（龙虎榜/大宗交易/解禁/新股/期货期权等）",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "data_type": {
                            "type": "string",
                            "enum": ["longhu", "block_trade", "unlock", "new_stock", "futures", "options", "convertible_bond"],
                            "description": "数据类型：longhu(龙虎榜), block_trade(大宗交易), unlock(解禁), new_stock(新股), futures(期货), options(期权), convertible_bond(可转债)",
                        },
                        "contract": {
                            "type": "string",
                            "description": "期货合约代码（仅futures类型）：IH, IF, IC, IM",
                        },
                        "underlying": {
                            "type": "string",
                            "description": "期权标的（仅options类型）：50ETF, 300ETF",
                        },
                        "sort_by": {
                            "type": "string",
                            "description": "排序方式",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "返回数量",
                            "default": 10,
                        },
                    },
                    "required": ["data_type"],
                },
            ),
            Tool(
                name="generate_advice",
                description="生成投资建议（基于多维度分析的综合投资建议）",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "analysis_depth": {
                            "type": "string",
                            "enum": ["simple", "normal", "detailed"],
                            "description": "分析深度：simple(简单), normal(标准), detailed(详细)",
                            "default": "normal",
                        },
                        "focus_area": {
                            "type": "string",
                            "enum": ["technical", "fundamental", "sentiment", "capital", "news", "all"],
                            "description": "关注领域：technical(技术), fundamental(基本面), sentiment(情绪), capital(资金), news(消息), all(全部)",
                            "default": "all",
                        },
                        "date": {
                            "type": "string",
                            "description": "分析日期（YYYY-MM-DD格式），可选",
                        },
                        "include_risk": {
                            "type": "boolean",
                            "description": "是否包含风险评估",
                            "default": True,
                        },
                        "include_backtest": {
                            "type": "boolean",
                            "description": "是否包含策略回测",
                            "default": False,
                        },
                        "strategy_params": {
                            "type": "object",
                            "description": "回测策略参数",
                        },
                    },
                },
            ),
            Tool(
                name="get_market_overview",
                description="获取市场全景（综合所有数据的市场快照）",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "查询日期（YYYY-MM-DD格式），可选",
                        },
                        "include_details": {
                            "type": "boolean",
                            "description": "是否包含详细数据",
                            "default": False,
                        },
                    },
                },
            ),
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: Any) -> list[TextContent]:
        """Handle tool calls."""
        try:
            logger.info(f"Tool called: {name} with arguments: {arguments}")

            # Route to appropriate tool handler
            tool_map = {
                "get_market_data": get_market_data,
                "calculate_indicators": calculate_indicators,
                "get_money_flow": get_money_flow,
                "get_sentiment_analysis": get_sentiment_analysis,
                "get_news": get_news,
                "get_sector_data": get_sector_data,
                "get_macro_data": get_macro_data,
                "get_special_data": get_special_data,
                "generate_advice": generate_advice,
                "get_market_overview": get_market_overview,
            }

            if name in tool_map:
                # Unpack arguments dictionary as keyword arguments
                result = tool_map[name](**arguments) if isinstance(arguments, dict) else tool_map[name](arguments)
                import json
                return [TextContent(type="text", text=json.dumps(result, ensure_ascii=False, indent=2))]

            return [
                TextContent(
                    type="text",
                    text=f"Unknown tool: {name}",
                )
            ]

        except Exception as e:
            logger.error(f"Error executing tool {name}: {e}", exc_info=True)
            import json
            error_response = {
                "success": False,
                "error": {
                    "code": "TOOL_EXECUTION_ERROR",
                    "message": str(e),
                    "tool": name,
                }
            }
            return [
                TextContent(
                    type="text",
                    text=json.dumps(error_response, ensure_ascii=False, indent=2),
                )
            ]

    @server.list_resources()
    async def handle_list_resources() -> list[Resource]:
        """List available MCP resources."""
        resources_list = list_resources()
        return [
            Resource(
                uri=res["uri"],
                name=res["name"],
                description=res["description"],
                mimeType=res["mimeType"],
            )
            for res in resources_list
        ]

    @server.read_resource()
    async def handle_read_resource(uri: Any) -> str:
        """Read a resource by URI."""
        try:
            from urllib.parse import unquote
            # Convert URI to string if it's an AnyUrl object
            uri_str = str(uri) if not isinstance(uri, str) else uri
            # URL decode the URI (e.g., %7Bdate%7D -> {date})
            decoded_uri = unquote(uri_str)
            logger.info(f"Reading resource: {decoded_uri}")
            result = read_resource(decoded_uri)
            
            # Ensure all values are JSON serializable
            import json
            from decimal import Decimal
            
            def serialize_value(obj):
                """Convert non-JSON-serializable objects to serializable forms."""
                if isinstance(obj, Decimal):
                    return float(obj)
                elif isinstance(obj, dict):
                    return {k: serialize_value(v) for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [serialize_value(item) for item in obj]
                else:
                    return obj
            
            serialized_result = serialize_value(result)
            return json.dumps(serialized_result, ensure_ascii=False, indent=2)
            
        except Exception as e:
            logger.error(f"Error reading resource {uri}: {e}")
            import json
            return json.dumps({
                "error": {
                    "code": "RESOURCE_ERROR",
                    "message": str(e),
                }
            }, ensure_ascii=False)

    logger.info(f"MCP server '{config.server_name}' created with 10 tools and 10 resources")
    return server


async def run_server() -> None:
    """Run the MCP server with stdio transport.
    
    Handles server startup, initialization, and graceful shutdown.
    """
    # Setup logging
    setup_logging()
    config = get_config()
    
    logger.info("=" * 60)
    logger.info("Stock MCP Server - Starting")
    logger.info("=" * 60)
    logger.info(f"Server Name: {config.server_name}")
    logger.info(f"Version: 0.0.5")
    logger.info(f"Transport: stdio")
    logger.info(f"Cache DB: {config.cache_db_path}")
    logger.info("=" * 60)

    try:
        # Initialize cache and database
        from stock_mcp_server.services.cache_service import CacheService
        cache = CacheService()
        logger.info(f"✓ Cache initialized: {config.cache_db_path}")
        logger.info(f"  - In-memory cache size: {config.cache.in_memory_max_items} items")
        logger.info(f"  - Database backend: SQLite")
        
        # Create server
        server = create_server()
        logger.info("✓ Server initialized successfully")
        logger.info(f"  - Tools registered: 10")
        logger.info(f"  - Resources registered: 10")
        
        # Run with stdio transport
        async with stdio_server() as (read_stream, write_stream):
            logger.info("Server running - waiting for requests")
            await server.run(
                read_stream, 
                write_stream, 
                server.create_initialization_options()
            )
            
    except Exception as e:
        logger.error(f"Fatal server error: {e}", exc_info=True)
        raise
    finally:
        logger.info("Server shutting down...")
        logger.info("Cleanup completed")


def main() -> None:
    """Main entry point for the MCP server.
    
    Handles server lifecycle, including startup, execution, and graceful shutdown.
    """
    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        logger.info("Server stopped by user (Ctrl+C)")
    except Exception as e:
        logger.error(f"Unexpected server error: {e}", exc_info=True)
        raise
    finally:
        logger.info("Stock MCP Server terminated")


if __name__ == "__main__":
    main()
