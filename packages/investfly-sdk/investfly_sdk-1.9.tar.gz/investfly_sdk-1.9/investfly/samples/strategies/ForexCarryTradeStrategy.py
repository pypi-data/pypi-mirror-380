"""
Forex Carry Trade Strategy

This strategy implements a carry trade approach for forex markets, focusing on
interest rate differentials between currency pairs and trend confirmation.
It combines fundamental interest rate analysis with technical trend indicators.

Strategy Logic:
- Buy high-yielding currencies against low-yielding currencies
- Use trend indicators to confirm carry trade direction
- Include volatility filters for risk management
- Implement correlation-based position sizing
- Focus on major currency pairs with stable spreads

This is a fundamental strategy that capitalizes on interest rate differentials
while using technical analysis for entry/exit timing.
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math


class ForexCarryTradeStrategy(TradingStrategy):
    """
    A carry trade strategy for forex markets using interest rate differentials.
    
    This strategy:
    1. Identifies high-yielding vs low-yielding currency pairs
    2. Uses trend indicators for entry confirmation
    3. Implements volatility-based position sizing
    4. Includes correlation analysis for risk management
    5. Focuses on major currency pairs
    """

    def __init__(self) -> None:
        super().__init__()
        # Track forex-specific state
        self.state["carry_trend"] = 0  # 0=neutral, 1=bullish, -1=bearish
        self.state["volatility_regime"] = 0  # 0=low, 1=medium, 2=high
        self.state["last_carry_signal"] = 0
        
        # Define carry trade currency pairs (high yield vs low yield)
        # In real implementation, these would be dynamic based on current rates
        self.carry_pairs = {
            "AUDUSD": {"high_yield": "AUD", "low_yield": "USD", "carry_score": 2.5},
            "NZDUSD": {"high_yield": "NZD", "low_yield": "USD", "carry_score": 3.0},
            "GBPUSD": {"high_yield": "GBP", "low_yield": "USD", "carry_score": 1.5},
            "EURUSD": {"high_yield": "EUR", "low_yield": "USD", "carry_score": 0.5},
            "USDJPY": {"high_yield": "USD", "low_yield": "JPY", "carry_score": 2.0}
        }

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """
        Select major forex pairs for carry trading.
        """
        # Use all forex pairs as they have good liquidity and carry opportunities
        return SecurityUniverseSelector.fromStandardList(StandardSymbolsList.ALL_FOREX)

    @DataParams({
        "sma_20": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.ONE_MINUTE, "period": 20, "count": 3},
        "sma_50": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.ONE_MINUTE, "period": 50, "count": 3},
        "rsi": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.ONE_MINUTE, "period": 14, "count": 1},
        "atr": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.ATR, "barinterval": BarInterval.ONE_MINUTE, "period": 14, "count": 1},
        "current_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_MINUTE, "count": 1}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """
        Evaluate carry trade conditions for forex pairs.
        """
        sma_20 = data["sma_20"]
        sma_50 = data["sma_50"]
        rsi = data["rsi"]
        atr = data["atr"]
        current_bar = data["current_bar"][-1]
        
        # Need at least 3 data points for trend analysis
        if len(sma_20) < 3 or len(sma_50) < 3:
            return None
        
        # Extract current and previous values
        current_sma_20 = sma_20[-1].value
        prev_sma_20 = sma_20[-2].value
        current_sma_50 = sma_50[-1].value
        prev_sma_50 = sma_50[-2].value
        
        current_rsi = rsi.value
        current_atr = atr.value
        current_price = current_bar.close
        
        # Calculate trend strength
        sma_20_slope = current_sma_20 - prev_sma_20
        sma_50_slope = current_sma_50 - prev_sma_50
        
        # Determine volatility regime
        atr_ratio = current_atr / current_price if current_price != 0 else 0
        if atr_ratio > 0.002:  # 0.2% ATR
            self.state["volatility_regime"] = 2  # high
        elif atr_ratio > 0.001:  # 0.1% ATR
            self.state["volatility_regime"] = 1  # medium
        else:
            self.state["volatility_regime"] = 0  # low
        
        # Get carry score for this currency pair
        symbol = security.symbol
        carry_info = self.carry_pairs.get(symbol, {"carry_score": 0})
        carry_score = carry_info["carry_score"]
        
        # Buy signal: Bullish trend + positive carry + oversold RSI
        if (current_sma_20 > current_sma_50 and  # Price above long-term trend
            sma_20_slope > 0 and sma_50_slope > 0 and  # Both SMAs trending up
            current_rsi < 40 and  # Oversold condition
            isinstance(carry_score, (int, float)) and carry_score > 1.0):  # Positive carry
            
            # Calculate signal strength based on trend, carry, and volatility
            trend_strength = min(abs(float(sma_20_slope)) * 1000, 100)
            carry_strength = min(float(carry_score) * 20, 100) if isinstance(carry_score, (int, float)) else 0
            rsi_strength = min((40 - float(current_rsi)) * 2, 100)
            
            # Adjust for volatility regime
            volatility_multiplier = 1.0
            if self.state.get("volatility_regime", 0) == 1:  # medium volatility
                volatility_multiplier = 1.1
            elif self.state.get("volatility_regime", 0) == 2:  # high volatility
                volatility_multiplier = 1.2
            
            signal_strength = int(((trend_strength + carry_strength + rsi_strength) / 3) * volatility_multiplier)
            signal_strength = min(signal_strength, 100)
            
            # Update state
            self.state["carry_trend"] = 1
            self.state["last_carry_signal"] = len(sma_20)
            
            return TradeSignal(security, PositionType.LONG, signal_strength)
        
        # Sell signal: Bearish trend + negative carry + overbought RSI
        elif (current_sma_20 < current_sma_50 and  # Price below long-term trend
              sma_20_slope < 0 and sma_50_slope < 0 and  # Both SMAs trending down
              current_rsi > 60 and  # Overbought condition
              isinstance(carry_score, (int, float)) and carry_score < 0):  # Negative carry
            
            # Calculate signal strength based on trend, carry, and volatility
            trend_strength = min(abs(float(sma_20_slope)) * 1000, 100)
            carry_strength = min(abs(float(carry_score)) * 20, 100) if isinstance(carry_score, (int, float)) else 0
            rsi_strength = min((float(current_rsi) - 60) * 2, 100)
            
            # Adjust for volatility regime
            volatility_multiplier = 1.0
            if self.state.get("volatility_regime", 0) == 1:  # medium volatility
                volatility_multiplier = 1.1
            elif self.state.get("volatility_regime", 0) == 2:  # high volatility
                volatility_multiplier = 1.2
            
            signal_strength = int(((trend_strength + carry_strength + rsi_strength) / 3) * volatility_multiplier)
            signal_strength = min(signal_strength, 100)
            
            # Update state
            self.state["carry_trend"] = -1
            self.state["last_carry_signal"] = len(sma_20)
            
            return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        # Additional signal: Strong trend continuation with carry confirmation
        elif abs(float(sma_20_slope)) > abs(float(sma_50_slope)) * 2:  # Strong trend acceleration
            
            if (float(sma_20_slope) > 0 and isinstance(carry_score, (int, float)) and float(carry_score) > 0.5 and  # Bullish acceleration
                current_price > current_sma_20):  # Price above short-term trend
                signal_strength = int(min(abs(float(sma_20_slope)) * 500, 100))
                return TradeSignal(security, PositionType.LONG, signal_strength)
                
            elif (float(sma_20_slope) < 0 and isinstance(carry_score, (int, float)) and float(carry_score) < 0 and  # Bearish acceleration
                  current_price < current_sma_20):  # Price below short-term trend
                signal_strength = int(min(abs(float(sma_20_slope)) * 500, 100))
                return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        return None

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """
        Process trade signals with forex carry trade allocation.
        """
        # Sort signals by strength and take top 5 for currency diversification
        sorted_signals = sorted(tradeSignals, key=lambda x: x.strength if x.strength is not None else 0, reverse=True)
        top_signals = sorted_signals[:5]
        
        # Use portfolio allocator for forex strategy
        portfolioAllocator = PercentBasedPortfolioAllocator(20)  # 20% per position
        return portfolioAllocator.allocatePortfolio(portfolio, top_signals)

    def getStandardCloseCondition(self) -> StandardCloseCriteria | None:
        """
        Set standard exit criteria for forex carry trades.
        """
        # Adjust exit criteria based on volatility regime
        if self.state.get("volatility_regime", 0) == 2:  # high volatility
            return StandardCloseCriteria(
                targetProfit=3,                      # Lower profit target for high volatility
                stopLoss=-2,                         # Tighter stop loss for high volatility
                trailingStop=-1,                     # Tighter trailing stop
                timeOut=TimeDelta(7, TimeUnit.DAYS)  # Longer holding period for carry
            )
        elif self.state.get("volatility_regime", 0) == 1:  # medium volatility
            return StandardCloseCriteria(
                targetProfit=4,                      # Medium profit target
                stopLoss=-2.5,                       # Medium stop loss
                trailingStop=-1.5,                   # Medium trailing stop
                timeOut=TimeDelta(10, TimeUnit.DAYS) # Longer holding period for carry
            )
        else:  # low volatility
            return StandardCloseCriteria(
                targetProfit=5,                      # Higher profit target for low volatility
                stopLoss=-3,                         # Wider stop loss for low volatility
                trailingStop=-2,                     # Wider trailing stop
                timeOut=TimeDelta(14, TimeUnit.DAYS) # Longer holding period for carry
            )

    @DataParams({
        "sma_20": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.ONE_MINUTE, "period": 20, "count": 1},
        "sma_50": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.ONE_MINUTE, "period": 50, "count": 1},
        "rsi": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.ONE_MINUTE, "period": 14, "count": 1}
    })
    def evaluateCloseTradeCondition(self, openPos: OpenPosition, data: Dict[str, Any]) -> TradeOrder | None:
        """
        Custom exit condition: Close based on trend reversal or carry deterioration.
        """
        sma_20 = data["sma_20"]
        sma_50 = data["sma_50"]
        rsi = data["rsi"]
        
        current_sma_20 = sma_20.value
        current_sma_50 = sma_50.value
        current_rsi = rsi.value
        
        # Close long position if trend turns bearish
        if openPos.position == PositionType.LONG:
            if current_sma_20 < current_sma_50 or current_rsi > 70:  # Below trend or overbought
                return TradeOrder(openPos.security, TradeType.SELL)
        
        # Close short position if trend turns bullish
        elif openPos.position == PositionType.SHORT:
            if current_sma_20 > current_sma_50 or current_rsi < 30:  # Above trend or oversold
                return TradeOrder(openPos.security, TradeType.BUY)
        
        return None
