from typing import Dict, Any, List

from investfly.models import *
from investfly.utils import PercentBasedPortfolioAllocator


class MacdTrendFollowingStrategy(TradingStrategy):
    """
    A trend following strategy based on the MACD (Moving Average Convergence Divergence) indicator.
    
    This strategy:
    1. Uses the MACD indicator to identify trend momentum
    2. Generates buy signals when the MACD line crosses above the signal line (bullish momentum)
    3. Includes risk management with target profit, stop loss, and time-based exit criteria
    4. Allocates portfolio to the top 5 stocks showing the strongest signals
    
    Note: This strategy operates on daily bars, so evaluateOpenTradeCondition is called
    at most once per day when a new daily bar is available.
    """

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """
        Select the universe of securities to trade.
        This strategy uses the S&P 100 stocks.
        """
        return SecurityUniverseSelector.fromStandardList(StandardSymbolsList.SP_100)

    @DataParams({
        # MACD is typically calculated with 12, 26, and 9 as the standard parameters
        # We request the MACD line and the signal line (MACDS)
        "macd": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.MACD, "barinterval": BarInterval.ONE_DAY, "count": 2},
        "macds": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.MACDS, "barinterval": BarInterval.ONE_DAY, "count": 2},
        # Request the latest daily bar to get the closing price for signal strength calculation
        "daily_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_DAY, "count": 1}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """
        Generate a buy signal when the MACD line crosses above the signal line,
        indicating increasing bullish momentum.
        
        The signal strength is calculated based on the magnitude of the difference
        between MACD and signal line relative to the stock's closing price from the latest daily bar.
        
        This method is called at most once per day when a new daily bar is available.
        """
        macd = data["macd"]
        macds = data["macds"]
        daily_bar = data["daily_bar"][-1]  # Get the latest daily bar
        
        # Check for MACD line crossing above the signal line (bullish crossover)
        if macd[-1].value > macds[-1].value and macd[-2].value <= macds[-2].value:
            # Get the closing price from the latest daily bar
            closing_price = daily_bar.close
            
            # Calculate signal strength as a percentage of the difference relative to price
            # This helps prioritize stronger signals when allocating portfolio
            macd_diff = abs(macd[-1].value - macds[-1].value)
            
            # Calculate signal strength based on:
            # 1. The magnitude of the MACD crossover (larger difference = stronger signal)
            # 2. The relative size of the difference compared to the stock price
            signal_strength = (macd_diff / closing_price) * 100
            
            # Add a component based on the rate of change of MACD to further strengthen the signal
            macd_change_rate = abs(macd[-1].value - macd[-2].value) / abs(macd[-2].value) if macd[-2].value != 0 else 0
            signal_strength = signal_strength * (1 + macd_change_rate)
            
            # Return a long position signal with the calculated strength
            return TradeSignal(security, PositionType.LONG, signal_strength)
        
        return None

    def getStandardCloseCondition(self) -> StandardCloseCriteria:
        """
        Define standard exit criteria for positions:
        - Take profit at 5% gain
        - Stop loss at 3% loss
        - Time-based exit after 10 trading days (to prevent holding positions too long)
        """
        return StandardCloseCriteria(
            targetProfit=5,           # Take profit at 5% gain
            stopLoss=-3,              # Stop loss at 3% loss
            trailingStop=None,        # No trailing stop for this strategy
            timeOut=TimeDelta(10, TimeUnit.DAYS)  # Exit after 10 trading days
        )

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """
        Process the trade signals and allocate the portfolio.
        This strategy allocates to the top 5 stocks with the strongest signals.
        """
        # Sort trade signals by strength in descending order
        sorted_signals = sorted(tradeSignals, key=lambda signal: signal.strength if signal.strength is not None else 0, reverse=True)
        
        # Use the PercentBasedPortfolioAllocator to allocate the portfolio
        # Allocate to the top 5 stocks with equal weight (20% each)
        portfolioAllocator = PercentBasedPortfolioAllocator(5)
        return portfolioAllocator.allocatePortfolio(portfolio, sorted_signals) 