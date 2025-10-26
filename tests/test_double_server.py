# tests/test_double_server.py
import subprocess
import time

def test_double_server_start():
    # Primer servidor
    server1 = subprocess.Popen(["python", "src/singletonproxyobserver.py", "-p=8080"])
    time.sleep(2)

    # Segundo servidor en el mismo puerto → debe fallar
    result = subprocess.run(["python", "src/singletonproxyobserver.py", "-p=8080"], capture_output=True)
    assert result.returncode != 0
    assert b"Address already in use" in result.stderr or b"OSError" in result.stderr

    server1.terminate()
