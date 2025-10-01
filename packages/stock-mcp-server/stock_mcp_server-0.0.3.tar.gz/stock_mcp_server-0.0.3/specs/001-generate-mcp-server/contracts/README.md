# MCP Contracts: Stock Market Data Server

This directory contains the contract specifications for all MCP tools and resources provided by the Stock MCP Server.

## Overview

The Stock MCP Server exposes:
- **10 Tools**: Interactive operations for querying and analyzing market data
- **10 Resources**: Read-only data resources at specific URIs

## Tools Directory

Contains JSON schemas for each of the 10 tools:
1. `get_market_data` - Market data retrieval (real-time, historical, breadth, valuation)
2. `calculate_indicators` - Technical indicator calculations (50+ indicators)
3. `get_money_flow` - Capital flow tracking (northbound, margin, main)
4. `get_sentiment_analysis` - Market sentiment analysis
5. `get_news` - News retrieval and sentiment analysis
6. `get_sector_data` - Sector performance data
7. `get_macro_data` - Macroeconomic indicators
8. `get_special_data` - Special market data (Dragon-Tiger, block trades, IPOs)
9. `generate_advice` - Investment recommendation generation
10. `get_market_overview` - Comprehensive market snapshot

## Resources Directory

Contains URI schemas for each of the 10 resources:
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

## Contract Testing

Each contract has corresponding tests in `/tests/contract/` to verify:
- Input schema validation
- Output schema compliance
- Required vs optional parameters
- Error handling
- Data type correctness

Tests must **fail** before implementation (TDD approach).

## Schema Format

All contracts follow MCP protocol specification:
- Tools use JSON Schema for input parameters
- Resources use URI templates with path/query parameters
- Responses follow standardized formats with metadata
