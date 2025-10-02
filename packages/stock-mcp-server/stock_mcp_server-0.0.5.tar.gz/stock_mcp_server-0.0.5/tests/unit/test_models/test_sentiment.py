"""Unit tests for sentiment models."""

import pytest
from datetime import datetime
from decimal import Decimal

from stock_mcp_server.models.sentiment import (
    MarketSentiment,
    SentimentLevel,
    InvestmentRecommendation,
    MarketOutlook,
    OperationSuggestion,
    PositionRecommendation,
)


class TestMarketSentiment:
    """Tests for MarketSentiment model."""

    def test_valid_market_sentiment(self):
        """Test creating valid market sentiment."""
        sentiment = MarketSentiment(
            sentiment_index=Decimal("62.5"),
            sentiment_level=SentimentLevel.OPTIMISTIC,
            volume_sentiment=Decimal("70.0"),
            price_sentiment=Decimal("68.0"),
            volatility_sentiment=Decimal("55.0"),
            capital_sentiment=Decimal("58.0"),
            news_sentiment=Decimal("65.0"),
            interpretation="市场情绪偏乐观",
            date="2025-09-30",
            calculated_at=datetime.now(),
        )
        assert sentiment.sentiment_index == Decimal("62.5")
        assert sentiment.sentiment_level == SentimentLevel.OPTIMISTIC

    def test_sentiment_index_range(self):
        """Test sentiment index must be 0-100."""
        # Valid
        sentiment = MarketSentiment(
            sentiment_index=Decimal("50.0"),
            sentiment_level=SentimentLevel.NEUTRAL,
            volume_sentiment=Decimal("50.0"),
            price_sentiment=Decimal("50.0"),
            volatility_sentiment=Decimal("50.0"),
            capital_sentiment=Decimal("50.0"),
            interpretation="中性",
            date="2025-09-30",
            calculated_at=datetime.now(),
        )
        assert sentiment.sentiment_index == Decimal("50.0")

        # Invalid: > 100
        with pytest.raises(ValueError):
            MarketSentiment(
                sentiment_index=Decimal("101.0"),  # Invalid
                sentiment_level=SentimentLevel.NEUTRAL,
                volume_sentiment=Decimal("50.0"),
                price_sentiment=Decimal("50.0"),
                volatility_sentiment=Decimal("50.0"),
                capital_sentiment=Decimal("50.0"),
                interpretation="测试",
                date="2025-09-30",
                calculated_at=datetime.now(),
            )

    def test_sentiment_levels(self):
        """Test all sentiment levels."""
        assert SentimentLevel.EXTREME_PANIC.value == "extreme_panic"
        assert SentimentLevel.PANIC.value == "panic"
        assert SentimentLevel.NEUTRAL.value == "neutral"
        assert SentimentLevel.OPTIMISTIC.value == "optimistic"
        assert SentimentLevel.EXTREME_OPTIMISM.value == "extreme_optimism"

    def test_component_scores_range(self):
        """Test all component scores are 0-100."""
        sentiment = MarketSentiment(
            sentiment_index=Decimal("60.0"),
            sentiment_level=SentimentLevel.OPTIMISTIC,
            volume_sentiment=Decimal("100.0"),  # Max
            price_sentiment=Decimal("0.0"),     # Min
            volatility_sentiment=Decimal("50.0"),
            capital_sentiment=Decimal("50.0"),
            interpretation="测试",
            date="2025-09-30",
            calculated_at=datetime.now(),
        )
        assert sentiment.volume_sentiment == Decimal("100.0")
        assert sentiment.price_sentiment == Decimal("0.0")


class TestInvestmentRecommendation:
    """Tests for InvestmentRecommendation model."""

    def test_valid_recommendation(self):
        """Test creating valid investment recommendation."""
        rec = InvestmentRecommendation(
            market_outlook=MarketOutlook.BULLISH,
            operation_suggestion=OperationSuggestion.CAUTIOUS,
            position_recommendation=PositionRecommendation.HALF,
            technical_analysis="技术面偏多",
            fundamental_analysis="市场宽度良好",
            sentiment_analysis="情绪偏乐观",
            capital_analysis="北向资金流入",
            risk_level="中等风险",
            risk_factors=["风险1", "风险2"],
            risk_warning="控制仓位",
            key_focus_points=["关注点1", "关注点2"],
            operational_strategy="半仓操作",
            analysis_depth="detailed",
            generated_at=datetime.now(),
        )
        assert rec.market_outlook == MarketOutlook.BULLISH
        assert rec.operation_suggestion == OperationSuggestion.CAUTIOUS
        assert rec.position_recommendation == PositionRecommendation.HALF

    def test_market_outlook_types(self):
        """Test market outlook types."""
        assert MarketOutlook.BULLISH.value == "bullish"
        assert MarketOutlook.BEARISH.value == "bearish"
        assert MarketOutlook.SIDEWAYS.value == "sideways"

    def test_operation_suggestions(self):
        """Test operation suggestion types."""
        assert OperationSuggestion.AGGRESSIVE.value == "aggressive"
        assert OperationSuggestion.CAUTIOUS.value == "cautious"
        assert OperationSuggestion.WAIT.value == "wait"

    def test_position_recommendations(self):
        """Test position recommendation types."""
        assert PositionRecommendation.HEAVY.value == "heavy"
        assert PositionRecommendation.HALF.value == "half"
        assert PositionRecommendation.LIGHT.value == "light"
        assert PositionRecommendation.EMPTY.value == "empty"

    def test_confidence_score_range(self):
        """Test confidence score is 0-100 if provided."""
        rec = InvestmentRecommendation(
            market_outlook=MarketOutlook.BULLISH,
            operation_suggestion=OperationSuggestion.CAUTIOUS,
            position_recommendation=PositionRecommendation.HALF,
            technical_analysis="测试",
            fundamental_analysis="测试",
            sentiment_analysis="测试",
            capital_analysis="测试",
            risk_level="低风险",
            risk_factors=[],
            risk_warning="测试",
            key_focus_points=[],
            operational_strategy="测试",
            confidence_score=Decimal("75.0"),
            analysis_depth="simple",
            generated_at=datetime.now(),
        )
        assert rec.confidence_score == Decimal("75.0")

    def test_default_disclaimer(self):
        """Test default disclaimer is present."""
        rec = InvestmentRecommendation(
            market_outlook=MarketOutlook.BULLISH,
            operation_suggestion=OperationSuggestion.CAUTIOUS,
            position_recommendation=PositionRecommendation.HALF,
            technical_analysis="测试",
            fundamental_analysis="测试",
            sentiment_analysis="测试",
            capital_analysis="测试",
            risk_level="低风险",
            risk_factors=[],
            risk_warning="测试",
            key_focus_points=[],
            operational_strategy="测试",
            analysis_depth="simple",
            generated_at=datetime.now(),
        )
        assert "投资有风险" in rec.disclaimer
