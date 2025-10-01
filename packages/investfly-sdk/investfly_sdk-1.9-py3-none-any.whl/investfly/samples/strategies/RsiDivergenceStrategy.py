"""
RSI Divergence Strategy

This strategy identifies potential trend reversals by detecting divergences between
price action and the RSI indicator. Divergence occurs when price makes new highs/lows
but RSI fails to confirm, indicating weakening momentum.

Strategy Logic:
- Bullish divergence: Price makes lower low, RSI makes higher low (buy signal)
- Bearish divergence: Price makes higher high, RSI makes lower high (sell signal)
- Uses 14-period RSI with divergence confirmation
- Includes volume and price action validation
- Implements momentum-based position sizing

This is a momentum strategy that capitalizes on trend reversals
when momentum indicators diverge from price action.
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math


class RsiDivergenceStrategy(TradingStrategy):
    """
    A momentum strategy using RSI divergence to identify trend reversals.
    
    This strategy:
    1. Detects bullish divergence (potential buy signal)
    2. Detects bearish divergence (potential sell signal)
    3. Uses volume confirmation for signal validation
    4. Implements momentum-based position sizing
    5. Includes risk management with trailing stops
    """

    def __init__(self) -> None:
        super().__init__()
        # Track divergence patterns to avoid false signals
        self.state["last_bullish_divergence"] = 0
        self.state["last_bearish_divergence"] = 0
        self.state["divergence_count"] = 0

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """
        Select liquid stocks that are suitable for momentum trading.
        """
        # Use NASDAQ 100 stocks as they tend to show clear momentum patterns
        return SecurityUniverseSelector.fromStandardList(StandardSymbolsList.NASDAQ_100)

    @DataParams({
        "rsi": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.ONE_MINUTE, "period": 14, "count": 20},
        "price_bars": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_MINUTE, "count": 20},
        "volume_sma": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.ONE_MINUTE, "period": 20, "count": 1}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """
        Evaluate RSI divergence conditions for trade signals.
        """
        rsi_values = data["rsi"]
        price_bars = data["price_bars"]
        volume_sma = data["volume_sma"]
        
        # Need at least 10 data points to detect divergence
        if len(rsi_values) < 10 or len(price_bars) < 10:
            return None
        
        # Extract recent price and RSI data
        recent_prices = [bar.close for bar in price_bars[-10:]]
        recent_rsi = [rsi.value for rsi in rsi_values[-10:]]
        
        # Find local extremes in price and RSI
        price_highs = self._find_local_extremes(recent_prices, "high")
        price_lows = self._find_local_extremes(recent_prices, "low")
        rsi_highs = self._find_local_extremes(recent_rsi, "high")
        rsi_lows = self._find_local_extremes(recent_rsi, "low")
        
        # Check for bullish divergence (price lower low, RSI higher low)
        bullish_divergence = self._check_bullish_divergence(price_lows, rsi_lows, recent_prices, recent_rsi)
        
        # Check for bearish divergence (price higher high, RSI lower high)
        bearish_divergence = self._check_bearish_divergence(price_highs, rsi_highs, recent_prices, recent_rsi)
        
        # Volume confirmation
        current_volume = price_bars[-1].volume
        avg_volume = volume_sma.value
        volume_ratio = current_volume / avg_volume if avg_volume > 0 else 1
        
        # Generate signals based on divergence detection
        if bullish_divergence and volume_ratio > 1.2:  # Volume confirmation
            # Calculate signal strength based on divergence quality and volume
            divergence_strength = self._calculate_divergence_strength(price_lows, rsi_lows, "bullish")
            signal_strength = int(divergence_strength * volume_ratio)
            
            # Update state
            self.state["last_bullish_divergence"] = len(price_bars)
            self.state["divergence_count"] += 1
            
            return TradeSignal(security, PositionType.LONG, signal_strength)
        
        elif bearish_divergence and volume_ratio > 1.2:  # Volume confirmation
            # Calculate signal strength based on divergence quality and volume
            divergence_strength = self._calculate_divergence_strength(price_highs, rsi_highs, "bearish")
            signal_strength = int(divergence_strength * volume_ratio)
            
            # Update state
            self.state["last_bearish_divergence"] = len(price_bars)
            self.state["divergence_count"] += 1
            
            return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        return None

    def _find_local_extremes(self, data: List[float], extreme_type: str) -> List[int]:
        """Find indices of local extremes in the data."""
        extremes = []
        for i in range(1, len(data) - 1):
            if extreme_type == "high":
                if data[i] > data[i-1] and data[i] > data[i+1]:
                    extremes.append(i)
            else:  # low
                if data[i] < data[i-1] and data[i] < data[i+1]:
                    extremes.append(i)
        return extremes

    def _check_bullish_divergence(self, price_lows: List[int], rsi_lows: List[int], 
                                 prices: List[float], rsi_values: List[float]) -> bool:
        """Check for bullish divergence pattern."""
        if len(price_lows) < 2 or len(rsi_lows) < 2:
            return False
        
        # Check if price made lower low but RSI made higher low
        latest_price_low_idx = price_lows[-1]
        prev_price_low_idx = price_lows[-2]
        latest_rsi_low_idx = rsi_lows[-1]
        prev_rsi_low_idx = rsi_lows[-2]
        
        # Price should be making lower low
        price_lower_low = prices[latest_price_low_idx] < prices[prev_price_low_idx]
        
        # RSI should be making higher low
        rsi_higher_low = rsi_values[latest_rsi_low_idx] > rsi_values[prev_rsi_low_idx]
        
        # Additional check: RSI should be oversold (< 40)
        rsi_oversold = rsi_values[latest_rsi_low_idx] < 40
        
        return price_lower_low and rsi_higher_low and rsi_oversold

    def _check_bearish_divergence(self, price_highs: List[int], rsi_highs: List[int], 
                                 prices: List[float], rsi_values: List[float]) -> bool:
        """Check for bearish divergence pattern."""
        if len(price_highs) < 2 or len(rsi_highs) < 2:
            return False
        
        # Check if price made higher high but RSI made lower high
        latest_price_high_idx = price_highs[-1]
        prev_price_high_idx = price_highs[-2]
        latest_rsi_high_idx = rsi_highs[-1]
        prev_rsi_high_idx = rsi_highs[-2]
        
        # Price should be making higher high
        price_higher_high = prices[latest_price_high_idx] > prices[prev_price_high_idx]
        
        # RSI should be making lower high
        rsi_lower_high = rsi_values[latest_rsi_high_idx] < rsi_values[prev_rsi_high_idx]
        
        # Additional check: RSI should be overbought (> 60)
        rsi_overbought = rsi_values[latest_rsi_high_idx] > 60
        
        return price_higher_high and rsi_lower_high and rsi_overbought

    def _calculate_divergence_strength(self, price_extremes: List[int], rsi_extremes: List[int], 
                                     divergence_type: str) -> float:
        """Calculate the strength of the divergence signal."""
        if len(price_extremes) < 2 or len(rsi_extremes) < 2:
            return 0.0
        
        # Calculate the magnitude of the divergence
        if divergence_type == "bullish":
            # For bullish divergence, measure how much RSI improved
            rsi_improvement = rsi_extremes[-1] - rsi_extremes[-2]
            return min(rsi_improvement * 10, 100)  # Scale and cap at 100
        else:
            # For bearish divergence, measure how much RSI deteriorated
            rsi_deterioration = rsi_extremes[-2] - rsi_extremes[-1]
            return min(rsi_deterioration * 10, 100)  # Scale and cap at 100

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """
        Process trade signals with momentum-based allocation.
        """
        # Sort signals by strength and take top 3 for concentrated positions
        sorted_signals = sorted(tradeSignals, key=lambda x: x.strength if x.strength is not None else 0, reverse=True)
        top_signals = sorted_signals[:3]
        
        # Use portfolio allocator with higher concentration for momentum trades
        portfolioAllocator = PercentBasedPortfolioAllocator(33)  # 33% per position
        return portfolioAllocator.allocatePortfolio(portfolio, top_signals)

    def getStandardCloseCondition(self) -> StandardCloseCriteria | None:
        """
        Set standard exit criteria for momentum trades.
        """
        return StandardCloseCriteria(
            targetProfit=8,                      # Take profit at 8% gain
            stopLoss=-4,                         # Stop loss at 4% loss
            trailingStop=-2,                     # Trailing stop at 2% from peak
            timeOut=TimeDelta(5, TimeUnit.DAYS)  # Exit after 5 days
        )

    @DataParams({
        "rsi": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.ONE_MINUTE, "period": 14, "count": 1},
        "current_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_MINUTE, "count": 1}
    })
    def evaluateCloseTradeCondition(self, openPos: OpenPosition, data: Dict[str, Any]) -> TradeOrder | None:
        """
        Custom exit condition: Close based on RSI momentum reversal.
        """
        rsi = data["rsi"]
        current_bar = data["current_bar"][-1]
        
        current_rsi = rsi.value
        current_price = current_bar.close
        
        # Close long position if RSI becomes overbought (> 70)
        if openPos.position == PositionType.LONG and current_rsi > 70:
            return TradeOrder(openPos.security, TradeType.SELL)
        
        # Close short position if RSI becomes oversold (< 30)
        elif openPos.position == PositionType.SHORT and current_rsi < 30:
            return TradeOrder(openPos.security, TradeType.BUY)
        
        return None
