# MCP Resources Summary

Complete list of all 10 resources provided by Stock MCP Server.

Resources are **read-only** data endpoints accessed via URIs. Unlike tools (which are invoked with parameters), resources are fetched directly by URI.

## Resource 1: market-summary
**Contract**: `resources/market-summary.json`  
**URI**: `market://summary/{date}`

Comprehensive market summary with index quotes, breadth, and key statistics.

**Parameters**:
- `{date}`: Trading date (YYYY-MM-DD) or "latest"
- `?include_breadth`: Include detailed breadth (default: true)
- `?include_valuation`: Include valuation metrics (default: false)

**Example**: `market://summary/latest?include_valuation=true`

---

## Resource 2: technical-analysis
**URI**: `market://analysis/technical/{date}`

Technical analysis report with indicators and signals.

**Content**:
- Multiple indicator calculations (MA, MACD, RSI, etc.)
- Overall technical signal (buy/sell/neutral)
- Support/resistance levels
- Trend analysis

**Example**: `market://analysis/technical/2025-09-30`

---

## Resource 3: sentiment-report
**URI**: `market://sentiment/{date}`

Market sentiment analysis report.

**Content**:
- Overall sentiment index (0-100)
- Component breakdowns (volume, price, volatility, capital, news)
- Sentiment trend vs previous days
- Risk level assessment
- Chinese interpretation

**Example**: `market://sentiment/latest`

---

## Resource 4: daily-briefing
**URI**: `market://briefing/{date}`

Comprehensive daily market briefing combining data + news + analysis.

**Content**:
- Market summary (index performance)
- Key news highlights (top 5)
- Technical analysis summary
- Sentiment overview
- Investment suggestion
- Tomorrow's outlook

**Example**: `market://briefing/2025-09-30`

---

## Resource 5: news-digest
**URI**: `market://news/{date}`

Curated news digest with sentiment analysis.

**Parameters**:
- `{date}`: News date or "today"
- `?category`: Filter by category (policy/market/company/industry/international)
- `?importance`: Minimum importance score (0-10)

**Content**:
- Top news by importance
- Sentiment classification
- Hot topics summary
- Overall market impact

**Example**: `market://news/today?category=policy&importance=8`

---

## Resource 6: money-flow-report
**URI**: `market://moneyflow/{date}`

Capital flow analysis report.

**Content**:
- Northbound capital summary
- Margin trading statistics
- Main capital flow breakdown
- 5-day trend comparison
- Flow interpretation

**Example**: `market://moneyflow/2025-09-30`

---

## Resource 7: sector-heatmap
**URI**: `market://sectors/heatmap/{date}`

Sector performance heatmap data.

**Parameters**:
- `{date}`: Trading date or "latest"
- `?type`: Sector type (industry/concept/region/style)

**Content**:
- All sectors with performance %
- Capital flow by sector
- Color-coded heatmap data (JSON)
- Top gainers/losers

**Example**: `market://sectors/heatmap/latest?type=industry`

---

## Resource 8: market-indicators
**URI**: `market://indicators/all/{date}`

All market indicators aggregated.

**Content**:
- Key technical indicators (20+)
- Market breadth indicators
- Sentiment indicators
- Valuation indicators
- Composite signal

**Example**: `market://indicators/all/2025-09-30`

---

## Resource 9: risk-report
**URI**: `market://risk/{date}`

Market risk assessment report.

**Content**:
- Overall risk level (low/medium/high/extreme)
- Risk factors breakdown
- Market extremes detection
- VIX-style volatility index
- Risk warnings
- Suggested hedging strategies

**Example**: `market://risk/latest`

---

## Resource 10: macro-calendar
**URI**: `market://macro/calendar`

Economic calendar with upcoming data releases.

**Parameters**:
- `?start_date`: Calendar start date
- `?end_date`: Calendar end date
- `?importance`: Filter by importance (high/medium/low)

**Content**:
- Upcoming economic data releases
- Central bank meetings
- Policy announcements
- Historical calendar data
- Expected market impact

**Example**: `market://macro/calendar?start_date=2025-10-01&importance=high`

---

## Common Resource Format

All resources return data in this format:

```json
{
  "uri": "market://...",
  "data": { ... },  // Resource-specific content
  "metadata": {
    "generated_at": "ISO 8601 datetime",
    "data_source": "string",
    "cache_age_seconds": integer | null
  },
  "error": {  // Only if error
    "code": "ERROR_CODE",
    "message": "string",
    "details": "string"
  } | null
}
```

## Date Parameter Conventions

All resources with `{date}` parameter support:

- **Specific date**: `2025-09-30` (YYYY-MM-DD format)
- **Latest/Today**: `latest` or `today` (resolves to most recent trading day)
- **Relative**: Some resources support `yesterday`, `last_week` (where applicable)

## Caching Strategy

| Resource | Cache TTL | Strategy |
|----------|-----------|----------|
| market-summary | 5 min (trading) / 24h (closed) | Hot data |
| technical-analysis | 30 min | Recalculated periodically |
| sentiment-report | 1 hour | Stable over short periods |
| daily-briefing | 1 hour | Generated once per session |
| news-digest | 30 min | News updates |
| money-flow-report | 30 min | Capital flow data |
| sector-heatmap | 15 min | Sector data |
| market-indicators | 30 min | Aggregated indicators |
| risk-report | 1 hour | Risk calculations |
| macro-calendar | 24 hours | Calendar updates |

## Access Patterns

Resources are optimized for:

1. **Direct URL Access**: AI assistants can fetch resources directly by URI
2. **Read-Only**: No side effects, safe to cache aggressively
3. **Idempotent**: Same URI always returns same data (for same time)
4. **Content Negotiation**: Primarily JSON, some support text/plain for summaries

## Resource vs Tool

**When to use Resources**:
- Fixed data endpoints (summary, reports)
- Cached aggregated data
- Pre-generated analysis
- Regular polling/monitoring

**When to use Tools**:
- Dynamic queries with parameters
- Real-time calculations
- Custom indicator parameters
- Interactive exploration

## Example Use Cases

### Morning Routine
```
1. market://briefing/today
2. market://sentiment/latest
3. market://macro/calendar
```

### Intraday Monitoring
```
1. market://summary/latest (every 15 min)
2. market://moneyflow/today (every 30 min)
3. market://news/today (hourly)
```

### End-of-Day Analysis
```
1. market://analysis/technical/today
2. market://risk/today
3. market://sectors/heatmap/latest
```

---

**Total Resources**: 10  
**All Resources**: Read-only, cacheable, URI-based access  
**Primary Format**: JSON with metadata
