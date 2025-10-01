"""
Bollinger Bands Mean Reversion Strategy

This strategy implements a mean reversion approach using Bollinger Bands.
It generates buy signals when prices touch or fall below the lower Bollinger Band,
and sell signals when prices touch or rise above the upper Bollinger Band.

Strategy Logic:
- Buy when price touches lower Bollinger Band (oversold condition)
- Sell when price touches upper Bollinger Band (overbought condition)
- Uses 20-period SMA with 2 standard deviations
- Includes volume confirmation for signal strength
- Implements risk management with stop losses and profit targets

This is a contrarian strategy that assumes prices will revert to the mean
after reaching extreme levels.
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math
import statistics


class BollingerBandsMeanReversion(TradingStrategy):
    """
    A mean reversion strategy using Bollinger Bands for stock trading.
    
    This strategy:
    1. Identifies oversold conditions when price touches lower Bollinger Band
    2. Identifies overbought conditions when price touches upper Bollinger Band
    3. Uses volume confirmation to validate signals
    4. Implements standard risk management criteria
    """

    def __init__(self) -> None:
        super().__init__()
        # Track the number of consecutive signals to avoid overtrading
        self.state["last_signal_date"] = 0
        self.state["consecutive_signals"] = 0

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """
        Select large-cap stocks with good liquidity for mean reversion trading.
        """
        # Use S&P 100 stocks as they have good liquidity and mean reversion tendencies
        return SecurityUniverseSelector.fromStandardList(StandardSymbolsList.SP_100)

    @DataParams({
        "bb_upper": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.UPPERBBAND, "barinterval": BarInterval.ONE_DAY, "period": 20, "count": 2},
        "bb_lower": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.LOWERBBAND, "barinterval": BarInterval.ONE_DAY, "period": 20, "count": 2},
        "bb_middle": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.ONE_DAY, "period": 20, "count": 2},
        "current_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_DAY, "count": 1},
        "volume_sma": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.ONE_DAY, "period": 20, "count": 1}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """
        Evaluate mean reversion conditions using Bollinger Bands.
        """
        bb_upper = data["bb_upper"]
        bb_lower = data["bb_lower"]
        bb_middle = data["bb_middle"]
        current_bar = data["current_bar"][-1]
        volume_sma = data["volume_sma"]
        
        current_price = current_bar.close
        current_volume = current_bar.volume
        
        # Get current and previous Bollinger Band values
        upper_band = bb_upper[-1].value
        lower_band = bb_lower[-1].value
        middle_band = bb_middle[-1].value
        
        # Calculate signal strength based on how far price is from the mean
        price_to_mean_distance = abs(current_price - middle_band) / middle_band if middle_band != 0 else 0
        
        # Volume confirmation - higher volume strengthens the signal
        volume_ratio = current_volume / volume_sma.value if volume_sma.value > 0 else 1
        
        # Buy signal: Price touches or falls below lower Bollinger Band
        if current_price <= lower_band:
            # Calculate signal strength based on distance from mean and volume
            signal_strength = (price_to_mean_distance * 100) * volume_ratio
            
            # Additional strength if price is significantly below the band
            if current_price < lower_band * 0.995:  # 0.5% below the band
                signal_strength *= 1.5
                
            return TradeSignal(security, PositionType.LONG, int(signal_strength))
        
        # Sell signal: Price touches or rises above upper Bollinger Band
        elif current_price >= upper_band:
            # Calculate signal strength based on distance from mean and volume
            signal_strength = (price_to_mean_distance * 100) * volume_ratio
            
            # Additional strength if price is significantly above the band
            if current_price > upper_band * 1.005:  # 0.5% above the band
                signal_strength *= 1.5
                
            return TradeSignal(security, PositionType.SHORT, int(signal_strength))
        
        return None

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """
        Process trade signals with portfolio allocation.
        """
        # Sort signals by strength and take top 5 to avoid over-diversification
        sorted_signals = sorted(tradeSignals, key=lambda x: x.strength if x.strength is not None else 0, reverse=True)
        top_signals = sorted_signals[:5]
        
        # Use portfolio allocator to distribute capital
        portfolioAllocator = PercentBasedPortfolioAllocator(20)  # 20% per position
        return portfolioAllocator.allocatePortfolio(portfolio, top_signals)

    def getStandardCloseCondition(self) -> StandardCloseCriteria | None:
        """
        Set standard exit criteria for mean reversion trades.
        """
        return StandardCloseCriteria(
            targetProfit=3,                      # Take profit at 3% gain
            stopLoss=-2,                         # Stop loss at 2% loss
            trailingStop=-1,                     # Trailing stop at 1% from peak
            timeOut=TimeDelta(2, TimeUnit.DAYS)  # Exit after 2 days
        )

    @DataParams({
        "bb_middle": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.ONE_DAY, "period": 20, "count": 1},
        "current_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_DAY, "count": 1}
    })
    def evaluateCloseTradeCondition(self, openPos: OpenPosition, data: Dict[str, Any]) -> TradeOrder | None:
        """
        Custom exit condition: Close when price returns to the middle band (mean).
        """
        bb_middle = data["bb_middle"]
        current_bar = data["current_bar"][-1]
        
        middle_band = bb_middle.value
        current_price = current_bar.close
        
        # Close long position when price returns to or above the middle band
        if openPos.position == PositionType.LONG and current_price >= middle_band:
            return TradeOrder(openPos.security, TradeType.SELL)
        
        # Close short position when price returns to or below the middle band
        elif openPos.position == PositionType.SHORT and current_price <= middle_band:
            return TradeOrder(openPos.security, TradeType.BUY)
        
        return None
