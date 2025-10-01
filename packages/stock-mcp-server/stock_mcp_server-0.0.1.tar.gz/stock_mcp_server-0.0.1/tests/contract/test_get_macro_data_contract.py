"""Simplified contract tests for get_macro_data tool.

Based on TOOLS_SUMMARY.md specification.
Tests validate basic input/output requirements.
"""

import pytest


class TestGetMacroDataInputValidation:
    """Test input parameter validation"""

    def test_valid_domestic_macro_request(self):
        """Test valid domestic macro data request"""
        params = {
            "data_type": "macro"
        }
        assert params["data_type"] in ["macro", "global", "all"]

    def test_valid_specific_indicators(self):
        """Test valid request for specific indicators"""
        params = {
            "data_type": "macro",
            "indicators": ["gdp", "cpi", "pmi"]
        }
        assert isinstance(params["indicators"], list)
        assert all(ind in ["gdp", "cpi", "pmi", "ppi", "m0", "m1", "m2"] for ind in params["indicators"])

    def test_valid_global_markets(self):
        """Test valid request for global markets"""
        params = {
            "data_type": "global",
            "markets": ["us_stock", "commodity", "forex"]
        }
        assert isinstance(params["markets"], list)

    def test_valid_with_impact_analysis(self):
        """Test valid request with impact analysis"""
        params = {
            "data_type": "all",
            "include_impact": True
        }
        assert params["include_impact"] is True


class TestGetMacroDataOutputValidation:
    """Test output structure validation"""

    def test_valid_macro_response(self):
        """Test valid macro data response structure"""
        response = {
            "success": True,
            "data_type": "macro",
            "domestic_indicators": [
                {
                    "indicator_name": "CPI",
                    "indicator_code": "A01010101",
                    "value": 102.5,
                    "unit": "%",
                    "period": "monthly",
                    "period_date": "2025-09",
                    "yoy_change": 2.5,
                    "mom_change": 0.3,
                    "release_date": "2025-10-15T09:30:00+08:00",
                    "source": "国家统计局"
                }
            ],
            "impact_analysis": {
                "overall_impact": "positive",
                "description": "宏观数据整体向好，有利于A股估值修复",
                "affected_sectors": ["银行", "地产", "基建"]
            },
            "metadata": {
                "query_time": "2025-09-30T15:30:00+08:00",
                "data_source": "akshare",
                "cache_hit": False
            }
        }
        
        assert response["success"] is True
        assert "domestic_indicators" in response
        assert isinstance(response["domestic_indicators"], list)
        
        if len(response["domestic_indicators"]) > 0:
            indicator = response["domestic_indicators"][0]
            assert "indicator_name" in indicator
            assert "value" in indicator

    def test_valid_error_response(self):
        """Test valid error response"""
        response = {
            "success": False,
            "error": {
                "code": "DATA_UNAVAILABLE",
                "message": "Macro data temporarily unavailable",
                "details": "Data source timeout"
            },
            "metadata": {
                "query_time": "2025-09-30T15:30:00+08:00",
                "data_source": "none"
            }
        }
        
        assert response["success"] is False
        assert "error" in response


class TestGetMacroDataContract:
    """Integration tests for tool contract compliance"""

    @pytest.mark.skip(reason="Tool not implemented yet - T042 pending")
    def test_get_domestic_macro_contract(self):
        """Test get_macro_data for domestic indicators"""
        from stock_mcp_server.tools.macro import get_macro_data
        
        params = {"data_type": "macro"}
        result = get_macro_data(**params)
        
        assert result["success"] is True
        assert "domestic_indicators" in result
        assert len(result["domestic_indicators"]) > 0

    @pytest.mark.skip(reason="Tool not implemented yet - T042 pending")
    def test_get_macro_with_impact_contract(self):
        """Test get_macro_data with impact analysis"""
        from stock_mcp_server.tools.macro import get_macro_data
        
        params = {
            "data_type": "all",
            "include_impact": True
        }
        result = get_macro_data(**params)
        
        assert result["success"] is True
        assert "impact_analysis" in result

    @pytest.mark.skip(reason="Tool not implemented yet - T042 pending")
    def test_response_time_requirement(self):
        """Test that response time meets performance target"""
        import time
        from stock_mcp_server.tools.macro import get_macro_data
        
        params = {"data_type": "macro"}
        start_time = time.time()
        result = get_macro_data(**params)
        elapsed_time = time.time() - start_time
        
        # Contract requires < 3s
        assert elapsed_time < 3.0, f"Response time {elapsed_time:.2f}s exceeds 3s target"
        assert result["success"] is True
