"""
Center of Gravity Oscillator (COG) Indicator

The Center of Gravity Oscillator is a momentum indicator that measures the
balance point of price action over a specified period. It helps identify
trend reversals and momentum shifts.

Formula:
COG = -SUM(i * price[i]) / SUM(price[i]) for i = 0 to period-1
where price[i] is the price i periods ago

This indicator is particularly useful for:
- Identifying trend reversals
- Measuring momentum strength
- Finding overbought/oversold conditions
- Divergence analysis
- Entry/exit timing
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math
import numpy as np


class CenterOfGravityOscillator(Indicator):
    """
    Center of Gravity Oscillator indicator implementation.
    
    This indicator measures the balance point of price action to identify
    momentum shifts and trend reversals.
    """

    def getIndicatorSpec(self) -> IndicatorSpec:
        """Define the indicator specification."""
        indicator = IndicatorSpec("Center of Gravity Oscillator")
        indicator.description = "COG - Measures momentum balance point for trend reversal identification"
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
        """Compute the Center of Gravity Oscillator series."""
        dates, close = CommonUtils.extractCloseSeries(bars)
        period = params['period']
        
        if len(close) < period:
            return []
        
        # Calculate COG
        cog_series = self._calculate_cog(close, period)
        
        # Convert to DatedValue list
        return CommonUtils.createListOfDatedValue(dates, np.array(cog_series))

    def _calculate_cog(self, prices: List[float], period: int) -> List[float]:
        """Calculate Center of Gravity Oscillator values."""
        cog_values = []
        
        for i in range(len(prices)):
            if i < period - 1:
                cog_values.append(0.0)
                continue
            
            # Get the price window
            price_window = prices[i - period + 1:i + 1]
            
            # Calculate weighted sum
            weighted_sum = 0.0
            price_sum = 0.0
            
            for j, price in enumerate(price_window):
                weighted_sum += j * price
                price_sum += price
            
            # Avoid division by zero
            if price_sum == 0:
                cog_values.append(0.0)
                continue
            
            # Calculate COG
            cog = -weighted_sum / price_sum
            cog_values.append(cog)
        
        return cog_values

    def dataCountToComputeCurrentValue(self, params: Dict[str, Any]) -> int | None:
        """Return the number of data points needed to compute current value."""
        period = params['period']
        return period
