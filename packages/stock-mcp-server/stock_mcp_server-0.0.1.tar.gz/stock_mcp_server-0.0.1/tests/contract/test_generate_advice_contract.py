"""Contract tests for generate_advice tool.

Tests validate input/output schema compliance with
contracts/tools/generate_advice.json
"""

import json
import pytest
from pathlib import Path
from jsonschema import validate, ValidationError


# Load contract specification
CONTRACT_PATH = Path(__file__).parent.parent.parent / "specs" / "001-generate-mcp-server" / "contracts" / "tools" / "generate_advice.json"

with open(CONTRACT_PATH) as f:
    CONTRACT = json.load(f)

INPUT_SCHEMA = CONTRACT["inputSchema"]
OUTPUT_SCHEMA = CONTRACT["outputSchema"]


class TestGenerateAdviceInputValidation:
    """Test input parameter validation against contract schema"""

    def test_valid_simple_request(self):
        """Test valid simple analysis request"""
        params = {
            "analysis_depth": "simple"
        }
        validate(instance=params, schema=INPUT_SCHEMA)

    def test_valid_normal_request(self):
        """Test valid normal analysis request"""
        params = {
            "analysis_depth": "normal",
            "focus_area": "all",
            "include_risk": True
        }
        validate(instance=params, schema=INPUT_SCHEMA)

    def test_valid_detailed_request(self):
        """Test valid detailed analysis with backtest"""
        params = {
            "analysis_depth": "detailed",
            "focus_area": "all",
            "date": "2025-09-30",
            "include_risk": True,
            "include_backtest": True,
            "strategy_params": {
                "entry_threshold": 0.6,
                "exit_threshold": 0.4,
                "stop_loss_pct": 5.0,
                "take_profit_pct": 10.0
            }
        }
        validate(instance=params, schema=INPUT_SCHEMA)

    def test_valid_technical_focus(self):
        """Test valid request with technical focus"""
        params = {
            "analysis_depth": "normal",
            "focus_area": "technical",
            "include_risk": False
        }
        validate(instance=params, schema=INPUT_SCHEMA)

    def test_invalid_analysis_depth(self):
        """Test invalid analysis_depth enum value"""
        params = {
            "analysis_depth": "invalid_depth"
        }
        with pytest.raises(ValidationError):
            validate(instance=params, schema=INPUT_SCHEMA)

    def test_invalid_focus_area(self):
        """Test invalid focus_area enum value"""
        params = {
            "focus_area": "invalid_area"
        }
        with pytest.raises(ValidationError):
            validate(instance=params, schema=INPUT_SCHEMA)

    def test_invalid_date_format(self):
        """Test invalid date format"""
        params = {
            "date": "2025/09/30"  # Should be YYYY-MM-DD
        }
        with pytest.raises(ValidationError):
            validate(instance=params, schema=INPUT_SCHEMA)

    def test_empty_request(self):
        """Test empty request (should be valid with defaults)"""
        params = {}
        validate(instance=params, schema=INPUT_SCHEMA)


class TestGenerateAdviceOutputValidation:
    """Test output schema validation against contract"""

    def test_valid_normal_response(self):
        """Test valid normal depth response structure"""
        response = {
            "success": True,
            "recommendation": {
                "market_outlook": "bullish",
                "operation_suggestion": "cautious",
                "position_recommendation": "half",
                "analysis": {
                    "technical_analysis": "短期均线多头排列，MACD金叉",
                    "fundamental_analysis": "涨跌家数比2:1，市场宽度良好",
                    "sentiment_analysis": "市场情绪指数62.5，偏乐观",
                    "capital_analysis": "北向资金净流入16亿",
                    "news_analysis": "央行降准利好"
                },
                "risk_assessment": {
                    "risk_level": "中等风险",
                    "risk_factors": [
                        "市场情绪偏高，需警惕回调风险",
                        "主力资金流出"
                    ],
                    "risk_warning": "市场短期波动可能加大"
                },
                "actionable_insights": {
                    "key_focus_points": [
                        "关注北向资金动向",
                        "留意主力资金是否回流"
                    ],
                    "operational_strategy": "建议半仓操作",
                    "entry_points": [3200, 3220, 3240],
                    "exit_points": [3280, 3300, 3320]
                },
                "backtest_results": None,
                "confidence_score": 72.5,
                "disclaimer": "本建议仅供参考，不构成投资建议。投资有风险，入市需谨慎。",
                "metadata": {
                    "analysis_depth": "normal",
                    "generated_at": "2025-09-30T16:00:00+08:00",
                    "valid_until": "2025-10-01T09:30:00+08:00",
                    "data_sources": ["market_data", "technical_indicators"]
                }
            }
        }
        validate(instance=response, schema=OUTPUT_SCHEMA)

    def test_valid_simple_response(self):
        """Test valid simple response structure"""
        response = {
            "success": True,
            "recommendation": {
                "market_outlook": "bullish",
                "operation_suggestion": "aggressive",
                "position_recommendation": "half",
                "analysis": {
                    "technical_analysis": "MACD金叉",
                    "fundamental_analysis": "市场参与度较高",
                    "sentiment_analysis": "情绪偏乐观",
                    "capital_analysis": "资金面中性"
                },
                "actionable_insights": {
                    "key_focus_points": ["关注技术指标信号变化"],
                    "operational_strategy": "半仓操作",
                    "entry_points": [3220],
                    "exit_points": [3280]
                },
                "confidence_score": 65.0,
                "disclaimer": "本建议仅供参考，不构成投资建议。投资有风险，入市需谨慎。",
                "metadata": {
                    "analysis_depth": "simple",
                    "generated_at": "2025-09-30T16:00:00+08:00",
                    "data_sources": ["technical_indicators"]
                }
            }
        }
        validate(instance=response, schema=OUTPUT_SCHEMA)

    def test_valid_response_with_backtest(self):
        """Test valid response with backtesting results"""
        response = {
            "success": True,
            "recommendation": {
                "market_outlook": "bullish",
                "operation_suggestion": "cautious",
                "position_recommendation": "half",
                "analysis": {
                    "technical_analysis": "技术面偏多",
                    "fundamental_analysis": "市场宽度良好",
                    "sentiment_analysis": "情绪乐观",
                    "capital_analysis": "资金流入"
                },
                "actionable_insights": {
                    "key_focus_points": ["关注量能"],
                    "operational_strategy": "半仓操作"
                },
                "backtest_results": {
                    "win_rate": 65.5,
                    "avg_return": 8.2,
                    "max_drawdown": -12.3,
                    "sharpe_ratio": 1.85,
                    "sample_size": 50
                },
                "confidence_score": 75.0,
                "disclaimer": "本建议仅供参考，不构成投资建议。投资有风险，入市需谨慎。",
                "metadata": {
                    "analysis_depth": "detailed",
                    "generated_at": "2025-09-30T16:00:00+08:00",
                    "data_sources": ["all"]
                }
            }
        }
        validate(instance=response, schema=OUTPUT_SCHEMA)

    def test_valid_error_response(self):
        """Test valid error response structure"""
        response = {
            "success": False,
            "error": {
                "code": "INSUFFICIENT_DATA",
                "message": "Insufficient historical data",
                "details": "Market holiday or non-trading day"
            }
        }
        validate(instance=response, schema=OUTPUT_SCHEMA)

    def test_invalid_market_outlook(self):
        """Test invalid market_outlook enum"""
        response = {
            "success": True,
            "recommendation": {
                "market_outlook": "invalid",  # Should be bullish/bearish/sideways
                "operation_suggestion": "cautious",
                "position_recommendation": "half",
                "analysis": {
                    "technical_analysis": "test",
                    "fundamental_analysis": "test",
                    "sentiment_analysis": "test",
                    "capital_analysis": "test"
                },
                "actionable_insights": {
                    "key_focus_points": ["test"],
                    "operational_strategy": "test"
                },
                "confidence_score": 50.0,
                "disclaimer": "disclaimer",
                "metadata": {
                    "analysis_depth": "normal",
                    "generated_at": "2025-09-30T16:00:00+08:00",
                    "data_sources": []
                }
            }
        }
        with pytest.raises(ValidationError):
            validate(instance=response, schema=OUTPUT_SCHEMA)

    def test_invalid_confidence_score_range(self):
        """Test confidence score outside 0-100 range"""
        response = {
            "success": True,
            "recommendation": {
                "market_outlook": "bullish",
                "operation_suggestion": "cautious",
                "position_recommendation": "half",
                "analysis": {
                    "technical_analysis": "test",
                    "fundamental_analysis": "test",
                    "sentiment_analysis": "test",
                    "capital_analysis": "test"
                },
                "actionable_insights": {
                    "key_focus_points": ["test"],
                    "operational_strategy": "test"
                },
                "confidence_score": 150.0,  # Should be 0-100
                "disclaimer": "disclaimer",
                "metadata": {
                    "analysis_depth": "normal",
                    "generated_at": "2025-09-30T16:00:00+08:00",
                    "data_sources": []
                }
            }
        }
        with pytest.raises(ValidationError):
            validate(instance=response, schema=OUTPUT_SCHEMA)


class TestGenerateAdviceContract:
    """Integration tests for tool contract compliance
    
    Note: These tests will FAIL until the tool is implemented.
    This is expected behavior for TDD.
    """

    @pytest.mark.skip(reason="Tool not implemented yet - T044 pending")
    def test_generate_simple_advice_contract(self):
        """Test generate_advice with simple depth"""
        from stock_mcp_server.tools.advice import generate_advice
        
        params = {
            "analysis_depth": "simple",
            "focus_area": "technical"
        }
        result = generate_advice(**params)
        
        # Validate output against schema
        validate(instance=result, schema=OUTPUT_SCHEMA)
        
        # Additional semantic checks
        assert result["success"] is True
        assert result["recommendation"]["market_outlook"] in ["bullish", "bearish", "sideways"]
        assert result["recommendation"]["confidence_score"] >= 0
        assert result["recommendation"]["confidence_score"] <= 100
        assert "disclaimer" in result["recommendation"]

    @pytest.mark.skip(reason="Tool not implemented yet - T044 pending")
    def test_generate_normal_advice_contract(self):
        """Test generate_advice with normal depth"""
        from stock_mcp_server.tools.advice import generate_advice
        
        params = {
            "analysis_depth": "normal",
            "focus_area": "all",
            "include_risk": True
        }
        result = generate_advice(**params)
        
        validate(instance=result, schema=OUTPUT_SCHEMA)
        
        assert result["success"] is True
        assert "risk_assessment" in result["recommendation"]
        assert len(result["recommendation"]["risk_assessment"]["risk_factors"]) > 0

    @pytest.mark.skip(reason="Tool not implemented yet - T044 pending")
    def test_generate_detailed_advice_with_backtest_contract(self):
        """Test generate_advice with detailed depth and backtesting"""
        from stock_mcp_server.tools.advice import generate_advice
        
        params = {
            "analysis_depth": "detailed",
            "include_backtest": True
        }
        result = generate_advice(**params)
        
        validate(instance=result, schema=OUTPUT_SCHEMA)
        
        assert result["success"] is True
        if result["recommendation"]["backtest_results"]:
            assert "win_rate" in result["recommendation"]["backtest_results"]
            assert "sharpe_ratio" in result["recommendation"]["backtest_results"]

    @pytest.mark.skip(reason="Tool not implemented yet - T044 pending")
    def test_insufficient_data_error_contract(self):
        """Test error handling for insufficient data"""
        from stock_mcp_server.tools.advice import generate_advice
        
        params = {"date": "2025-01-01"}  # Holiday
        result = generate_advice(**params)
        
        validate(instance=result, schema=OUTPUT_SCHEMA)
        
        # Should return error for holiday/non-trading day
        assert result["success"] is False
        assert result["error"]["code"] in ["INSUFFICIENT_DATA", "INVALID_DATE"]

    @pytest.mark.skip(reason="Tool not implemented yet - T044 pending")
    def test_response_time_requirement(self):
        """Test that response time meets performance target"""
        import time
        from stock_mcp_server.tools.advice import generate_advice
        
        params = {"analysis_depth": "normal"}
        start_time = time.time()
        result = generate_advice(**params)
        elapsed_time = time.time() - start_time
        
        # Contract requires < 5s for normal analysis
        assert elapsed_time < 5.0, f"Response time {elapsed_time:.2f}s exceeds 5s target"
        assert result["success"] is True

    @pytest.mark.skip(reason="Tool not implemented yet - T044 pending")
    def test_disclaimer_always_present(self):
        """Test that disclaimer is always present in recommendations"""
        from stock_mcp_server.tools.advice import generate_advice
        
        params = {"analysis_depth": "simple"}
        result = generate_advice(**params)
        
        validate(instance=result, schema=OUTPUT_SCHEMA)
        
        assert result["success"] is True
        assert result["recommendation"]["disclaimer"]
        assert "风险" in result["recommendation"]["disclaimer"]
        assert "谨慎" in result["recommendation"]["disclaimer"]


class TestGenerateAdviceExamples:
    """Test all examples from contract specification"""

    def test_example_1_normal_advice(self):
        """Test Example 1: Generate normal depth investment advice"""
        example = CONTRACT["examples"][0]
        
        # Validate input
        validate(instance=example["input"], schema=INPUT_SCHEMA)
        
        # Validate output
        validate(instance=example["output"], schema=OUTPUT_SCHEMA)
        
        # Check semantic correctness
        output = example["output"]
        assert output["success"] is True
        assert output["recommendation"]["market_outlook"] == "bullish"
        assert output["recommendation"]["operation_suggestion"] == "cautious"
        assert output["recommendation"]["position_recommendation"] == "half"

    def test_example_2_simple_advice(self):
        """Test Example 2: Simple advice with technical focus only"""
        example = CONTRACT["examples"][1]
        
        validate(instance=example["input"], schema=INPUT_SCHEMA)
        validate(instance=example["output"], schema=OUTPUT_SCHEMA)
        
        output = example["output"]
        assert output["success"] is True
        assert output["recommendation"]["metadata"]["analysis_depth"] == "simple"


class TestGenerateAdviceErrors:
    """Test all error scenarios from contract specification"""

    def test_error_insufficient_data(self):
        """Test INSUFFICIENT_DATA error example"""
        error_spec = CONTRACT["errors"][0]
        
        # Validate error input
        validate(instance=error_spec["example"]["input"], schema=INPUT_SCHEMA)
        
        # Validate error output
        validate(instance=error_spec["example"]["output"], schema=OUTPUT_SCHEMA)
        
        # Check error structure
        output = error_spec["example"]["output"]
        assert output["success"] is False
        assert output["error"]["code"] == "INSUFFICIENT_DATA"

    def test_error_analysis_failed(self):
        """Test ANALYSIS_FAILED error example"""
        error_spec = CONTRACT["errors"][1]
        
        validate(instance=error_spec["example"]["input"], schema=INPUT_SCHEMA)
        validate(instance=error_spec["example"]["output"], schema=OUTPUT_SCHEMA)
        
        output = error_spec["example"]["output"]
        assert output["success"] is False
        assert output["error"]["code"] == "ANALYSIS_FAILED"
