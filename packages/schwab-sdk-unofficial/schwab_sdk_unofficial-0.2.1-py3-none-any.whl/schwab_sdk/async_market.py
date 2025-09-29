"""
Schwab SDK - Async Market Module
Asynchronous market data endpoints.
"""

from typing import Optional, Dict, Any, List


class AsyncMarket:
    """
    Async Market module for Schwab SDK.
    
    Provides async access to market data endpoints:
    - get_quote() - Get quote for symbol
    - get_quotes() - Get quotes for multiple symbols
    - get_movers() - Get market movers
    - get_option_chain() - Get option chain
    - get_expiration_chain() - Get expiration dates
    - get_markets() - Get market hours
    - get_market_hours() - Get market hours for date
    """
    
    def __init__(self, client):
        """Initialize with async client."""
        self.client = client
        self.base_url = self.client.market_base_url
    
    async def get_quote(self, symbol: str) -> Dict[str, Any]:
        """
        Get quote for a single symbol.
        
        Args:
            symbol: Stock symbol
            
        Returns:
            Quote data
        """
        return await self.client._make_request(
            method="GET",
            url=f"{self.base_url}/quotes",
            params={'symbol': symbol}
        )
    
    async def get_quotes(self, symbols: List[str]) -> Dict[str, Any]:
        """
        Get quotes for multiple symbols.
        
        Args:
            symbols: List of stock symbols
            
        Returns:
            Quotes data
        """
        return await self.client._make_request(
            method="GET",
            url=f"{self.base_url}/quotes",
            params={'symbol': ','.join(symbols)}
        )
    
    async def get_movers(
        self,
        symbol_id: str,
        sort: Optional[str] = None,
        frequency: Optional[int] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Get market movers.
        
        Args:
            symbol_id: Market identifier (e.g., '$DJI', '$SPX.X')
            sort: Sort field (e.g., 'PERCENT_CHANGE', 'VOLUME')
            frequency: Update frequency in minutes
            params: Additional parameters
            
        Returns:
            Market movers data
        """
        request_params = {}
        if sort:
            request_params['sort'] = sort
        if frequency:
            request_params['frequency'] = frequency
        if params:
            request_params.update(params)
            
        return await self.client._make_request(
            method="GET",
            url=f"{self.base_url}/movers/{symbol_id}",
            params=request_params
        )
    
    async def get_option_chain(
        self,
        symbol: str,
        contract_type: Optional[str] = None,
        strike_count: Optional[int] = None,
        include_underlying_quote: Optional[bool] = None,
        strategy: Optional[str] = None,
        interval: Optional[float] = None,
        strike: Optional[float] = None,
        range: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        volatility: Optional[float] = None,
        underlying_price: Optional[float] = None,
        interest_rate: Optional[float] = None,
        days_to_expiration: Optional[int] = None,
        exp_month: Optional[str] = None,
        option_type: Optional[str] = None,
        entitlement: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Get option chain for a symbol.
        
        Args:
            symbol: Underlying symbol
            contract_type: CALL, PUT, or ALL
            strike_count: Number of strikes above/below ATM
            include_underlying_quote: Include underlying quote
            strategy: Option strategy (SINGLE, ANALYTICAL, etc.)
            interval: Strike interval for spread strategies
            strike: Strike price
            range: ITM/NTM/OTM range
            from_date: From date (YYYY-MM-DD)
            to_date: To date (YYYY-MM-DD)
            volatility: Volatility for calculations
            underlying_price: Underlying price for calculations
            interest_rate: Interest rate for calculations
            days_to_expiration: Days to expiration for calculations
            exp_month: Expiration month (JAN, FEB, etc.)
            option_type: Option type
            entitlement: Client entitlement (PN, NP, PP)
            params: Additional parameters
            
        Returns:
            Option chain data
        """
        # Date normalization
        def _norm_date_only(val: Optional[str]) -> Optional[str]:
            if not val:
                return None
            s = str(val).strip()
            if "T" in s and len(s) >= 10:
                return s[:10]
            return s

        request_params = {}
        if contract_type:
            request_params['contractType'] = contract_type
        if strike_count:
            request_params['strikeCount'] = strike_count
        if include_underlying_quote is not None:
            request_params['includeUnderlyingQuote'] = include_underlying_quote
        if strategy:
            request_params['strategy'] = strategy
        if interval:
            request_params['interval'] = interval
        if strike:
            request_params['strike'] = strike
        if range:
            request_params['range'] = range
        if from_date:
            request_params['fromDate'] = _norm_date_only(from_date)
        if to_date:
            request_params['toDate'] = _norm_date_only(to_date)
        if volatility:
            request_params['volatility'] = volatility
        if underlying_price:
            request_params['underlyingPrice'] = underlying_price
        if interest_rate:
            request_params['interestRate'] = interest_rate
        if days_to_expiration:
            request_params['daysToExpiration'] = days_to_expiration
        if exp_month:
            request_params['expMonth'] = exp_month
        if option_type:
            request_params['optionType'] = option_type
        if entitlement:
            request_params['entitlement'] = entitlement
        if params:
            request_params.update(params)
            
        return await self.client._make_request(
            method="GET",
            url=f"{self.base_url}/chains",
            params=request_params
        )
    
    async def get_expiration_chain(
        self,
        symbol: str,
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Get expiration dates for option chain.
        
        Args:
            symbol: Underlying symbol
            params: Additional parameters
            
        Returns:
            Expiration chain data
        """
        request_params = {}
        if params:
            request_params.update(params)
            
        return await self.client._make_request(
            method="GET",
            url=f"{self.base_url}/expirationchain",
            params=request_params
        )
    
    async def get_markets(self, date: Optional[str] = None) -> Dict[str, Any]:
        """
        Get market hours.
        
        Args:
            date: Date for market hours (YYYY-MM-DD)
            
        Returns:
            Market hours data
        """
        # Date normalization
        def _norm_date_only(val: Optional[str]) -> Optional[str]:
            if not val:
                return None
            s = str(val).strip()
            if "T" in s and len(s) >= 10:
                return s[:10]
            return s

        params = {}
        if date:
            params['date'] = _norm_date_only(date)
            
        return await self.client._make_request(
            method="GET",
            url=f"{self.base_url}/markets",
            params=params
        )
    
    async def get_market_hours(self, date: Optional[str] = None) -> Dict[str, Any]:
        """
        Get market hours for specific date.
        
        Args:
            date: Date for market hours (YYYY-MM-DD)
            
        Returns:
            Market hours data
        """
        # Date normalization
        def _norm_date_only(val: Optional[str]) -> Optional[str]:
            if not val:
                return None
            s = str(val).strip()
            if "T" in s and len(s) >= 10:
                return s[:10]
            return s

        params = {}
        if date:
            params['date'] = _norm_date_only(date)
            
        return await self.client._make_request(
            method="GET",
            url=f"{self.base_url}/marketHours",
            params=params
        )
