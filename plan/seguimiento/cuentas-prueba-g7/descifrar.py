"""Descifra las cuentas de prueba G7 en una carpeta local ignorada por Git."""

from __future__ import annotations

from getpass import getpass
from pathlib import Path
import sys

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


MAGIC = b"G7H4v1\x00"
ITERATIONS = 600_000
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
SOURCE = HERE / "g7-h4-cuentas.enc"
OUTPUT = REPO / ".local-private" / "g7-h4-cuentas.json"


def main() -> int:
    data = SOURCE.read_bytes()
    if not data.startswith(MAGIC) or len(data) < len(MAGIC) + 16 + 12 + 16:
        print("Archivo cifrado inválido.", file=sys.stderr)
        return 1
    salt = data[len(MAGIC) : len(MAGIC) + 16]
    nonce = data[len(MAGIC) + 16 : len(MAGIC) + 28]
    ciphertext = data[len(MAGIC) + 28 :]
    password = getpass("Contraseña para cuentas G7 H4: ")
    key = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITERATIONS
    ).derive(password.encode("utf-8"))
    try:
        plaintext = AESGCM(key).decrypt(nonce, ciphertext, MAGIC)
    except InvalidTag:
        print("Contraseña incorrecta o archivo alterado.", file=sys.stderr)
        return 1
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(plaintext)
    print(f"Archivo local creado: {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
