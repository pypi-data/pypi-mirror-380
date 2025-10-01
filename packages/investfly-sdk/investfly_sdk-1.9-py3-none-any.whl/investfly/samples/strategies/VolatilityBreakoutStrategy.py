"""
Volatility Breakout Strategy

This strategy identifies breakouts from low volatility periods and trades
the resulting directional moves. It uses ATR and Bollinger Bands to detect
volatility expansion and breakout opportunities.

Strategy Logic:
- Buy when price breaks above upper Bollinger Band with expanding ATR
- Sell when price breaks below lower Bollinger Band with expanding ATR
- Uses volatility expansion for signal strength calculation
- Includes volume confirmation for breakout validation
- Implements volatility-adjusted position sizing

This is a breakout strategy that capitalizes on volatility expansion
and price breakouts from consolidation periods.
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math


class VolatilityBreakoutStrategy(TradingStrategy):
    """
    A breakout strategy that identifies volatility expansion and price breakouts.
    
    This strategy:
    1. Identifies low volatility consolidation periods
    2. Detects breakouts with expanding volatility
    3. Uses ATR and Bollinger Bands for signal generation
    4. Includes volume confirmation for breakout validation
    5. Implements volatility-adjusted position sizing
    """

    def __init__(self) -> None:
        super().__init__()
        # Track volatility and breakout state
        self.state["volatility_regime"] = 0  # 0=low, 1=expanding, 2=high
        self.state["last_breakout"] = 0
        self.state["breakout_direction"] = 0  # 0=neutral, 1=bullish, -1=bearish

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """
        Select liquid stocks suitable for breakout trading.
        """
        # Use Russell 1000 stocks as they show clear breakout patterns
        return SecurityUniverseSelector.fromStandardList(StandardSymbolsList.RUSSELL_1000)

    @DataParams({
        "bb_upper": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.UPPERBBAND, "barinterval": BarInterval.ONE_MINUTE, "period": 20, "count": 3},
        "bb_lower": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.LOWERBBAND, "barinterval": BarInterval.ONE_MINUTE, "period": 20, "count": 3},
        "bb_middle": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.ONE_MINUTE, "period": 20, "count": 3},
        "atr": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.ATR, "barinterval": BarInterval.ONE_MINUTE, "period": 14, "count": 5},
        "current_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_MINUTE, "count": 3},
        "volume_sma": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.ONE_MINUTE, "period": 20, "count": 1}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """
        Evaluate volatility breakout conditions for trade signals.
        """
        bb_upper = data["bb_upper"]
        bb_lower = data["bb_lower"]
        bb_middle = data["bb_middle"]
        atr = data["atr"]
        current_bars = data["current_bar"]
        volume_sma = data["volume_sma"]
        
        # Need at least 3 data points for analysis
        if len(bb_upper) < 3 or len(bb_lower) < 3 or len(atr) < 5:
            return None
        
        # Extract current and previous values
        current_bb_upper = bb_upper[-1].value
        prev_bb_upper = bb_upper[-2].value
        current_bb_lower = bb_lower[-1].value
        prev_bb_lower = bb_lower[-2].value
        current_bb_middle = bb_middle[-1].value
        
        current_atr = atr[-1].value
        prev_atr = atr[-2].value
        atr_5_periods_ago = atr[-5].value
        
        current_price = current_bars[-1].close
        prev_price = current_bars[-2].close
        current_volume = current_bars[-1].volume
        avg_volume = volume_sma.value
        
        # Calculate volatility metrics
        bb_width = current_bb_upper - current_bb_lower
        bb_width_ratio = bb_width / current_bb_middle if current_bb_middle != 0 else 0
        
        atr_expansion = (current_atr - atr_5_periods_ago) / atr_5_periods_ago if atr_5_periods_ago != 0 else 0
        
        # Determine volatility regime
        if atr_expansion > 0.3:  # 30% ATR expansion
            self.state["volatility_regime"] = 2  # high
        elif atr_expansion > 0.1:  # 10% ATR expansion
            self.state["volatility_regime"] = 1  # expanding
        else:
            self.state["volatility_regime"] = 0  # low
        
        # Volume confirmation
        volume_ratio = current_volume / avg_volume if avg_volume > 0 else 1
        
        # Buy signal: Breakout above upper Bollinger Band with expanding volatility
        if (current_price > current_bb_upper and  # Price above upper band
            prev_price <= prev_bb_upper and  # Previous price was at or below band
            atr_expansion > 0.1 and  # ATR expanding
            volume_ratio > 1.3):  # Volume confirmation
            
            # Calculate signal strength based on breakout magnitude and volatility
            breakout_magnitude = (current_price - current_bb_upper) / current_bb_upper * 100
            volatility_strength = min(atr_expansion * 200, 100)
            volume_strength = min(volume_ratio * 20, 100)
            
            # Combine factors for signal strength
            signal_strength = int((breakout_magnitude + volatility_strength + volume_strength) / 3)
            signal_strength = min(signal_strength, 100)
            
            # Update state
            self.state["last_breakout"] = len(current_bars)
            self.state["breakout_direction"] = 1
            
            return TradeSignal(security, PositionType.LONG, signal_strength)
        
        # Sell signal: Breakdown below lower Bollinger Band with expanding volatility
        elif (current_price < current_bb_lower and  # Price below lower band
              prev_price >= prev_bb_lower and  # Previous price was at or above band
              atr_expansion > 0.1 and  # ATR expanding
              volume_ratio > 1.3):  # Volume confirmation
            
            # Calculate signal strength based on breakdown magnitude and volatility
            breakdown_magnitude = (current_bb_lower - current_price) / current_price * 100
            volatility_strength = min(atr_expansion * 200, 100)
            volume_strength = min(volume_ratio * 20, 100)
            
            # Combine factors for signal strength
            signal_strength = int((breakdown_magnitude + volatility_strength + volume_strength) / 3)
            signal_strength = min(signal_strength, 100)
            
            # Update state
            self.state["last_breakout"] = len(current_bars)
            self.state["breakout_direction"] = -1
            
            return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        # Additional signal: Strong volatility expansion with price momentum
        elif atr_expansion > 0.5 and volume_ratio > 1.5:  # High volatility expansion
            
            price_momentum = (current_price - prev_price) / prev_price * 100 if prev_price != 0 else 0
            
            if price_momentum > 1.0:  # Strong upward momentum
                signal_strength = int(min(atr_expansion * 150, 100))
                return TradeSignal(security, PositionType.LONG, signal_strength)
                
            elif price_momentum < -1.0:  # Strong downward momentum
                signal_strength = int(min(atr_expansion * 150, 100))
                return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        return None

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """
        Process trade signals with volatility breakout allocation.
        """
        # Sort signals by strength and take top 5 for breakout diversification
        sorted_signals = sorted(tradeSignals, key=lambda x: x.strength if x.strength is not None else 0, reverse=True)
        top_signals = sorted_signals[:5]
        
        # Use portfolio allocator for breakout strategy
        portfolioAllocator = PercentBasedPortfolioAllocator(20)  # 20% per position
        return portfolioAllocator.allocatePortfolio(portfolio, top_signals)

    def getStandardCloseCondition(self) -> StandardCloseCriteria | None:
        """
        Set standard exit criteria for volatility breakout trades.
        """
        # Adjust exit criteria based on volatility regime
        if self.state["volatility_regime"] == 2:  # high volatility
            return StandardCloseCriteria(
                targetProfit=8,                      # Higher profit target for high volatility
                stopLoss=-4,                         # Wider stop loss for high volatility
                trailingStop=-2,                     # Wider trailing stop
                timeOut=TimeDelta(3, TimeUnit.DAYS)  # Shorter holding period
            )
        elif self.state["volatility_regime"] == 1:  # expanding volatility
            return StandardCloseCriteria(
                targetProfit=6,                      # Medium profit target
                stopLoss=-3,                         # Medium stop loss
                trailingStop=-1.5,                   # Medium trailing stop
                timeOut=TimeDelta(5, TimeUnit.DAYS)  # Medium holding period
            )
        else:  # low volatility
            return StandardCloseCriteria(
                targetProfit=4,                      # Lower profit target for low volatility
                stopLoss=-2,                         # Tighter stop loss for low volatility
                trailingStop=-1,                     # Tighter trailing stop
                timeOut=TimeDelta(7, TimeUnit.DAYS)  # Longer holding period
            )

    @DataParams({
        "bb_middle": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.ONE_MINUTE, "period": 20, "count": 1},
        "atr": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.ATR, "barinterval": BarInterval.ONE_MINUTE, "period": 14, "count": 1}
    })
    def evaluateCloseTradeCondition(self, openPos: OpenPosition, data: Dict[str, Any]) -> TradeOrder | None:
        """
        Custom exit condition: Close based on volatility contraction or trend reversal.
        """
        bb_middle = data["bb_middle"]
        atr = data["atr"]
        
        current_bb_middle = bb_middle.value
        current_atr = atr.value
        
        # Close long position if price falls below middle band (trend reversal)
        if openPos.position == PositionType.LONG:
            if openPos.avgPrice > current_bb_middle * 1.02:  # Price significantly above middle band
                return TradeOrder(openPos.security, TradeType.SELL)
        
        # Close short position if price rises above middle band (trend reversal)
        elif openPos.position == PositionType.SHORT:
            if openPos.avgPrice < current_bb_middle * 0.98:  # Price significantly below middle band
                return TradeOrder(openPos.security, TradeType.BUY)
        
        return None
