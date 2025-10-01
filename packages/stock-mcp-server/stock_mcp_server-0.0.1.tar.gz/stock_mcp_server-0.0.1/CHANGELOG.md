# Changelog

All notable changes to Stock MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2025-10-01

### Added
- Initial release of Stock MCP Server
- 10 MCP tools for comprehensive A-share market analysis:
  - `get_market_data` - Real-time and historical market data
  - `calculate_indicators` - 50+ technical indicators with signals
  - `get_money_flow` - Capital flow tracking (northbound, margin, main)
  - `get_sentiment_analysis` - Multi-dimensional sentiment index
  - `get_news` - Financial news scraping with sentiment analysis
  - `get_sector_data` - Sector performance and rotation analysis
  - `get_macro_data` - Macroeconomic indicators and global markets
  - `get_special_data` - Dragon-Tiger List, block trades, IPOs, derivatives
  - `generate_advice` - Investment advisory with multi-dimensional analysis
  - `get_market_overview` - Comprehensive market snapshot

- 10 MCP resources for quick access to pre-generated reports:
  - `market://summary/{date}` - Market summary
  - `market://analysis/technical/{date}` - Technical analysis report
  - `market://sentiment/{date}` - Sentiment analysis report
  - `market://briefing/{date}` - Daily briefing
  - `market://news/{date}` - News digest
  - `market://moneyflow/{date}` - Money flow report
  - `market://sectors/heatmap/{date}` - Sector heatmap
  - `market://indicators/all/{date}` - Market indicators aggregation
  - `market://risk/{date}` - Risk assessment report
  - `market://macro/calendar` - Macroeconomic calendar

- Core features:
  - Multi-source data fetching with automatic fallback (Eastmoney → Tencent → Sina)
  - Two-tier caching system (in-memory + SQLite) for optimal performance
  - Anti-crawler measures with realistic User-Agent and rate limiting
  - Proxy bypass for domestic data sources
  - Comprehensive error handling with graceful degradation
  - Structured logging with loguru
  - Type-safe implementation with Pydantic models
  - Support for 50+ technical indicators across 4 categories
  - Chinese sentiment analysis with SnowNLP
  - News scraping from 4 major sources
  - 400+ sector classifications

- Performance optimizations:
  - Real-time queries <2s
  - Historical data <3s
  - Technical indicators <5s
  - News scraping <10s
  - 10+ concurrent requests support
  - Smart cache TTL strategy (5min-24hr)

- Testing:
  - 64 tasks across 8 phases
  - Contract tests for all 10 tools
  - Integration tests for 8 end-to-end scenarios
  - Unit tests for models and services
  - Test coverage >80%

- Documentation:
  - Comprehensive README (Chinese and English)
  - Quick start guide with 8 usage scenarios
  - API documentation
  - Troubleshooting guide
  - Terminology glossary
  - Configuration examples

### Security
- Environment-based configuration
- No hardcoded API keys or credentials
- Safe error messages (no sensitive data exposure)
- Secure cache storage

### Known Issues
- Market breadth data may be temporarily unavailable due to rate limiting from data sources
- This is expected behavior with fallback mechanisms in place

### Migration Guide
- First release, no migration needed

---

## Release Notes Format

### Version Numbering
- **Major.Minor.Patch** (e.g., 1.0.0)
- **Major**: Breaking changes to API or architecture
- **Minor**: New features, backwards compatible
- **Patch**: Bug fixes, backwards compatible

### Version 0.0.x
- Pre-release versions for initial testing
- API may change without notice
- Use with caution in production

[0.0.1]: https://github.com/yourusername/stock-mcp-server/releases/tag/v0.0.1

