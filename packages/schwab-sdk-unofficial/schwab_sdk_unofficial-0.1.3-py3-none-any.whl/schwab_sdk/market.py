"""
Schwab SDK - Market Data Module
Handles all market data endpoints.
"""

import requests
from typing import Optional, Dict, Any, List, Union
from urllib.parse import urlencode


class Market:
    """
    Module for market data endpoints.
    
    Includes:
    - Quotes (single and multiple)
    - Option Chains
    - Price History
    - Movers
    - Market Hours
    - Instruments
    """
    
    def __init__(self, client):
        """
        Initializes the Market module.
        
        Args:
            client: Instance of the main client
        """
        self.client = client
        self.base_url = client.market_base_url
    
    # ===== QUOTES =====
    
    def get_quotes(self, symbols: Union[str, List[str]], params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Retrieves quotes for multiple symbols.
        
        GET /quotes?symbols=...
        
        Args:
            symbols: Single symbol (str) or list of symbols (List[str])
            
        Returns:
            JSON response with quotes for the requested symbols
        """
        # Convert list to string if needed
        if isinstance(symbols, list):
            symbol_string = ",".join(symbols)
        else:
            symbol_string = symbols
        
        endpoint = f"{self.base_url}/quotes"
        query_params = {"symbols": symbol_string}
        if params:
            query_params.update(params)
        response = self.client._request("GET", endpoint, params=query_params, timeout=10)
        response.raise_for_status()
        return response.json()
    
    def get_quote(self, symbol: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Retrieves a quote for a specific symbol.
        
        GET /{symbol_id}/quotes
        
        Args:
            symbol: Instrument symbol (e.g., "AAPL")
            
        Returns:
            JSON response with the quote for the specific symbol
        """
        endpoint = f"{self.base_url}/{symbol}/quotes"
        response = self.client._request("GET", endpoint, params=params or {}, timeout=10)
        response.raise_for_status()
        return response.json()
    
    # ===== OPTION CHAINS =====
    
    def get_option_chain(self, symbol: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Retrieves an option chain for a symbol.
        
        GET /chains
        
        Args:
            symbol: Underlying asset symbol
            params: Optional parameters (contractType, strikeCount, strategy, etc.)
            
        Returns:
            JSON response with the option chain
        """
        endpoint = f"{self.base_url}/chains"
        # Required parameters
        query_params = {"symbol": symbol}
        # Add optional parameters
        if params:
            query_params.update(params)

        # Normalize fromDate/toDate (accepts 'YYYY-MM-DD' or trims date from ISO)
        def _norm_date_only(val: Optional[str]) -> Optional[str]:
            if not val:
                return None
            s = str(val).strip()
            # If ISO, trim to YYYY-MM-DD
            if "T" in s and len(s) >= 10:
                return s[:10]
            return s

        if "fromDate" in query_params:
            query_params["fromDate"] = _norm_date_only(query_params.get("fromDate"))
        if "toDate" in query_params:
            query_params["toDate"] = _norm_date_only(query_params.get("toDate"))
        response = self.client._request("GET", endpoint, params=query_params, timeout=15)
        response.raise_for_status()
        return response.json()
    
    def get_option_expiration_chain(self, symbol: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Retrieves the option expiration chain for a symbol.
        
        GET /expirationchain
        
        Args:
            symbol: Underlying asset symbol
            
        Returns:
            JSON response with option expiration dates
        """
        endpoint = f"{self.base_url}/expirationchain"
        query_params = {"symbol": symbol}
        if params:
            query_params.update(params)
        response = self.client._request("GET", endpoint, params=query_params, timeout=10)
        response.raise_for_status()
        return response.json()
    
    # ===== PRICE HISTORY =====
    
    def get_price_history(
        self, 
        symbol: str, 
        periodType: str = "month",
        period: int = 1,
        frequencyType: str = "daily", 
        frequency: int = 1,
        startDate: str = None,
        endDate: str = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Retrieves price history for a symbol.
        
        GET /pricehistory
        
        Args:
            symbol: Instrument symbol
            periodType: Period type (day, month, year, ytd)
            period: Number of periods
            frequencyType: Frequency type (minute, daily, weekly, monthly)
            frequency: Specific frequency
            startDate: Start date in milliseconds (optional)
            endDate: End date in milliseconds (optional)
            
        Returns:
            JSON response with price history (candles)
        """
        endpoint = f"{self.base_url}/pricehistory"
        # Required and optional parameters
        query_params = {
            "symbol": symbol,
            "periodType": periodType,
            "period": period,
            "frequencyType": frequencyType,
            "frequency": frequency
        }
        if startDate is not None:
            query_params["startDate"] = startDate
        if endDate is not None:
            query_params["endDate"] = endDate
        if params:
            query_params.update(params)
        response = self.client._request("GET", endpoint, params=query_params, timeout=15)
        response.raise_for_status()
        return response.json()
    
    # ===== MOVERS =====
    
    def get_movers(self, symbol_id: str, sort: Optional[str] = None, frequency: Optional[int] = None, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Retrieves movers for a specific index.
        
        GET /movers/{symbol_id}
        
        Args:
            symbol_id: Index Symbol (required). Available values: $DJI, $COMPX, $SPX, NYSE, NASDAQ, OTCBB, INDEX_ALL, EQUITY_ALL, OPTION_ALL, OPTION_PUT, OPTION_CALL
            sort: Sort by a particular attribute. Available values: VOLUME, TRADES, PERCENT_CHANGE_UP, PERCENT_CHANGE_DOWN
            frequency: To return movers with the specified directions of up or down. Available values: 0, 1, 5, 10, 30, 60. Default: 0
            params: Additional query parameters
            
        Returns:
            JSON response with the most active symbols of the index
        """
        endpoint = f"{self.base_url}/movers/{symbol_id}"
        
        # Construir parámetros de consulta
        query_params = {}
        if sort:
            query_params['sort'] = sort
        if frequency is not None:
            query_params['frequency'] = frequency
        if params:
            query_params.update(params)
        
        response = self.client._request("GET", endpoint, params=query_params, timeout=10)
        response.raise_for_status()
        return response.json()
    
    # ===== MARKET HOURS =====
    
    def get_markets(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Retrieves hours for different markets.
        
        GET /markets
        
        Returns:
            JSON response with hours for all markets
        """
        endpoint = f"{self.base_url}/markets"
        query_params = dict(params or {})

        # Normalize 'date' (accepts 'YYYY-MM-DD' or ISO -> YYYY-MM-DD)
        if "date" in query_params and query_params["date"]:
            s = str(query_params["date"]).strip()
            if "T" in s and len(s) >= 10:
                query_params["date"] = s[:10]

        response = self.client._request("GET", endpoint, params=query_params, timeout=10)
        response.raise_for_status()
        return response.json()
    
    def get_market_hours(self, market_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Retrieves hours for a specific market.
        
        GET /markets/{market_id}
        
        Args:
            market_id: Market ID (e.g., "equity", "option", "bond", "forex")
            
        Returns:
            JSON response with hours for the specific market
        """
        endpoint = f"{self.base_url}/markets/{market_id}"
        query_params = dict(params or {})
        if "date" in query_params and query_params["date"]:
            s = str(query_params["date"]).strip()
            if "T" in s and len(s) >= 10:
                query_params["date"] = s[:10]

        response = self.client._request("GET", endpoint, params=query_params, timeout=10)
        response.raise_for_status()
        return response.json()
    
    # ===== INSTRUMENTS =====
    
    def get_instruments(
        self, 
        symbols: Union[str, List[str]], 
        projection: Optional[str] = None,
        extra_params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Retrieves instruments by symbols and projection.
        
        GET /instruments
        
        Args:
            symbols: Single symbol or list of symbols
            projection: Projection type ("symbol-search", "symbol-regex", "desc-search", "desc-regex", "cusip")
            
        Returns:
            JSON response with instrument information
        """
        endpoint = f"{self.base_url}/instruments"
        # Convert list to string if needed
        if isinstance(symbols, list):
            symbol_string = ",".join(symbols)
        else:
            symbol_string = symbols
        params = {"symbols": symbol_string}
        # Add projection if specified
        if projection:
            params["projection"] = projection
        if extra_params:
            params.update(extra_params)
        response = self.client._request("GET", endpoint, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    
    def get_instrument_by_cusip(self, cusip_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Retrieves an instrument by specific CUSIP.
        
        GET /instruments/{cusip_id}
        
        Args:
            cusip_id: Instrument CUSIP
            
        Returns:
            JSON response with the specific instrument information
        """
        endpoint = f"{self.base_url}/instruments/{cusip_id}"
        response = self.client._request("GET", endpoint, params=params or {}, timeout=10)
        response.raise_for_status()
        return response.json()
