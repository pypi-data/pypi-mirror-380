"""
Hull Moving Average (HMA) Indicator

The Hull Moving Average is a type of moving average that was developed by Alan Hull
and is designed to be more responsive to current price activity while maintaining
smoothness. It reduces lag while maintaining smoothness.

Formula:
1. Calculate WMA(period/2) of the price
2. Calculate WMA(period) of the price  
3. Calculate 2 * WMA(period/2) - WMA(period)
4. Calculate WMA(sqrt(period)) of the result from step 3

This indicator is particularly useful for:
- Trend identification
- Entry/exit timing
- Reducing lag in moving average crossovers
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math
import numpy as np
import talib  # type: ignore


class HullMovingAverage(Indicator):
    """
    Hull Moving Average indicator implementation.
    
    This indicator provides a fast, smooth moving average that reduces lag
    while maintaining the smoothness of traditional moving averages.
    """

    def getIndicatorSpec(self) -> IndicatorSpec:
        """Define the indicator specification."""
        indicator = IndicatorSpec("Hull Moving Average")
        indicator.description = "Hull Moving Average - Fast, smooth moving average that reduces lag"
        indicator.valueType = IndicatorValueType.PRICE
        
        # Add period parameter
        indicator.addParam("period", IndicatorParamSpec(
            paramType=ParamType.INTEGER, 
            required=True, 
            defaultValue=20, 
            options=IndicatorParamSpec.PERIOD_VALUES
        ))
        
        return indicator

    def getDataSourceType(self) -> DataSource:
        """Specify that this indicator uses bar data."""
        return DataSource.BARS

    def computeSeries(self, params: Dict[str, Any], bars: List[Bar]) -> List[DatedValue]:
        """Compute the Hull Moving Average series."""
        dates, close = CommonUtils.extractCloseSeries(bars)
        period = params['period']
        
        if len(close) < period:
            return []
        
        # Convert to numpy array
        close_array = np.array(close)
        
        # Calculate HMA using the formula
        hma_series = self._calculate_hma(close_array, period)
        
        # Convert to DatedValue list
        return CommonUtils.createListOfDatedValue(dates, hma_series)

    def _calculate_hma(self, prices: np.ndarray, period: int) -> np.ndarray:
        """Calculate Hull Moving Average."""
        # Step 1: Calculate WMA(period/2)
        half_period = max(1, period // 2)
        wma_half = talib.WMA(prices, timeperiod=half_period)
        
        # Step 2: Calculate WMA(period)
        wma_full = talib.WMA(prices, timeperiod=period)
        
        # Step 3: Calculate 2 * WMA(period/2) - WMA(period)
        raw_hma = 2 * wma_half - wma_full
        
        # Step 4: Calculate WMA(sqrt(period)) of the result
        sqrt_period = max(1, int(math.sqrt(period)))
        hma = talib.WMA(raw_hma, timeperiod=sqrt_period)
        
        return hma

    def dataCountToComputeCurrentValue(self, params: Dict[str, Any]) -> int | None:
        """Return the number of data points needed to compute current value."""
        period = params['period']
        # Need the full period plus some extra for the WMA calculations
        return period + 10
