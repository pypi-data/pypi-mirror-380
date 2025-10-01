"""
Chandelier Exit Indicator

The Chandelier Exit is a dynamic stop-loss indicator that uses Average True Range (ATR)
to create trailing stop levels. It provides both long and short exit levels based on
trend direction and volatility.

Formula:
For Long Positions:
- Long Exit = Highest High - (ATR * multiplier)

For Short Positions:
- Short Exit = Lowest Low + (ATR * multiplier)

This indicator is particularly useful for:
- Dynamic stop-loss management
- Trend following strategies
- Risk management
- Position sizing
- Exit timing
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math
import numpy as np
import talib  # type: ignore


class ChandelierExit(Indicator):
    """
    Chandelier Exit indicator implementation.
    
    This indicator provides dynamic stop-loss levels based on ATR and trend direction,
    helping traders manage risk and exit positions effectively.
    """

    def getIndicatorSpec(self) -> IndicatorSpec:
        """Define the indicator specification."""
        indicator = IndicatorSpec("Chandelier Exit")
        indicator.description = "Dynamic stop-loss levels based on ATR and trend direction"
        indicator.valueType = IndicatorValueType.PRICE
        
        # Add period parameter for ATR
        indicator.addParam("atr_period", IndicatorParamSpec(
            paramType=ParamType.INTEGER, 
            required=True, 
            defaultValue=14, 
            options=IndicatorParamSpec.PERIOD_VALUES
        ))
        
        # Add ATR multiplier parameter
        indicator.addParam("atr_multiplier", IndicatorParamSpec(
            paramType=ParamType.FLOAT, 
            required=True, 
            defaultValue=3.0, 
            options=[1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
        ))
        
        return indicator

    def getDataSourceType(self) -> DataSource:
        """Specify that this indicator uses bar data."""
        return DataSource.BARS

    def computeSeries(self, params: Dict[str, Any], bars: List[Bar]) -> List[DatedValue]:
        """Compute the Chandelier Exit series."""
        dates, closes = CommonUtils.extractCloseSeries(bars)
        highs = [bar["high"] for bar in bars]
        lows = [bar["low"] for bar in bars]
        atr_period = params['atr_period']
        atr_multiplier = params['atr_multiplier']
        
        if len(closes) < atr_period:
            return []
        
        # Calculate ATR
        atr_series = self._calculate_atr(highs, lows, closes, atr_period)
        
        # Calculate Chandelier Exit levels
        long_exit_series = self._calculate_long_exit(highs, atr_series, atr_multiplier)
        
        # Return the long exit levels
        return CommonUtils.createListOfDatedValue(dates, np.array(long_exit_series))

    def _calculate_atr(self, highs: List[float], lows: List[float], closes: List[float], period: int) -> List[float]:
        """Calculate Average True Range."""
        # Calculate True Range
        tr_values = []
        for i in range(len(highs)):
            if i == 0:
                tr_values.append(highs[i] - lows[i])
            else:
                tr1 = highs[i] - lows[i]  # Current high - current low
                tr2 = abs(highs[i] - closes[i-1])  # Current high - previous close
                tr3 = abs(lows[i] - closes[i-1])   # Current low - previous close
                tr_values.append(max(tr1, tr2, tr3))
        
        # Calculate ATR using simple moving average
        atr_values = []
        for i in range(len(tr_values)):
            if i < period - 1:
                atr_values.append(tr_values[i])
            else:
                window = tr_values[i - period + 1:i + 1]
                atr = sum(window) / len(window)
                atr_values.append(atr)
        
        return atr_values

    def _calculate_long_exit(self, highs: List[float], atr: List[float], multiplier: float) -> List[float]:
        """Calculate long exit levels."""
        long_exit_values = []
        highest_high = 0.0
        
        for i in range(len(highs)):
            if i == 0:
                highest_high = highs[i]
                long_exit_values.append(highs[i] - (atr[i] * multiplier))
            else:
                # Update highest high
                if highs[i] > highest_high:
                    highest_high = highs[i]
                
                # Calculate long exit level
                long_exit = highest_high - (atr[i] * multiplier)
                long_exit_values.append(long_exit)
        
        return long_exit_values

    def _calculate_short_exit(self, lows: List[float], atr: List[float], multiplier: float) -> List[float]:
        """Calculate short exit levels."""
        short_exit_values = []
        lowest_low = float('inf')
        
        for i in range(len(lows)):
            if i == 0:
                lowest_low = lows[i]
                short_exit_values.append(lows[i] + (atr[i] * multiplier))
            else:
                # Update lowest low
                if lows[i] < lowest_low:
                    lowest_low = lows[i]
                
                # Calculate short exit level
                short_exit = lowest_low + (atr[i] * multiplier)
                short_exit_values.append(short_exit)
        
        return short_exit_values

    def dataCountToComputeCurrentValue(self, params: Dict[str, Any]) -> int | None:
        """Return the number of data points needed to compute current value."""
        atr_period = params['atr_period']
        return atr_period + 10
