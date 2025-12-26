import socket

def get_local_ip():
    ip = '127.0.0.1'
    try:
        host_name = socket.gethostname()
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(0.1)
            try:
                s.connect(('8.8.8.8', 1))
                ip = s.getsockname()[0]
            except Exception: pass
    except Exception: pass
    return ip