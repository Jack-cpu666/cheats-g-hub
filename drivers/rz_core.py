import ctypes
import logging
from ctypes.wintypes import HANDLE, DWORD
from drivers.native import get_libs
from drivers.defines.flags import *
from drivers.structs.ioctl import RZCONTROL_IOCTL_STRUCT
from drivers.utils import find_sym_link, INVALID_HANDLE_VALUE
from core.security import _, STR_RZCONTROL

IOCTL_MOUSE = 0x88883020
MAX_VAL = 65536
RZCONTROL_MOUSE = 2
RZCONTROL_KEYBOARD = 1

class RZCONTROL:
    hDevice = HANDLE(INVALID_HANDLE_VALUE)

    def init(self):
        ntdll, kernel32 = get_libs()
        if not ntdll or not kernel32:
            logging.error("ntdll or kernel32 not available")
            RZCONTROL.hDevice = HANDLE(INVALID_HANDLE_VALUE)
            return False
        
        # Close existing handle if valid
        if RZCONTROL.hDevice and hasattr(RZCONTROL.hDevice, 'value') and RZCONTROL.hDevice.value != INVALID_HANDLE_VALUE:
            try:
                kernel32.CloseHandle(RZCONTROL.hDevice)
            except Exception:
                pass
            RZCONTROL.hDevice = HANDLE(INVALID_HANDLE_VALUE)
        
        # Find the driver symlink using encrypted string
        target_name = _(STR_RZCONTROL)
        found, name = find_sym_link("\\GLOBAL??", target_name)
        if not found or not name:
            logging.error(f"Driver not found in \\GLOBAL??")
            RZCONTROL.hDevice = HANDLE(INVALID_HANDLE_VALUE)
            return False
        
        # Build the symlink path
        sym_link = "\\\\?\\" + name
        logging.info(f"Attempting to open device: {sym_link}")
        
        # Set up CreateFileW properly
        try:
            kernel32.CreateFileW.restype = HANDLE
            kernel32.CreateFileW.argtypes = [ctypes.c_wchar_p, DWORD, DWORD, ctypes.c_void_p, DWORD, DWORD, HANDLE]
        except Exception:
            pass
        
        dwDesiredAccess = DWORD(GENERIC_READ | GENERIC_WRITE)
        dwShareMode = DWORD(FILE_SHARE_READ | FILE_SHARE_WRITE)
        dwCreationDisposition = DWORD(OPEN_EXISTING)
        dwFlagsAndAttributes = DWORD(0)
        
        try:
            temp_handle = kernel32.CreateFileW(
                ctypes.c_wchar_p(sym_link), 
                dwDesiredAccess, 
                dwShareMode, 
                None, 
                dwCreationDisposition, 
                dwFlagsAndAttributes, 
                None
            )
            RZCONTROL.hDevice = temp_handle
        except Exception as e:
            logging.error(f"CreateFileW failed: {e}")
            RZCONTROL.hDevice = HANDLE(INVALID_HANDLE_VALUE)
            return False
        
        handle_value_to_check = getattr(RZCONTROL.hDevice, 'value', RZCONTROL.hDevice)
        if handle_value_to_check == INVALID_HANDLE_VALUE:
            logging.error("CreateFileW returned INVALID_HANDLE_VALUE")
            if not isinstance(RZCONTROL.hDevice, HANDLE):
                RZCONTROL.hDevice = HANDLE(INVALID_HANDLE_VALUE)
            return False
        else:
            if not isinstance(RZCONTROL.hDevice, HANDLE):
                try:
                    RZCONTROL.hDevice = HANDLE(handle_value_to_check)
                except Exception:
                    pass
            logging.info(f"Driver opened successfully, handle: {handle_value_to_check}")
            return True

    def impl_mouse_ioctl(self, ioctl_struct):
        _, kernel32 = get_libs()
        if not kernel32:
            return
        if not ioctl_struct:
            return
        
        handle_value_to_check = getattr(RZCONTROL.hDevice, 'value', RZCONTROL.hDevice)
        if handle_value_to_check == INVALID_HANDLE_VALUE:
            # Try to reinitialize
            if not self.init():
                return
        
        p_ioctl = ctypes.pointer(ioctl_struct)
        bytes_returned = DWORD(0)
        bResult = False
        
        try:
            bResult = kernel32.DeviceIoControl(
                RZCONTROL.hDevice, 
                IOCTL_MOUSE, 
                p_ioctl, 
                ctypes.sizeof(RZCONTROL_IOCTL_STRUCT), 
                None, 0, 
                ctypes.byref(bytes_returned), 
                None
            )
        except Exception as e:
            logging.error(f"DeviceIoControl failed: {e}")
            bResult = False
        
        if not bResult:
            pass

    def mouse_move(self, x, y, from_start_point):
        max_val = 0
        if not from_start_point:
            max_val = MAX_VAL
            x = max(1, min(x, max_val))
            y = max(1, min(y, max_val))
        mm = RZCONTROL_IOCTL_STRUCT(
            unk0=0, 
            unk1=RZCONTROL_MOUSE, 
            max_val_or_scan_code=max_val, 
            click_mask=0, 
            unk3=0, 
            x=x, 
            y=y, 
            unk4=0
        )
        self.impl_mouse_ioctl(mm)

    def mouse_click(self, click_mask):
        mm = RZCONTROL_IOCTL_STRUCT(
            unk0=0, 
            unk1=RZCONTROL_MOUSE, 
            max_val_or_scan_code=0, 
            click_mask=click_mask, 
            unk3=0, 
            x=0, 
            y=0, 
            unk4=0
        )
        self.impl_mouse_ioctl(mm)

    def keyboard_input(self, scan_code, up_down):
        packed_scan_code = int(scan_code) << 16
        mm = RZCONTROL_IOCTL_STRUCT(
            unk0=0, 
            unk1=RZCONTROL_KEYBOARD, 
            max_val_or_scan_code=packed_scan_code, 
            click_mask=up_down, 
            unk3=0, 
            x=0, 
            y=0, 
            unk4=0
        )
        self.impl_mouse_ioctl(mm)