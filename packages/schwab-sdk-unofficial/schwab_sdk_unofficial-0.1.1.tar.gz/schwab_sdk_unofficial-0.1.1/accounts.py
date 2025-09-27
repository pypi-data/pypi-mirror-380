"""
Schwab SDK - Accounts Module
Maneja endpoints de cuentas, transacciones y preferencias de usuario.
"""

import requests
from typing import Optional, Dict, Any, List
from urllib.parse import urlencode


class Accounts:
    """
    Módulo para endpoints relacionados con cuentas.
    
    Incluye:
    - Información de cuentas (números, balances, posiciones)
    - Transacciones
    - Preferencias de usuario
    """
    
    def __init__(self, client):
        """
        Inicializa el módulo Accounts.
        
        Args:
            client: Instancia del cliente principal
        """
        self.client = client
        self.base_url = client.trader_base_url
    
    def get_account_numbers(self) -> Dict[str, Any]:
        """
        Obtiene lista de números de cuenta y sus valores encriptados.
        
        GET /accounts/accountNumbers
        
        Returns:
            Respuesta JSON con accountNumber y accountHash para cada cuenta
        """
        endpoint = f"{self.base_url}/accounts/accountNumbers"
        response = self.client._request("GET", endpoint, timeout=10)
        response.raise_for_status()
        return response.json()
    
    def get_accounts(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Obtiene balances y posiciones para todas las cuentas vinculadas.
        
        GET /accounts
        
        Returns:
            Respuesta JSON con información completa de todas las cuentas
        """
        endpoint = f"{self.base_url}/accounts"
        response = self.client._request("GET", endpoint, params=params or {}, timeout=10)
        response.raise_for_status()
        return response.json()
    
    def get_account_by_id(self, account_hash: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Obtiene balance y posiciones para una cuenta específica.
        
        GET /accounts/{accountNumber}
        
        Args:
            account_hash: Identificador cifrado de la cuenta (hashValue)
            
        Returns:
            Respuesta JSON con información de la cuenta específica
        """
        endpoint = f"{self.base_url}/accounts/{account_hash}"
        response = self.client._request("GET", endpoint, params=params or {}, timeout=10)
        response.raise_for_status()
        return response.json()
    
    def find_account(self, last_4_digits: str) -> Optional[Dict[str, Any]]:
        """
        Busca una cuenta por los últimos 4 dígitos del número de cuenta.
        
        Método helper que obtiene todas las cuentas y filtra por los últimos 4 dígitos.
        
        Args:
            last_4_digits: Últimos 4 dígitos del número de cuenta
            
        Returns:
            Información de la cuenta encontrada o None si no se encuentra
        """
        # Obtener números de cuenta
        account_numbers = self.get_account_numbers()
        # Buscar cuenta que termine en los dígitos especificados
        for account_info in account_numbers:
            account_number = account_info.get("accountNumber", "")
            if account_number.endswith(last_4_digits):
                # Obtener información completa de esta cuenta
                account_hash = account_info.get("hashValue", account_number)
                return self.get_account_by_id(account_hash)
        return None
    
    def get_transactions(self, account_hash: str, from_date: str = None, to_date: str = None, filters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Obtiene todas las transacciones para una cuenta específica.
        
        GET /accounts/{accountNumber}/transactions
        
        Args:
            account_hash: Identificador cifrado de la cuenta (hashValue)
            from_date: Fecha inicio en formato corto 'YYYY-MM-DD' o ISO UTC 'YYYY-MM-DDTHH:MM:SS.ffffffZ'
            to_date: Fecha fin en formato corto 'YYYY-MM-DD' o ISO UTC 'YYYY-MM-DDTHH:MM:SS.ffffffZ'
            filters: Filtros opcionales adicionales para la consulta
            
        Returns:
            Respuesta JSON con transacciones de la cuenta
        """
        endpoint = f"{self.base_url}/accounts/{account_hash}/transactions"
        # Construir parámetros de consulta (acepta 'YYYY-MM-DD' o ISO UTC completo)
        params: Dict[str, Any] = {}

        def _normalize_date(date_str: Optional[str], *, is_end: bool) -> Optional[str]:
            """Normaliza fechas:
            - 'YYYY-MM-DD' -> 'YYYY-MM-DDT00:00:00.000Z' (inicio) o 'YYYY-MM-DDT23:59:59.000Z' (fin)
            - ISO existente -> se pasa tal cual
            """
            if not date_str:
                return None
            ds = str(date_str).strip()
            # Formato corto YYYY-MM-DD
            import re
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", ds):
                return f"{ds}T23:59:59.000Z" if is_end else f"{ds}T00:00:00.000Z"
            # Si parece ISO, devolver tal cual
            return ds

        start_norm = _normalize_date(from_date, is_end=False) if from_date else None
        end_norm = _normalize_date(to_date, is_end=True) if to_date else None

        # Si solo una fecha es provista, completar la otra con el mismo día
        if start_norm and not end_norm:
            # Derivar fecha base del start
            import re as _re
            m = _re.match(r"(\d{4}-\d{2}-\d{2})", start_norm)
            base = m.group(1) if m else start_norm[:10]
            end_norm = f"{base}T23:59:59.000Z"
        elif end_norm and not start_norm:
            import re as _re
            m = _re.match(r"(\d{4}-\d{2}-\d{2})", end_norm)
            base = m.group(1) if m else end_norm[:10]
            start_norm = f"{base}T00:00:00.000Z"

        if start_norm:
            params['startDate'] = start_norm
        if end_norm:
            params['endDate'] = end_norm
        if filters:
            params.update(filters)
        response = self.client._request("GET", endpoint, params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    
    def get_transaction(self, account_hash: str, transaction_id: str) -> Dict[str, Any]:
        """
        Obtiene información específica de una transacción.
        
        GET /accounts/{accountNumber}/transactions/{transactionId}
        
        Args:
            account_hash: Identificador cifrado de la cuenta (hashValue)
            transaction_id: ID de la transacción específica
            
        Returns:
            Respuesta JSON con información de la transacción específica
        """
        endpoint = f"{self.base_url}/accounts/{account_hash}/transactions/{transaction_id}"
        response = self.client._request("GET", endpoint, timeout=10)
        response.raise_for_status()
        return response.json()
    
    def get_user_preferences(self) -> Dict[str, Any]:
        """
        Obtiene información de preferencias del usuario autenticado.
        
        GET /userPreference
        
        Esta información incluye datos necesarios para streaming como:
        - schwabClientCustomerId
        - schwabClientCorrelId
        - SchwabClientChannel
        - SchwabClientFunctionId
        
        Returns:
            Respuesta JSON con preferencias del usuario
        """
        endpoint = f"{self.base_url}/userPreference"
        response = self.client._request("GET", endpoint, timeout=10)
        response.raise_for_status()
        return response.json()
