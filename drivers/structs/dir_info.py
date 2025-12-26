from ctypes import Structure
from drivers.structs.unicode import UNICODE_STRING

class OBJECT_DIRECTORY_INFORMATION(Structure):
    _fields_ = [("Name", UNICODE_STRING), ("TypeName", UNICODE_STRING)]