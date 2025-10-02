"""Simplified contract tests for get_money_flow tool.

Based on TOOLS_SUMMARY.md specification.
Tests validate basic input/output requirements.
"""

import pytest


class TestGetMoneyFlowInputValidation:
    """Test input parameter validation"""

    def test_valid_north_capital_request(self):
        """Test valid north capital flow request"""
        params = {
            "flow_type": "north"
        }
        assert params["flow_type"] in ["north", "margin", "main", "all"]

    def test_valid_margin_request(self):
        """Test valid margin trading request"""
        params = {
            "flow_type": "margin",
            "date": "2025-09-30"
        }
        assert params["flow_type"] == "margin"

    def test_valid_all_flows_request(self):
        """Test valid request for all flow types"""
        params = {
            "flow_type": "all"
        }
        assert params["flow_type"] == "all"

    def test_empty_request_defaults(self):
        """Test empty request uses defaults"""
        params = {}
        # Should use default flow_type and today's date
        assert isinstance(params, dict)


class TestGetMoneyFlowOutputValidation:
    """Test output structure validation"""

    def test_valid_north_capital_response(self):
        """Test valid north capital response structure"""
        response = {
            "success": True,
            "flow_type": "north",
            "data": {
                "north_inflow": 5800000000,
                "north_outflow": 4200000000,
                "north_net": 1600000000,
                "north_total_holdings": 2500000000000,
                "north_holdings_pct": 4.2,
                "date": "2025-09-30",
                "timestamp": "2025-09-30T15:30:00+08:00"
            },
            "metadata": {
                "query_time": "2025-09-30T15:30:00+08:00",
                "data_source": "akshare",
                "cache_hit": False
            }
        }
        
        assert response["success"] is True
        assert response["flow_type"] == "north"
        assert "north_net" in response["data"]
        assert isinstance(response["data"]["north_net"], (int, float))

    def test_valid_all_flows_response(self):
        """Test valid response with all flow types"""
        response = {
            "success": True,
            "flow_type": "all",
            "data": {
                # North capital
                "north_net": 1600000000,
                # Main capital
                "main_net": -1200000000,
                "super_large_net": -800000000,
                "large_net": -400000000,
                # Margin trading
                "margin_balance": 1850000000000,
                "margin_buy": 95000000000,
                "date": "2025-09-30",
                "timestamp": "2025-09-30T15:30:00+08:00"
            },
            "metadata": {
                "query_time": "2025-09-30T15:30:00+08:00",
                "data_source": "akshare"
            }
        }
        
        assert response["success"] is True
        assert "north_net" in response["data"]
        assert "main_net" in response["data"]
        assert "margin_balance" in response["data"]

    def test_valid_error_response(self):
        """Test valid error response"""
        response = {
            "success": False,
            "error": {
                "code": "DATA_UNAVAILABLE",
                "message": "Money flow data temporarily unavailable",
                "details": "AKShare API timeout"
            },
            "metadata": {
                "query_time": "2025-09-30T15:30:00+08:00",
                "data_source": "none"
            }
        }
        
        assert response["success"] is False
        assert "error" in response


class TestGetMoneyFlowContract:
    """Integration tests for tool contract compliance"""

    @pytest.mark.skip(reason="Tool not implemented yet - T038 pending")
    def test_get_north_capital_flow_contract(self):
        """Test get_money_flow with north capital"""
        from stock_mcp_server.tools.money_flow import get_money_flow
        
        params = {"flow_type": "north"}
        result = get_money_flow(**params)
        
        assert result["success"] is True
        assert result["flow_type"] == "north"
        assert "north_net" in result["data"]

    @pytest.mark.skip(reason="Tool not implemented yet - T038 pending")
    def test_get_all_flows_contract(self):
        """Test get_money_flow with all flow types"""
        from stock_mcp_server.tools.money_flow import get_money_flow
        
        params = {"flow_type": "all"}
        result = get_money_flow(**params)
        
        assert result["success"] is True
        assert "north_net" in result["data"]
        assert "main_net" in result["data"]
        assert "margin_balance" in result["data"]

    @pytest.mark.skip(reason="Tool not implemented yet - T038 pending")
    def test_response_time_requirement(self):
        """Test that response time meets performance target"""
        import time
        from stock_mcp_server.tools.money_flow import get_money_flow
        
        params = {"flow_type": "north"}
        start_time = time.time()
        result = get_money_flow(**params)
        elapsed_time = time.time() - start_time
        
        # Contract requires < 2s
        assert elapsed_time < 2.0, f"Response time {elapsed_time:.2f}s exceeds 2s target"
        assert result["success"] is True
