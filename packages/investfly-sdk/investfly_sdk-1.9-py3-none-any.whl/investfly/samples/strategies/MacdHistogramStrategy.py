"""
MACD Histogram Strategy

This strategy uses MACD histogram momentum and zero-line crossovers to identify
trend changes and momentum shifts. It focuses on the histogram component which
provides early signals of trend reversals.

Strategy Logic:
- Buy when MACD histogram turns positive (bullish momentum)
- Sell when MACD histogram turns negative (bearish momentum)
- Uses histogram slope for signal strength calculation
- Includes volume confirmation for signal validation
- Implements trend-following position management

This is a trend-following strategy that capitalizes on momentum shifts
when MACD histogram crosses the zero line.
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math


class MacdHistogramStrategy(TradingStrategy):
    """
    A trend-following strategy using MACD histogram momentum.
    
    This strategy:
    1. Identifies bullish momentum when MACD histogram turns positive
    2. Identifies bearish momentum when MACD histogram turns negative
    3. Uses histogram slope for signal strength calculation
    4. Includes volume confirmation for signal validation
    5. Implements trend-following position management
    """

    def __init__(self) -> None:
        super().__init__()
        # Track MACD state to avoid false signals
        self.state["last_macd_signal"] = 0
        self.state["macd_trend"] = 0  # 0=neutral, 1=bullish, -1=bearish

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """
        Select liquid stocks suitable for trend following.
        """
        # Use S&P 500 stocks as they show clear trending behavior
        return SecurityUniverseSelector.fromStandardList(StandardSymbolsList.SP_500)

    @DataParams({
        "macd": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.MACD, "barinterval": BarInterval.ONE_MINUTE, "period": 12, "count": 3},
        "macd_signal": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.MACDS, "barinterval": BarInterval.ONE_MINUTE, "period": 12, "count": 3},
        "current_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_MINUTE, "count": 3},
        "volume_sma": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.ONE_MINUTE, "period": 20, "count": 1}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """
        Evaluate MACD histogram momentum for trade signals.
        """
        macd_values = data["macd"]
        macd_signal_values = data["macd_signal"]
        current_bars = data["current_bar"]
        volume_sma = data["volume_sma"]
        
        # Need at least 3 data points to calculate momentum
        if len(macd_values) < 3 or len(macd_signal_values) < 3:
            return None
        
        # Calculate MACD histogram values
        current_histogram = macd_values[-1].value - macd_signal_values[-1].value
        prev_histogram = macd_values[-2].value - macd_signal_values[-2].value
        prev_prev_histogram = macd_values[-3].value - macd_signal_values[-3].value
        
        # Calculate histogram slope (momentum)
        histogram_slope = current_histogram - prev_histogram
        prev_histogram_slope = prev_histogram - prev_prev_histogram
        
        # Volume confirmation
        current_volume = current_bars[-1].volume
        avg_volume = volume_sma.value
        volume_ratio = current_volume / avg_volume if avg_volume > 0 else 1
        
        # Buy signal: MACD histogram turns positive with positive slope
        if (prev_histogram <= 0 and current_histogram > 0 and 
            histogram_slope > 0 and volume_ratio > 1.1):
            
            # Calculate signal strength based on histogram momentum and volume
            momentum_strength = min(abs(histogram_slope) * 100, 100)
            signal_strength = int(momentum_strength * volume_ratio)
            
            # Update state
            self.state["last_macd_signal"] = len(current_bars)
            self.state["macd_trend"] = 1  # bullish
            
            return TradeSignal(security, PositionType.LONG, signal_strength)
        
        # Sell signal: MACD histogram turns negative with negative slope
        elif (prev_histogram >= 0 and current_histogram < 0 and 
              histogram_slope < 0 and volume_ratio > 1.1):
            
            # Calculate signal strength based on histogram momentum and volume
            momentum_strength = min(abs(histogram_slope) * 100, 100)
            signal_strength = int(momentum_strength * volume_ratio)
            
            # Update state
            self.state["last_macd_signal"] = len(current_bars)
            self.state["macd_trend"] = -1  # bearish
            
            return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        # Additional signal: Strong histogram momentum continuation
        elif abs(histogram_slope) > abs(prev_histogram_slope) * 1.5 and volume_ratio > 1.2:
            
            if current_histogram > 0 and histogram_slope > 0:  # Strong bullish momentum
                momentum_strength = min(abs(histogram_slope) * 80, 100)
                signal_strength = int(momentum_strength * volume_ratio)
                return TradeSignal(security, PositionType.LONG, signal_strength)
                
            elif current_histogram < 0 and histogram_slope < 0:  # Strong bearish momentum
                momentum_strength = min(abs(histogram_slope) * 80, 100)
                signal_strength = int(momentum_strength * volume_ratio)
                return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        return None

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """
        Process trade signals with trend-following allocation.
        """
        # Sort signals by strength and take top 4 for diversified trend exposure
        sorted_signals = sorted(tradeSignals, key=lambda x: x.strength if x.strength is not None else 0, reverse=True)
        top_signals = sorted_signals[:4]
        
        # Use portfolio allocator for trend-following strategy
        portfolioAllocator = PercentBasedPortfolioAllocator(25)  # 25% per position
        return portfolioAllocator.allocatePortfolio(portfolio, top_signals)

    def getStandardCloseCondition(self) -> StandardCloseCriteria | None:
        """
        Set standard exit criteria for trend-following trades.
        """
        return StandardCloseCriteria(
            targetProfit=6,                      # Take profit at 6% gain
            stopLoss=-3,                         # Stop loss at 3% loss
            trailingStop=-1.5,                   # Trailing stop at 1.5% from peak
            timeOut=TimeDelta(7, TimeUnit.DAYS)  # Exit after 7 days
        )

    @DataParams({
        "macd": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.MACD, "barinterval": BarInterval.ONE_MINUTE, "period": 12, "count": 2},
        "macd_signal": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.MACDS, "barinterval": BarInterval.ONE_MINUTE, "period": 12, "count": 2}
    })
    def evaluateCloseTradeCondition(self, openPos: OpenPosition, data: Dict[str, Any]) -> TradeOrder | None:
        """
        Custom exit condition: Close based on MACD histogram reversal.
        """
        macd_values = data["macd"]
        macd_signal_values = data["macd_signal"]
        
        # Calculate current and previous histogram values
        current_histogram = macd_values[-1].value - macd_signal_values[-1].value
        prev_histogram = macd_values[-2].value - macd_signal_values[-2].value
        
        # Close long position if histogram turns negative
        if openPos.position == PositionType.LONG and current_histogram < 0 and prev_histogram > 0:
            return TradeOrder(openPos.security, TradeType.SELL)
        
        # Close short position if histogram turns positive
        elif openPos.position == PositionType.SHORT and current_histogram > 0 and prev_histogram < 0:
            return TradeOrder(openPos.security, TradeType.BUY)
        
        return None
