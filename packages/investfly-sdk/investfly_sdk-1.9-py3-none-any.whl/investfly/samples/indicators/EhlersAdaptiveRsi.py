"""
Ehlers Adaptive RSI Indicator

The Ehlers Adaptive RSI is an enhanced version of the traditional RSI that
automatically adjusts its period based on market volatility. This makes it
more responsive in volatile markets and more stable in quiet markets.

Formula:
1. Calculate Adaptive Period = 0.5 * (1 + cos(2π * t / cycle_length))
2. Calculate RSI using the adaptive period
3. The adaptive period varies between min_period and max_period

This indicator is particularly useful for:
- Adapting to changing market conditions
- Reducing false signals in different volatility regimes
- More responsive RSI in volatile markets
- More stable RSI in quiet markets
- Dynamic period adjustment
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math
import numpy as np


class EhlersAdaptiveRsi(Indicator):
    """
    Ehlers Adaptive RSI indicator implementation.
    
    This indicator automatically adjusts its period based on market volatility,
    providing more responsive readings in volatile markets and more stable
    readings in quiet markets.
    """

    def getIndicatorSpec(self) -> IndicatorSpec:
        """Define the indicator specification."""
        indicator = IndicatorSpec("Ehlers Adaptive RSI")
        indicator.description = "Adaptive RSI that adjusts period based on market volatility"
        indicator.valueType = IndicatorValueType.PERCENT
        
        # Add minimum period parameter
        indicator.addParam("min_period", IndicatorParamSpec(
            paramType=ParamType.INTEGER, 
            required=True, 
            defaultValue=5, 
            options=[3, 5, 7, 10, 14]
        ))
        
        # Add maximum period parameter
        indicator.addParam("max_period", IndicatorParamSpec(
            paramType=ParamType.INTEGER, 
            required=True, 
            defaultValue=25, 
            options=[20, 25, 30, 35, 40]
        ))
        
        # Add cycle length parameter
        indicator.addParam("cycle_length", IndicatorParamSpec(
            paramType=ParamType.INTEGER, 
            required=True, 
            defaultValue=20, 
            options=[10, 15, 20, 25, 30]
        ))
        
        return indicator

    def getDataSourceType(self) -> DataSource:
        """Specify that this indicator uses bar data."""
        return DataSource.BARS

    def computeSeries(self, params: Dict[str, Any], bars: List[Bar]) -> List[DatedValue]:
        """Compute the Ehlers Adaptive RSI series."""
        dates, closes = CommonUtils.extractCloseSeries(bars)
        min_period = params['min_period']
        max_period = params['max_period']
        cycle_length = params['cycle_length']
        
        if len(closes) < max_period:
            return []
        
        # Calculate Adaptive RSI
        adaptive_rsi_series = self._calculate_adaptive_rsi(closes, min_period, max_period, cycle_length)
        
        # Convert to DatedValue list
        return CommonUtils.createListOfDatedValue(dates, np.array(adaptive_rsi_series))

    def _calculate_adaptive_rsi(self, closes: List[float], min_period: int, 
                               max_period: int, cycle_length: int) -> List[float]:
        """Calculate Ehlers Adaptive RSI values."""
        if len(closes) < 2:
            return [50.0] * len(closes)
        
        # Calculate price changes
        price_changes = []
        for i in range(1, len(closes)):
            change = closes[i] - closes[i-1]
            price_changes.append(change)
        
        # Calculate Adaptive RSI
        adaptive_rsi_values = []
        
        for i in range(len(closes)):
            if i < max_period:
                adaptive_rsi_values.append(50.0)  # Neutral value
                continue
            
            # Calculate adaptive period
            adaptive_period = self._calculate_adaptive_period(i, cycle_length, min_period, max_period)
            
            # Calculate RSI using adaptive period
            rsi = self._calculate_rsi_for_period(price_changes, i, int(adaptive_period))
            adaptive_rsi_values.append(rsi)
        
        return adaptive_rsi_values

    def _calculate_adaptive_period(self, current_index: int, cycle_length: int, 
                                 min_period: int, max_period: int) -> float:
        """Calculate adaptive period using cosine function."""
        # Normalize time to cycle
        t = current_index % cycle_length
        
        # Calculate cosine-based adaptive factor
        cos_factor = 0.5 * (1 + math.cos(2 * math.pi * t / cycle_length))
        
        # Map to period range
        adaptive_period = min_period + (max_period - min_period) * cos_factor
        
        return adaptive_period

    def _calculate_rsi_for_period(self, price_changes: List[float], current_index: int, period: int) -> float:
        """Calculate RSI for a specific period."""
        if current_index < period:
            return 50.0
        
        # Get the window of price changes
        start_index = max(0, current_index - period)
        window = price_changes[start_index:current_index]
        
        if len(window) == 0:
            return 50.0
        
        # Calculate gains and losses
        gains = [change if change > 0 else 0 for change in window]
        losses = [-change if change < 0 else 0 for change in window]
        
        avg_gain = sum(gains) / len(gains)
        avg_loss = sum(losses) / len(losses)
        
        if avg_loss == 0:
            return 100.0
        
        # Calculate RSI
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi

    def dataCountToComputeCurrentValue(self, params: Dict[str, Any]) -> int | None:
        """Return the number of data points needed to compute current value."""
        max_period = params['max_period']
        return max_period + 10
