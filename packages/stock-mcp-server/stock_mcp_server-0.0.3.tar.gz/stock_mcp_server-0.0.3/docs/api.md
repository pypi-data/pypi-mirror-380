# Stock MCP Server - API Documentation

**Version**: 0.0.1  
**Protocol**: Model Context Protocol (MCP)  
**Last Updated**: 2025-10-01

[中文文档](../README.md) | [English Documentation](../README_EN.md)

---

## Table of Contents

- [Overview](#overview)
- [MCP Tools (10)](#mcp-tools)
  - [1. get_market_data](#1-get_market_data)
  - [2. calculate_indicators](#2-calculate_indicators)
  - [3. get_money_flow](#3-get_money_flow)
  - [4. get_sentiment_analysis](#4-get_sentiment_analysis)
  - [5. get_news](#5-get_news)
  - [6. get_sector_data](#6-get_sector_data)
  - [7. get_macro_data](#7-get_macro_data)
  - [8. get_special_data](#8-get_special_data)
  - [9. generate_advice](#9-generate_advice)
  - [10. get_market_overview](#10-get_market_overview)
- [MCP Resources (10)](#mcp-resources)
- [Common Response Format](#common-response-format)
- [Error Codes](#error-codes)
- [Data Models](#data-models)

---

## Overview

Stock MCP Server provides **10 MCP tools** and **10 MCP resources** for comprehensive Chinese A-share market analysis. All tools follow a consistent response format with success/error handling, metadata, and structured data output.

### Base URL
- **MCP Protocol**: stdio (standard input/output)
- **Resources URI Scheme**: `market://`

### Authentication
No authentication required. Data sourced from public APIs (AKShare).

### Rate Limiting
- **Real-time data**: 5-minute cache during trading hours
- **Historical data**: 24-hour cache
- **News**: 30-minute cache
- **Concurrent requests**: 10+ supported

---

## MCP Tools

### 1. get_market_data

**Description**: Retrieve comprehensive market data including real-time quotes, historical K-line data, market breadth, valuation metrics, and turnover analysis.

**Input Schema**:

```json
{
  "type": "object",
  "properties": {
    "data_type": {
      "type": "string",
      "enum": ["realtime", "history", "breadth", "valuation", "turnover", "all"],
      "description": "Type of market data to retrieve",
      "default": "realtime"
    },
    "index_code": {
      "type": "string",
      "description": "Index code (e.g., '000001' for Shanghai Composite)",
      "default": "000001"
    },
    "date": {
      "type": "string",
      "description": "Query date in YYYY-MM-DD format (optional)",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
    },
    "period": {
      "type": "string",
      "enum": ["daily", "weekly", "monthly"],
      "description": "K-line timeframe for historical data",
      "default": "daily"
    },
    "adjust": {
      "type": "string",
      "enum": ["qfq", "hfq", "none"],
      "description": "Price adjustment method (qfq=forward, hfq=backward, none=unadjusted)",
      "default": "qfq"
    },
    "start_date": {
      "type": "string",
      "description": "Start date for historical data (YYYY-MM-DD)",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
    },
    "end_date": {
      "type": "string",
      "description": "End date for historical data (YYYY-MM-DD)",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
    }
  },
  "required": []
}
```

**Output Example** (data_type="realtime"):

```json
{
  "success": true,
  "data": {
    "index": {
      "code": "000001",
      "name": "上证指数",
      "current": "3245.67",
      "change": "10.67",
      "change_pct": "0.33",
      "open": "3230.50",
      "high": "3250.00",
      "low": "3228.00",
      "volume": 285000000,
      "amount": "345000000000",
      "turnover": "1.23",
      "amplitude": "0.68",
      "timestamp": "2025-10-01T15:00:00+08:00",
      "trading_date": "2025-10-01",
      "market_status": "closed"
    }
  },
  "metadata": {
    "query_time": "2025-10-01T16:00:00+08:00",
    "data_source": "Tencent Finance",
    "cache_hit": false,
    "data_age_seconds": null
  },
  "error": null
}
```

**Output Example** (data_type="breadth"):

```json
{
  "success": true,
  "data": {
    "breadth": {
      "total_stocks": 5436,
      "advancing": 2800,
      "declining": 2100,
      "unchanged": 536,
      "limit_up": 45,
      "limit_down": 12,
      "gain_over_5pct": 420,
      "loss_over_5pct": 280,
      "gain_over_7pct": 180,
      "loss_over_7pct": 95,
      "advance_decline_ratio": "1.33",
      "advance_pct": "51.51",
      "decline_pct": "38.64",
      "date": "2025-10-01",
      "timestamp": "2025-10-01T15:00:00+08:00"
    }
  },
  "metadata": { ... },
  "error": null
}
```

**Response Time**: <2s (realtime), <3s (historical)

---

### 2. calculate_indicators

**Description**: Calculate 50+ technical indicators across trend, momentum, volatility, and volume categories with trading signals and interpretations.

**Input Schema**:

```json
{
  "type": "object",
  "properties": {
    "index_code": {
      "type": "string",
      "description": "Index code",
      "default": "000001"
    },
    "indicators": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["ma", "ema", "macd", "rsi", "kdj", "boll", "atr", "obv", "mfi", "all"]
      },
      "description": "List of indicators to calculate",
      "default": ["ma", "macd", "rsi", "kdj"]
    },
    "category": {
      "type": "string",
      "enum": ["trend", "momentum", "volatility", "volume", "all"],
      "description": "Filter by indicator category",
      "default": "all"
    },
    "params": {
      "type": "object",
      "description": "Custom indicator parameters",
      "properties": {
        "ma_periods": {
          "type": "array",
          "items": {"type": "integer"},
          "default": [5, 10, 20, 60]
        },
        "rsi_period": {
          "type": "integer",
          "default": 14
        },
        "macd_fast": {
          "type": "integer",
          "default": 12
        },
        "macd_slow": {
          "type": "integer",
          "default": 26
        },
        "macd_signal": {
          "type": "integer",
          "default": 9
        }
      }
    },
    "period": {
      "type": "string",
      "enum": ["d", "w", "m"],
      "description": "Calculation timeframe",
      "default": "d"
    },
    "start_date": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
    },
    "end_date": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
    }
  },
  "required": []
}
```

**Supported Indicators**:

| Category | Indicators |
|----------|------------|
| **Trend** | MA, EMA, MACD, DMI, ADX, TRIX, Aroon, CCI, SAR, Ichimoku Cloud |
| **Momentum** | RSI, KDJ, Stochastic, Williams %R, ROC, Momentum |
| **Volatility** | Bollinger Bands, ATR, Keltner Channels, Donchian Channels |
| **Volume** | OBV, MFI, CMF, VWAP, A/D Line, Volume Profile |

**Output Example**:

```json
{
  "success": true,
  "data": {
    "indicators": [
      {
        "name": "MA",
        "category": "trend",
        "values": {
          "MA5": "3240.50",
          "MA10": "3235.00",
          "MA20": "3230.00",
          "MA60": "3220.00"
        },
        "signal": "BUY",
        "interpretation": "短期均线上穿中期均线，呈多头排列",
        "timestamp": "2025-10-01T15:00:00+08:00"
      },
      {
        "name": "MACD",
        "category": "trend",
        "values": {
          "DIF": "5.23",
          "DEA": "3.45",
          "MACD": "1.78"
        },
        "signal": "BUY",
        "interpretation": "金叉，DIF上穿DEA",
        "timestamp": "2025-10-01T15:00:00+08:00"
      },
      {
        "name": "RSI",
        "category": "momentum",
        "values": {
          "RSI6": "65.5",
          "RSI12": "62.3",
          "RSI24": "58.7"
        },
        "signal": "NEUTRAL",
        "interpretation": "处于正常区间，无超买超卖",
        "timestamp": "2025-10-01T15:00:00+08:00"
      }
    ],
    "overall_signal": "BUY",
    "bullish_count": 7,
    "bearish_count": 1,
    "neutral_count": 2,
    "confidence": "72.5"
  },
  "metadata": { ... },
  "error": null
}
```

**Response Time**: <5s

---

### 3. get_money_flow

**Description**: Track capital flows including northbound capital (Stock Connect), margin trading, and main capital flows by order size.

**Input Schema**:

```json
{
  "type": "object",
  "properties": {
    "date": {
      "type": "string",
      "description": "Query date (YYYY-MM-DD)",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
    },
    "flow_type": {
      "type": "string",
      "enum": ["north", "margin", "main", "all"],
      "description": "Type of capital flow data",
      "default": "all"
    }
  },
  "required": []
}
```

**Output Example**:

```json
{
  "success": true,
  "data": {
    "north_capital": {
      "inflow": "18500000000",
      "outflow": "2500000000",
      "net_flow": "16000000000",
      "holdings": "2850000000000",
      "date": "2025-10-01"
    },
    "margin_trading": {
      "financing_balance": "1850000000000",
      "financing_buy": "125000000000",
      "financing_repay": "122000000000",
      "short_balance": "85000000000",
      "short_sell": "5000000000",
      "short_cover": "4800000000",
      "total_balance": "1935000000000",
      "date": "2025-10-01"
    },
    "main_capital": {
      "super_large_inflow": "45000000000",
      "super_large_outflow": "48000000000",
      "super_large_net": "-3000000000",
      "large_inflow": "38000000000",
      "large_outflow": "47000000000",
      "large_net": "-9000000000",
      "medium_net": "5000000000",
      "small_net": "7000000000",
      "date": "2025-10-01"
    }
  },
  "metadata": { ... },
  "error": null
}
```

**Response Time**: <2s

---

### 4. get_sentiment_analysis

**Description**: Calculate multi-dimensional market sentiment index with component breakdowns and risk assessment.

**Input Schema**:

```json
{
  "type": "object",
  "properties": {
    "date": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
    },
    "dimension": {
      "type": "string",
      "enum": ["all", "volume", "price", "volatility", "capital", "news"],
      "default": "all"
    },
    "days": {
      "type": "integer",
      "description": "Historical trend period",
      "default": 30,
      "minimum": 1,
      "maximum": 365
    },
    "include_trend": {
      "type": "boolean",
      "default": true
    }
  },
  "required": []
}
```

**Output Example**:

```json
{
  "success": true,
  "data": {
    "overall_sentiment": {
      "score": "62.5",
      "level": "OPTIMISTIC",
      "classification": "偏乐观",
      "date": "2025-10-01"
    },
    "components": {
      "volume_sentiment": {
        "score": "70.0",
        "interpretation": "成交活跃，量能充足"
      },
      "price_sentiment": {
        "score": "68.0",
        "interpretation": "涨多跌少，市场偏强"
      },
      "volatility_sentiment": {
        "score": "55.0",
        "interpretation": "波动正常"
      },
      "capital_sentiment": {
        "score": "58.0",
        "interpretation": "资金观望，流入一般"
      },
      "news_sentiment": {
        "score": "65.0",
        "interpretation": "消息面偏正面"
      }
    },
    "trend": {
      "direction": "IMPROVING",
      "change": "4.0",
      "comparison": "较昨日"
    },
    "risk_level": "MEDIUM",
    "interpretation": "市场情绪偏乐观，成交活跃，资金流入积极。技术面呈多头排列，短期可适当参与。但需注意情绪是否过热，建议控制仓位。"
  },
  "metadata": { ... },
  "error": null
}
```

**Sentiment Levels**:
- 0-20: EXTREME_PANIC (极度恐慌)
- 20-40: PANIC (恐慌)
- 40-60: NEUTRAL (中性)
- 60-80: OPTIMISTIC (乐观)
- 80-100: EXTREME_OPTIMISM (极度乐观)

**Response Time**: <3s

---

### 5. get_news

**Description**: Retrieve and analyze financial news from major sources with sentiment scoring and hot topics aggregation.

**Input Schema**:

```json
{
  "type": "object",
  "properties": {
    "limit": {
      "type": "integer",
      "description": "Number of news items to return",
      "default": 10,
      "minimum": 1,
      "maximum": 100
    },
    "category": {
      "type": "string",
      "enum": ["policy", "market", "company", "industry", "international", "all"],
      "default": "all"
    },
    "importance": {
      "type": "number",
      "description": "Minimum importance score (0-10)",
      "default": 0,
      "minimum": 0,
      "maximum": 10
    },
    "include_sentiment": {
      "type": "boolean",
      "default": true
    },
    "include_hot_topics": {
      "type": "boolean",
      "default": true
    },
    "sentiment_method": {
      "type": "string",
      "enum": ["snownlp", "llm"],
      "default": "snownlp"
    }
  },
  "required": []
}
```

**News Sources**:
- 东方财富 (Eastmoney)
- 新浪财经 (Sina Finance)
- 证券时报 (Securities Times)
- 21世纪经济报道 (21st Century Business Herald)

**Output Example**:

```json
{
  "success": true,
  "data": {
    "news": [
      {
        "title": "央行宣布降准0.5个百分点 释放流动性约1.2万亿",
        "summary": "中国人民银行决定于2025年10月15日下调金融机构存款准备金率0.5个百分点...",
        "source": "东方财富",
        "url": "https://...",
        "publish_time": "2025-10-01T16:30:00+08:00",
        "importance": 9.5,
        "sentiment": {
          "score": 0.85,
          "classification": "POSITIVE",
          "label": "正面"
        },
        "impact": {
          "scope": "全市场",
          "time_horizon": "中期",
          "related_sectors": ["银行", "房地产"]
        },
        "tags": ["货币政策", "降准", "流动性"]
      }
    ],
    "overall_sentiment": {
      "positive_pct": 75.0,
      "neutral_pct": 20.0,
      "negative_pct": 5.0,
      "classification": "POSITIVE"
    },
    "hot_topics": [
      {
        "topic": "货币政策",
        "count": 5,
        "avg_sentiment": 0.82
      },
      {
        "topic": "北向资金",
        "count": 3,
        "avg_sentiment": 0.75
      }
    ],
    "total_count": 10,
    "query_date": "2025-10-01"
  },
  "metadata": { ... },
  "error": null
}
```

**Response Time**: <10s

---

### 6. get_sector_data

**Description**: Retrieve sector and industry performance data with capital flows and rotation analysis.

**Input Schema**:

```json
{
  "type": "object",
  "properties": {
    "sector_type": {
      "type": "string",
      "enum": ["industry", "concept", "region", "style", "all"],
      "default": "industry"
    },
    "sort_by": {
      "type": "string",
      "enum": ["change", "turnover", "money_flow"],
      "default": "change"
    },
    "limit": {
      "type": "integer",
      "default": 20,
      "minimum": 1,
      "maximum": 100
    },
    "include_rotation": {
      "type": "boolean",
      "default": true
    },
    "include_leaders": {
      "type": "boolean",
      "description": "Include leading stocks in each sector",
      "default": true
    },
    "rotation_days": {
      "type": "integer",
      "default": 30,
      "minimum": 5,
      "maximum": 120
    }
  },
  "required": []
}
```

**Sector Coverage**:
- **Industry**: 28 SW Level-1 industries (申万一级行业)
- **Concept**: 200+ concept sectors (概念板块)
- **Region**: Province/city sectors (地域板块)
- **Style**: Large/mid/small cap, value/growth (风格板块)

**Output Example**:

```json
{
  "success": true,
  "data": {
    "sectors": [
      {
        "name": "银行",
        "type": "industry",
        "change_pct": "2.35",
        "stock_count": 42,
        "main_capital_flow": "1200000000",
        "turnover": "2.15",
        "leaders": [
          {"code": "601398", "name": "工商银行", "change_pct": "2.80"},
          {"code": "601939", "name": "建设银行", "change_pct": "2.50"}
        ]
      }
    ],
    "rotation_analysis": {
      "from_sectors": ["半导体", "新能源"],
      "to_sectors": ["银行", "房地产"],
      "pattern": "从科技股向金融股轮动",
      "driver": "政策利好推动低估值板块反弹"
    },
    "top_gainers": [...],
    "top_losers": [...]
  },
  "metadata": { ... },
  "error": null
}
```

**Response Time**: <3s

---

### 7. get_macro_data

**Description**: Retrieve macroeconomic indicators and global market data with A-share impact analysis.

**Input Schema**:

```json
{
  "type": "object",
  "properties": {
    "data_type": {
      "type": "string",
      "enum": ["macro", "global", "all"],
      "default": "all"
    },
    "indicators": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["gdp", "cpi", "ppi", "pmi", "m0", "m1", "m2", "all"]
      },
      "default": ["all"]
    },
    "markets": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["us_stock", "commodity", "forex", "all"]
      }
    },
    "period": {
      "type": "string",
      "enum": ["monthly", "quarterly", "yearly"],
      "default": "monthly"
    },
    "include_impact": {
      "type": "boolean",
      "description": "Include A-share impact analysis",
      "default": true
    }
  },
  "required": []
}
```

**Output Example**:

```json
{
  "success": true,
  "data": {
    "macro_indicators": {
      "gdp": {
        "value": "5.2",
        "unit": "%",
        "period": "2025-Q3",
        "yoy_change": "-0.1",
        "impact": "GDP增速略有放缓，但仍在合理区间"
      },
      "cpi": {
        "value": "0.4",
        "unit": "%",
        "period": "2025-09",
        "yoy_change": "-0.2",
        "mom_change": "0.1",
        "impact": "通胀温和，货币政策空间充足"
      },
      "pmi": {
        "manufacturing": "49.8",
        "non_manufacturing": "51.5",
        "period": "2025-09",
        "impact": "制造业略弱，服务业保持扩张"
      }
    },
    "global_markets": {
      "us_indices": {
        "SP500": {"value": "5,650.23", "change_pct": "0.12"},
        "NASDAQ": {"value": "17,850.45", "change_pct": "0.25"}
      },
      "commodities": {
        "crude_oil": {"value": "88.50", "unit": "USD/barrel", "change_pct": "-1.2"},
        "gold": {"value": "2,650.00", "unit": "USD/oz", "change_pct": "0.5"}
      }
    },
    "a_share_impact": "全球市场相对稳定，对A股影响中性偏正面"
  },
  "metadata": { ... },
  "error": null
}
```

**Response Time**: <3s

---

### 8. get_special_data

**Description**: Retrieve special market data including Dragon-Tiger List, block trades, lock-up expirations, IPOs, and derivatives.

**Input Schema**:

```json
{
  "type": "object",
  "properties": {
    "data_type": {
      "type": "string",
      "enum": ["longhu", "block_trade", "unlock", "new_stock", "futures", "options", "convertible_bond"],
      "description": "Type of special data"
    },
    "contract": {
      "type": "string",
      "enum": ["IH", "IF", "IC", "IM"],
      "description": "Futures contract (for futures data)"
    },
    "underlying": {
      "type": "string",
      "enum": ["50ETF", "300ETF"],
      "description": "Option underlying (for options data)"
    },
    "sort_by": {
      "type": "string",
      "description": "Sorting criteria"
    },
    "limit": {
      "type": "integer",
      "default": 20,
      "minimum": 1,
      "maximum": 100
    }
  },
  "required": ["data_type"]
}
```

**Output Example** (longhu):

```json
{
  "success": true,
  "data": {
    "dragon_tiger_list": [
      {
        "stock_code": "600519",
        "stock_name": "贵州茅台",
        "change_pct": "3.25",
        "turnover": "1500000000",
        "buy_seats": [
          {
            "seat_name": "机构专用",
            "buy_amount": "450000000",
            "sell_amount": "0",
            "net_amount": "450000000"
          }
        ],
        "sell_seats": [...],
        "net_institutional": "380000000",
        "net_retail": "-380000000"
      }
    ],
    "date": "2025-10-01"
  },
  "metadata": { ... },
  "error": null
}
```

**Response Time**: <3s

---

### 9. generate_advice

**Description**: Generate comprehensive investment recommendations based on multi-dimensional analysis including technical, fundamental, sentiment, capital flow, and news analysis.

**Input Schema**:

```json
{
  "type": "object",
  "properties": {
    "analysis_depth": {
      "type": "string",
      "enum": ["simple", "normal", "detailed"],
      "default": "normal"
    },
    "focus_area": {
      "type": "string",
      "enum": ["technical", "fundamental", "sentiment", "capital", "news", "all"],
      "default": "all"
    },
    "date": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
    },
    "include_risk": {
      "type": "boolean",
      "default": true
    },
    "include_backtest": {
      "type": "boolean",
      "description": "Include strategy backtest results",
      "default": false
    },
    "strategy_params": {
      "type": "object",
      "description": "Custom backtest parameters",
      "properties": {
        "lookback_days": {"type": "integer", "default": 60},
        "position_size": {"type": "number", "default": 0.5}
      }
    }
  },
  "required": []
}
```

**Output Example**:

```json
{
  "success": true,
  "data": {
    "market_outlook": "BULLISH",
    "operation": "CAUTIOUS",
    "position_recommendation": {
      "level": "HALF",
      "percentage": "40-70",
      "description": "半仓操作"
    },
    "analysis": {
      "technical": {
        "summary": "短期均线多头排列，MACD金叉，RSI处于正常区间",
        "details": "技术面偏多，但需注意短期涨幅较大，可能面临回调"
      },
      "fundamental": {
        "summary": "涨跌家数比2:1，市场宽度良好",
        "details": "成交量放大，市场参与度较高。估值水平合理，PE约15倍"
      },
      "sentiment": {
        "summary": "市场情绪指数62.5，处于偏乐观区间",
        "details": "需注意情绪是否过热，警惕追高风险"
      },
      "capital": {
        "summary": "北向资金净流入16亿，外资态度积极",
        "details": "主力资金小幅流出12亿，观望情绪浓厚。融资余额上升，杠杆资金活跃"
      },
      "news": {
        "summary": "央行降准利好，释放流动性1.2万亿",
        "details": "短期提振市场信心，中期有利于估值修复"
      }
    },
    "risk_assessment": {
      "level": "MEDIUM",
      "factors": [
        "市场情绪偏高，需警惕回调风险",
        "主力资金流出，缺乏持续性支撑",
        "外部环境仍有不确定性"
      ],
      "warning": "市场短期波动可能加大，建议控制仓位，设置止损"
    },
    "actionable_strategy": {
      "focus_points": [
        "关注北向资金动向，持续流入则多头延续",
        "留意主力资金是否回流，资金面是关键",
        "关注量能是否持续放大，缩量上涨不可持续"
      ],
      "operations": [
        "建议半仓操作（40-70%），可逢低适当加仓",
        "重点关注政策受益板块：银行、地产、基建",
        "短线关注强势板块，波段操作控制风险",
        "严格止损，破3200点减仓观望"
      ],
      "entry_levels": ["3200-3220"],
      "exit_levels": ["3280-3300"],
      "stop_loss": "3180"
    },
    "backtest": {
      "enabled": false
    },
    "confidence": "72.5",
    "valid_until": "2025-10-02T09:30:00+08:00",
    "disclaimer": "本建议仅供参考，不构成投资建议。投资有风险，入市需谨慎。"
  },
  "metadata": { ... },
  "error": null
}
```

**Market Outlook Values**:
- `BULLISH`: 看多
- `BEARISH`: 看空
- `SIDEWAYS`: 震荡

**Operation Values**:
- `AGGRESSIVE`: 激进
- `CAUTIOUS`: 谨慎
- `WAIT`: 观望

**Position Levels**:
- `HEAVY`: 重仓 (70-90%)
- `HALF`: 半仓 (40-70%)
- `LIGHT`: 轻仓 (10-40%)
- `EMPTY`: 空仓 (0-10%)

**Response Time**: <5s (normal), <7s (detailed)

---

### 10. get_market_overview

**Description**: Get comprehensive market snapshot combining index quotes, market breadth, capital flows, sentiment, top sectors, and key news.

**Input Schema**:

```json
{
  "type": "object",
  "properties": {
    "date": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
    },
    "include_details": {
      "type": "boolean",
      "description": "Include detailed breakdowns",
      "default": false
    }
  },
  "required": []
}
```

**Output Example**:

```json
{
  "success": true,
  "data": {
    "indices": [
      {"code": "000001", "name": "上证指数", "current": "3245.67", "change_pct": "0.33"},
      {"code": "399001", "name": "深证成指", "current": "10850.23", "change_pct": "0.45"},
      {"code": "399006", "name": "创业板指", "current": "2234.56", "change_pct": "0.28"}
    ],
    "market_breadth": {
      "advancing": 2800,
      "declining": 2100,
      "limit_up": 45,
      "limit_down": 12
    },
    "capital_flows": {
      "north_capital_net": "16000000000",
      "main_capital_net": "-12000000000",
      "margin_balance": "1850000000000"
    },
    "sentiment": {
      "score": "62.5",
      "level": "OPTIMISTIC",
      "trend": "IMPROVING",
      "change": "4.0"
    },
    "top_sectors": {
      "gainers": [
        {"name": "银行", "change_pct": "2.35"},
        {"name": "房地产", "change_pct": "2.10"}
      ],
      "losers": [
        {"name": "医疗器械", "change_pct": "-1.80"},
        {"name": "半导体", "change_pct": "-1.25"}
      ]
    },
    "top_news": [
      {
        "title": "央行宣布降准0.5个百分点",
        "importance": 9.5,
        "sentiment": "POSITIVE"
      }
    ],
    "core_insight": "市场情绪偏乐观，政策利好提振信心。建议半仓操作，关注银行、地产板块。控制风险，逢低参与。",
    "date": "2025-10-01"
  },
  "metadata": { ... },
  "error": null
}
```

**Response Time**: <3s

---

## MCP Resources

Resources are read-only data endpoints accessed via URI. Unlike tools (which are invoked with parameters), resources are fetched directly by URI.

### Resource List

| Resource | URI Pattern | Description |
|----------|-------------|-------------|
| market-summary | `market://summary/{date}` | Market summary with index quotes and breadth |
| technical-analysis | `market://analysis/technical/{date}` | Technical analysis report |
| sentiment-report | `market://sentiment/{date}` | Sentiment analysis report |
| daily-briefing | `market://briefing/{date}` | Comprehensive daily briefing |
| news-digest | `market://news/{date}` | Curated news digest |
| money-flow-report | `market://moneyflow/{date}` | Capital flow analysis |
| sector-heatmap | `market://sectors/heatmap/{date}` | Sector performance heatmap |
| market-indicators | `market://indicators/all/{date}` | All market indicators |
| risk-report | `market://risk/{date}` | Market risk assessment |
| macro-calendar | `market://macro/calendar` | Economic calendar |

### Date Parameter Conventions

All resources with `{date}` parameter support:
- **Specific date**: `2025-09-30` (YYYY-MM-DD)
- **Latest/Today**: `latest` or `today` (resolves to most recent trading day)

### Query Parameters

Resources support optional query parameters:

**market-summary**:
- `?include_breadth=true` - Include detailed market breadth
- `?include_valuation=true` - Include valuation metrics

**news-digest**:
- `?category=policy` - Filter by category
- `?importance=8` - Minimum importance score

**sector-heatmap**:
- `?type=industry` - Sector type

**macro-calendar**:
- `?start_date=2025-10-01` - Calendar start date
- `?end_date=2025-10-31` - Calendar end date
- `?importance=high` - Filter by importance

### Example Resource URIs

```
market://summary/latest
market://summary/2025-10-01?include_valuation=true
market://analysis/technical/today
market://sentiment/latest
market://briefing/2025-10-01
market://news/today?category=policy&importance=8
market://moneyflow/2025-10-01
market://sectors/heatmap/latest?type=industry
market://indicators/all/2025-10-01
market://risk/latest
market://macro/calendar?start_date=2025-10-01&importance=high
```

---

## Common Response Format

All tools return responses in this standardized format:

```json
{
  "success": boolean,
  "data": {
    // Tool-specific data structure
  },
  "metadata": {
    "query_time": "ISO 8601 datetime",
    "data_source": "string",
    "cache_hit": boolean,
    "data_age_seconds": integer | null
  },
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": "Additional context and debugging information"
  } | null
}
```

### Field Descriptions

- **success**: `true` if request succeeded, `false` if error occurred
- **data**: Tool-specific response data (null on error)
- **metadata**: Query execution metadata
  - **query_time**: When the query was executed (ISO 8601 format with timezone)
  - **data_source**: Source of the data (e.g., "Eastmoney", "Tencent Finance", "Sina Finance")
  - **cache_hit**: Whether data was served from cache
  - **data_age_seconds**: Age of cached data in seconds (null if fresh)
- **error**: Error information (null on success)
  - **code**: Machine-readable error code
  - **message**: Human-readable error description
  - **details**: Additional context for debugging

---

## Error Codes

### Common Error Codes

| Code | Description | HTTP Equivalent |
|------|-------------|-----------------|
| `INVALID_DATE` | Invalid date format or out of range | 400 |
| `INVALID_PARAMETER` | Invalid parameter value | 400 |
| `MISSING_PARAMETER` | Required parameter missing | 400 |
| `DATA_UNAVAILABLE` | Data source temporarily unavailable | 503 |
| `INSUFFICIENT_DATA` | Not enough historical data for calculation | 422 |
| `RATE_LIMIT_EXCEEDED` | Too many requests in short period | 429 |
| `CACHE_ERROR` | Cache operation failed (non-fatal) | 500 |
| `CALCULATION_ERROR` | Indicator calculation failed | 500 |
| `PARSE_ERROR` | Failed to parse data source response | 502 |
| `NETWORK_ERROR` | Network request to data source failed | 503 |
| `TIMEOUT` | Request exceeded time limit | 504 |

### Error Response Example

```json
{
  "success": false,
  "data": null,
  "metadata": {
    "query_time": "2025-10-01T16:00:00+08:00",
    "data_source": null,
    "cache_hit": false,
    "data_age_seconds": null
  },
  "error": {
    "code": "INVALID_DATE",
    "message": "Invalid date format",
    "details": "Date must be in YYYY-MM-DD format. Received: '2025-13-01'"
  }
}
```

---

## Data Models

### MarketIndex

```typescript
interface MarketIndex {
  code: string;           // Index code (e.g., "000001")
  name: string;           // Index name (e.g., "上证指数")
  current: Decimal;       // Current price
  change: Decimal;        // Price change
  change_pct: Decimal;    // Change percentage
  open: Decimal;          // Opening price
  high: Decimal;          // Highest price
  low: Decimal;           // Lowest price
  close?: Decimal;        // Closing price (if market closed)
  pre_close: Decimal;     // Previous close
  volume: number;         // Trading volume (lots)
  amount: Decimal;        // Trading amount (CNY)
  turnover?: Decimal;     // Turnover rate (%)
  amplitude?: Decimal;    // Price amplitude (%)
  timestamp: datetime;    // Data timestamp
  trading_date: string;   // Trading date (YYYY-MM-DD)
  market_status: string;  // "open" | "closed" | "pre_market" | "after_hours"
}
```

### TechnicalIndicator

```typescript
interface TechnicalIndicator {
  name: string;                    // Indicator name (e.g., "MA", "MACD")
  category: IndicatorCategory;     // "trend" | "momentum" | "volatility" | "volume"
  values: Record<string, Decimal>; // Indicator values (e.g., {"MA5": 3240.50})
  signal: Signal;                  // "BUY" | "SELL" | "NEUTRAL"
  interpretation: string;          // Chinese interpretation
  timestamp: datetime;             // Calculation timestamp
  params?: Record<string, any>;    // Indicator parameters
}
```

### MarketBreadth

```typescript
interface MarketBreadth {
  total_stocks: number;           // Total number of stocks
  advancing: number;              // Number of advancing stocks
  declining: number;              // Number of declining stocks
  unchanged: number;              // Number of unchanged stocks
  limit_up: number;               // Number of limit-up stocks
  limit_down: number;             // Number of limit-down stocks
  gain_over_5pct: number;         // Stocks up >5%
  loss_over_5pct: number;         // Stocks down >5%
  gain_over_7pct: number;         // Stocks up >7%
  loss_over_7pct: number;         // Stocks down >7%
  advance_decline_ratio: Decimal; // Advancing/Declining ratio
  advance_pct: Decimal;           // Advancing percentage
  decline_pct: Decimal;           // Declining percentage
  date: string;                   // Date (YYYY-MM-DD)
  timestamp: datetime;            // Data timestamp
}
```

### SentimentAnalysis

```typescript
interface SentimentAnalysis {
  overall_sentiment: {
    score: Decimal;           // 0-100 sentiment score
    level: SentimentLevel;    // Classification
    classification: string;    // Chinese description
    date: string;             // Date (YYYY-MM-DD)
  };
  components: {
    volume_sentiment: ComponentScore;
    price_sentiment: ComponentScore;
    volatility_sentiment: ComponentScore;
    capital_sentiment: ComponentScore;
    news_sentiment: ComponentScore;
  };
  trend: {
    direction: "IMPROVING" | "DETERIORATING" | "STABLE";
    change: Decimal;          // Change from previous
    comparison: string;       // Comparison period
  };
  risk_level: "LOW" | "MEDIUM" | "HIGH" | "EXTREME";
  interpretation: string;     // Detailed Chinese interpretation
}
```

### NewsArticle

```typescript
interface NewsArticle {
  title: string;                  // Article title
  summary?: string;               // Article summary
  source: string;                 // News source
  url: string;                    // Article URL
  publish_time: datetime;         // Publication timestamp
  importance: number;             // Importance score (0-10)
  sentiment: {
    score: number;                // Sentiment score (-1 to 1)
    classification: "POSITIVE" | "NEUTRAL" | "NEGATIVE";
    label: string;                // Chinese label
  };
  impact: {
    scope: string;                // Impact scope
    time_horizon: string;         // Time horizon
    related_sectors: string[];    // Related sectors
  };
  tags: string[];                 // Article tags
}
```

---

## Performance Benchmarks

### Response Time Targets

| Tool | Target | P50 | P95 | P99 |
|------|--------|-----|-----|-----|
| get_market_data (realtime) | <2s | 500ms | 1.5s | 2s |
| get_market_data (historical) | <3s | 1s | 2.5s | 3s |
| calculate_indicators | <5s | 2s | 4s | 5s |
| get_money_flow | <2s | 500ms | 1.5s | 2s |
| get_sentiment_analysis | <3s | 1.5s | 2.5s | 3s |
| get_news | <10s | 5s | 8s | 10s |
| get_sector_data | <3s | 1s | 2.5s | 3s |
| get_macro_data | <3s | 1s | 2.5s | 3s |
| get_special_data | <3s | 1s | 2.5s | 3s |
| generate_advice (normal) | <5s | 3s | 4.5s | 5s |
| generate_advice (detailed) | <7s | 4s | 6s | 7s |
| get_market_overview | <3s | 2s | 2.8s | 3s |

### Cache Hit Rates

- **Real-time data**: 60-80% during trading hours
- **Historical data**: 90-95%
- **News**: 70-85%
- **Indicators**: 75-90%
- **Overall**: Target >60% cache hit rate

### Concurrent Load

- **Supported**: 10+ concurrent requests
- **Response degradation**: <10% under 10 concurrent requests
- **No failures**: Under normal load conditions

---

## Rate Limiting

### Client-Side Limits

No explicit client-side rate limits, but caching is strongly recommended:

- **Real-time queries**: Cache for 5 minutes during trading hours
- **Historical data**: Cache for 24 hours
- **News**: Cache for 30 minutes
- **Calculated indicators**: Cache for 30 minutes

### Data Source Limits

The server implements intelligent rate limiting and fallback mechanisms:

1. **Primary source** (Eastmoney): If rate-limited, auto-fallback to secondary
2. **Secondary source** (Tencent Finance): Fallback for index data
3. **Tertiary source** (Sina Finance): Fallback for market breadth (when available)
4. **Request spacing**: 1.5s between requests to same source
5. **Exponential backoff**: 2s initial delay, doubles on retry

---

## Best Practices

### 1. Leverage Caching

Always check `metadata.cache_hit` and `metadata.data_age_seconds`:

```python
result = get_market_data(data_type="realtime")
if result["metadata"]["cache_hit"]:
    age = result["metadata"]["data_age_seconds"]
    print(f"Data is {age}s old (cached)")
```

### 2. Handle Errors Gracefully

Check `success` field before accessing `data`:

```python
result = get_market_data(...)
if not result["success"]:
    error = result["error"]
    print(f"Error {error['code']}: {error['message']}")
else:
    # Process data
    index = result["data"]["index"]
```

### 3. Batch Related Requests

Use `data_type="all"` to get multiple data types in one request:

```python
# Good: Single request
result = get_market_data(data_type="all")

# Avoid: Multiple requests
realtime = get_market_data(data_type="realtime")
breadth = get_market_data(data_type="breadth")
```

### 4. Respect Trading Hours

Be aware that real-time data only updates during trading hours (09:30-15:00 CST):

```python
# Check market status
if result["data"]["index"]["market_status"] == "closed":
    print("Market is closed. Data from last session.")
```

### 5. Use Resources for Regular Monitoring

For periodic checks, use resources instead of tools:

```python
# Good for monitoring
uri = "market://summary/latest"

# Avoid repeated tool calls
result = get_market_data(...)  # Don't poll this
```

---

## Changelog

### Version 0.0.1 (2025-10-01)

- Initial release
- 10 MCP tools implemented
- 10 MCP resources defined
- Multi-source data fetching with automatic fallback
- Two-tier caching system
- 50+ technical indicators supported
- Comprehensive error handling

---

## Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/stock-mcp-server/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/stock-mcp-server/discussions)
- **Documentation**: [README](../README.md)

---

**Last Updated**: 2025-10-01  
**API Version**: 0.0.1  
**Protocol**: MCP 1.0

