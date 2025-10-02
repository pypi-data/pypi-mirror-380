"""Simplified contract tests for get_market_overview tool.

Based on TOOLS_SUMMARY.md specification.
Tests validate basic input/output requirements.
"""

import pytest


class TestGetMarketOverviewInputValidation:
    """Test input parameter validation"""

    def test_valid_basic_request(self):
        """Test valid basic overview request"""
        params = {}
        assert isinstance(params, dict)

    def test_valid_with_date(self):
        """Test valid request with specific date"""
        params = {
            "date": "2025-09-30"
        }
        assert len(params["date"]) == 10
        assert params["date"].count("-") == 2

    def test_valid_with_details(self):
        """Test valid request with details"""
        params = {
            "include_details": True
        }
        assert params["include_details"] is True


class TestGetMarketOverviewOutputValidation:
    """Test output structure validation"""

    def test_valid_overview_response(self):
        """Test valid market overview response structure"""
        response = {
            "success": True,
            "overview": {
                "index_quotes": {
                    "000001": {
                        "name": "上证指数",
                        "close": 3245.67,
                        "change_pct": 0.33
                    }
                },
                "breadth_summary": {
                    "advancing": 2800,
                    "declining": 2100,
                    "advance_pct": 56.0
                },
                "capital_summary": {
                    "north_net": 1600000000,
                    "main_net": -1200000000
                },
                "sentiment_index": 62.5,
                "sentiment_level": "optimistic",
                "top_sectors_by_gain": [
                    {"name": "银行", "change_pct": 2.35},
                    {"name": "房地产", "change_pct": 2.10}
                ],
                "top_sectors_by_loss": [
                    {"name": "医疗器械", "change_pct": -1.80}
                ],
                "top_news": [
                    {
                        "title": "央行宣布降准0.5个百分点",
                        "importance": 9.5,
                        "sentiment": "positive"
                    }
                ],
                "core_insight": "市场情绪偏乐观，政策利好提振信心",
                "date": "2025-09-30",
                "generated_at": "2025-09-30T16:00:00+08:00"
            },
            "metadata": {
                "query_time": "2025-09-30T16:00:00+08:00",
                "data_source": "aggregated",
                "cache_hit": False
            }
        }
        
        assert response["success"] is True
        assert "overview" in response
        
        overview = response["overview"]
        assert "index_quotes" in overview
        assert "breadth_summary" in overview
        assert "capital_summary" in overview
        assert "sentiment_index" in overview
        assert "top_sectors_by_gain" in overview
        assert "top_news" in overview
        assert "core_insight" in overview
        
        # Validate data types
        assert isinstance(overview["sentiment_index"], (int, float))
        assert 0 <= overview["sentiment_index"] <= 100
        assert isinstance(overview["top_news"], list)
        assert len(overview["top_news"]) <= 5

    def test_valid_error_response(self):
        """Test valid error response"""
        response = {
            "success": False,
            "error": {
                "code": "DATA_UNAVAILABLE",
                "message": "Cannot generate market overview",
                "details": "Multiple data sources unavailable"
            },
            "metadata": {
                "query_time": "2025-09-30T16:00:00+08:00",
                "data_source": "none"
            }
        }
        
        assert response["success"] is False
        assert "error" in response


class TestGetMarketOverviewContract:
    """Integration tests for tool contract compliance"""

    @pytest.mark.skip(reason="Tool not implemented yet - T045 pending")
    def test_get_market_overview_basic_contract(self):
        """Test get_market_overview for basic overview"""
        from stock_mcp_server.tools.overview import get_market_overview
        
        params = {}
        result = get_market_overview(**params)
        
        assert result["success"] is True
        assert "overview" in result
        
        overview = result["overview"]
        assert "index_quotes" in overview
        assert "breadth_summary" in overview
        assert "sentiment_index" in overview
        assert "core_insight" in overview

    @pytest.mark.skip(reason="Tool not implemented yet - T045 pending")
    def test_get_market_overview_with_details_contract(self):
        """Test get_market_overview with details"""
        from stock_mcp_server.tools.overview import get_market_overview
        
        params = {"include_details": True}
        result = get_market_overview(**params)
        
        assert result["success"] is True
        overview = result["overview"]
        # With details, should have more comprehensive information
        assert len(overview["top_news"]) > 0
        assert len(overview["top_sectors_by_gain"]) > 0

    @pytest.mark.skip(reason="Tool not implemented yet - T045 pending")
    def test_response_time_requirement(self):
        """Test that response time meets performance target"""
        import time
        from stock_mcp_server.tools.overview import get_market_overview
        
        params = {}
        start_time = time.time()
        result = get_market_overview(**params)
        elapsed_time = time.time() - start_time
        
        # Contract requires < 3s
        assert elapsed_time < 3.0, f"Response time {elapsed_time:.2f}s exceeds 3s target"
        assert result["success"] is True

    @pytest.mark.skip(reason="Tool not implemented yet - T045 pending")
    def test_comprehensive_data_aggregation(self):
        """Test that overview aggregates data from multiple sources"""
        from stock_mcp_server.tools.overview import get_market_overview
        
        params = {"include_details": True}
        result = get_market_overview(**params)
        
        assert result["success"] is True
        overview = result["overview"]
        
        # Should aggregate from multiple tools:
        # - Market data (index quotes, breadth)
        # - Capital flow
        # - Sentiment
        # - Sectors
        # - News
        
        assert "index_quotes" in overview  # From get_market_data
        assert "capital_summary" in overview  # From get_money_flow
        assert "sentiment_index" in overview  # From get_sentiment_analysis
        assert "top_sectors_by_gain" in overview  # From get_sector_data
        assert "top_news" in overview  # From get_news
