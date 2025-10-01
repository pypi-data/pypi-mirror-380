"""
Volume Price Trend Strategy

This strategy combines volume analysis with price momentum to identify
strong buying or selling pressure. It looks for volume confirmation
of price movements to generate high-probability trade signals.

Strategy Logic:
- Buy when price rises with above-average volume (accumulation)
- Sell when price falls with above-average volume (distribution)
- Uses volume-weighted price momentum for signal strength
- Includes volume trend analysis for confirmation
- Implements volume-based position sizing

This is a volume-based strategy that capitalizes on institutional
buying/selling patterns and market sentiment shifts.
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math


class VolumePriceTrendStrategy(TradingStrategy):
    """
    A volume-based strategy that combines price momentum with volume analysis.
    
    This strategy:
    1. Identifies accumulation patterns (price up + high volume)
    2. Identifies distribution patterns (price down + high volume)
    3. Uses volume-weighted momentum for signal strength
    4. Includes volume trend confirmation
    5. Implements volume-based position sizing
    """

    def __init__(self) -> None:
        super().__init__()
        # Track volume patterns to identify institutional activity
        self.state["volume_trend"] = 0  # 0=neutral, 1=increasing, -1=decreasing
        self.state["last_volume_signal"] = 0

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """
        Select liquid stocks with good volume characteristics.
        """
        # Use Russell 1000 stocks as they have good volume and institutional interest
        return SecurityUniverseSelector.fromStandardList(StandardSymbolsList.RUSSELL_1000)

    @DataParams({
        "price_bars": {"datatype": DataType.BARS, "barinterval": BarInterval.FIVE_MINUTE, "count": 10},
        "volume_sma": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.FIVE_MINUTE, "period": 20, "count": 1},
        "volume_trend": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.FIVE_MINUTE, "period": 5, "count": 5}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """
        Evaluate volume-price relationships for trade signals.
        """
        price_bars = data["price_bars"]
        volume_sma = data["volume_sma"]
        volume_trend = data["volume_trend"]
        
        # Need at least 5 bars for analysis
        if len(price_bars) < 5 or len(volume_trend) < 5:
            return None
        
        # Calculate price momentum
        current_price = price_bars[-1].close
        prev_price = price_bars[-2].close
        price_change = current_price - prev_price
        price_change_pct = (price_change / prev_price) * 100 if prev_price != 0 else 0
        
        # Calculate volume metrics
        current_volume = price_bars[-1].volume
        avg_volume = volume_sma.value
        volume_ratio = current_volume / avg_volume if avg_volume > 0 else 1
        
        # Calculate volume trend (5-period volume momentum)
        recent_volumes = [v.value for v in volume_trend]
        volume_momentum = (recent_volumes[-1] - recent_volumes[0]) / recent_volumes[0] if recent_volumes[0] != 0 else 0
        
        # Calculate volume-weighted price momentum
        vw_momentum = price_change_pct * volume_ratio
        
        # Buy signal: Price up with high volume (accumulation)
        if (price_change > 0 and volume_ratio > 1.5 and 
            volume_momentum > 0.1 and vw_momentum > 2.0):
            
            # Calculate signal strength based on volume confirmation and momentum
            volume_strength = min(volume_ratio * 20, 100)
            momentum_strength = min(abs(vw_momentum) * 10, 100)
            signal_strength = int((volume_strength + momentum_strength) / 2)
            
            # Update state
            self.state["last_volume_signal"] = len(price_bars)
            self.state["volume_trend"] = 1
            
            return TradeSignal(security, PositionType.LONG, signal_strength)
        
        # Sell signal: Price down with high volume (distribution)
        elif (price_change < 0 and volume_ratio > 1.5 and 
              volume_momentum > 0.1 and vw_momentum < -2.0):
            
            # Calculate signal strength based on volume confirmation and momentum
            volume_strength = min(volume_ratio * 20, 100)
            momentum_strength = min(abs(vw_momentum) * 10, 100)
            signal_strength = int((volume_strength + momentum_strength) / 2)
            
            # Update state
            self.state["last_volume_signal"] = len(price_bars)
            self.state["volume_trend"] = -1
            
            return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        # Additional signal: Volume breakout with price confirmation
        elif volume_ratio > 2.0 and abs(price_change_pct) > 1.0:
            
            if price_change > 0:  # Volume breakout to upside
                signal_strength = int(min(volume_ratio * 15, 100))
                return TradeSignal(security, PositionType.LONG, signal_strength)
                
            elif price_change < 0:  # Volume breakout to downside
                signal_strength = int(min(volume_ratio * 15, 100))
                return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        return None

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """
        Process trade signals with volume-based allocation.
        """
        # Sort signals by strength and take top 6 for volume diversification
        sorted_signals = sorted(tradeSignals, key=lambda x: x.strength if x.strength is not None else 0, reverse=True)
        top_signals = sorted_signals[:6]
        
        # Use portfolio allocator for volume-based strategy
        portfolioAllocator = PercentBasedPortfolioAllocator(16)  # 16% per position
        return portfolioAllocator.allocatePortfolio(portfolio, top_signals)

    def getStandardCloseCondition(self) -> StandardCloseCriteria | None:
        """
        Set standard exit criteria for volume-based trades.
        """
        return StandardCloseCriteria(
            targetProfit=4,                      # Take profit at 4% gain
            stopLoss=-2.5,                       # Stop loss at 2.5% loss
            trailingStop=-1,                     # Trailing stop at 1% from peak
            timeOut=TimeDelta(3, TimeUnit.DAYS)  # Exit after 3 days
        )

    @DataParams({
        "current_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.FIVE_MINUTE, "count": 1},
        "volume_sma": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.FIVE_MINUTE, "period": 20, "count": 1}
    })
    def evaluateCloseTradeCondition(self, openPos: OpenPosition, data: Dict[str, Any]) -> TradeOrder | None:
        """
        Custom exit condition: Close based on volume drying up.
        """
        current_bar = data["current_bar"][-1]
        volume_sma = data["volume_sma"]
        
        current_volume = current_bar.volume
        avg_volume = volume_sma.value
        volume_ratio = current_volume / avg_volume if avg_volume > 0 else 1
        
        # Close position if volume dries up significantly (< 50% of average)
        if volume_ratio < 0.5:
            if openPos.position == PositionType.LONG:
                return TradeOrder(openPos.security, TradeType.SELL)
            elif openPos.position == PositionType.SHORT:
                return TradeOrder(openPos.security, TradeType.BUY)
        
        return None
