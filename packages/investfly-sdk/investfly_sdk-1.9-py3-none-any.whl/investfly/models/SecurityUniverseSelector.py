from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from numbers import Number
from typing import List, Dict, Any, Set, cast

from investfly.models.MarketData import SecurityType, Security
from investfly.models.MarketDataIds import FinancialField


class StandardSymbolsList(str, Enum):
    # Stock lists
    SP_100 = "SP_100"
    SP_500 = "SP_500"
    NASDAQ_100 = "NASDAQ_100"
    NASDAQ_COMPOSITE = "NASDAQ_COMPOSITE"
    RUSSELL_1000 = "RUSSELL_1000"
    RUSSELL_2000 = "RUSSELL_2000"
    DOW_JONES_INDUSTRIALS = "DOW_JONES_INDUSTRIALS"
    
    # General lists
    STOCKS = "STOCKS"
    ETFS = "ETFS"

    ALL_CRYPTO = "ALL_CRYPTO"
    USD_CRYPTO = "USD_CRYPTO"

    # Forex lists
    ALL_FOREX = "ALL_FOREX"

    @property
    def securityType(self) -> SecurityType:
        # Map each enum value to its corresponding security type
        security_type_map = {
            "SP_100": SecurityType.STOCK,
            "SP_500": SecurityType.STOCK,
            "NASDAQ_100": SecurityType.STOCK,
            "NASDAQ_COMPOSITE": SecurityType.STOCK,
            "RUSSELL_1000": SecurityType.STOCK,
            "RUSSELL_2000": SecurityType.STOCK,
            "DOW_JONES_INDUSTRIALS": SecurityType.STOCK,
            "STOCKS": SecurityType.STOCK,
            "ETFS": SecurityType.STOCK,
            "ALL_CRYPTO": SecurityType.CRYPTO,
            "USD_CRYPTO": SecurityType.CRYPTO,
            "ALL_FOREX": SecurityType.FOREX
        }
        return security_type_map[self.value]

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class CustomSecurityList:
    def __init__(self):
        self.symbols: List[str] = []

    def addSymbol(self, symbol: str) -> None:
        self.symbols.append(symbol)

    @staticmethod
    def fromJson(json_dict: Dict[str, Any]) -> CustomSecurityList:
        securityList = CustomSecurityList()
        securityList.symbols = json_dict['symbols']
        return securityList

    def toDict(self) -> Dict[str, Any]:
        return self.__dict__.copy()

    def validate(self) -> None:
        if len(self.symbols) == 0:
            raise Exception("CustomSecurityList.symbols: At least one symbol is required")


class SecurityUniverseType(str, Enum):
    STANDARD_LIST = "STANDARD_LIST",
    CUSTOM_LIST = "CUSTOM_LIST",
    FUNDAMENTAL_QUERY = "FUNDAMENTAL_QUERY"


class ComparisonOperator(str, Enum):
    GREATER_THAN = ">"
    LESS_THAN = "<"
    GREATER_OR_EQUAL = ">="
    LESS_OR_EQUAL = "<="
    EQUAL_TO = "=="


@dataclass
class FinancialCondition:
    financialField: FinancialField
    operator: ComparisonOperator
    value: str | FinancialField

    @staticmethod
    def fromDict(json_dict: Dict[str, Any]) -> FinancialCondition:
        financialField = FinancialField[json_dict['financialField']]
        operator = ComparisonOperator[json_dict['operator']]
        valueFromJson = json_dict['value']
        allFinancialFields = [cast(FinancialField, f).name for f in FinancialField]
        if valueFromJson is allFinancialFields:
            value = FinancialField[valueFromJson]
        else:
            value = valueFromJson

        return FinancialCondition(financialField, operator, value)

    def toDict(self) -> Dict[str, Any]:
        return self.__dict__.copy()

    def validate(self) -> None:
        if not isinstance(self.financialField, FinancialField):
            raise Exception("Left expression in financial query must be of type FinancialField")
        if not isinstance(self.value, FinancialField) and not isinstance(self.value, str):
            raise Exception("Right expression in financial query must of type Financial Field or string")
        if isinstance(self.value, str):
            # it must represent a number
            valueStr = self.value
            if valueStr.endswith("K") or valueStr.endswith("M") or valueStr.endswith("B"):
                valueStr = valueStr[:-1]
                if not valueStr.replace('.', '', 1).isdigit():
                    raise Exception(f"Right expression offFinancial query must be a number or Financial Field. You provided: {self.value}")



class FinancialQuery:
    def __init__(self) -> None:
        self.queryConditions: List[FinancialCondition] = []
        self.sectors: Set[str] = set()

    def addCondition(self, condition: FinancialCondition) -> None:
        self.queryConditions.append(condition)
    
    def addSector(self, sector: str) -> None:
        self.sectors.add(sector)

    @staticmethod
    def fromDict(json_dict: Dict[str, Any]) -> FinancialQuery:
        financialQuery = FinancialQuery()
        conditionsList = json_dict['queryConditions']
        for cond in conditionsList:
            financialQuery.queryConditions.append(FinancialCondition.fromDict(cond))
        if 'sectors' in json_dict:
            financialQuery.sectors = set(json_dict['sectors'])
        return financialQuery

    def toDict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {'queryConditions': [q.toDict() for q in self.queryConditions]}
        if self.sectors:
            result['sectors'] = [sector for sector in self.sectors]
        return result

    def validate(self) -> None:
        if len(self.queryConditions) == 0:
            raise Exception("FinancialQuery must have at least one criteria")
        for f in self.queryConditions:
            f.validate()



@dataclass
class SecurityUniverseSelector:
    """
    This class is used to specify the set of stocks to use in trading strategy.
    You can pick one of the standard list (e.g SP100) that we provide, provide your own list with comma separated symbols list,
    or provide a query based on fundamental metrics like MarketCap, PE Ratio etc.
    """

    securityType: SecurityType
    """The security type for the universe selector"""

    universeType: SecurityUniverseType
    """The approach used to specify the stocks. Depending on the universeType, one of the attribute below must be specified"""

    standardList: StandardSymbolsList | None = None
    "Standard Symbol List (i.e SP500, SP100). Required if `universeType` is set to `STANDARD_LIST`"

    customList: CustomSecurityList | None = None
    financialQuery: FinancialQuery | None = None

    @staticmethod
    def getValidSymbolLists(securityType: SecurityType) -> List[StandardSymbolsList]:
        if securityType == SecurityType.CRYPTO:
            return [StandardSymbolsList.USD_CRYPTO]
        elif securityType == SecurityType.FOREX:
            return [StandardSymbolsList.ALL_FOREX]
        else:
            # For STOCK and other types, return only STOCK security type lists except STOCKS
            return [symbol_list for symbol_list in StandardSymbolsList 
                    if symbol_list.securityType == SecurityType.STOCK and symbol_list != StandardSymbolsList.STOCKS]

    @staticmethod
    def fromDict(json_dict: Dict[str, Any]) -> SecurityUniverseSelector:
        securityType = SecurityType[json_dict['securityType']]
        universeType = SecurityUniverseType[json_dict['universeType']]
        standardList = None
        if 'standardList' in json_dict:
            list_name = json_dict['standardList']
            standardList = StandardSymbolsList(list_name)
        customList = CustomSecurityList.fromJson(json_dict['customList']) if 'customList' in json_dict else None
        fundamentalQuery = FinancialQuery.fromDict(json_dict['financialQuery']) if 'financialQuery' in json_dict else None
        
        return SecurityUniverseSelector(securityType, universeType, standardList, customList, cast(FinancialQuery, fundamentalQuery))

    def toDict(self) -> Dict[str, Any]:
        jsonDict: Dict[str, Any] = {
            'securityType': self.securityType.value,
            'universeType': self.universeType.value
        }
        if self.standardList is not None:
            jsonDict["standardList"] = self.standardList.value
        if self.customList is not None:
            jsonDict['customList'] = self.customList.toDict()
        if self.financialQuery is not None:
            jsonDict["financialQuery"] = self.financialQuery.toDict()
        return jsonDict

    @staticmethod
    def singleStock(symbol: str) -> SecurityUniverseSelector:
        scopeType = SecurityUniverseType.CUSTOM_LIST
        customList = CustomSecurityList()
        customList.addSymbol(symbol)
        return SecurityUniverseSelector(SecurityType.STOCK, scopeType, customList=customList)

    @staticmethod
    def fromSecurity(security: Security) -> SecurityUniverseSelector:
        scopeType = SecurityUniverseType.CUSTOM_LIST
        customList = CustomSecurityList()
        customList.addSymbol(security.symbol)
        return SecurityUniverseSelector(security.securityType, scopeType, customList=customList)

    @staticmethod
    def fromSymbols(securityType: SecurityType, symbols: List[str]) -> SecurityUniverseSelector:
        scopeType = SecurityUniverseType.CUSTOM_LIST
        customList = CustomSecurityList()
        customList.symbols = symbols
        return SecurityUniverseSelector(SecurityType.STOCK, scopeType, customList=customList)

    @staticmethod
    def fromStandardList(standardListName: StandardSymbolsList) -> SecurityUniverseSelector:
        return SecurityUniverseSelector(standardListName.securityType, SecurityUniverseType.STANDARD_LIST, standardList=standardListName)

    @staticmethod
    def fromFinancialQuery(financialQuery: FinancialQuery) -> SecurityUniverseSelector:
        universeType = SecurityUniverseType.FUNDAMENTAL_QUERY
        return SecurityUniverseSelector(SecurityType.STOCK, universeType, financialQuery=financialQuery)


    def validate(self) -> None:
        # Note - Python should have exact code to validate SecurityUniverseSelector because custom strategy also return SecurityUniverseSelector
        # Technically, we could avoid duplicate validation here, but we keep it here to avoid sending network call to Python server to fail fast

        # Validate securityType is not null
        if self.securityType is None:
            raise Exception("SecurityUniverseSelector.securityType is required")
        
        # Validate securityType is one of STOCK, CRYPTO, or FOREX
        if self.securityType not in (SecurityType.STOCK, SecurityType.CRYPTO, SecurityType.FOREX):
            raise Exception(f"SecurityUniverseSelector.securityType must be one of STOCK, CRYPTO, or FOREX, not {self.securityType}")
        
        # Validate universeType is not null
        if self.universeType is None:
            raise Exception("SecurityUniverseSelector.universeType is required")
        
        # For CRYPTO, ETF, CURRENCY - only STANDARD_LIST and CUSTOM_LIST are valid
        if self.securityType != SecurityType.STOCK and self.universeType == SecurityUniverseType.FUNDAMENTAL_QUERY:
            raise Exception(f"FUNDAMENTAL_QUERY universe type is only valid for SecurityType.STOCK, not for {self.securityType}")
        
        if self.universeType == SecurityUniverseType.STANDARD_LIST:
            if self.standardList is None:
                raise Exception("SecurityUniverseSelector.standardList is required for StandardList UniverseType")
            
            # If using STANDARD_LIST, StandardSymbolsList.security_type must match securityType
            if self.standardList.securityType != self.securityType:
                raise Exception(f"StandardSymbolsList security type ({self.standardList.securityType}) must match SecurityUniverseSelector security type ({self.securityType})")
            
            # Validate that the standardList is allowed for the given securityType
            validLists = self.getValidSymbolLists(self.securityType)
            if self.standardList not in validLists:
                raise Exception(f"StandardSymbolsList ({self.standardList}) is not valid for SecurityType ({self.securityType}). Valid lists are: {validLists}")
                
        elif self.universeType == SecurityUniverseType.CUSTOM_LIST:
            if self.customList is None:
                raise Exception("SecurityUniverseSelector.customList is required for CustomList UniverseType")
            self.customList.validate()
            
        elif self.universeType == SecurityUniverseType.FUNDAMENTAL_QUERY:
            if self.financialQuery is None:
                raise Exception("SecurityUniverseSelector.fundamentalQuery is required for FUNDAMENTAL_QUERY UniverseType")
            self.financialQuery.validate()

