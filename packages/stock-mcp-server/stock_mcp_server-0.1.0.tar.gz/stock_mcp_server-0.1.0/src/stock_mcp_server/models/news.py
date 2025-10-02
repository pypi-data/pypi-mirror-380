"""News article models."""

from datetime import datetime
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field


class NewsCategory(str, Enum):
    """News categories."""

    POLICY = "policy"  # 政策
    MARKET = "market"  # 市场
    COMPANY = "company"  # 公司
    INDUSTRY = "industry"  # 行业
    INTERNATIONAL = "international"  # 国际
    ALL = "all"  # 全部


class NewsSentiment(str, Enum):
    """News sentiment classification."""

    POSITIVE = "positive"  # 利好
    NEUTRAL = "neutral"  # 中性
    NEGATIVE = "negative"  # 利空


class NewsArticle(BaseModel):
    """Financial news article with sentiment analysis."""

    # Content
    title: str = Field(..., description="News title")
    summary: str | None = Field(None, description="News summary/excerpt")
    content: str | None = Field(None, description="Full content if available")
    url: str | None = Field(None, description="Source URL")

    # Classification
    category: NewsCategory = Field(..., description="News category")
    source: str = Field(..., description="News source, e.g., '东方财富'")
    published_at: datetime = Field(..., description="Publication timestamp")

    # Analysis
    importance: Decimal = Field(..., ge=0, le=10, description="Importance score (0-10)")
    sentiment: NewsSentiment | None = Field(None, description="Sentiment classification")
    sentiment_score: Decimal | None = Field(None, ge=0, le=1, description="Sentiment score (0-1)")

    # Relations
    related_stocks: list[str] | None = Field(None, description="Related stock codes")
    related_sectors: list[str] | None = Field(None, description="Related sectors")
    tags: list[str] | None = Field(None, description="Keywords/tags")

    # Impact
    market_impact: str | None = Field(None, description="全市场/行业/个股")
    time_horizon: str | None = Field(None, description="长期/中期/短期")

    # Metadata
    scraped_at: datetime = Field(..., description="When the news was scraped")

    class Config:
        json_schema_extra = {
            "example": {
                "title": "央行宣布降准0.5个百分点 释放流动性约1.2万亿",
                "summary": "中国人民银行决定于2025年10月15日下调金融机构存款准备金率0.5个百分点...",
                "content": None,
                "url": "https://finance.eastmoney.com/...",
                "category": "policy",
                "source": "东方财富",
                "published_at": "2025-09-30T16:30:00+08:00",
                "importance": 9.5,
                "sentiment": "positive",
                "sentiment_score": 0.85,
                "related_stocks": None,
                "related_sectors": ["银行", "房地产"],
                "tags": ["货币政策", "降准", "流动性"],
                "market_impact": "全市场",
                "time_horizon": "中期",
                "scraped_at": "2025-09-30T17:00:00+08:00",
            }
        }

