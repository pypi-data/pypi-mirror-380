"""Unit tests for news models."""

import pytest
from datetime import datetime
from decimal import Decimal

from stock_mcp_server.models.news import (
    NewsArticle,
    NewsCategory,
    NewsSentiment,
)


class TestNewsArticle:
    """Tests for NewsArticle model."""

    def test_valid_news_article(self):
        """Test creating valid news article."""
        article = NewsArticle(
            title="央行宣布降准0.5个百分点",
            summary="中国人民银行决定于2025年10月15日下调金融机构存款准备金率...",
            url="https://finance.eastmoney.com/...",
            category=NewsCategory.POLICY,
            source="东方财富",
            published_at=datetime.now(),
            importance=Decimal("9.5"),
            sentiment=NewsSentiment.POSITIVE,
            sentiment_score=Decimal("0.85"),
            scraped_at=datetime.now(),
        )
        assert article.title == "央行宣布降准0.5个百分点"
        assert article.category == NewsCategory.POLICY
        assert article.sentiment == NewsSentiment.POSITIVE

    def test_importance_range(self):
        """Test importance score is between 0-10."""
        # Valid: 0-10
        article = NewsArticle(
            title="Test",
            category=NewsCategory.MARKET,
            source="测试",
            published_at=datetime.now(),
            importance=Decimal("5.0"),
            scraped_at=datetime.now(),
        )
        assert article.importance == Decimal("5.0")

        # Invalid: > 10
        with pytest.raises(ValueError):
            NewsArticle(
                title="Test",
                category=NewsCategory.MARKET,
                source="测试",
                published_at=datetime.now(),
                importance=Decimal("11.0"),  # Invalid
                scraped_at=datetime.now(),
            )

    def test_sentiment_score_range(self):
        """Test sentiment score is between 0-1."""
        # Valid
        article = NewsArticle(
            title="Test",
            category=NewsCategory.MARKET,
            source="测试",
            published_at=datetime.now(),
            importance=Decimal("5.0"),
            sentiment_score=Decimal("0.75"),
            scraped_at=datetime.now(),
        )
        assert article.sentiment_score == Decimal("0.75")

        # Invalid: > 1
        with pytest.raises(ValueError):
            NewsArticle(
                title="Test",
                category=NewsCategory.MARKET,
                source="测试",
                published_at=datetime.now(),
                importance=Decimal("5.0"),
                sentiment_score=Decimal("1.5"),  # Invalid
                scraped_at=datetime.now(),
            )

    def test_news_categories(self):
        """Test all news categories."""
        assert NewsCategory.POLICY.value == "policy"
        assert NewsCategory.MARKET.value == "market"
        assert NewsCategory.COMPANY.value == "company"
        assert NewsCategory.INDUSTRY.value == "industry"
        assert NewsCategory.INTERNATIONAL.value == "international"

    def test_news_sentiment_types(self):
        """Test news sentiment types."""
        assert NewsSentiment.POSITIVE.value == "positive"
        assert NewsSentiment.NEUTRAL.value == "neutral"
        assert NewsSentiment.NEGATIVE.value == "negative"

    def test_optional_fields(self):
        """Test optional fields can be None."""
        article = NewsArticle(
            title="Test",
            category=NewsCategory.MARKET,
            source="测试",
            published_at=datetime.now(),
            importance=Decimal("5.0"),
            scraped_at=datetime.now(),
        )
        assert article.summary is None
        assert article.content is None
        assert article.sentiment is None
        assert article.related_stocks is None
