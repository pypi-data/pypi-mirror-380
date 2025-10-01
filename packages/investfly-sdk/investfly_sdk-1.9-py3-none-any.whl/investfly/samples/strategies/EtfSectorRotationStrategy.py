"""
ETF Sector Rotation Strategy

This strategy identifies sector rotation opportunities by analyzing relative strength
of different ETF sectors and rotating into stronger sectors while avoiding weaker ones.
It uses daily bars for swing trading and focuses on major sector ETFs.

Strategy Logic:
1. Monitor multiple sector ETFs for relative strength
2. Calculate momentum and trend indicators for each sector
3. Rotate into sectors showing strongest momentum
4. Exit positions when sector momentum weakens
5. Use daily bars for swing trading (1-2 week holds)

This strategy is particularly useful for:
- Sector rotation strategies
- ETF-focused portfolios
- Swing trading (daily timeframe)
- Diversification across sectors
- Momentum-based allocation
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math


class EtfSectorRotationStrategy(TradingStrategy):
    """
    ETF Sector Rotation Strategy implementation.
    
    This strategy identifies sector rotation opportunities by analyzing
    relative strength and momentum of different sector ETFs.
    """

    def __init__(self) -> None:
        super().__init__()
        # Track sector performance and rotation history
        self.state["last_rotation_date"] = 0
        self.state["current_sector_count"] = 0
        self.state["rotation_count"] = 0

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """Select major sector ETFs for analysis."""
        # Focus on major sector ETFs for sector rotation
        return SecurityUniverseSelector.fromStandardList(StandardSymbolsList.ETFS)

    def getSecurityType(self) -> SecurityType:
        """This strategy works with ETFs (which use SecurityType.STOCK)."""
        return SecurityType.STOCK

    @DataParams({
        "sma_20": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.ONE_DAY, "period": 20, "count": 3},
        "sma_50": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.ONE_DAY, "period": 50, "count": 3},
        "rsi": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.ONE_DAY, "period": 14, "count": 3},
        "macd": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.MACD, "barinterval": BarInterval.ONE_DAY, "period": 12, "count": 3},
        "macd_signal": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.MACDS, "barinterval": BarInterval.ONE_DAY, "period": 12, "count": 3},
        "current_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_DAY, "count": 1},
        "volume_sma": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.ONE_DAY, "period": 20, "count": 1}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """Evaluate if a sector ETF should be bought based on momentum and trend."""
        # Extract data
        sma_20 = data["sma_20"]
        sma_50 = data["sma_50"]
        rsi = data["rsi"]
        macd = data["macd"]
        macd_signal = data["macd_signal"]
        current_bar = data["current_bar"]
        volume_sma = data["volume_sma"]
        
        if not all([sma_20, sma_50, rsi, macd, macd_signal, current_bar, volume_sma]):
            return None
        
        # Get current values
        current_sma_20 = sma_20[0].value if isinstance(sma_20, list) else sma_20.value
        current_sma_50 = sma_50[0].value if isinstance(sma_50, list) else sma_50.value
        current_rsi = rsi[0].value if isinstance(rsi, list) else rsi.value
        current_macd = macd[0].value if isinstance(macd, list) else macd.value
        current_macd_signal = macd_signal[0].value if isinstance(macd_signal, list) else macd_signal.value
        current_price = current_bar[0].close if isinstance(current_bar, list) else current_bar.close
        current_volume = current_bar[0].volume if isinstance(current_bar, list) else current_bar.volume
        avg_volume = volume_sma[0].value if isinstance(volume_sma, list) else volume_sma.value
        
        # Calculate momentum and trend scores
        trend_score = self._calculate_trend_score(current_sma_20, current_sma_50)
        momentum_score = self._calculate_momentum_score(current_rsi, current_macd, current_macd_signal)
        volume_score = self._calculate_volume_score(current_volume, avg_volume)
        
        # Sector rotation criteria
        if (trend_score > 0.7 and momentum_score > 0.6 and volume_score > 1.2):
            # Calculate signal strength based on combined scores
            signal_strength = int((trend_score + momentum_score + volume_score) * 33)
            signal_strength = min(signal_strength, 100)  # Cap at 100
            
            # Update state
            self.state["last_rotation_date"] = len(data.get("sma_20", []))
            self.state["current_sector_count"] += 1
            
            return TradeSignal(security, PositionType.LONG, signal_strength)
        
        return None

    def _calculate_trend_score(self, sma_20: float, sma_50: float) -> float:
        """Calculate trend strength score (0-1)."""
        if sma_50 == 0:
            return 0.0
        
        # Trend is positive when 20-day SMA > 50-day SMA
        trend_ratio = sma_20 / sma_50
        if trend_ratio > 1.0:
            # Strong uptrend
            return min(1.0, (trend_ratio - 1.0) * 5 + 0.5)
        else:
            # Weak or downtrend
            return max(0.0, trend_ratio - 0.8) * 2.5

    def _calculate_momentum_score(self, rsi: float, macd: float, macd_signal: float) -> float:
        """Calculate momentum strength score (0-1)."""
        # RSI momentum (30-70 range is good)
        rsi_score = 0.0
        if 30 <= rsi <= 70:
            rsi_score = 1.0 - abs(rsi - 50) / 20
        elif rsi > 70:
            rsi_score = max(0.0, 1.0 - (rsi - 70) / 30)
        else:  # rsi < 30
            rsi_score = max(0.0, 1.0 - (30 - rsi) / 30)
        
        # MACD momentum
        macd_score = 0.0
        if macd > macd_signal:
            macd_score = min(1.0, (macd - macd_signal) / abs(macd_signal) if macd_signal != 0 else 0.5)
        else:
            macd_score = 0.0
        
        # Combine scores
        return (rsi_score + macd_score) / 2

    def _calculate_volume_score(self, current_volume: float, avg_volume: float) -> float:
        """Calculate volume strength score."""
        if avg_volume == 0:
            return 1.0
        
        volume_ratio = current_volume / avg_volume
        # Volume > 1.2x average is considered strong
        if volume_ratio >= 1.2:
            return min(2.0, volume_ratio)
        else:
            return max(0.0, volume_ratio)

    @DataParams({
        "sma_20": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.ONE_DAY, "period": 20, "count": 1},
        "rsi": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.ONE_DAY, "period": 14, "count": 1},
        "current_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_DAY, "count": 1}
    })
    def evaluateCloseTradeCondition(self, openPos: OpenPosition, data: Dict[str, Any]) -> TradeOrder | None:
        """Evaluate if a position should be closed based on weakening momentum."""
        sma_20 = data["sma_20"]
        rsi = data["rsi"]
        current_bar = data["current_bar"]
        
        if not all([sma_20, rsi, current_bar]):
            return None
        
        current_sma_20 = sma_20[0].value if isinstance(sma_20, list) else sma_20.value
        current_rsi = rsi[0].value if isinstance(rsi, list) else rsi.value
        current_price = current_bar[0].close if isinstance(current_bar, list) else current_bar.close
        
        # Exit conditions for sector rotation
        if openPos.position == PositionType.LONG:
            # Exit if trend weakens or momentum fades
            if (current_price < current_sma_20 * 0.95 or  # Price below 20-day SMA
                current_rsi > 80 or  # Overbought
                current_rsi < 25):   # Oversold
                
                self.state["current_sector_count"] = max(0, self.state["current_sector_count"] - 1)
                return TradeOrder(openPos.security, TradeType.SELL)
        
        return None

    def getStandardCloseCondition(self) -> StandardCloseCriteria | None:
        """Set standard exit criteria for sector rotation."""
        return StandardCloseCriteria(
            targetProfit=0.15,      # 15% profit target
            stopLoss=0.08,          # 8% stop loss
            trailingStop=0.05,      # 5% trailing stop
            timeOut=TimeDelta(14, TimeUnit.DAYS)  # 2 week timeout
        )

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """Process trade signals with sector rotation logic."""
        # Limit to top 3-5 sector positions for diversification
        max_sectors = 5
        
        # Sort by signal strength and limit positions
        sorted_signals = sorted(tradeSignals, key=lambda x: x.strength, reverse=True)
        limited_signals = sorted_signals[:max_sectors]
        
        # Use portfolio allocator
        portfolioAllocator = PercentBasedPortfolioAllocator(max_sectors)
        return portfolioAllocator.allocatePortfolio(portfolio, limited_signals)
