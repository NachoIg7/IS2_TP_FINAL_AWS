# tests/test_invalid_args.py
import subprocess

def test_invalid_arguments():
    # Falta argumento obligatorio -i
    result = subprocess.run(["python", "singletonclient.py"], capture_output=True)
    assert result.returncode != 0
    assert b"Error" in result.stderr or b"usage" in result.stdout
