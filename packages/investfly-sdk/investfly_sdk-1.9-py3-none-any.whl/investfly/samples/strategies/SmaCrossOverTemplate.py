# This is a self-documenting starter template to define custom trading strategy in Python Programming Language
# This code can be used as-it-is to try a new strategy

"""
SmaCrossOverTemplate - A comprehensive template for creating trading strategies with Investfly

This template demonstrates how to implement a complete trading strategy using the Investfly SDK.
It shows a moving average crossover strategy that generates buy signals when a shorter-period SMA
crosses above a longer-period EMA, indicating potential upward momentum.

Key components demonstrated:
1. Security universe selection (how to choose which stocks to trade)
2. Data request specification (how to request indicator data, bars, etc.)
3. Trade signal generation (when to enter trades)
4. Portfolio allocation (how to allocate capital across multiple signals)
5. Exit criteria (when to exit trades)
6. State management (how to track state between executions)

Important note on evaluation frequency:
- Strategies using DataType.QUOTE are evaluated on every price quote (multiple times per second)
- Strategies using DataType.BARS are evaluated when a new bar is available (based on barinterval)
- For day trading, prefer using ONE_MINUTE bars instead of quotes to reduce computational load

This template is designed to be educational and can be used as a starting point for
developing your own custom trading strategies.
"""

# Following two imports are required
from investfly.models import *
from investfly.utils import *

# Import basic types, they aren't required but recommended
from typing import Any, List, Dict

# Following numeric analysis imports are allowed
import math
import statistics
import numpy as np

# https://pypi.org/project/TA-Lib/
import talib  # type: ignore
import pandas
# ! WARN ! Imports other than listed above are disallowed and won't pass validation

# Create a class that extends TradingStrategy and implement 5 methods shown below
class SmaCrossOverTemplate(TradingStrategy):
    """
    A template strategy demonstrating a moving average crossover system.
    
    This strategy:
    1. Uses a combination of SMA and EMA indicators with different periods
    2. Generates buy signals when the shorter SMA crosses above the longer EMA
    3. Includes risk management with profit targets and stop losses
    4. Demonstrates how to implement custom exit conditions
    
    Moving average crossovers are one of the most basic and widely used technical analysis techniques
    for identifying trend changes. When a shorter-period moving average crosses above a longer-period
    moving average, it often indicates the beginning of an uptrend.
    
    Note: This strategy operates on one-minute bars, so evaluateOpenTradeCondition is called
    at most once per minute when a new one-minute bar is available.
    """

    def __init__(self) -> None:
        """
        Initialize the strategy.
        
        This method is called when the strategy is first created. You can use it to:
        - Initialize any state variables you want to track between executions
        - Set up any configuration parameters for the strategy
        
        The state dictionary is automatically persisted between strategy runs.
        """
        super().__init__()
        # Initialize state dictionary if needed
        # self.state = {"my_custom_state": {}}

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """
        Define the universe of securities to trade.
        
        This method narrows down the set of securities against which to run the strategy logic.
        There are three main approaches to selecting securities:
        1. Standard lists (e.g., S&P 100, NASDAQ 100)
        2. Custom lists (specific symbols you want to trade)
        3. Financial queries (dynamic lists based on fundamental metrics)
        
        Returns:
            SecurityUniverseSelector: A selector configured with your chosen securities
        """
        # Narrow down the scope (or universe of stocks) against which to run this strategy. We support 3 options
        
        # OPTION 1: Standard List: SP_100, SP_500, NASDAQ_100, NASDAQ_COMPOSITE, RUSSELL_1000, DOW_JONES_INDUSTRIALS, ETFS
        # universe = SecurityUniverseSelector.fromStandardList(StandardSymbolsList.SP_100)
        
        # OPTION 2: Custom List - specify exactly which symbols you want to trade
        # universe = SecurityUniverseSelector.fromStockSymbols(['AAPL', 'MSFT'])
        
        # OPTION 3: Financial Query (Dynamic List) - select stocks based on fundamental metrics
        # This example selects stocks with market cap > $1B and P/E ratio > 20
        financialQuery = FinancialQuery()
        financialQuery.addCondition(FinancialCondition(FinancialField.MARKET_CAP, ComparisonOperator.GREATER_THAN, "1B"))
        financialQuery.addCondition(FinancialCondition(FinancialField.PRICE_TO_EARNINGS_RATIO, ComparisonOperator.GREATER_THAN, "20"))
        universe = SecurityUniverseSelector.fromFinancialQuery(financialQuery)
        return universe


    """
    The function evaluateOpenTradeCondition below must be annotated with DataParams to indicate what data is needed.
    This function is called separately for each security whenever new data is available based on the requested data types.
    
    IMPORTANT: The types of data you request determine how frequently this function is called:
    - DataType.BARS: Called when a new bar is available (frequency depends on barinterval)
    - DataType.INDICATOR: Called based on the underlying data the indicator uses
    - DataType.FINANCIAL: Called when new financial data is available (typically infrequent)
    
    AVOID using DataType.QUOTE in day trading strategies as it causes the function to be called
    multiple times per second, which is computationally expensive.
    
    The DataParams annotation specifies what data you need for your strategy. For example:
    
    @DataParams({
        "sma2":             {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.ONE_MINUTE,  "period": 2, "count": 2},
        "sma3":             {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.ONE_MINUTE, "period": 3, "count": 2},
        "allOneMinBars":    {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_MINUTE},
        "latestDailyBar":   {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_DAY, "count":1},
        "revenue":          {"datatype": DataType.FINANCIAL, "field": FinancialField.REVENUE}
    })
    
    The keys in the dictionary become the keys in the 'data' parameter passed to the function.
    """
    @DataParams({
        # Request 2-period SMA data for the last 2 data points to detect crossover
        "sma5": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.ONE_MINUTE, "period": 2, "count": 2},
        # Request 14-period EMA data for the last 2 data points to detect crossover
        "ema14": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.EMA, "barinterval": BarInterval.ONE_MINUTE, "period": 14, "count": 2},
        # Request the latest one-minute bar to get price and volume data for signal strength calculation
        "minute_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_MINUTE, "count": 1}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """
        Evaluate whether to open a trade for a given security.
        
        This method is called for each security in the universe whenever a new one-minute bar is available.
        It analyzes the requested data to determine if a trade signal should be generated.
        
        Args:
            security: The security (stock) being evaluated
            data: Dictionary containing the requested data based on @DataParams annotation
                  The keys match those specified in the DataParams decorator
                  
        Data types in the 'data' dictionary:
         - datatype=INDICATOR: value is DatedValue (or List[DatedValue] if count > 1)
         - datatype=BARS: value is Bar (or List[Bar] if count > 1)
         - datatype=FINANCIAL: value depends on the specific financial data requested
        
        Returns:
            TradeSignal: A signal to open a position if conditions are met
            None: If conditions for opening a trade are not met
        """
        # Extract the indicator data from the data dictionary
        sma5 = data["sma5"]    # List of the last 2 values of 2-period SMA
        ema14 = data["ema14"]  # List of the last 2 values of 14-period EMA
        minute_bar = data["minute_bar"][-1]  # Get the latest one-minute bar
        
        # Implement crossover detection logic:
        # We generate a trade signal when the SMA crosses above the EMA
        # This happens when:
        # 1. Current SMA is above current EMA (sma5[-1].value > ema14[-1].value)
        # 2. Previous SMA was below or equal to previous EMA (sma5[-2].value <= ema14[-2].value)
        if sma5[-1].value > ema14[-1].value and sma5[-2].value <= ema14[-2].value:
            # Calculate signal strength based on multiple factors:
            
            # Get the closing price and volume from the latest bar
            closing_price = minute_bar.close
            volume = minute_bar.volume
            
            # 1. Calculate the crossover magnitude as a percentage
            crossover_magnitude = ((sma5[-1].value - ema14[-1].value) / ema14[-1].value) * 100
            
            # 2. Calculate the rate of change of the shorter SMA to measure momentum
            sma_change = ((sma5[-1].value - sma5[-2].value) / sma5[-2].value) * 100 if sma5[-2].value != 0 else 0
            
            # 3. Consider the bar's price movement (close vs open)
            price_change_pct = ((minute_bar.close - minute_bar.open) / minute_bar.open) * 100 if minute_bar.open != 0 else 0
            
            # Combine factors for signal strength (adjust weights as needed)
            # Higher volume, larger crossover magnitude, and positive price movement result in stronger signals
            signal_strength = (crossover_magnitude * 0.4) + (sma_change * 0.3) + (price_change_pct * 0.3)
            
            # Apply volume as a multiplier (normalized)
            signal_strength = signal_strength * (1 + (volume / 100000))
            
            # Crossover detected - generate a long position signal with calculated strength
            return TradeSignal(security, PositionType.LONG, signal_strength)
        else:
            # No crossover - return None (no trade signal)
            return None

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """
        Process trade signals and allocate the portfolio accordingly.
        
        This method is called after evaluateOpenTradeCondition has been called for all securities
        in the universe. It receives a list of all the trade signals generated and must convert
        them into actual trade orders.
        
        This is where you implement your portfolio allocation logic, such as:
        1. Limiting the number of positions (e.g., only take the top 10 signals)
        2. Allocating different amounts to different positions
        3. Handling existing positions in the portfolio
        4. Setting order types, quantities, and other specifications
        
        Args:
            portfolio: The current portfolio state, including:
                      - Current cash balance
                      - Open positions
                      - Pending orders
            tradeSignals: List of trade signals generated by evaluateOpenTradeCondition
        
        Returns:
            List[TradeOrder]: Orders to execute based on the signals and portfolio allocation
        """
        # Sort trade signals by strength in descending order to prioritize stronger signals
        sorted_signals = sorted(tradeSignals, key=lambda signal: signal.strength if signal.strength is not None else 0, reverse=True)
        
        # We provide a convenience utility that allocates a given percent of the portfolio to each position
        # In this case, we allocate 10% of the portfolio to each position (max 10 positions)
        portfolioAllocator = PercentBasedPortfolioAllocator(10)
        return portfolioAllocator.allocatePortfolio(portfolio, sorted_signals)

    def getStandardCloseCondition(self) -> StandardCloseCriteria | None:
        """
        Define standard exit criteria for positions.
        
        This method specifies when to automatically close positions based on:
        - Profit target: Close when position gains a certain percentage
        - Stop loss: Close when position loses a certain percentage
        - Trailing stop: Close when position retraces a certain percentage from its peak
        - Time limit: Close after a certain amount of time regardless of performance
        
        These are considered "standard" exit conditions that are commonly used.
        For more complex exit conditions, implement the evaluateCloseTradeCondition method.
        
        Returns:
            StandardCloseCriteria: The configured exit criteria
            None: If you don't want to use standard exit criteria
        """
        # TargetProfit and StopLoss are specified in percentages (5% and -5%)
        # TimeOut specifies a maximum holding period (10 days in this case)
        return StandardCloseCriteria(
            targetProfit=5,                      # Take profit at 5% gain
            stopLoss=-5,                         # Stop loss at 5% loss
            trailingStop=None,                   # No trailing stop for this strategy
            timeOut=TimeDelta(10, TimeUnit.DAYS) # Exit after 10 days
        )


    @DataParams({
        # Request current SMA value (no need for history since we're not detecting crossover)
        "sma5": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.SMA, "barinterval": BarInterval.ONE_MINUTE, "period": 2},
        # Request current EMA value
        "ema14": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.EMA, "barinterval": BarInterval.ONE_MINUTE, "period": 14},
        # Request the latest one-minute bar for price information
        "minute_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_MINUTE, "count": 1}
    })
    def evaluateCloseTradeCondition(self, openPos: OpenPosition, data: Dict[str, Any]) -> TradeOrder | None:
        """
        Evaluate whether to close an existing position.
        
        This method is called for each open position whenever new data is available.
        It allows you to implement custom exit conditions beyond the standard criteria.
        
        Note: This method is optional. If you don't implement it, only the standard
        close conditions specified in getStandardCloseCondition will be used.
        
        Args:
            openPos: The open position being evaluated, including:
                    - The security
                    - Entry price
                    - Position type (LONG or SHORT)
                    - Quantity
                    - Open date
            data: Dictionary containing the requested data based on @DataParams annotation
        
        Returns:
            TradeOrder: An order to close the position if conditions are met
            None: If conditions for closing the position are not met
        """
        # Note that unlike in evaluateOpenTradeCondition, we didn't specify "count" for the indicators
        # When count is omitted, it defaults to count=1, which means we get a single DatedValue
        # instead of a List[DatedValue]
        
        # Extract the indicator data
        sma5 = data["sma5"]   # Current value of 2-period SMA (a single DatedValue)
        ema14 = data["ema14"] # Current value of 14-period EMA (a single DatedValue)
        minute_bar = data["minute_bar"][-1]  # Get the latest one-minute bar

        # Custom exit condition: Close the position if SMA falls below 90% of EMA
        # This might indicate that the uptrend is weakening
        if sma5.value < 0.9 * ema14.value:
            # Create a sell order to close the position
            return TradeOrder(openPos.security, TradeType.SELL)
        
        # Additional exit condition: Close if the current bar shows significant price weakness
        # (e.g., if the close is near the low of the bar and significantly below the open)
        bar_range = minute_bar.high - minute_bar.low
        if bar_range > 0:
            # Calculate how close the close is to the low (0 = at low, 1 = at high)
            close_to_low_ratio = (minute_bar.close - minute_bar.low) / bar_range
            
            # Calculate the percentage drop from open to close
            open_to_close_drop = ((minute_bar.open - minute_bar.close) / minute_bar.open) * 100 if minute_bar.open != 0 else 0
            
            # Exit if close is in bottom 20% of the bar range and there's a significant drop from open
            if close_to_low_ratio < 0.2 and open_to_close_drop > 0.5:
                return TradeOrder(openPos.security, TradeType.SELL)
        
        # Conditions not met - don't close the position
        return None
            
    # Optional methods for state management
    
    def getState(self) -> Dict[str, Any]:
        """
        Return the current state to be persisted between strategy runs.
        
        This method is called to save the strategy's state between executions.
        The returned dictionary will be passed to restoreState when the strategy
        is next executed.
        
        Returns:
            Dict[str, Any]: The state to be persisted
        """
        return self.state
        
    def restoreState(self, state: Dict[str, Any]) -> None:
        """
        Restore the strategy state from persisted data.
        
        This method is called when the strategy is executed, passing in the state
        that was previously returned by getState.
        
        Args:
            state: The previously saved state
        """
        self.state = state
