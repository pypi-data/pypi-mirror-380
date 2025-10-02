"""Contract tests for get_market_data tool.

Tests validate input/output schema compliance with
contracts/tools/get_market_data.json
"""

import json
import pytest
from pathlib import Path
from jsonschema import validate, ValidationError
from datetime import datetime


# Load contract specification
CONTRACT_PATH = Path(__file__).parent.parent.parent / "specs" / "001-generate-mcp-server" / "contracts" / "tools" / "get_market_data.json"

with open(CONTRACT_PATH) as f:
    CONTRACT = json.load(f)

INPUT_SCHEMA = CONTRACT["inputSchema"]
OUTPUT_SCHEMA = CONTRACT["outputSchema"]


class TestGetMarketDataInputValidation:
    """Test input parameter validation against contract schema"""

    def test_valid_realtime_request(self):
        """Test valid real-time data request"""
        params = {
            "data_type": "realtime"
        }
        # Should not raise
        validate(instance=params, schema=INPUT_SCHEMA)

    def test_valid_history_request(self):
        """Test valid historical data request"""
        params = {
            "data_type": "history",
            "period": "1day",
            "start_date": "2025-09-01",
            "end_date": "2025-09-30"
        }
        validate(instance=params, schema=INPUT_SCHEMA)

    def test_valid_breadth_request(self):
        """Test valid market breadth request"""
        params = {
            "data_type": "breadth"
        }
        validate(instance=params, schema=INPUT_SCHEMA)

    def test_valid_valuation_request(self):
        """Test valid valuation request"""
        params = {
            "data_type": "valuation"
        }
        validate(instance=params, schema=INPUT_SCHEMA)

    def test_valid_turnover_request(self):
        """Test valid turnover request"""
        params = {
            "data_type": "turnover"
        }
        validate(instance=params, schema=INPUT_SCHEMA)

    def test_valid_all_request(self):
        """Test valid comprehensive data request"""
        params = {
            "data_type": "all",
            "index_code": "000001",
            "date": "2025-09-30"
        }
        validate(instance=params, schema=INPUT_SCHEMA)

    def test_invalid_data_type(self):
        """Test invalid data_type enum value"""
        params = {
            "data_type": "invalid_type"
        }
        with pytest.raises(ValidationError):
            validate(instance=params, schema=INPUT_SCHEMA)

    def test_invalid_index_code_format(self):
        """Test invalid index code format (not 6 digits)"""
        params = {
            "data_type": "realtime",
            "index_code": "123"  # Should be 6 digits
        }
        with pytest.raises(ValidationError):
            validate(instance=params, schema=INPUT_SCHEMA)

    def test_invalid_date_format(self):
        """Test invalid date format"""
        params = {
            "data_type": "realtime",
            "date": "2025/09/30"  # Should be YYYY-MM-DD
        }
        with pytest.raises(ValidationError):
            validate(instance=params, schema=INPUT_SCHEMA)

    def test_invalid_period_enum(self):
        """Test invalid period enum value"""
        params = {
            "data_type": "history",
            "period": "invalid_period"
        }
        with pytest.raises(ValidationError):
            validate(instance=params, schema=INPUT_SCHEMA)

    def test_invalid_adjust_enum(self):
        """Test invalid adjust enum value"""
        params = {
            "data_type": "history",
            "adjust": "invalid_adjust"
        }
        with pytest.raises(ValidationError):
            validate(instance=params, schema=INPUT_SCHEMA)

    def test_empty_request(self):
        """Test empty request (should be valid with defaults)"""
        params = {}
        validate(instance=params, schema=INPUT_SCHEMA)


class TestGetMarketDataOutputValidation:
    """Test output schema validation against contract"""

    def test_valid_realtime_response(self):
        """Test valid real-time response structure"""
        response = {
            "success": True,
            "data_type": "realtime",
            "data": {
                "index": {
                    "code": "000001",
                    "name": "上证指数",
                    "current": 3245.67,
                    "open": 3230.50,
                    "high": 3250.00,
                    "low": 3228.00,
                    "close": 3245.67,
                    "pre_close": 3235.00,
                    "change": 10.67,
                    "change_pct": 0.33,
                    "amplitude": 0.68,
                    "volume": 28500000,
                    "amount": 345000000000,
                    "turnover_rate": 1.25,
                    "volume_ratio": 1.15,
                    "timestamp": "2025-09-30T15:00:00+08:00",
                    "trading_date": "2025-09-30",
                    "market_status": "closed"
                }
            },
            "metadata": {
                "query_time": "2025-09-30T15:30:00+08:00",
                "data_source": "akshare",
                "cache_hit": False,
                "data_age_seconds": 1800
            }
        }
        validate(instance=response, schema=OUTPUT_SCHEMA)

    def test_valid_historical_response(self):
        """Test valid historical data response structure"""
        response = {
            "success": True,
            "data_type": "history",
            "data": {
                "symbol": "000001",
                "timeframe": "1day",
                "adjust": "none",
                "records": [
                    {
                        "date": "2025-09-30",
                        "open": 3230.50,
                        "high": 3250.00,
                        "low": 3228.00,
                        "close": 3245.67,
                        "volume": 28500000,
                        "amount": 345000000000
                    }
                ],
                "count": 20
            },
            "metadata": {
                "query_time": "2025-09-30T15:30:00+08:00",
                "data_source": "akshare",
                "cache_hit": True
            }
        }
        validate(instance=response, schema=OUTPUT_SCHEMA)

    def test_valid_breadth_response(self):
        """Test valid market breadth response structure"""
        response = {
            "success": True,
            "data_type": "breadth",
            "data": {
                "breadth": {
                    "total_stocks": 5000,
                    "advancing": 2800,
                    "declining": 2100,
                    "unchanged": 100,
                    "limit_up": 45,
                    "limit_down": 12,
                    "advance_decline_ratio": 1.33,
                    "advance_pct": 56.0,
                    "decline_pct": 42.0,
                    "date": "2025-09-30",
                    "timestamp": "2025-09-30T15:00:00+08:00"
                }
            },
            "metadata": {
                "query_time": "2025-09-30T15:30:00+08:00",
                "data_source": "akshare",
                "cache_hit": False
            }
        }
        validate(instance=response, schema=OUTPUT_SCHEMA)

    def test_valid_error_response(self):
        """Test valid error response structure"""
        response = {
            "success": False,
            "data_type": "realtime",
            "metadata": {
                "query_time": "2025-09-30T15:30:00+08:00",
                "data_source": "akshare"
            },
            "error": {
                "code": "DATA_UNAVAILABLE",
                "message": "Unable to fetch market data after 3 retries",
                "details": "AKShare API timeout"
            }
        }
        validate(instance=response, schema=OUTPUT_SCHEMA)

    def test_missing_required_fields_in_response(self):
        """Test response missing required fields"""
        response = {
            "success": True
            # Missing data_type and metadata
        }
        with pytest.raises(ValidationError):
            validate(instance=response, schema=OUTPUT_SCHEMA)

    def test_invalid_success_type(self):
        """Test invalid success field type"""
        response = {
            "success": "true",  # Should be boolean
            "data_type": "realtime",
            "metadata": {
                "query_time": "2025-09-30T15:30:00+08:00",
                "data_source": "akshare"
            }
        }
        with pytest.raises(ValidationError):
            validate(instance=response, schema=OUTPUT_SCHEMA)


class TestGetMarketDataContract:
    """Integration tests for tool contract compliance
    
    Note: These tests will FAIL until the tool is implemented.
    This is expected behavior for TDD.
    """

    @pytest.mark.skip(reason="Tool not implemented yet - T036 pending")
    def test_get_realtime_data_contract(self):
        """Test get_market_data with realtime data_type"""
        # This will be implemented in T036
        from stock_mcp_server.tools.market_data import get_market_data
        
        params = {"data_type": "realtime"}
        result = get_market_data(**params)
        
        # Validate output against schema
        validate(instance=result, schema=OUTPUT_SCHEMA)
        
        # Additional semantic checks
        assert result["success"] is True
        assert result["data_type"] == "realtime"
        assert "index" in result["data"]
        assert result["data"]["index"]["code"] == "000001"

    @pytest.mark.skip(reason="Tool not implemented yet - T036 pending")
    def test_get_historical_data_contract(self):
        """Test get_market_data with history data_type"""
        from stock_mcp_server.tools.market_data import get_market_data
        
        params = {
            "data_type": "history",
            "period": "1day",
            "start_date": "2025-09-01",
            "end_date": "2025-09-30"
        }
        result = get_market_data(**params)
        
        validate(instance=result, schema=OUTPUT_SCHEMA)
        
        assert result["success"] is True
        assert result["data_type"] == "history"
        assert "records" in result["data"]
        assert isinstance(result["data"]["records"], list)
        assert result["data"]["count"] > 0

    @pytest.mark.skip(reason="Tool not implemented yet - T036 pending")
    def test_get_breadth_data_contract(self):
        """Test get_market_data with breadth data_type"""
        from stock_mcp_server.tools.market_data import get_market_data
        
        params = {"data_type": "breadth"}
        result = get_market_data(**params)
        
        validate(instance=result, schema=OUTPUT_SCHEMA)
        
        assert result["success"] is True
        assert result["data_type"] == "breadth"
        assert "breadth" in result["data"]
        assert result["data"]["breadth"]["total_stocks"] > 0

    @pytest.mark.skip(reason="Tool not implemented yet - T036 pending")
    def test_invalid_date_error_contract(self):
        """Test error handling for invalid date"""
        from stock_mcp_server.tools.market_data import get_market_data
        
        params = {"date": "2025-13-45"}  # Invalid date
        result = get_market_data(**params)
        
        validate(instance=result, schema=OUTPUT_SCHEMA)
        
        assert result["success"] is False
        assert result["error"]["code"] == "INVALID_DATE"

    @pytest.mark.skip(reason="Tool not implemented yet - T036 pending")
    def test_response_time_requirement(self):
        """Test that response time meets performance target"""
        import time
        from stock_mcp_server.tools.market_data import get_market_data
        
        params = {"data_type": "realtime"}
        start_time = time.time()
        result = get_market_data(**params)
        elapsed_time = time.time() - start_time
        
        # Contract requires < 2s for realtime data
        assert elapsed_time < 2.0, f"Response time {elapsed_time:.2f}s exceeds 2s target"
        assert result["success"] is True


class TestGetMarketDataExamples:
    """Test all examples from contract specification"""

    def test_example_1_realtime(self):
        """Test Example 1: Get real-time Shanghai index data"""
        example = CONTRACT["examples"][0]
        
        # Validate input
        validate(instance=example["input"], schema=INPUT_SCHEMA)
        
        # Validate output
        validate(instance=example["output"], schema=OUTPUT_SCHEMA)

    def test_example_2_historical(self):
        """Test Example 2: Get historical daily K-line"""
        example = CONTRACT["examples"][1]
        
        validate(instance=example["input"], schema=INPUT_SCHEMA)
        validate(instance=example["output"], schema=OUTPUT_SCHEMA)

    def test_example_3_breadth(self):
        """Test Example 3: Get market breadth statistics"""
        example = CONTRACT["examples"][2]
        
        validate(instance=example["input"], schema=INPUT_SCHEMA)
        validate(instance=example["output"], schema=OUTPUT_SCHEMA)


class TestGetMarketDataErrors:
    """Test all error scenarios from contract specification"""

    def test_error_invalid_date(self):
        """Test INVALID_DATE error example"""
        error_spec = CONTRACT["errors"][0]
        
        # Validate error input
        validate(instance=error_spec["example"]["input"], schema=INPUT_SCHEMA)
        
        # Validate error output
        validate(instance=error_spec["example"]["output"], schema=OUTPUT_SCHEMA)
        
        # Check error structure
        output = error_spec["example"]["output"]
        assert output["success"] is False
        assert output["error"]["code"] == "INVALID_DATE"

    def test_error_data_unavailable(self):
        """Test DATA_UNAVAILABLE error example"""
        error_spec = CONTRACT["errors"][1]
        
        validate(instance=error_spec["example"]["input"], schema=INPUT_SCHEMA)
        validate(instance=error_spec["example"]["output"], schema=OUTPUT_SCHEMA)
        
        output = error_spec["example"]["output"]
        assert output["success"] is False
        assert output["error"]["code"] == "DATA_UNAVAILABLE"
