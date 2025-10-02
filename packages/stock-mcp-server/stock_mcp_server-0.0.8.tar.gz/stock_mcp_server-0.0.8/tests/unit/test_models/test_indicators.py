"""Unit tests for indicator models."""

import pytest
from datetime import datetime
from decimal import Decimal

from stock_mcp_server.models.indicators import (
    TechnicalIndicator,
    IndicatorCategory,
    Signal,
)


class TestTechnicalIndicator:
    """Tests for TechnicalIndicator model."""

    def test_valid_ma_indicator(self):
        """Test creating valid MA indicator."""
        indicator = TechnicalIndicator(
            name="MA",
            category=IndicatorCategory.TREND,
            period=20,
            values={
                "ma5": Decimal("3240.50"),
                "ma10": Decimal("3235.00"),
                "ma20": Decimal("3230.00"),
            },
            signal=Signal.BUY,
            interpretation="短期均线上穿中期均线，呈多头排列",
            date="2025-09-30",
            calculated_at=datetime.now(),
        )
        assert indicator.name == "MA"
        assert indicator.category == IndicatorCategory.TREND
        assert indicator.period == 20
        assert indicator.signal == Signal.BUY

    def test_valid_macd_indicator(self):
        """Test creating valid MACD indicator."""
        indicator = TechnicalIndicator(
            name="MACD",
            category=IndicatorCategory.TREND,
            period=None,  # MACD doesn't have single period
            values={
                "dif": Decimal("5.23"),
                "dea": Decimal("3.45"),
                "macd": Decimal("1.78"),
            },
            signal=Signal.BUY,
            interpretation="MACD金叉，DIF上穿DEA",
            date="2025-09-30",
            calculated_at=datetime.now(),
        )
        assert indicator.name == "MACD"
        assert indicator.period is None
        assert "dif" in indicator.values

    def test_valid_rsi_indicator(self):
        """Test creating valid RSI indicator."""
        indicator = TechnicalIndicator(
            name="RSI",
            category=IndicatorCategory.MOMENTUM,
            period=14,
            values={
                "rsi6": Decimal("65.5"),
                "rsi12": Decimal("62.3"),
                "rsi24": Decimal("58.7"),
            },
            signal=Signal.NEUTRAL,
            interpretation="RSI处于正常区间，无超买超卖",
            date="2025-09-30",
            calculated_at=datetime.now(),
        )
        assert indicator.category == IndicatorCategory.MOMENTUM
        assert indicator.signal == Signal.NEUTRAL

    def test_indicator_categories(self):
        """Test all indicator categories."""
        assert IndicatorCategory.TREND.value == "trend"
        assert IndicatorCategory.MOMENTUM.value == "momentum"
        assert IndicatorCategory.VOLATILITY.value == "volatility"
        assert IndicatorCategory.VOLUME.value == "volume"
        assert IndicatorCategory.STRENGTH.value == "strength"

    def test_signal_types(self):
        """Test all signal types."""
        assert Signal.STRONG_BUY.value == "strong_buy"
        assert Signal.BUY.value == "buy"
        assert Signal.NEUTRAL.value == "neutral"
        assert Signal.SELL.value == "sell"
        assert Signal.STRONG_SELL.value == "strong_sell"

    def test_period_validation(self):
        """Test period must be >= 1 if provided."""
        with pytest.raises(ValueError):
            TechnicalIndicator(
                name="MA",
                category=IndicatorCategory.TREND,
                period=0,  # Invalid: must be >= 1
                values={"ma5": Decimal("3240.50")},
                date="2025-09-30",
                calculated_at=datetime.now(),
            )
