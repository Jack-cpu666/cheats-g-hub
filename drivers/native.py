from ctypes import windll
try:
    ntdll = windll.ntdll
    kernel32 = windll.kernel32
except OSError:
    ntdll = None
    kernel32 = None

def get_libs():
    return ntdll, kernel32