# Implementation Plan: Stock Market Data MCP Server

**Branch**: `001-generate-mcp-server` | **Date**: 2025-09-30 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-generate-mcp-server/spec.md`

## Execution Flow (/plan command scope)
```
1. Load feature spec from Input path
   → SUCCESS: Feature spec loaded
2. Fill Technical Context (scan for NEEDS CLARIFICATION)
   → Project Type: Single project (MCP server)
   → Structure Decision: Python package with MCP tools and resources
3. Fill the Constitution Check section
   → Constitution is template-only, proceeding with standard best practices
4. Evaluate Constitution Check section
   → No violations, standard MCP server architecture
   → Progress: Initial Constitution Check ✓
5. Execute Phase 0 → research.md
   → Research completed on MCP protocol, AKShare, technical indicators
6. Execute Phase 1 → contracts, data-model.md, quickstart.md
   → Design artifacts generated
7. Re-evaluate Constitution Check
   → No new violations
   → Progress: Post-Design Constitution Check ✓
8. Plan Phase 2 → Task generation approach described
9. STOP - Ready for /tasks command ✓
```

**STATUS**: ✅ COMPLETE - Ready for /tasks command

## Summary

This implementation creates a Model Context Protocol (MCP) server that provides comprehensive Chinese A-share stock market data and analysis through 10 core tools. The server enables AI assistants to retrieve real-time market data, calculate 50+ technical indicators, analyze market sentiment, scrape financial news, track capital flows, and generate investment recommendations. The system is designed as a Python package executable via `uvx`, integrating seamlessly with MCP-compatible AI assistants like Claude Desktop.

**Primary Requirement**: Provide AI assistants with comprehensive A-share market analysis capabilities through MCP protocol
**Technical Approach**: Python MCP server using AKShare for data, pandas-ta for indicators, BeautifulSoup for news scraping, SnowNLP for sentiment analysis, with SQLite caching and stdio/SSE transport

## Technical Context

**Language/Version**: Python 3.10+  
**Primary Dependencies**: 
- `mcp` (MCP Python SDK for protocol implementation)
- `akshare` (free financial data API for A-share market data)
- `pandas` + `pandas-ta` (data processing and technical indicators)
- `requests` + `beautifulsoup4` + `lxml` (news scraping)
- `snownlp` + `jieba` (Chinese sentiment analysis and NLP)
- `sqlalchemy` (SQLite cache management)
- `pydantic` (data validation and schemas)
- `loguru` (structured logging)
- `aiohttp` (async HTTP requests)
- `cachetools` (in-memory caching)

**Storage**: SQLite (local cache for historical data, news, and calculations)  
**Testing**: pytest + pytest-cov + pytest-asyncio  
**Target Platform**: Cross-platform (Windows, macOS, Linux) - runs as stdio MCP server  
**Project Type**: Single Python package with MCP server entry point  
**Performance Goals**: 
- Real-time queries < 2s
- Historical data < 3s  
- Technical indicators < 5s
- News scraping < 10s
- Investment advice < 5s
- 10+ concurrent requests

**Constraints**: 
- Must use free data sources (AKShare, public websites)
- Respect robots.txt for web scraping
- 5-min cache for real-time data during trading hours
- 30-min cache for news
- 24-hour cache for historical data

**Scale/Scope**: 
- 10 MCP tools + 10 MCP resources
- 93 functional requirements
- 50+ technical indicators
- 200+ data points tracked
- Support for 400+ sector classifications

## Constitution Check

*Since the project constitution is a template, applying standard software engineering principles:*

**Standard Principles Applied**:
- ✅ **Modularity**: Separate tools, services, resources layers
- ✅ **Testability**: Unit, integration, and contract tests
- ✅ **Documentation**: Comprehensive docs, examples, and quickstart
- ✅ **Error Handling**: Graceful degradation, clear error messages
- ✅ **Performance**: Caching strategy, async operations where beneficial
- ✅ **Maintainability**: Type hints, logging, clear structure

**No Violations Detected**: Standard MCP server architecture follows established patterns

## Project Structure

### Documentation (this feature)
```
specs/001-generate-mcp-server/
├── spec.md              # Feature specification (complete)
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output - technology research
├── data-model.md        # Phase 1 output - entity schemas
├── quickstart.md        # Phase 1 output - getting started guide
├── contracts/           # Phase 1 output - MCP tool/resource contracts
│   ├── tools/           # Tool schemas (10 tools)
│   └── resources/       # Resource schemas (10 resources)
└── tasks.md             # Phase 2 output (/tasks command - NOT YET CREATED)
```

### Source Code (repository root)
```
stock-mcp-server/
├── src/
│   └── stock_mcp_server/
│       ├── __init__.py
│       ├── server.py              # MCP server entry point
│       ├── tools/                 # 10 MCP tool implementations
│       │   ├── __init__.py
│       │   ├── market_data.py     # Tool 1: Market data
│       │   ├── indicators.py      # Tool 2: Technical indicators
│       │   ├── money_flow.py      # Tool 3: Capital flows
│       │   ├── sentiment.py       # Tool 4: Sentiment analysis
│       │   ├── news.py            # Tool 5: News analysis
│       │   ├── sector.py          # Tool 6: Sector data
│       │   ├── macro.py           # Tool 7: Macro data
│       │   ├── special.py         # Tool 8: Special data
│       │   ├── advice.py          # Tool 9: Investment advice
│       │   └── overview.py        # Tool 10: Market overview
│       ├── resources/             # 10 MCP resource implementations
│       │   ├── __init__.py
│       │   └── market_resources.py
│       ├── services/              # Business logic layer
│       │   ├── __init__.py
│       │   ├── akshare_service.py # AKShare data fetching
│       │   ├── news_service.py    # News scraping
│       │   ├── cache_service.py   # Cache management
│       │   ├── indicator_service.py # Indicator calculations
│       │   └── sentiment_service.py # Sentiment calculations
│       ├── models/                # Data models (Pydantic schemas)
│       │   ├── __init__.py
│       │   ├── market.py          # Market data models
│       │   ├── indicators.py      # Indicator models
│       │   ├── news.py            # News models
│       │   └── sentiment.py       # Sentiment models
│       └── utils/                 # Utilities
│           ├── __init__.py
│           ├── logger.py          # Logging setup
│           ├── date_utils.py      # Date helpers
│           └── validators.py      # Input validation
│
├── tests/
│   ├── __init__.py
│   ├── contract/                  # Contract tests (MCP tool/resource schemas)
│   │   ├── test_tools_contract.py
│   │   └── test_resources_contract.py
│   ├── integration/               # Integration tests (end-to-end scenarios)
│   │   ├── test_market_data_flow.py
│   │   ├── test_news_analysis_flow.py
│   │   └── test_investment_advice_flow.py
│   └── unit/                      # Unit tests
│       ├── test_services/
│       ├── test_models/
│       └── test_utils/
│
├── pyproject.toml                 # Project config (PEP 621)
├── uv.lock                        # Dependency lock file
├── README.md                      # User documentation
├── README_EN.md                   # English documentation
├── LICENSE                        # MIT license
├── .gitignore
└── PRD.md                         # Product requirements (reference)
```

**Structure Decision**: Single Python package structure (Option 1) selected because this is a standalone MCP server with no frontend/backend split. The server is organized into clear layers: tools (MCP interface), services (business logic), models (data schemas), and utils (helpers). This follows standard Python package conventions and MCP server patterns.

## Phase 0: Outline & Research

### Research Tasks Completed

1. **MCP Protocol Research**
   - Decision: Use official `mcp` Python SDK
   - Rationale: Official SDK provides standard protocol implementation, handles stdio/SSE transports, tool/resource registration
   - Alternatives: Implement protocol from scratch (rejected: reinventing wheel, error-prone)

2. **Market Data Source Research**
   - Decision: Use AKShare as primary data source
   - Rationale: Free, comprehensive A-share data, actively maintained, no API keys required
   - Alternatives: tushare (requires paid membership), baostock (less comprehensive), yfinance (limited A-share support)

3. **Technical Indicator Library Research**
   - Decision: Use pandas-ta as primary library
   - Rationale: 50+ indicators, pandas integration, actively maintained, extensible
   - Alternatives: ta-lib (C dependency issues), stockstats (limited indicators), manual calculation (time-consuming)

4. **News Scraping Strategy Research**
   - Decision: Use requests + BeautifulSoup4 + lxml
   - Rationale: Standard Python scraping stack, reliable, good documentation
   - Alternatives: Scrapy (overkill for simple scraping), selenium (heavy, slow), newspaper3k (abandoned)
   - Sources: Dongfang Fortune, Sina Finance, Securities Times (public news sites, respect robots.txt)

5. **Sentiment Analysis Research**
   - Decision: Use SnowNLP for Chinese sentiment + optional LLM fallback
   - Rationale: SnowNLP specifically designed for Chinese, lightweight, good for finance domain
   - Alternatives: jieba + custom dictionary (more work), LLM-only (expensive, slow), transformers (heavy)

6. **Caching Strategy Research**
   - Decision: Two-tier caching (in-memory + SQLite)
   - Rationale: Fast in-memory for hot data, persistent SQLite for historical data
   - Implementation: cachetools for in-memory, SQLAlchemy for SQLite
   - TTLs: 5min (real-time), 30min (news), 24hr (historical)

7. **MCP Server Architecture Research**
   - Decision: Async-capable tools with sync fallback
   - Rationale: Some data fetching benefits from async (news scraping), but not all tools need it
   - Pattern: Tools → Services → Data Sources (clean separation of concerns)

**Output**: All technical decisions resolved, no remaining NEEDS CLARIFICATION

## Phase 1: Design & Contracts

### 1. Data Model (data-model.md)

**Core Entities** (from spec requirements):

1. **MarketIndex** - Shanghai Composite Index data
2. **HistoricalPrice** - Historical OHLCV data
3. **TechnicalIndicator** - Calculated indicator values
4. **MarketBreadth** - Market-wide statistics
5. **CapitalFlow** - Money flow tracking
6. **MarketSentiment** - Sentiment calculations
7. **NewsArticle** - Financial news items
8. **Sector** - Sector/industry data
9. **MacroIndicator** - Economic indicators
10. **InvestmentRecommendation** - Generated advice
11. **MarketOverview** - Comprehensive snapshot

### 2. API Contracts (contracts/)

**MCP Tools** (10 tools as defined in PRD):

1. `get_market_data` - Market data retrieval
   - Inputs: data_type, index_code, date, period, adjust
   - Outputs: Real-time/historical/breadth/valuation/turnover data

2. `calculate_indicators` - Technical indicator calculation
   - Inputs: indicators, category, params, period, date range
   - Outputs: Indicator values, signals, recommendations

3. `get_money_flow` - Capital flow tracking
   - Inputs: date, flow_type
   - Outputs: North/margin/main capital flows

4. `get_sentiment_analysis` - Sentiment calculation
   - Inputs: date, dimension, days, include_trend
   - Outputs: Sentiment index, breakdown, trends

5. `get_news` - News retrieval and analysis
   - Inputs: limit, category, importance, include_sentiment, include_hot_topics
   - Outputs: News list, sentiment, hot topics

6. `get_sector_data` - Sector performance
   - Inputs: sector_type, sort_by, limit, include_rotation, include_leaders
   - Outputs: Sector rankings, rotation analysis, leaders

7. `get_macro_data` - Macroeconomic data
   - Inputs: data_type, indicators, markets, period, include_impact
   - Outputs: Macro indicators, global markets, impact analysis

8. `get_special_data` - Special market data
   - Inputs: data_type, contract, underlying, sort_by, limit
   - Outputs: Dragon-Tiger List, block trades, IPOs, etc.

9. `generate_advice` - Investment recommendations
   - Inputs: analysis_depth, focus_area, include_risk, include_backtest
   - Outputs: Outlook, suggestions, position, risk assessment

10. `get_market_overview` - Comprehensive snapshot
    - Inputs: date, include_details
    - Outputs: Index, breadth, flows, sentiment, sectors, news

**MCP Resources** (10 read-only resources):

1. `market://summary/{date}` - Market summary
2. `market://analysis/technical/{date}` - Technical analysis report
3. `market://sentiment/{date}` - Sentiment report
4. `market://briefing/{date}` - Daily briefing
5. `market://news/{date}` - News digest
6. `market://moneyflow/{date}` - Money flow report
7. `market://sectors/heatmap/{date}` - Sector heatmap
8. `market://indicators/all/{date}` - All indicators
9. `market://risk/{date}` - Risk assessment
10. `market://macro/calendar` - Economic calendar

### 3. Contract Tests Generated

Tests created for each tool and resource to verify:
- Input schema validation
- Output schema compliance
- Error handling
- Required vs optional parameters
- Data type correctness

### 4. Quickstart Scenario

**User Story**: AI assistant user queries Shanghai index performance, gets comprehensive analysis

**Steps**:
1. Install: `uvx stock-mcp-server`
2. Configure Claude Desktop with MCP server
3. Ask: "How is the Shanghai index performing today?"
4. Receive: Real-time price, change %, volume, market breadth
5. Follow up: "Show me technical indicators"
6. Receive: MA, RSI, MACD with buy/sell signals
7. Ask: "What's the market sentiment?"
8. Receive: Sentiment index, breakdown, interpretation
9. Request: "Give me investment advice"
10. Receive: Multi-dimensional analysis with recommendations

### 5. Agent Context File Update

Running agent context update script to maintain cursor context...

**Output**: data-model.md, contracts/, quickstart.md created with comprehensive specifications

## Phase 2: Task Planning Approach

*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:

1. **Load base template**: `.specify/templates/tasks-template.md`

2. **Generate from Phase 1 artifacts**:
   - Each tool contract → tool implementation task + contract test task
   - Each resource → resource implementation task + contract test task
   - Each entity → model creation task with Pydantic schema
   - Each service → service implementation task
   - Each user scenario → integration test task

3. **Task Categories**:
   - **P0 Foundation** (parallel where possible):
     - Project setup (pyproject.toml, dependencies)
     - Logging and utilities setup
     - Data models (11 Pydantic schemas)
     - Cache service setup
   
   - **P0 Services** (some parallel):
     - AKShare service implementation
     - News scraper service
     - Indicator calculation service
     - Sentiment calculation service
   
   - **P0 MCP Tools** (can parallelize after services):
     - 10 tool implementations (market_data, indicators, etc.)
     - Tool contract tests (10 test files)
   
   - **P0 MCP Resources**:
     - Resource provider implementation
     - 10 resource handlers
     - Resource contract tests
   
   - **P0 Integration**:
     - MCP server setup
     - Tool/resource registration
     - Integration tests (8 scenarios from spec)
   
   - **P1 Documentation**:
     - README with examples
     - API documentation
     - Configuration guide

4. **Ordering Strategy**:
   - **TDD Order**: Contract tests → Implementation → Integration tests
   - **Dependency Order**: Models → Services → Tools/Resources → Server → Integration
   - **Parallelization**: Mark independent tasks with [P] flag
     - All model tasks can run in parallel
     - Service tasks can partially parallel (AKShare service first)
     - Tool implementations can parallel after services complete

5. **Estimated Task Breakdown**:
   - Setup & Infrastructure: ~5 tasks
   - Data Models: ~11 tasks (parallel)
   - Services: ~5 tasks (partially parallel)
   - MCP Tools: ~20 tasks (10 tools × 2 for impl + tests)
   - MCP Resources: ~11 tasks (10 resources + provider)
   - MCP Server: ~3 tasks
   - Integration Tests: ~8 tasks
   - Documentation: ~3 tasks
   - **Total**: ~65-70 tasks

6. **Task Template Format**:
   ```markdown
   ### Task N: [Task Name] [P]
   **Type**: [Contract Test | Implementation | Integration Test | Documentation]
   **Dependencies**: Task M, Task K
   **Files**: 
   - Create: path/to/new/file.py
   - Modify: path/to/existing/file.py
   **Acceptance**: 
   - [ ] Criteria 1
   - [ ] Criteria 2
   ```

**IMPORTANT**: Phase 2 execution (actual tasks.md creation) happens via /tasks command

## Phase 3+: Future Implementation

*These phases are beyond the scope of the /plan command*

**Phase 3**: Task execution
- /tasks command will generate tasks.md with 65-70 ordered tasks
- Tasks follow TDD: tests first, then implementation
- Track progress in tasks.md

**Phase 4**: Implementation
- Execute tasks in order respecting dependencies
- Run tests continuously (red-green-refactor)
- Update documentation as features complete

**Phase 5**: Validation
- Run full test suite (contract + integration + unit)
- Execute quickstart.md end-to-end
- Performance validation against requirements (2s, 5s targets)
- Package and publish to PyPI

## Complexity Tracking

*No constitutional violations requiring justification*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | No violations | Standard MCP server architecture |

## Progress Tracking

**Phase Status**:
- [x] Phase 0: Research complete (/plan command) ✅
- [x] Phase 1: Design complete (/plan command) ✅
- [x] Phase 2: Task planning approach described (/plan command) ✅
- [ ] Phase 3: Tasks generated (/tasks command) - NEXT STEP
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:
- [x] Initial Constitution Check: PASS ✅
- [x] Post-Design Constitution Check: PASS ✅
- [x] All NEEDS CLARIFICATION resolved ✅
- [x] Complexity deviations documented ✅

---
*Plan completed 2025-09-30 - Ready for /tasks command*