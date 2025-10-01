import base64
import json
import os
from typing import Any

CONFIG_DIR = os.path.expanduser("~/.corecli")
TOKENS_FILE = os.path.join(CONFIG_DIR, "tokens.json")


def save_tokens(tokens: dict):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(TOKENS_FILE, "w") as f:
        json.dump(tokens, f, indent=2)


def load_tokens():
    if os.path.exists(TOKENS_FILE):
        with open(TOKENS_FILE) as f:
            return json.load(f)
    return None


def decode_jwt(token: str) -> dict[str, Any]:
    """Decodifica un JWT (solo payload, sin validar firma)."""
    parts = token.split(".")
    if len(parts) != 3:
        raise ValueError("Token JWT inválido")

    payload_b64 = parts[1] + "=" * (-len(parts[1]) % 4)  # padding
    payload_json = base64.urlsafe_b64decode(payload_b64.encode()).decode()
    return json.loads(payload_json)  # type: ignore[no-any-return]


def clear_tokens() -> bool:
    """Elimina el archivo de tokens local si existe."""
    if os.path.exists(TOKENS_FILE):
        try:
            os.remove(TOKENS_FILE)
            return True
        except OSError:
            return False
    return True
