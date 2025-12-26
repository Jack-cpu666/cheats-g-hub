from ctypes import Structure, POINTER, c_void_p
from ctypes.wintypes import ULONG, HANDLE
from drivers.structs.unicode import UNICODE_STRING

class OBJECT_ATTRIBUTES(Structure):
    _fields_ = [("Length", ULONG), ("RootDirectory", HANDLE), ("ObjectName", POINTER(UNICODE_STRING)),
                ("Attributes", ULONG), ("SecurityDescriptor", c_void_p), ("SecurityQualityOfService", c_void_p)]