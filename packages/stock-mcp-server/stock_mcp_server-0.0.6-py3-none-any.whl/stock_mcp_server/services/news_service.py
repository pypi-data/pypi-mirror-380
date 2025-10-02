"""News Scraper Service - Web scraping for financial news with sentiment analysis"""

import asyncio
import time
from datetime import datetime, timedelta
from decimal import Decimal
from typing import List, Optional
from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin, urlparse

import aiohttp
from bs4 import BeautifulSoup
from loguru import logger

from stock_mcp_server.models.news import NewsArticle, NewsCategory, NewsSentiment
from stock_mcp_server.services.cache_service import CacheService


class NewsService:
    """News scraping service with async fetching and caching"""

    def __init__(self, cache: Optional[CacheService] = None):
        """Initialize news service

        Args:
            cache: Cache service instance (optional)
        """
        self.cache = cache or CacheService()
        self.sources = {
            "dongfang": "https://finance.eastmoney.com/news.html",
            "sina": "https://finance.sina.com.cn/stock/",
        }
        self.robots_cache = {}  # Cache robots.txt results
        self._last_request_time = {}  # Track last request time per source
        logger.info("News service initialized")

    def fetch_latest_news(
        self,
        limit: int = 10,
        category: Optional[NewsCategory] = None,
        hours_back: int = 24
    ) -> List[NewsArticle]:
        """Fetch latest news articles.
        
        Args:
            limit: Maximum number of articles to return
            category: Filter by category (optional)
            hours_back: How many hours back to fetch news
            
        Returns:
            List of news articles
        """
        try:
            # Use get_news to fetch articles
            articles = self.get_news(
                category=category or NewsCategory.ALL,
                limit=limit,
                hours_back=hours_back
            )
            return articles
        except Exception as e:
            logger.error(f"Failed to fetch latest news: {e}")
            return []

    def get_headers(self) -> dict:
        """Get HTTP headers for requests"""
        return {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/91.0.4472.124 Safari/537.36"
        }

    def check_robots_txt(self, url: str) -> bool:
        """Check if URL is allowed by robots.txt

        Args:
            url: URL to check

        Returns:
            True if allowed, False otherwise
        """
        try:
            parsed = urlparse(url)
            base_url = f"{parsed.scheme}://{parsed.netloc}"
            robots_url = urljoin(base_url, "/robots.txt")

            # Check cache first
            if robots_url in self.robots_cache:
                parser = self.robots_cache[robots_url]
            else:
                parser = RobotFileParser()
                parser.set_url(robots_url)
                try:
                    parser.read()
                except Exception:
                    # If we can't read robots.txt, be conservative and allow
                    logger.debug(f"Could not read robots.txt from {robots_url}, allowing access")
                    return True
                self.robots_cache[robots_url] = parser

            # Check if our User-Agent can fetch this URL
            can_fetch = parser.can_fetch("*", url)
            logger.debug(f"robots.txt check for {url}: {can_fetch}")
            return can_fetch

        except Exception as e:
            logger.warning(f"Failed to check robots.txt for {url}: {e}")
            # If we can't check robots.txt, allow (be conservative)
            return True

    def _rate_limit(self, source: str, delay: float = 2.5):
        """Apply rate limiting between requests

        Args:
            source: Source name
            delay: Delay in seconds (default 2.5s)
        """
        last_time = self._last_request_time.get(source, 0)
        elapsed = time.time() - last_time
        if elapsed < delay:
            sleep_time = delay - elapsed
            logger.debug(f"Rate limiting {source}: sleeping {sleep_time:.2f}s")
            time.sleep(sleep_time)
        self._last_request_time[source] = time.time()

    async def _fetch_html(self, url: str) -> Optional[str]:
        """Fetch HTML content from URL

        Args:
            url: URL to fetch

        Returns:
            HTML content or None if failed
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.get_headers(), timeout=10) as response:
                    if response.status == 200:
                        return await response.text()
                    else:
                        logger.warning(f"Failed to fetch {url}: HTTP {response.status}")
                        return None
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return None

    def parse_article(self, html: str) -> Optional[NewsArticle]:
        """Parse news article from HTML

        Args:
            html: HTML content

        Returns:
            NewsArticle or None if parsing fails
        """
        try:
            soup = BeautifulSoup(html, "lxml")

            # Try to extract title
            title_elem = soup.find("h2") or soup.find("h1") or soup.find(class_="title")
            title = title_elem.get_text().strip() if title_elem else "Unknown"

            # Try to extract summary
            summary_elem = soup.find("p", class_="summary") or soup.find("p")
            summary = summary_elem.get_text().strip() if summary_elem else None

            # Try to extract source
            source_elem = soup.find(class_="source") or soup.find("span", class_="source")
            source = source_elem.get_text().strip() if source_elem else "Unknown"

            # Try to extract time
            time_elem = soup.find("time") or soup.find(class_="time")
            published_at = datetime.now()  # Default to now
            if time_elem:
                time_str = time_elem.get_text().strip()
                try:
                    published_at = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    pass

            # Try to extract URL
            link_elem = soup.find("a")
            url = link_elem.get("href") if link_elem else None

            # Classify category based on title
            category = self.classify_category(title)

            # Calculate importance
            importance = self.calculate_importance(title)

            return NewsArticle(
                title=title,
                summary=summary,
                source=source,
                category=category,
                published_at=published_at,
                importance=importance,
                url=url,
                scraped_at=datetime.now()
            )

        except Exception as e:
            logger.error(f"Error parsing article: {e}")
            return None

    def classify_category(self, title: str) -> NewsCategory:
        """Classify news category based on title keywords

        Args:
            title: News title

        Returns:
            NewsCategory
        """
        title_lower = title.lower()

        # International keywords (check first to avoid "美联储加息" being classified as policy)
        if any(kw in title for kw in ["美联储", "美国", "欧洲", "日本", "国际", "海外", "全球"]):
            return NewsCategory.INTERNATIONAL

        # Policy keywords
        if any(kw in title for kw in ["央行", "货币政策", "降准", "加息", "政策", "国务院", "发改委"]):
            return NewsCategory.POLICY

        # Company keywords
        if any(kw in title for kw in ["公司", "企业", "财报", "业绩", "股份", "集团"]):
            return NewsCategory.COMPANY

        # Industry keywords
        if any(kw in title for kw in ["行业", "板块", "银行", "地产", "科技", "医药", "能源"]):
            return NewsCategory.INDUSTRY

        # Default to market
        return NewsCategory.MARKET

    def calculate_importance(self, title: str) -> Decimal:
        """Calculate news importance score (0-10)

        Args:
            title: News title

        Returns:
            Importance score
        """
        score = 1.5  # Very low base score

        # High importance keywords (+6)
        high_keywords = ["央行", "重大", "突发", "紧急", "货币政策", "降准", "加息", "崩盘", "暴跌", "暴涨"]
        for kw in high_keywords:
            if kw in title:
                score += 6
                break

        # Medium importance keywords (+3)
        medium_keywords = ["政策", "改革", "监管", "调整", "变化", "影响"]
        for kw in medium_keywords:
            if kw in title:
                score += 3
                break

        # Low importance (just informational)
        low_keywords = ["公司", "公告", "日常"]
        has_low = any(kw in title for kw in low_keywords)
        if has_low and score == 1.5:  # No high/medium keywords
            score = 1.0  # Keep it low

        # Exclamation or question marks (+0.5)
        if "！" in title or "？" in title:
            score += 0.5

        # Cap at 10
        return Decimal(str(min(score, 10.0)))

    def scrape_dongfang_fortune(self, limit: int = 10) -> List[NewsArticle]:
        """Scrape news from Dongfang Fortune

        Args:
            limit: Maximum number of articles

        Returns:
            List of NewsArticle
        """
        url = self.sources["dongfang"]

        # Check robots.txt
        if not self.check_robots_txt(url):
            logger.warning(f"Robots.txt disallows scraping {url}")
            return []

        # Apply rate limiting
        self._rate_limit("dongfang")

        try:
            logger.info(f"Scraping Dongfang Fortune (limit={limit})")
            
            # Fetch HTML using asyncio
            import asyncio
            html = asyncio.run(self._fetch_html(url))
            
            if not html:
                return []
            
            # Parse HTML
            soup = BeautifulSoup(html, "lxml")
            articles = []
            
            # Find all news items (adjust selectors based on actual site structure)
            news_items = soup.find_all("div", class_="news-item", limit=limit)
            if not news_items:
                # Fallback: try to find any div/article elements
                news_items = soup.find_all(["div", "article"], limit=limit)
            
            for item in news_items[:limit]:
                try:
                    # Extract title
                    title_elem = item.find("h2") or item.find("h1") or item.find(class_="title")
                    if not title_elem:
                        continue
                    title = title_elem.get_text().strip()
                    
                    # Extract summary
                    summary_elem = item.find("p", class_="summary") or item.find("p")
                    summary = summary_elem.get_text().strip() if summary_elem else None
                    
                    # Extract time
                    time_elem = item.find("time") or item.find(class_="time")
                    published_at = datetime.now()
                    if time_elem:
                        time_str = time_elem.get_text().strip()
                        try:
                            published_at = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
                        except ValueError:
                            pass
                    
                    # Extract URL
                    link_elem = item.find("a")
                    article_url = link_elem.get("href") if link_elem else None
                    
                    # Create article
                    article = NewsArticle(
                        title=title,
                        summary=summary,
                        source="东方财富",
                        category=self.classify_category(title),
                        published_at=published_at,
                        importance=self.calculate_importance(title),
                        url=article_url,
                        scraped_at=datetime.now()
                    )
                    articles.append(article)
                    
                except Exception as e:
                    logger.debug(f"Failed to parse news item: {e}")
                    continue
            
            logger.info(f"Scraped {len(articles)} articles from Dongfang Fortune")
            return articles

        except Exception as e:
            logger.error(f"Error scraping Dongfang Fortune: {e}")
            return []

    def scrape_sina_finance(self, limit: int = 10) -> List[NewsArticle]:
        """Scrape news from Sina Finance

        Args:
            limit: Maximum number of articles

        Returns:
            List of NewsArticle
        """
        url = self.sources["sina"]

        # Check robots.txt
        if not self.check_robots_txt(url):
            logger.warning(f"Robots.txt disallows scraping {url}")
            return []

        # Apply rate limiting
        self._rate_limit("sina")

        try:
            logger.info(f"Scraping Sina Finance (limit={limit})")
            
            # Fetch HTML using asyncio
            import asyncio
            html = asyncio.run(self._fetch_html(url))
            
            if not html:
                return []
            
            # Parse HTML
            soup = BeautifulSoup(html, "lxml")
            articles = []
            
            # Find all news items
            news_items = soup.find_all("div", class_="news-item", limit=limit)
            if not news_items:
                news_items = soup.find_all(["div", "article"], limit=limit)
            
            for item in news_items[:limit]:
                try:
                    # Extract title
                    title_elem = item.find("h2") or item.find("h1") or item.find(class_="title")
                    if not title_elem:
                        continue
                    title = title_elem.get_text().strip()
                    
                    # Extract summary
                    summary_elem = item.find("p", class_="summary") or item.find("p")
                    summary = summary_elem.get_text().strip() if summary_elem else None
                    
                    # Extract time
                    time_elem = item.find("time") or item.find(class_="time")
                    published_at = datetime.now()
                    if time_elem:
                        time_str = time_elem.get_text().strip()
                        try:
                            published_at = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
                        except ValueError:
                            pass
                    
                    # Extract URL
                    link_elem = item.find("a")
                    article_url = link_elem.get("href") if link_elem else None
                    
                    # Create article
                    article = NewsArticle(
                        title=title,
                        summary=summary,
                        source="新浪财经",
                        category=self.classify_category(title),
                        published_at=published_at,
                        importance=self.calculate_importance(title),
                        url=article_url,
                        scraped_at=datetime.now()
                    )
                    articles.append(article)
                    
                except Exception as e:
                    logger.debug(f"Failed to parse news item: {e}")
                    continue
            
            logger.info(f"Scraped {len(articles)} articles from Sina Finance")
            return articles

        except Exception as e:
            logger.error(f"Error scraping Sina Finance: {e}")
            return []

    def _fetch_from_source(self, sources: List[str], limit: int) -> List[NewsArticle]:
        """Fetch articles from specified sources

        Args:
            sources: List of source names
            limit: Maximum number of articles

        Returns:
            List of NewsArticle
        """
        all_articles = []

        for source in sources:
            if source == "dongfang":
                articles = self.scrape_dongfang_fortune(limit=limit)
                all_articles.extend(articles)
            elif source == "sina":
                articles = self.scrape_sina_finance(limit=limit)
                all_articles.extend(articles)

        # Sort by importance and published time
        all_articles.sort(key=lambda x: (x.importance, x.published_at), reverse=True)

        return all_articles[:limit]

    def get_news(
        self,
        limit: int = 10,
        category: Optional[NewsCategory] = None,
        sources: Optional[List[str]] = None
    ) -> List[NewsArticle]:
        """Get news articles with caching

        Args:
            limit: Maximum number of articles
            category: Filter by category (optional)
            sources: List of sources to fetch from (default: all)

        Returns:
            List of NewsArticle
        """
        if sources is None:
            sources = ["dongfang", "sina"]

        # Check cache first
        cache_key = f"news_{'-'.join(sources)}_{category or 'all'}_{limit}"
        cached = self.cache.get("news", source=cache_key)
        if cached:
            logger.info(f"Cache hit for news: {cache_key}")
            return cached

        # Fetch from sources
        logger.info(f"Fetching news from sources: {sources}")
        articles = self._fetch_from_source(sources, limit)

        # Filter by category if specified
        if category:
            articles = [a for a in articles if a.category == category][:limit]

        # Cache for 30 minutes
        if articles:
            self.cache.set(
                "news",
                articles,
                ttl=1800,  # 30 minutes
                source=cache_key
            )

        return articles


# Singleton instance
_news_service_instance: Optional[NewsService] = None


def get_news_service() -> NewsService:
    """Get singleton NewsService instance"""
    global _news_service_instance
    if _news_service_instance is None:
        _news_service_instance = NewsService()
    return _news_service_instance
