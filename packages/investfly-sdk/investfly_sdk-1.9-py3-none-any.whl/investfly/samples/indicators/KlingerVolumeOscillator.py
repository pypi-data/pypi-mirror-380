"""
Klinger Volume Oscillator (KVO) Indicator

The Klinger Volume Oscillator combines price and volume data to identify
trend reversals and confirm price movements. It helps distinguish between
accumulation and distribution phases.

Formula:
1. Calculate Trend Direction (TD)
2. Calculate Daily Force (DF) = Volume * TD * |Close - Close[1]|
3. Calculate KVO = EMA(short_period, DF) - EMA(long_period, DF)
4. Calculate Signal Line = EMA(signal_period, KVO)

This indicator is particularly useful for:
- Identifying trend reversals
- Confirming price movements
- Distinguishing accumulation/distribution
- Volume-price divergence analysis
- Entry/exit timing
"""

from investfly.models import *
from investfly.utils import *
from typing import Any, List, Dict
import math
import numpy as np
import talib  # type: ignore


class KlingerVolumeOscillator(Indicator):
    """
    Klinger Volume Oscillator indicator implementation.
    
    This indicator combines price and volume data to identify trend reversals
    and confirm price movements.
    """

    def getIndicatorSpec(self) -> IndicatorSpec:
        """Define the indicator specification."""
        indicator = IndicatorSpec("Klinger Volume Oscillator")
        indicator.description = "Combines price and volume to identify trend reversals and confirm movements"
        indicator.valueType = IndicatorValueType.NUMBER
        
        # Add short period parameter
        indicator.addParam("short_period", IndicatorParamSpec(
            paramType=ParamType.INTEGER, 
            required=True, 
            defaultValue=34, 
            options=IndicatorParamSpec.PERIOD_VALUES
        ))
        
        # Add long period parameter
        indicator.addParam("long_period", IndicatorParamSpec(
            paramType=ParamType.INTEGER, 
            required=True, 
            defaultValue=55, 
            options=IndicatorParamSpec.PERIOD_VALUES
        ))
        
        # Add signal period parameter
        indicator.addParam("signal_period", IndicatorParamSpec(
            paramType=ParamType.INTEGER, 
            required=True, 
            defaultValue=13, 
            options=IndicatorParamSpec.PERIOD_VALUES
        ))
        
        return indicator

    def getDataSourceType(self) -> DataSource:
        """Specify that this indicator uses bar data."""
        return DataSource.BARS

    def computeSeries(self, params: Dict[str, Any], bars: List[Bar]) -> List[DatedValue]:
        """Compute the Klinger Volume Oscillator series."""
        dates, closes = CommonUtils.extractCloseSeries(bars)
        volumes = [float(bar["volume"]) for bar in bars]
        short_period = params['short_period']
        long_period = params['long_period']
        signal_period = params['signal_period']
        
        if len(closes) < max(short_period, long_period):
            return []
        
        # Calculate KVO
        kvo_series = self._calculate_kvo(closes, volumes, short_period, long_period)
        
        # Calculate signal line
        signal_series = self._calculate_signal_line(kvo_series, signal_period)
        
        # Return the main KVO line (you could also return signal line as a separate indicator)
        return CommonUtils.createListOfDatedValue(dates, np.array(kvo_series))

    def _calculate_kvo(self, closes: List[float], volumes: List[float], short_period: int, long_period: int) -> List[float]:
        """Calculate Klinger Volume Oscillator values."""
        if len(closes) < 2:
            return [0.0] * len(closes)
        
        # Calculate trend direction and daily force
        trend_directions = []
        daily_forces = []
        
        for i in range(len(closes)):
            if i == 0:
                trend_directions.append(1)  # Default to upward trend
                daily_forces.append(0.0)
            else:
                # Calculate trend direction
                if closes[i] > closes[i-1]:
                    trend_directions.append(1)  # Upward trend
                elif closes[i] < closes[i-1]:
                    trend_directions.append(-1)  # Downward trend
                else:
                    # Same price, use previous trend direction
                    trend_directions.append(trend_directions[i-1])
                
                # Calculate daily force
                price_change = abs(closes[i] - closes[i-1])
                daily_force = volumes[i] * trend_directions[i] * price_change
                daily_forces.append(daily_force)
        
        # Calculate EMAs
        short_ema = self._calculate_ema(daily_forces, short_period)
        long_ema = self._calculate_ema(daily_forces, long_period)
        
        # Calculate KVO
        kvo_values = []
        for i in range(len(short_ema)):
            if i < len(long_ema):
                kvo = short_ema[i] - long_ema[i]
            else:
                kvo = 0.0
            kvo_values.append(kvo)
        
        return kvo_values

    def _calculate_ema(self, values: List[float], period: int) -> List[float]:
        """Calculate Exponential Moving Average."""
        if len(values) < period:
            return values
        
        # Calculate SMA for the first period values
        sma = sum(values[:period]) / period
        
        ema_values = []
        multiplier = 2.0 / (period + 1)
        
        for i, value in enumerate(values):
            if i < period - 1:
                ema_values.append(value)
            elif i == period - 1:
                ema_values.append(sma)
            else:
                ema = (value * multiplier) + (ema_values[i-1] * (1 - multiplier))
                ema_values.append(ema)
        
        return ema_values

    def _calculate_signal_line(self, kvo_values: List[float], signal_period: int) -> List[float]:
        """Calculate signal line using EMA of KVO."""
        return self._calculate_ema(kvo_values, signal_period)

    def dataCountToComputeCurrentValue(self, params: Dict[str, Any]) -> int | None:
        """Return the number of data points needed to compute current value."""
        short_period = params['short_period']
        long_period = params['long_period']
        return max(short_period, long_period) + 10
