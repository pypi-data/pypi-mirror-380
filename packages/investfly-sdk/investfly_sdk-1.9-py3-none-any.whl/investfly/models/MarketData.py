from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import TypedDict, Dict, Any, cast

from investfly.models.CommonModels import DatedValue
from investfly.models.MarketDataIds import QuoteField
from investfly.models.ModelUtils import ModelUtils

def parseDatetime(date_str: str) -> datetime:
    return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f%z').astimezone(ModelUtils.est_zone) 


def formatDatetime(dt: datetime) -> str:
    return dt.strftime('%Y-%m-%dT%H:%M:%S.%f%z')


class SecurityType(str, Enum):
    """
    Enum representing Security Type (STOCK, ETF)
    """

    STOCK = "STOCK"
    ETF = "ETF"
    CRYPTO = "CRYPTO"
    FOREX = "FOREX"
    OPTION = "OPTION"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


# All enums subclass str to make them JSON serializable

@dataclass(frozen=True)
class Security:
    """
    Class representing a security instrument that is traded in the market
    """

    symbol: str
    """ Security Symbol """

    securityType: SecurityType
    """ Security Type """

    @staticmethod
    def createStock(symbol: str):
        return Security(symbol, SecurityType.STOCK)

    @staticmethod
    def fromDict(jsonDict: Dict[str, Any]) -> Security:
        return Security(jsonDict["symbol"], SecurityType[jsonDict["securityType"]])

    def toDict(self) -> Dict[str, Any]:
        return self.__dict__.copy()


@dataclass
class Quote:
    """ Class representing Price Quote """
    symbol: str
    date: datetime
    lastPrice: float
    prevClose: float| None = None
    todayChange: float | None = None
    todayChangePct: float | None = None
    dayOpen: float | None = None
    dayHigh: float | None = None
    dayLow: float | None = None
    volume: int | None = None

    @staticmethod
    def fromDict(jsonDict: Dict[str, Any]) -> Quote:
        quote = Quote(jsonDict["symbol"], parseDatetime(jsonDict["date"]), jsonDict["lastPrice"])
        quote.prevClose = jsonDict.get('prevClose')
        quote.todayChange = jsonDict.get("todayChange")
        quote.todayChangePct = jsonDict.get('todayChangePct')
        quote.dayOpen = jsonDict.get('dayOpen')
        quote.dayHigh = jsonDict.get('dayHigh')
        quote.dayLow = jsonDict.get('dayLow')
        quote.volume = jsonDict.get('volume')
        return quote

    def toDict(self) -> Dict[str, Any]:
        jsonDict = self.__dict__.copy()
        jsonDict["date"] = formatDatetime(self.date)
        return jsonDict

    def toIndicatorValue(self, quoteField: QuoteField) -> DatedValue:
        if quoteField == QuoteField.LASTPRICE:
            return DatedValue(self.date, self.lastPrice)
        elif quoteField == QuoteField.DAY_OPEN:
            if self.dayOpen is None:
                raise Exception("DAY_OPEN price not available in Quote")
            return DatedValue(self.date, self.dayOpen)
        elif quoteField == QuoteField.DAY_HIGH:
            if self.dayHigh is None:
                raise Exception("DAY_HIGH price not available in Quote")
            return DatedValue(self.date, self.dayHigh)
        elif quoteField == QuoteField.DAY_LOW:
            if self.dayLow is None:
                raise Exception("DAY_LOW price not available in Quote")
            return DatedValue(self.date, self.dayLow)
        elif quoteField == QuoteField.PREV_DAY_CLOSE:
            if self.prevClose is None:
                raise Exception("PREV_DAY_CLOSE price not available in Quote")
            return DatedValue(self.date, self.prevClose)
        elif quoteField == QuoteField.DAY_CHANGE:
            if self.todayChange is None:
                raise Exception("DAY_CHANGE not available in Quote")
            return DatedValue(self.date, self.todayChange)
        elif quoteField == QuoteField.DAY_CHANGE_PCT:
            if self.todayChangePct is None:
                raise Exception("DAY_CHANGE_PCT value not available in Quote")
            return DatedValue(self.date, self.todayChangePct)
        elif quoteField == QuoteField.DAY_VOLUME:
            if self.volume is None:
                raise Exception("DAY_VOLUME not available in Quote")
            return DatedValue(self.date, self.volume)
        elif quoteField == QuoteField.DAY_CHANGE_OPEN:
            if self.dayOpen is None or self.lastPrice is None:
                raise Exception("DAY_CHANGE_OPEN not available in Quote")
            return DatedValue(self.date, self.lastPrice - self.dayOpen)
        else:
            raise Exception("Invalid Quote Indicator ID: " + quoteField)

    def toEODBar(self) -> Bar:
        return Bar(
            symbol=self.symbol,
            barinterval=BarInterval.ONE_DAY,
            date=self.date.replace(second=0, microsecond=0),
            open=cast(float, self.dayOpen),
            high=cast(float, self.dayHigh),
            low=cast(float, self.dayLow),
            close=cast(float, self.lastPrice),
            volume=cast(int, self.volume)
        )


class BarInterval(str, Enum):
    """ Enum to represent BarInterval """
    ONE_MINUTE = "ONE_MINUTE"
    FIVE_MINUTE = "FIVE_MINUTE"
    FIFTEEN_MINUTE = "FIFTEEN_MINUTE"
    THIRTY_MINUTE = "THIRTY_MINUTE"
    SIXTY_MINUTE = "SIXTY_MINUTE"
    ONE_DAY = "ONE_DAY"

    def getMinutes(self) -> int:
        if self == BarInterval.ONE_MINUTE:
            return 1
        elif self == BarInterval.FIVE_MINUTE:
            return 5
        elif self == BarInterval.FIFTEEN_MINUTE:
            return 15
        elif self == BarInterval.THIRTY_MINUTE:
            return 30
        elif self == BarInterval.SIXTY_MINUTE:
            return 60
        else:
            return 24 * 60



Bar = TypedDict("Bar", {"symbol": str,
                        "barinterval": BarInterval,
                        "date": datetime,
                        "open": float,
                        "close": float,
                        "high": float,
                        "low": float,
                        "volume": int
                        })

@dataclass
class StockNews:
    date: datetime
    title: str
    description: str


class NoDataException(Exception):
    def __init__(self,  dataParams: Dict[str, Any]):
        self.message = f"Data Not Available: {dataParams}"

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return self.message
