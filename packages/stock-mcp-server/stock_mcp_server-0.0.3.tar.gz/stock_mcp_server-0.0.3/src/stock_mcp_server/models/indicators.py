"""Technical indicator models."""

from datetime import datetime
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field


class IndicatorCategory(str, Enum):
    """Technical indicator categories."""

    TREND = "trend"  # 趋势指标
    MOMENTUM = "momentum"  # 动量指标
    VOLATILITY = "volatility"  # 波动性指标
    VOLUME = "volume"  # 成交量指标
    STRENGTH = "strength"  # 强弱指标
    OTHER = "other"  # 其他


class Signal(str, Enum):
    """Trading signals."""

    STRONG_BUY = "strong_buy"  # 强烈买入
    BUY = "buy"  # 买入
    NEUTRAL = "neutral"  # 中性
    SELL = "sell"  # 卖出
    STRONG_SELL = "strong_sell"  # 强烈卖出


class TechnicalIndicator(BaseModel):
    """Technical indicator calculation result."""

    # Identification
    name: str = Field(..., description="Indicator name, e.g., 'MA', 'RSI', 'MACD'")
    category: IndicatorCategory = Field(..., description="Indicator category")
    period: int | None = Field(None, description="Calculation period (days)", ge=1)

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
                        "ma60": 3220.00,
                    },
                    "signal": "buy",
                    "interpretation": "短期均线上穿中期均线，呈多头排列",
                    "date": "2025-09-30",
                    "calculated_at": "2025-09-30T15:30:00+08:00",
                },
                {
                    "name": "MACD",
                    "category": "trend",
                    "period": None,
                    "values": {"dif": 5.23, "dea": 3.45, "macd": 1.78},
                    "signal": "buy",
                    "interpretation": "MACD金叉，DIF上穿DEA",
                    "date": "2025-09-30",
                    "calculated_at": "2025-09-30T15:30:00+08:00",
                },
                {
                    "name": "RSI",
                    "category": "momentum",
                    "period": 14,
                    "values": {"rsi6": 65.5, "rsi12": 62.3, "rsi24": 58.7},
                    "signal": "neutral",
                    "interpretation": "RSI处于正常区间，无超买超卖",
                    "date": "2025-09-30",
                    "calculated_at": "2025-09-30T15:30:00+08:00",
                },
            ]
        }

