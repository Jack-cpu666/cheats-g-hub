"""
Logitech G Hub Driver Integration
Uses G Hub's internal driver for mouse/keyboard input
Device path: \\??\\ROOT#SYSTEM#000X#{1abc05c0-c378-41b9-9cef-df1aba82b015}
IOCTL: 0x2a2010
"""

import ctypes
import ctypes.wintypes as wintypes
from ctypes import windll
import logging

# G Hub IOCTL code
IOCTL_GHUB_MOUSE = 0x2a2010

# Click masks
MOUSE_LEFT_DOWN = 0x01
MOUSE_LEFT_UP = 0x00
MOUSE_RIGHT_DOWN = 0x02
MOUSE_RIGHT_UP = 0x00


def clamp_char(value: int) -> int:
    """Clamp value to signed char range (-128 to 127)"""
    return max(-128, min(127, value))


class GHUB_MOUSE_IO(ctypes.Structure):
    """G Hub mouse input structure - 5 bytes"""
    _fields_ = [
        ("button", ctypes.c_char),   # Button state
        ("x", ctypes.c_char),        # X delta (-128 to 127)
        ("y", ctypes.c_char),        # Y delta (-128 to 127)
        ("wheel", ctypes.c_char),    # Wheel delta
        ("unk1", ctypes.c_char)      # Unknown/padding
    ]


def _DeviceIoControl(devhandle, ioctl, inbuf, inbufsiz, outbuf, outbufsiz):
    """Low-level DeviceIoControl wrapper"""
    DeviceIoControl_Fn = windll.kernel32.DeviceIoControl
    DeviceIoControl_Fn.argtypes = [
        wintypes.HANDLE,
        wintypes.DWORD,
        wintypes.LPVOID,
        wintypes.DWORD,
        wintypes.LPVOID,
        wintypes.DWORD,
        ctypes.POINTER(wintypes.DWORD),
        wintypes.LPVOID
    ]
    DeviceIoControl_Fn.restype = wintypes.BOOL
    
    dwBytesReturned = wintypes.DWORD(0)
    lpBytesReturned = ctypes.byref(dwBytesReturned)
    status = DeviceIoControl_Fn(
        int(devhandle),
        ioctl,
        inbuf,
        inbufsiz,
        outbuf,
        outbufsiz,
        lpBytesReturned,
        None
    )
    return status, dwBytesReturned


class GHUB:
    """Logitech G Hub driver interface - compatible API with RZCONTROL"""
    hDevice = None
    _initialized = False
    
    def __init__(self):
        pass
    
    def _device_initialize(self, device_name: str) -> bool:
        """Initialize device handle"""
        try:
            # Use CreateFileW from kernel32
            kernel32 = windll.kernel32
            kernel32.CreateFileW.restype = wintypes.HANDLE
            kernel32.CreateFileW.argtypes = [
                wintypes.LPCWSTR,
                wintypes.DWORD,
                wintypes.DWORD,
                wintypes.LPVOID,
                wintypes.DWORD,
                wintypes.DWORD,
                wintypes.HANDLE
            ]
            
            GENERIC_WRITE = 0x40000000
            OPEN_EXISTING = 3
            FILE_ATTRIBUTE_NORMAL = 0x80
            
            handle = kernel32.CreateFileW(
                device_name,
                GENERIC_WRITE,
                0,
                None,
                OPEN_EXISTING,
                FILE_ATTRIBUTE_NORMAL,
                None
            )
            
            INVALID_HANDLE = wintypes.HANDLE(-1).value
            if handle and handle != INVALID_HANDLE:
                GHUB.hDevice = handle
                return True
            return False
        except Exception as e:
            logging.error(f"GHUB device init error: {e}")
            return False
    
    def init(self) -> bool:
        """Initialize G Hub driver - scans for device"""
        if GHUB._initialized and GHUB.hDevice:
            return True
        
        # Device path pattern for G Hub
        GHUB_GUID = "{1abc05c0-c378-41b9-9cef-df1aba82b015}"
        
        # Try multiple device path formats and indices
        # Format 1: Standard 4-digit index (0001, 0002, etc.)
        for i in range(0, 10):
            devpath = f"\\\\?\\ROOT#SYSTEM#{i:04d}#{GHUB_GUID}"
            if self._device_initialize(devpath):
                GHUB._initialized = True
                logging.info(f"G Hub driver initialized: {devpath}")
                return True
        
        # Format 2: Try with \\.\\ prefix
        for i in range(0, 10):
            devpath = f"\\\\.\\ROOT#SYSTEM#{i:04d}#{GHUB_GUID}"
            if self._device_initialize(devpath):
                GHUB._initialized = True
                logging.info(f"G Hub driver initialized: {devpath}")
                return True
        
        logging.error("G Hub driver not found - is Logitech G Hub installed and running?")
        return False
    
    def _call_mouse(self, buffer: GHUB_MOUSE_IO) -> bool:
        """Send mouse input via IOCTL"""
        if not GHUB.hDevice:
            return False
        
        status, _ = _DeviceIoControl(
            GHUB.hDevice,
            IOCTL_GHUB_MOUSE,
            ctypes.c_void_p(ctypes.addressof(buffer)),
            ctypes.sizeof(buffer),
            None,
            0
        )
        
        if not status:
            logging.warning("GHUB DeviceIoControl failed")
            # Try to reinitialize
            GHUB._initialized = False
            GHUB.hDevice = None
        
        return status
    
    def mouse_move(self, x: int, y: int, from_start_point: bool = False):
        """
        Move mouse by relative delta
        Compatible with RZCONTROL.mouse_move() API
        
        Args:
            x: X delta (will be clamped to -128..127)
            y: Y delta (will be clamped to -128..127)
            from_start_point: Ignored for G Hub (always relative)
        """
        if not GHUB._initialized:
            if not self.init():
                return
        
        # G Hub uses signed char for delta, need to handle large movements
        # by breaking them into smaller chunks
        remaining_x = x
        remaining_y = y
        
        while remaining_x != 0 or remaining_y != 0:
            # Clamp to signed char range
            move_x = clamp_char(remaining_x)
            move_y = clamp_char(remaining_y)
            
            io = GHUB_MOUSE_IO()
            io.button = ctypes.c_char(b'\x00')
            io.x = ctypes.c_char(move_x.to_bytes(1, 'little', signed=True))
            io.y = ctypes.c_char(move_y.to_bytes(1, 'little', signed=True))
            io.wheel = ctypes.c_char(b'\x00')
            io.unk1 = ctypes.c_char(b'\x00')
            
            if not self._call_mouse(io):
                break
            
            remaining_x -= move_x
            remaining_y -= move_y
    
    def mouse_click(self, click_mask: int):
        """
        Send mouse click
        Compatible with RZCONTROL.mouse_click() API
        
        Args:
            click_mask: Button mask (1=left, 2=right, etc)
        """
        if not GHUB._initialized:
            if not self.init():
                return
        
        io = GHUB_MOUSE_IO()
        io.button = ctypes.c_char(clamp_char(click_mask).to_bytes(1, 'little', signed=True))
        io.x = ctypes.c_char(b'\x00')
        io.y = ctypes.c_char(b'\x00')
        io.wheel = ctypes.c_char(b'\x00')
        io.unk1 = ctypes.c_char(b'\x00')
        
        self._call_mouse(io)
    
    def keyboard_input(self, scan_code: int, up_down: int):
        """
        Keyboard input - NOT SUPPORTED by G Hub mouse driver
        This is a stub for API compatibility with RZCONTROL
        """
        logging.warning("GHUB keyboard_input not supported - use separate keyboard driver")
        pass
    
    def close(self):
        """Close device handle"""
        if GHUB.hDevice:
            try:
                windll.kernel32.CloseHandle(GHUB.hDevice)
            except Exception:
                pass
            GHUB.hDevice = None
            GHUB._initialized = False


# Alias for backwards compatibility
RZCONTROL = GHUB
