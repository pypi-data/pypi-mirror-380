"""
Ehlers Fisher Transform Indicator

The Ehlers Fisher Transform is an enhanced version of the Fisher Transform that
provides better signal processing for trend identification. It uses a more
sophisticated normalization approach and includes signal smoothing.

Formula:
1. Calculate normalized price: (price - lowest) / (highest - lowest)
2. Apply Fisher Transform: 0.5 * ln((1 + x) / (1 - x))
3. Apply smoothing filter to reduce noise
4. The result is a Gaussian-distributed oscillator

This indicator is particularly useful for:
- Enhanced trend identification
- Reduced noise in signals
- Better overbought/oversold detection
- Improved divergence analysis
- Signal smoothing and filtering
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math
import numpy as np


class EhlersFisherTransform(Indicator):
    """
    Ehlers Fisher Transform indicator implementation.
    
    This indicator provides enhanced signal processing for trend identification
    with reduced noise and better signal quality.
    """

    def getIndicatorSpec(self) -> IndicatorSpec:
        """Define the indicator specification."""
        indicator = IndicatorSpec("Ehlers Fisher Transform")
        indicator.description = "Enhanced Fisher Transform with signal smoothing for trend identification"
        indicator.valueType = IndicatorValueType.NUMBER
        
        # Add period parameter
        indicator.addParam("period", IndicatorParamSpec(
            paramType=ParamType.INTEGER, 
            required=True, 
            defaultValue=10, 
            options=IndicatorParamSpec.PERIOD_VALUES
        ))
        
        # Add smoothing parameter
        indicator.addParam("smoothing_period", IndicatorParamSpec(
            paramType=ParamType.INTEGER, 
            required=True, 
            defaultValue=3, 
            options=[2, 3, 4, 5, 6]
        ))
        
        return indicator

    def getDataSourceType(self) -> DataSource:
        """Specify that this indicator uses bar data."""
        return DataSource.BARS

    def computeSeries(self, params: Dict[str, Any], bars: List[Bar]) -> List[DatedValue]:
        """Compute the Ehlers Fisher Transform series."""
        dates, closes = CommonUtils.extractCloseSeries(bars)
        period = params['period']
        smoothing_period = params['smoothing_period']
        
        if len(closes) < period:
            return []
        
        # Calculate Ehlers Fisher Transform
        eft_series = self._calculate_ehlers_fisher_transform(closes, period, smoothing_period)
        
        # Convert to DatedValue list
        return CommonUtils.createListOfDatedValue(dates, np.array(eft_series))

    def _calculate_ehlers_fisher_transform(self, prices: List[float], period: int, smoothing_period: int) -> List[float]:
        """Calculate Ehlers Fisher Transform values."""
        if len(prices) < period:
            return [0.0] * len(prices)
        
        # Calculate Fisher Transform values
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
            
            # Apply Fisher Transform with bounds checking
            if transformed_price >= 0.999:
                fisher_value = 2.0  # Approximate limit
            elif transformed_price <= -0.999:
                fisher_value = -2.0  # Approximate limit
            else:
                fisher_value = 0.5 * math.log((1 + transformed_price) / (1 - transformed_price))
            
            fisher_values.append(fisher_value)
        
        # Apply smoothing filter
        smoothed_values = self._apply_smoothing_filter(fisher_values, smoothing_period)
        
        return smoothed_values

    def _apply_smoothing_filter(self, values: List[float], smoothing_period: int) -> List[float]:
        """Apply smoothing filter to reduce noise."""
        if len(values) < smoothing_period:
            return values
        
        smoothed_values = []
        
        for i in range(len(values)):
            if i < smoothing_period - 1:
                smoothed_values.append(values[i])
            else:
                # Calculate weighted average for smoothing
                window = values[i - smoothing_period + 1:i + 1]
                
                # Use exponential weighting (more weight to recent values)
                weights = []
                for j in range(smoothing_period):
                    weight = math.exp(j - smoothing_period + 1)
                    weights.append(weight)
                
                # Normalize weights
                total_weight = sum(weights)
                normalized_weights = [w / total_weight for w in weights]
                
                # Calculate weighted average
                smoothed_value = sum(v * w for v, w in zip(window, normalized_weights))
                smoothed_values.append(smoothed_value)
        
        return smoothed_values

    def dataCountToComputeCurrentValue(self, params: Dict[str, Any]) -> int | None:
        """Return the number of data points needed to compute current value."""
        period = params['period']
        smoothing_period = params['smoothing_period']
        return period + smoothing_period
