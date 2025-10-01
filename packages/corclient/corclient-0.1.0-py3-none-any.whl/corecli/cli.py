from typing import Optional

import typer

from corecli import auth

app = typer.Typer(help="CoreCLI - CLI de ejemplo con login en Cognito usando PKCE")


@app.command()
def login(
    app_redirect: Optional[str] = typer.Option(
        None,
        "--app-redirect",
        "-r",
        help="URL o esquema (p.ej. myapp://callback) al que redirigir tras login",
    ),
):
    """Inicia el flujo de autenticación con Cognito (Hosted UI + PKCE)."""
    auth.login(app_redirect=app_redirect)


@app.command()
def refresh():
    """Refresca los tokens usando refresh_token guardado."""
    auth.refresh_tokens()


@app.command()
def whoami():
    """Muestra información del usuario autenticado (id_token)."""
    auth.whoami()


@app.command()
def logout():
    """Cierra sesión local (revoca/borrado de tokens)."""
    auth.logout()


def main():
    """Compatibilidad: permite ejecutar como 'python -m corecli.cli' o entrypoint antiguo."""
    app()
