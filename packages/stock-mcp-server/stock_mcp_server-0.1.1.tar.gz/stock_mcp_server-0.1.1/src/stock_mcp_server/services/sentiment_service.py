"""Sentiment Analysis Service - Chinese text sentiment analysis with SnowNLP"""

from datetime import datetime
from decimal import Decimal
from typing import List, Optional, Dict

from snownlp import SnowNLP
from loguru import logger

from stock_mcp_server.models.sentiment import MarketSentiment, SentimentLevel
from stock_mcp_server.models.news import NewsArticle


class SentimentService:
    """Sentiment analysis service using SnowNLP and domain knowledge"""

    def __init__(self):
        """Initialize sentiment service"""
        # Financial domain keywords with weights
        self._positive_keywords = {
            "利好": 1.5,
            "牛市": 2.0,
            "上涨": 1.2,
            "大涨": 1.8,
            "暴涨": 2.0,
            "买入": 1.3,
            "突破": 1.5,
            "创新高": 1.8,
            "看好": 1.4,
            "信心": 1.3,
            "增长": 1.2,
            "回升": 1.3,
            "反弹": 1.4,
            "走强": 1.3,
            "向好": 1.3,
        }
        
        self._negative_keywords = {
            "利空": 1.5,
            "熊市": 2.0,
            "下跌": 1.2,
            "大跌": 1.8,
            "暴跌": 2.0,
            "卖出": 1.3,
            "跌破": 1.5,
            "创新低": 1.8,
            "看空": 1.4,
            "恐慌": 1.8,
            "下滑": 1.2,
            "萎缩": 1.3,
            "回落": 1.2,
            "走弱": 1.3,
            "堪忧": 1.4,
        }
        
        # Default weights for sentiment components
        self._default_weights = {
            "volume": 0.25,
            "price": 0.35,
            "volatility": 0.15,
            "capital": 0.15,
            "news": 0.10,
        }
        
        logger.info("Sentiment service initialized")

    def get_positive_keywords(self) -> Dict[str, float]:
        """Get positive keywords dictionary"""
        return self._positive_keywords.copy()

    def get_negative_keywords(self) -> Dict[str, float]:
        """Get negative keywords dictionary"""
        return self._negative_keywords.copy()

    def get_keyword_weights(self) -> Dict[str, float]:
        """Get all keyword weights"""
        return {**self._positive_keywords, **self._negative_keywords}

    def get_default_weights(self) -> Dict[str, Decimal]:
        """Get default component weights"""
        return {k: Decimal(str(v)) for k, v in self._default_weights.items()}

    def analyze_text_sentiment(self, text: str) -> Decimal:
        """Analyze sentiment of Chinese text using SnowNLP with domain keywords

        Args:
            text: Chinese text to analyze

        Returns:
            Sentiment score between 0 (negative) and 1 (positive)
        """
        try:
            # Base sentiment from SnowNLP
            s = SnowNLP(text)
            base_score = s.sentiments
            
            # Apply domain keyword adjustments
            keyword_adjustment = 0.0
            
            # Check for positive keywords
            for keyword, weight in self._positive_keywords.items():
                if keyword in text:
                    keyword_adjustment += weight * 0.05  # Each keyword adds 5% * weight
            
            # Check for negative keywords
            for keyword, weight in self._negative_keywords.items():
                if keyword in text:
                    keyword_adjustment -= weight * 0.05  # Each keyword subtracts 5% * weight
            
            # Combine base score with keyword adjustments
            adjusted_score = base_score + keyword_adjustment
            
            # Clamp to [0, 1] range
            final_score = max(0.0, min(1.0, adjusted_score))
            
            return Decimal(str(round(final_score, 4)))
            
        except Exception as e:
            logger.error(f"Error analyzing text sentiment: {e}")
            return Decimal("0.5")  # Return neutral on error

    def analyze_news_sentiment(self, articles: List[NewsArticle]) -> Decimal:
        """Analyze overall sentiment from news articles

        Args:
            articles: List of news articles

        Returns:
            Overall news sentiment score (0-100)
        """
        if not articles:
            return Decimal("50")  # Neutral
        
        try:
            total_sentiment = Decimal("0")
            total_weight = Decimal("0")
            
            for article in articles:
                # Combine title and summary for analysis
                text = article.title
                if article.summary:
                    text += " " + article.summary
                
                # Get sentiment score (0-1)
                score = self.analyze_text_sentiment(text)
                
                # Weight by importance
                weight = article.importance
                total_sentiment += score * 100 * weight
                total_weight += weight
            
            if total_weight > 0:
                return Decimal(str(round(total_sentiment / total_weight, 2)))
            else:
                return Decimal("50")
                
        except Exception as e:
            logger.error(f"Error analyzing news sentiment: {e}")
            return Decimal("50")

    def calculate_volume_sentiment(self, volume_ratio: float) -> Decimal:
        """Calculate sentiment from volume ratio

        Args:
            volume_ratio: Current volume / average volume

        Returns:
            Volume sentiment score (0-100)
        """
        # High volume = bullish, low volume = bearish
        # 1.0 = neutral (50)
        # > 1.5 = very bullish (80+)
        # < 0.5 = very bearish (20-)
        
        if volume_ratio >= 2.0:
            score = 90
        elif volume_ratio >= 1.5:
            score = 50 + (volume_ratio - 1.0) * 40 / 0.5  # 70-90
        elif volume_ratio >= 1.0:
            score = 50 + (volume_ratio - 1.0) * 20 / 0.5  # 50-70
        elif volume_ratio >= 0.5:
            score = 30 + (volume_ratio - 0.5) * 20 / 0.5  # 30-50
        else:
            score = 10 + volume_ratio * 20 / 0.5  # 10-30
        
        return Decimal(str(round(score, 2)))

    def calculate_price_sentiment(self, market_breadth: dict) -> Decimal:
        """Calculate sentiment from price movements and market breadth

        Args:
            market_breadth: Dict with advancing, declining, total_stocks, change_pct

        Returns:
            Price sentiment score (0-100)
        """
        advancing = market_breadth.get("advancing", 0)
        declining = market_breadth.get("declining", 0)
        total = market_breadth.get("total_stocks", 1)
        change_pct = market_breadth.get("change_pct", 0.0)
        
        # Market breadth component (60% weight)
        if total > 0:
            advance_pct = advancing / total * 100
            breadth_score = advance_pct  # 0-100
        else:
            breadth_score = 50
        
        # Index change component (40% weight)
        # +10% = 100, 0% = 50, -10% = 0
        index_score = 50 + change_pct * 5  # Each 1% = 5 points
        index_score = max(0, min(100, index_score))
        
        # Combine
        price_sentiment = breadth_score * 0.6 + index_score * 0.4
        
        return Decimal(str(round(price_sentiment, 2)))

    def calculate_volatility_sentiment(self, amplitude: float) -> Decimal:
        """Calculate sentiment from volatility (amplitude)

        Args:
            amplitude: Price amplitude percentage

        Returns:
            Volatility sentiment score (0-100), lower volatility = higher score
        """
        # Low volatility (< 1%) = stable, positive (70-80)
        # Moderate volatility (1-2%) = normal (50-70)
        # High volatility (> 3%) = risky, negative (20-40)
        
        if amplitude <= 0.5:
            score = 80
        elif amplitude <= 1.0:
            score = 80 - (amplitude - 0.5) * 20 / 0.5  # 60-80
        elif amplitude <= 2.0:
            score = 60 - (amplitude - 1.0) * 20 / 1.0  # 40-60
        elif amplitude <= 3.0:
            score = 40 - (amplitude - 2.0) * 10 / 1.0  # 30-40
        else:
            score = max(20, 30 - (amplitude - 3.0) * 5)  # 20-30
        
        return Decimal(str(round(score, 2)))

    def calculate_capital_sentiment(self, capital_flow: dict) -> Decimal:
        """Calculate sentiment from capital flows

        Args:
            capital_flow: Dict with north_net, main_net (in CNY)

        Returns:
            Capital sentiment score (0-100)
        """
        north_net = float(capital_flow.get("north_net", 0))
        main_net = float(capital_flow.get("main_net", 0))
        
        # Normalize to billions
        north_bn = north_net / 1_000_000_000
        main_bn = main_net / 1_000_000_000
        
        # North capital (60% weight): +50 bn = 100, 0 = 50, -50 bn = 0
        north_score = 50 + north_bn  # Each billion = 1 point
        north_score = max(0, min(100, north_score))
        
        # Main capital (40% weight): +20 bn = 100, 0 = 50, -20 bn = 0
        main_score = 50 + main_bn * 2.5  # Each billion = 2.5 points
        main_score = max(0, min(100, main_score))
        
        # Combine
        capital_sentiment = north_score * 0.6 + main_score * 0.4
        
        return Decimal(str(round(capital_sentiment, 2)))

    def classify_sentiment_level(self, sentiment_index: Decimal) -> SentimentLevel:
        """Classify sentiment index into sentiment level

        Args:
            sentiment_index: Sentiment index (0-100)

        Returns:
            SentimentLevel enum
        """
        index = float(sentiment_index)
        
        if index <= 20:
            return SentimentLevel.EXTREME_PANIC
        elif index <= 40:
            return SentimentLevel.PANIC
        elif index <= 60:
            return SentimentLevel.NEUTRAL
        elif index <= 80:
            return SentimentLevel.OPTIMISTIC
        else:
            return SentimentLevel.EXTREME_OPTIMISM

    def generate_interpretation(self, sentiment: MarketSentiment) -> str:
        """Generate Chinese interpretation of sentiment

        Args:
            sentiment: MarketSentiment object

        Returns:
            Chinese interpretation string
        """
        level = sentiment.sentiment_level
        index = float(sentiment.sentiment_index)
        
        # Level descriptions
        level_desc = {
            SentimentLevel.EXTREME_PANIC: "市场情绪极度恐慌",
            SentimentLevel.PANIC: "市场情绪较为恐慌",
            SentimentLevel.NEUTRAL: "市场情绪中性",
            SentimentLevel.OPTIMISTIC: "市场情绪偏乐观",
            SentimentLevel.EXTREME_OPTIMISM: "市场情绪极度乐观",
        }
        
        base = level_desc.get(level, "市场情绪正常")
        
        # Add component insights
        components = []
        if sentiment.volume_sentiment > 70:
            components.append("成交活跃")
        elif sentiment.volume_sentiment < 30:
            components.append("成交清淡")
        
        if sentiment.capital_sentiment > 65:
            components.append("资金流入积极")
        elif sentiment.capital_sentiment < 35:
            components.append("资金流出明显")
        
        # Recommendations
        if index > 80:
            suggestion = "市场可能过热，注意风险"
        elif index > 60:
            suggestion = "可适当参与，控制仓位"
        elif index > 40:
            suggestion = "谨慎观望，等待方向"
        elif index > 20:
            suggestion = "警惕下跌风险，轻仓或空仓"
        else:
            suggestion = "市场极度悲观，可能存在超跌机会"
        
        # Combine
        if components:
            return f"{base}，{','.join(components)}，{suggestion}"
        else:
            return f"{base}，{suggestion}"

    def assess_risk_level(self, sentiment_index: Decimal) -> str:
        """Assess risk level from sentiment index

        Args:
            sentiment_index: Sentiment index (0-100)

        Returns:
            Risk level string
        """
        index = float(sentiment_index)
        
        # Extreme values (both ends) = high risk
        if index >= 85 or index <= 15:
            return "极高风险"
        elif index >= 75 or index <= 25:
            return "高风险"
        elif index >= 60 or index <= 40:
            return "中等风险"
        else:
            return "低风险"

    def calculate_sentiment_trend(self, historical_sentiments: List[Decimal]) -> str:
        """Calculate sentiment trend from historical data

        Args:
            historical_sentiments: List of historical sentiment values

        Returns:
            Trend string: "improving", "deteriorating", or "stable"
        """
        if len(historical_sentiments) < 2:
            return "stable"
        
        # Calculate simple moving average trend
        recent = sum(historical_sentiments[-3:]) / len(historical_sentiments[-3:])
        older = sum(historical_sentiments[:-3] or historical_sentiments) / max(1, len(historical_sentiments[:-3] or historical_sentiments))
        
        diff = float(recent - older)
        
        if diff > 5:
            return "improving"
        elif diff < -5:
            return "deteriorating"
        else:
            return "stable"

    def calculate_market_sentiment(
        self,
        market_data: dict,
        news_articles: Optional[List[NewsArticle]] = None,
        weights: Optional[Dict[str, Decimal]] = None
    ) -> MarketSentiment:
        """Calculate comprehensive market sentiment

        Args:
            market_data: Dict with market metrics
            news_articles: Optional list of news articles
            weights: Optional custom weights for components

        Returns:
            MarketSentiment object
        """
        if weights is None:
            weights = self.get_default_weights()
        
        # Calculate component sentiments
        volume_sentiment = self.calculate_volume_sentiment(
            market_data.get("volume_ratio", 1.0)
        )
        
        price_sentiment = self.calculate_price_sentiment({
            "advancing": market_data.get("advancing", 0),
            "declining": market_data.get("declining", 0),
            "total_stocks": market_data.get("total_stocks", 1),
            "change_pct": market_data.get("change_pct", 0.0),
        })
        
        volatility_sentiment = self.calculate_volatility_sentiment(
            market_data.get("amplitude", 1.0)
        )
        
        capital_sentiment = self.calculate_capital_sentiment({
            "north_net": market_data.get("north_net", Decimal("0")),
            "main_net": market_data.get("main_net", Decimal("0")),
        })
        
        news_sentiment = None
        if news_articles:
            news_sentiment = self.analyze_news_sentiment(news_articles)
        
        # Calculate overall sentiment index
        sentiment_index = (
            volume_sentiment * weights["volume"] +
            price_sentiment * weights["price"] +
            volatility_sentiment * weights["volatility"] +
            capital_sentiment * weights["capital"]
        )
        
        if news_sentiment is not None:
            sentiment_index += news_sentiment * weights["news"]
        else:
            # Redistribute news weight to other components
            redistribution = weights["news"] / 4
            sentiment_index += (
                volume_sentiment * redistribution +
                price_sentiment * redistribution +
                volatility_sentiment * redistribution +
                capital_sentiment * redistribution
            )
        
        # Round to 2 decimal places
        sentiment_index = Decimal(str(round(float(sentiment_index), 2)))
        
        # Classify sentiment level
        sentiment_level = self.classify_sentiment_level(sentiment_index)
        
        # Create MarketSentiment object
        sentiment = MarketSentiment(
            sentiment_index=sentiment_index,
            sentiment_level=sentiment_level,
            volume_sentiment=volume_sentiment,
            price_sentiment=price_sentiment,
            volatility_sentiment=volatility_sentiment,
            capital_sentiment=capital_sentiment,
            news_sentiment=news_sentiment,
            weights=weights,
            interpretation="",  # Will be filled
            date=datetime.now().strftime("%Y-%m-%d"),
            calculated_at=datetime.now()
        )
        
        # Generate interpretation
        sentiment.interpretation = self.generate_interpretation(sentiment)
        sentiment.risk_level = self.assess_risk_level(sentiment_index)
        
        logger.info(f"Calculated market sentiment: {sentiment_index} ({sentiment_level})")
        
        return sentiment


# Singleton instance
_sentiment_service_instance: Optional[SentimentService] = None


def get_sentiment_service() -> SentimentService:
    """Get singleton SentimentService instance"""
    global _sentiment_service_instance
    if _sentiment_service_instance is None:
        _sentiment_service_instance = SentimentService()
    return _sentiment_service_instance
