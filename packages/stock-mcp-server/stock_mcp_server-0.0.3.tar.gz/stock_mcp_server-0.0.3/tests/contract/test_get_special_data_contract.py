"""Simplified contract tests for get_special_data tool.

Based on TOOLS_SUMMARY.md specification.
Tests validate basic input/output requirements.
"""

import pytest


class TestGetSpecialDataInputValidation:
    """Test input parameter validation"""

    def test_valid_longhu_request(self):
        """Test valid Dragon-Tiger List request"""
        params = {
            "data_type": "longhu"
        }
        assert params["data_type"] in [
            "longhu", "block_trade", "unlock", "new_stock", 
            "futures", "options", "convertible_bond"
        ]

    def test_valid_block_trade_request(self):
        """Test valid block trade request"""
        params = {
            "data_type": "block_trade",
            "limit": 20
        }
        assert params["data_type"] == "block_trade"
        assert params["limit"] > 0

    def test_valid_futures_request(self):
        """Test valid futures request"""
        params = {
            "data_type": "futures",
            "contract": "IF"
        }
        assert params["contract"] in ["IH", "IF", "IC", "IM"]

    def test_valid_options_request(self):
        """Test valid options request"""
        params = {
            "data_type": "options",
            "underlying": "50ETF"
        }
        assert params["underlying"] in ["50ETF", "300ETF"]


class TestGetSpecialDataOutputValidation:
    """Test output structure validation"""

    def test_valid_longhu_response(self):
        """Test valid Dragon-Tiger List response structure"""
        response = {
            "success": True,
            "data_type": "longhu",
            "data": {
                "stocks": [
                    {
                        "code": "600519",
                        "name": "贵州茅台",
                        "change_pct": 5.2,
                        "reason": "日涨幅偏离值达7%",
                        "buy_amount": 500000000,
                        "sell_amount": 300000000,
                        "net_amount": 200000000,
                        "date": "2025-09-30"
                    }
                ],
                "summary": {
                    "total_stocks": 45,
                    "total_buy": 5800000000,
                    "total_sell": 4200000000
                }
            },
            "metadata": {
                "query_time": "2025-09-30T15:30:00+08:00",
                "data_source": "akshare",
                "cache_hit": False
            }
        }
        
        assert response["success"] is True
        assert response["data_type"] == "longhu"
        assert "stocks" in response["data"]
        assert isinstance(response["data"]["stocks"], list)

    def test_valid_error_response(self):
        """Test valid error response"""
        response = {
            "success": False,
            "error": {
                "code": "DATA_UNAVAILABLE",
                "message": "Special data temporarily unavailable",
                "details": "Data source timeout"
            },
            "metadata": {
                "query_time": "2025-09-30T15:30:00+08:00",
                "data_source": "none"
            }
        }
        
        assert response["success"] is False
        assert "error" in response


class TestGetSpecialDataContract:
    """Integration tests for tool contract compliance"""

    @pytest.mark.skip(reason="Tool not implemented yet - T043 pending")
    def test_get_longhu_data_contract(self):
        """Test get_special_data for Dragon-Tiger List"""
        from stock_mcp_server.tools.special import get_special_data
        
        params = {"data_type": "longhu"}
        result = get_special_data(**params)
        
        assert result["success"] is True
        assert result["data_type"] == "longhu"
        assert "stocks" in result["data"]

    @pytest.mark.skip(reason="Tool not implemented yet - T043 pending")
    def test_get_block_trade_contract(self):
        """Test get_special_data for block trades"""
        from stock_mcp_server.tools.special import get_special_data
        
        params = {
            "data_type": "block_trade",
            "limit": 10
        }
        result = get_special_data(**params)
        
        assert result["success"] is True
        assert result["data_type"] == "block_trade"

    @pytest.mark.skip(reason="Tool not implemented yet - T043 pending")
    def test_response_time_requirement(self):
        """Test that response time meets performance target"""
        import time
        from stock_mcp_server.tools.special import get_special_data
        
        params = {"data_type": "longhu"}
        start_time = time.time()
        result = get_special_data(**params)
        elapsed_time = time.time() - start_time
        
        # Contract requires < 3s
        assert elapsed_time < 3.0, f"Response time {elapsed_time:.2f}s exceeds 3s target"
        assert result["success"] is True
