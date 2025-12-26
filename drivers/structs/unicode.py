from ctypes import Structure, c_wchar_p
from ctypes.wintypes import USHORT

class UNICODE_STRING(Structure):
    _fields_ = [("Length", USHORT), ("MaximumLength", USHORT), ("Buffer", c_wchar_p)]
    _buffer_ref = None