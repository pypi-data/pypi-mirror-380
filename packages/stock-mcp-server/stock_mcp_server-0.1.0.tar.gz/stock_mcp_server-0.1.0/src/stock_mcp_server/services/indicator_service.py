"""Indicator Calculation Service - Technical analysis using pandas-ta"""

from datetime import datetime
from decimal import Decimal
from typing import List, Optional, Dict
import pandas as pd
import pandas_ta as ta

from loguru import logger

from stock_mcp_server.models.indicators import (
    TechnicalIndicator,
    IndicatorCategory,
    Signal,
)
from stock_mcp_server.models.market import HistoricalPrice
from stock_mcp_server.services.cache_service import get_cache


class IndicatorService:
    """Technical indicator calculation service using pandas-ta"""

    def __init__(self):
        """Initialize indicator service"""
        self.cache = get_cache()
        
        # Indicator descriptions
        self._descriptions = {
            "MA": "移动平均线 - 趋势指标",
            "EMA": "指数移动平均线 - 趋势指标",
            "MACD": "指数平滑异同移动平均线 - 动量指标",
            "RSI": "相对强弱指标 - 动量指标",
            "KDJ": "随机指标 - 动量指标",
            "BOLL": "布林带 - 波动率指标",
            "ATR": "平均真实波幅 - 波动率指标",
            "OBV": "能量潮 - 成交量指标",
            "VWAP": "成交量加权平均价 - 成交量指标",
        }
        
        logger.info("Indicator service initialized")

    def to_dataframe(self, price_data: List[HistoricalPrice]) -> pd.DataFrame:
        """Convert HistoricalPrice list to pandas DataFrame

        Args:
            price_data: List of HistoricalPrice objects

        Returns:
            pandas DataFrame with OHLCV data
        """
        data = []
        for price in price_data:
            data.append({
                'date': price.date,
                'open': float(price.open),
                'high': float(price.high),
                'low': float(price.low),
                'close': float(price.close),
                'volume': price.volume,
            })
        
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'])
        df = df.set_index('date')
        return df

    def apply_ta_indicator(
        self,
        df: pd.DataFrame,
        indicator: str,
        **kwargs
    ) -> pd.Series | pd.DataFrame:
        """Apply pandas-ta indicator to DataFrame

        Args:
            df: DataFrame with OHLCV data
            indicator: Indicator name (rsi, macd, etc.)
            **kwargs: Indicator parameters

        Returns:
            Series or DataFrame with indicator values
        """
        # Use pandas-ta to calculate indicator
        result = getattr(ta, indicator)(df['close'], **kwargs)
        return result

    def calculate_ma(
        self,
        price_data: List[HistoricalPrice],
        period: int = 5
    ) -> List[TechnicalIndicator]:
        """Calculate Moving Average

        Args:
            price_data: List of historical prices
            period: MA period

        Returns:
            List of TechnicalIndicator objects
        """
        if len(price_data) < period:
            return []
        
        try:
            df = self.to_dataframe(price_data)
            ma_series = ta.sma(df['close'], length=period)
            
            if ma_series is None or ma_series.isna().all():
                return []
            
            # Get latest MA value
            ma_value = ma_series.iloc[-1]
            current_price = float(price_data[-1].close)
            
            # Generate signal: price above MA = buy, below = sell
            if current_price > ma_value:
                signal = Signal.BUY
                signal_strength = min(100, ((current_price - ma_value) / ma_value) * 1000)
            elif current_price < ma_value:
                signal = Signal.SELL
                signal_strength = min(100, ((ma_value - current_price) / ma_value) * 1000)
            else:
                signal = Signal.NEUTRAL
                signal_strength = 0
            
            indicator = TechnicalIndicator(
                name="MA",
                category=IndicatorCategory.TREND,
                period=period,
                values={
                    f"ma{period}": Decimal(str(round(ma_value, 4))),
                    "current_price": Decimal(str(round(current_price, 4))),
                },
                signal=signal,
                interpretation=f"MA({period})={ma_value:.2f}, 当前价格={current_price:.2f}",
                date=datetime.now().strftime("%Y-%m-%d"),
                calculated_at=datetime.now()
            )
            
            return [indicator]
            
        except Exception as e:
            logger.error(f"Error calculating MA: {e}")
            return []

    def calculate_ema(
        self,
        price_data: List[HistoricalPrice],
        period: int = 12
    ) -> List[TechnicalIndicator]:
        """Calculate Exponential Moving Average

        Args:
            price_data: List of historical prices
            period: EMA period

        Returns:
            List of TechnicalIndicator objects
        """
        if len(price_data) < period:
            return []
        
        try:
            df = self.to_dataframe(price_data)
            ema_series = ta.ema(df['close'], length=period)
            
            if ema_series is None or ema_series.isna().all():
                return []
            
            ema_value = ema_series.iloc[-1]
            current_price = float(price_data[-1].close)
            
            # Generate signal
            if current_price > ema_value:
                signal = Signal.BUY
                signal_strength = min(100, ((current_price - ema_value) / ema_value) * 1000)
            elif current_price < ema_value:
                signal = Signal.SELL
                signal_strength = min(100, ((ema_value - current_price) / ema_value) * 1000)
            else:
                signal = Signal.NEUTRAL
                signal_strength = 0
            
            indicator = TechnicalIndicator(
                name="EMA",
                category=IndicatorCategory.TREND,
                period=period,
                values={
                    f"ema{period}": Decimal(str(round(ema_value, 4))),
                    "current_price": Decimal(str(round(current_price, 4))),
                },
                signal=signal,
                interpretation=f"EMA({period})={ema_value:.2f}, 当前价格={current_price:.2f}",
                date=datetime.now().strftime("%Y-%m-%d"),
                calculated_at=datetime.now()
            )
            
            return [indicator]
            
        except Exception as e:
            logger.error(f"Error calculating EMA: {e}")
            return []

    def calculate_macd(
        self,
        price_data: List[HistoricalPrice],
        fast: int = 12,
        slow: int = 26,
        signal_period: int = 9
    ) -> List[TechnicalIndicator]:
        """Calculate MACD indicator

        Args:
            price_data: List of historical prices
            fast: Fast EMA period
            slow: Slow EMA period
            signal_period: Signal line period

        Returns:
            List of TechnicalIndicator objects
        """
        if len(price_data) < slow + signal_period:
            return []
        
        try:
            df = self.to_dataframe(price_data)
            macd_result = ta.macd(df['close'], fast=fast, slow=slow, signal=signal_period)
            
            if macd_result is None or macd_result.empty:
                return []
            
            # Extract MACD, Signal, and Histogram
            macd_value = macd_result.iloc[-1, 0]  # MACD line
            signal_value = macd_result.iloc[-1, 1]  # Signal line
            histogram = macd_result.iloc[-1, 2]  # Histogram
            
            # Generate signal: MACD > Signal = buy
            if macd_value > signal_value:
                signal = Signal.BUY
                signal_strength = min(100, abs(histogram) * 100)
            elif macd_value < signal_value:
                signal = Signal.SELL
                signal_strength = min(100, abs(histogram) * 100)
            else:
                signal = Signal.NEUTRAL
                signal_strength = 0
            
            indicator = TechnicalIndicator(
                name="MACD",
                category=IndicatorCategory.MOMENTUM,
                period=None,
                values={
                    "macd": Decimal(str(round(macd_value, 4))),
                    "signal": Decimal(str(round(signal_value, 4))),
                    "histogram": Decimal(str(round(histogram, 4))),
                },
                signal=signal,
                interpretation=f"MACD={macd_value:.2f}, Signal={signal_value:.2f}, Histogram={histogram:.2f}",
                date=datetime.now().strftime("%Y-%m-%d"),
                calculated_at=datetime.now()
            )
            
            return [indicator]
            
        except Exception as e:
            logger.error(f"Error calculating MACD: {e}")
            return []

    def calculate_rsi(
        self,
        price_data: List[HistoricalPrice],
        period: int = 14
    ) -> List[TechnicalIndicator]:
        """Calculate RSI indicator

        Args:
            price_data: List of historical prices
            period: RSI period

        Returns:
            List of TechnicalIndicator objects
        """
        if len(price_data) < period + 1:
            return []
        
        try:
            df = self.to_dataframe(price_data)
            rsi_series = ta.rsi(df['close'], length=period)
            
            if rsi_series is None or rsi_series.isna().all():
                return []
            
            rsi_value = rsi_series.iloc[-1]
            
            # Generate signal: RSI > 70 = overbought (sell), RSI < 30 = oversold (buy)
            if rsi_value > 70:
                signal = Signal.SELL
                signal_strength = min(100, (rsi_value - 70) * 3.33)
            elif rsi_value < 30:
                signal = Signal.BUY
                signal_strength = min(100, (30 - rsi_value) * 3.33)
            else:
                signal = Signal.NEUTRAL
                signal_strength = 0
            
            indicator = TechnicalIndicator(
                name="RSI",
                category=IndicatorCategory.MOMENTUM,
                period=period,
                values={
                    f"rsi{period}": Decimal(str(round(rsi_value, 2))),
                },
                signal=signal,
                interpretation=f"RSI({period})={rsi_value:.2f}",
                date=datetime.now().strftime("%Y-%m-%d"),
                calculated_at=datetime.now()
            )
            
            return [indicator]
            
        except Exception as e:
            logger.error(f"Error calculating RSI: {e}")
            return []

    def calculate_kdj(
        self,
        price_data: List[HistoricalPrice],
        period: int = 9
    ) -> List[TechnicalIndicator]:
        """Calculate KDJ indicator

        Args:
            price_data: List of historical prices
            period: KDJ period

        Returns:
            List of TechnicalIndicator objects
        """
        if len(price_data) < period:
            return []
        
        try:
            df = self.to_dataframe(price_data)
            stoch = ta.stoch(df['high'], df['low'], df['close'], k=period, d=3, smooth_k=3)
            
            if stoch is None or stoch.empty:
                return []
            
            k_value = stoch.iloc[-1, 0]  # K line
            d_value = stoch.iloc[-1, 1]  # D line
            j_value = 3 * k_value - 2 * d_value  # J = 3K - 2D
            
            # Generate signal: K > 80 = overbought, K < 20 = oversold
            if k_value > 80:
                signal = Signal.SELL
                signal_strength = min(100, (k_value - 80) * 5)
            elif k_value < 20:
                signal = Signal.BUY
                signal_strength = min(100, (20 - k_value) * 5)
            else:
                signal = Signal.NEUTRAL
                signal_strength = 0
            
            indicator = TechnicalIndicator(
                name="KDJ",
                category=IndicatorCategory.MOMENTUM,
                period=period,
                values={
                    "k": Decimal(str(round(k_value, 2))),
                    "d": Decimal(str(round(d_value, 2))),
                    "j": Decimal(str(round(j_value, 2))),
                },
                signal=signal,
                interpretation=f"K={k_value:.2f}, D={d_value:.2f}, J={j_value:.2f}",
                date=datetime.now().strftime("%Y-%m-%d"),
                calculated_at=datetime.now()
            )
            
            return [indicator]
            
        except Exception as e:
            logger.error(f"Error calculating KDJ: {e}")
            return []

    def calculate_boll(
        self,
        price_data: List[HistoricalPrice],
        period: int = 20,
        std_dev: float = 2.0
    ) -> List[TechnicalIndicator]:
        """Calculate Bollinger Bands

        Args:
            price_data: List of historical prices
            period: Period for moving average
            std_dev: Standard deviation multiplier

        Returns:
            List of TechnicalIndicator objects
        """
        if len(price_data) < period:
            return []
        
        try:
            df = self.to_dataframe(price_data)
            bbands = ta.bbands(df['close'], length=period, std=std_dev)
            
            if bbands is None or bbands.empty:
                return []
            
            lower = bbands.iloc[-1, 0]  # Lower band
            middle = bbands.iloc[-1, 1]  # Middle band
            upper = bbands.iloc[-1, 2]  # Upper band
            
            current_price = float(price_data[-1].close)
            
            # Generate signal: price near upper = sell, near lower = buy
            band_width = upper - lower
            if current_price > upper:
                signal = Signal.SELL
                signal_strength = min(100, ((current_price - upper) / band_width) * 100)
            elif current_price < lower:
                signal = Signal.BUY
                signal_strength = min(100, ((lower - current_price) / band_width) * 100)
            else:
                signal = Signal.NEUTRAL
                signal_strength = 0
            
            indicator = TechnicalIndicator(
                name="BOLL",
                category=IndicatorCategory.VOLATILITY,
                period=period,
                values={
                    "upper": Decimal(str(round(upper, 4))),
                    "middle": Decimal(str(round(middle, 4))),
                    "lower": Decimal(str(round(lower, 4))),
                    "current_price": Decimal(str(round(current_price, 4))),
                },
                signal=signal,
                interpretation=f"Upper={upper:.2f}, Middle={middle:.2f}, Lower={lower:.2f}, Price={current_price:.2f}",
                date=datetime.now().strftime("%Y-%m-%d"),
                calculated_at=datetime.now()
            )
            
            return [indicator]
            
        except Exception as e:
            logger.error(f"Error calculating BOLL: {e}")
            return []

    def calculate_atr(
        self,
        price_data: List[HistoricalPrice],
        period: int = 14
    ) -> List[TechnicalIndicator]:
        """Calculate Average True Range

        Args:
            price_data: List of historical prices
            period: ATR period

        Returns:
            List of TechnicalIndicator objects
        """
        if len(price_data) < period + 1:
            return []
        
        try:
            df = self.to_dataframe(price_data)
            atr_series = ta.atr(df['high'], df['low'], df['close'], length=period)
            
            if atr_series is None or atr_series.isna().all():
                return []
            
            atr_value = atr_series.iloc[-1]
            
            indicator = TechnicalIndicator(
                name="ATR",
                category=IndicatorCategory.VOLATILITY,
                period=period,
                values={
                    f"atr{period}": Decimal(str(round(atr_value, 4))),
                },
                signal=Signal.NEUTRAL,  # ATR doesn't generate buy/sell signals
                interpretation=f"ATR({period})={atr_value:.4f}",
                date=datetime.now().strftime("%Y-%m-%d"),
                calculated_at=datetime.now()
            )
            
            return [indicator]
            
        except Exception as e:
            logger.error(f"Error calculating ATR: {e}")
            return []

    def calculate_volume_indicators(
        self,
        price_data: List[HistoricalPrice]
    ) -> List[TechnicalIndicator]:
        """Calculate volume-based indicators

        Args:
            price_data: List of historical prices

        Returns:
            List of TechnicalIndicator objects
        """
        if len(price_data) < 10:
            return []
        
        indicators = []
        
        try:
            df = self.to_dataframe(price_data)
            
            # OBV (On Balance Volume)
            obv_series = ta.obv(df['close'], df['volume'])
            if obv_series is not None and not obv_series.isna().all():
                obv_value = obv_series.iloc[-1]
                indicators.append(TechnicalIndicator(
                    name="OBV",
                    category=IndicatorCategory.VOLUME,
                    period=None,
                    values={
                        "obv": Decimal(str(round(obv_value, 2))),
                    },
                    signal=Signal.NEUTRAL,
                    interpretation=f"OBV={obv_value:.2f}",
                    date=datetime.now().strftime("%Y-%m-%d"),
                    calculated_at=datetime.now()
                ))
            
        except Exception as e:
            logger.error(f"Error calculating volume indicators: {e}")
        
        return indicators

    def calculate_all_indicators(
        self,
        price_data: List[HistoricalPrice],
        indicators: Optional[List[str]] = None
    ) -> List[TechnicalIndicator]:
        """Calculate multiple indicators at once

        Args:
            price_data: List of historical prices
            indicators: List of indicator names (default: all)

        Returns:
            List of TechnicalIndicator objects
        """
        if indicators is None:
            indicators = ["MA", "EMA", "RSI", "MACD", "KDJ", "BOLL", "ATR"]
        
        all_indicators = []
        
        for indicator_name in indicators:
            if indicator_name == "MA":
                all_indicators.extend(self.calculate_ma(price_data))
            elif indicator_name == "EMA":
                all_indicators.extend(self.calculate_ema(price_data))
            elif indicator_name == "RSI":
                all_indicators.extend(self.calculate_rsi(price_data))
            elif indicator_name == "MACD":
                all_indicators.extend(self.calculate_macd(price_data))
            elif indicator_name == "KDJ":
                all_indicators.extend(self.calculate_kdj(price_data))
            elif indicator_name == "BOLL":
                all_indicators.extend(self.calculate_boll(price_data))
            elif indicator_name == "ATR":
                all_indicators.extend(self.calculate_atr(price_data))
        
        return all_indicators

    def calculate_indicators_by_category(
        self,
        price_data: List[HistoricalPrice],
        category: IndicatorCategory
    ) -> List[TechnicalIndicator]:
        """Calculate indicators by category

        Args:
            price_data: List of historical prices
            category: Indicator category

        Returns:
            List of TechnicalIndicator objects
        """
        if category == IndicatorCategory.TREND:
            indicators = []
            indicators.extend(self.calculate_ma(price_data))
            indicators.extend(self.calculate_ema(price_data))
            return indicators
        elif category == IndicatorCategory.MOMENTUM:
            indicators = []
            indicators.extend(self.calculate_rsi(price_data))
            indicators.extend(self.calculate_macd(price_data))
            indicators.extend(self.calculate_kdj(price_data))
            return indicators
        elif category == IndicatorCategory.VOLATILITY:
            indicators = []
            indicators.extend(self.calculate_boll(price_data))
            indicators.extend(self.calculate_atr(price_data))
            return indicators
        elif category == IndicatorCategory.VOLUME:
            return self.calculate_volume_indicators(price_data)
        else:
            return []

    def generate_ma_crossover_signal(
        self,
        price_data: List[HistoricalPrice],
        fast_period: int = 5,
        slow_period: int = 20
    ) -> Signal:
        """Generate signal from MA crossover

        Args:
            price_data: List of historical prices
            fast_period: Fast MA period
            slow_period: Slow MA period

        Returns:
            Signal enum
        """
        if len(price_data) < slow_period:
            return Signal.NEUTRAL
        
        try:
            df = self.to_dataframe(price_data)
            fast_ma = ta.sma(df['close'], length=fast_period)
            slow_ma = ta.sma(df['close'], length=slow_period)
            
            if fast_ma is None or slow_ma is None:
                return Signal.NEUTRAL
            
            # Check crossover
            fast_current = fast_ma.iloc[-1]
            slow_current = slow_ma.iloc[-1]
            fast_prev = fast_ma.iloc[-2]
            slow_prev = slow_ma.iloc[-2]
            
            # Golden cross: fast crosses above slow
            if fast_prev <= slow_prev and fast_current > slow_current:
                return Signal.BUY
            # Death cross: fast crosses below slow
            elif fast_prev >= slow_prev and fast_current < slow_current:
                return Signal.SELL
            else:
                return Signal.NEUTRAL
                
        except Exception as e:
            logger.error(f"Error generating MA crossover signal: {e}")
            return Signal.NEUTRAL

    def detect_golden_cross(self, price_data: List[HistoricalPrice]) -> bool:
        """Detect golden cross (MA5 crosses above MA20)

        Args:
            price_data: List of historical prices

        Returns:
            True if golden cross detected
        """
        signal = self.generate_ma_crossover_signal(price_data, 5, 20)
        return signal == Signal.BUY

    def detect_death_cross(self, price_data: List[HistoricalPrice]) -> bool:
        """Detect death cross (MA5 crosses below MA20)

        Args:
            price_data: List of historical prices

        Returns:
            True if death cross detected
        """
        signal = self.generate_ma_crossover_signal(price_data, 5, 20)
        return signal == Signal.SELL

    def detect_rsi_divergence(self, price_data: List[HistoricalPrice]) -> bool:
        """Detect RSI divergence (simplified)

        Args:
            price_data: List of historical prices

        Returns:
            True if divergence detected
        """
        # Simplified: just check if RSI and price trend differ
        if len(price_data) < 20:
            return False
        
        try:
            df = self.to_dataframe(price_data)
            rsi = ta.rsi(df['close'], length=14)
            
            if rsi is None:
                return False
            
            # Compare recent trends
            price_trend = df['close'].iloc[-1] > df['close'].iloc[-10]
            rsi_trend = rsi.iloc[-1] > rsi.iloc[-10]
            
            # Divergence if trends differ
            return price_trend != rsi_trend
            
        except Exception as e:
            logger.error(f"Error detecting RSI divergence: {e}")
            return False

    def detect_bollinger_squeeze(self, price_data: List[HistoricalPrice]) -> bool:
        """Detect Bollinger Band squeeze (low volatility)

        Args:
            price_data: List of historical prices

        Returns:
            True if squeeze detected
        """
        if len(price_data) < 20:
            return False
        
        try:
            indicators = self.calculate_boll(price_data)
            if not indicators:
                return False
            
            values = indicators[0].values
            upper = float(values["upper"])
            lower = float(values["lower"])
            middle = float(values["middle"])
            
            # Squeeze: band width is small relative to middle
            band_width = upper - lower
            band_width_pct = (band_width / middle) * 100
            
            # Squeeze if band width < 5% of middle
            return band_width_pct < 5.0
            
        except Exception as e:
            logger.error(f"Error detecting Bollinger squeeze: {e}")
            return False

    def calculate_indicators_cached(
        self,
        symbol: str,
        price_data: List[HistoricalPrice],
        indicators: List[str]
    ) -> List[TechnicalIndicator]:
        """Calculate indicators with caching

        Args:
            symbol: Stock symbol
            price_data: List of historical prices
            indicators: List of indicator names

        Returns:
            List of TechnicalIndicator objects
        """
        # Check cache
        cached = self.cache.get(
            "indicators",
            symbol=symbol,
            indicators='_'.join(sorted(indicators))
        )
        if cached:
            return cached
        
        # Calculate indicators
        result = self.calculate_all_indicators(price_data, indicators)
        
        # Cache for 5 minutes
        self.cache.set(
            "indicators",
            result,
            ttl=300,
            symbol=symbol,
            indicators='_'.join(sorted(indicators))
        )
        
        return result

    def get_indicator_descriptions(self) -> Dict[str, str]:
        """Get indicator descriptions

        Returns:
            Dictionary of indicator descriptions
        """
        return self._descriptions.copy()

    def get_supported_indicators(self) -> List[str]:
        """Get list of supported indicators

        Returns:
            List of indicator names
        """
        return list(self._descriptions.keys())


# Singleton instance
_indicator_service_instance: Optional[IndicatorService] = None


def get_indicator_service() -> IndicatorService:
    """Get singleton IndicatorService instance"""
    global _indicator_service_instance
    if _indicator_service_instance is None:
        _indicator_service_instance = IndicatorService()
    return _indicator_service_instance
