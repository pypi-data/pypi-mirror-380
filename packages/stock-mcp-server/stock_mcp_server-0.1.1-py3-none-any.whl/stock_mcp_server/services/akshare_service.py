"""AKShare data service with retry logic and caching."""

import os
import time
from datetime import datetime
from decimal import Decimal
from typing import Any

import akshare as ak
import pandas as pd
import requests
from loguru import logger

from stock_mcp_server.models.market import MarketIndex, MarketBreadth, CapitalFlow
from stock_mcp_server.services.cache_service import get_cache
from stock_mcp_server.services.data_source_manager import get_data_source_manager
from stock_mcp_server.utils.date_utils import get_latest_trading_date, is_trading_time


# 配置反爬虫headers - 模拟真实浏览器
def _setup_anti_crawler_headers():
    """设置反爬虫headers，模拟真实浏览器访问"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Cache-Control': 'max-age=0',
    }
    
    # 修改requests的默认session
    session = requests.Session()
    session.headers.update(headers)
    
    # 猴子补丁：替换requests.get和requests.post
    original_get = requests.get
    original_post = requests.post
    
    def patched_get(*args, **kwargs):
        if 'headers' not in kwargs:
            kwargs['headers'] = headers
        else:
            kwargs['headers'] = {**headers, **kwargs['headers']}
        return original_get(*args, **kwargs)
    
    def patched_post(*args, **kwargs):
        if 'headers' not in kwargs:
            kwargs['headers'] = headers
        else:
            kwargs['headers'] = {**headers, **kwargs['headers']}
        return original_post(*args, **kwargs)
    
    requests.get = patched_get
    requests.post = patched_post
    
    return session


# 在模块加载时设置headers
_setup_anti_crawler_headers()


class AKShareService:
    """Service for fetching data from AKShare."""

    def __init__(self) -> None:
        """Initialize AKShare service."""
        self.cache = get_cache()
        self.data_source_manager = get_data_source_manager()  # 多数据源管理器
        self.retry_count = 3
        self.retry_delay = 2.0  # 增加到2秒，避免触发限流
        self.request_interval = 1.5  # 每次请求间隔1.5秒
        self._last_request_time = 0
        
        # Store original proxy settings
        self._original_http_proxy = os.environ.get('HTTP_PROXY')
        self._original_https_proxy = os.environ.get('HTTPS_PROXY')
        self._original_http_proxy_lower = os.environ.get('http_proxy')
        self._original_https_proxy_lower = os.environ.get('https_proxy')
        
        # Disable proxy for AKShare requests (accessing Chinese financial data sources)
        # This prevents proxy issues when accessing domestic websites
        os.environ['NO_PROXY'] = '*'
        os.environ['no_proxy'] = '*'
        if 'HTTP_PROXY' in os.environ:
            del os.environ['HTTP_PROXY']
        if 'HTTPS_PROXY' in os.environ:
            del os.environ['HTTPS_PROXY']
        if 'http_proxy' in os.environ:
            del os.environ['http_proxy']
        if 'https_proxy' in os.environ:
            del os.environ['https_proxy']
        
        logger.info("AKShare service initialized (multi-source enabled, anti-crawler enabled, proxy disabled)")

    def _retry_fetch(self, func: Any, *args: Any, **kwargs: Any) -> Any:
        """Retry fetching data with exponential backoff and rate limiting."""
        for attempt in range(self.retry_count):
            try:
                # Ensure proxy is disabled for each request
                os.environ['NO_PROXY'] = '*'
                os.environ['no_proxy'] = '*'
                for key in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy']:
                    if key in os.environ:
                        del os.environ[key]
                
                # 智能请求间隔：确保两次请求之间有足够的时间间隔
                current_time = time.time()
                elapsed = current_time - self._last_request_time
                if elapsed < self.request_interval:
                    sleep_time = self.request_interval - elapsed
                    logger.debug(f"Rate limiting: sleeping {sleep_time:.2f}s")
                    time.sleep(sleep_time)
                
                # 记录请求时间
                self._last_request_time = time.time()
                
                # 执行请求
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                if attempt == self.retry_count - 1:
                    logger.error(f"Failed after {self.retry_count} attempts: {e}")
                    raise
                # 指数退避：2秒、4秒、8秒
                backoff_time = self.retry_delay * (2**attempt)
                logger.warning(f"Attempt {attempt + 1} failed: {e}, retrying in {backoff_time}s...")
                time.sleep(backoff_time)
        return None

    def get_index_spot(self, index_code: str = "000001") -> MarketIndex | None:
        """
        Get real-time index data with multi-source fallback.
        
        Args:
            index_code: Index code (default: 000001 for Shanghai Composite)
            
        Returns:
            MarketIndex model or None if failed
        """
        # Check cache first
        cached = self.cache.get("market_data", index_code=index_code)
        if cached:
            logger.debug(f"Cache hit for index {index_code}")
            return cached

        try:
            # Use data source manager (auto-fallback to Tencent if Eastmoney fails)
            index_data = self.data_source_manager.get_index_spot(index_code)
            
            if index_data:
                # Cache the result
                self.cache.set("market_data", index_data, index_code=index_code)
                logger.info(f"Fetched index data: {index_code}")
                return index_data
            else:
                logger.warning(f"No data available for index {index_code}")
                return None

        except Exception as e:
            logger.error(f"Error fetching index data: {e}")
            return None

    def get_market_breadth(self, date: str | None = None) -> MarketBreadth | None:
        """
        Get market breadth statistics with multi-source fallback.
        
        Args:
            date: Trading date (YYYY-MM-DD) or None for latest
            
        Returns:
            MarketBreadth model or None if failed
        """
        if date is None:
            date = get_latest_trading_date()

        # Check cache
        cached = self.cache.get("market_data", type="breadth", date=date)
        if cached:
            return cached

        try:
            # Use data source manager
            breadth = self.data_source_manager.get_market_breadth(date)
            
            if breadth:
                self.cache.set("market_data", breadth, type="breadth", date=date)
                logger.info(f"Fetched market breadth for {date}")
                return breadth
            else:
                logger.warning("No market breadth data available")
                return None

        except Exception as e:
            logger.error(f"Error fetching market breadth: {e}")
            return None

    def get_capital_flow(self, date: str | None = None) -> CapitalFlow | None:
        """
        Get capital flow data with multi-source fallback.
        
        Args:
            date: Trading date or None for latest
            
        Returns:
            CapitalFlow model or None if failed
        """
        if date is None:
            date = get_latest_trading_date()

        # Check cache
        cached = self.cache.get("market_data", type="capital_flow", date=date)
        if cached:
            return cached

        try:
            # Use data source manager
            flow = self.data_source_manager.get_capital_flow(date)
            
            if flow:
                self.cache.set("market_data", flow, type="capital_flow", date=date)
                logger.info(f"Fetched capital flow for {date}")
                return flow
            else:
                logger.warning("No capital flow data available")
                return None

        except Exception as e:
            logger.error(f"Error fetching capital flow: {e}")
            return None

    def get_stock_hist(
        self,
        symbol: str,
        period: str = "daily",
        start_date: str | None = None,
        end_date: str | None = None,
        adjust: str = "qfq"
    ) -> list[dict] | None:
        """Get historical stock data.
        
        Args:
            symbol: Stock symbol (e.g., "000001" for index)
            period: Data period (daily/weekly/monthly)
            start_date: Start date (YYYY-MM-DD)
            end_date: End date (YYYY-MM-DD)
            adjust: Adjustment type (none/qfq/hfq)
            
        Returns:
            List of historical data dictionaries
        """
        try:
            # Get index historical data
            df = ak.stock_zh_index_daily(symbol=f"sh{symbol}")
            
            if df is None or df.empty:
                logger.warning(f"No historical data for {symbol}")
                return None
            
            # Filter by date range if specified
            if start_date:
                df = df[df["date"].astype(str) >= start_date]
            if end_date:
                df = df[df["date"].astype(str) <= end_date]
            
            # Convert to list of dicts
            result = df.to_dict("records")
            logger.info(f"Fetched {len(result)} days of historical data for {symbol}")
            return result
            
        except Exception as e:
            logger.error(f"Error fetching historical data for {symbol}: {e}")
            return None

    def get_news(self, limit: int = 10) -> list:
        """Get financial news from akshare.
        
        Args:
            limit: Number of news items to fetch
            
        Returns:
            List of NewsArticle objects
        """
        from stock_mcp_server.models.news import NewsArticle, NewsCategory
        from datetime import datetime
        
        articles = []
        
        try:
            # Try getting news from akshare stock news
            try:
                df = ak.stock_news_em()  # 东方财富新闻
                if df is not None and not df.empty:
                    for idx, row in df.head(limit).iterrows():
                        try:
                            article = NewsArticle(
                                title=str(row.get("新闻标题", "")),
                                url=str(row.get("新闻链接", "")),
                                source="东方财富",
                                published_at=datetime.now(),
                                category=NewsCategory.MARKET,
                                summary=str(row.get("新闻内容", ""))[:200] if "新闻内容" in row else None,
                                importance=5.0
                            )
                            articles.append(article)
                        except Exception as e:
                            logger.warning(f"Failed to parse news article: {e}")
                            continue
            except Exception as e:
                logger.warning(f"Failed to fetch from stock_news_em: {e}")
            
            logger.info(f"Fetched {len(articles)} news articles from akshare")
            
        except Exception as e:
            logger.error(f"Error fetching news from akshare: {e}")
        
        return articles


# Global instance
_akshare_service: AKShareService | None = None


def get_akshare_service() -> AKShareService:
    """Get global AKShare service instance."""
    global _akshare_service
    if _akshare_service is None:
        _akshare_service = AKShareService()
    return _akshare_service
