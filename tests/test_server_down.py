# tests/test_server_down.py
import subprocess
import json

def test_server_unavailable():
    # Servidor no está corriendo
    input_data = {
        "UUID": "CPU-TEST-003",
        "ACTION": "list"
    }
    with open("input_down.json", "w") as f:
        json.dump(input_data, f)

    result = subprocess.run(
        ["python", "src/singletonclient.py", "-i=input_down.json", "-o=out_down.json"],
        capture_output=True
    )

    # Esperamos un error de conexión
    assert result.returncode != 0
    assert b"Error" in result.stderr or b"Connection" in result.stdout
