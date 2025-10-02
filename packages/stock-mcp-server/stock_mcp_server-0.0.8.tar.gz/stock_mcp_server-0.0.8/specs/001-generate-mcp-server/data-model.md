# Data Model: Stock Market Data MCP Server

**Date**: 2025-09-30  
**Phase**: 1 - Design & Contracts  
**Status**: Complete

## Overview

This document defines the data models (entities) for the Stock MCP Server. All models will be implemented as Pydantic schemas for validation and serialization.

## Entity Relationship Diagram

```
MarketIndex ──┬──> HistoricalPrice (many)
              ├──> TechnicalIndicator (many)
              ├──> MarketBreadth (one per date)
              ├──> CapitalFlow (one per date)
              └──> MarketSentiment (one per date)

NewsArticle ──> MarketSentiment (influences)

Sector ──> MarketIndex (performance correlation)

MacroIndicator ──> MarketIndex (market impact)

MarketOverview ──> [aggregates all entities]

InvestmentRecommendation ──> [derived from all entities]
```

---

## 1. MarketIndex

Represents the Shanghai Composite Index or other market indices.

### Schema
```python
from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal

class MarketIndex(BaseModel):
    """Market index data model"""
    
    # Identification
    code: str = Field(..., description="Index code, e.g., '000001' for Shanghai Composite")
    name: str = Field(..., description="Index name, e.g., '上证指数'")
    
    # Price data
    current: Decimal = Field(..., description="Current/latest price")
    open: Decimal = Field(..., description="Opening price")
    high: Decimal = Field(..., description="Highest price of the day")
    low: Decimal = Field(..., description="Lowest price of the day")
    close: Decimal | None = Field(None, description="Closing price (None if market open)")
    pre_close: Decimal = Field(..., description="Previous close price")
    
    # Change metrics
    change: Decimal = Field(..., description="Price change amount")
    change_pct: Decimal = Field(..., description="Price change percentage")
    amplitude: Decimal = Field(..., description="Price amplitude (high-low)/pre_close")
    
    # Volume metrics
    volume: int = Field(..., description="Trading volume in lots (手)")
    amount: Decimal = Field(..., description="Trading amount in CNY")
    turnover_rate: Decimal | None = Field(None, description="Turnover rate percentage")
    volume_ratio: Decimal | None = Field(None, description="Volume ratio vs 5-day average")
    avg_amount_60d: Decimal | None = Field(None, description="60-day average trading amount")
    
    # Metadata
    timestamp: datetime = Field(..., description="Data timestamp")
    trading_date: str = Field(..., description="Trading date YYYY-MM-DD")
    market_status: str = Field(..., description="Market status: open/closed/pre-market/after-hours")
    
    class Config:
        json_schema_extra = {
            "example": {
                "code": "000001",
                "name": "上证指数",
                "current": 3245.67,
                "open": 3230.50,
                "high": 3250.00,
                "low": 3228.00,
                "close": 3245.67,
                "pre_close": 3235.00,
                "change": 10.67,
                "change_pct": 0.33,
                "amplitude": 0.68,
                "volume": 28500000,
                "amount": 345000000000,
                "turnover_rate": 1.25,
                "volume_ratio": 1.15,
                "avg_amount_60d": 320000000000,
                "timestamp": "2025-09-30T15:00:00+08:00",
                "trading_date": "2025-09-30",
                "market_status": "closed"
            }
        }
```

### Validation Rules
- `change_pct` must be calculated as `(current - pre_close) / pre_close * 100`
- `amplitude` must be `(high - low) / pre_close * 100`
- `volume` must be >= 0
- `amount` must be >= 0
- `trading_date` must match timestamp date

---

## 2. HistoricalPrice

Represents OHLCV data for a specific time period.

### Schema
```python
class TimeFrame(str, Enum):
    """Supported timeframes"""
    MIN_1 = "1min"
    MIN_5 = "5min"
    MIN_15 = "15min"
    MIN_30 = "30min"
    MIN_60 = "60min"
    DAILY = "1day"
    WEEKLY = "1week"
    MONTHLY = "1month"
    QUARTERLY = "1quarter"
    YEARLY = "1year"

class AdjustType(str, Enum):
    """Price adjustment types"""
    NONE = "none"      # 不复权
    FORWARD = "qfq"    # 前复权
    BACKWARD = "hfq"   # 后复权

class HistoricalPrice(BaseModel):
    """Historical OHLCV data"""
    
    # Identification
    symbol: str = Field(..., description="Symbol code")
    date: str = Field(..., description="Trading date/time YYYY-MM-DD or YYYY-MM-DD HH:MM:SS")
    timeframe: TimeFrame = Field(..., description="K-line timeframe")
    adjust: AdjustType = Field(AdjustType.NONE, description="Price adjustment method")
    
    # OHLCV
    open: Decimal = Field(..., description="Opening price")
    high: Decimal = Field(..., description="Highest price")
    low: Decimal = Field(..., description="Lowest price")
    close: Decimal = Field(..., description="Closing price")
    volume: int = Field(..., description="Trading volume (lots)")
    amount: Decimal | None = Field(None, description="Trading amount (CNY)")
    
    # Derived metrics
    change: Decimal | None = Field(None, description="Price change from previous period")
    change_pct: Decimal | None = Field(None, description="Change percentage")
    amplitude: Decimal | None = Field(None, description="Amplitude percentage")
    turnover_rate: Decimal | None = Field(None, description="Turnover rate")
    
    class Config:
        json_schema_extra = {
            "example": {
                "symbol": "000001",
                "date": "2025-09-30",
                "timeframe": "1day",
                "adjust": "qfq",
                "open": 3230.50,
                "high": 3250.00,
                "low": 3228.00,
                "close": 3245.67,
                "volume": 28500000,
                "amount": 345000000000,
                "change": 10.67,
                "change_pct": 0.33,
                "amplitude": 0.68,
                "turnover_rate": 1.25
            }
        }
```

### Validation Rules
- `high` >= `low`
- `high` >= `open`, `close`
- `low` <= `open`, `close`
- `volume` >= 0

---

## 3. TechnicalIndicator

Represents calculated technical indicator values.

### Schema
```python
class IndicatorCategory(str, Enum):
    """Indicator categories"""
    TREND = "trend"
    MOMENTUM = "momentum"
    VOLATILITY = "volatility"
    VOLUME = "volume"
    STRENGTH = "strength"
    OTHER = "other"

class Signal(str, Enum):
    """Trading signals"""
    STRONG_BUY = "strong_buy"
    BUY = "buy"
    NEUTRAL = "neutral"
    SELL = "sell"
    STRONG_SELL = "strong_sell"

class TechnicalIndicator(BaseModel):
    """Technical indicator calculation result"""
    
    # Identification
    name: str = Field(..., description="Indicator name, e.g., 'MA', 'RSI', 'MACD'")
    category: IndicatorCategory = Field(..., description="Indicator category")
    period: int | None = Field(None, description="Calculation period (days)")
    
    # Values (flexible structure for different indicators)
    values: dict[str, Decimal | list[Decimal]] = Field(..., description="Indicator values")
    
    # Interpretation
    signal: Signal | None = Field(None, description="Trading signal")
    interpretation: str | None = Field(None, description="Human-readable interpretation")
    
    # Metadata
    date: str = Field(..., description="Calculation date")
    calculated_at: datetime = Field(..., description="Calculation timestamp")
    
    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "name": "MA",
                    "category": "trend",
                    "period": 20,
                    "values": {
                        "ma5": 3240.50,
                        "ma10": 3235.00,
                        "ma20": 3230.00,
                        "ma60": 3220.00
                    },
                    "signal": "buy",
                    "interpretation": "短期均线上穿中期均线，呈多头排列",
                    "date": "2025-09-30",
                    "calculated_at": "2025-09-30T15:30:00+08:00"
                },
                {
                    "name": "MACD",
                    "category": "trend",
                    "period": None,
                    "values": {
                        "dif": 5.23,
                        "dea": 3.45,
                        "macd": 1.78
                    },
                    "signal": "buy",
                    "interpretation": "MACD金叉，DIF上穿DEA",
                    "date": "2025-09-30",
                    "calculated_at": "2025-09-30T15:30:00+08:00"
                },
                {
                    "name": "RSI",
                    "category": "momentum",
                    "period": 14,
                    "values": {
                        "rsi6": 65.5,
                        "rsi12": 62.3,
                        "rsi24": 58.7
                    },
                    "signal": "neutral",
                    "interpretation": "RSI处于正常区间，无超买超卖",
                    "date": "2025-09-30",
                    "calculated_at": "2025-09-30T15:30:00+08:00"
                }
            ]
        }
```

---

## 4. MarketBreadth

Market-wide participation and breadth metrics.

### Schema
```python
class MarketBreadth(BaseModel):
    """Market breadth metrics"""
    
    # Basic counts
    total_stocks: int = Field(..., description="Total number of stocks")
    advancing: int = Field(..., description="Number of advancing stocks")
    declining: int = Field(..., description="Number of declining stocks")
    unchanged: int = Field(..., description="Number of unchanged stocks")
    
    # Extreme moves
    limit_up: int = Field(..., description="Stocks hitting upper limit (+10%)")
    limit_down: int = Field(..., description="Stocks hitting lower limit (-10%)")
    consecutive_limit_up: int = Field(0, description="Stocks with consecutive limit ups")
    consecutive_limit_down: int = Field(0, description="Stocks with consecutive limit downs")
    broken_limit: int = Field(0, description="Stocks that broke limit (opened limit)")
    
    # Distribution
    gain_over_5pct: int = Field(0, description="Stocks gaining >5%")
    loss_over_5pct: int = Field(0, description="Stocks losing >5%")
    gain_over_7pct: int = Field(0, description="Stocks gaining >7%")
    loss_over_7pct: int = Field(0, description="Stocks losing >7%")
    
    # New highs/lows
    new_high_60d: int = Field(0, description="Stocks at 60-day high")
    new_low_60d: int = Field(0, description="Stocks at 60-day low")
    new_high_all_time: int = Field(0, description="Stocks at all-time high")
    new_low_all_time: int = Field(0, description="Stocks at all-time low")
    
    # Ratios (calculated)
    advance_decline_ratio: Decimal = Field(..., description="Advancing / Declining ratio")
    advance_pct: Decimal = Field(..., description="% of stocks advancing")
    decline_pct: Decimal = Field(..., description="% of stocks declining")
    
    # Metadata
    date: str = Field(..., description="Trading date")
    timestamp: datetime = Field(..., description="Data timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "total_stocks": 5000,
                "advancing": 2800,
                "declining": 2100,
                "unchanged": 100,
                "limit_up": 45,
                "limit_down": 12,
                "consecutive_limit_up": 8,
                "consecutive_limit_down": 3,
                "broken_limit": 15,
                "gain_over_5pct": 420,
                "loss_over_5pct": 280,
                "gain_over_7pct": 180,
                "loss_over_7pct": 95,
                "new_high_60d": 250,
                "new_low_60d": 120,
                "new_high_all_time": 15,
                "new_low_all_time": 8,
                "advance_decline_ratio": 1.33,
                "advance_pct": 56.0,
                "decline_pct": 42.0,
                "date": "2025-09-30",
                "timestamp": "2025-09-30T15:00:00+08:00"
            }
        }
```

### Validation Rules
- `advancing + declining + unchanged` should equal `total_stocks`
- All counts >= 0
- Percentages between 0-100

---

## 5. CapitalFlow

Money flow and capital tracking data.

### Schema
```python
class CapitalFlow(BaseModel):
    """Capital flow data"""
    
    # Northbound capital (Shanghai/Shenzhen Connect)
    north_inflow: Decimal | None = Field(None, description="Northbound inflow (CNY)")
    north_outflow: Decimal | None = Field(None, description="Northbound outflow (CNY)")
    north_net: Decimal | None = Field(None, description="Northbound net buy (CNY)")
    north_total_holdings: Decimal | None = Field(None, description="Total northbound holdings")
    north_holdings_pct: Decimal | None = Field(None, description="% of market cap held by northbound")
    
    # Main capital flows (by order size)
    super_large_net: Decimal | None = Field(None, description="Super large orders (>100万) net inflow")
    large_net: Decimal | None = Field(None, description="Large orders (50-100万) net inflow")
    medium_net: Decimal | None = Field(None, description="Medium orders (10-50万) net inflow")
    small_net: Decimal | None = Field(None, description="Small orders (<10万) net inflow")
    main_net: Decimal | None = Field(None, description="Main capital (super+large) net inflow")
    
    # Margin trading (融资融券)
    margin_balance: Decimal | None = Field(None, description="Financing balance (CNY)")
    margin_buy: Decimal | None = Field(None, description="Financing buy amount (CNY)")
    margin_repay: Decimal | None = Field(None, description="Financing repayment (CNY)")
    short_balance: Decimal | None = Field(None, description="Short selling balance (shares)")
    short_sell: int | None = Field(None, description="Short selling volume (shares)")
    short_cover: int | None = Field(None, description="Short covering volume (shares)")
    margin_total: Decimal | None = Field(None, description="Total margin + short balance")
    
    # Metadata
    date: str = Field(..., description="Trading date")
    timestamp: datetime = Field(..., description="Data timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "north_inflow": 5800000000,
                "north_outflow": 4200000000,
                "north_net": 1600000000,
                "north_total_holdings": 2500000000000,
                "north_holdings_pct": 4.2,
                "super_large_net": -800000000,
                "large_net": -400000000,
                "medium_net": 600000000,
                "small_net": 800000000,
                "main_net": -1200000000,
                "margin_balance": 1850000000000,
                "margin_buy": 95000000000,
                "margin_repay": 92000000000,
                "short_balance": 12500000000,
                "short_sell": 180000000,
                "short_cover": 160000000,
                "margin_total": 1862500000000,
                "date": "2025-09-30",
                "timestamp": "2025-09-30T15:30:00+08:00"
            }
        }
```

---

## 6. MarketSentiment

Aggregated market sentiment analysis.

### Schema
```python
class SentimentLevel(str, Enum):
    """Sentiment classification"""
    EXTREME_PANIC = "extreme_panic"      # 0-20
    PANIC = "panic"                      # 21-40
    NEUTRAL = "neutral"                  # 41-60
    OPTIMISTIC = "optimistic"            # 61-80
    EXTREME_OPTIMISM = "extreme_optimism"  # 81-100

class MarketSentiment(BaseModel):
    """Market sentiment analysis"""
    
    # Overall sentiment
    sentiment_index: Decimal = Field(..., ge=0, le=100, description="Overall sentiment score (0-100)")
    sentiment_level: SentimentLevel = Field(..., description="Sentiment classification")
    
    # Component scores
    volume_sentiment: Decimal = Field(..., ge=0, le=100, description="Volume-based sentiment")
    price_sentiment: Decimal = Field(..., ge=0, le=100, description="Price movement sentiment")
    volatility_sentiment: Decimal = Field(..., ge=0, le=100, description="Volatility sentiment")
    capital_sentiment: Decimal = Field(..., ge=0, le=100, description="Capital flow sentiment")
    news_sentiment: Decimal | None = Field(None, ge=0, le=100, description="News sentiment")
    
    # Component weights (for transparency)
    weights: dict[str, Decimal] = Field(
        default={"volume": 0.25, "price": 0.35, "volatility": 0.15, "capital": 0.15, "news": 0.10},
        description="Weights used in sentiment calculation"
    )
    
    # Trend
    sentiment_trend: str | None = Field(None, description="Trend: improving/deteriorating/stable")
    previous_sentiment: Decimal | None = Field(None, description="Previous day sentiment for comparison")
    sentiment_change: Decimal | None = Field(None, description="Change from previous day")
    
    # Interpretation
    interpretation: str = Field(..., description="Human-readable sentiment interpretation")
    risk_level: str | None = Field(None, description="Risk level: low/medium/high/extreme")
    
    # Metadata
    date: str = Field(..., description="Analysis date")
    calculated_at: datetime = Field(..., description="Calculation timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "sentiment_index": 62.5,
                "sentiment_level": "optimistic",
                "volume_sentiment": 70.0,
                "price_sentiment": 68.0,
                "volatility_sentiment": 55.0,
                "capital_sentiment": 58.0,
                "news_sentiment": 65.0,
                "weights": {
                    "volume": 0.25,
                    "price": 0.35,
                    "volatility": 0.15,
                    "capital": 0.15,
                    "news": 0.10
                },
                "sentiment_trend": "improving",
                "previous_sentiment": 58.5,
                "sentiment_change": 4.0,
                "interpretation": "市场情绪偏乐观,成交活跃,资金流入积极,建议适当参与",
                "risk_level": "medium",
                "date": "2025-09-30",
                "calculated_at": "2025-09-30T15:45:00+08:00"
            }
        }
```

### Calculation Formula
```python
sentiment_index = (
    volume_sentiment * 0.25 +
    price_sentiment * 0.35 +
    volatility_sentiment * 0.15 +
    capital_sentiment * 0.15 +
    news_sentiment * 0.10
)
```

---

## 7. NewsArticle

Financial news article with sentiment analysis.

### Schema
```python
class NewsCategory(str, Enum):
    """News categories"""
    POLICY = "policy"              # 政策
    MARKET = "market"              # 市场
    COMPANY = "company"            # 公司
    INDUSTRY = "industry"          # 行业
    INTERNATIONAL = "international"  # 国际
    ALL = "all"

class NewsSentiment(str, Enum):
    """News sentiment"""
    POSITIVE = "positive"    # 利好
    NEUTRAL = "neutral"      # 中性
    NEGATIVE = "negative"    # 利空

class NewsArticle(BaseModel):
    """Financial news article"""
    
    # Content
    title: str = Field(..., description="News title")
    summary: str | None = Field(None, description="News summary/excerpt")
    content: str | None = Field(None, description="Full content if available")
    url: str | None = Field(None, description="Source URL")
    
    # Classification
    category: NewsCategory = Field(..., description="News category")
    source: str = Field(..., description="News source, e.g., '东方财富'")
    published_at: datetime = Field(..., description="Publication timestamp")
    
    # Analysis
    importance: Decimal = Field(..., ge=0, le=10, description="Importance score (0-10)")
    sentiment: NewsSentiment | None = Field(None, description="Sentiment classification")
    sentiment_score: Decimal | None = Field(None, ge=0, le=1, description="Sentiment score (0-1)")
    
    # Relations
    related_stocks: list[str] | None = Field(None, description="Related stock codes")
    related_sectors: list[str] | None = Field(None, description="Related sectors")
    tags: list[str] | None = Field(None, description="Keywords/tags")
    
    # Impact
    market_impact: str | None = Field(None, description="全市场/行业/个股")
    time_horizon: str | None = Field(None, description="长期/中期/短期")
    
    # Metadata
    scraped_at: datetime = Field(..., description="When the news was scraped")
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "央行宣布降准0.5个百分点 释放流动性约1.2万亿",
                "summary": "中国人民银行决定于2025年10月15日下调金融机构存款准备金率0.5个百分点...",
                "content": None,
                "url": "https://finance.eastmoney.com/...",
                "category": "policy",
                "source": "东方财富",
                "published_at": "2025-09-30T16:30:00+08:00",
                "importance": 9.5,
                "sentiment": "positive",
                "sentiment_score": 0.85,
                "related_stocks": None,
                "related_sectors": ["银行", "房地产"],
                "tags": ["货币政策", "降准", "流动性"],
                "market_impact": "全市场",
                "time_horizon": "中期",
                "scraped_at": "2025-09-30T17:00:00+08:00"
            }
        }
```

---

## 8. Sector

Sector/industry performance data.

### Schema
```python
class SectorType(str, Enum):
    """Sector types"""
    INDUSTRY = "industry"    # 申万行业
    CONCEPT = "concept"      # 概念板块
    REGION = "region"        # 地域板块
    STYLE = "style"          # 风格板块

class Sector(BaseModel):
    """Sector data"""
    
    # Identification
    code: str = Field(..., description="Sector code")
    name: str = Field(..., description="Sector name")
    type: SectorType = Field(..., description="Sector type")
    level: int | None = Field(None, description="Industry level (1/2/3) for SW industries")
    
    # Performance
    change_pct: Decimal = Field(..., description="Price change %")
    turnover: Decimal | None = Field(None, description="Turnover amount (CNY)")
    turnover_rate: Decimal | None = Field(None, description="Turnover rate %")
    
    # Composition
    stock_count: int = Field(..., description="Number of stocks in sector")
    leader_stocks: list[dict] | None = Field(None, description="Leading stocks in sector")
    
    # Capital flow
    main_net_inflow: Decimal | None = Field(None, description="Main capital net inflow")
    
    # Metadata
    date: str = Field(..., description="Trading date")
    timestamp: datetime = Field(..., description="Data timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "code": "801780",
                "name": "银行",
                "type": "industry",
                "level": 1,
                "change_pct": 2.35,
                "turnover": 58000000000,
                "turnover_rate": 0.85,
                "stock_count": 42,
                "leader_stocks": [
                    {"code": "601398", "name": "工商银行", "change_pct": 2.8},
                    {"code": "601939", "name": "建设银行", "change_pct": 2.5}
                ],
                "main_net_inflow": 1200000000,
                "date": "2025-09-30",
                "timestamp": "2025-09-30T15:00:00+08:00"
            }
        }
```

---

## 9. MacroIndicator

Macroeconomic indicator data.

### Schema
```python
class MacroPeriod(str, Enum):
    """Macro data periods"""
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    YEARLY = "yearly"

class MacroIndicator(BaseModel):
    """Macroeconomic indicator"""
    
    # Identification
    indicator_name: str = Field(..., description="Indicator name, e.g., 'GDP', 'CPI', 'PMI'")
    indicator_code: str | None = Field(None, description="Official indicator code")
    
    # Value
    value: Decimal = Field(..., description="Indicator value")
    unit: str | None = Field(None, description="Unit, e.g., '%', '亿元'")
    
    # Period
    period: MacroPeriod = Field(..., description="Data period")
    period_date: str = Field(..., description="Period date, e.g., '2025-09' or '2025-Q3'")
    
    # Changes
    yoy_change: Decimal | None = Field(None, description="Year-over-year change")
    mom_change: Decimal | None = Field(None, description="Month-over-month change")
    
    # Metadata
    release_date: datetime = Field(..., description="Official release date")
    source: str = Field(..., description="Data source, e.g., '国家统计局'")
    
    class Config:
        json_schema_extra = {
            "example": {
                "indicator_name": "CPI",
                "indicator_code": "A01010101",
                "value": 102.5,
                "unit": "%",
                "period": "monthly",
                "period_date": "2025-09",
                "yoy_change": 2.5,
                "mom_change": 0.3,
                "release_date": "2025-10-15T09:30:00+08:00",
                "source": "国家统计局"
            }
        }
```

---

## 10. InvestmentRecommendation

Generated investment advice.

### Schema
```python
class MarketOutlook(str, Enum):
    """Market outlook"""
    BULLISH = "bullish"      # 看多
    BEARISH = "bearish"      # 看空
    SIDEWAYS = "sideways"    # 震荡

class OperationSuggestion(str, Enum):
    """Operation suggestion"""
    AGGRESSIVE = "aggressive"  # 积极
    CAUTIOUS = "cautious"      # 谨慎
    WAIT = "wait"              # 观望

class PositionRecommendation(str, Enum):
    """Position recommendation"""
    HEAVY = "heavy"    # 重仓 (70-100%)
    HALF = "half"      # 半仓 (40-70%)
    LIGHT = "light"    # 轻仓 (10-40%)
    EMPTY = "empty"    # 空仓 (0-10%)

class InvestmentRecommendation(BaseModel):
    """Investment recommendation"""
    
    # Core recommendations
    market_outlook: MarketOutlook = Field(..., description="Overall market view")
    operation_suggestion: OperationSuggestion = Field(..., description="Suggested approach")
    position_recommendation: PositionRecommendation = Field(..., description="Position sizing")
    
    # Multi-dimensional analysis
    technical_analysis: str = Field(..., description="Technical analysis summary")
    fundamental_analysis: str = Field(..., description="Fundamental/market breadth analysis")
    sentiment_analysis: str = Field(..., description="Sentiment analysis summary")
    capital_analysis: str = Field(..., description="Capital flow analysis")
    news_analysis: str | None = Field(None, description="News impact analysis")
    
    # Risk assessment
    risk_level: str = Field(..., description="低风险/中等风险/高风险/极高风险")
    risk_factors: list[str] = Field(..., description="Key risk factors")
    risk_warning: str = Field(..., description="Risk warning statement")
    
    # Actionable insights
    key_focus_points: list[str] = Field(..., description="Key points to watch")
    operational_strategy: str = Field(..., description="Specific operational strategy")
    
    # Confidence & disclaimers
    confidence_score: Decimal | None = Field(None, ge=0, le=100, description="Recommendation confidence")
    disclaimer: str = Field(
        default="本建议仅供参考，不构成投资建议。投资有风险，入市需谨慎。",
        description="Investment disclaimer"
    )
    
    # Metadata
    analysis_depth: str = Field(..., description="simple/normal/detailed")
    generated_at: datetime = Field(..., description="Generation timestamp")
    valid_until: datetime | None = Field(None, description="Recommendation validity period")
    
    class Config:
        json_schema_extra = {
            "example": {
                "market_outlook": "bullish",
                "operation_suggestion": "cautious",
                "position_recommendation": "half",
                "technical_analysis": "短期均线多头排列，MACD金叉，RSI处于正常区间，技术面偏多",
                "fundamental_analysis": "涨跌家数比2:1，市场宽度良好，成交量放大，市场参与度较高",
                "sentiment_analysis": "市场情绪指数62.5，处于偏乐观区间，但需注意是否过热",
                "capital_analysis": "北向资金净流入16亿，主力资金小幅流出12亿，观望情绪浓厚",
                "news_analysis": "央行降准利好，释放流动性，短期提振市场信心",
                "risk_level": "中等风险",
                "risk_factors": [
                    "市场情绪偏高，需警惕回调风险",
                    "主力资金流出，缺乏持续性支撑",
                    "外部环境仍有不确定性"
                ],
                "risk_warning": "市场短期波动可能加大，建议控制仓位，设置止损",
                "key_focus_points": [
                    "关注北向资金动向",
                    "留意主力资金是否回流",
                    "关注量能是否持续放大"
                ],
                "operational_strategy": "建议半仓操作，可逢低适当加仓，重点关注银行、地产等政策受益板块",
                "confidence_score": 72.5,
                "disclaimer": "本建议仅供参考，不构成投资建议。投资有风险，入市需谨慎。",
                "analysis_depth": "detailed",
                "generated_at": "2025-09-30T16:00:00+08:00",
                "valid_until": "2025-10-01T09:30:00+08:00"
            }
        }
```

---

## 11. MarketOverview

Comprehensive market snapshot.

### Schema
```python
class MarketOverview(BaseModel):
    """Comprehensive market overview"""
    
    # Index quotes (simplified)
    index_quotes: dict[str, dict] = Field(..., description="Key index quotes")
    
    # Market breadth summary
    breadth_summary: dict = Field(..., description="Market breadth key metrics")
    
    # Capital flow summary
    capital_summary: dict = Field(..., description="Capital flow summary")
    
    # Sentiment
    sentiment_index: Decimal = Field(..., description="Overall sentiment index")
    sentiment_level: str = Field(..., description="Sentiment classification")
    
    # Top sectors
    top_sectors_by_gain: list[dict] = Field(..., description="Top performing sectors")
    top_sectors_by_loss: list[dict] | None = Field(None, description="Worst performing sectors")
    
    # Top news
    top_news: list[dict] = Field(..., max_length=5, description="Top 5 important news")
    
    # Core insight
    core_insight: str = Field(..., description="Today's core market insight")
    
    # Metadata
    date: str = Field(..., description="Trading date")
    generated_at: datetime = Field(..., description="Generation timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "index_quotes": {
                    "000001": {
                        "name": "上证指数",
                        "close": 3245.67,
                        "change_pct": 0.33
                    }
                },
                "breadth_summary": {
                    "advancing": 2800,
                    "declining": 2100,
                    "advance_pct": 56.0
                },
                "capital_summary": {
                    "north_net": 1600000000,
                    "main_net": -1200000000
                },
                "sentiment_index": 62.5,
                "sentiment_level": "optimistic",
                "top_sectors_by_gain": [
                    {"name": "银行", "change_pct": 2.35},
                    {"name": "房地产", "change_pct": 2.10}
                ],
                "top_news": [
                    {
                        "title": "央行宣布降准0.5个百分点",
                        "importance": 9.5,
                        "sentiment": "positive"
                    }
                ],
                "core_insight": "市场情绪偏乐观，政策利好提振信心，建议关注银行、地产板块",
                "date": "2025-09-30",
                "generated_at": "2025-09-30T16:00:00+08:00"
            }
        }
```

---

## Implementation Notes

### Pydantic Configuration
All models will use Pydantic v2 with:
- Strict type validation
- JSON schema generation for contracts
- Automatic validation on instantiation
- Serialization helpers (`.model_dump()`, `.model_dump_json()`)

### Database Schema (SQLite Cache)
```sql
CREATE TABLE market_index_cache (
    id INTEGER PRIMARY KEY,
    code TEXT NOT NULL,
    date TEXT NOT NULL,
    data JSON NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL,
    UNIQUE(code, date)
);

CREATE TABLE news_cache (
    id INTEGER PRIMARY KEY,
    url TEXT UNIQUE,
    data JSON NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL
);

CREATE TABLE indicator_cache (
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL,
    indicator_name TEXT NOT NULL,
    period INTEGER,
    date TEXT NOT NULL,
    data JSON NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL,
    UNIQUE(symbol, indicator_name, period, date)
);

CREATE INDEX idx_expires ON market_index_cache(expires_at);
CREATE INDEX idx_news_expires ON news_cache(expires_at);
CREATE INDEX idx_indicator_expires ON indicator_cache(expires_at);
```

### Validation Patterns
```python
from pydantic import field_validator, model_validator

class MarketIndex(BaseModel):
    # ... fields ...
    
    @field_validator('change_pct')
    @classmethod
    def validate_change_pct(cls, v, info):
        """Validate change_pct is calculated correctly"""
        if 'current' in info.data and 'pre_close' in info.data:
            expected = (info.data['current'] - info.data['pre_close']) / info.data['pre_close'] * 100
            if abs(v - expected) > 0.01:
                raise ValueError(f"change_pct {v} doesn't match calculated {expected}")
        return v
    
    @model_validator(mode='after')
    def validate_ohlc(self):
        """Validate OHLC relationships"""
        if self.high < self.low:
            raise ValueError("high must be >= low")
        if self.high < self.open or self.high < self.close:
            raise ValueError("high must be >= open and close")
        return self
```

---

**Phase 1 Data Model Complete**: All 11 entities defined with comprehensive schemas, validation rules, and implementation notes.
