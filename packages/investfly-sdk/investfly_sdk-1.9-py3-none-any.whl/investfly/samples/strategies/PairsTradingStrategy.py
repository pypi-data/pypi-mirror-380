"""
Pairs Trading Strategy

This strategy implements statistical arbitrage by identifying pairs of
correlated securities and trading them when they diverge from their
historical relationship. It capitalizes on mean reversion in spreads.

Strategy Logic:
- Identify highly correlated security pairs
- Calculate spread between pair prices
- Buy the underperformer, sell the outperformer when spread widens
- Close positions when spread reverts to mean
- Uses correlation analysis and z-score for signal generation

This is a market-neutral strategy that profits from temporary
disequilibria in correlated securities.
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math


class PairsTradingStrategy(TradingStrategy):
    """
    A statistical arbitrage strategy using pairs trading.
    
    This strategy:
    1. Identifies highly correlated security pairs
    2. Calculates spread and z-score for signal generation
    3. Implements mean reversion trading logic
    4. Uses correlation analysis for pair selection
    5. Implements market-neutral position sizing
    """

    def __init__(self) -> None:
        super().__init__()
        # Track pairs trading state
        self.state["active_pairs"] = 0  # Track active pair trades count
        self.state["correlation_cache"] = 0  # Cache correlation calculations count
        self.state["last_pairs_signal"] = 0
        
        # Define correlated security pairs (in real implementation, these would be dynamic)
        # Format: {pair_id: {"security1": symbol1, "security2": symbol2, "correlation": corr}}
        self.correlated_pairs = {
            "tech_pair_1": {"security1": "AAPL", "security2": "MSFT", "correlation": 0.85},
            "tech_pair_2": {"security1": "GOOGL", "security2": "META", "correlation": 0.82},
            "bank_pair_1": {"security1": "JPM", "security2": "BAC", "correlation": 0.78},
            "energy_pair_1": {"security1": "XOM", "security2": "CVX", "correlation": 0.91},
            "retail_pair_1": {"security1": "WMT", "security2": "TGT", "correlation": 0.76}
        }

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """
        Select stocks that are part of correlated pairs.
        """
        # Create custom list from correlated pairs
        all_symbols: List[str] = []
        for pair_info in self.correlated_pairs.values():
            all_symbols.extend([str(pair_info["security1"]), str(pair_info["security2"])])
        
        # Remove duplicates
        unique_symbols: List[str] = list(set(all_symbols))
        
        # Use custom security list for pairs trading
        return SecurityUniverseSelector.fromSymbols(SecurityType.STOCK, unique_symbols)

    @DataParams({
        "price_bars": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_MINUTE, "count": 60},
        "volume_sma": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.ONE_MINUTE, "period": 20, "count": 1}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """
        Evaluate pairs trading conditions for trade signals.
        """
        price_bars = data["price_bars"]
        volume_sma = data["volume_sma"]
        
        # Need at least 60 bars for correlation analysis
        if len(price_bars) < 60:
            return None
        
        # Find which pair this security belongs to
        pair_info = self._find_security_pair(security.symbol)
        if not pair_info:
            return None
        
        # Get the other security in the pair
        other_symbol = pair_info["other_security"]
        pair_id = pair_info["pair_id"]
        
        # Calculate current prices and spread
        current_price = price_bars[-1].close
        other_price = self._get_other_security_price(other_symbol)  # In real implementation, this would be fetched
        
        if other_price is None:
            return None
        
        # Calculate spread and z-score
        spread = current_price - other_price
        spread_history = self._calculate_spread_history(price_bars, other_symbol)
        
        if len(spread_history) < 30:
            return None
        
        spread_mean = sum(spread_history) / len(spread_history)
        spread_std = math.sqrt(sum((x - spread_mean) ** 2 for x in spread_history) / len(spread_history))
        
        if spread_std == 0:
            return None
        
        z_score = (spread - spread_mean) / spread_std
        
        # Volume confirmation
        current_volume = price_bars[-1].volume
        avg_volume = volume_sma.value
        volume_ratio = current_volume / avg_volume if avg_volume > 0 else 1
        
        # Buy signal: Security is underperforming (negative z-score)
        if (z_score < -2.0 and  # Significant underperformance
            volume_ratio > 1.2 and  # Volume confirmation
            pair_info["correlation"] > 0.7):  # High correlation
            
            # Calculate signal strength based on z-score and correlation
            z_score_strength = min(abs(z_score) * 20, 100)
            correlation_strength = min(pair_info["correlation"] * 100, 100)
            volume_strength = min(volume_ratio * 20, 100)
            
            signal_strength = int((z_score_strength + correlation_strength + volume_strength) / 3)
            
            # Update state
            self.state["active_pairs"] += 1
            self.state["last_pairs_signal"] = len(price_bars)
            
            return TradeSignal(security, PositionType.LONG, signal_strength)
        
        # Sell signal: Security is outperforming (positive z-score)
        elif (z_score > 2.0 and  # Significant outperformance
              volume_ratio > 1.2 and  # Volume confirmation
              pair_info["correlation"] > 0.7):  # High correlation
            
            # Calculate signal strength based on z-score and correlation
            z_score_strength = min(abs(z_score) * 20, 100)
            correlation_strength = min(pair_info["correlation"] * 100, 100)
            volume_strength = min(volume_ratio * 20, 100)
            
            signal_strength = int((z_score_strength + correlation_strength + volume_strength) / 3)
            
            # Update state
            self.state["active_pairs"] += 1
            self.state["last_pairs_signal"] = len(price_bars)
            
            return TradeSignal(security, PositionType.SHORT, signal_strength)
        
        return None

    def _find_security_pair(self, symbol: str) -> Dict[str, Any] | None:
        """Find which pair a security belongs to."""
        for pair_id, pair_info in self.correlated_pairs.items():
            if pair_info["security1"] == symbol:
                return {
                    "pair_id": pair_id,
                    "other_security": pair_info["security2"],
                    "correlation": pair_info["correlation"]
                }
            elif pair_info["security2"] == symbol:
                return {
                    "pair_id": pair_id,
                    "other_security": pair_info["security1"],
                    "correlation": pair_info["correlation"]
                }
        return None

    def _get_other_security_price(self, symbol: str) -> float | None:
        """Get the current price of the other security in the pair."""
        # In real implementation, this would fetch the current price
        # For this example, we'll return a placeholder
        return 100.0  # Placeholder price

    def _calculate_spread_history(self, price_bars: List[Any], other_symbol: str) -> List[float]:
        """Calculate historical spread between the two securities."""
        # In real implementation, this would calculate actual spread history
        # For this example, we'll return a placeholder
        return [0.0] * 30  # Placeholder spread history

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """
        Process trade signals with pairs trading allocation.
        """
        # Sort signals by strength and take top 3 for concentrated pairs
        sorted_signals = sorted(tradeSignals, key=lambda x: x.strength if x.strength is not None else 0, reverse=True)
        top_signals = sorted_signals[:3]
        
        # Use portfolio allocator for pairs trading strategy
        portfolioAllocator = PercentBasedPortfolioAllocator(33)  # 33% per position
        return portfolioAllocator.allocatePortfolio(portfolio, top_signals)

    def getStandardCloseCondition(self) -> StandardCloseCriteria | None:
        """
        Set standard exit criteria for pairs trading.
        """
        return StandardCloseCriteria(
            targetProfit=3,                      # Take profit at 3% gain
            stopLoss=-2,                         # Stop loss at 2% loss
            trailingStop=-1,                     # Trailing stop at 1% from peak
            timeOut=TimeDelta(7, TimeUnit.DAYS)  # Exit after 7 days
        )

    @DataParams({
        "price_bars": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_MINUTE, "count": 30},
        "volume_sma": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.AVGVOL, "barinterval": BarInterval.ONE_MINUTE, "period": 20, "count": 1}
    })
    def evaluateCloseTradeCondition(self, openPos: OpenPosition, data: Dict[str, Any]) -> TradeOrder | None:
        """
        Custom exit condition: Close based on spread reversion to mean.
        """
        price_bars = data["price_bars"]
        
        # Simple exit condition: Close if price moves significantly from entry
        current_price = price_bars[-1].close
        entry_price = openPos.avgPrice
        
        # Close if price has moved 3% from entry (profit or loss)
        price_change = abs(current_price - entry_price) / entry_price if entry_price != 0 else 0
        
        if price_change > 0.03:  # 3% move
            if openPos.position == PositionType.LONG:
                return TradeOrder(openPos.security, TradeType.SELL)
            elif openPos.position == PositionType.SHORT:
                return TradeOrder(openPos.security, TradeType.BUY)
        
        return None
