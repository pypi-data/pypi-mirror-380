# Feature Specification: Stock Market Data MCP Server

**Feature Branch**: `001-generate-mcp-server`  
**Created**: 2025-09-30  
**Status**: Draft  
**Input**: User description: "Generate MCP server for Chinese A-share stock market data and analysis based on PRD"

## Execution Flow (main)
```
1. Parse user description from Input
   → SUCCESS: Feature description parsed from PRD
2. Extract key concepts from description
   → Identified: AI assistants, stock data retrieval, market analysis, investment insights
3. For each unclear aspect:
   → No major ambiguities - PRD is comprehensive
4. Fill User Scenarios & Testing section
   → SUCCESS: Multiple user flows identified
5. Generate Functional Requirements
   → SUCCESS: 90+ testable requirements extracted
6. Identify Key Entities
   → SUCCESS: Market data, indicators, news, sentiment entities identified
7. Run Review Checklist
   → SUCCESS: No implementation details in spec
8. Return: SUCCESS (spec ready for planning)
```

---

## ⚡ Quick Guidelines
- ✅ Focus on WHAT users need and WHY
- ❌ Avoid HOW to implement (no tech stack, APIs, code structure)
- 👥 Written for business stakeholders, not developers

---

## User Scenarios & Testing *(mandatory)*

### Primary User Story
An AI assistant user wants to get real-time Chinese A-share market insights through natural conversation. They ask questions like "How is the Shanghai index performing today?" or "What's the market sentiment?" and receive comprehensive analysis including current prices, technical indicators, news sentiment, and actionable investment recommendations.

### Acceptance Scenarios

1. **Given** an AI assistant with MCP support, **When** a user asks about current Shanghai index performance, **Then** the system provides real-time price data, change percentage, trading volume, and market breadth statistics

2. **Given** current market data is available, **When** a user requests technical analysis, **Then** the system calculates and returns relevant indicators (moving averages, RSI, MACD, etc.) with clear buy/sell/hold signals

3. **Given** market news is being monitored, **When** a user asks for today's important news, **Then** the system provides categorized news with sentiment analysis and impact assessment

4. **Given** all data sources are available, **When** a user requests investment advice, **Then** the system generates multi-dimensional analysis (technical, fundamental, sentiment, capital flow) with specific recommendations and risk warnings

5. **Given** a user wants to track specific sectors, **When** they request sector performance data, **Then** the system shows ranking by performance, capital flow, and identifies leading stocks

6. **Given** market is closed, **When** a user requests data, **Then** the system provides the most recent available data with clear timestamp indicating data age

7. **Given** multiple data queries in sequence, **When** a user makes repeated requests, **Then** the system uses cached data appropriately to maintain quick response times

8. **Given** market data shows extreme conditions, **When** generating advice, **Then** the system includes prominent risk warnings about market volatility or unusual conditions

### Edge Cases

- What happens when data sources are temporarily unavailable?
  - System should provide cached data with clear staleness indicators
  - System should gracefully degrade and explain which features are unavailable
  
- How does system handle malformed or invalid date requests?
  - System should validate date inputs and provide helpful error messages
  - System should suggest valid date ranges
  
- What happens during market holidays or non-trading hours?
  - System should clearly indicate market status
  - System should provide last trading day's data
  
- How does system handle concurrent requests from multiple AI assistants?
  - System should handle at least 10 concurrent requests without degradation
  - System should use caching to minimize redundant data fetching
  
- What happens when news scraping fails or is blocked?
  - System should continue operating with other features
  - System should log errors for monitoring
  
- How does system handle extremely volatile market days (circuit breakers)?
  - System should flag unusual market conditions
  - System should adjust sentiment calculations accordingly


## Requirements *(mandatory)*

### Functional Requirements - Market Data

- **FR-001**: System MUST provide real-time Shanghai Composite Index data including current price, open, high, low, close, volume, and change percentage
- **FR-002**: System MUST provide historical K-line data for multiple timeframes (daily, weekly, monthly, 5min, 15min, 30min, 60min)
- **FR-003**: System MUST calculate and provide market breadth metrics (stock count-based): number of advancing/declining stocks, stocks hitting limit up/down, and stocks making new highs/lows
- **FR-004**: System MUST provide market turnover analysis (order flow-based): capital flows categorized by order size (super large/large/medium/small orders)
- **FR-005**: System MUST provide market valuation metrics including weighted average P/E, P/B ratios, dividend yield, and total market capitalization
- **FR-006**: System MUST support data queries by date with appropriate validation and error handling

### Functional Requirements - Technical Analysis

- **FR-007**: System MUST calculate at least 50 technical indicators across trend, momentum, volatility, and volume categories (see contracts/tools/calculate_indicators.json for complete enumeration)
- **FR-008**: System MUST provide trend indicators including multiple types of moving averages (SMA, EMA, WMA), MACD, DMI/ADX, and Ichimoku Cloud
- **FR-009**: System MUST provide momentum indicators including RSI, KDJ, Stochastic oscillator, Williams %R, and ROC
- **FR-010**: System MUST provide volatility indicators including Bollinger Bands, ATR, Keltner Channel, and Donchian Channel
- **FR-011**: System MUST provide volume indicators including OBV, MFI, CMF, VWAP, and accumulation/distribution line
- **FR-012**: System MUST generate clear buy/sell/hold signals based on technical indicators (e.g., golden cross, death cross, overbought, oversold)
- **FR-013**: System MUST allow users to specify indicator parameters (periods, sensitivity) when calculating indicators
- **FR-014**: System MUST support calculating indicators for different timeframes (daily, weekly, monthly)

### Functional Requirements - Capital Flow

- **FR-015**: System MUST track northbound capital (Shanghai Connect) including inflows, outflows, and net buying amount
- **FR-016**: System MUST track margin trading data including financing balance, financing buy amount, margin balance, and short selling volume
- **FR-017**: System MUST track main capital flows categorized by order size (super large, large, medium, small orders)
- **FR-018**: System MUST provide capital flow trends over time with historical comparison

### Functional Requirements - Market Sentiment

- **FR-019**: System MUST calculate a comprehensive market sentiment index (0-100 scale) based on multiple dimensions with documented weights (see data-model.md for calculation formula: volume 25%, price 35%, volatility 15%, capital 15%, news 10%)
- **FR-020**: System MUST provide sentiment classification (extreme panic, panic, neutral, optimistic, extreme optimism)
- **FR-021**: System MUST analyze volume sentiment through comparison with historical averages
- **FR-022**: System MUST analyze price movement sentiment through advancing/declining ratio and limit moves
- **FR-023**: System MUST analyze volatility sentiment through amplitude metrics and VIX-style calculation
- **FR-024**: System MUST track sentiment trends over time to show improving or deteriorating conditions
- **FR-025**: System MUST identify extreme sentiment conditions that may signal market reversals

### Functional Requirements - News Analysis

- **FR-026**: System MUST collect financial news from multiple authoritative Chinese financial media sources (primary sources: Dongfang Fortune, Sina Finance, Securities Times - see plan.md research section)
- **FR-027**: System MUST categorize news by type (policy, market, company, industry, international)
- **FR-028**: System MUST perform sentiment analysis on news content to determine positive/neutral/negative tone
- **FR-029**: System MUST assign importance scores (0-10) to news items
- **FR-030**: System MUST identify and aggregate related news items into common topics
- **FR-031**: System MUST provide news digest with configurable number of items to return
- **FR-032**: System MUST include news publication timestamp and source attribution
- **FR-033**: System MUST filter news by minimum importance threshold when requested

### Functional Requirements - Sector Analysis

- **FR-034**: System MUST provide performance data for industry sectors (SW Level 1 industries - 28 sectors)
- **FR-035**: System MUST provide performance data for concept sectors (200+ market concepts)
- **FR-036**: System MUST provide performance data for regional sectors (provinces and cities)
- **FR-037**: System MUST provide performance data for style sectors (large/mid/small cap, value/growth)
- **FR-038**: System MUST identify leading stocks in each sector
- **FR-039**: System MUST support sorting sectors by performance, turnover, or capital flow
- **FR-040**: System MUST analyze sector rotation patterns over specified time periods

### Functional Requirements - Macroeconomic Data

- **FR-041**: System MUST provide domestic macroeconomic indicators including GDP growth, industrial production, fixed asset investment, and retail sales
- **FR-042**: System MUST provide price indices including CPI, PPI, and PMI
- **FR-043**: System MUST provide monetary data including M0/M1/M2, social financing, reserve ratio, and LPR
- **FR-044**: System MUST provide international market data including major global stock indices
- **FR-045**: System MUST provide commodity prices including crude oil and gold
- **FR-046**: System MUST provide forex market data including USD index and RMB exchange rate
- **FR-047**: System MUST analyze correlation between macroeconomic indicators and A-share market performance

### Functional Requirements - Special Data

- **FR-048**: System MUST provide Dragon-Tiger List (trading disclosure) data including stocks on the list, institutional/retail trading
- **FR-049**: System MUST provide block trade data including transaction volume and premium/discount rates
- **FR-050**: System MUST provide lock-up expiration data including unlocking market value and share counts
- **FR-051**: System MUST provide IPO data including new listings and first-day performance

### Functional Requirements - Investment Advice

- **FR-052**: System MUST generate investment recommendations based on technical, fundamental, sentiment, and capital flow analysis
- **FR-053**: System MUST provide clear market outlook (bullish/bearish/sideways)
- **FR-054**: System MUST provide operation suggestions (aggressive/cautious/wait-and-see)
- **FR-055**: System MUST provide position recommendations (heavy/half/light/empty)
- **FR-056**: System MUST include prominent risk warnings in all investment advice
- **FR-057**: System MUST identify key focus points and operational strategies
- **FR-058**: System MUST support different analysis depths (simple/normal/detailed)
- **FR-059**: System MUST include disclaimer stating advice is for reference only and not investment guidance

### Functional Requirements - Market Overview

- **FR-060**: System MUST provide quick comprehensive market summary combining all data types
- **FR-061**: System MUST include index quotes, market breadth, capital flows, sentiment index, sector highlights, and top news in overview
- **FR-062**: System MUST present overview data in easy-to-digest format suitable for quick decision making

### Functional Requirements - System Integration

- **FR-063**: System MUST expose all capabilities through Model Context Protocol (MCP) with 10 core tools
- **FR-064**: System MUST provide 10 MCP resources for read-only data access
- **FR-065**: System MUST communicate via standard MCP protocol over stdio or SSE transport
- **FR-066**: System MUST be executable through package runner (uvx) without complex installation
- **FR-067**: System MUST integrate with AI assistants supporting MCP (Claude Desktop, Continue, etc.)

### Functional Requirements - Performance

- **FR-068**: System MUST respond to real-time data queries within 2 seconds
- **FR-069**: System MUST respond to historical data queries within 3 seconds
- **FR-070**: System MUST respond to technical indicator calculations within 5 seconds (full 50+ indicator suite)
- **FR-071**: System MUST respond to news scraping requests within 10 seconds
- **FR-072**: System MUST respond to investment advice generation within 5 seconds (normal depth; detailed depth allows 7 seconds)
- **FR-073**: System MUST handle at least 10 concurrent requests without performance degradation

### Functional Requirements - Caching & Data Management

- **FR-074**: System MUST cache real-time market data for 5 minutes during trading hours
- **FR-075**: System MUST cache news data for 30 minutes
- **FR-076**: System MUST cache historical data for 24 hours
- **FR-077**: System MUST provide data freshness indicators (timestamps) with all responses
- **FR-078**: System MUST automatically retry failed data requests up to 3 times
- **FR-079**: System MUST log all data retrieval operations for monitoring and debugging

### Functional Requirements - Error Handling

- **FR-080**: System MUST provide clear, actionable error messages when operations fail
- **FR-081**: System MUST gracefully degrade when partial data is unavailable
- **FR-082**: System MUST validate all date inputs and provide helpful correction suggestions
- **FR-083**: System MUST handle network failures without crashing
- **FR-084**: System MUST detect and handle data source format changes
- **FR-085**: System MUST continue operating when individual features fail

### Functional Requirements - Data Quality

- **FR-086**: System MUST ensure data accuracy matches source data
- **FR-087**: System MUST detect and handle anomalous data (missing values, outliers)
- **FR-088**: System MUST validate indicator calculation results for correctness
- **FR-089**: System MUST provide data source attribution for transparency

### Functional Requirements - Configuration

- **FR-090**: System MUST support configuring data refresh intervals
- **FR-091**: System MUST support configuring news sources to scrape
- **FR-092**: System MUST support configuring sentiment calculation weights
- **FR-093**: System MUST support environment-based configuration for different deployment scenarios


### Key Entities

*Note: Full entity schemas with validation rules are defined in data-model.md*

- **Market Index**: Represents a stock market index (e.g., Shanghai Composite) with attributes including code, name, current price, open/high/low/close prices, volume, trading value, change amount, change percentage, amplitude, turnover ratio, and timestamp

- **Historical Price**: Represents historical market data for a specific date and timeframe, including OHLCV data (open, high, low, close, volume), and support for different adjustment methods (forward/backward/none)

- **Technical Indicator**: Represents a calculated technical analysis indicator with attributes including indicator type, calculation parameters, calculated values, signal interpretation, and calculation timestamp

- **Market Breadth**: Represents overall market participation metrics including counts of advancing/declining stocks, stocks hitting limit up/down, stocks with various gain/loss thresholds, stocks making new highs/lows, and percentage distributions

- **Capital Flow**: Represents money flow data including northbound capital (Shanghai Connect) flows, margin trading balances and volumes, and main capital flows segmented by order size categories

- **Market Sentiment**: Represents aggregated market sentiment with attributes including overall sentiment score (0-100), sentiment level classification, component dimension scores (volume, price movement, volatility, capital, news), sentiment trend direction, and calculation timestamp

- **News Article**: Represents a financial news item with attributes including title, summary/content, publication timestamp, source, category, related stocks/sectors, importance score, sentiment score (positive/neutral/negative), and tags

- **Sector**: Represents a market sector or industry group with attributes including sector type (industry/concept/region/style), sector name, member stock count, aggregate performance metrics, capital flow, and leading stock identification

- **Macroeconomic Indicator**: Represents a macro economic data point including indicator name, value, period (monthly/quarterly/yearly), release date, year-over-year change, month-over-month change, and historical trend

- **Investment Recommendation**: Represents generated investment advice including market outlook classification, operation suggestion, position recommendation, multi-dimensional analysis results, risk assessment, focus points, operational strategies, generation timestamp, and disclaimer

- **Market Overview**: Represents a comprehensive market snapshot combining key metrics from indices, breadth, flows, sentiment, sectors, and news for quick consumption

---

## Review & Acceptance Checklist
*GATE: Automated checks run during main() execution*

### Content Quality
- [x] No implementation details (languages, frameworks, APIs)
- [x] Focused on user value and business needs
- [x] Written for non-technical stakeholders
- [x] All mandatory sections completed

### Requirement Completeness
- [x] No [NEEDS CLARIFICATION] markers remain
- [x] Requirements are testable and unambiguous  
- [x] Success criteria are measurable
- [x] Scope is clearly bounded
- [x] Dependencies and assumptions identified

---

## Execution Status
*Updated by main() during processing*

- [x] User description parsed
- [x] Key concepts extracted
- [x] Ambiguities marked
- [x] User scenarios defined
- [x] Requirements generated
- [x] Entities identified
- [x] Review checklist passed

---

## Dependencies and Assumptions

### Dependencies
- System depends on external Chinese A-share market data sources being available and stable
- System depends on financial news websites being accessible for scraping
- System depends on AI assistants supporting Model Context Protocol standard
- System depends on Python runtime environment being available (version 3.10+)

### Assumptions
- Users are primarily Chinese-speaking or familiar with Chinese stock market terminology
- Users have AI assistants capable of MCP integration (Claude Desktop, Continue, etc.)
- Market data sources provide free or reasonably-priced access for individual users
- News scraping complies with website terms of service and robots.txt policies
- Users understand investment advice is for reference only and not professional financial guidance
- Trading hours are assumed to be regular Shanghai Stock Exchange hours
- System will be used primarily during Asian business hours when A-share market is active

---

## Success Metrics

### User Value Metrics
- AI assistant users can successfully query market data and receive accurate responses
- Users receive investment insights within acceptable response time limits
- Users report the advice and analysis helps inform their market understanding
- Users find the sentiment analysis accurately reflects market mood

### System Performance Metrics
- 99% of real-time data queries complete within 2 seconds
- 99% of technical indicator calculations complete within 5 seconds
- System handles 10 concurrent requests without degradation
- Data accuracy matches source data with 99.9% consistency
- Cache hit rate exceeds 60% during trading hours (measured over 1-week average during typical market conditions)

### Adoption Metrics
- Successfully integrates with major MCP-compatible AI assistants
- Package can be installed and run via simple uvx command
- Clear documentation enables users to get started within 5 minutes
- System maintains 99% uptime during trading hours

---

## Out of Scope

The following are explicitly NOT included in this feature:

- Individual stock analysis (focus is on Shanghai Index and market-wide metrics)
- Real-time tick-by-tick data streaming
- Order execution or trading capabilities
- Portfolio management features
- Paid data sources requiring subscription fees
- Support for markets outside of Chinese A-shares
- Mobile app or web UI (MCP server only, accessed through AI assistants)
- User authentication or multi-user management
- Automated trading signals or algorithmic trading
- Regulatory compliance for professional investment advisory services
- Storage of user trading history or personal positions
- Social features or community interactions
- Backtesting historical trading strategies
- Machine learning model training on market data

---
