# callback-md — Documentación del servidor de callback OAuth (Flask)

Servidor mínimo pensado para **recibir el callback OAuth** en `https://127.0.0.1:<puerto>/<ruta>` con una configuración **simple** y lista para **entornos profesionales** (modo producción sencillo) sin perder facilidad de uso.

> Este documento describe exclusivamente el módulo `callback.py` y su API. No incluye licencia ni código de intercambio de tokens; es una guía de integración del módulo en tu proyecto/SDK.

---

## Características
- **HTTPS por defecto** (recomendado/obligatorio para la mayoría de proveedores).
- **Dos modos de TLS**:
  - **PEM**: certificados en archivos (`ssl_cert`, `ssl_key`) → recomendado para uso profesional.
  - **Adhoc**: `adhoc_ssl=True` genera un certificado temporal en memoria (requiere `cryptography`) → ideal para desarrollo.
- **Modo producción simple** con `gevent.pywsgi` (si está instalado) o *fallback* a Werkzeug.
- **API de alto nivel** (`run_callback_server(...)`) y **CLI**.
- **Captura robusta de parámetros**: query (GET), form (POST), JSON, y tokens en `#fragment` mediante una página puente que los reenvía por POST.
- **Respuesta JSON opcional** en la ruta del callback usando `Accept: application/json` o `?format=json`.
- **Páginas personalizables**: puedes pasar rutas a **Success HTML** y **Error HTML**; si no existen o fallan, se usan **fallbacks** legibles.
- **Apagado limpio** incluso en HTTPS.

---

## Requisitos
- **Python** ≥ 3.8
- **Dependencias**:
  - Requerida: `Flask`
  - Opcionales:
    - `gevent` (modo producción sin warning)
    - `cryptography` (para `adhoc_ssl=True`)
    - `requests` (apagado limpio en HTTPS)

### Instalación
```bash
pip install Flask
# Producción simple (recomendado):
pip install gevent
# Adhoc SSL (si vas a usar adhoc_ssl=True):
pip install cryptography
# Apagado limpio en HTTPS:
pip install requests
```

---

## Uso rápido

### Como librería (producción simple con certificados PEM)
```python
from callback import run_callback_server

res = run_callback_server(
    host="127.0.0.1",
    port=8080,
    path="/callback",
    timeout=180,
    ssl_cert="cert.pem",
    ssl_key="key.pem",
    server="auto",   # usa gevent si está instalado
    success_html_path="/ruta/a/success.html",  # opcional
    error_html_path="/ruta/a/error.html",      # opcional
)

if res is None:
    raise TimeoutError("No llegó el callback a tiempo")

params = res["params"]
print(params)  # {'code': '...', 'state': '...'} o tokens si el proveedor los devuelve
```

### Como librería (desarrollo rápido con certificado adhoc)
```python
res = run_callback_server(
    host="127.0.0.1",
    port=8080,
    path="/callback",
    timeout=180,
    adhoc_ssl=True,
    server="werkzeug",  # verás el warning de dev; normal en pruebas
    # success_html_path / error_html_path también son válidos aquí
)
```

### CLI (producción, usará gevent si está instalado y --server auto)
```bash
python callback.py --host 127.0.0.1 --port 8080 --path callback   --timeout 180 --ssl-cert cert.pem --ssl-key key.pem --server auto   --success-html /ruta/a/success.html --error-html /ruta/a/error.html
```

### CLI (desarrollo, certificado adhoc)
```bash
python callback.py --host 127.0.0.1 --port 8080 --path callback   --timeout 180 --adhoc-ssl --server werkzeug   --success-html /ruta/a/success.html --error-html /ruta/a/error.html
```

**Salida esperada (una sola línea JSON):**
```json
{"params":{"code":"...","state":"..."},"method":"GET","path":"/callback","received_at":1730000000}
```

---

## Páginas HTML personalizadas (Success / Error)
Puedes pasar rutas a archivos estáticos HTML para mostrar una UI final al usuario:
- **`success_html_path`**: se sirve cuando el callback incluye `code` o tokens (éxito).
- **`error_html_path`**: se sirve cuando el callback incluye `error` (fracaso).

Si el archivo **no existe** o **falla** al leerse, el servidor registra un log y usa:
- Fallback de **éxito**: “Credenciales recibidas correctamente. Ya puedes cerrar esta ventana.”
- Fallback de **error**: “No se pudo completar la autenticación. Cierra esta ventana y vuelve a intentarlo.”

> Si la petición incluye `Accept: application/json` o `?format=json`, **siempre** se responde JSON (útil para automatización) y no se renderiza HTML.

---

## API de alto nivel

### `run_callback_server(...)`
**Firma**
```python
def run_callback_server(
    host: str = "127.0.0.1",
    port: int = 8080,
    path: str = "/callback",
    *,
    timeout: float = 180.0,
    ssl_cert: Optional[str] = None,
    ssl_key: Optional[str] = None,
    adhoc_ssl: bool = False,
    force_https: bool = True,
    server: str = "auto",
    success_html_path: Optional[str] = None,
    error_html_path: Optional[str] = None,
    logger: Optional[logging.Logger] = None,
) -> Optional[Dict[str, Any]]:
    ...
```

**Descripción**: Levanta el servidor, espera **una** respuesta (patrón *one-shot*) y lo apaga. Devuelve un `dict` con los datos del callback, o `None` si expira el `timeout`.

**Parámetros**
- `host`: normalmente `"127.0.0.1"` para uso local.
- `port`: p. ej. `8080`. Debe coincidir con el `redirect_uri` registrado.
- `path`: p. ej. `"/callback"`. Se normaliza si pasas `"callback"`.
- `timeout`: segundos a esperar antes de devolver `None`.
- `ssl_cert`, `ssl_key`: rutas a archivos PEM para TLS (recomendado en producción simple).
- `adhoc_ssl`: genera un certificado temporal en memoria (requiere `cryptography`). Útil para desarrollo.
- `force_https`: si `True` (por defecto), exige TLS (adhoc o PEM). Si `False`, permite HTTP (no recomendado).
- `server`: `"auto"` | `"gevent"` | `"werkzeug"`.
  - `auto`: usa gevent si hay certs PEM y `gevent` está instalado; si no, cae a werkzeug (o HTTP si `force_https=False`).
  - `gevent`: fuerza gevent (requiere certs PEM).
  - `werkzeug`: usa `app.run` (dev server), compatible con `adhoc_ssl`.
- `success_html_path`: ruta al HTML de éxito (opcional). Si falla, se usa fallback de éxito.
- `error_html_path`: ruta al HTML de error (opcional). Si falla, se usa fallback de error.
- `logger`: permite inyectar un `logging.Logger` propio.

**Valor devuelto**
```json
{
  "params": { "code": "...", "state": "..." },
  "method": "GET",
  "path": "/callback",
  "received_at": 1730000000
}
```

---

## API de bajo nivel (opcional)

### `CallbackServer`
- `start()`: levanta el servidor en un hilo de fondo.
- `wait(timeout: Optional[float]) -> Optional[dict]`: bloquea hasta recibir el primer callback o agotar `timeout`.
- `shutdown()`: apaga el servidor limpiamente. En HTTPS + Werkzeug, usa una ruta interna `GET /__shutdown__` (se invoca con `verify=False` sobre loopback).

**Rutas expuestas**
- `/<path>` (tu `path`): captura parámetros.
- `/health`: devuelve `200 OK` (texto `OK`).
- `/__shutdown__`: (interno) detiene el server Werkzeug; se usa sólo para apagado.

---

## Comportamiento HTTP
- **Respuesta HTML** por defecto con un mensaje de *ok*.
- **Respuesta JSON** si el cliente envía `Accept: application/json` o agrega `?format=json` a la URL.
- **Bridge de fragmento**: si el proveedor devuelve tokens en `#fragment`, el HTML de la ruta ejecuta un script que:
  1) extrae el fragmento,
  2) lo convierte a objeto (`{access_token: ..., id_token: ..., ...}`),
  3) lo envía por `POST` (JSON) a la misma ruta como `{ "fragment_params": { ... } }`.
- El servidor **mergea**: query (GET) + form (POST) + JSON + `fragment_params` (si están) en `result["params"]`.
- Si el callback llega sin `error` **y** sin `code/tokens`, se muestra el **bridge** y **no** se marca como completado hasta recibir el POST con `fragment_params`.

---

## Matriz de configuración TLS/servidor
| `server`     | Certificados                      | Resultado                   |
|--------------|-----------------------------------|-----------------------------|
| `auto`       | PEM + `gevent` instalado          | **gevent.pywsgi** (prod)    |
| `auto`       | Sólo PEM (sin `gevent`)           | Werkzeug (dev server)       |
| `auto`       | `adhoc_ssl=True`                  | Werkzeug (dev + adhoc)      |
| `gevent`     | **PEM obligatorio**               | **gevent.pywsgi** (prod)    |
| `werkzeug`   | PEM o `adhoc_ssl=True`            | Werkzeug (dev server)       |

> Nota: gevent **no** soporta `adhoc_ssl`. Para adhoc, usa `werkzeug`.

---

## Integración en tu proyecto
Esta sección explica **cómo encajar `callback.py` en cualquier proyecto** (CLI, app de escritorio, servicio interno) sin imponer estructura.

### Estructura sugerida (opcional)
```
project/
  callback.py
  oauth_flow.py           # orquesta el flujo OAuth (tu código)
  assets/
    success.html
    error.html
```

### Pasos de integración
1. **Define el `redirect_uri`** que registrarás con el proveedor (debe ser EXACTO):
   - Ej.: `https://127.0.0.1:8080/callback` → host, puerto y ruta deben coincidir.
2. **Construye la URL de autorización** con `response_type=code`, `client_id`, `redirect_uri`, `scope` y `state` (un valor aleatorio que guardarás para validar).
3. **Abre el navegador** apuntando a esa URL (por ejemplo con `webbrowser.open`).
4. **Arranca el callback** con `run_callback_server(...)` usando **HTTPS**:
   - En dev: `adhoc_ssl=True` y `server="werkzeug"`.
   - En prod local: `ssl_cert` + `ssl_key` y `server="auto"` (con `gevent` instalado).
   - (Opcional) Pasa `success_html_path` / `error_html_path` para una mejor UX.
5. **Espera el resultado** (`dict`) y **valida `state`**. Si viene `error`, trátalo. Si viene `code`/tokens, continúa.
6. **Entrega `code`** a tu capa de intercambio de tokens (NO incluida aquí) y persiste el resultado según tus políticas.

### Ejemplo mínimo de orquestación (pseudo-código)
```python
# oauth_flow.py (ejemplo de integración)
import secrets, webbrowser
from urllib.parse import quote_plus
from callback import run_callback_server

CLIENT_ID = "..."
REDIRECT_URI = "https://127.0.0.1:8080/callback"
SCOPE = "read"

state = secrets.token_urlsafe(24)
auth_url = (
    "https://api.schwabapi.com/v1/oauth/authorize"
    f"?response_type=code&client_id={CLIENT_ID}"
    f"&redirect_uri={quote_plus(REDIRECT_URI)}&scope={SCOPE}&state={state}"
)
webbrowser.open(auth_url, new=2)

result = run_callback_server(
    host="127.0.0.1", port=8080, path="/callback",
    timeout=180,
    ssl_cert="cert.pem", ssl_key="key.pem", server="auto",
    success_html_path="assets/success.html",
    error_html_path="assets/error.html",
)

if result is None:
    raise TimeoutError("Timeout esperando callback")

params = result["params"]
if params.get("state") != state:
    raise ValueError("State inválido")
if "error" in params:
    raise RuntimeError(params.get("error_description") or params["error"])  # manejar según tu app
code = params.get("code")
# Aquí delegas el intercambio de `code` por tokens a tu propia implementación
```

> Tu módulo de tokens (persistencia/refresh/rotación) queda a tu criterio; `callback.py` sólo gestiona el retorno del navegador de forma segura y amigable.

---

## Manejo de errores y logs
- Si no se encuentran/leen `success_html_path` o `error_html_path`, se registra un **log de error** y se usa el **fallback** correspondiente.
- Si llega un callback con `error`, el servidor:
  - marca el flujo como completado,
  - devuelve JSON (`{"ok": true, ...}`) si se pide JSON,
  - o sirve `error_html_path` (o fallback) en modo HTML.
- Si el callback aún no trae `code`/tokens ni `error`, se sirve el **bridge** y no se completa hasta recibir los **fragment_params** por POST.

---

## Solución de problemas
- **“WARNING: This is a development server…”**: aparece con Werkzeug (dev). Para evitarlo, instala `gevent` y usa `server="auto"` o `"gevent"` con PEM.
- **El navegador advierte sobre el certificado**: normal con adhoc o autofirmados. Usa PEM confiable (mkcert) para evitarlo.
- **No llega el callback**:
  - Verifica que la URL de autorización tenga el `redirect_uri` exacto (incluye puerto y ruta).
  - Revisa firewall/antivirus.
  - Aumenta `timeout`.
- **`adhoc_ssl=True` falla**: instala `cryptography`.
- **`server="gevent"` falla**: instala `gevent` y usa PEM (gevent no soporta adhoc).
- **Puerto ocupado**: cambia `port` o libera el 8080.

---

## Compatibilidad
- **SO**: Windows, macOS, Linux.
- **Python**: 3.8+
- **Servidores**: Werkzeug (dev), gevent.pywsgi (prod simple).
