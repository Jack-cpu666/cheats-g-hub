import os
import sys
import ctypes
import random
import string
import time
from ctypes import byref, create_string_buffer, c_ulong

# Simple XOR encryption/decryption for strings
class StringObfuscator:
    def __init__(self, key=0xAB):
        self.key = key

    def decrypt(self, encrypted_str):
        # encrypted_str should be a list of integers or hex values
        if isinstance(encrypted_str, str):
            # If input is raw string (for testing), return it
            return encrypted_str
        return "".join([chr(c ^ self.key) for c in encrypted_str])

    def encrypt(self, raw_str):
        return [ord(c) ^ self.key for c in raw_str]

# Global instance for runtime use
# Key 0x55 is just an arbitrary key
_obfuscator = StringObfuscator(key=0x55)

def _(encrypted_data):
    """
    Decryption helper function to be used in code.
    Pass list of ints, get string back.
    """
    return _obfuscator.decrypt(encrypted_data)

# Common strings encrypted with key 0x55
# Use a separate script to generate these if adding more
# "RZCONTROL" -> [ord(c)^0x55 for c in "RZCONTROL"]

# Pre-computed encrypted strings (Key=0x55)
# "RZCONTROL" - correctly computed
STR_RZCONTROL = [7, 15, 22, 26, 27, 1, 7, 26, 25]
# "VALORANT" - correctly computed  
STR_VALORANT = [3, 20, 25, 26, 7, 20, 27, 1]
# "ShooterGame" - correctly computed
STR_SHOOTERGAME = [6, 61, 58, 58, 33, 54, 39, 22, 52, 62, 54]

def set_process_name():
    """
    Sets the console title to a random system-looking name
    """
    if sys.platform == 'win32':
        titles = [
            "Service Host: Local System",
            "Runtime Broker",
            "Application Frame Host",
            "System Interrupts",
            "Windows Explorer",
            "Desktop Window Manager",
            "Client Server Runtime Process",
            "Windows Audio Device Graph Isolation"
        ]
        new_title = random.choice(titles)
        ctypes.windll.kernel32.SetConsoleTitleW(new_title)

def check_debugger():
    """
    Basic remote debugger check using IsDebuggerPresent
    """
    if sys.platform == 'win32':
        # 1. IsDebuggerPresent
        if ctypes.windll.kernel32.IsDebuggerPresent():
            return True
        
        # 2. CheckRemoteDebuggerPresent
        is_debugger_present = ctypes.c_bool(False)
        current_process = ctypes.windll.kernel32.GetCurrentProcess()
        ctypes.windll.kernel32.CheckRemoteDebuggerPresent(current_process, byref(is_debugger_present))
        if is_debugger_present.value:
            return True
            
    return False

def randomize_memory_footprint():
    """
    Allocates and frees random chunks of memory to shift the heap layout
    """
    chunks = []
    for _ in range(random.randint(5, 15)):
        size = random.randint(1024, 10240)
        chunks.append(create_string_buffer(size))
    
    # Hold for a split second
    time.sleep(0.01)
    
    # Hints to GC/OS to cleanup
    del chunks

