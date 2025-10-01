"""
Ultimate Oscillator Indicator

The Ultimate Oscillator is a momentum oscillator that combines multiple timeframes
to identify overbought and oversold conditions. It uses three different periods
to reduce false signals and provide more reliable readings.

Formula:
1. Calculate True Range (TR) = max(High - Low, |High - Close[1]|, |Low - Close[1]|)
2. Calculate Buying Pressure (BP) = Close - min(Low, Close[1])
3. Calculate Selling Pressure (SP) = max(High, Close[1]) - Close
4. Calculate Average7 = Sum(BP) / Sum(TR) over 7 periods
5. Calculate Average14 = Sum(BP) / Sum(TR) over 14 periods  
6. Calculate Average28 = Sum(BP) / Sum(TR) over 28 periods
7. Ultimate Oscillator = 100 * ((4 * Average7) + (2 * Average14) + Average28) / 7

This indicator is particularly useful for:
- Identifying overbought/oversold conditions
- Divergence analysis
- Trend confirmation
- Entry/exit timing
- Multi-timeframe analysis
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math
import numpy as np


class UltimateOscillator(Indicator):
    """
    Ultimate Oscillator indicator implementation.
    
    This indicator combines multiple timeframes to identify overbought and
    oversold conditions with reduced false signals.
    """

    def getIndicatorSpec(self) -> IndicatorSpec:
        """Define the indicator specification."""
        indicator = IndicatorSpec("Ultimate Oscillator")
        indicator.description = "Multi-timeframe momentum oscillator for overbought/oversold identification"
        indicator.valueType = IndicatorValueType.PERCENT
        
        # Add period parameters
        indicator.addParam("period1", IndicatorParamSpec(
            paramType=ParamType.INTEGER, 
            required=True, 
            defaultValue=7, 
            options=[5, 7, 10, 14]
        ))
        
        indicator.addParam("period2", IndicatorParamSpec(
            paramType=ParamType.INTEGER, 
            required=True, 
            defaultValue=14, 
            options=[10, 14, 20, 28]
        ))
        
        indicator.addParam("period3", IndicatorParamSpec(
            paramType=ParamType.INTEGER, 
            required=True, 
            defaultValue=28, 
            options=[20, 28, 40, 50]
        ))
        
        return indicator

    def getDataSourceType(self) -> DataSource:
        """Specify that this indicator uses bar data."""
        return DataSource.BARS

    def computeSeries(self, params: Dict[str, Any], bars: List[Bar]) -> List[DatedValue]:
        """Compute the Ultimate Oscillator series."""
        dates, closes = CommonUtils.extractCloseSeries(bars)
        highs = [bar["high"] for bar in bars]
        lows = [bar["low"] for bar in bars]
        period1 = params['period1']
        period2 = params['period2']
        period3 = params['period3']
        
        if len(closes) < max(period1, period2, period3):
            return []
        
        # Calculate Ultimate Oscillator
        uo_series = self._calculate_ultimate_oscillator(highs, lows, closes, period1, period2, period3)
        
        # Convert to DatedValue list
        return CommonUtils.createListOfDatedValue(dates, np.array(uo_series))

    def _calculate_ultimate_oscillator(self, highs: List[float], lows: List[float], 
                                     closes: List[float], period1: int, period2: int, period3: int) -> List[float]:
        """Calculate Ultimate Oscillator values."""
        if len(closes) < 2:
            return [0.0] * len(closes)
        
        # Calculate True Range, Buying Pressure, and Selling Pressure
        tr_values = []
        bp_values = []
        sp_values = []
        
        for i in range(len(closes)):
            if i == 0:
                tr_values.append(highs[i] - lows[i])
                bp_values.append(closes[i] - lows[i])
                sp_values.append(highs[i] - closes[i])
            else:
                # True Range
                tr1 = highs[i] - lows[i]
                tr2 = abs(highs[i] - closes[i-1])
                tr3 = abs(lows[i] - closes[i-1])
                tr_values.append(max(tr1, tr2, tr3))
                
                # Buying Pressure
                bp = closes[i] - min(lows[i], closes[i-1])
                bp_values.append(bp)
                
                # Selling Pressure
                sp = max(highs[i], closes[i-1]) - closes[i]
                sp_values.append(sp)
        
        # Calculate Ultimate Oscillator
        uo_values = []
        for i in range(len(closes)):
            if i < max(period1, period2, period3) - 1:
                uo_values.append(50.0)  # Neutral value
                continue
            
            # Calculate averages for each period
            avg1 = self._calculate_average(bp_values, tr_values, i, period1)
            avg2 = self._calculate_average(bp_values, tr_values, i, period2)
            avg3 = self._calculate_average(bp_values, tr_values, i, period3)
            
            # Calculate Ultimate Oscillator
            uo = 100 * ((4 * avg1) + (2 * avg2) + avg3) / 7
            uo_values.append(uo)
        
        return uo_values

    def _calculate_average(self, bp_values: List[float], tr_values: List[float], 
                          current_index: int, period: int) -> float:
        """Calculate average of BP/TR over a period."""
        start_index = max(0, current_index - period + 1)
        
        bp_sum = sum(bp_values[start_index:current_index + 1])
        tr_sum = sum(tr_values[start_index:current_index + 1])
        
        if tr_sum == 0:
            return 0.0
        
        return bp_sum / tr_sum

    def dataCountToComputeCurrentValue(self, params: Dict[str, Any]) -> int | None:
        """Return the number of data points needed to compute current value."""
        period1 = params['period1']
        period2 = params['period2']
        period3 = params['period3']
        return max(period1, period2, period3) + 5
