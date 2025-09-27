"""
Schwab SDK - Client Principal
Clase principal que orquesta todos los módulos del SDK.
"""

import os
import time
from typing import Optional, TYPE_CHECKING
import requests

try:
    from .token_handler import TokenHandler
    from .authentication import Authentication
except ImportError:
    # Fallback para testing directo
    from token_handler import TokenHandler
    from authentication import Authentication

# Forward declarations para type hints
if TYPE_CHECKING:
    try:
        from .accounts import Accounts
        from .orders import Orders
        from .market import Market
        from .streaming import Streaming
    except ImportError:
        from accounts import Accounts
        from orders import Orders
        from market import Market
        from streaming import Streaming


class Client:
    """
    Cliente principal del Schwab SDK.
    
    Proporciona acceso a todas las funcionalidades:
    - client.account.* - Endpoints de cuentas, transacciones y preferencias
    - client.orders.* - Endpoints de órdenes
    - client.market.* - Endpoints de datos de mercado
    - client.streaming.* - WebSocket streaming
    
    Usage:
        client = Client(client_id, client_secret, redirect_uri)
        client.login()  # Solo si no hay tokens válidos
        
        # Usar submódulos
        accounts = client.account.get_accounts()
        quote = client.market.get_quote("AAPL")
        client.orders.place_order(account_hash, order_data)
    """
    
    def __init__(
        self, 
        client_id: str, 
        client_secret: str, 
        redirect_uri: str = "https://localhost:8080/callback"
    ):
        """
        Inicializa el cliente Schwab SDK.
        
        Args:
            client_id: Client ID de la aplicación Schwab
            client_secret: Client Secret de la aplicación Schwab
            redirect_uri: URI de redirección para OAuth (default: https://localhost:8080/callback)
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        
        # URLs base de Schwab API
        self.trader_base_url = "https://api.schwabapi.com/trader/v1"
        self.market_base_url = "https://api.schwabapi.com/marketdata/v1"
        
        # Inicializar componentes core
        self.token_handler = TokenHandler(client_id, client_secret, redirect_uri)
        self.authentication = Authentication(client_id, client_secret, redirect_uri, self.token_handler)
        
        # Configurar callback para re-login automático cuando refresh token expire
        self.token_handler.on_refresh_token_expired = self._handle_refresh_token_expired
        
        # Inicializar submódulos (lazy loading para evitar import circular)
        self._account_module: Optional['Accounts'] = None
        self._orders_module: Optional['Orders'] = None  
        self._market_module: Optional['Market'] = None
        self._streaming_module: Optional['Streaming'] = None
        
        # Auto-login si no hay tokens válidos
        self._auto_authenticate()
    
    @property
    def account(self) -> 'Accounts':
        """
        Acceso al módulo de cuentas, transacciones y preferencias.
        
        Returns:
            Instancia del módulo Accounts
        """
        if self._account_module is None:
            try:
                from .accounts import Accounts
            except ImportError:
                from accounts import Accounts
            self._account_module = Accounts(self)
        return self._account_module
    
    @property 
    def orders(self) -> 'Orders':
        """
        Acceso al módulo de órdenes.
        
        Returns:
            Instancia del módulo Orders
        """
        if self._orders_module is None:
            try:
                from .orders import Orders
            except ImportError:
                from orders import Orders
            self._orders_module = Orders(self)
        return self._orders_module
    
    @property
    def market(self) -> 'Market':
        """
        Acceso al módulo de datos de mercado.
        
        Returns:
            Instancia del módulo Market
        """
        if self._market_module is None:
            try:
                from .market import Market
            except ImportError:
                from market import Market
            self._market_module = Market(self)
        return self._market_module
    
    @property
    def streaming(self) -> 'Streaming':
        """
        Acceso al módulo de streaming WebSocket.
        
        Returns:
            Instancia del módulo Streaming
        """
        if self._streaming_module is None:
            try:
                from .streaming import Streaming
            except ImportError:
                from streaming import Streaming
            self._streaming_module = Streaming(self)
        return self._streaming_module
    
    def login(self, timeout: int = 300, auto_open_browser: bool = True) -> bool:
        """
        Ejecuta el flujo de autenticación OAuth.
        
        Args:
            timeout: Tiempo máximo para esperar callback (default: 300s)
            auto_open_browser: Abrir browser automáticamente (default: True)
            
        Returns:
            True si la autenticación fue exitosa, False si falló
        """
        return self.authentication.login(timeout, auto_open_browser)
    
    def has_valid_token(self) -> bool:
        """
        Verifica si hay tokens de acceso válidos.
        
        Returns:
            True si los tokens son válidos, False si no
        """
        return self.token_handler.has_valid_token()
    
    def refresh_token(self) -> bool:
        """
        Refresca automáticamente el access token.
        
        La rotación automática se maneja internamente cada 29 minutos.
        Este método es principalmente informativo.
        
        Returns:
            True si hay tokens válidos o refresh exitoso, False si no
        """
        if self.has_valid_token():
            return True
        return self.token_handler.refresh_token_now()
    
    def refresh_token_now(self) -> bool:
        """
        Fuerza un refresh inmediato del access token.
        
        Returns:
            True si el refresh fue exitoso, False si falló
        """
        return self.token_handler.refresh_token_now()
    
    def logout(self) -> None:
        """
        Cierra sesión eliminando todos los tokens.
        """
        self.authentication.logout()
    
    def get_access_token(self) -> Optional[str]:
        """
        Obtiene el access token actual para uso en requests.
        
        Returns:
            Access token válido o None si no hay
        """
        return self.token_handler.get_access_token()
    
    def get_auth_headers(self) -> dict:
        """
        Obtiene headers de autenticación para requests API.
        
        Returns:
            Dict con headers de Authorization, o dict vacío si no hay token
        """
        token = self.get_access_token()
        if token:
            return {
                "Authorization": f"Bearer {token}"
            }
        return {}

    def _request(
        self,
        method: str,
        url: str,
        *,
        params: Optional[dict] = None,
        json: Optional[dict] = None,
        headers: Optional[dict] = None,
        timeout: int = 15,
        max_retries: int = 3,
        backoff_factor: float = 0.5,
    ) -> requests.Response:
        """
        Realiza una request HTTP con:
        - Headers de Authorization automáticos
        - Refresh de token en 401 (una vez)
        - Reintentos con backoff para 429/5xx
        
        Returns:
            requests.Response
        """
        # Merge de headers
        req_headers = {**self.get_auth_headers(), **(headers or {})}

        def _send() -> requests.Response:
            return requests.request(
                method=method.upper(),
                url=url,
                params=params,
                json=json,
                headers=req_headers,
                timeout=timeout,
            )

        last_exc: Optional[Exception] = None
        attempt = 0
        while attempt < max_retries:
            try:
                resp = _send()
                # Manejo 401: intentar refresh una vez y reintentar inmediato
                if resp.status_code == 401:
                    try:
                        if self.refresh_token_now():
                            req_headers = {**self.get_auth_headers(), **(headers or {})}
                            resp = _send()
                            if resp.status_code != 401:
                                return resp
                    except Exception:
                        pass
                    # Si sigue 401, devolver respuesta para que el caller maneje
                    return resp

                # Reintentos para 429 y 5xx
                if resp.status_code in (429, 500, 502, 503, 504):
                    sleep_s = backoff_factor * (2 ** attempt)
                    time.sleep(sleep_s)
                    attempt += 1
                    continue
                return resp
            except requests.RequestException as e:
                last_exc = e
                sleep_s = backoff_factor * (2 ** attempt)
                time.sleep(sleep_s)
                attempt += 1

        # Si agotamos reintentos y hubo excepción, relanzar; si no, devolver última resp (no disponible aquí)
        if last_exc:
            raise last_exc
        # Caso improbable: sin excepción pero sin retorno
        return _send()
    
    def is_authenticated(self) -> bool:
        """
        Verifica si el cliente está autenticado.
        
        Returns:
            True si está autenticado, False si no
        """
        return self.authentication.is_authenticated()
    
    def _auto_authenticate(self) -> None:
        """
        Intenta autenticación automática si no hay tokens válidos.
        """
        if not self.has_valid_token():
            print("ℹ️ No se encontraron tokens válidos. Usa client.login() para autenticarte.")
        else:
            print("✅ Cliente autenticado con tokens válidos")
    
    def _handle_refresh_token_expired(self) -> None:
        """
        Callback que se ejecuta cuando el refresh token expira.
        
        Notifica al usuario que necesita hacer re-login.
        """
        print("🔄 Refresh token expirado. Por favor, ejecuta client.login() para re-autenticarte.")
    
    def __enter__(self):
        """
        Context manager entry.
        """
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context manager exit - limpia recursos.
        """
        if hasattr(self, 'token_handler'):
            self.token_handler.cleanup()
    
    def __del__(self):
        """
        Destructor - limpia recursos.
        """
        if hasattr(self, 'token_handler'):
            self.token_handler.cleanup()
    
    def __repr__(self) -> str:
        """
        Representación string del cliente.
        """
        status = "authenticated" if self.is_authenticated() else "not authenticated"
        return f"SchwabClient(client_id='{self.client_id[:8]}...', status='{status}')"
