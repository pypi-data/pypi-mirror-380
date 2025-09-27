"""
Schwab SDK - Orders Module
Maneja todos los endpoints relacionados con órdenes.
"""

import requests
from typing import Optional, Dict, Any
from urllib.parse import urlencode
from datetime import datetime, timedelta
import re


class Orders:
    """
    Módulo para endpoints relacionados con órdenes.
    
    Incluye funcionalidad para:
    - Obtener órdenes existentes
    - Colocar nuevas órdenes
    - Cancelar órdenes
    - Reemplazar órdenes
    - Preview de órdenes
    
    Todos los métodos que crean/modifican órdenes extraen el order_id
    del header Location y lo agregan a la respuesta JSON.
    """
    
    def __init__(self, client):
        """
        Inicializa el módulo Orders.
        
        Args:
            client: Instancia del cliente principal
        """
        self.client = client
        self.base_url = client.trader_base_url
        # Valores permitidos (case-insensitive) para el query param 'status'
        self._allowed_status_values = {
            "AWAITING_PARENT_ORDER",
            "AWAITING_CONDITION",
            "AWAITING_STOP_CONDITION",
            "AWAITING_MANUAL_REVIEW",
            "ACCEPTED",
            "AWAITING_UR_OUT",
            "PENDING_ACTIVATION",
            "QUEUED",
            "WORKING",
            "REJECTED",
            "PENDING_CANCEL",
            "CANCELED",
            "PENDING_REPLACE",
            "REPLACED",
            "FILLED",
            "EXPIRED",
            "NEW",
            "AWAITING_RELEASE_TIME",
            "PENDING_ACKNOWLEDGEMENT",
            "PENDING_RECALL",
            "UNKNOWN",
        }
    
    def get_orders(
        self,
        account_hash: str,
        from_entered_time: str = None,
        to_entered_time: str = None,
        status: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Obtiene todas las órdenes para una cuenta específica.
        
        GET /accounts/{accountNumber}/orders
        
        Args:
            account_hash: Identificador cifrado de la cuenta (hashValue)
            from_entered_time: Fecha desde la cual obtener órdenes (ISO format). Si no se especifica, usa 60 días atrás.
            to_entered_time: Fecha hasta la cual obtener órdenes (ISO format). Si no se especifica, usa fecha actual.
            
        Returns:
            Dict con metadatos HTTP completos + respuesta nativa:
            {
                'status_code': 200,
                'success': True,
                'headers': {...},
                'url': 'https://...',
                'elapsed_seconds': 0.5,
                'data': [...]  # Lista de órdenes nativa de Schwab
            }
        """
        # Normalización de fechas: acepta 'YYYY-MM-DD' o ISO completo.
        def _normalize_dt(dt: Optional[str], *, is_end: bool) -> Optional[str]:
            if not dt:
                return None
            s = str(dt).strip()
            import re as _re
            if _re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
                return f"{s}T23:59:59.000Z" if is_end else f"{s}T00:00:00.000Z"
            return s

        start_norm = _normalize_dt(from_entered_time, is_end=False) if from_entered_time else None
        end_norm = _normalize_dt(to_entered_time, is_end=True) if to_entered_time else None

        # Si ambas faltan, usar últimos 60 días por defecto
        if not start_norm and not end_norm:
            from datetime import datetime, timedelta
            to_date = datetime.now()
            from_date = to_date - timedelta(days=60)
            start_norm = from_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
            end_norm = to_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        # Si sólo una está presente, derivar la otra para el mismo día
        elif start_norm and not end_norm:
            import re as _re
            m = _re.search(r"(\d{4}-\d{2}-\d{2})", start_norm)
            base = m.group(1) if m else start_norm[:10]
            end_norm = f"{base}T23:59:59.000Z"
        elif end_norm and not start_norm:
            import re as _re
            m = _re.search(r"(\d{4}-\d{2}-\d{2})", end_norm)
            base = m.group(1) if m else end_norm[:10]
            start_norm = f"{base}T00:00:00.000Z"
        
        endpoint = f"{self.base_url}/accounts/{account_hash}/orders"
        # Agregar parámetros requeridos
        params = {
            'fromEnteredTime': start_norm,
            'toEnteredTime': end_norm,
        }
        if status:
            # Normalizar a mayúsculas (case-insensitive). No se fuerza validación estricta.
            norm_status = str(status).strip().upper()
            params['status'] = norm_status
        if max_results is not None:
            params['maxResults'] = max_results
        try:
            response = self.client._request("GET", endpoint, params=params, timeout=30)
            
            # Preparar respuesta con metadatos completos
            result = {
                'status_code': response.status_code,
                'success': 200 <= response.status_code < 300,
                'headers': dict(response.headers),
                'url': str(response.url),
                'elapsed_seconds': response.elapsed.total_seconds(),
                'method': 'GET',
                'params': params
            }
            
            # Procesar datos según el status
            if result['success']:
                try:
                    schwab_data = response.json()
                except:
                    schwab_data = []
                result['data'] = schwab_data
                
            else:
                # Manejar errores
                try:
                    error_data = response.json() if response.text else {}
                except:
                    error_data = {'error': response.text or 'No error details'}
                
                result['data'] = error_data
                result['error_message'] = f"{response.status_code} {response.reason} for url: {response.url}"
                
                # Lanzar excepción como antes para mantener compatibilidad
                response.raise_for_status()
            
            return result
            
        except requests.RequestException as e:
            # En caso de excepción, devolver metadatos del error
            return {
                'status_code': getattr(e.response, 'status_code', 0) if hasattr(e, 'response') else 0,
                'success': False,
                'headers': dict(getattr(e.response, 'headers', {})) if hasattr(e, 'response') else {},
                'url': str(getattr(e.response, 'url', endpoint)) if hasattr(e, 'response') else endpoint,
                'elapsed_seconds': 0,
                'method': 'GET',
                'params': params,
                'data': {'error': str(e)},
                'error_message': str(e)
            }
    
    def place_order(self, account_hash: str, order_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Coloca una nueva orden para una cuenta específica.
        
        POST /accounts/{accountNumber}/orders
        
        Args:
            account_hash: Identificador cifrado de la cuenta (hashValue)
            order_data: Datos de la orden en formato JSON
            
        Returns:
            Dict con metadatos HTTP completos + respuesta nativa + order_id:
            {
                'status_code': 201,
                'success': True,
                'headers': {...},
                'url': 'https://...',
                'elapsed_seconds': 0.5,
                'data': {...},  # Respuesta nativa de Schwab
                'order_id': '123456'
            }
        """
        endpoint = f"{self.base_url}/accounts/{account_hash}/orders"
        headers = {"Content-Type": "application/json"}
        try:
            response = self.client._request("POST", endpoint, json=order_data, headers=headers, timeout=15)
            
            # Preparar respuesta con metadatos completos
            result = {
                'status_code': response.status_code,
                'success': 200 <= response.status_code < 300,
                'headers': dict(response.headers),
                'url': str(response.url),
                'elapsed_seconds': response.elapsed.total_seconds(),
                'method': 'POST'
            }
            
            # Procesar datos según el status
            if result['success']:
                # Obtener respuesta JSON nativa de Schwab
                try:
                    schwab_data = response.json() if response.text else {}
                except:
                    schwab_data = {}
                
                result['data'] = schwab_data
                
                # Extraer order_id del header Location
                order_id = self._extract_order_id_from_location(response.headers.get("Location"))
                if order_id:
                    result['order_id'] = order_id
                
            else:
                # Manejar errores - incluir info del error
                try:
                    error_data = response.json() if response.text else {}
                except:
                    error_data = {'error': response.text or 'No error details'}
                
                result['data'] = error_data
                result['error_message'] = f"{response.status_code} {response.reason} for url: {response.url}"
                
                # Lanzar excepción como antes para mantener compatibilidad
                response.raise_for_status()
            
            return result
            
        except requests.RequestException as e:
            # En caso de excepción, devolver metadatos del error
            return {
                'status_code': getattr(e.response, 'status_code', 0) if hasattr(e, 'response') else 0,
                'success': False,
                'headers': dict(getattr(e.response, 'headers', {})) if hasattr(e, 'response') else {},
                'url': str(getattr(e.response, 'url', endpoint)) if hasattr(e, 'response') else endpoint,
                'elapsed_seconds': 0,
                'method': 'POST',
                'data': {'error': str(e)},
                'error_message': str(e)
            }
    
    def get_order(self, account_hash: str, order_id: str) -> Dict[str, Any]:
        """
        Obtiene una orden específica por su ID.
        
        GET /accounts/{accountNumber}/orders/{orderId}
        
        Args:
            account_hash: Identificador cifrado de la cuenta (hashValue)
            order_id: ID de la orden
            
        Returns:
            Dict con metadatos HTTP completos + respuesta nativa:
            {
                'status_code': 200,
                'success': True,
                'headers': {...},
                'url': 'https://...',
                'elapsed_seconds': 0.5,
                'data': {...}  # Información de la orden específica
            }
        """
        endpoint = f"{self.base_url}/accounts/{account_hash}/orders/{order_id}"
        try:
            response = self.client._request("GET", endpoint, timeout=10)
            
            # Preparar respuesta con metadatos completos
            result = {
                'status_code': response.status_code,
                'success': 200 <= response.status_code < 300,
                'headers': dict(response.headers),
                'url': str(response.url),
                'elapsed_seconds': response.elapsed.total_seconds(),
                'method': 'GET',
                'order_id': order_id
            }
            
            # Procesar datos según el status
            if result['success']:
                try:
                    schwab_data = response.json()
                except:
                    schwab_data = {}
                result['data'] = schwab_data
                
            else:
                # Manejar errores
                try:
                    error_data = response.json() if response.text else {}
                except:
                    error_data = {'error': response.text or 'No error details'}
                
                result['data'] = error_data
                result['error_message'] = f"{response.status_code} {response.reason} for url: {response.url}"
                
                # Lanzar excepción como antes para mantener compatibilidad
                response.raise_for_status()
            
            return result
            
        except requests.RequestException as e:
            # En caso de excepción, devolver metadatos del error
            return {
                'status_code': getattr(e.response, 'status_code', 0) if hasattr(e, 'response') else 0,
                'success': False,
                'headers': dict(getattr(e.response, 'headers', {})) if hasattr(e, 'response') else {},
                'url': str(getattr(e.response, 'url', endpoint)) if hasattr(e, 'response') else endpoint,
                'elapsed_seconds': 0,
                'method': 'GET',
                'order_id': order_id,
                'data': {'error': str(e)},
                'error_message': str(e)
            }
    
    def cancel_order(self, account_hash: str, order_id: str) -> Dict[str, Any]:
        """
        Cancela una orden específica.
        
        DELETE /accounts/{accountNumber}/orders/{orderId}
        
        Args:
            account_hash: Identificador cifrado de la cuenta (hashValue)
            order_id: ID de la orden a cancelar
            
        Returns:
            Dict con metadatos HTTP completos + respuesta nativa:
            {
                'status_code': 200,
                'success': True,
                'headers': {...},
                'url': 'https://...',
                'elapsed_seconds': 0.5,
                'data': {...},  # Respuesta nativa de Schwab
                'order_id': '123456'
            }
        """
        endpoint = f"{self.base_url}/accounts/{account_hash}/orders/{order_id}"
        try:
            response = self.client._request("DELETE", endpoint, timeout=10)
            
            # Preparar respuesta con metadatos completos
            result = {
                'status_code': response.status_code,
                'success': 200 <= response.status_code < 300,
                'headers': dict(response.headers),
                'url': str(response.url),
                'elapsed_seconds': response.elapsed.total_seconds(),
                'method': 'DELETE',
                'order_id': order_id
            }
            
            # Procesar datos según el status
            if result['success']:
                try:
                    schwab_data = response.json()
                except:
                    schwab_data = {}
                result['data'] = schwab_data
                # Intentar extraer order_id del header Location si está presente
                extracted_id = self._extract_order_id_from_location(response.headers.get("Location"))
                if extracted_id:
                    result['order_id'] = extracted_id
                
            else:
                # Manejar errores
                try:
                    error_data = response.json() if response.text else {}
                except:
                    error_data = {'error': response.text or 'No error details'}
                
                result['data'] = error_data
                result['error_message'] = f"{response.status_code} {response.reason} for url: {response.url}"
                
                # Lanzar excepción como antes para mantener compatibilidad
                response.raise_for_status()
            
            return result
            
        except requests.RequestException as e:
            # En caso de excepción, devolver metadatos del error
            return {
                'status_code': getattr(e.response, 'status_code', 0) if hasattr(e, 'response') else 0,
                'success': False,
                'headers': dict(getattr(e.response, 'headers', {})) if hasattr(e, 'response') else {},
                'url': str(getattr(e.response, 'url', endpoint)) if hasattr(e, 'response') else endpoint,
                'elapsed_seconds': 0,
                'method': 'DELETE',
                'order_id': order_id,
                'data': {'error': str(e)},
                'error_message': str(e)
            }
        
    def replace_order(self, account_hash: str, order_id: str, new_order_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reemplaza una orden existente con nueva información.
        
        PUT /accounts/{accountNumber}/orders/{orderId}
        
        Args:
            account_hash: Identificador cifrado de la cuenta (hashValue)
            order_id: ID de la orden a reemplazar
            new_order_data: Nuevos datos de la orden en formato JSON
            
        Returns:
            Dict con metadatos HTTP completos + respuesta nativa + order_id:
            {
                'status_code': 201,
                'success': True,
                'headers': {...},
                'url': 'https://...',
                'elapsed_seconds': 0.5,
                'data': {...},  # Respuesta nativa de Schwab
                'order_id': '123456'
            }
        """
        endpoint = f"{self.base_url}/accounts/{account_hash}/orders/{order_id}"
        headers = {"Content-Type": "application/json"}
        try:
            response = self.client._request("PUT", endpoint, json=new_order_data, headers=headers, timeout=15)
            
            # Preparar respuesta con metadatos completos
            result = {
                'status_code': response.status_code,
                'success': 200 <= response.status_code < 300,
                'headers': dict(response.headers),
                'url': str(response.url),
                'elapsed_seconds': response.elapsed.total_seconds(),
                'method': 'PUT',
                'original_order_id': order_id
            }
            
            # Procesar datos según el status
            if result['success']:
                # Obtener respuesta JSON nativa de Schwab
                try:
                    schwab_data = response.json() if response.text else {}
                except:
                    schwab_data = {}
                
                result['data'] = schwab_data
                
                # Extraer nuevo order_id del header Location
                new_order_id = self._extract_order_id_from_location(response.headers.get("Location"))
                if new_order_id:
                    result['order_id'] = new_order_id
                
            else:
                # Manejar errores
                try:
                    error_data = response.json() if response.text else {}
                except:
                    error_data = {'error': response.text or 'No error details'}
                
                result['data'] = error_data
                result['error_message'] = f"{response.status_code} {response.reason} for url: {response.url}"
                
                # Lanzar excepción como antes para mantener compatibilidad
                response.raise_for_status()
            
            return result
            
        except requests.RequestException as e:
            # En caso de excepción, devolver metadatos del error
            return {
                'status_code': getattr(e.response, 'status_code', 0) if hasattr(e, 'response') else 0,
                'success': False,
                'headers': dict(getattr(e.response, 'headers', {})) if hasattr(e, 'response') else {},
                'url': str(getattr(e.response, 'url', endpoint)) if hasattr(e, 'response') else endpoint,
                'elapsed_seconds': 0,
                'method': 'PUT',
                'original_order_id': order_id,
                'data': {'error': str(e)},
                'error_message': str(e)
            }
    
    def get_all_orders(
        self,
        from_entered_time: str = None,
        to_entered_time: str = None,
        status: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Obtiene todas las órdenes para todas las cuentas.
        
        GET /orders
        
        Args:
            from_entered_time: Fecha desde la cual obtener órdenes (ISO format). Si no se especifica, usa 60 días atrás.
            to_entered_time: Fecha hasta la cual obtener órdenes (ISO format). Si no se especifica, usa fecha actual.
        
        Returns:
            Dict con metadatos HTTP completos + respuesta nativa:
            {
                'status_code': 200,
                'success': True,
                'headers': {...},
                'url': 'https://...',
                'elapsed_seconds': 0.5,
                'data': [...]  # Órdenes de todas las cuentas
            }
        """
        # Normalización de fechas: acepta 'YYYY-MM-DD' o ISO completo.
        def _normalize_dt(dt: Optional[str], *, is_end: bool) -> Optional[str]:
            if not dt:
                return None
            s = str(dt).strip()
            import re as _re
            if _re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
                return f"{s}T23:59:59.000Z" if is_end else f"{s}T00:00:00.000Z"
            return s

        start_norm = _normalize_dt(from_entered_time, is_end=False) if from_entered_time else None
        end_norm = _normalize_dt(to_entered_time, is_end=True) if to_entered_time else None

        # Si ambas faltan, usar últimos 60 días por defecto
        if not start_norm and not end_norm:
            from datetime import datetime, timedelta
            to_date = datetime.now()
            from_date = to_date - timedelta(days=60)
            start_norm = from_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
            end_norm = to_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        # Si sólo una está presente, derivar la otra para el mismo día
        elif start_norm and not end_norm:
            import re as _re
            m = _re.search(r"(\d{4}-\d{2}-\d{2})", start_norm)
            base = m.group(1) if m else start_norm[:10]
            end_norm = f"{base}T23:59:59.000Z"
        elif end_norm and not start_norm:
            import re as _re
            m = _re.search(r"(\d{4}-\d{2}-\d{2})", end_norm)
            base = m.group(1) if m else end_norm[:10]
            start_norm = f"{base}T00:00:00.000Z"
        
        endpoint = f"{self.base_url}/orders"
        # Agregar parámetros requeridos
        params = {
            'fromEnteredTime': start_norm,
            'toEnteredTime': end_norm,
        }
        if status:
            norm_status = str(status).strip().upper()
            params['status'] = norm_status
        if max_results is not None:
            params['maxResults'] = max_results
        try:
            response = self.client._request("GET", endpoint, params=params, timeout=30)
            
            # Preparar respuesta con metadatos completos
            result = {
                'status_code': response.status_code,
                'success': 200 <= response.status_code < 300,
                'headers': dict(response.headers),
                'url': str(response.url),
                'elapsed_seconds': response.elapsed.total_seconds(),
                'method': 'GET',
                'params': params
            }
            
            # Procesar datos según el status
            if result['success']:
                try:
                    schwab_data = response.json()
                except:
                    schwab_data = []
                result['data'] = schwab_data
                
            else:
                # Manejar errores
                try:
                    error_data = response.json() if response.text else {}
                except:
                    error_data = {'error': response.text or 'No error details'}
                
                result['data'] = error_data
                result['error_message'] = f"{response.status_code} {response.reason} for url: {response.url}"
                
                # Lanzar excepción como antes para mantener compatibilidad
                response.raise_for_status()
            
            return result
            
        except requests.RequestException as e:
            # En caso de excepción, devolver metadatos del error
            return {
                'status_code': getattr(e.response, 'status_code', 0) if hasattr(e, 'response') else 0,
                'success': False,
                'headers': dict(getattr(e.response, 'headers', {})) if hasattr(e, 'response') else {},
                'url': str(getattr(e.response, 'url', endpoint)) if hasattr(e, 'response') else endpoint,
                'elapsed_seconds': 0,
                'method': 'GET',
                'params': params,
                'data': {'error': str(e)},
                'error_message': str(e)
            }
    
    def preview_order(self, account_hash: str, order_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Previsualiza una orden sin colocarla.
        
        POST /accounts/{accountNumber}/previewOrder
        
        Args:
            account_hash: Identificador cifrado de la cuenta (hashValue)
            order_data: Datos de la orden para previsualizar
            
        Returns:
            Dict con metadatos HTTP completos + respuesta nativa:
            {
                'status_code': 200,
                'success': True,
                'headers': {...},
                'url': 'https://...',
                'elapsed_seconds': 0.5,
                'data': {...}  # Información de preview nativa de Schwab
            }
        """
        endpoint = f"{self.base_url}/accounts/{account_hash}/previewOrder"
        headers = {"Content-Type": "application/json"}
        try:
            response = self.client._request("POST", endpoint, json=order_data, headers=headers, timeout=15)
            
            # Preparar respuesta con metadatos completos
            result = {
                'status_code': response.status_code,
                'success': 200 <= response.status_code < 300,
                'headers': dict(response.headers),
                'url': str(response.url),
                'elapsed_seconds': response.elapsed.total_seconds(),
                'method': 'POST'
            }
            
            # Procesar datos según el status
            if result['success']:
                try:
                    schwab_data = response.json()
                except:
                    schwab_data = {}
                result['data'] = schwab_data
                # Intentar extraer order_id del header Location si está presente
                extracted_id = self._extract_order_id_from_location(response.headers.get("Location"))
                if extracted_id:
                    result['order_id'] = extracted_id
                
            else:
                # Manejar errores
                try:
                    error_data = response.json() if response.text else {}
                except:
                    error_data = {'error': response.text or 'No error details'}
                
                result['data'] = error_data
                result['error_message'] = f"{response.status_code} {response.reason} for url: {response.url}"
                
                # Lanzar excepción como antes para mantener compatibilidad
                response.raise_for_status()
            
            return result
            
        except requests.RequestException as e:
            # En caso de excepción, devolver metadatos del error
            return {
                'status_code': getattr(e.response, 'status_code', 0) if hasattr(e, 'response') else 0,
                'success': False,
                'headers': dict(getattr(e.response, 'headers', {})) if hasattr(e, 'response') else {},
                'url': str(getattr(e.response, 'url', endpoint)) if hasattr(e, 'response') else endpoint,
                'elapsed_seconds': 0,
                'method': 'POST',
                'data': {'error': str(e)},
                'error_message': str(e)
            }
    
    def _extract_order_id_from_location(self, location_header: Optional[str]) -> Optional[str]:
        """
        Extrae el order_id del header Location.
        
        El header Location típicamente tiene formato:
        https://api.schwabapi.com/trader/v1/accounts/{accountHash}/orders/{orderId}
        
        Args:
            location_header: Valor del header Location
            
        Returns:
            Order ID extraído o None si no se pudo extraer
        """
        if not location_header:
            return None
        
        try:
            # Buscar patrón /orders/{order_id} al final de la URL
            match = re.search(r'/orders/([^/]+)(?:/.*)?$', location_header)
            if match:
                return match.group(1)
            
            # Fallback: tomar el último segmento de la URL
            segments = location_header.rstrip('/').split('/')
            if len(segments) > 0:
                return segments[-1]
            
        except Exception as e:
            print(f"Error extrayendo order_id del Location header: {e}")
        
        return None

    # ===== Helpers para construir órdenes comunes =====
    @staticmethod
    def build_limit_order(symbol: str, quantity: int, price: float, instruction: str = "BUY") -> Dict[str, Any]:
        return {
            "orderType": "LIMIT",
            "session": "NORMAL",
            "duration": "DAY",
            "orderStrategyType": "SINGLE",
            "orderLegCollection": [
                {
                    "instruction": instruction,
                    "quantity": quantity,
                    "instrument": {"symbol": symbol, "assetType": "EQUITY"},
                }
            ],
            "price": price,
        }

    @staticmethod
    def build_market_order(symbol: str, quantity: int, instruction: str = "BUY") -> Dict[str, Any]:
        return {
            "orderType": "MARKET",
            "session": "NORMAL",
            "duration": "DAY",
            "orderStrategyType": "SINGLE",
            "orderLegCollection": [
                {
                    "instruction": instruction,
                    "quantity": quantity,
                    "instrument": {"symbol": symbol, "assetType": "EQUITY"},
                }
            ],
        }

    @staticmethod
    def build_bracket_order(symbol: str, quantity: int, entry_price: float, take_profit_price: float, stop_loss_price: float) -> Dict[str, Any]:
        return {
            "orderType": "LIMIT",
            "session": "NORMAL",
            "duration": "DAY",
            "orderStrategyType": "TRIGGER",
            "orderLegCollection": [
                {
                    "instruction": "BUY",
                    "quantity": quantity,
                    "instrument": {"symbol": symbol, "assetType": "EQUITY"},
                }
            ],
            "price": entry_price,
            "childOrderStrategies": [
                {
                    "orderStrategyType": "OCO",
                    "childOrderStrategies": [
                        {
                            "orderType": "LIMIT",
                            "session": "NORMAL",
                            "duration": "DAY",
                            "orderStrategyType": "SINGLE",
                            "orderLegCollection": [
                                {
                                    "instruction": "SELL",
                                    "quantity": quantity,
                                    "instrument": {"symbol": symbol, "assetType": "EQUITY"},
                                }
                            ],
                            "price": take_profit_price,
                        },
                        {
                            "orderType": "STOP",
                            "session": "NORMAL",
                            "duration": "DAY",
                            "orderStrategyType": "SINGLE",
                            "orderLegCollection": [
                                {
                                    "instruction": "SELL",
                                    "quantity": quantity,
                                    "instrument": {"symbol": symbol, "assetType": "EQUITY"},
                                }
                            ],
                            "stopPrice": stop_loss_price,
                        },
                    ],
                }
            ],
        }
