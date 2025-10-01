import math
from datetime import datetime
from typing import List, Tuple, Any

import numpy
import pandas as pd

from investfly.models import DatedValue, Bar


def createPandasDf(bars: List[Bar]) -> pd.DataFrame:
    df = pd.DataFrame(bars)
    df.set_index("date", inplace=True)
    return df

def extractCloseSeries(bars: List[Bar]) -> Tuple[List[datetime], List[float]]:
    dates: List[datetime] = [b['date'] for b in bars]
    closeSeries: List[float] = [b['close'] for b in bars]
    return dates, closeSeries

def extractOHLCSeries(bars: List[Bar]) -> Tuple[List[datetime], List[float], List[float], List[float], List[float]]:
    dates: List[datetime] = [b['date'] for b in bars]
    openSeries: List[float] = [b['open'] for b in bars]
    highSeries: List[float] = [b['high'] for b in bars]
    lowSeries: List[float] = [b['low'] for b in bars]
    closeSeries: List[float] = [b['close'] for b in bars]
    return dates, openSeries, highSeries, lowSeries, closeSeries


def pandasSeriesToList(series: pd.Series) -> List[DatedValue]:
    records = series.to_dict() # float64 is auto-converted to float by to_dict
    result: List[DatedValue] = []
    for key in records:
        date = key.to_pydatetime()  # type: ignore
        val = records[key]
        if not math.isnan(val):
            result.append(DatedValue(date, val))
    return result

def createListOfDatedValue(dates: List[datetime], values: numpy.ndarray[Any, numpy.dtype[numpy.float64]]):
    result: List[DatedValue] = []
    for i in range(len(dates)):
        date: datetime = dates[i]
        val = values[i]
        if not numpy.isnan(val):
            result.append(DatedValue(date, val.item()))
    return result

def floatListToDatedValueList(dates: List[datetime], values: List[float|int]):
    result: List[DatedValue] = []
    for i in range(len(dates)):
        date: datetime = dates[i]
        val = values[i]
        result.append(DatedValue(date, val))
    return result

def toHeikinAshi(bars: List[Bar]) -> List[Bar]:
    heiken: List[Bar] = []
    for i in range(len(bars)):
        b = bars[i]
        
        # Calculate Heikin-Ashi values
        ha_close = (b['open'] + b['high'] + b['low'] + b['close']) / 4
        
        if i == 0:
            ha_open = (b['open'] + b['close'])/2
        else:
            ha_open = (heiken[i-1]['open'] + heiken[i-1]['close'])/2
            
        ha_high = max(b['high'], ha_open, ha_close)
        ha_low = min(b['low'], ha_open, ha_close)
        
        h = Bar(
            symbol=b['symbol'],
            date=b['date'],
            barinterval=b['barinterval'],
            volume=b['volume'],
            open=ha_open,
            close=ha_close,
            high=ha_high,
            low=ha_low
        )
        
        heiken.append(h)

    return heiken
