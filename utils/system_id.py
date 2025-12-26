import subprocess
import re

def get_windows_uuid():
    try:
        ps_command = ["powershell", "-Command", "(Get-CimInstance -ClassName Win32_ComputerSystemProduct).UUID"]
        process = subprocess.run(ps_command, shell=False, capture_output=True, text=True, check=False, creationflags=subprocess.CREATE_NO_WINDOW)
        output = process.stdout.strip()
        if process.returncode == 0 and output and re.match(r"^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}$", output):
            return output
    except Exception:
        pass
    return None