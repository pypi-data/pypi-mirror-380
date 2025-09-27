"""
Schwab SDK - Market Data Module
Maneja todos los endpoints de datos de mercado.
"""

import requests
from typing import Optional, Dict, Any, List, Union
from urllib.parse import urlencode


class Market:
    """
    Módulo para endpoints de datos de mercado.
    
    Incluye:
    - Quotes (cotizaciones individuales y múltiples)
    - Option Chains (cadenas de opciones)
    - Price History (historial de precios)
    - Movers (valores en movimiento)
    - Market Hours (horarios de mercado)
    - Instruments (instrumentos financieros)
    """
    
    def __init__(self, client):
        """
        Inicializa el módulo Market.
        
        Args:
            client: Instancia del cliente principal
        """
        self.client = client
        self.base_url = client.market_base_url
    
    # ===== QUOTES =====
    
    def get_quotes(self, symbols: Union[str, List[str]], params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Obtiene cotizaciones para múltiples símbolos.
        
        GET /quotes?symbols=...
        
        Args:
            symbols: Símbolo único (str) o lista de símbolos (List[str])
            
        Returns:
            Respuesta JSON con cotizaciones de los símbolos solicitados
        """
        # Convertir lista a string si es necesario
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
        Obtiene cotización para un símbolo específico.
        
        GET /{symbol_id}/quotes
        
        Args:
            symbol: Símbolo del instrumento (ej: "AAPL")
            
        Returns:
            Respuesta JSON con cotización del símbolo específico
        """
        endpoint = f"{self.base_url}/{symbol}/quotes"
        response = self.client._request("GET", endpoint, params=params or {}, timeout=10)
        response.raise_for_status()
        return response.json()
    
    # ===== OPTION CHAINS =====
    
    def get_option_chain(self, symbol: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Obtiene cadena de opciones para un símbolo.
        
        GET /chains
        
        Args:
            symbol: Símbolo del activo subyacente
            params: Parámetros opcionales (contractType, strikeCount, strategy, etc.)
            
        Returns:
            Respuesta JSON con cadena de opciones
        """
        endpoint = f"{self.base_url}/chains"
        # Parámetros requeridos
        query_params = {"symbol": symbol}
        # Agregar parámetros opcionales
        if params:
            query_params.update(params)

        # Normalizar fechas fromDate/toDate (acepta 'YYYY-MM-DD' o extrae fecha de ISO)
        def _norm_date_only(val: Optional[str]) -> Optional[str]:
            if not val:
                return None
            s = str(val).strip()
            # Si viene ISO, recortar a YYYY-MM-DD
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
        Obtiene cadena de vencimientos de opciones para un símbolo.
        
        GET /expirationchain
        
        Args:
            symbol: Símbolo del activo subyacente
            
        Returns:
            Respuesta JSON con fechas de vencimiento de opciones
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
        Obtiene historial de precios para un símbolo.
        
        GET /pricehistory
        
        Args:
            symbol: Símbolo del instrumento
            periodType: Tipo de periodo (day, month, year, ytd)
            period: Número de periodos
            frequencyType: Tipo de frecuencia (minute, daily, weekly, monthly)
            frequency: Frecuencia específica
            startDate: Fecha inicio en milisegundos (opcional)
            endDate: Fecha fin en milisegundos (opcional)
            
        Returns:
            Respuesta JSON con historial de precios (velas/candles)
        """
        endpoint = f"{self.base_url}/pricehistory"
        # Parámetros requeridos y opcionales
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
    
    def get_movers(self, symbol_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Obtiene valores en movimiento para un índice específico.
        
        GET /movers/{symbol_id}
        
        Args:
            symbol_id: ID del índice (ej: "$DJI", "$COMPX", "$SPX")
            
        Returns:
            Respuesta JSON con valores más activos del índice
        """
        endpoint = f"{self.base_url}/movers/{symbol_id}"
        response = self.client._request("GET", endpoint, params=params or {}, timeout=10)
        response.raise_for_status()
        return response.json()
    
    # ===== MARKET HOURS =====
    
    def get_markets(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Obtiene horarios para diferentes mercados.
        
        GET /markets
        
        Returns:
            Respuesta JSON con horarios de todos los mercados
        """
        endpoint = f"{self.base_url}/markets"
        query_params = dict(params or {})

        # Normalizar 'date' (acepta 'YYYY-MM-DD' o ISO -> YYYY-MM-DD)
        if "date" in query_params and query_params["date"]:
            s = str(query_params["date"]).strip()
            if "T" in s and len(s) >= 10:
                query_params["date"] = s[:10]

        response = self.client._request("GET", endpoint, params=query_params, timeout=10)
        response.raise_for_status()
        return response.json()
    
    def get_market_hours(self, market_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Obtiene horarios para un mercado específico.
        
        GET /markets/{market_id}
        
        Args:
            market_id: ID del mercado (ej: "equity", "option", "bond", "forex")
            
        Returns:
            Respuesta JSON con horarios del mercado específico
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
        Obtiene instrumentos por símbolos y proyección.
        
        GET /instruments
        
        Args:
            symbols: Símbolo único o lista de símbolos
            projection: Tipo de proyección ("symbol-search", "symbol-regex", "desc-search", "desc-regex", "cusip")
            
        Returns:
            Respuesta JSON con información de instrumentos
        """
        endpoint = f"{self.base_url}/instruments"
        # Convertir lista a string si es necesario
        if isinstance(symbols, list):
            symbol_string = ",".join(symbols)
        else:
            symbol_string = symbols
        params = {"symbols": symbol_string}
        # Agregar proyección si se especifica
        if projection:
            params["projection"] = projection
        if extra_params:
            params.update(extra_params)
        response = self.client._request("GET", endpoint, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    
    def get_instrument_by_cusip(self, cusip_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Obtiene instrumento por CUSIP específico.
        
        GET /instruments/{cusip_id}
        
        Args:
            cusip_id: CUSIP del instrumento
            
        Returns:
            Respuesta JSON con información del instrumento específico
        """
        endpoint = f"{self.base_url}/instruments/{cusip_id}"
        response = self.client._request("GET", endpoint, params=params or {}, timeout=10)
        response.raise_for_status()
        return response.json()
