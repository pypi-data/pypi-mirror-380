"""
Detrended Price Oscillator (DPO) Indicator

The Detrended Price Oscillator removes the trend component from price data,
allowing traders to focus on cyclical patterns and overbought/oversold conditions.

Formula:
DPO = Price - SMA(period/2 + 1) shifted back by (period/2 + 1) periods

This indicator is particularly useful for:
- Identifying cyclical patterns
- Finding overbought/oversold conditions
- Mean reversion trading
- Divergence analysis
- Timing entry/exit points
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math
import numpy as np
import talib  # type: ignore


class DetrendedPriceOscillator(Indicator):
    """
    Detrended Price Oscillator indicator implementation.
    
    This indicator removes the trend component from price data to reveal
    cyclical patterns and overbought/oversold conditions.
    """

    def getIndicatorSpec(self) -> IndicatorSpec:
        """Define the indicator specification."""
        indicator = IndicatorSpec("Detrended Price Oscillator")
        indicator.description = "DPO - Removes trend from price data to show cyclical patterns"
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
        """Compute the Detrended Price Oscillator series."""
        dates, close = CommonUtils.extractCloseSeries(bars)
        period = params['period']
        
        if len(close) < period:
            return []
        
        # Calculate DPO
        dpo_series = self._calculate_dpo(close, period)
        
        # Convert to DatedValue list
        return CommonUtils.createListOfDatedValue(dates, np.array(dpo_series))

    def _calculate_dpo(self, prices: List[float], period: int) -> List[float]:
        """Calculate Detrended Price Oscillator values."""
        dpo_values = []
        
        # Calculate the shift period
        shift_period = period // 2 + 1
        
        # Calculate SMA
        sma_period = shift_period
        sma_values = []
        
        for i in range(len(prices)):
            if i < sma_period - 1:
                sma_values.append(prices[i])
            else:
                # Calculate SMA for the window
                window = prices[i - sma_period + 1:i + 1]
                sma = sum(window) / len(window)
                sma_values.append(sma)
        
        # Calculate DPO
        for i in range(len(prices)):
            if i < shift_period:
                dpo_values.append(0.0)
            else:
                # DPO = Price - Shifted SMA
                current_price = prices[i]
                shifted_sma = sma_values[i - shift_period]
                dpo = current_price - shifted_sma
                dpo_values.append(dpo)
        
        return dpo_values

    def dataCountToComputeCurrentValue(self, params: Dict[str, Any]) -> int | None:
        """Return the number of data points needed to compute current value."""
        period = params['period']
        shift_period = period // 2 + 1
        return period + shift_period
