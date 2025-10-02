"""Market sentiment and investment recommendation models."""

from datetime import datetime
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field


class SentimentLevel(str, Enum):
    """Sentiment classification levels."""

    EXTREME_PANIC = "extreme_panic"  # 极度恐慌 (0-20)
    PANIC = "panic"  # 恐慌 (21-40)
    NEUTRAL = "neutral"  # 中性 (41-60)
    OPTIMISTIC = "optimistic"  # 乐观 (61-80)
    EXTREME_OPTIMISM = "extreme_optimism"  # 极度乐观 (81-100)


class MarketSentiment(BaseModel):
    """Market sentiment analysis."""

    # Overall sentiment
    sentiment_index: Decimal = Field(
        ..., ge=0, le=100, description="Overall sentiment score (0-100)"
    )
    sentiment_level: SentimentLevel = Field(..., description="Sentiment classification")

    # Component scores
    volume_sentiment: Decimal = Field(..., ge=0, le=100, description="Volume-based sentiment")
    price_sentiment: Decimal = Field(..., ge=0, le=100, description="Price movement sentiment")
    volatility_sentiment: Decimal = Field(..., ge=0, le=100, description="Volatility sentiment")
    capital_sentiment: Decimal = Field(..., ge=0, le=100, description="Capital flow sentiment")
    news_sentiment: Decimal | None = Field(None, ge=0, le=100, description="News sentiment")

    # Component weights (for transparency)
    weights: dict[str, Decimal] = Field(
        default={
            "volume": Decimal("0.25"),
            "price": Decimal("0.35"),
            "volatility": Decimal("0.15"),
            "capital": Decimal("0.15"),
            "news": Decimal("0.10"),
        },
        description="Weights used in sentiment calculation",
    )

    # Trend
    sentiment_trend: str | None = Field(None, description="Trend: improving/deteriorating/stable")
    previous_sentiment: Decimal | None = Field(
        None, description="Previous day sentiment for comparison"
    )
    sentiment_change: Decimal | None = Field(None, description="Change from previous day")

    # Interpretation
    interpretation: str = Field(..., description="Human-readable sentiment interpretation")
    risk_level: str | None = Field(None, description="Risk level: low/medium/high/extreme")

    # Metadata
    date: str = Field(..., description="Analysis date")
    calculated_at: datetime = Field(..., description="Calculation timestamp")

    class Config:
        json_schema_extra = {
            "example": {
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
                    "news": 0.10,
                },
                "sentiment_trend": "improving",
                "previous_sentiment": 58.5,
                "sentiment_change": 4.0,
                "interpretation": "市场情绪偏乐观,成交活跃,资金流入积极,建议适当参与",
                "risk_level": "medium",
                "date": "2025-09-30",
                "calculated_at": "2025-09-30T15:45:00+08:00",
            }
        }


class MarketOutlook(str, Enum):
    """Market outlook classification."""

    BULLISH = "bullish"  # 看多
    BEARISH = "bearish"  # 看空
    SIDEWAYS = "sideways"  # 震荡


class OperationSuggestion(str, Enum):
    """Operation suggestion."""

    AGGRESSIVE = "aggressive"  # 积极
    CAUTIOUS = "cautious"  # 谨慎
    WAIT = "wait"  # 观望


class PositionRecommendation(str, Enum):
    """Position sizing recommendation."""

    HEAVY = "heavy"  # 重仓 (70-100%)
    HALF = "half"  # 半仓 (40-70%)
    LIGHT = "light"  # 轻仓 (10-40%)
    EMPTY = "empty"  # 空仓 (0-10%)


class InvestmentRecommendation(BaseModel):
    """Investment recommendation with multi-dimensional analysis."""

    # Core recommendations
    market_outlook: MarketOutlook = Field(..., description="Overall market view")
    operation_suggestion: OperationSuggestion = Field(..., description="Suggested approach")
    position_recommendation: PositionRecommendation = Field(..., description="Position sizing")

    # Multi-dimensional analysis
    technical_analysis: str = Field(..., description="Technical analysis summary")
    fundamental_analysis: str = Field(..., description="Fundamental/market breadth analysis")
    sentiment_analysis: str = Field(..., description="Sentiment analysis summary")
    capital_analysis: str = Field(..., description="Capital flow analysis")
    news_analysis: str | None = Field(None, description="News impact analysis")

    # Risk assessment
    risk_level: str = Field(..., description="低风险/中等风险/高风险/极高风险")
    risk_factors: list[str] = Field(..., description="Key risk factors")
    risk_warning: str = Field(..., description="Risk warning statement")

    # Actionable insights
    key_focus_points: list[str] = Field(..., description="Key points to watch")
    operational_strategy: str = Field(..., description="Specific operational strategy")

    # Confidence & disclaimers
    confidence_score: Decimal | None = Field(
        None, ge=0, le=100, description="Recommendation confidence"
    )
    disclaimer: str = Field(
        default="本建议仅供参考，不构成投资建议。投资有风险，入市需谨慎。", description="Investment disclaimer"
    )

    # Metadata
    analysis_depth: str = Field(..., description="simple/normal/detailed")
    generated_at: datetime = Field(..., description="Generation timestamp")
    valid_until: datetime | None = Field(None, description="Recommendation validity period")

    class Config:
        json_schema_extra = {
            "example": {
                "market_outlook": "bullish",
                "operation_suggestion": "cautious",
                "position_recommendation": "half",
                "technical_analysis": "短期均线多头排列，MACD金叉，RSI处于正常区间，技术面偏多",
                "fundamental_analysis": "涨跌家数比2:1，市场宽度良好，成交量放大，市场参与度较高",
                "sentiment_analysis": "市场情绪指数62.5，处于偏乐观区间，但需注意是否过热",
                "capital_analysis": "北向资金净流入16亿，主力资金小幅流出12亿，观望情绪浓厚",
                "news_analysis": "央行降准利好，释放流动性，短期提振市场信心",
                "risk_level": "中等风险",
                "risk_factors": [
                    "市场情绪偏高，需警惕回调风险",
                    "主力资金流出，缺乏持续性支撑",
                    "外部环境仍有不确定性",
                ],
                "risk_warning": "市场短期波动可能加大，建议控制仓位，设置止损",
                "key_focus_points": [
                    "关注北向资金动向",
                    "留意主力资金是否回流",
                    "关注量能是否持续放大",
                ],
                "operational_strategy": "建议半仓操作，可逢低适当加仓，重点关注银行、地产等政策受益板块",
                "confidence_score": 72.5,
                "disclaimer": "本建议仅供参考，不构成投资建议。投资有风险，入市需谨慎。",
                "analysis_depth": "detailed",
                "generated_at": "2025-09-30T16:00:00+08:00",
                "valid_until": "2025-10-01T09:30:00+08:00",
            }
        }

