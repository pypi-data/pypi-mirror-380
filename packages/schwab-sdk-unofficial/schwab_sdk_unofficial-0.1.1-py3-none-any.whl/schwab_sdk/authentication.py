"""
Schwab SDK - Authentication Handler
Maneja el flujo completo de OAuth con Schwab API.
"""

import webbrowser
import time
from typing import Optional, Dict, Any, Callable
from urllib.parse import urlencode
import requests

try:
    from .callback import CallbackServer
    from .token_handler import TokenHandler
except ImportError:
    # Fallback para testing directo
    from callback import CallbackServer
    from token_handler import TokenHandler

class Authentication:
    """
    Maneja la autenticación OAuth con Schwab API.
    
    - Construye URL de autorización
    - Levanta servidor callback para recibir authorization code
    - Intercambia code por tokens
    - Integra con TokenHandler para manejo persistente
    """
    
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, token_handler: TokenHandler):
        """
        Inicializa el Authentication handler.
        
        Args:
            client_id: Client ID de la aplicación Schwab
            client_secret: Client Secret de la aplicación Schwab  
            redirect_uri: URI de redirección para OAuth (debe coincidir con callback server)
            token_handler: Instancia de TokenHandler para manejo de tokens
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.token_handler = token_handler
        
        # URLs de Schwab OAuth
        self.auth_url_base = "https://api.schwabapi.com/v1/oauth/authorize"
        self.token_url = "https://api.schwabapi.com/v1/oauth/token"
        
        # Callback server
        self.callback_server: Optional[CallbackServer] = None
        
        # Estado del último login
        self.last_login_result: Optional[Dict[str, Any]] = None
    
    def login(self, timeout: int = 300, auto_open_browser: bool = True) -> bool:
        """
        Ejecuta el flujo completo de OAuth para obtener tokens.
        
        Verifica primero si ya hay tokens válidos antes de iniciar el flujo.
        
        Args:
            timeout: Tiempo máximo en segundos para esperar el callback (default: 300)
            auto_open_browser: Si True, abre automáticamente el browser (default: True)
            
        Returns:
            True si la autenticación fue exitosa, False si falló
        """
        # Verificar si ya tenemos tokens válidos
        if self.token_handler.has_valid_token():
            print("✅ Ya tienes tokens válidos, no es necesario hacer login")
            return True
        
        print("🔐 Iniciando flujo de autenticación OAuth...")
        
        try:
            # 1. Iniciar servidor callback
            if not self._start_callback_server():
                return False
            
            # 2. Construir URL de autorización y abrir browser
            auth_url = self._build_auth_url()
            print(f"🌐 URL de autorización: {auth_url}")
            
            if auto_open_browser:
                print("🚀 Abriendo navegador automáticamente...")
                webbrowser.open(auth_url)
            else:
                print("🔗 Por favor, ve a la URL anterior en tu navegador")
            
            # 3. Esperar callback con authorization code
            print(f"⏰ Esperando callback (timeout: {timeout}s)...")
            callback_result = self.callback_server.wait(timeout)
            
            # 4. Cerrar servidor callback
            self._stop_callback_server()
            
            # 5. Procesar resultado del callback
            if not callback_result:
                print("❌ Timeout esperando callback de autorización")
                return False
            
            # Los parámetros están dentro de la key "params"
            params = callback_result.get("params", {})
            
            if params.get("error"):
                error = params["error"]
                error_desc = params.get("error_description", "")
                print(f"❌ Error en OAuth: {error} - {error_desc}")
                return False
            
            # 6. Extraer authorization code
            auth_code = params.get("code")
            if not auth_code:
                print("❌ No se recibió authorization code en el callback")
                print(f"🔍 Callback recibido: {callback_result}")
                return False
            
            print("✅ Authorization code recibido, intercambiando por tokens...")
            
            # 7. Intercambiar code por tokens
            if self._exchange_code_for_tokens(auth_code):
                print("🎉 ¡Autenticación completada exitosamente!")
                return True
            else:
                print("❌ Falló el intercambio de code por tokens")
                return False
                
        except Exception as e:
            print(f"❌ Error durante autenticación: {e}")
            self._stop_callback_server()
            return False
    
    def _build_auth_url(self) -> str:
        """
        Construye la URL de autorización de Schwab.
        
        Returns:
            URL completa para autorización
        """
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code",
            "scope": "api"  # Scope requerido por Schwab
        }
        
        return f"{self.auth_url_base}?{urlencode(params)}"
    
    def _start_callback_server(self) -> bool:
        """
        Inicia el servidor callback para recibir el authorization code.
        
        Returns:
            True si el servidor se inició correctamente, False si falló
        """
        try:
            # Extraer información del redirect_uri para configurar el server
            # Ejemplo: https://127.0.0.1:8443/callback -> host=127.0.0.1, puerto 8443
            import urllib.parse
            parsed = urllib.parse.urlparse(self.redirect_uri)
            host = parsed.hostname or "127.0.0.1"
            port = parsed.port or (443 if parsed.scheme == 'https' else 80)
            path = parsed.path or "/callback"
            
            # Inicializar servidor callback con configuración completa
            self.callback_server = CallbackServer(
                host=host,
                port=port,
                path=path,
                force_https=True,
                adhoc_ssl=True,
                server="auto"
            )
            
            # Iniciar el servidor (no retorna booleano, lanza excepción si falla)
            self.callback_server.start()
            
            print(f"✅ Servidor callback iniciado en https://{host}:{port}{path}")
            return True
                
        except Exception as e:
            print(f"❌ Error iniciando servidor callback: {e}")
            return False
    
    def _stop_callback_server(self) -> None:
        """
        Detiene el servidor callback.
        """
        if self.callback_server:
            try:
                self.callback_server.shutdown()
                print("✅ Servidor callback detenido")
            except Exception as e:
                print(f"⚠️ Error deteniendo servidor callback: {e}")
            finally:
                self.callback_server = None
    
    def _exchange_code_for_tokens(self, auth_code: str) -> bool:
        """
        Intercambia el authorization code por access y refresh tokens.
        
        Args:
            auth_code: Authorization code recibido del callback
            
        Returns:
            True si el intercambio fue exitoso, False si falló
        """
        payload = {
            "grant_type": "authorization_code",
            "code": auth_code,
            "redirect_uri": self.redirect_uri
        }
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        # Usar Basic Authentication como es común en OAuth
        import base64
        credentials = f"{self.client_id}:{self.client_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        headers["Authorization"] = f"Basic {encoded_credentials}"
        
        try:
            print("🔄 Intercambiando authorization code por tokens...")
            
            response = requests.post(
                self.token_url,
                data=urlencode(payload),
                headers=headers,
                timeout=15
            )
            
            if response.status_code == 200:
                token_data = response.json()
                
                # Extraer tokens
                access_token = token_data.get("access_token")
                refresh_token = token_data.get("refresh_token")
                expires_in = token_data.get("expires_in", 1800)  # Default 30 min
                
                if not access_token or not refresh_token:
                    print("❌ Respuesta de tokens incompleta")
                    return False
                
                # Guardar tokens usando TokenHandler
                self.token_handler.save_tokens(access_token, refresh_token, expires_in)
                
                print("✅ Tokens guardados exitosamente")
                return True
            
            else:
                try:
                    error_data = response.json()
                    error = error_data.get("error", "unknown_error")
                    error_desc = error_data.get("error_description", "")
                    print(f"❌ Error intercambiando tokens: {error} - {error_desc}")
                except:
                    print(f"❌ Error intercambiando tokens: HTTP {response.status_code}")
                
                return False
                
        except requests.RequestException as e:
            print(f"❌ Error de red intercambiando tokens: {e}")
            return False
        except Exception as e:
            print(f"❌ Error inesperado intercambiando tokens: {e}")
            return False
    
    def is_authenticated(self) -> bool:
        """
        Verifica si el usuario está autenticado con tokens válidos.
        
        Returns:
            True si hay tokens válidos, False si no
        """
        return self.token_handler.has_valid_token()
    
    def get_access_token(self) -> Optional[str]:
        """
        Obtiene el access token actual.
        
        Returns:
            Access token válido o None si no hay
        """
        return self.token_handler.get_access_token()
    
    def logout(self) -> None:
        """
        Cierra sesión eliminando todos los tokens.
        """
        print("👋 Cerrando sesión...")
        self.token_handler._clear_tokens()
        print("✅ Sesión cerrada exitosamente")
    
    def __del__(self):
        """
        Destructor para asegurar que el servidor callback se cierre.
        """
        self._stop_callback_server()
