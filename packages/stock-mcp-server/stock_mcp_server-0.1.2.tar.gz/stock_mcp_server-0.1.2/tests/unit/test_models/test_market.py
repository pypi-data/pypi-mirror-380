"""Unit tests for market models."""

import pytest
from datetime import datetime
from decimal import Decimal

from stock_mcp_server.models.market import (
    MarketIndex,
    HistoricalPrice,
    MarketBreadth,
    CapitalFlow,
    Sector,
    MacroIndicator,
    MarketOverview,
    TimeFrame,
    AdjustType,
    SectorType,
    MacroPeriod,
)


class TestMarketIndex:
    """Tests for MarketIndex model."""

    def test_valid_market_index(self):
        """Test creating valid market index."""
        index = MarketIndex(
            code="000001",
            name="上证指数",
            current=Decimal("3245.67"),
            open=Decimal("3230.50"),
            high=Decimal("3250.00"),
            low=Decimal("3228.00"),
            close=Decimal("3245.67"),
            pre_close=Decimal("3235.00"),
            change=Decimal("10.67"),
            change_pct=Decimal("0.33"),
            amplitude=Decimal("0.68"),
            volume=28500000,
            amount=Decimal("345000000000"),
            timestamp=datetime.now(),
            trading_date="2025-09-30",
            market_status="closed",
        )
        assert index.code == "000001"
        assert index.name == "上证指数"
        assert index.current == Decimal("3245.67")

    def test_ohlc_validation_high_low(self):
        """Test OHLC validation: high must be >= low."""
        with pytest.raises(ValueError, match="high must be >= low"):
            MarketIndex(
                code="000001",
                name="上证指数",
                current=Decimal("3245.67"),
                open=Decimal("3230.50"),
                high=Decimal("3200.00"),  # Invalid: high < low
                low=Decimal("3228.00"),
                pre_close=Decimal("3235.00"),
                change=Decimal("10.67"),
                change_pct=Decimal("0.33"),
                amplitude=Decimal("0.68"),
                volume=28500000,
                amount=Decimal("345000000000"),
                timestamp=datetime.now(),
                trading_date="2025-09-30",
                market_status="closed",
            )

    def test_negative_volume(self):
        """Test that negative volume is rejected."""
        with pytest.raises(ValueError):
            MarketIndex(
                code="000001",
                name="上证指数",
                current=Decimal("3245.67"),
                open=Decimal("3230.50"),
                high=Decimal("3250.00"),
                low=Decimal("3228.00"),
                pre_close=Decimal("3235.00"),
                change=Decimal("10.67"),
                change_pct=Decimal("0.33"),
                amplitude=Decimal("0.68"),
                volume=-1000,  # Invalid: negative
                amount=Decimal("345000000000"),
                timestamp=datetime.now(),
                trading_date="2025-09-30",
                market_status="closed",
            )


class TestHistoricalPrice:
    """Tests for HistoricalPrice model."""

    def test_valid_historical_price(self):
        """Test creating valid historical price."""
        price = HistoricalPrice(
            symbol="000001",
            date="2025-09-30",
            timeframe=TimeFrame.DAILY,
            adjust=AdjustType.FORWARD,
            open=Decimal("3230.50"),
            high=Decimal("3250.00"),
            low=Decimal("3228.00"),
            close=Decimal("3245.67"),
            volume=28500000,
        )
        assert price.symbol == "000001"
        assert price.timeframe == TimeFrame.DAILY
        assert price.adjust == AdjustType.FORWARD

    def test_timeframe_enum(self):
        """Test TimeFrame enum values."""
        assert TimeFrame.MIN_1.value == "1min"
        assert TimeFrame.DAILY.value == "1day"
        assert TimeFrame.WEEKLY.value == "1week"


class TestMarketBreadth:
    """Tests for MarketBreadth model."""

    def test_valid_market_breadth(self):
        """Test creating valid market breadth."""
        breadth = MarketBreadth(
            total_stocks=5000,
            advancing=2800,
            declining=2100,
            unchanged=100,
            limit_up=45,
            limit_down=12,
            advance_decline_ratio=Decimal("1.33"),
            advance_pct=Decimal("56.0"),
            decline_pct=Decimal("42.0"),
            date="2025-09-30",
        )
        assert breadth.total_stocks == 5000
        assert breadth.advancing == 2800
        assert breadth.advance_pct == Decimal("56.0")

    def test_stock_count_consistency(self):
        """Test that advancing + declining + unchanged = total."""
        # This should be valid
        breadth = MarketBreadth(
            total_stocks=100,
            advancing=50,
            declining=40,
            unchanged=10,  # 50 + 40 + 10 = 100 ✓
            limit_up=5,
            limit_down=2,
            advance_decline_ratio=Decimal("1.25"),
            advance_pct=Decimal("50.0"),
            decline_pct=Decimal("40.0"),
            date="2025-09-30",
        )
        assert breadth.advancing + breadth.declining + breadth.unchanged == breadth.total_stocks


class TestCapitalFlow:
    """Tests for CapitalFlow model."""

    def test_valid_capital_flow(self):
        """Test creating valid capital flow."""
        flow = CapitalFlow(
            north_inflow=Decimal("5800000000"),
            north_outflow=Decimal("4200000000"),
            north_net=Decimal("1600000000"),
            main_net=Decimal("-1200000000"),
            date="2025-09-30",
        )
        assert flow.north_net == Decimal("1600000000")
        assert flow.main_net == Decimal("-1200000000")

    def test_optional_fields(self):
        """Test that optional fields can be None."""
        flow = CapitalFlow(
            date="2025-09-30",
        )
        assert flow.north_inflow is None
        assert flow.margin_balance is None


class TestSector:
    """Tests for Sector model."""

    def test_valid_sector(self):
        """Test creating valid sector."""
        sector = Sector(
            code="801780",
            name="银行",
            type=SectorType.INDUSTRY,
            level=1,
            change_pct=Decimal("2.35"),
            stock_count=42,
            date="2025-09-30",
        )
        assert sector.code == "801780"
        assert sector.type == SectorType.INDUSTRY

    def test_sector_types(self):
        """Test all sector types."""
        assert SectorType.INDUSTRY.value == "industry"
        assert SectorType.CONCEPT.value == "concept"
        assert SectorType.REGION.value == "region"
        assert SectorType.STYLE.value == "style"


class TestMacroIndicator:
    """Tests for MacroIndicator model."""

    def test_valid_macro_indicator(self):
        """Test creating valid macro indicator."""
        indicator = MacroIndicator(
            indicator_name="CPI",
            indicator_code="A01010101",
            value=Decimal("102.5"),
            unit="%",
            period=MacroPeriod.MONTHLY,
            period_date="2025-09",
            yoy_change=Decimal("2.5"),
            release_date=datetime.now(),
            source="国家统计局",
        )
        assert indicator.indicator_name == "CPI"
        assert indicator.period == MacroPeriod.MONTHLY


class TestMarketOverview:
    """Tests for MarketOverview model."""

    def test_valid_market_overview(self):
        """Test creating valid market overview."""
        overview = MarketOverview(
            index_quotes={"000001": {"name": "上证指数", "close": Decimal("3245.67")}},
            breadth_summary={"advancing": 2800, "declining": 2100},
            capital_summary={"north_net": Decimal("1600000000")},
            sentiment_index=Decimal("62.5"),
            sentiment_level="optimistic",
            top_sectors_by_gain=[{"name": "银行", "change_pct": Decimal("2.35")}],
            top_news=[{"title": "测试新闻", "importance": Decimal("8.5")}],
            core_insight="市场情绪偏乐观",
            date="2025-09-30",
        )
        assert overview.sentiment_index == Decimal("62.5")
        assert len(overview.top_news) <= 5
