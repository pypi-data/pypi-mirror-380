from typing import Dict, Any, List

from investfly.models import *
from investfly.utils import PercentBasedPortfolioAllocator


class RsiMeanReversionStrategy(TradingStrategy):
    """
    A mean reversion strategy based on the RSI (Relative Strength Index) indicator.
    
    This strategy:
    1. Uses the RSI indicator to identify overbought and oversold conditions
    2. Generates buy signals when RSI moves from below 30 (oversold) back above 30 (potential upward reversal)
    3. Includes risk management with target profit, stop loss, and time-based exit criteria
    4. Allocates portfolio to the top 5 stocks showing the strongest reversal signals
    
    Note: This strategy operates on daily bars, so evaluateOpenTradeCondition is called
    at most once per day when a new daily bar is available.
    """

    def __init__(self) -> None:
        """
        Initialize the strategy with state to track RSI values.
        
        Since the strategy state can only contain primitive values (int, float, bool),
        we use a flattened key structure to track which securities were previously oversold.
        """
        super().__init__()
        # The state starts empty and will be populated as we process securities
        # We'll use keys in the format "oversold_{symbol}" with boolean values

    def getSecurityUniverseSelector(self) -> SecurityUniverseSelector:
        """
        Select the universe of securities to trade.
        
        This strategy uses the S&P 100 stocks, which includes 100 of the largest
        and most established companies in the U.S. market.
        
        Returns:
            SecurityUniverseSelector: A selector configured to use the S&P 100 stocks
        """
        return SecurityUniverseSelector.fromStandardList(StandardSymbolsList.SP_100)

    @DataParams({
        # RSI with standard 14-period setting
        "rsi": {"datatype": DataType.INDICATOR, "indicator": INDICATORS.RSI, "barinterval": BarInterval.ONE_DAY, "period": 14, "count": 2},
        # Get the latest daily bar to access volume and price data
        "daily_bar": {"datatype": DataType.BARS, "barinterval": BarInterval.ONE_DAY, "count": 5}
    })
    def evaluateOpenTradeCondition(self, security: Security, data: Dict[str, Any]) -> TradeSignal | None:
        """
        Generate a buy signal when RSI moves from oversold territory (below 30) back above 30,
        indicating a potential upward reversal.
        
        The signal strength is calculated based on the magnitude of the RSI change, volume,
        and price action from the daily bars.
        
        This method is called at most once per day when a new daily bar is available.
        
        Args:
            security: The security (stock) being evaluated
            data: Dictionary containing the requested data:
                  - "rsi": List of the last 2 values of the 14-period RSI
                  - "daily_bar": List of the last 5 daily bars
        
        Returns:
            TradeSignal: A signal to open a long position if reversal condition is met
            None: If no reversal is detected
        """
        rsi = data["rsi"]
        daily_bars = data["daily_bar"]
        symbol = security.symbol
        
        # Get current and previous RSI values
        current_rsi = rsi[-1].value
        previous_rsi = rsi[-2].value
        
        # Get the latest daily bar for volume and price data
        latest_bar = daily_bars[-1]
        
        # Create a key for this symbol in our state
        state_key = f"oversold_{symbol}"
        
        # Check if the security was previously oversold (RSI below 30)
        # If the key doesn't exist yet, default to False
        was_oversold = bool(self.state.get(state_key, False))
        
        # Update the oversold state
        if previous_rsi < 30:
            self.state[state_key] = True
        elif current_rsi > 50:  # Reset once RSI moves well above oversold
            self.state[state_key] = False
        
        # Generate buy signal if RSI was below 30 and is now moving above 30
        if was_oversold and previous_rsi < 30 and current_rsi >= 30:
            # Calculate signal strength based on multiple factors
            
            # 1. RSI change - larger change indicates stronger momentum
            rsi_change = current_rsi - previous_rsi
            
            # 2. Volume - higher volume indicates stronger confirmation
            volume = latest_bar.volume
            
            # 3. Price action - calculate the percentage gain in the latest bar
            price_change_pct = ((latest_bar.close - latest_bar.open) / latest_bar.open) * 100 if latest_bar.open != 0 else 0
            
            # 4. Volume trend - compare current volume to average of previous bars
            avg_volume = sum(bar.volume for bar in daily_bars[:-1]) / (len(daily_bars) - 1) if len(daily_bars) > 1 else volume
            volume_ratio = volume / avg_volume if avg_volume > 0 else 1
            
            # Combine factors for signal strength (adjust weights as needed)
            # Higher RSI change, higher volume, and positive price action result in stronger signals
            base_strength = rsi_change * (1 + max(0, price_change_pct) / 10)
            volume_factor = volume_ratio * (volume / 1000000)  # Normalize volume
            
            signal_strength = base_strength * volume_factor
            
            # Return a long position signal with the calculated strength
            return TradeSignal(security, PositionType.LONG, signal_strength)
        
        return None

    def getStandardCloseCondition(self) -> StandardCloseCriteria:
        """
        Define standard exit criteria for positions.
        
        Mean reversion strategies typically have shorter holding periods and tighter
        profit targets compared to trend following strategies.
        
        Returns:
            StandardCloseCriteria: The configured exit criteria
        """
        return StandardCloseCriteria(
            targetProfit=4,           # Take profit at 4% gain
            stopLoss=-2,              # Stop loss at 2% loss
            trailingStop=None,        # No trailing stop for this strategy
            timeOut=TimeDelta(5, TimeUnit.DAYS)  # Exit after 5 trading days
        )

    def processOpenTradeSignals(self, portfolio: Portfolio, tradeSignals: List[TradeSignal]) -> List[TradeOrder]:
        """
        Process trade signals and allocate the portfolio accordingly.
        
        This method converts TradeSignals into actual TradeOrders, determining:
        - Which signals to act on (if there are more signals than available capital)
        - How much capital to allocate to each position
        
        The strategy allocates to a maximum of 5 stocks with equal weight (20% each).
        
        Args:
            portfolio: The current portfolio state
            tradeSignals: List of trade signals generated by evaluateOpenTradeCondition
        
        Returns:
            List[TradeOrder]: Orders to execute based on the signals and portfolio allocation
        """
        # Sort trade signals by strength in descending order
        sorted_signals = sorted(tradeSignals, key=lambda signal: signal.strength if signal.strength is not None else 0, reverse=True)
        
        # Use the PercentBasedPortfolioAllocator to allocate the portfolio
        # Allocate to the top 5 stocks with equal weight (20% each)
        portfolioAllocator = PercentBasedPortfolioAllocator(5)
        return portfolioAllocator.allocatePortfolio(portfolio, sorted_signals) 