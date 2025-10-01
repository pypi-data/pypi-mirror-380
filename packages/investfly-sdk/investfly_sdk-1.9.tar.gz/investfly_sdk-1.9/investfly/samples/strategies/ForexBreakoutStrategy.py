"""
Forex Breakout Strategy

This strategy identifies breakout opportunities in forex pairs by monitoring
support/resistance levels and volume confirmation. It uses 15-minute bars
for medium-term trading and focuses on major currency pairs.

Strategy Logic:
1. Monitor forex pairs for breakout patterns
2. Identify key support/resistance levels
3. Wait for volume confirmation on breakouts
4. Use 15-minute bars for medium-term holds
5. Focus on major currency pairs with high liquidity

This strategy is particularly useful for:
- Forex breakout trading
- Support/resistance analysis
- Volume-based forex strategies
- Medium-term forex positions
- Major currency pair trading
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math


class ForexBreakoutStrategy(TradingStrategy):
    """
    Forex Breakout Strategy implementation.
    
    This strategy identifies breakout opportunities in forex pairs by monitoring
    support/resistance levels and volume confirmation.
    """

    def __init__(self) -> None:
        super().__init__()
        # Track breakout patterns and execution history
        self.state["last_breakout_date"] = 0
        self.state["breakout_count"] = 0
        self.state["successful_breakouts"] = 0

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """Select major forex pairs for breakout analysis."""
        # Focus on major forex pairs with high liquidity
        return SecurityUniverseSelector.fromStandardList(StandardSymbolsList.ALL_FOREX)

    def getSecurityType(self) -> SecurityType:
        """This strategy works with forex pairs."""
        return SecurityType.FOREX

    @DataParams({
        "sma_20": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.FIFTEEN_MINUTE, "period": 20, "count": 3},
        "sma_50": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.FIFTEEN_MINUTE, "period": 50, "count": 3},
        "rsi": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.FIFTEEN_MINUTE, "period": 14, "count": 3},
        "atr": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.ATR, "barinterval": BarInterval.FIFTEEN_MINUTE, "period": 14, "count": 3},
        "current_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.FIFTEEN_MINUTE, "count": 5},
        "volume_sma": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.FIFTEEN_MINUTE, "period": 20, "count": 1}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """Evaluate if a forex breakout opportunity exists."""
        # Extract data
        sma_20 = data["sma_20"]
        sma_50 = data["sma_50"]
        rsi = data["rsi"]
        atr = data["atr"]
        current_bar = data["current_bar"]
        volume_sma = data["volume_sma"]
        
        if not all([sma_20, sma_50, rsi, atr, current_bar, volume_sma]):
            return None
        
        # Get current values
        current_sma_20 = sma_20[0].value if isinstance(sma_20, list) else sma_20.value
        current_sma_50 = sma_50[0].value if isinstance(sma_50, list) else sma_50.value
        current_rsi = rsi[0].value if isinstance(rsi, list) else rsi.value
        current_atr = atr[0].value if isinstance(atr, list) else atr.value
        current_price = current_bar[0].close if isinstance(current_bar, list) else current_bar.close
        current_volume = current_bar[0].volume if isinstance(current_bar, list) else current_bar.volume
        avg_volume = volume_sma[0].value if isinstance(volume_sma, list) else volume_sma.value
        
        # Calculate breakout scores
        trend_score = self._calculate_trend_score(current_sma_20, current_sma_50)
        momentum_score = self._calculate_momentum_score(current_rsi)
        volatility_score = self._calculate_volatility_score(current_atr, current_price)
        volume_score = self._calculate_volume_score(current_volume, avg_volume)
        
        # Breakout criteria - look for strong trend with momentum and volume
        if (trend_score > 0.6 and momentum_score > 0.5 and 
            volatility_score > 0.4 and volume_score > 1.3):
            
            # Calculate signal strength based on combined scores
            signal_strength = int((trend_score + momentum_score + volatility_score + volume_score) * 25)
            signal_strength = min(signal_strength, 100)  # Cap at 100
            
            # Update state
            self.state["last_breakout_date"] = len(data.get("sma_20", []))
            self.state["breakout_count"] += 1
            
            # Determine position type based on trend
            if current_sma_20 > current_sma_50:
                return TradeSignal(security, PositionType.LONG, signal_strength)
            else:
                return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        return None

    def _calculate_trend_score(self, sma_20: float, sma_50: float) -> float:
        """Calculate trend strength score (0-1)."""
        if sma_50 == 0:
            return 0.0
        
        # Trend is positive when 20-period SMA > 50-period SMA
        trend_ratio = sma_20 / sma_50
        if trend_ratio > 1.0:
            # Strong uptrend
            return min(1.0, (trend_ratio - 1.0) * 10 + 0.5)
        else:
            # Weak or downtrend
            return max(0.0, trend_ratio - 0.9) * 5

    def _calculate_momentum_score(self, rsi: float) -> float:
        """Calculate momentum strength score (0-1)."""
        # RSI momentum (avoid extreme overbought/oversold for breakouts)
        if 25 <= rsi <= 75:
            # Good momentum range for breakouts
            return 1.0 - abs(rsi - 50) / 25
        elif rsi > 75:
            # Overbought - momentum may be fading
            return max(0.0, 1.0 - (rsi - 75) / 25)
        else:  # rsi < 25
            # Oversold - momentum may be fading
            return max(0.0, 1.0 - (25 - rsi) / 25)

    def _calculate_volatility_score(self, atr: float, price: float) -> float:
        """Calculate volatility score (0-1)."""
        if price == 0:
            return 0.0
        
        # ATR as percentage of price
        atr_percent = atr / price
        
        # Optimal volatility for breakouts (not too low, not too high)
        if 0.005 <= atr_percent <= 0.02:  # 0.5-2% volatility
            return 1.0
        elif atr_percent < 0.005:  # Too low volatility
            return atr_percent * 200
        else:  # Too high volatility
            return max(0.0, 1.0 - (atr_percent - 0.02) * 50)

    def _calculate_volume_score(self, current_volume: float, avg_volume: float) -> float:
        """Calculate volume strength score."""
        if avg_volume == 0:
            return 1.0
        
        volume_ratio = current_volume / avg_volume
        # High volume confirms breakouts
        if volume_ratio >= 1.5:
            return min(2.0, volume_ratio)
        elif volume_ratio >= 1.3:
            return volume_ratio
        else:
            return max(0.0, volume_ratio)

    @DataParams({
        "sma_20": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.FIFTEEN_MINUTE, "period": 20, "count": 1},
        "rsi": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.FIFTEEN_MINUTE, "period": 14, "count": 1},
        "current_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.FIFTEEN_MINUTE, "count": 1}
    })
    def evaluateCloseTradeCondition(self, openPos: OpenPosition, data: Dict[str, Any]) -> TradeOrder | None:
        """Evaluate if a position should be closed based on breakout conditions."""
        sma_20 = data["sma_20"]
        rsi = data["rsi"]
        current_bar = data["current_bar"]
        
        if not all([sma_20, rsi, current_bar]):
            return None
        
        current_sma_20 = sma_20[0].value if isinstance(sma_20, list) else sma_20.value
        current_rsi = rsi[0].value if isinstance(rsi, list) else rsi.value
        current_price = current_bar[0].close if isinstance(current_bar, list) else current_bar.close
        
        # Exit conditions for breakouts
        if openPos.position == PositionType.LONG:
            # Exit if trend weakens or momentum fades
            if (current_price < current_sma_20 * 0.98 or  # Price below 20-period SMA
                current_rsi > 80 or  # Overbought
                current_rsi < 20):   # Oversold
                
                return TradeOrder(openPos.security, TradeType.SELL)
        
        elif openPos.position == PositionType.SHORT:
            # Exit if trend weakens or momentum fades
            if (current_price > current_sma_20 * 1.02 or  # Price above 20-period SMA
                current_rsi < 20 or  # Oversold
                current_rsi > 80):   # Overbought
                
                return TradeOrder(openPos.security, TradeType.BUY)
        
        return None

    def getStandardCloseCondition(self) -> StandardCloseCriteria | None:
        """Set standard exit criteria for forex breakouts."""
        return StandardCloseCriteria(
            targetProfit=0.03,      # 3% profit target (forex)
            stopLoss=0.02,          # 2% stop loss
            trailingStop=0.015,     # 1.5% trailing stop
            timeOut=TimeDelta(8, TimeUnit.HOURS)  # 8 hour timeout
        )

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """Process trade signals with breakout logic."""
        # Limit to top 4 breakout opportunities for diversification
        max_positions = 4
        
        # Sort by signal strength and limit positions
        sorted_signals = sorted(tradeSignals, key=lambda x: x.strength, reverse=True)
        limited_signals = sorted_signals[:max_positions]
        
        # Use portfolio allocator
        portfolioAllocator = PercentBasedPortfolioAllocator(max_positions)
        return portfolioAllocator.allocatePortfolio(portfolio, limited_signals)
