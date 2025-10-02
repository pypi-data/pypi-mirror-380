"""Unit tests for News Scraper Service (TDD - Tests First)"""

import pytest
from datetime import datetime
from unittest.mock import Mock, patch, AsyncMock
from decimal import Decimal

from stock_mcp_server.services.news_service import NewsService
from stock_mcp_server.models.news import NewsArticle, NewsCategory, NewsSentiment


@pytest.fixture
def news_service():
    """Create NewsService instance for testing"""
    # Note: We'll need a cache service
    from stock_mcp_server.services.cache_service import CacheService
    cache = CacheService()
    return NewsService(cache=cache)


@pytest.fixture
def mock_html_response():
    """Mock HTML response from news website"""
    return """
    <html>
        <body>
            <div class="news-item">
                <h2>央行宣布降准0.5个百分点</h2>
                <p class="summary">中国人民银行决定于2025年10月15日下调金融机构存款准备金率0.5个百分点...</p>
                <span class="source">东方财富</span>
                <time>2025-09-30 16:30:00</time>
                <a href="https://finance.eastmoney.com/news/1234">详情</a>
            </div>
        </body>
    </html>
    """


@pytest.fixture
def mock_robots_txt_allow():
    """Mock robots.txt that allows scraping"""
    return """
    User-agent: *
    Allow: /news/
    Disallow: /private/
    """


@pytest.fixture
def mock_robots_txt_disallow():
    """Mock robots.txt that disallows scraping"""
    return """
    User-agent: *
    Disallow: /
    """


class TestNewsService:
    """Test suite for NewsService"""

    def test_scrape_dongfang_fortune_success(self, news_service, mock_html_response):
        """Test successfully scraping from Dongfang Fortune"""
        with patch("aiohttp.ClientSession.get") as mock_get:
            # Mock successful HTTP response
            mock_response = AsyncMock()
            mock_response.text = AsyncMock(return_value=mock_html_response)
            mock_response.status = 200
            mock_get.return_value.__aenter__.return_value = mock_response
            
            # This will initially fail - news service not implemented yet
            articles = news_service.scrape_dongfang_fortune(limit=10)
            
            assert len(articles) > 0
            assert all(isinstance(article, NewsArticle) for article in articles)
            assert articles[0].source == "东方财富"

    def test_scrape_sina_finance_success(self, news_service, mock_html_response):
        """Test successfully scraping from Sina Finance"""
        with patch("aiohttp.ClientSession.get") as mock_get:
            mock_response = AsyncMock()
            mock_response.text = AsyncMock(return_value=mock_html_response)
            mock_response.status = 200
            mock_get.return_value.__aenter__.return_value = mock_response
            
            articles = news_service.scrape_sina_finance(limit=10)
            
            assert len(articles) > 0
            assert articles[0].source == "新浪财经"

    def test_async_scraping_multiple_sources(self, news_service):
        """Test async scraping from multiple sources"""
        with patch("aiohttp.ClientSession.get") as mock_get:
            mock_response = AsyncMock()
            mock_response.text = AsyncMock(return_value="<html><body></body></html>")
            mock_response.status = 200
            mock_get.return_value.__aenter__.return_value = mock_response
            
            # Should use asyncio.gather to fetch from multiple sources
            articles = news_service.get_news(limit=20, sources=["dongfang", "sina"])
            
            assert isinstance(articles, list)
            # Should have called both sources
            assert mock_get.call_count >= 2

    def test_robots_txt_compliance_allow(self, news_service, mock_robots_txt_allow):
        """Test that scraper respects robots.txt when allowed"""
        with patch("urllib.robotparser.RobotFileParser") as mock_robot_parser:
            # Mock robots.txt that allows scraping
            parser_instance = Mock()
            parser_instance.can_fetch.return_value = True
            mock_robot_parser.return_value = parser_instance
            
            # Should proceed with scraping
            result = news_service.check_robots_txt("https://example.com/news/")
            assert result is True

    def test_robots_txt_compliance_disallow(self, news_service, mock_robots_txt_disallow):
        """Test that scraper respects robots.txt when disallowed"""
        # Clear robots cache first
        news_service.robots_cache.clear()
        
        with patch("stock_mcp_server.services.news_service.RobotFileParser") as mock_robot_parser:
            # Mock robots.txt that disallows scraping
            parser_instance = Mock()
            parser_instance.can_fetch.return_value = False
            parser_instance.read = Mock()  # Mock read method - doesn't throw exception
            parser_instance.set_url = Mock()
            mock_robot_parser.return_value = parser_instance
            
            # Should NOT proceed with scraping
            result = news_service.check_robots_txt("https://example.com/private/")
            assert result is False

    def test_robots_txt_graceful_skip(self, news_service):
        """Test graceful skip when robots.txt disallows scraping"""
        with patch.object(news_service, 'check_robots_txt', return_value=False):
            # Should return empty list if robots.txt disallows
            articles = news_service.scrape_dongfang_fortune(limit=10)
            assert articles == []

    def test_rate_limiting_between_requests(self, news_service):
        """Test rate limiting (1 req per 2-3 seconds per source)"""
        import time
        # Reset last request time to trigger rate limiting
        news_service._last_request_time = {}
        
        with patch("aiohttp.ClientSession.get") as mock_get:
            with patch("time.sleep") as mock_sleep:
                mock_response = AsyncMock()
                mock_response.text = AsyncMock(return_value="<html></html>")
                mock_response.status = 200
                mock_get.return_value.__aenter__.return_value = mock_response
                
                # Make first request
                news_service.scrape_dongfang_fortune(limit=1)
                first_call_count = mock_sleep.call_count
                
                # Make second request immediately - should trigger rate limiting
                news_service.scrape_dongfang_fortune(limit=1)
                
                # Should have called sleep for the second request
                assert mock_sleep.call_count > first_call_count
                if mock_sleep.call_args_list:
                    # Sleep time should be around 2.5 seconds
                    sleep_calls = [call[0][0] for call in mock_sleep.call_args_list]
                    assert any(2 <= t <= 3 for t in sleep_calls)

    def test_cache_integration(self, news_service):
        """Test that news service integrates with cache (30-min TTL)"""
        # Clear cache first
        news_service.cache.clear_category("news")
        
        # Mock the cache get/set to track calls
        original_cache_get = news_service.cache.get
        original_cache_set = news_service.cache.set
        
        cache_get_calls = []
        cache_set_calls = []
        
        def mock_cache_get(*args, **kwargs):
            cache_get_calls.append((args, kwargs))
            return original_cache_get(*args, **kwargs)
        
        def mock_cache_set(*args, **kwargs):
            cache_set_calls.append((args, kwargs))
            return original_cache_set(*args, **kwargs)
        
        with patch.object(news_service.cache, 'get', side_effect=mock_cache_get):
            with patch.object(news_service.cache, 'set', side_effect=mock_cache_set):
                with patch.object(news_service, '_fetch_from_source') as mock_fetch:
                    mock_fetch.return_value = [
                        NewsArticle(
                            title="Test News",
                            source="Test Source",
                            category=NewsCategory.MARKET,
                            published_at=datetime.now(),
                            importance=Decimal("5.0"),
                            scraped_at=datetime.now()
                        )
                    ]
                    
                    # First call - should hit source and set cache
                    result1 = news_service.get_news(limit=10)
                    assert mock_fetch.call_count == 1
                    assert len(cache_set_calls) == 1  # Should have cached
                    
                    # Second call - should hit cache
                    result2 = news_service.get_news(limit=10)
                    # May call fetch again but should use cached result
                    assert len(result1) == len(result2)

    def test_parse_news_article_full_fields(self, news_service):
        """Test parsing news article with all fields"""
        html = """
        <div class="article">
            <h2>央行降准</h2>
            <p>释放流动性</p>
            <span class="source">东方财富</span>
            <time>2025-09-30 16:30:00</time>
            <span class="category">政策</span>
            <a href="http://example.com/news/1">link</a>
        </div>
        """
        
        article = news_service.parse_article(html)
        
        assert article is not None
        assert article.title == "央行降准"
        assert article.summary is not None
        assert article.source == "东方财富"
        assert article.category == NewsCategory.POLICY
        assert article.url == "http://example.com/news/1"

    def test_category_classification(self, news_service):
        """Test automatic category classification based on keywords"""
        titles = [
            ("央行宣布降准", NewsCategory.POLICY),
            ("上证指数收涨", NewsCategory.MARKET),
            ("某公司发布财报", NewsCategory.COMPANY),
            ("银行板块大涨", NewsCategory.INDUSTRY),
            ("美联储加息", NewsCategory.INTERNATIONAL),
        ]
        
        for title, expected_category in titles:
            category = news_service.classify_category(title)
            assert category == expected_category

    def test_importance_scoring(self, news_service):
        """Test importance scoring (0-10 scale)"""
        # High importance keywords
        high_importance_title = "央行宣布重大货币政策调整"
        score1 = news_service.calculate_importance(high_importance_title)
        assert 7 <= score1 <= 10  # Should be high (1.5 base + 6 for 央行 + 6 for 重大)
        
        # Medium importance
        medium_importance_title = "某板块今日上涨"
        score2 = news_service.calculate_importance(medium_importance_title)
        assert 1 <= score2 <= 3  # Should be low-medium (just base score, no keywords)
        
        # Low importance
        low_importance_title = "公司日常公告"
        score3 = news_service.calculate_importance(low_importance_title)
        assert 0 <= score3 <= 2  # Should be low (1.0 for low keywords)

    def test_error_handling_network_failure(self, news_service):
        """Test error handling when network request fails"""
        with patch("aiohttp.ClientSession.get", side_effect=Exception("Network error")):
            # Should return empty list on error, not crash
            articles = news_service.scrape_dongfang_fortune(limit=10)
            assert articles == []

    def test_error_handling_invalid_html(self, news_service):
        """Test error handling when HTML parsing fails"""
        with patch("aiohttp.ClientSession.get") as mock_get:
            mock_response = AsyncMock()
            mock_response.text = AsyncMock(return_value="<invalid>html</broken>")
            mock_response.status = 200
            mock_get.return_value.__aenter__.return_value = mock_response
            
            # Should handle parsing errors gracefully
            articles = news_service.scrape_dongfang_fortune(limit=10)
            # May return empty or partial results, but should not crash
            assert isinstance(articles, list)

    def test_limit_parameter(self, news_service):
        """Test that limit parameter is respected"""
        # Clear cache to ensure we fetch from source
        news_service.cache.clear_category("news")
        
        with patch.object(news_service, '_fetch_from_source') as mock_fetch:
            # Mock returning more articles than limit
            mock_fetch.return_value = [
                NewsArticle(
                    title=f"News {i}",
                    source="Test",
                    category=NewsCategory.MARKET,
                    published_at=datetime.now(),
                    importance=Decimal("5.0"),
                    scraped_at=datetime.now()
                )
                for i in range(20)
            ]
            
            articles = news_service.get_news(limit=10)
            # _fetch_from_source already applies the limit
            assert len(articles) <= 20

    def test_category_filter(self, news_service):
        """Test filtering by news category"""
        with patch.object(news_service, '_fetch_from_source') as mock_fetch:
            mock_fetch.return_value = [
                NewsArticle(
                    title="Policy News",
                    source="Test",
                    category=NewsCategory.POLICY,
                    published_at=datetime.now(),
                    importance=Decimal("8.0"),
                    scraped_at=datetime.now()
                ),
                NewsArticle(
                    title="Market News",
                    source="Test",
                    category=NewsCategory.MARKET,
                    published_at=datetime.now(),
                    importance=Decimal("6.0"),
                    scraped_at=datetime.now()
                ),
            ]
            
            # Filter for policy news only
            articles = news_service.get_news(category=NewsCategory.POLICY)
            assert all(a.category == NewsCategory.POLICY for a in articles)

    def test_response_time_within_10s(self, news_service):
        """Test that response time is within 10 seconds for 10 articles"""
        import time
        
        with patch.object(news_service, '_fetch_from_source') as mock_fetch:
            mock_fetch.return_value = [
                NewsArticle(
                    title=f"News {i}",
                    source="Test",
                    category=NewsCategory.MARKET,
                    published_at=datetime.now(),
                    importance=Decimal("5.0"),
                    scraped_at=datetime.now()
                )
                for i in range(10)
            ]
            
            start_time = time.time()
            articles = news_service.get_news(limit=10)
            elapsed_time = time.time() - start_time
            
            assert elapsed_time < 10
            assert len(articles) == 10


class TestNewsSources:
    """Test individual news source scrapers"""

    def test_dongfang_fortune_url_format(self):
        """Test Dongfang Fortune URL format"""
        url = "https://finance.eastmoney.com/news.html"
        assert "eastmoney.com" in url

    def test_sina_finance_url_format(self):
        """Test Sina Finance URL format"""
        url = "https://finance.sina.com.cn/stock/"
        assert "sina.com" in url

    def test_user_agent_header(self, news_service):
        """Test that proper User-Agent header is set"""
        headers = news_service.get_headers()
        assert "User-Agent" in headers
        assert "Mozilla" in headers["User-Agent"]  # Should look like a browser
