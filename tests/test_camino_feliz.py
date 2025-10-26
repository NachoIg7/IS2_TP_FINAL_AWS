import subprocess
import time
import json
import os

def test_happy_path_all_actions():
    # --- Levantar servidor ---
    server = subprocess.Popen(["python", "singletonproxyobserver.py", "-p=8080"], cwd="src")
    time.sleep(2)

    # --- Acción SET ---
    input_set = {
        "UUID": "CPU-TEST-001",
        "ACTION": "set",
        "id": "UADER-FCyT-IS2",
        "cp": "3260",
        "CUIT": "30-70925411-8",
        "domicilio": "25 de Mayo 385-1P",
        "localidad": "Concepción del Uruguay",
        "provincia": "Entre Rios",
        "telefono": "03442 43-1442",
        "web": "http://www.uader.edu.ar"
    }
    with open("src/input_set.json", "w") as f:
        json.dump(input_set, f)

    subprocess.run(["python", "singletonclient.py", "-i=input_set.json", "-o=out_set.json", "-v"], cwd="src")
    assert os.path.exists("src/out_set.json")

    # --- Acción GET ---
    input_get = {
        "UUID": "CPU-TEST-001",
        "ACTION": "get",
        "id": "UADER-FCyT-IS2"
    }
    with open("src/input_get.json", "w") as f:
        json.dump(input_get, f)

    subprocess.run(["python", "singletonclient.py", "-i=input_get.json", "-o=out_get.json", "-v"], cwd="src")
    assert os.path.exists("src/out_get.json")

    # --- Verificar contenido ---
    with open("src/out_get.json") as f:
        data = json.load(f)
    assert data["id"] == "UADER-FCyT-IS2"

    server.terminate()
