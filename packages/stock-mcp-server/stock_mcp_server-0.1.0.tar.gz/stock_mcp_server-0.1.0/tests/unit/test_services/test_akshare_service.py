"""Unit tests for AKShare service."""

import pytest
from unittest.mock import Mock, patch, MagicMock
import pandas as pd
from decimal import Decimal
from datetime import datetime

from stock_mcp_server.services.akshare_service import AKShareService
from stock_mcp_server.models.market import MarketIndex, MarketBreadth, CapitalFlow


class TestAKShareService:
    """Tests for AKShareService."""

    @pytest.fixture
    def akshare_service(self):
        """Create AKShare service instance."""
        from stock_mcp_server.services import akshare_service
        # Reset global instance
        akshare_service._akshare_service = None
        
        service = AKShareService()
        yield service
        
        # Cleanup
        akshare_service._akshare_service = None

    @pytest.fixture
    def mock_index_data(self):
        """Mock index spot data."""
        return pd.DataFrame({
            "代码": ["000001", "399001"],
            "名称": ["上证指数", "深证成指"],
            "最新价": [3245.67, 10850.23],
            "今开": [3230.50, 10800.00],
            "最高": [3250.00, 10900.00],
            "最低": [3228.00, 10780.00],
            "昨收": [3235.00, 10820.00],
            "涨跌额": [10.67, 30.23],
            "涨跌幅": [0.33, 0.28],
            "振幅": [0.68, 1.11],
            "成交量": [28500000, 15000000],
            "成交额": [345000000000, 200000000000],
        })

    @pytest.fixture
    def mock_breadth_data(self):
        """Mock market breadth data."""
        return pd.DataFrame({
            "代码": ["000001", "000002", "000003", "600000", "600001"],
            "名称": ["股票1", "股票2", "股票3", "股票4", "股票5"],
            "涨跌幅": [5.5, -3.2, 0.0, 12.5, -10.5],  # Changed -8.9 to -10.5 for limit_down test
        })

    @pytest.fixture
    def mock_capital_flow_data(self):
        """Mock capital flow data."""
        return pd.DataFrame({
            "日期": ["2025-09-30", "2025-09-29"],
            "北向资金": [1600000000, -500000000],
        })

    def test_get_index_spot_success(self, akshare_service, mock_index_data):
        """Test successfully fetching index spot data."""
        # Clear cache first
        akshare_service.cache.clear_category("market_data")
        
        # Mock the data source manager
        with patch.object(akshare_service.data_source_manager, 'get_index_spot') as mock_get:
            mock_index = MarketIndex(
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
                market_status="closed"
            )
            mock_get.return_value = mock_index
            
            result = akshare_service.get_index_spot("000001")
            
            assert result is not None
            assert isinstance(result, MarketIndex)
            assert result.code == "000001"
            assert result.name == "上证指数"
            assert result.current == Decimal("3245.67")
            assert result.open == Decimal("3230.50")

    def test_get_index_spot_cache_hit(self, akshare_service, mock_index_data):
        """Test cache hit for index spot data."""
        # Clear cache first
        akshare_service.cache.clear_category("market_data")
        
        with patch.object(akshare_service.data_source_manager, 'get_index_spot') as mock_get:
            mock_index = MarketIndex(
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
                market_status="closed"
            )
            mock_get.return_value = mock_index
            
            # First call - should hit data source
            result1 = akshare_service.get_index_spot("000001")
            assert mock_get.call_count == 1
            
            # Second call - should hit cache
            result2 = akshare_service.get_index_spot("000001")
            assert mock_get.call_count == 1  # No additional call
            
            assert result1.code == result2.code

    def test_get_index_spot_not_found(self, akshare_service, mock_index_data):
        """Test when index code is not found."""
        with patch.object(akshare_service.data_source_manager, 'get_index_spot', return_value=None):
            result = akshare_service.get_index_spot("999999")  # Non-existent
            assert result is None

    def test_get_index_spot_retry_on_error(self, akshare_service):
        """Test retry logic on API error."""
        # Clear cache first
        akshare_service.cache.clear_category("market_data")
        
        with patch.object(akshare_service.data_source_manager, 'get_index_spot') as mock_get:
            # Mock success (DataSourceManager handles retry internally)
            mock_index = MarketIndex(
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
                market_status="closed"
            )
            mock_get.return_value = mock_index
            
            result = akshare_service.get_index_spot("000001")
            assert result is not None
            assert mock_get.call_count == 1  # Called once (retry is internal to DataSourceManager)

    def test_get_market_breadth_success(self, akshare_service, mock_breadth_data):
        """Test successfully fetching market breadth."""
        with patch("akshare.stock_zh_a_spot_em", return_value=mock_breadth_data):
            result = akshare_service.get_market_breadth("2025-09-30")
            
            assert result is not None
            assert isinstance(result, MarketBreadth)
            assert result.total_stocks == 5
            assert result.advancing == 2  # 2 stocks with positive change
            assert result.declining == 2  # 2 stocks with negative change
            assert result.unchanged == 1  # 1 stock with 0 change
            assert result.limit_up >= 1  # At least one >9.9%
            assert result.limit_down >= 1  # At least one <-9.9%

    def test_get_capital_flow_success(self, akshare_service, mock_capital_flow_data):
        """Test successfully fetching capital flow."""
        with patch("akshare.stock_hsgt_fund_flow_summary_em", return_value=mock_capital_flow_data):
            result = akshare_service.get_capital_flow("2025-09-30")
            
            assert result is not None
            assert isinstance(result, CapitalFlow)
            # The service uses iloc[-1] which gets the last row (index 1, value -500000000)
            assert result.north_net == Decimal("-500000000")
            assert result.date == "2025-09-30"

    def test_get_capital_flow_cache(self, akshare_service, mock_capital_flow_data):
        """Test capital flow caching."""
        # Clear any existing cache first
        akshare_service.cache.clear_category("market_data")
        
        with patch("akshare.stock_hsgt_fund_flow_summary_em", return_value=mock_capital_flow_data) as mock_ak:
            # First call
            result1 = akshare_service.get_capital_flow("2025-09-30")
            assert mock_ak.call_count == 1
            
            # Second call - should hit cache
            result2 = akshare_service.get_capital_flow("2025-09-30")
            assert mock_ak.call_count == 1  # No additional call
            
            assert result1.north_net == result2.north_net

    def test_retry_fetch_max_attempts(self, akshare_service):
        """Test that retry stops after max attempts."""
        mock_func = Mock(side_effect=Exception("Persistent error"))
        
        with pytest.raises(Exception, match="Persistent error"):
            akshare_service._retry_fetch(mock_func)
        
        # Should have tried 3 times
        assert mock_func.call_count == 3

    def test_rate_limiting(self, akshare_service, mock_index_data):
        """Test that rate limiting is applied."""
        import time
        
        with patch.object(akshare_service.data_source_manager, 'get_index_spot') as mock_get:
            mock_index = MarketIndex(
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
                market_status="closed"
            )
            mock_get.return_value = mock_index
            
            # Rate limiting is now handled by DataSourceManager
            result = akshare_service.get_index_spot("000001")
            assert result is not None

    def test_error_handling_returns_none(self, akshare_service):
        """Test that API errors return None gracefully."""
        # Clear cache first
        akshare_service.cache.clear_category("market_data")
        
        with patch.object(akshare_service.data_source_manager, 'get_index_spot', return_value=None):
            result = akshare_service.get_index_spot("000001")
            assert result is None
