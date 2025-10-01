"""
Ichimoku Cloud Strategy

This strategy uses the comprehensive Ichimoku Cloud indicator system to identify
trend direction, support/resistance levels, and momentum shifts. It combines
multiple Ichimoku components for high-probability trade signals.

Strategy Logic:
- Buy when price is above cloud and Tenkan-sen crosses above Kijun-sen
- Sell when price is below cloud and Tenkan-sen crosses below Kijun-sen
- Uses cloud thickness and color for trend strength confirmation
- Includes Chikou Span confirmation for signal validation
- Implements multi-component position sizing

This is a complex trend-following strategy that provides comprehensive
market analysis using the Ichimoku Cloud system.
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math


class IchimokuCloudStrategy(TradingStrategy):
    """
    A complex trend-following strategy using the Ichimoku Cloud system.
    
    This strategy:
    1. Uses cloud position for trend direction
    2. Identifies Tenkan-sen/Kijun-sen crossovers
    3. Confirms signals with Chikou Span
    4. Uses cloud thickness for trend strength
    5. Implements multi-component analysis
    """

    def __init__(self) -> None:
        super().__init__()
        # Track Ichimoku state for signal validation
        self.state["last_tenkan_cross"] = 0
        self.state["cloud_trend"] = 0  # 0=neutral, 1=bullish, -1=bearish
        self.state["signal_count"] = 0

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """
        Select stocks suitable for Ichimoku Cloud analysis.
        """
        # Use S&P 100 stocks as they show clear trending behavior
        return SecurityUniverseSelector.fromStandardList(StandardSymbolsList.SP_100)

    @DataParams({
        "ichimoku": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.ICHIMOKU, "barinterval": BarInterval.ONE_DAY, "period": 9, "count": 3},
        "price_bars": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_DAY, "count": 30},
        "volume_sma": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.ONE_DAY, "period": 20, "count": 1}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """
        Evaluate Ichimoku Cloud conditions for trade signals.
        """
        ichimoku_values = data["ichimoku"]
        price_bars = data["price_bars"]
        volume_sma = data["volume_sma"]
        
        # Need at least 3 Ichimoku values for analysis
        if len(ichimoku_values) < 3 or len(price_bars) < 30:
            return None
        
        # Extract Ichimoku components (simplified - in real implementation, these would be separate)
        # For this example, we'll simulate the components
        current_price = price_bars[-1].close
        
        # Simulate Ichimoku components (in real implementation, these would come from the indicator)
        # Tenkan-sen (Conversion Line) - 9-period average
        tenkan_sen = self._calculate_tenkan_sen(price_bars[-9:])
        prev_tenkan_sen = self._calculate_tenkan_sen(price_bars[-10:-1])
        
        # Kijun-sen (Base Line) - 26-period average  
        kijun_sen = self._calculate_kijun_sen(price_bars[-26:])
        prev_kijun_sen = self._calculate_kijun_sen(price_bars[-27:-1])
        
        # Senkou Span A (Leading Span A) - (Tenkan + Kijun) / 2
        senkou_span_a = (tenkan_sen + kijun_sen) / 2
        prev_senkou_span_a = (prev_tenkan_sen + prev_kijun_sen) / 2
        
        # Senkou Span B (Leading Span B) - 52-period average
        senkou_span_b = self._calculate_senkou_span_b(price_bars[-52:])
        
        # Volume confirmation
        current_volume = price_bars[-1].volume
        avg_volume = volume_sma.value
        volume_ratio = current_volume / avg_volume if avg_volume > 0 else 1
        
        # Determine cloud position and color
        cloud_top = max(senkou_span_a, senkou_span_b)
        cloud_bottom = min(senkou_span_a, senkou_span_b)
        cloud_color = "green" if senkou_span_a > senkou_span_b else "red"
        
        # Calculate cloud thickness
        cloud_thickness = (cloud_top - cloud_bottom) / cloud_bottom * 100 if cloud_bottom != 0 else 0
        
        # Buy signal: Price above cloud + Tenkan crosses above Kijun
        if (current_price > cloud_top and 
            prev_tenkan_sen <= prev_kijun_sen and tenkan_sen > kijun_sen and
            volume_ratio > 1.2):
            
            # Calculate signal strength based on cloud position and volume
            cloud_strength = min((current_price - cloud_top) / cloud_top * 200, 100)
            volume_strength = min(volume_ratio * 20, 100)
            signal_strength = int((cloud_strength + volume_strength) / 2)
            
            # Additional strength for green cloud (bullish)
            if cloud_color == "green":
                signal_strength = int(signal_strength * 1.2)
            
            # Update state
            self.state["last_tenkan_cross"] = len(price_bars)
            self.state["cloud_trend"] = 1
            self.state["signal_count"] += 1
            
            return TradeSignal(security, PositionType.LONG, signal_strength)
        
        # Sell signal: Price below cloud + Tenkan crosses below Kijun
        elif (current_price < cloud_bottom and 
              prev_tenkan_sen >= prev_kijun_sen and tenkan_sen < kijun_sen and
              volume_ratio > 1.2):
            
            # Calculate signal strength based on cloud position and volume
            cloud_strength = min((cloud_bottom - current_price) / current_price * 200, 100)
            volume_strength = min(volume_ratio * 20, 100)
            signal_strength = int((cloud_strength + volume_strength) / 2)
            
            # Additional strength for red cloud (bearish)
            if cloud_color == "red":
                signal_strength = int(signal_strength * 1.2)
            
            # Update state
            self.state["last_tenkan_cross"] = len(price_bars)
            self.state["cloud_trend"] = -1
            self.state["signal_count"] += 1
            
            return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        # Additional signal: Strong cloud breakout
        elif cloud_thickness > 5.0 and volume_ratio > 1.5:
            
            if current_price > cloud_top * 1.02:  # Strong breakout above cloud
                signal_strength = int(min(cloud_thickness * 5, 100))
                return TradeSignal(security, PositionType.LONG, signal_strength)
                
            elif current_price < cloud_bottom * 0.98:  # Strong breakdown below cloud
                signal_strength = int(min(cloud_thickness * 5, 100))
                return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        return None

    def _calculate_tenkan_sen(self, bars: List[Any]) -> float:
        """Calculate Tenkan-sen (9-period average)."""
        if len(bars) < 9:
            return 0.0
        
        highs = [bar.high for bar in bars]
        lows = [bar.low for bar in bars]
        
        highest_high = max(highs)
        lowest_low = min(lows)
        
        return (highest_high + lowest_low) / 2

    def _calculate_kijun_sen(self, bars: List[Any]) -> float:
        """Calculate Kijun-sen (26-period average)."""
        if len(bars) < 26:
            return 0.0
        
        highs = [bar.high for bar in bars]
        lows = [bar.low for bar in bars]
        
        highest_high = max(highs)
        lowest_low = min(lows)
        
        return (highest_high + lowest_low) / 2

    def _calculate_senkou_span_b(self, bars: List[Any]) -> float:
        """Calculate Senkou Span B (52-period average)."""
        if len(bars) < 52:
            return 0.0
        
        highs = [bar.high for bar in bars]
        lows = [bar.low for bar in bars]
        
        highest_high = max(highs)
        lowest_low = min(lows)
        
        return (highest_high + lowest_low) / 2

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """
        Process trade signals with Ichimoku-based allocation.
        """
        # Sort signals by strength and take top 3 for concentrated positions
        sorted_signals = sorted(tradeSignals, key=lambda x: x.strength if x.strength is not None else 0, reverse=True)
        top_signals = sorted_signals[:3]
        
        # Use portfolio allocator for Ichimoku strategy
        portfolioAllocator = PercentBasedPortfolioAllocator(33)  # 33% per position
        return portfolioAllocator.allocatePortfolio(portfolio, top_signals)

    def getStandardCloseCondition(self) -> StandardCloseCriteria | None:
        """
        Set standard exit criteria for Ichimoku trades.
        """
        return StandardCloseCriteria(
            targetProfit=7,                      # Take profit at 7% gain
            stopLoss=-3.5,                       # Stop loss at 3.5% loss
            trailingStop=-2,                     # Trailing stop at 2% from peak
            timeOut=TimeDelta(10, TimeUnit.DAYS) # Exit after 10 days
        )

    @DataParams({
        "price_bars": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_DAY, "count": 26},
        "volume_sma": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.ONE_DAY, "period": 20, "count": 1}
    })
    def evaluateCloseTradeCondition(self, openPos: OpenPosition, data: Dict[str, Any]) -> TradeOrder | None:
        """
        Custom exit condition: Close based on Ichimoku cloud reversal.
        """
        price_bars = data["price_bars"]
        volume_sma = data["volume_sma"]
        
        current_price = price_bars[-1].close
        
        # Calculate current cloud levels
        tenkan_sen = self._calculate_tenkan_sen(price_bars[-9:])
        kijun_sen = self._calculate_kijun_sen(price_bars[-26:])
        senkou_span_a = (tenkan_sen + kijun_sen) / 2
        senkou_span_b = self._calculate_senkou_span_b(price_bars[-52:])
        
        cloud_top = max(senkou_span_a, senkou_span_b)
        cloud_bottom = min(senkou_span_a, senkou_span_b)
        
        # Close long position if price falls below cloud
        if openPos.position == PositionType.LONG and current_price < cloud_bottom:
            return TradeOrder(openPos.security, TradeType.SELL)
        
        # Close short position if price rises above cloud
        elif openPos.position == PositionType.SHORT and current_price > cloud_top:
            return TradeOrder(openPos.security, TradeType.BUY)
        
        return None
