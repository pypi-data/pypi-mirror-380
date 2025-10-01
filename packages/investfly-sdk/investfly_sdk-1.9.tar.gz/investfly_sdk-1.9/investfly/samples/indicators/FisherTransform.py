"""
Fisher Transform Indicator

The Fisher Transform is a mathematical transformation that converts price data
into a Gaussian (normal) distribution, making it easier to identify overbought
and oversold conditions and trend reversals.

Formula:
1. Calculate the median price over a period
2. Find the highest high and lowest low over the period
3. Apply Fisher Transform: 0.5 * ln((1 + x) / (1 - x))
   where x = (price - lowest) / (highest - lowest) - 0.5

This indicator is particularly useful for:
- Identifying overbought/oversold conditions
- Trend reversal signals
- Mean reversion strategies
- Normalizing price data for statistical analysis
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math
import numpy as np


class FisherTransform(Indicator):
    """
    Fisher Transform indicator implementation.
    
    This indicator transforms price data to a Gaussian distribution,
    making it easier to identify extreme values and trend changes.
    """

    def getIndicatorSpec(self) -> IndicatorSpec:
        """Define the indicator specification."""
        indicator = IndicatorSpec("Fisher Transform")
        indicator.description = "Fisher Transform - Converts price data to Gaussian distribution for trend identification"
        indicator.valueType = IndicatorValueType.NUMBER
        
        # Add period parameter
        indicator.addParam("period", IndicatorParamSpec(
            paramType=ParamType.INTEGER, 
            required=True, 
            defaultValue=10, 
            options=IndicatorParamSpec.PERIOD_VALUES
        ))
        
        return indicator

    def getDataSourceType(self) -> DataSource:
        """Specify that this indicator uses bar data."""
        return DataSource.BARS

    def computeSeries(self, params: Dict[str, Any], bars: List[Bar]) -> List[DatedValue]:
        """Compute the Fisher Transform series."""
        dates, close = CommonUtils.extractCloseSeries(bars)
        period = params['period']
        
        if len(close) < period:
            return []
        
        # Calculate Fisher Transform
        fisher_series = self._calculate_fisher_transform(close, period)
        
        # Convert to DatedValue list
        return CommonUtils.createListOfDatedValue(dates, np.array(fisher_series))

    def _calculate_fisher_transform(self, prices: List[float], period: int) -> List[float]:
        """Calculate Fisher Transform values."""
        fisher_values = []
        
        for i in range(len(prices)):
            if i < period - 1:
                fisher_values.append(0.0)
                continue
            
            # Get the price window
            price_window = prices[i - period + 1:i + 1]
            current_price = prices[i]
            
            # Find highest and lowest in the window
            highest = max(price_window)
            lowest = min(price_window)
            
            # Avoid division by zero
            if highest == lowest:
                fisher_values.append(0.0)
                continue
            
            # Calculate normalized price (0 to 1 range)
            normalized_price = (current_price - lowest) / (highest - lowest)
            
            # Transform to -1 to 1 range
            transformed_price = 2 * normalized_price - 1
            
            # Apply Fisher Transform
            if transformed_price == 1:
                fisher_value = 2.0  # Approximate limit
            elif transformed_price == -1:
                fisher_value = -2.0  # Approximate limit
            else:
                fisher_value = 0.5 * math.log((1 + transformed_price) / (1 - transformed_price))
            
            fisher_values.append(fisher_value)
        
        return fisher_values

    def dataCountToComputeCurrentValue(self, params: Dict[str, Any]) -> int | None:
        """Return the number of data points needed to compute current value."""
        period = params['period']
        return period
