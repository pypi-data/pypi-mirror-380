# Quickstart Guide: Stock MCP Server

**Target User**: AI assistant user wanting to get Chinese A-share market insights  
**Time to Complete**: 5 minutes  
**Prerequisites**: Python 3.10+, Claude Desktop (or other MCP-compatible AI assistant)

## Overview

This guide walks through installing and using the Stock MCP Server to get comprehensive Shanghai Composite Index analysis through your AI assistant.

## Installation

### Option 1: Direct Run with uvx (Recommended)

```bash
# No installation needed! Just run:
uvx stock-mcp-server
```

### Option 2: Install via pip

```bash
pip install stock-mcp-server
stock-mcp-server
```

### Option 3: Development Setup

```bash
git clone https://github.com/yourusername/stock-mcp-server.git
cd stock-mcp-server
uv sync
uv run stock-mcp-server
```

## Configuration

### Claude Desktop Setup

Add to your Claude Desktop config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "stock-mcp": {
      "command": "uvx",
      "args": ["stock-mcp-server"]
    }
  }
}
```

**Or for local development**:
```json
{
  "mcpServers": {
    "stock-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/stock-mcp-server",
        "run",
        "stock-mcp-server"
      ]
    }
  }
}
```

### Restart Claude Desktop

After updating the config, restart Claude Desktop for changes to take effect.

## Quick Test

Once configured, the server should auto-start when Claude Desktop launches. You can verify by checking Claude's MCP status indicator.

## Usage Scenarios

### Scenario 1: Basic Market Query

**User**: "How is the Shanghai index performing today?"

**Expected Response**:
```
Shanghai Composite Index (000001)
Current: 3,245.67 (+0.33%)
Open: 3,230.50 | High: 3,250.00 | Low: 3,228.00
Volume: 285M lots | Amount: ¥345B

Market Breadth:
- Advancing: 2,800 stocks (56%)
- Declining: 2,100 stocks (42%)
- Limit Up: 45 | Limit Down: 12

Trading Status: Closed at 15:00
Data timestamp: 2025-09-30 15:00:00
```

**Acceptance Criteria**:
- ✅ Current price displayed
- ✅ Change percentage shown
- ✅ OHLC data included
- ✅ Volume and amount displayed
- ✅ Market breadth statistics shown
- ✅ Timestamp indicates data freshness

---

### Scenario 2: Technical Indicators

**User**: "Show me technical indicators for the Shanghai index"

**Expected Response**:
```
Technical Indicators for Shanghai Composite (000001)

Trend Indicators:
- MA5: 3,240.50 | MA10: 3,235.00 | MA20: 3,230.00 | MA60: 3,220.00
  Signal: BUY (短期均线上穿中期均线，呈多头排列)

- MACD: DIF=5.23 | DEA=3.45 | MACD=1.78
  Signal: BUY (金叉，DIF上穿DEA)

Momentum Indicators:
- RSI(6): 65.5 | RSI(12): 62.3 | RSI(24): 58.7
  Signal: NEUTRAL (处于正常区间，无超买超卖)

- KDJ: K=75.3 | D=68.2 | J=89.5
  Signal: NEUTRAL (J值偏高，注意回调风险)

Volatility Indicators:
- Bollinger Bands: Upper=3,260 | Middle=3,230 | Lower=3,200
  Signal: NEUTRAL (价格接近中轨)

Overall Technical Signal: BUY (7/10 indicators bullish)
```

**Acceptance Criteria**:
- ✅ Multiple indicator categories shown
- ✅ Indicator values calculated correctly
- ✅ Clear buy/sell/neutral signals
- ✅ Chinese interpretation provided
- ✅ Overall recommendation synthesized

---

### Scenario 3: Market Sentiment

**User**: "What's the market sentiment today?"

**Expected Response**:
```
Market Sentiment Analysis - 2025-09-30

Overall Sentiment: OPTIMISTIC (62.5/100)

Component Breakdown:
- Volume Sentiment: 70.0/100 (成交活跃，量能充足)
- Price Sentiment: 68.0/100 (涨多跌少，市场偏强)
- Volatility Sentiment: 55.0/100 (波动正常)
- Capital Sentiment: 58.0/100 (资金观望，流入一般)
- News Sentiment: 65.0/100 (消息面偏正面)

Sentiment Trend: IMPROVING (+4.0 from yesterday)

Interpretation:
市场情绪偏乐观，成交活跃，资金流入积极。
技术面呈多头排列，短期可适当参与。
但需注意情绪是否过热，建议控制仓位。

Risk Level: MEDIUM
```

**Acceptance Criteria**:
- ✅ Overall sentiment score (0-100)
- ✅ Classification (panic/neutral/optimistic)
- ✅ Component scores with explanations
- ✅ Trend analysis vs previous day
- ✅ Chinese interpretation
- ✅ Risk level assessment

---

### Scenario 4: News Analysis

**User**: "Show me today's important stock market news"

**Expected Response**:
```
Top Financial News - 2025-09-30

1. [9.5/10] 央行宣布降准0.5个百分点 释放流动性约1.2万亿
   Source: 东方财富 | Published: 16:30
   Sentiment: POSITIVE (0.85)
   Impact: 全市场 | Time Horizon: 中期
   Related: 银行, 房地产
   
2. [8.5/10] 北向资金大幅净流入160亿 创近期新高
   Source: 新浪财经 | Published: 15:45
   Sentiment: POSITIVE (0.78)
   Impact: 全市场 | Time Horizon: 短期
   
3. [7.0/10] 多家券商上调A股年底目标位
   Source: 证券时报 | Published: 14:20
   Sentiment: POSITIVE (0.72)
   Impact: 全市场 | Time Horizon: 中期

Overall News Sentiment: POSITIVE (75% positive, 20% neutral, 5% negative)

Hot Topics:
- 货币政策 (5 articles)
- 北向资金 (3 articles)
- 年底行情 (4 articles)
```

**Acceptance Criteria**:
- ✅ News sorted by importance
- ✅ Sentiment classification shown
- ✅ Source and timestamp included
- ✅ Impact scope and horizon indicated
- ✅ Related sectors/topics identified
- ✅ Overall sentiment aggregated
- ✅ Hot topics identified

---

### Scenario 5: Investment Advice

**User**: "Give me investment advice for the Shanghai market"

**Expected Response**:
```
Investment Recommendation - Shanghai Composite Index
Generated: 2025-09-30 16:00:00 | Valid Until: 2025-10-01 09:30:00

═══════════════════════════════════════════════

MARKET OUTLOOK: BULLISH
OPERATION: CAUTIOUS
POSITION: HALF (40-70%)

═══════════════════════════════════════════════

MULTI-DIMENSIONAL ANALYSIS

Technical Analysis:
短期均线多头排列，MACD金叉，RSI处于正常区间。
技术面偏多，但需注意短期涨幅较大，可能面临回调。

Fundamental Analysis:
涨跌家数比2:1，市场宽度良好。
成交量放大，市场参与度较高。
估值水平合理，PE约15倍。

Sentiment Analysis:
市场情绪指数62.5，处于偏乐观区间。
需注意情绪是否过热，警惕追高风险。

Capital Flow Analysis:
北向资金净流入16亿，外资态度积极。
主力资金小幅流出12亿，观望情绪浓厚。
融资余额上升，杠杆资金活跃。

News Analysis:
央行降准利好，释放流动性1.2万亿。
短期提振市场信心，中期有利于估值修复。

═══════════════════════════════════════════════

RISK ASSESSMENT: MEDIUM RISK

Key Risk Factors:
1. 市场情绪偏高，需警惕回调风险
2. 主力资金流出，缺乏持续性支撑
3. 外部环境仍有不确定性

Risk Warning:
市场短期波动可能加大，建议控制仓位，设置止损。

═══════════════════════════════════════════════

ACTIONABLE STRATEGY

Key Focus Points:
- 关注北向资金动向，持续流入则多头延续
- 留意主力资金是否回流，资金面是关键
- 关注量能是否持续放大，缩量上涨不可持续

Operational Strategy:
建议半仓操作（40-70%），可逢低适当加仓。
重点关注政策受益板块：银行、地产、基建。
短线关注强势板块，波段操作控制风险。
严格止损，破3200点减仓观望。

Confidence: 72.5/100

═══════════════════════════════════════════════

DISCLAIMER:
本建议仅供参考，不构成投资建议。
投资有风险，入市需谨慎。
```

**Acceptance Criteria**:
- ✅ Clear market outlook (bullish/bearish/sideways)
- ✅ Operation suggestion (aggressive/cautious/wait)
- ✅ Position recommendation with percentage
- ✅ Multi-dimensional analysis (technical/fundamental/sentiment/capital/news)
- ✅ Risk assessment with specific factors
- ✅ Risk warnings prominent
- ✅ Actionable focus points
- ✅ Specific operational strategy
- ✅ Confidence score
- ✅ Disclaimer included

---

### Scenario 6: Sector Performance

**User**: "Which sectors are performing best today?"

**Expected Response**:
```
Top Performing Sectors - 2025-09-30

By Change %:
1. 银行 (+2.35%) | Stocks: 42 | Main Inflow: ¥1.2B
   Leaders: 工商银行 (+2.8%), 建设银行 (+2.5%)
   
2. 房地产 (+2.10%) | Stocks: 138 | Main Inflow: ¥850M
   Leaders: 万科A (+3.2%), 保利发展 (+2.9%)
   
3. 保险 (+1.85%) | Stocks: 28 | Main Inflow: ¥420M
   Leaders: 中国平安 (+2.1%), 中国人寿 (+1.9%)

Worst Performing:
1. 医疗器械 (-1.80%) | Main Outflow: -¥650M
2. 半导体 (-1.25%) | Main Outflow: -¥820M
3. 新能源 (-0.95%) | Main Outflow: -¥1.1B

Sector Rotation:
从科技股向金融股轮动，政策利好推动低估值板块反弹。
```

**Acceptance Criteria**:
- ✅ Top sectors by performance
- ✅ Capital flow for each sector
- ✅ Leading stocks identified
- ✅ Worst performers shown
- ✅ Rotation pattern analysis

---

### Scenario 7: Market Overview

**User**: "Give me a quick market overview"

**Expected Response**:
```
Market Overview - 2025-09-30

📊 INDEX QUOTES
上证指数: 3,245.67 (+0.33%)
深证成指: 10,850.23 (+0.45%)
创业板指: 2,234.56 (+0.28%)

📈 MARKET BREADTH
Advancing: 2,800 (56%) | Declining: 2,100 (42%)
Limit Up: 45 | Limit Down: 12
New 60d High: 250 | New 60d Low: 120

💰 CAPITAL FLOWS
North Capital: +¥16B (net inflow)
Main Capital: -¥12B (net outflow)
Margin Balance: ¥1,850B (+¥30B)

😊 SENTIMENT
Index: 62.5/100 (OPTIMISTIC, +4.0)
Trend: IMPROVING
Risk Level: MEDIUM

🔥 HOT SECTORS
Top Gainers: 银行 (+2.35%), 房地产 (+2.10%)
Top Losers: 医疗器械 (-1.80%), 半导体 (-1.25%)

📰 TOP NEWS
1. [9.5] 央行宣布降准0.5个百分点 (POSITIVE)
2. [8.5] 北向资金大幅净流入160亿 (POSITIVE)
3. [7.0] 多家券商上调A股年底目标位 (POSITIVE)

💡 CORE INSIGHT
市场情绪偏乐观，政策利好提振信心。
建议半仓操作，关注银行、地产板块。
控制风险，逢低参与。
```

**Acceptance Criteria**:
- ✅ Quick summary of all key metrics
- ✅ Index quotes
- ✅ Market breadth
- ✅ Capital flows
- ✅ Sentiment index
- ✅ Hot sectors
- ✅ Top news (5 items max)
- ✅ Core insight/recommendation
- ✅ Easy to scan format

---

### Scenario 8: Market Closed / Non-Trading Hours

**User**: "How is the Shanghai index performing today?" (asked at 22:00)

**Expected Response**:
```
Shanghai Composite Index (000001)
⚠️ Market Closed

Latest Data (2025-09-30 15:00:00):
Close: 3,245.67 (+0.33%)
Open: 3,230.50 | High: 3,250.00 | Low: 3,228.00
Volume: 285M lots | Amount: ¥345B

Market Status: Closed
Next Trading Session: 2025-10-01 09:30:00

Note: Data is from the most recent trading session.
For real-time data, please query during trading hours (09:30-15:00).
```

**Acceptance Criteria**:
- ✅ Clear market status indicator
- ✅ Most recent data provided
- ✅ Timestamp shows data age
- ✅ Next trading session indicated
- ✅ No misleading "current" or "today" language

---

## Troubleshooting

### Server Not Connecting

1. **Check Claude Desktop config**:
   - Verify JSON syntax is valid
   - Check file path is correct
   - Restart Claude Desktop after config change

2. **Verify server installation**:
   ```bash
   uvx stock-mcp-server --version
   ```

3. **Check server logs**:
   - macOS: `~/Library/Logs/Claude/mcp-server-stock-mcp.log`
   - Windows: `%APPDATA%\Claude\Logs\mcp-server-stock-mcp.log`

### Slow Response Times

1. **Clear cache** (if response > 10s):
   ```bash
   # Cache stored in ~/.stock-mcp-server/cache.db
   rm ~/.stock-mcp-server/cache.db
   ```

2. **Check network** (data fetching requires internet)

3. **Reduce query scope**:
   - Request fewer indicators at once
   - Limit news results
   - Use simpler analysis depth

### Data Not Up-to-Date

1. **Check market hours**: Data only updates during trading hours (09:30-15:00 CST)
2. **Cache TTL**: Real-time data cached for 5 min, may not be instant
3. **Force refresh**: Ask for different timeframe then query again

## Next Steps

After completing this quickstart:

1. **Explore Advanced Features**:
   - Try different indicator combinations
   - Request detailed analysis depth
   - Query specific sectors
   - Get macro economic data

2. **Customize Queries**:
   - "Calculate RSI with 20-day period"
   - "Show me news about banking sector only"
   - "Give me a detailed investment analysis"

3. **Integrate into Workflow**:
   - Morning: Market overview + sentiment
   - Midday: Check capital flows + news
   - End of day: Technical analysis + advice

4. **Read Full Documentation**:
   - See README.md for complete tool reference
   - Check contracts/ for API specifications
   - Review data-model.md for entity schemas

## Success Criteria

You've successfully completed the quickstart if you can:

- ✅ Get real-time Shanghai index data
- ✅ Calculate and interpret technical indicators
- ✅ View market sentiment analysis
- ✅ See today's financial news
- ✅ Receive investment recommendations
- ✅ Query sector performance
- ✅ Get comprehensive market overview
- ✅ Understand data freshness and market status

**Time to Complete**: ~5 minutes  
**Tools Used**: 7 out of 10 MCP tools  
**Scenarios Covered**: 8 acceptance scenarios from spec

---

**Quickstart Complete!** You're now ready to leverage the Stock MCP Server for comprehensive A-share market analysis through your AI assistant.
