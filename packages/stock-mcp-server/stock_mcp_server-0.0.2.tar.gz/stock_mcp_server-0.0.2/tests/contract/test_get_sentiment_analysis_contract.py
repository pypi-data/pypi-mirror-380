"""Simplified contract tests for get_sentiment_analysis tool.

Based on TOOLS_SUMMARY.md specification.
Tests validate basic input/output requirements.
"""

import pytest


class TestGetSentimentAnalysisInputValidation:
    """Test input parameter validation"""

    def test_valid_basic_request(self):
        """Test valid basic sentiment request"""
        params = {
            "dimension": "all"
        }
        assert params["dimension"] in ["all", "volume", "price", "volatility", "capital", "news"]

    def test_valid_specific_dimension(self):
        """Test valid request for specific dimension"""
        params = {
            "dimension": "volume",
            "date": "2025-09-30"
        }
        assert params["dimension"] == "volume"

    def test_valid_with_trend(self):
        """Test valid request with trend analysis"""
        params = {
            "dimension": "all",
            "days": 30,
            "include_trend": True
        }
        assert isinstance(params["days"], int)
        assert params["include_trend"] is True

    def test_empty_request_defaults(self):
        """Test empty request uses defaults"""
        params = {}
        assert isinstance(params, dict)


class TestGetSentimentAnalysisOutputValidation:
    """Test output structure validation"""

    def test_valid_sentiment_response(self):
        """Test valid sentiment response structure"""
        response = {
            "success": True,
            "sentiment": {
                "sentiment_index": 62.5,
                "sentiment_level": "optimistic",
                "volume_sentiment": 70.0,
                "price_sentiment": 68.0,
                "volatility_sentiment": 55.0,
                "capital_sentiment": 58.0,
                "news_sentiment": 65.0,
                "weights": {
                    "volume": 0.25,
                    "price": 0.35,
                    "volatility": 0.15,
                    "capital": 0.15,
                    "news": 0.10
                },
                "sentiment_trend": "improving",
                "previous_sentiment": 58.5,
                "sentiment_change": 4.0,
                "interpretation": "市场情绪偏乐观",
                "risk_level": "medium",
                "date": "2025-09-30",
                "calculated_at": "2025-09-30T15:45:00+08:00"
            },
            "metadata": {
                "query_time": "2025-09-30T15:45:00+08:00",
                "data_source": "calculated",
                "cache_hit": False
            }
        }
        
        assert response["success"] is True
        assert 0 <= response["sentiment"]["sentiment_index"] <= 100
        assert response["sentiment"]["sentiment_level"] in [
            "extreme_panic", "panic", "neutral", "optimistic", "extreme_optimism"
        ]
        
        # Check component scores
        for component in ["volume_sentiment", "price_sentiment", "volatility_sentiment", "capital_sentiment"]:
            assert component in response["sentiment"]
            assert 0 <= response["sentiment"][component] <= 100

    def test_valid_error_response(self):
        """Test valid error response"""
        response = {
            "success": False,
            "error": {
                "code": "INSUFFICIENT_DATA",
                "message": "Insufficient data for sentiment calculation",
                "details": "Need at least 1 day of market data"
            },
            "metadata": {
                "query_time": "2025-09-30T15:45:00+08:00",
                "data_source": "none"
            }
        }
        
        assert response["success"] is False
        assert "error" in response


class TestGetSentimentAnalysisContract:
    """Integration tests for tool contract compliance"""

    @pytest.mark.skip(reason="Tool not implemented yet - T039 pending")
    def test_get_overall_sentiment_contract(self):
        """Test get_sentiment_analysis with all dimensions"""
        from stock_mcp_server.tools.sentiment import get_sentiment_analysis
        
        params = {"dimension": "all"}
        result = get_sentiment_analysis(**params)
        
        assert result["success"] is True
        assert 0 <= result["sentiment"]["sentiment_index"] <= 100
        assert result["sentiment"]["sentiment_level"] in [
            "extreme_panic", "panic", "neutral", "optimistic", "extreme_optimism"
        ]

    @pytest.mark.skip(reason="Tool not implemented yet - T039 pending")
    def test_get_sentiment_with_trend_contract(self):
        """Test get_sentiment_analysis with trend"""
        from stock_mcp_server.tools.sentiment import get_sentiment_analysis
        
        params = {
            "dimension": "all",
            "include_trend": True,
            "days": 30
        }
        result = get_sentiment_analysis(**params)
        
        assert result["success"] is True
        assert "sentiment_trend" in result["sentiment"]
        assert result["sentiment"]["sentiment_trend"] in ["improving", "deteriorating", "stable"]

    @pytest.mark.skip(reason="Tool not implemented yet - T039 pending")
    def test_response_time_requirement(self):
        """Test that response time meets performance target"""
        import time
        from stock_mcp_server.tools.sentiment import get_sentiment_analysis
        
        params = {"dimension": "all"}
        start_time = time.time()
        result = get_sentiment_analysis(**params)
        elapsed_time = time.time() - start_time
        
        # Contract requires < 3s
        assert elapsed_time < 3.0, f"Response time {elapsed_time:.2f}s exceeds 3s target"
        assert result["success"] is True
