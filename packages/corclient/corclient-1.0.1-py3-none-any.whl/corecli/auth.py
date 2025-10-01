import json
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Optional
from urllib.parse import parse_qs, urlparse

import requests
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from corecli.pkce import generate_pkce_pair
from corecli.utils import clear_tokens, decode_jwt, load_tokens, save_tokens

console = Console()


# =====================
# CONFIG FIJA (NO SE MODIFICA)
# =====================
CLIENT_ID = "1gd8tf85qs07ra4b38vcm4mih5"  # <-- tu Client ID
COGNITO_DOMAIN = "https://corcli.projectcor.com"
REDIRECT_URI = "http://localhost:8000/callback"
SCOPES = ["openid", "email", "profile"]
LOGOUT_REDIRECT_URI = "http://localhost:8000/logout"


# =====================
# HTTP HANDLER PARA CALLBACK
# =====================
class CallbackHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Silencia logs de acceso/informativos
        return

    def log_error(self, format, *args):
        # Muestra únicamente errores a stderr
        try:
            sys.stderr.write(
                f"{self.address_string()} - - [{self.log_date_time_string()}] ERROR: {format % args}\n"
            )
        except Exception:
            pass

    def do_GET(self):
        if self.path.startswith("/callback"):
            query = parse_qs(urlparse(self.path).query)
            self.server.auth_code = query.get("code", [None])[0]
            app_redirect = getattr(self.server, "app_redirect", None)
            js_app_redirect = json.dumps(app_redirect) if app_redirect else "null"

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()

            html = f"""
<!doctype html>
<html lang=\"es\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>CoreCLI · Login exitoso</title>
  <style>
    :root {{
      --bg: #0b1020;
      --card: #121a33;
      --accent: #8ab4f8;
      --ok: #34d399;
      --text: #e5e7eb;
      --muted: #94a3b8;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      background: radial-gradient(1200px 600px at 20% -10%, #1f2a52 0%, #0b1020 70%);
      color: var(--text);
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Inter, Arial, sans-serif;
    }}
    .card {{
      width: min(680px, 92vw);
      background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 16px;
      padding: 28px 24px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.06);
      backdrop-filter: blur(6px);
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: 24px;
      letter-spacing: 0.2px;
    }}
    p {{
      margin: 6px 0;
      color: var(--muted);
      line-height: 1.6;
    }}
    .ok {{ color: var(--ok); font-weight: 600; }}
    .meta {{
      margin-top: 16px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px 16px;
      font-size: 14px;
      color: #c7d2fe;
    }}
    .countdown {{
      margin-top: 14px;
      padding: 10px 12px;
      border: 1px dashed rgba(138,180,248,0.4);
      border-radius: 10px;
      background: rgba(26, 35, 75, 0.35);
      color: var(--accent);
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }}
    .small {{ font-size: 13px; color: var(--muted); }}
    a.btn {{
      display: inline-block;
      margin-top: 16px;
      padding: 10px 14px;
      border-radius: 10px;
      background: #22315f;
      color: #e8eeff;
      text-decoration: none;
      border: 1px solid rgba(138,180,248,0.25);
    }}
    a.btn:hover {{ background: #2b3c70; }}
  </style>
  <script>
    const appRedirect = {js_app_redirect};
    if (appRedirect) {{
      // Intenta volver a la app que abrió el login
      setTimeout(() => {{ window.location.href = appRedirect; }}, 0);
    }}
    let secs = 10;
    function tick() {{
      const el = document.getElementById('secs');
      if (el) el.textContent = secs.toString();
      secs -= 1;
      if (secs < 0) {{
        try {{
          window.open('', '_self');
          window.close();
        }} catch (e) {{}}
      }} else {{
        setTimeout(tick, 1000);
      }}
    }}
    window.addEventListener('DOMContentLoaded', tick);
  </script>
  <meta http-equiv=\"refresh\" content=\"35;url=about:blank\">
  <!-- meta de respaldo: si window.close falla, al menos salimos de la página -->
  <link rel=\"icon\" href=\"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><circle cx='32' cy='32' r='30' fill='%238ab4f8'/><path d='M20 34l7 7 17-17' stroke='white' stroke-width='6' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>\" />

</head>
<body>
  <div class=\"card\">
    <h1>✅ Login exitoso</h1>
    <p>Ya puedes volver a la terminal. Esta pestaña se cerrará automáticamente.</p>
    <div class=\"countdown\">Cerrando en <span id=\"secs\">10</span> segundos…</div>
    <p class=\"small\">Si no se cierra por políticas del navegador, puedes cerrarla manualmente.</p>
    <a class=\"btn\" href=\"about:blank\">Cerrar ahora</a>
  </div>
</body>
</html>
"""
            self.wfile.write(html.encode("utf-8"))
        elif self.path.startswith("/logout"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()

            html = """
<!doctype html>
<html lang=\"es\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>CoreCLI · Logout</title>
  <style>
    :root {
      --bg: #0b1020;
      --card: #121a33;
      --accent: #fca5a5;
      --ok: #34d399;
      --text: #e5e7eb;
      --muted: #94a3b8;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      background: radial-gradient(1200px 600px at 20% -10%, #1f2a52 0%, #0b1020 70%);
      color: var(--text);
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Inter, Arial, sans-serif;
    }
    .card {
      width: min(680px, 92vw);
      background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 16px;
      padding: 28px 24px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.06);
      backdrop-filter: blur(6px);
    }
    h1 {
      margin: 0 0 8px;
      font-size: 24px;
      letter-spacing: 0.2px;
    }
    p {
      margin: 6px 0;
      color: var(--muted);
      line-height: 1.6;
    }
    .countdown {
      margin-top: 14px;
      padding: 10px 12px;
      border: 1px dashed rgba(252,165,165,0.35);
      border-radius: 10px;
      background: rgba(75, 26, 35, 0.25);
      color: var(--accent);
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }
    .small { font-size: 13px; color: var(--muted); }
    a.btn {
      display: inline-block;
      margin-top: 16px;
      padding: 10px 14px;
      border-radius: 10px;
      background: #5f2222;
      color: #ffe8e8;
      text-decoration: none;
      border: 1px solid rgba(252,165,165,0.35);
    }
    a.btn:hover { background: #703030; }
  </style>
  <script>
    let secs = 5;
    function tick() {
      const el = document.getElementById('secs');
      if (el) el.textContent = secs.toString();
      secs -= 1;
      if (secs < 0) {
        try {
          window.open('', '_self');
          window.close();
        } catch (e) {}
      } else {
        setTimeout(tick, 1000);
      }
    }
    window.addEventListener('DOMContentLoaded', tick);
  </script>
  <meta http-equiv=\"refresh\" content=\"10;url=about:blank\">
</head>
<body>
  <div class=\"card\">
    <h1>👋 Sesión cerrada</h1>
    <p>Ya puedes volver a la terminal. Esta pestaña se cerrará automáticamente.</p>
    <div class=\"countdown\">Cerrando en <span id=\"secs\">5</span> segundos…</div>
    <a class=\"btn\" href=\"about:blank\">Cerrar ahora</a>
  </div>
</body>
</html>
"""
            self.wfile.write(html.encode("utf-8"))


def start_local_server(app_redirect: Optional[str] = None):
    server = HTTPServer(("localhost", 8000), CallbackHandler)
    # adjunta destino para que la página callback pueda redirigir
    server.app_redirect = app_redirect  # type: ignore[attr-defined]
    server.handle_request()
    return server.auth_code  # type: ignore[attr-defined]


# =====================
# AUTH FLOW
# =====================
def login(app_redirect: Optional[str] = None):
    code_verifier, code_challenge = generate_pkce_pair()

    auth_url = (
        f"{COGNITO_DOMAIN}/oauth2/authorize?"
        f"response_type=code&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope={' '.join(SCOPES)}"
        f"&code_challenge={code_challenge}&code_challenge_method=S256"
    )

    console.print(
        Panel.fit(
            "Abriendo navegador para autenticación…\n\n"
            "Si no se abre automáticamente, copia y pega esta URL:\n"
            f"[cyan]{auth_url}[/cyan]",
            title="[bold cyan]CoreCLI · Login",
            border_style="cyan",
        )
    )
    webbrowser.open(auth_url)

    auth_code = start_local_server(app_redirect=app_redirect)
    if not auth_code:
        console.print(
            Panel(
                "No se recibió el código de autorización.", title="[red]Error", border_style="red"
            )
        )
        raise Exception("No se recibió el código de autorización.")

    token_url = f"{COGNITO_DOMAIN}/oauth2/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "code": auth_code,
        "code_verifier": code_verifier,
    }

    resp = requests.post(
        token_url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    resp.raise_for_status()
    tokens = resp.json()

    save_tokens(tokens)
    console.print(
        Panel.fit(
            "✅ Autenticación exitosa, tokens guardados.", border_style="green", title="[green]OK"
        )
    )


def refresh_tokens():
    tokens = load_tokens()
    if not tokens or "refresh_token" not in tokens:
        console.print(
            Panel.fit(
                "No hay refresh token guardado. Ejecuta `core-login login` para autenticarse de nuevo.",
                title="[yellow]Aviso",
                border_style="yellow",
            )
        )
        return

    token_url = f"{COGNITO_DOMAIN}/oauth2/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "refresh_token": tokens["refresh_token"],
    }

    resp = requests.post(
        token_url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    resp.raise_for_status()
    new_tokens = resp.json()

    if "refresh_token" not in new_tokens:
        new_tokens["refresh_token"] = tokens["refresh_token"]

    save_tokens(new_tokens)
    console.print(
        Panel.fit("🔄 Tokens refrescados correctamente.", border_style="green", title="[green]OK")
    )


def whoami():
    tokens = load_tokens()
    if not tokens or "id_token" not in tokens:
        console.print(
            Panel.fit(
                "No hay sesión activa. Ejecuta `core-login login` primero.",
                title="[yellow]Aviso",
                border_style="yellow",
            )
        )
        return

    id_token = tokens["id_token"]
    claims = decode_jwt(id_token)

    table = Table(
        title="👤 Usuario autenticado",
        show_header=False,
        box=box.SIMPLE,
        padding=(0, 1),
        border_style="cyan",
    )
    table.add_row("sub", f"[white]{claims.get('sub')}[/white]")
    table.add_row("email", f"[white]{claims.get('email')}[/white]")
    table.add_row("username", f"[white]{claims.get('cognito:username')}[/white]")
    console.print(table)


def logout(local_only: bool = True):
    """Cierra sesión local: revoca refresh token (best-effort) y borra tokens locales."""
    tokens = load_tokens()

    # Revocación opcional de refresh_token (si el pool lo permite)
    try:
        if tokens and tokens.get("refresh_token"):
            revoke_url = f"{COGNITO_DOMAIN}/oauth2/revoke"
            data = {
                "token": tokens["refresh_token"],
                "client_id": CLIENT_ID,
            }
            # best-effort
            requests.post(
                revoke_url,
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=5,
            )
    except Exception:
        pass

    # Borra tokens locales
    cleared = clear_tokens()

    # Ya no se abre Hosted UI: logout 100% local

    if cleared:
        console.print(
            Panel.fit("🧹 Tokens locales eliminados.", border_style="green", title="[green]OK")
        )
    else:
        console.print(
            Panel.fit(
                "No se pudieron borrar los tokens locales.", border_style="red", title="[red]Aviso"
            )
        )
