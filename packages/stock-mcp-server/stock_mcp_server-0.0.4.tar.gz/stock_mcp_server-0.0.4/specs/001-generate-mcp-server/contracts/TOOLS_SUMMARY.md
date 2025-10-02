# MCP Tools Summary

Complete list of all 10 tools provided by Stock MCP Server.

## Tool 1: get_market_data
**Contract**: `tools/get_market_data.json`

Retrieve comprehensive market data for Shanghai Composite Index.

**Inputs**:
- `data_type`: realtime | history | breadth | valuation | turnover | all
- `index_code`: Index code (default: "000001")
- `date`: Query date (optional)
- `period`: K-line timeframe for history
- `adjust`: Price adjustment method
- `start_date`, `end_date`: Date range for history

**Outputs**:
- Real-time quotes (OHLC, volume, change %)
- Historical K-line data (OHLCV time series)
- Market breadth (advancing/declining stocks, limit moves)
- Valuation metrics (PE, PB, market cap)
- Turnover analysis (order flow by size)

**Response Time**: <2s (real-time), <3s (historical)

---

## Tool 2: calculate_indicators
**Contract**: `tools/calculate_indicators.json`

Calculate 50+ technical indicators across multiple categories.

**Inputs**:
- `indicators`: List of indicator names (ma, rsi, macd, kdj, boll, etc.)
- `category`: Filter by category (trend/momentum/volatility/volume/all)
- `params`: Indicator parameters (periods, sensitivity)
- `period`: Calculation timeframe (d/w/m)
- `start_date`, `end_date`: Date range

**Outputs**:
- Indicator values with timestamps
- Trading signals (buy/sell/neutral)
- Signal interpretations in Chinese
- Comprehensive analysis summary

**Supported Indicators**:
- Trend: MA, EMA, MACD, DMI, ADX, TRIX, Aroon, CCI, SAR, Ichimoku
- Momentum: RSI, KDJ, Stochastic, Williams %R, ROC
- Volatility: BOLL, ATR, Keltner, Donchian
- Volume: OBV, MFI, CMF, VWAP, AD Line

**Response Time**: <5s

---

## Tool 3: get_money_flow
**Contract**: `tools/get_money_flow.json`

Track capital flows across different categories.

**Inputs**:
- `date`: Query date (optional)
- `flow_type`: north | margin | main | all

**Outputs**:
- Northbound capital (Shanghai Connect): inflow/outflow/net/holdings
- Margin trading: financing/short balance, buy/sell volumes
- Main capital: super large/large/medium/small order net flows
- Historical trends and comparisons

**Response Time**: <2s

---

## Tool 4: get_sentiment_analysis
**Contract**: `tools/get_sentiment_analysis.json`

Calculate multi-dimensional market sentiment index.

**Inputs**:
- `date`: Analysis date (optional)
- `dimension`: all | volume | price | volatility | capital | news
- `days`: Historical trend period (default: 30)
- `include_trend`: Include trend analysis (true/false)

**Outputs**:
- Overall sentiment index (0-100)
- Sentiment level classification (extreme panic to extreme optimism)
- Component scores (volume, price, volatility, capital, news)
- Sentiment trend (improving/deteriorating/stable)
- Chinese interpretation with risk level

**Response Time**: <3s

---

## Tool 5: get_news
**Contract**: `tools/get_news.json`

Retrieve and analyze financial news with sentiment scoring.

**Inputs**:
- `limit`: Number of news items (default: 10)
- `category`: policy | market | company | industry | international | all
- `importance`: Minimum importance score (0-10)
- `include_sentiment`: Perform sentiment analysis (true/false)
- `include_hot_topics`: Include hot topics aggregation (true/false)
- `sentiment_method`: snownlp | llm

**Outputs**:
- News articles (title, summary, source, timestamp)
- Sentiment classification (positive/neutral/negative)
- Importance scores
- Related stocks/sectors/tags
- Hot topics aggregation
- Overall news sentiment

**Sources**: Dongfang Fortune, Sina Finance, Securities Times, 21 Finance

**Response Time**: <10s

---

## Tool 6: get_sector_data
**Contract**: `tools/get_sector_data.json`

Retrieve sector and industry performance data.

**Inputs**:
- `sector_type`: industry | concept | region | style | all
- `sort_by`: change | turnover | money_flow
- `limit`: Number of sectors to return
- `include_rotation`: Include rotation analysis (true/false)
- `include_leaders`: Include leading stocks (true/false)
- `rotation_days`: Rotation analysis period (default: 30)

**Outputs**:
- Sector rankings by performance/capital flow
- Leading stocks in each sector
- Sector rotation patterns and trends
- Capital flow by sector

**Coverage**:
- 28 SW Level-1 industries
- 200+ concept sectors
- Regional sectors (provinces/cities)
- Style sectors (large/mid/small cap, value/growth)

**Response Time**: <3s

---

## Tool 7: get_macro_data
**Contract**: `tools/get_macro_data.json`

Retrieve macroeconomic indicators and global market data.

**Inputs**:
- `data_type`: macro | global | all
- `indicators`: gdp | cpi | pmi | m2 | etc. (multiple)
- `markets`: us_stock | commodity | forex | etc.
- `period`: monthly | quarterly | yearly
- `include_impact`: Include A-share impact analysis (true/false)

**Outputs**:
- Domestic macro indicators (GDP, CPI, PPI, PMI, M0/M1/M2)
- International markets (US/EU/Asia indices, commodities, forex)
- Year-over-year and month-over-month changes
- Market impact analysis on A-shares

**Response Time**: <3s

---

## Tool 8: get_special_data
**Contract**: `tools/get_special_data.json`

Retrieve special market data (Dragon-Tiger List, block trades, IPOs, derivatives).

**Inputs**:
- `data_type`: longhu | block_trade | unlock | new_stock | futures | options | convertible_bond
- `contract`: Futures contract (IH/IF/IC/IM) - for futures
- `underlying`: Option underlying (50ETF/300ETF) - for options
- `sort_by`: Sorting criteria
- `limit`: Number of items

**Outputs**:
- Dragon-Tiger List: top stocks, institutional/retail trading
- Block trades: volume, premium/discount rates
- Lock-up expirations: unlocking value, share counts
- IPOs: new listings, first-day performance
- Futures: quotes, basis, open interest (optional)
- Options: option chain, IV, PCR (optional)
- Convertible bonds: list, premium rates (optional)

**Response Time**: <3s

---

## Tool 9: generate_advice
**Contract**: `tools/generate_advice.json`

Generate comprehensive investment recommendations based on multi-dimensional analysis.

**Inputs**:
- `analysis_depth`: simple | normal | detailed
- `focus_area`: technical | fundamental | sentiment | capital | news | all
- `date`: Analysis date (optional)
- `include_risk`: Include risk assessment (true/false)
- `include_backtest`: Include strategy backtest (true/false)
- `strategy_params`: Custom backtest parameters

**Outputs**:
- Market outlook (bullish/bearish/sideways)
- Operation suggestion (aggressive/cautious/wait)
- Position recommendation (heavy/half/light/empty with %)
- Multi-dimensional analysis (technical/fundamental/sentiment/capital/news)
- Risk assessment (level, factors, warnings)
- Actionable insights (focus points, strategy, entry/exit levels)
- Backtest results (optional): win rate, returns, Sharpe ratio
- Confidence score
- Investment disclaimer

**Response Time**: <5s (normal), <7s (detailed)

---

## Tool 10: get_market_overview
**Contract**: `tools/get_market_overview.json`

Get comprehensive market snapshot combining all data types.

**Inputs**:
- `date`: Query date (optional)
- `include_details`: Include detailed breakdowns (true/false)

**Outputs**:
- Index quotes summary
- Market breadth statistics
- Capital flow summary
- Sentiment index
- Top sectors (gainers/losers)
- Top 5 important news
- Core market insight

**Response Time**: <3s

---

## Common Response Format

All tools return responses in this format:

```json
{
  "success": boolean,
  "data": { ... },  // Tool-specific data
  "metadata": {
    "query_time": "ISO 8601 datetime",
    "data_source": "string",
    "cache_hit": boolean,
    "data_age_seconds": integer | null
  },
  "error": {  // Only if success=false
    "code": "ERROR_CODE",
    "message": "Human-readable message",
    "details": "Additional context"
  } | null
}
```

## Error Codes

Common error codes across all tools:

- `INVALID_DATE`: Invalid date format or out of range
- `INVALID_PARAMETER`: Invalid parameter value
- `DATA_UNAVAILABLE`: Data source temporarily unavailable
- `INSUFFICIENT_DATA`: Not enough data for calculation
- `RATE_LIMIT_EXCEEDED`: Too many requests
- `CACHE_ERROR`: Cache operation failed (non-fatal)
- `CALCULATION_ERROR`: Indicator calculation failed
- `PARSE_ERROR`: Failed to parse data source response

## Performance Targets

| Tool | Target | Typical |
|------|--------|---------|
| get_market_data | 2s | 500ms |
| calculate_indicators | 5s | 2s |
| get_money_flow | 2s | 500ms |
| get_sentiment_analysis | 3s | 1.5s |
| get_news | 10s | 5s |
| get_sector_data | 3s | 1s |
| get_macro_data | 3s | 1s |
| get_special_data | 3s | 1s |
| generate_advice | 5s | 3s |
| get_market_overview | 3s | 2s |
