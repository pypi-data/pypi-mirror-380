"""
Crypto Momentum Strategy

This strategy is specifically designed for cryptocurrency trading, using
momentum indicators and volatility analysis to capitalize on crypto's
high volatility and trending characteristics.

Strategy Logic:
- Buy when multiple timeframes show bullish momentum
- Sell when momentum shifts to bearish across timeframes
- Uses RSI, MACD, and volatility indicators
- Includes volume confirmation for signal validation
- Implements volatility-adjusted position sizing

This is a momentum strategy optimized for cryptocurrency markets
that exhibit high volatility and strong trending behavior.
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math


class CryptoMomentumStrategy(TradingStrategy):
    """
    A momentum strategy specifically designed for cryptocurrency trading.
    
    This strategy:
    1. Analyzes multiple timeframes for momentum confirmation
    2. Uses volatility indicators for position sizing
    3. Combines RSI and MACD for signal generation
    4. Includes volume confirmation for crypto markets
    5. Implements volatility-adjusted risk management
    """

    def __init__(self) -> None:
        super().__init__()
        # Track crypto-specific state
        self.state["momentum_trend"] = 0  # 0=neutral, 1=bullish, -1=bearish
        self.state["volatility_regime"] = 0  # 0=normal, 1=high, 2=extreme
        self.state["last_signal_time"] = 0

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """
        Select major cryptocurrencies for momentum trading.
        """
        # Use USD crypto pairs as they have good liquidity and momentum
        return SecurityUniverseSelector.fromStandardList(StandardSymbolsList.USD_CRYPTO)

    @DataParams({
        "rsi_1min": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.ONE_MINUTE, "period": 14, "count": 3},
        "rsi_5min": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.FIVE_MINUTE, "period": 14, "count": 3},
        "macd_1min": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.MACD, "barinterval": BarInterval.ONE_MINUTE, "period": 12, "count": 3},
        "macd_signal_1min": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.MACDS, "barinterval": BarInterval.ONE_MINUTE, "period": 12, "count": 3},
        "atr_1min": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.ATR, "barinterval": BarInterval.ONE_MINUTE, "period": 14, "count": 1},
        "current_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_MINUTE, "count": 1},
        "volume_sma": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.ONE_MINUTE, "period": 20, "count": 1}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """
        Evaluate crypto momentum conditions across multiple timeframes.
        """
        rsi_1min = data["rsi_1min"]
        rsi_5min = data["rsi_5min"]
        macd_1min = data["macd_1min"]
        macd_signal_1min = data["macd_signal_1min"]
        atr_1min = data["atr_1min"]
        current_bar = data["current_bar"][-1]
        volume_sma = data["volume_sma"]
        
        # Need at least 3 data points for momentum analysis
        if (len(rsi_1min) < 3 or len(rsi_5min) < 3 or 
            len(macd_1min) < 3 or len(macd_signal_1min) < 3):
            return None
        
        # Extract current and previous values
        current_rsi_1min = rsi_1min[-1].value
        prev_rsi_1min = rsi_1min[-2].value
        current_rsi_5min = rsi_5min[-1].value
        prev_rsi_5min = rsi_5min[-2].value
        
        current_macd = macd_1min[-1].value
        prev_macd = macd_1min[-2].value
        current_macd_signal = macd_signal_1min[-1].value
        prev_macd_signal = macd_signal_1min[-2].value
        
        current_atr = atr_1min.value
        current_price = current_bar.close
        current_volume = current_bar.volume
        avg_volume = volume_sma.value
        
        # Calculate volatility regime
        volatility_ratio = current_atr / current_price if current_price != 0 else 0
        if volatility_ratio > 0.05:  # 5% ATR
            self.state["volatility_regime"] = 2  # extreme
        elif volatility_ratio > 0.03:  # 3% ATR
            self.state["volatility_regime"] = 1  # high
        else:
            self.state["volatility_regime"] = 0  # normal
        
        # Volume confirmation
        volume_ratio = current_volume / avg_volume if avg_volume > 0 else 1
        
        # Calculate momentum scores
        rsi_momentum_1min = current_rsi_1min - prev_rsi_1min
        rsi_momentum_5min = current_rsi_5min - prev_rsi_5min
        
        macd_histogram = current_macd - current_macd_signal
        prev_macd_histogram = prev_macd - prev_macd_signal
        macd_momentum = macd_histogram - prev_macd_histogram
        
        # Buy signal: Multiple timeframe bullish momentum
        if (rsi_momentum_1min > 5 and rsi_momentum_5min > 3 and  # RSI momentum
            macd_momentum > 0 and current_macd > current_macd_signal and  # MACD momentum
            volume_ratio > 1.3):  # Volume confirmation
            
            # Calculate signal strength based on momentum and volatility
            rsi_strength = min(abs(rsi_momentum_1min) * 10, 100)
            macd_strength = min(abs(macd_momentum) * 50, 100)
            volume_strength = min(volume_ratio * 20, 100)
            
            # Adjust for volatility regime
            volatility_multiplier = 1.0
            if self.state["volatility_regime"] == 1:  # high volatility
                volatility_multiplier = 1.2
            elif self.state["volatility_regime"] == 2:  # extreme volatility
                volatility_multiplier = 1.5
            
            signal_strength = int(((rsi_strength + macd_strength + volume_strength) / 3) * volatility_multiplier)
            signal_strength = min(signal_strength, 100)
            
            # Update state
            self.state["momentum_trend"] = 1
            self.state["last_signal_time"] = len(rsi_1min)
            
            return TradeSignal(security, PositionType.LONG, signal_strength)
        
        # Sell signal: Multiple timeframe bearish momentum
        elif (rsi_momentum_1min < -5 and rsi_momentum_5min < -3 and  # RSI momentum
              macd_momentum < 0 and current_macd < current_macd_signal and  # MACD momentum
              volume_ratio > 1.3):  # Volume confirmation
            
            # Calculate signal strength based on momentum and volatility
            rsi_strength = min(abs(rsi_momentum_1min) * 10, 100)
            macd_strength = min(abs(macd_momentum) * 50, 100)
            volume_strength = min(volume_ratio * 20, 100)
            
            # Adjust for volatility regime
            volatility_multiplier = 1.0
            if self.state["volatility_regime"] == 1:  # high volatility
                volatility_multiplier = 1.2
            elif self.state["volatility_regime"] == 2:  # extreme volatility
                volatility_multiplier = 1.5
            
            signal_strength = int(((rsi_strength + macd_strength + volume_strength) / 3) * volatility_multiplier)
            signal_strength = min(signal_strength, 100)
            
            # Update state
            self.state["momentum_trend"] = -1
            self.state["last_signal_time"] = len(rsi_1min)
            
            return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        # Additional signal: Extreme RSI levels with volume
        elif volume_ratio > 2.0:  # High volume spike
            
            if current_rsi_1min < 20 and current_rsi_5min < 25:  # Oversold condition
                signal_strength = int(min((30 - current_rsi_1min) * 5, 100))
                return TradeSignal(security, PositionType.LONG, signal_strength)
                
            elif current_rsi_1min > 80 and current_rsi_5min > 75:  # Overbought condition
                signal_strength = int(min((current_rsi_1min - 70) * 5, 100))
                return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        return None

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """
        Process trade signals with crypto-optimized allocation.
        """
        # Sort signals by strength and take top 4 for crypto diversification
        sorted_signals = sorted(tradeSignals, key=lambda x: x.strength if x.strength is not None else 0, reverse=True)
        top_signals = sorted_signals[:4]
        
        # Use portfolio allocator for crypto strategy
        portfolioAllocator = PercentBasedPortfolioAllocator(25)  # 25% per position
        return portfolioAllocator.allocatePortfolio(portfolio, top_signals)

    def getStandardCloseCondition(self) -> StandardCloseCriteria | None:
        """
        Set standard exit criteria for crypto trades with volatility adjustment.
        """
        # Adjust exit criteria based on volatility regime
        if self.state["volatility_regime"] == 2:  # extreme volatility
            return StandardCloseCriteria(
                targetProfit=12,                     # Higher profit target for extreme volatility
                stopLoss=-6,                         # Wider stop loss for extreme volatility
                trailingStop=-3,                     # Wider trailing stop
                timeOut=TimeDelta(2, TimeUnit.DAYS)  # Shorter holding period
            )
        elif self.state["volatility_regime"] == 1:  # high volatility
            return StandardCloseCriteria(
                targetProfit=8,                      # Higher profit target for high volatility
                stopLoss=-4,                         # Wider stop loss for high volatility
                trailingStop=-2,                     # Wider trailing stop
                timeOut=TimeDelta(3, TimeUnit.DAYS)  # Shorter holding period
            )
        else:  # normal volatility
            return StandardCloseCriteria(
                targetProfit=6,                      # Standard profit target
                stopLoss=-3,                         # Standard stop loss
                trailingStop=-1.5,                   # Standard trailing stop
                timeOut=TimeDelta(5, TimeUnit.DAYS)  # Standard holding period
            )

    @DataParams({
        "rsi_1min": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.ONE_MINUTE, "period": 14, "count": 1},
        "macd_1min": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.MACD, "barinterval": BarInterval.ONE_MINUTE, "period": 12, "count": 1},
        "macd_signal_1min": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.MACDS, "barinterval": BarInterval.ONE_MINUTE, "period": 12, "count": 1}
    })
    def evaluateCloseTradeCondition(self, openPos: OpenPosition, data: Dict[str, Any]) -> TradeOrder | None:
        """
        Custom exit condition: Close based on momentum reversal.
        """
        rsi_1min = data["rsi_1min"]
        macd_1min = data["macd_1min"]
        macd_signal_1min = data["macd_signal_1min"]
        
        current_rsi = rsi_1min.value
        current_macd = macd_1min.value
        current_macd_signal = macd_signal_1min.value
        
        macd_histogram = current_macd - current_macd_signal
        
        # Close long position if momentum turns bearish
        if openPos.position == PositionType.LONG:
            if current_rsi > 70 or macd_histogram < 0:  # Overbought or MACD bearish
                return TradeOrder(openPos.security, TradeType.SELL)
        
        # Close short position if momentum turns bullish
        elif openPos.position == PositionType.SHORT:
            if current_rsi < 30 or macd_histogram > 0:  # Oversold or MACD bullish
                return TradeOrder(openPos.security, TradeType.BUY)
        
        return None
