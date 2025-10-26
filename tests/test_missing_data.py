# tests/test_missing_data.py
import subprocess
import json

def test_missing_minimum_fields():
    # Faltan datos mínimos (sin "action")
    bad_input = {"UUID": "CPU-TEST-002"}
    with open("input_bad.json", "w") as f:
        json.dump(bad_input, f)

    result = subprocess.run(
        ["python", "src/singletonclient.py", "-i=input_bad.json", "-o=out_bad.json"],
        capture_output=True
    )

    assert result.returncode != 0
