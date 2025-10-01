"""
Multi-Timeframe RSI Strategy

This strategy analyzes RSI across multiple timeframes to identify
high-probability trading opportunities. It looks for RSI convergence
and divergence across different time periods for signal confirmation.

Strategy Logic:
- Buy when RSI is oversold across multiple timeframes
- Sell when RSI is overbought across multiple timeframes
- Uses RSI momentum and divergence for signal strength
- Includes volume confirmation for signal validation
- Implements timeframe-weighted position sizing

This is a complex momentum strategy that provides comprehensive
RSI analysis across multiple time horizons.
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math


class MultiTimeframeRsiStrategy(TradingStrategy):
    """
    A complex momentum strategy using RSI across multiple timeframes.
    
    This strategy:
    1. Analyzes RSI across 1-minute, 5-minute, and 15-minute timeframes
    2. Identifies RSI convergence and divergence patterns
    3. Uses momentum analysis for signal strength calculation
    4. Includes volume confirmation for signal validation
    5. Implements timeframe-weighted position sizing
    """

    def __init__(self) -> None:
        super().__init__()
        # Track multi-timeframe RSI state
        self.state["rsi_convergence"] = 0  # 0=neutral, 1=bullish, -1=bearish
        self.state["timeframe_alignment"] = 0  # Number of timeframes aligned
        self.state["last_rsi_signal"] = 0

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """
        Select liquid stocks suitable for multi-timeframe analysis.
        """
        # Use S&P 500 stocks as they show clear multi-timeframe patterns
        return SecurityUniverseSelector.fromStandardList(StandardSymbolsList.SP_500)

    @DataParams({
        "rsi_1min": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.ONE_MINUTE, "period": 14, "count": 5},
        "rsi_5min": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.FIVE_MINUTE, "period": 14, "count": 5},
        "rsi_15min": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.FIFTEEN_MINUTE, "period": 14, "count": 5},
        "current_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_MINUTE, "count": 1},
        "volume_sma": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.ONE_MINUTE, "period": 20, "count": 1}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """
        Evaluate multi-timeframe RSI conditions for trade signals.
        """
        rsi_1min = data["rsi_1min"]
        rsi_5min = data["rsi_5min"]
        rsi_15min = data["rsi_15min"]
        current_bar = data["current_bar"][-1]
        volume_sma = data["volume_sma"]
        
        # Need at least 5 data points for momentum analysis
        if len(rsi_1min) < 5 or len(rsi_5min) < 5 or len(rsi_15min) < 5:
            return None
        
        # Extract current and previous RSI values
        current_rsi_1min = rsi_1min[-1].value
        prev_rsi_1min = rsi_1min[-2].value
        current_rsi_5min = rsi_5min[-1].value
        prev_rsi_5min = rsi_5min[-2].value
        current_rsi_15min = rsi_15min[-1].value
        prev_rsi_15min = rsi_15min[-2].value
        
        # Calculate RSI momentum across timeframes
        rsi_momentum_1min = current_rsi_1min - prev_rsi_1min
        rsi_momentum_5min = current_rsi_5min - prev_rsi_5min
        rsi_momentum_15min = current_rsi_15min - prev_rsi_15min
        
        # Calculate RSI divergence across timeframes
        rsi_divergence_1min = self._calculate_rsi_divergence(rsi_1min)
        rsi_divergence_5min = self._calculate_rsi_divergence(rsi_5min)
        rsi_divergence_15min = self._calculate_rsi_divergence(rsi_15min)
        
        # Volume confirmation
        current_volume = current_bar.volume
        avg_volume = volume_sma.value
        volume_ratio = current_volume / avg_volume if avg_volume > 0 else 1
        
        # Buy signal: Oversold RSI across multiple timeframes with momentum
        if (current_rsi_1min < 30 and current_rsi_5min < 35 and current_rsi_15min < 40 and  # Oversold levels
            rsi_momentum_1min > 0 and rsi_momentum_5min > 0 and  # Positive momentum
            volume_ratio > 1.2):  # Volume confirmation
            
            # Calculate signal strength based on RSI alignment and momentum
            rsi_alignment_score = self._calculate_rsi_alignment_score(
                current_rsi_1min, current_rsi_5min, current_rsi_15min, "oversold")
            momentum_score = self._calculate_momentum_score(
                rsi_momentum_1min, rsi_momentum_5min, rsi_momentum_15min)
            divergence_score = self._calculate_divergence_score(
                rsi_divergence_1min, rsi_divergence_5min, rsi_divergence_15min)
            
            # Combine scores with volume confirmation
            signal_strength = int((rsi_alignment_score + momentum_score + divergence_score) / 3 * volume_ratio)
            signal_strength = min(signal_strength, 100)
            
            # Update state
            self.state["rsi_convergence"] = 1
            self.state["timeframe_alignment"] = 3
            self.state["last_rsi_signal"] = len(rsi_1min)
            
            return TradeSignal(security, PositionType.LONG, signal_strength)
        
        # Sell signal: Overbought RSI across multiple timeframes with momentum
        elif (current_rsi_1min > 70 and current_rsi_5min > 65 and current_rsi_15min > 60 and  # Overbought levels
              rsi_momentum_1min < 0 and rsi_momentum_5min < 0 and  # Negative momentum
              volume_ratio > 1.2):  # Volume confirmation
            
            # Calculate signal strength based on RSI alignment and momentum
            rsi_alignment_score = self._calculate_rsi_alignment_score(
                current_rsi_1min, current_rsi_5min, current_rsi_15min, "overbought")
            momentum_score = self._calculate_momentum_score(
                rsi_momentum_1min, rsi_momentum_5min, rsi_momentum_15min)
            divergence_score = self._calculate_divergence_score(
                rsi_divergence_1min, rsi_divergence_5min, rsi_divergence_15min)
            
            # Combine scores with volume confirmation
            signal_strength = int((rsi_alignment_score + momentum_score + divergence_score) / 3 * volume_ratio)
            signal_strength = min(signal_strength, 100)
            
            # Update state
            self.state["rsi_convergence"] = -1
            self.state["timeframe_alignment"] = 3
            self.state["last_rsi_signal"] = len(rsi_1min)
            
            return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        # Additional signal: Strong RSI momentum in one timeframe with confirmation
        elif volume_ratio > 1.5:  # High volume spike
            
            # Strong bullish momentum in 1-minute with 5-minute confirmation
            if (rsi_momentum_1min > 10 and rsi_momentum_5min > 5 and 
                current_rsi_1min < 50 and current_rsi_5min < 50):
                signal_strength = int(min(abs(rsi_momentum_1min) * 5, 100))
                return TradeSignal(security, PositionType.LONG, signal_strength)
                
            # Strong bearish momentum in 1-minute with 5-minute confirmation
            elif (rsi_momentum_1min < -10 and rsi_momentum_5min < -5 and 
                  current_rsi_1min > 50 and current_rsi_5min > 50):
                signal_strength = int(min(abs(rsi_momentum_1min) * 5, 100))
                return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        return None

    def _calculate_rsi_divergence(self, rsi_values: List[Any]) -> float:
        """Calculate RSI divergence strength."""
        if len(rsi_values) < 3:
            return 0.0
        
        # Simple divergence calculation based on RSI slope
        recent_rsi = [rsi.value for rsi in rsi_values[-3:]]
        rsi_slope = recent_rsi[-1] - recent_rsi[0]
        
        return abs(rsi_slope)

    def _calculate_rsi_alignment_score(self, rsi_1min: float, rsi_5min: float, 
                                     rsi_15min: float, condition: str) -> float:
        """Calculate RSI alignment score across timeframes."""
        if condition == "oversold":
            # Score based on how oversold each timeframe is
            score_1min = max(0, 30 - rsi_1min) * 2
            score_5min = max(0, 35 - rsi_5min) * 1.5
            score_15min = max(0, 40 - rsi_15min) * 1
        else:  # overbought
            # Score based on how overbought each timeframe is
            score_1min = max(0, rsi_1min - 70) * 2
            score_5min = max(0, rsi_5min - 65) * 1.5
            score_15min = max(0, rsi_15min - 60) * 1
        
        return min((score_1min + score_5min + score_15min) / 3, 100)

    def _calculate_momentum_score(self, momentum_1min: float, momentum_5min: float, 
                                momentum_15min: float) -> float:
        """Calculate momentum score across timeframes."""
        # Weight shorter timeframes more heavily
        weighted_momentum = (abs(momentum_1min) * 0.5 + 
                           abs(momentum_5min) * 0.3 + 
                           abs(momentum_15min) * 0.2)
        
        return min(weighted_momentum * 10, 100)

    def _calculate_divergence_score(self, divergence_1min: float, divergence_5min: float, 
                                  divergence_15min: float) -> float:
        """Calculate divergence score across timeframes."""
        # Average divergence strength across timeframes
        avg_divergence = (divergence_1min + divergence_5min + divergence_15min) / 3
        
        return min(avg_divergence * 20, 100)

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """
        Process trade signals with multi-timeframe RSI allocation.
        """
        # Sort signals by strength and take top 4 for concentrated positions
        sorted_signals = sorted(tradeSignals, key=lambda x: x.strength if x.strength is not None else 0, reverse=True)
        top_signals = sorted_signals[:4]
        
        # Use portfolio allocator for multi-timeframe strategy
        portfolioAllocator = PercentBasedPortfolioAllocator(25)  # 25% per position
        return portfolioAllocator.allocatePortfolio(portfolio, top_signals)

    def getStandardCloseCondition(self) -> StandardCloseCriteria | None:
        """
        Set standard exit criteria for multi-timeframe RSI trades.
        """
        return StandardCloseCriteria(
            targetProfit=6,                      # Take profit at 6% gain
            stopLoss=-3,                         # Stop loss at 3% loss
            trailingStop=-1.5,                   # Trailing stop at 1.5% from peak
            timeOut=TimeDelta(5, TimeUnit.DAYS)  # Exit after 5 days
        )

    @DataParams({
        "rsi_1min": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.ONE_MINUTE, "period": 14, "count": 1},
        "rsi_5min": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.FIVE_MINUTE, "period": 14, "count": 1},
        "rsi_15min": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.FIFTEEN_MINUTE, "period": 14, "count": 1}
    })
    def evaluateCloseTradeCondition(self, openPos: OpenPosition, data: Dict[str, Any]) -> TradeOrder | None:
        """
        Custom exit condition: Close based on RSI reversal across timeframes.
        """
        rsi_1min = data["rsi_1min"]
        rsi_5min = data["rsi_5min"]
        rsi_15min = data["rsi_15min"]
        
        current_rsi_1min = rsi_1min.value
        current_rsi_5min = rsi_5min.value
        current_rsi_15min = rsi_15min.value
        
        # Close long position if RSI becomes overbought across timeframes
        if openPos.position == PositionType.LONG:
            if (current_rsi_1min > 70 and current_rsi_5min > 65):  # Overbought in key timeframes
                return TradeOrder(openPos.security, TradeType.SELL)
        
        # Close short position if RSI becomes oversold across timeframes
        elif openPos.position == PositionType.SHORT:
            if (current_rsi_1min < 30 and current_rsi_5min < 35):  # Oversold in key timeframes
                return TradeOrder(openPos.security, TradeType.BUY)
        
        return None
