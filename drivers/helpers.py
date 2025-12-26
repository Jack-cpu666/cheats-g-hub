import ctypes
from ctypes import cast, addressof, sizeof, create_unicode_buffer, pointer, memset
from ctypes.wintypes import HANDLE, DWORD
from drivers.native import get_libs
from drivers.defines.ntstatus import *
from drivers.defines.flags import *
from drivers.structs.unicode import UNICODE_STRING
from drivers.structs.attributes import OBJECT_ATTRIBUTES

ntdll, _ = get_libs()

def RtlInitUnicodeString(DestinationString, Src):
    if not isinstance(Src, str): return STATUS_UNSUCCESSFUL
    try:
        buffer = create_unicode_buffer(Src)
        memset(addressof(DestinationString), 0, sizeof(DestinationString))
        DestinationString.Buffer = cast(buffer, ctypes.c_wchar_p)
        DestinationString.Length = (len(Src) * 2)
        DestinationString.MaximumLength = DestinationString.Length + 2
        DestinationString._buffer_ref = buffer
        return STATUS_SUCCESS
    except Exception: return STATUS_UNSUCCESSFUL