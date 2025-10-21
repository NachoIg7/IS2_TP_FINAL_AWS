# ============================================
# Programa: observerclient.py
# Autor: Camilo Escar
# Versión: 1.0
# Descripción: Cliente observador que se suscribe al servidor
#              y recibe actualizaciones en tiempo real.
# ============================================

import socket
import json
import argparse
import uuid
import time
import logging
from pathlib import Path

# --------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------
RETRY_DELAY = 30  # segundos entre reintentos de conexión
BUFFER_SIZE = 4096

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


def connect_and_subscribe(host, port, uuid_client, output_file):
    """Conecta al servidor, envía acción subscribe y espera actualizaciones."""
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
                msg = {"UUID": uuid_client, "ACTION": "subscribe"}
                s.sendall(json.dumps(msg).encode('utf-8'))

                logging.info(f"Suscrito al servidor {host}:{port}. Esperando actualizaciones...")

                # Escuchar mensajes infinitamente
                while True:
                    data = s.recv(BUFFER_SIZE)
                    if not data:
                        break
                    decoded = data.decode('utf-8')
                    print("\n📩 Actualización recibida:\n", decoded)

                    if output_file:
                        with open(output_file, "a") as f:
                            f.write(decoded + "\n")

        except Exception as e:
            logging.warning(f"Conexión interrumpida: {e}. Reintentando en {RETRY_DELAY}s...")
            time.sleep(RETRY_DELAY)


def main():
    parser = argparse.ArgumentParser(description="Cliente observador (subscribe)")
    parser.add_argument("-s", "--server", default="localhost", help="Host del servidor (default localhost)")
    parser.add_argument("-p", "--port", type=int, default=8080, help="Puerto del servidor (default 8080)")
    parser.add_argument("-o", "--output", help="Archivo para guardar actualizaciones")
    parser.add_argument("-v", "--verbose", action="store_true", help="Modo verboso")

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    uuid_client = str(uuid.getnode())
    connect_and_subscribe(args.server, args.port, uuid_client, args.output)


if __name__ == "__main__":
    main()
