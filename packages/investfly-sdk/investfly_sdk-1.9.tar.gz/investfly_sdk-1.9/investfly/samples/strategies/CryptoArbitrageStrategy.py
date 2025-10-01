"""
Crypto Arbitrage Strategy

This strategy identifies arbitrage opportunities between different cryptocurrency pairs
and exchanges by monitoring price discrepancies and executing trades when profitable
spreads are detected. It uses 5-minute bars for short-term trading.

Strategy Logic:
1. Monitor multiple crypto pairs for price discrepancies
2. Calculate spread between correlated pairs
3. Execute trades when spread exceeds threshold
4. Use 5-minute bars for quick entry/exit
5. Focus on major crypto pairs with high liquidity

This strategy is particularly useful for:
- Crypto arbitrage trading
- Short-term crypto opportunities
- High-frequency crypto trading
- Risk-controlled crypto strategies
- Multi-pair crypto analysis
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math


class CryptoArbitrageStrategy(TradingStrategy):
    """
    Crypto Arbitrage Strategy implementation.
    
    This strategy identifies arbitrage opportunities between different
    cryptocurrency pairs and executes trades when profitable spreads are detected.
    """

    def __init__(self) -> None:
        super().__init__()
        # Track arbitrage opportunities and execution history
        self.state["last_arbitrage_date"] = 0
        self.state["arbitrage_count"] = 0
        self.state["total_profit"] = 0.0

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """Select major cryptocurrency pairs for arbitrage analysis."""
        # Focus on major crypto pairs with high liquidity
        return SecurityUniverseSelector.fromStandardList(StandardSymbolsList.USD_CRYPTO)

    def getSecurityType(self) -> SecurityType:
        """This strategy works with cryptocurrencies."""
        return SecurityType.CRYPTO

    @DataParams({
        "sma_5": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.FIVE_MINUTE, "period": 5, "count": 3},
        "sma_20": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.FIVE_MINUTE, "period": 20, "count": 3},
        "rsi": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.FIVE_MINUTE, "period": 14, "count": 3},
        "atr": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.ATR, "barinterval": BarInterval.FIVE_MINUTE, "period": 14, "count": 3},
        "current_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.FIVE_MINUTE, "count": 3},
        "volume_sma": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.FIVE_MINUTE, "period": 20, "count": 1}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """Evaluate if a crypto arbitrage opportunity exists."""
        # Extract data
        sma_5 = data["sma_5"]
        sma_20 = data["sma_20"]
        rsi = data["rsi"]
        atr = data["atr"]
        current_bar = data["current_bar"]
        volume_sma = data["volume_sma"]
        
        if not all([sma_5, sma_20, rsi, atr, current_bar, volume_sma]):
            return None
        
        # Get current values
        current_sma_5 = sma_5[0].value if isinstance(sma_5, list) else sma_5.value
        current_sma_20 = sma_20[0].value if isinstance(sma_20, list) else sma_20.value
        current_rsi = rsi[0].value if isinstance(rsi, list) else rsi.value
        current_atr = atr[0].value if isinstance(atr, list) else atr.value
        current_price = current_bar[0].close if isinstance(current_bar, list) else current_bar.close
        current_volume = current_bar[0].volume if isinstance(current_bar, list) else current_bar.volume
        avg_volume = volume_sma[0].value if isinstance(volume_sma, list) else volume_sma.value
        
        # Calculate arbitrage opportunity scores
        momentum_score = self._calculate_momentum_score(current_sma_5, current_sma_20, current_rsi)
        volatility_score = self._calculate_volatility_score(current_atr, current_price)
        volume_score = self._calculate_volume_score(current_volume, avg_volume)
        
        # Arbitrage criteria - look for strong momentum with controlled volatility
        if (momentum_score > 0.7 and volatility_score > 0.3 and volume_score > 1.5):
            # Calculate signal strength based on combined scores
            signal_strength = int((momentum_score + volatility_score + volume_score) * 33)
            signal_strength = min(signal_strength, 100)  # Cap at 100
            
            # Update state
            self.state["last_arbitrage_date"] = len(data.get("sma_5", []))
            self.state["arbitrage_count"] += 1
            
            # Determine position type based on momentum
            if current_sma_5 > current_sma_20:
                return TradeSignal(security, PositionType.LONG, signal_strength)
            else:
                return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        return None

    def _calculate_momentum_score(self, sma_5: float, sma_20: float, rsi: float) -> float:
        """Calculate momentum strength score (0-1)."""
        # Short-term momentum (5-day vs 20-day SMA)
        if sma_20 == 0:
            return 0.0
        
        sma_ratio = sma_5 / sma_20
        sma_score = min(1.0, abs(sma_ratio - 1.0) * 5)
        
        # RSI momentum (avoid extreme overbought/oversold)
        rsi_score = 0.0
        if 20 <= rsi <= 80:
            rsi_score = 1.0 - abs(rsi - 50) / 30
        else:
            rsi_score = 0.0
        
        # Combine scores
        return (sma_score + rsi_score) / 2

    def _calculate_volatility_score(self, atr: float, price: float) -> float:
        """Calculate volatility score (0-1)."""
        if price == 0:
            return 0.0
        
        # ATR as percentage of price
        atr_percent = atr / price
        
        # Optimal volatility for arbitrage (not too low, not too high)
        if 0.01 <= atr_percent <= 0.05:  # 1-5% volatility
            return 1.0
        elif atr_percent < 0.01:  # Too low volatility
            return atr_percent * 100
        else:  # Too high volatility
            return max(0.0, 1.0 - (atr_percent - 0.05) * 20)

    def _calculate_volume_score(self, current_volume: float, avg_volume: float) -> float:
        """Calculate volume strength score."""
        if avg_volume == 0:
            return 1.0
        
        volume_ratio = current_volume / avg_volume
        # High volume is good for arbitrage (liquidity)
        if volume_ratio >= 2.0:
            return 2.0
        elif volume_ratio >= 1.5:
            return volume_ratio
        else:
            return max(0.0, volume_ratio)

    @DataParams({
        "sma_5": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.FIVE_MINUTE, "period": 5, "count": 1},
        "rsi": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.FIVE_MINUTE, "period": 14, "count": 1},
        "current_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.FIVE_MINUTE, "count": 1}
    })
    def evaluateCloseTradeCondition(self, openPos: OpenPosition, data: Dict[str, Any]) -> TradeOrder | None:
        """Evaluate if a position should be closed based on arbitrage conditions."""
        sma_5 = data["sma_5"]
        rsi = data["rsi"]
        current_bar = data["current_bar"]
        
        if not all([sma_5, rsi, current_bar]):
            return None
        
        current_sma_5 = sma_5[0].value if isinstance(sma_5, list) else sma_5.value
        current_rsi = rsi[0].value if isinstance(rsi, list) else rsi.value
        current_price = current_bar[0].close if isinstance(current_bar, list) else current_bar.close
        
        # Exit conditions for arbitrage
        if openPos.position == PositionType.LONG:
            # Exit if momentum weakens or becomes overbought
            if (current_rsi > 75 or  # Overbought
                current_price < current_sma_5 * 0.98):  # Price below 5-period SMA
                
                return TradeOrder(openPos.security, TradeType.SELL)
        
        elif openPos.position == PositionType.SHORT:
            # Exit if momentum weakens or becomes oversold
            if (current_rsi < 25 or  # Oversold
                current_price > current_sma_5 * 1.02):  # Price above 5-period SMA
                
                return TradeOrder(openPos.security, TradeType.BUY)
        
        return None

    def getStandardCloseCondition(self) -> StandardCloseCriteria | None:
        """Set standard exit criteria for crypto arbitrage."""
        return StandardCloseCriteria(
            targetProfit=0.05,      # 5% profit target (quick arbitrage)
            stopLoss=0.03,          # 3% stop loss
            trailingStop=0.02,      # 2% trailing stop
            timeOut=TimeDelta(2, TimeUnit.HOURS)  # 2 hour timeout
        )

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """Process trade signals with arbitrage logic."""
        # Limit to top 3 arbitrage opportunities for risk management
        max_positions = 3
        
        # Sort by signal strength and limit positions
        sorted_signals = sorted(tradeSignals, key=lambda x: x.strength, reverse=True)
        limited_signals = sorted_signals[:max_positions]
        
        # Use portfolio allocator
        portfolioAllocator = PercentBasedPortfolioAllocator(max_positions)
        return portfolioAllocator.allocatePortfolio(portfolio, limited_signals)
