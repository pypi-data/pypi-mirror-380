"""
Donchian Channel Indicator

The Donchian Channel is a volatility indicator that shows the highest high and
lowest low over a specified period. It consists of three lines: upper band
(highest high), lower band (lowest low), and middle line (average of upper and lower).

Formula:
- Upper Band = Highest High over period
- Lower Band = Lowest Low over period  
- Middle Line = (Upper Band + Lower Band) / 2

This indicator is particularly useful for:
- Identifying breakout levels
- Measuring volatility
- Trend following strategies
- Support/resistance levels
- Range trading
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math
import numpy as np


class DonchianChannel(Indicator):
    """
    Donchian Channel indicator implementation.
    
    This indicator shows the highest high and lowest low over a specified period,
    helping traders identify breakout levels and measure volatility.
    """

    def getIndicatorSpec(self) -> IndicatorSpec:
        """Define the indicator specification."""
        indicator = IndicatorSpec("Donchian Channel")
        indicator.description = "Shows highest high and lowest low over a period for breakout identification"
        indicator.valueType = IndicatorValueType.PRICE
        
        # Add period parameter
        indicator.addParam("period", IndicatorParamSpec(
            paramType=ParamType.INTEGER, 
            required=True, 
            defaultValue=20, 
            options=IndicatorParamSpec.PERIOD_VALUES
        ))
        
        # Add channel type parameter
        indicator.addParam("channel_type", IndicatorParamSpec(
            paramType=ParamType.STRING, 
            required=True, 
            defaultValue="upper", 
            options=["upper", "lower", "middle"]
        ))
        
        return indicator

    def getDataSourceType(self) -> DataSource:
        """Specify that this indicator uses bar data."""
        return DataSource.BARS

    def computeSeries(self, params: Dict[str, Any], bars: List[Bar]) -> List[DatedValue]:
        """Compute the Donchian Channel series."""
        dates, closes = CommonUtils.extractCloseSeries(bars)
        highs = [bar["high"] for bar in bars]
        lows = [bar["low"] for bar in bars]
        period = params['period']
        channel_type = params['channel_type']
        
        if len(closes) < period:
            return []
        
        # Calculate Donchian Channel
        upper_series, lower_series, middle_series = self._calculate_donchian_channel(highs, lows, period)
        
        # Return the requested channel type
        if channel_type == "upper":
            return CommonUtils.createListOfDatedValue(dates, np.array(upper_series))
        elif channel_type == "lower":
            return CommonUtils.createListOfDatedValue(dates, np.array(lower_series))
        else:  # middle
            return CommonUtils.createListOfDatedValue(dates, np.array(middle_series))

    def _calculate_donchian_channel(self, highs: List[float], lows: List[float], period: int) -> tuple[List[float], List[float], List[float]]:
        """Calculate Donchian Channel values."""
        upper_values = []
        lower_values = []
        middle_values = []
        
        for i in range(len(highs)):
            if i < period - 1:
                # Not enough data yet
                upper_values.append(highs[i])
                lower_values.append(lows[i])
                middle_values.append((highs[i] + lows[i]) / 2)
            else:
                # Get the window
                high_window = highs[i - period + 1:i + 1]
                low_window = lows[i - period + 1:i + 1]
                
                # Calculate upper and lower bands
                upper_band = max(high_window)
                lower_band = min(low_window)
                middle_band = (upper_band + lower_band) / 2
                
                upper_values.append(upper_band)
                lower_values.append(lower_band)
                middle_values.append(middle_band)
        
        return upper_values, lower_values, middle_values

    def dataCountToComputeCurrentValue(self, params: Dict[str, Any]) -> int | None:
        """Return the number of data points needed to compute current value."""
        period = params['period']
        return period
