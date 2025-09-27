"""
Schwab SDK - Token Handler
Maneja la rotación automática de tokens de acceso y refresh tokens.
"""

import json
import os
import time
import threading
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
import requests
from urllib.parse import urlencode

class TokenHandler:
    """
    Maneja tokens de acceso y refresh tokens con rotación automática.
    
    - Rotación automática de access token cada 29 minutos
    - Rotación automática de refresh token cada 6 días 23 horas  
    - Refresh manual disponible
    - Manejo robusto de errores
    """
    
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str):
        """
        Inicializa el TokenHandler.
        
        Args:
            client_id: Client ID de la aplicación Schwab
            client_secret: Client Secret de la aplicación Schwab
            redirect_uri: URI de redirección para OAuth
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        
        # URLs de Schwab
        self.token_url = "https://api.schwabapi.com/v1/oauth/token"
        
        # Tokens y metadata
        self.access_token: Optional[str] = None
        self.refresh_token: Optional[str] = None
        self.access_token_expires_at: Optional[datetime] = None
        self.refresh_token_expires_at: Optional[datetime] = None
        
        # File path para persistir tokens
        self.token_file = "schwab_tokens.json"
        
        # Threading para auto-refresh
        self._refresh_timer: Optional[threading.Timer] = None
        self._refresh_token_timer: Optional[threading.Timer] = None
        self._lock = threading.Lock()
        
        # Callback para re-login cuando refresh token expira
        self.on_refresh_token_expired = None
        
        # Cargar tokens existentes si existen
        self.load_tokens()
    
    def save_tokens(self, access_token: str, refresh_token: str, expires_in: int = 1800) -> None:
        """
        Guarda los tokens de forma segura.
        
        Args:
            access_token: Token de acceso
            refresh_token: Token de refresh
            expires_in: Segundos hasta que expire el access token (default 1800 = 30 min)
        """
        with self._lock:
            self.access_token = access_token
            self.refresh_token = refresh_token
            
            # Calcular tiempos de expiración
            now = datetime.now()
            self.access_token_expires_at = now + timedelta(seconds=expires_in)
            # Refresh token expira en ~7 días, lo programamos para 6d 23h para ser seguros
            self.refresh_token_expires_at = now + timedelta(days=6, hours=23)
            
            # Persistir a disco
            token_data = {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "access_token_expires_at": self.access_token_expires_at.isoformat(),
                "refresh_token_expires_at": self.refresh_token_expires_at.isoformat()
            }
            
            try:
                with open(self.token_file, 'w') as f:
                    json.dump(token_data, f, indent=2)
            except Exception as e:
                print(f"Error guardando tokens: {e}")
            
            # Programar auto-refresh
            self._schedule_auto_refresh()
    
    def load_tokens(self) -> bool:
        """
        Carga tokens existentes desde disco.
        
        Returns:
            True si se cargaron tokens válidos, False si no
        """
        if not os.path.exists(self.token_file):
            return False
        
        try:
            with open(self.token_file, 'r') as f:
                token_data = json.load(f)
            
            self.access_token = token_data.get("access_token")
            self.refresh_token = token_data.get("refresh_token")
            
            # Parsear fechas de expiración
            if token_data.get("access_token_expires_at"):
                self.access_token_expires_at = datetime.fromisoformat(
                    token_data["access_token_expires_at"]
                )
            
            if token_data.get("refresh_token_expires_at"):
                self.refresh_token_expires_at = datetime.fromisoformat(
                    token_data["refresh_token_expires_at"]
                )
            
            # Verificar si el refresh token aún es válido
            if self.refresh_token_expires_at and datetime.now() >= self.refresh_token_expires_at:
                print("Refresh token expirado, limpiando tokens")
                self._clear_tokens()
                return False
            
            # Programar auto-refresh si tenemos tokens válidos
            if self.refresh_token:
                self._schedule_auto_refresh()
                return True
                
            return False
            
        except Exception as e:
            print(f"Error cargando tokens: {e}")
            return False
    
    def has_valid_token(self) -> bool:
        """
        Verifica si tenemos un access token válido.
        
        Returns:
            True si el access token es válido, False si no
        """
        if not self.access_token or not self.access_token_expires_at:
            return False
        
        # Considerar válido si queda más de 1 minuto antes de expirar
        return datetime.now() < (self.access_token_expires_at - timedelta(minutes=1))
    
    def get_access_token(self) -> Optional[str]:
        """
        Obtiene el access token actual (sin refresh automático).
        
        Returns:
            Access token si es válido, None si no
        """
        if self.has_valid_token():
            return self.access_token
        return None
    
    def refresh_token_now(self) -> bool:
        """
        Refresca el access token inmediatamente usando el refresh token.
        
        Returns:
            True si el refresh fue exitoso, False si falló
        """
        if not self.refresh_token:
            print("No hay refresh token disponible")
            return False
        
        return self._refresh_access_token()
    
    def _refresh_access_token(self) -> bool:
        """
        Refresca el access token usando grant_type=refresh_token.
        
        Returns:
            True si exitoso, False si falló
        """
        if not self.refresh_token:
            return False
        
        payload = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        try:
            response = requests.post(
                self.token_url,
                data=urlencode(payload),
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200:
                token_data = response.json()
                
                # Guardar nuevos tokens
                self.save_tokens(
                    access_token=token_data["access_token"],
                    refresh_token=token_data.get("refresh_token", self.refresh_token),
                    expires_in=token_data.get("expires_in", 1800)
                )
                
                print("Access token refrescado exitosamente")
                return True
            
            else:
                error_data = response.json() if response.content else {}
                error = error_data.get("error", "unknown_error")
                
                # Manejo de errores específicos
                if error in ["invalid_grant", "invalid_client"]:
                    print(f"Refresh token expirado o inválido ({error}), requiere re-login")
                    self._clear_tokens()
                    # Disparar callback para re-login si está configurado
                    if self.on_refresh_token_expired:
                        self.on_refresh_token_expired()
                else:
                    print(f"Error refrescando token: {error}")
                
                return False
                
        except Exception as e:
            print(f"Excepción refrescando token: {e}")
            return False
    
    def _schedule_auto_refresh(self) -> None:
        """
        Programa la rotación automática de tokens.
        """
        # Cancelar timers existentes
        if self._refresh_timer:
            self._refresh_timer.cancel()
        if self._refresh_token_timer:
            self._refresh_token_timer.cancel()
        
        if not self.access_token_expires_at or not self.refresh_token_expires_at:
            return
        
        now = datetime.now()
        
        # Programar refresh de access token (29 minutos desde ahora)
        access_refresh_seconds = 29 * 60  # 29 minutos
        if self.access_token_expires_at > now:
            # Si el token actual no ha expirado, calcular tiempo restante - 1 minuto de buffer
            time_until_expires = (self.access_token_expires_at - now).total_seconds()
            access_refresh_seconds = max(60, time_until_expires - 60)  # Mínimo 1 minuto
        
        self._refresh_timer = threading.Timer(access_refresh_seconds, self._auto_refresh_access_token)
        self._refresh_timer.daemon = True
        self._refresh_timer.start()
        
        # Programar refresh de refresh token (6 días 23 horas desde su creación)
        refresh_token_seconds = (self.refresh_token_expires_at - now).total_seconds()
        if refresh_token_seconds > 0:
            self._refresh_token_timer = threading.Timer(refresh_token_seconds, self._auto_refresh_refresh_token)
            self._refresh_token_timer.daemon = True
            self._refresh_token_timer.start()
        
        print(f"Auto-refresh programado: access token en {access_refresh_seconds/60:.1f} min, refresh token en {refresh_token_seconds/3600:.1f} horas")
    
    def _auto_refresh_access_token(self) -> None:
        """
        Callback para refresh automático del access token cada 29 minutos.
        """
        print("Ejecutando auto-refresh de access token...")
        success = self._refresh_access_token()
        
        if success:
            # Programar el siguiente refresh en 29 minutos
            self._refresh_timer = threading.Timer(29 * 60, self._auto_refresh_access_token)
            self._refresh_timer.daemon = True
            self._refresh_timer.start()
        else:
            print("Auto-refresh falló, se requerirá re-login manual")
    
    def _auto_refresh_refresh_token(self) -> None:
        """
        Callback cuando el refresh token está por expirar.
        Dispara re-login si hay callback configurado.
        """
        print("Refresh token expirando, se requiere re-login")
        self._clear_tokens()
        
        if self.on_refresh_token_expired:
            self.on_refresh_token_expired()
    
    def _clear_tokens(self) -> None:
        """
        Limpia todos los tokens y cancela timers.
        """
        with self._lock:
            self.access_token = None
            self.refresh_token = None
            self.access_token_expires_at = None
            self.refresh_token_expires_at = None
            
            # Cancelar timers
            if self._refresh_timer:
                self._refresh_timer.cancel()
                self._refresh_timer = None
            if self._refresh_token_timer:
                self._refresh_token_timer.cancel()
                self._refresh_token_timer = None
            
            # Eliminar archivo de tokens
            try:
                if os.path.exists(self.token_file):
                    os.remove(self.token_file)
            except Exception as e:
                print(f"Error eliminando archivo de tokens: {e}")
    
    def cleanup(self) -> None:
        """
        Limpia recursos (timers) al destruir el objeto.
        """
        if self._refresh_timer:
            self._refresh_timer.cancel()
        if self._refresh_token_timer:
            self._refresh_token_timer.cancel()
    
    def __del__(self):
        """
        Destructor para limpiar recursos.
        """
        self.cleanup()
