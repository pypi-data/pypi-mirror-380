# Stock MCP Server

[![Version](https://img.shields.io/badge/version-0.0.1-blue.svg)](https://pypi.org/project/stock-mcp-server/)
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**Comprehensive Chinese A-Share market data and analysis for AI assistants via MCP**

Stock MCP Server is a [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that enables AI assistants like Claude Desktop to access real-time stock data, technical indicators, market sentiment, news analysis, and more for the Chinese A-share market. Provides 10 powerful tools and 10 resource endpoints with 50+ technical indicators, comprehensive market analysis, and investment advisory generation.

[中文文档](README.md) | [API Documentation](docs/api.md)

## ✨ Key Features

### 📊 10 Powerful MCP Tools

1. **`get_market_data`** - Market Data Query
   - Real-time quotes (OHLC, volume, change %)
   - Historical K-line data
   - Market breadth statistics (advancing/declining, limit moves)
   - Valuation metrics (PE, PB, market cap)

2. **`calculate_indicators`** - Technical Indicators (50+ indicators)
   - Trend: MA, EMA, MACD, DMI, ADX, TRIX, Aroon, CCI, SAR, Ichimoku
   - Momentum: RSI, KDJ, Stochastic, Williams %R, ROC
   - Volatility: BOLL, ATR, Keltner, Donchian
   - Volume: OBV, MFI, CMF, VWAP, AD Line

3. **`get_money_flow`** - Capital Flow Tracking
   - Northbound capital (Stock Connect)
   - Margin trading data
   - Main capital flow (super large/large/medium/small orders)

4. **`get_sentiment_analysis`** - Market Sentiment Analysis
   - Multi-dimensional sentiment index (0-100)
   - Five dimensions: volume, price, volatility, capital, news
   - Sentiment trend analysis
   - Risk level assessment

5. **`get_news`** - Financial News Scraping & Analysis
   - 4 major news sources: Eastmoney, Sina Finance, Securities Times, 21 Finance
   - Intelligent importance scoring
   - Chinese sentiment analysis (SnowNLP)
   - Hot topics aggregation

6. **`get_sector_data`** - Sector Performance Analysis
   - 400+ sector classifications (industry, concept, region, style)
   - Sector capital flows
   - Sector rotation analysis
   - Leading stocks identification

7. **`get_macro_data`** - Macroeconomic Data
   - Domestic indicators (GDP, CPI, PPI, PMI, M0/M1/M2)
   - International markets (US stocks, commodities, forex)
   - A-share impact analysis

8. **`get_special_data`** - Special Market Data
   - Dragon-Tiger List (institutional/retail seats)
   - Block trades
   - Lock-up expirations
   - IPO data
   - Futures & options (optional)

9. **`generate_advice`** - Investment Advisory Generation
   - Multi-dimensional analysis (technical, fundamental, sentiment, capital, news)
   - Market outlook (bullish/bearish/sideways)
   - Operation suggestion (aggressive/cautious/wait)
   - Position recommendation (heavy/half/light/empty + percentage)
   - Risk assessment and warnings
   - Actionable strategy

10. **`get_market_overview`** - Comprehensive Market Overview
    - Index quotes summary
    - Market breadth statistics
    - Capital flow overview
    - Sentiment index
    - Hot sectors
    - Top 5 important news
    - Core market insight

### 🎯 10 Resource Endpoints

Quick access to pre-generated analysis reports (via URI):

1. **`market://summary/{date}`** - Market Summary
2. **`market://analysis/technical/{date}`** - Technical Analysis Report
3. **`market://sentiment/{date}`** - Sentiment Analysis Report
4. **`market://briefing/{date}`** - Daily Briefing
5. **`market://news/{date}`** - News Digest
6. **`market://moneyflow/{date}`** - Money Flow Report
7. **`market://sectors/heatmap/{date}`** - Sector Heatmap
8. **`market://indicators/all/{date}`** - Market Indicators Aggregation
9. **`market://risk/{date}`** - Risk Assessment Report
10. **`market://macro/calendar`** - Macroeconomic Calendar

## 🚀 Quick Start

### Installation

#### Option 1: Run with uvx (Recommended)

No installation needed, just run:

```bash
uvx stock-mcp-server
```

#### Option 2: Install with pip

```bash
pip install stock-mcp-server
stock-mcp-server
```

#### Option 3: Development Setup

```bash
git clone https://github.com/yourusername/stock-mcp-server.git
cd stock-mcp-server
uv sync
uv run stock-mcp-server
```

### Configure Claude Desktop

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

**For development mode**:

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

**Restart Claude Desktop** after configuration.

### Verify Installation

Ask in Claude Desktop:

```
How is the Shanghai Composite Index performing today?
```

Expected response includes:
- ✅ Real-time price and change %
- ✅ OHLC data
- ✅ Volume and amount
- ✅ Market breadth statistics
- ✅ Data timestamp

## 📖 Usage Examples

### Example 1: Real-time Quote Query

**Question**:
```
What's the Shanghai index at now?
```

**AI Response**:
```
Shanghai Composite Index (000001)
Current: 3,245.67 (+0.33% ↑)
Open: 3,230.50 | High: 3,250.00 | Low: 3,228.00
Volume: 285M lots | Amount: ¥345B

Market Breadth:
- Advancing: 2,800 stocks (56%)
- Declining: 2,100 stocks (42%)
- Limit Up: 45 | Limit Down: 12

Trading Status: Closed (15:00)
Data Time: 2025-10-01 15:00:00
```

### Example 2: Technical Indicators

**Question**:
```
Show me technical indicators for the Shanghai index
```

**AI Response**:
```
Shanghai Composite Technical Indicators

Trend Indicators:
- MA5: 3,240.50 | MA10: 3,235.00 | MA20: 3,230.00 | MA60: 3,220.00
  Signal: BUY (Short-term MA crossing above medium-term MA, bullish alignment)

- MACD: DIF=5.23 | DEA=3.45 | MACD=1.78
  Signal: BUY (Golden cross, DIF crossing above DEA)

Momentum Indicators:
- RSI(6): 65.5 | RSI(12): 62.3 | RSI(24): 58.7
  Signal: NEUTRAL (Within normal range, no overbought/oversold)

- KDJ: K=75.3 | D=68.2 | J=89.5
  Signal: NEUTRAL (J value high, watch for pullback risk)

Volatility Indicators:
- Bollinger Bands: Upper=3,260 | Middle=3,230 | Lower=3,200
  Signal: NEUTRAL (Price near middle band)

Overall Signal: BUY (7/10 indicators bullish)
```

### Example 3: Investment Advice

**Question**:
```
Give me investment advice for the Shanghai market
```

**AI Response**:
```
Investment Recommendation - Shanghai Composite Index
Generated: 2025-10-01 16:00:00 | Valid Until: 2025-10-02 09:30:00

═══════════════════════════════════════════════

MARKET OUTLOOK: BULLISH
OPERATION: CAUTIOUS
POSITION: HALF (40-70%)

═══════════════════════════════════════════════

MULTI-DIMENSIONAL ANALYSIS

Technical Analysis:
Short-term MA in bullish alignment, MACD golden cross, RSI in normal range.
Technical side is bullish, but watch for pullback after recent gains.

Fundamental Analysis:
Advancing/declining ratio 2:1, good market breadth.
Volume expanding, high market participation.
Valuation reasonable, PE around 15x.

Sentiment Analysis:
Market sentiment index 62.5, in optimistic zone.
Watch for overheating, caution against chasing highs.

Capital Flow:
Northbound capital net inflow ¥16B, positive foreign attitude.
Main capital slight outflow ¥12B, cautious sentiment.
Margin balance rising, leveraged capital active.

News Analysis:
PBOC reserve cut positive, releasing ¥1.2T liquidity.
Short-term boosts market confidence, medium-term supports valuation repair.

═══════════════════════════════════════════════

RISK ASSESSMENT: MEDIUM RISK

Key Risk Factors:
1. Market sentiment elevated, watch for pullback risk
2. Main capital outflow, lacks sustained support
3. External environment still uncertain

Risk Warning:
Market volatility may increase in short term. Suggest controlling position and setting stop-loss.

═══════════════════════════════════════════════

ACTIONABLE STRATEGY

Key Focus Points:
- Watch northbound capital trend, continued inflow sustains bullish move
- Monitor main capital return, capital flow is key
- Watch volume sustainability, rally on declining volume unsustainable

Operational Strategy:
Suggest half position (40-70%), can add on dips moderately.
Focus on policy-benefited sectors: banks, real estate, infrastructure.
Short-term focus on strong sectors, swing trading to control risk.
Strict stop-loss, reduce position if breaks 3,200.

Confidence: 72.5/100

═══════════════════════════════════════════════

DISCLAIMER:
This advice is for reference only and does not constitute investment advice.
Investment involves risks. Trade with caution.
```

## 🛠️ Advanced Usage

### Custom Indicator Parameters

```
Calculate 20-day RSI and MACD (fast 12, slow 26) for Shanghai index
```

### Filter Important News

```
Show me policy news with importance score above 8
```

### Detailed Investment Analysis

```
Give me a detailed investment analysis report with backtest results
```

### Specific Sector Query

```
Show capital flow and leading stocks for medical equipment sector
```

### Macro Data Query

```
Display latest GDP, CPI and PMI data
```

## 📊 Performance Metrics

| Tool | Target Response Time | Typical Response Time |
|------|---------------------|----------------------|
| get_market_data | <2s | ~500ms |
| calculate_indicators | <5s | ~2s |
| get_money_flow | <2s | ~500ms |
| get_sentiment_analysis | <3s | ~1.5s |
| get_news | <10s | ~5s |
| get_sector_data | <3s | ~1s |
| get_macro_data | <3s | ~1s |
| get_special_data | <3s | ~1s |
| generate_advice | <5s | ~3s |
| get_market_overview | <3s | ~2s |

### Caching Strategy

- **Real-time data**: 5-minute cache during trading hours, 24-hour cache after market close
- **Historical data**: 24-hour cache
- **News data**: 30-minute cache
- **Technical indicators**: 30-minute cache
- **Sentiment analysis**: 1-hour cache

### Concurrent Support

- Supports **10+ concurrent requests**
- Intelligent request queue management
- Multi-source automatic fallback (Eastmoney → Tencent Finance → Sina Finance)

## 🔧 Configuration Options

### Environment Variables

```bash
# Log level
STOCK_MCP_LOG_LEVEL=INFO  # DEBUG | INFO | WARNING | ERROR

# Cache directory
STOCK_MCP_CACHE_DIR=~/.stock-mcp-server/

# Data refresh intervals (seconds)
STOCK_MCP_REALTIME_REFRESH=300  # 5 minutes
STOCK_MCP_NEWS_REFRESH=1800     # 30 minutes
```

### Configuration File

Create `config.yaml`:

```yaml
logging:
  level: INFO
  dir: ~/.stock-mcp-server/logs

cache:
  db_path: ~/.stock-mcp-server/cache.db
  ttl:
    realtime: 300      # 5 minutes
    historical: 86400  # 24 hours
    news: 1800         # 30 minutes
    indicators: 1800   # 30 minutes

data_sources:
  news:
    - eastmoney
    - sina
    - stcn
    - 21finance
  
sentiment:
  method: snownlp  # snownlp | llm
  weights:
    volume: 0.25
    price: 0.25
    volatility: 0.15
    capital: 0.20
    news: 0.15
```

## 🐛 Troubleshooting

### Server Not Connecting

1. **Check Claude Desktop config**
   - Verify JSON syntax is valid
   - Check file path is correct
   - Restart Claude Desktop after config change

2. **Verify server installation**
```bash
   uvx stock-mcp-server --version
   ```

3. **Check logs**
   - macOS: `~/Library/Logs/Claude/mcp-server-stock-mcp.log`
   - Windows: `%APPDATA%\Claude\Logs\mcp-server-stock-mcp.log`
   - Local: `~/.stock-mcp-server/logs/`

### Slow Response Times

1. **Clear cache** (if response > 10s)
```bash
   rm ~/.stock-mcp-server/cache.db
   ```

2. **Check network** (data fetching requires internet)

3. **Reduce query scope**
   - Request fewer indicators at once
   - Limit news results
   - Use simpler analysis depth

### Data Not Up-to-Date

1. **Check trading hours**: Data only updates during trading hours (09:30-15:00 CST)
2. **Cache TTL**: Real-time data cached for 5 min, not absolutely real-time
3. **Force refresh**: Query different timeframe then query again

### Proxy Issues

If encountering connection issues, the server automatically bypasses proxies for domestic data sources. To manually configure:

```bash
# Disable proxy
unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy
```

## 📚 Glossary

| Chinese Term | English | Code/Note |
|-------------|---------|-----------|
| 上证指数 | Shanghai Composite Index | 000001 |
| 深证成指 | Shenzhen Component Index | 399001 |
| 创业板指 | ChiNext Index | 399006 |
| 北向资金 | Northbound Capital | Via Stock Connect |
| 融资融券 | Margin Trading | Financing & short selling |
| 主力资金 | Main Capital | Large & super large orders |
| 涨跌停 | Limit Up/Down | Usually ±10% for A-shares |
| 龙虎榜 | Dragon-Tiger List | Unusual trading activity |

### Technical Indicator Acronyms

- **MA**: Moving Average
- **EMA**: Exponential Moving Average
- **MACD**: Moving Average Convergence Divergence
- **RSI**: Relative Strength Index
- **KDJ**: Stochastic Oscillator
- **BOLL**: Bollinger Bands
- **ATR**: Average True Range
- **OBV**: On-Balance Volume
- **MFI**: Money Flow Index

## 🤝 Contributing

Contributions welcome! Please submit Issues and Pull Requests.

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add some amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details

## ⚠️ Disclaimer

**Important Notice**:

1. All data, analysis, and advice provided by this tool are **for reference only** and do not constitute investment advice
2. Investment involves risks. Trade with caution. Users bear all risks from investment decisions made using this tool
3. Data sourced from third parties (AKShare, etc.), accuracy and timeliness not guaranteed
4. Technical indicators and sentiment analysis based on historical data, not representative of future performance
5. Author not responsible for any losses incurred from using this tool

Please exercise caution and fully understand the risks before making any investment decisions.

## 🔗 Related Links

- [MCP Protocol Website](https://modelcontextprotocol.io)
- [Claude Desktop](https://claude.ai/desktop)
- [AKShare Documentation](https://akshare.akfamily.xyz/)
- [API Documentation](docs/api.md)

## 📞 Support

- Issue reporting: [GitHub Issues](https://github.com/yourusername/stock-mcp-server/issues)
- Discussions: [GitHub Discussions](https://github.com/yourusername/stock-mcp-server/discussions)

---

**Happy Trading!** 📈✨
