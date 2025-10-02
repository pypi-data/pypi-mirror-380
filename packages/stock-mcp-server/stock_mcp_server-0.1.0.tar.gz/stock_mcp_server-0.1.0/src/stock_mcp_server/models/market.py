"""Market data models."""

from datetime import datetime
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field, model_validator


class TimeFrame(str, Enum):
    """Supported timeframes."""

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
    """Price adjustment types."""

    NONE = "none"
    FORWARD = "qfq"
    BACKWARD = "hfq"


class MarketIndex(BaseModel):
    """Market index data."""

    code: str = Field(..., description="Index code")
    name: str = Field(..., description="Index name")
    current: Decimal = Field(..., description="Current price")
    open: Decimal = Field(..., description="Opening price")
    high: Decimal = Field(..., description="Highest price")
    low: Decimal = Field(..., description="Lowest price")
    close: Decimal | None = Field(None, description="Closing price")
    pre_close: Decimal = Field(..., description="Previous close")
    change: Decimal = Field(..., description="Price change")
    change_pct: Decimal = Field(..., description="Change percentage")
    amplitude: Decimal = Field(..., description="Amplitude")
    volume: int = Field(..., description="Volume", ge=0)
    amount: Decimal = Field(..., description="Amount", ge=0)
    turnover_rate: Decimal | None = None
    volume_ratio: Decimal | None = None
    avg_amount_60d: Decimal | None = None
    timestamp: datetime = Field(default_factory=datetime.now)
    trading_date: str
    market_status: str

    @model_validator(mode="after")
    def validate_ohlc(self) -> "MarketIndex":
        if self.high < self.low:
            raise ValueError("high must be >= low")
        return self


class HistoricalPrice(BaseModel):
    """Historical OHLCV data."""

    symbol: str
    date: str
    timeframe: TimeFrame
    adjust: AdjustType = AdjustType.NONE
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int = Field(ge=0)
    amount: Decimal | None = None
    change: Decimal | None = None
    change_pct: Decimal | None = None
    amplitude: Decimal | None = None
    turnover_rate: Decimal | None = None


class MarketBreadth(BaseModel):
    """Market breadth metrics."""

    total_stocks: int = Field(ge=0)
    advancing: int = Field(ge=0)
    declining: int = Field(ge=0)
    unchanged: int = Field(ge=0)
    limit_up: int = Field(ge=0)
    limit_down: int = Field(ge=0)
    consecutive_limit_up: int = Field(default=0, ge=0)
    consecutive_limit_down: int = Field(default=0, ge=0)
    broken_limit: int = Field(default=0, ge=0)
    gain_over_5pct: int = Field(default=0, ge=0)
    loss_over_5pct: int = Field(default=0, ge=0)
    gain_over_7pct: int = Field(default=0, ge=0)
    loss_over_7pct: int = Field(default=0, ge=0)
    new_high_60d: int = Field(default=0, ge=0)
    new_low_60d: int = Field(default=0, ge=0)
    new_high_all_time: int = Field(default=0, ge=0)
    new_low_all_time: int = Field(default=0, ge=0)
    advance_decline_ratio: Decimal
    advance_pct: Decimal = Field(ge=0, le=100)
    decline_pct: Decimal = Field(ge=0, le=100)
    date: str
    timestamp: datetime = Field(default_factory=datetime.now)


class CapitalFlow(BaseModel):
    """Capital flow data."""

    north_inflow: Decimal | None = None
    north_outflow: Decimal | None = None
    north_net: Decimal | None = None
    north_total_holdings: Decimal | None = None
    north_holdings_pct: Decimal | None = None
    super_large_net: Decimal | None = None
    large_net: Decimal | None = None
    medium_net: Decimal | None = None
    small_net: Decimal | None = None
    main_net: Decimal | None = None
    margin_balance: Decimal | None = None
    margin_buy: Decimal | None = None
    margin_repay: Decimal | None = None
    short_balance: Decimal | None = None
    short_sell: int | None = None
    short_cover: int | None = None
    margin_total: Decimal | None = None
    date: str
    timestamp: datetime = Field(default_factory=datetime.now)


class SectorType(str, Enum):
    """Sector types."""

    INDUSTRY = "industry"
    CONCEPT = "concept"
    REGION = "region"
    STYLE = "style"


class Sector(BaseModel):
    """Sector data."""

    code: str
    name: str
    type: SectorType
    level: int | None = None
    change_pct: Decimal
    turnover: Decimal | None = None
    turnover_rate: Decimal | None = None
    stock_count: int = Field(ge=0)
    leader_stocks: list[dict[str, str | Decimal]] | None = None
    main_net_inflow: Decimal | None = None
    date: str
    timestamp: datetime = Field(default_factory=datetime.now)


class MacroPeriod(str, Enum):
    """Macro data periods."""

    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    YEARLY = "yearly"


class MacroIndicator(BaseModel):
    """Macroeconomic indicator."""

    indicator_name: str
    indicator_code: str | None = None
    value: Decimal
    unit: str | None = None
    period: MacroPeriod
    period_date: str
    yoy_change: Decimal | None = None
    mom_change: Decimal | None = None
    release_date: datetime
    source: str


class MarketOverview(BaseModel):
    """Market overview."""

    index_quotes: dict[str, dict[str, str | Decimal]]
    breadth_summary: dict[str, int | Decimal]
    capital_summary: dict[str, Decimal]
    sentiment_index: Decimal = Field(ge=0, le=100)
    sentiment_level: str
    top_sectors_by_gain: list[dict[str, str | Decimal]]
    top_sectors_by_loss: list[dict[str, str | Decimal]] | None = None
    top_news: list[dict[str, str | Decimal]] = Field(max_length=5)
    core_insight: str
    date: str
    generated_at: datetime = Field(default_factory=datetime.now)
