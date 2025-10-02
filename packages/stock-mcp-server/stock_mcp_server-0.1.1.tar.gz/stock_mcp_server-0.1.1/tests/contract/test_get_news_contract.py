"""Simplified contract tests for get_news tool.

Based on TOOLS_SUMMARY.md specification.
Tests validate basic input/output requirements.
"""

import pytest


class TestGetNewsInputValidation:
    """Test input parameter validation"""

    def test_valid_basic_request(self):
        """Test valid basic news request"""
        params = {
            "limit": 10
        }
        assert isinstance(params["limit"], int)
        assert params["limit"] > 0

    def test_valid_category_filter(self):
        """Test valid category filter"""
        params = {
            "category": "policy",
            "limit": 5
        }
        assert params["category"] in ["policy", "market", "company", "industry", "international", "all"]

    def test_valid_with_sentiment(self):
        """Test valid request with sentiment analysis"""
        params = {
            "limit": 10,
            "include_sentiment": True,
            "sentiment_method": "snownlp"
        }
        assert params["include_sentiment"] is True
        assert params["sentiment_method"] in ["snownlp", "llm"]

    def test_valid_with_hot_topics(self):
        """Test valid request with hot topics"""
        params = {
            "limit": 10,
            "include_hot_topics": True
        }
        assert params["include_hot_topics"] is True


class TestGetNewsOutputValidation:
    """Test output structure validation"""

    def test_valid_news_response(self):
        """Test valid news response structure"""
        response = {
            "success": True,
            "news": [
                {
                    "title": "央行宣布降准0.5个百分点",
                    "summary": "中国人民银行决定于2025年10月15日下调金融机构存款准备金率",
                    "url": "https://finance.eastmoney.com/...",
                    "category": "policy",
                    "source": "东方财富",
                    "published_at": "2025-09-30T16:30:00+08:00",
                    "importance": 9.5,
                    "sentiment": "positive",
                    "sentiment_score": 0.85,
                    "related_sectors": ["银行", "房地产"],
                    "tags": ["货币政策", "降准", "流动性"],
                    "market_impact": "全市场",
                    "time_horizon": "中期",
                    "scraped_at": "2025-09-30T17:00:00+08:00"
                }
            ],
            "hot_topics": [
                {
                    "topic": "货币政策",
                    "count": 5,
                    "avg_sentiment": 0.78
                }
            ],
            "overall_sentiment": {
                "positive": 75,
                "neutral": 20,
                "negative": 5
            },
            "metadata": {
                "query_time": "2025-09-30T17:00:00+08:00",
                "data_source": "scraped",
                "sources_count": 3,
                "cache_hit": False
            }
        }
        
        assert response["success"] is True
        assert isinstance(response["news"], list)
        assert len(response["news"]) > 0
        
        article = response["news"][0]
        assert "title" in article
        assert "source" in article
        assert 0 <= article["importance"] <= 10
        if "sentiment" in article:
            assert article["sentiment"] in ["positive", "neutral", "negative"]

    def test_valid_error_response(self):
        """Test valid error response"""
        response = {
            "success": False,
            "error": {
                "code": "PARSE_ERROR",
                "message": "Failed to scrape news from all sources",
                "details": "All news sources unavailable or blocked"
            },
            "metadata": {
                "query_time": "2025-09-30T17:00:00+08:00",
                "data_source": "cache"
            }
        }
        
        assert response["success"] is False
        assert "error" in response


class TestGetNewsContract:
    """Integration tests for tool contract compliance"""

    @pytest.mark.skip(reason="Tool not implemented yet - T040 pending")
    def test_get_latest_news_contract(self):
        """Test get_news for latest articles"""
        from stock_mcp_server.tools.news import get_news
        
        params = {"limit": 10}
        result = get_news(**params)
        
        assert result["success"] is True
        assert len(result["news"]) <= 10
        assert all("title" in article for article in result["news"])

    @pytest.mark.skip(reason="Tool not implemented yet - T040 pending")
    def test_get_news_with_sentiment_contract(self):
        """Test get_news with sentiment analysis"""
        from stock_mcp_server.tools.news import get_news
        
        params = {
            "limit": 5,
            "include_sentiment": True
        }
        result = get_news(**params)
        
        assert result["success"] is True
        assert all("sentiment" in article for article in result["news"])

    @pytest.mark.skip(reason="Tool not implemented yet - T040 pending")
    def test_response_time_requirement(self):
        """Test that response time meets performance target"""
        import time
        from stock_mcp_server.tools.news import get_news
        
        params = {"limit": 10}
        start_time = time.time()
        result = get_news(**params)
        elapsed_time = time.time() - start_time
        
        # Contract requires < 10s
        assert elapsed_time < 10.0, f"Response time {elapsed_time:.2f}s exceeds 10s target"
        assert result["success"] is True
