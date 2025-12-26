"""
Advanced Anti-Detection Module

This module provides additional techniques to evade anti-cheat detection:
1. Code flow obfuscation (dummy operations)
2. Anti-screenshot/capture detection
3. Window detection (anti-cheat GUIs)
4. Trace cleaning
5. System call timing obfuscation
6. Process integrity checks
"""

import os
import sys
import ctypes
import random
import time
import string
import hashlib
from typing import List, Tuple, Optional
from ctypes import wintypes


# Anti-cheat window class names and titles to detect
ANTICHEAT_WINDOWS = [
    "vgtray",           # Vanguard tray
    "vgc",              # Vanguard client
    "EasyAntiCheat",
    "BEClient",         # BattlEye
    "BEService",
    "PnkBstrA",         # PunkBuster
    "PnkBstrB",
]

CAPTURE_SOFTWARE = [
    "obs64.exe",
    "obs32.exe",
    "streamlabs",
    "xsplit",
    "action.exe",       # Mirillis Action
    "bandicam.exe",
    "fraps.exe",
    "nvidia share",
    "geforce experience",
]


def dummy_operation():
    """
    Performs meaningless operations to obfuscate code flow.
    Call this randomly throughout execution.
    """
    operations = [
        lambda: sum(range(random.randint(1, 100))),
        lambda: "".join(random.choices(string.ascii_letters, k=random.randint(5, 20))),
        lambda: hashlib.md5(str(random.random()).encode()).hexdigest(),
        lambda: [x ** 2 for x in range(random.randint(1, 50))],
        lambda: sorted([random.random() for _ in range(random.randint(5, 20))]),
    ]
    random.choice(operations)()


def obfuscated_sleep(base_ms: float):
    """
    Sleep with timing obfuscation - splits into multiple smaller sleeps
    with dummy operations in between.
    """
    total_ms = base_ms + random.uniform(-base_ms * 0.1, base_ms * 0.1)
    chunks = random.randint(2, 5)
    chunk_ms = total_ms / chunks
    
    for _ in range(chunks):
        time.sleep(chunk_ms / 1000.0)
        if random.random() < 0.3:
            dummy_operation()


def get_running_processes() -> List[str]:
    """
    Get list of running process names (Windows only).
    """
    if sys.platform != 'win32':
        return []
    
    try:
        import subprocess
        result = subprocess.run(
            ['tasklist', '/FO', 'CSV', '/NH'],
            capture_output=True,
            text=True,
            timeout=5
        )
        processes = []
        for line in result.stdout.strip().split('\n'):
            if line:
                parts = line.split('","')
                if parts:
                    name = parts[0].strip('"').lower()
                    processes.append(name)
        return processes
    except Exception:
        return []


def is_capture_software_running() -> bool:
    """
    Check if screen capture software is running.
    """
    processes = get_running_processes()
    for capture in CAPTURE_SOFTWARE:
        if capture.lower() in processes:
            return True
    return False


def find_window_by_class(class_name: str) -> bool:
    """
    Check if a window with given class name exists.
    """
    if sys.platform != 'win32':
        return False
    
    try:
        user32 = ctypes.windll.user32
        hwnd = user32.FindWindowW(class_name, None)
        return hwnd != 0
    except Exception:
        return False


def is_anticheat_window_visible() -> bool:
    """
    Check if any known anti-cheat windows are visible.
    """
    for class_name in ANTICHEAT_WINDOWS:
        if find_window_by_class(class_name):
            return True
    return False


def clean_traces():
    """
    Clean temporary files and traces that might identify the software.
    """
    if sys.platform != 'win32':
        return
    
    try:
        temp_dir = os.environ.get('TEMP', '')
        if not temp_dir:
            return
        
        # Look for any files we might have created
        suspicious_patterns = [
            '.pyc',
            '__pycache__',
        ]
        
        # Clean __pycache__ directories in our folder
        script_dir = os.path.dirname(os.path.abspath(__file__))
        for root, dirs, files in os.walk(script_dir):
            for d in dirs:
                if d == '__pycache__':
                    cache_path = os.path.join(root, d)
                    try:
                        import shutil
                        shutil.rmtree(cache_path, ignore_errors=True)
                    except Exception:
                        pass
    except Exception:
        pass


def randomize_import_timing():
    """
    Add random delays between imports to avoid timing fingerprinting.
    """
    time.sleep(random.uniform(0.001, 0.01))


def check_virtual_machine() -> bool:
    """
    Basic VM detection - some anti-cheats flag VMs.
    Returns True if running in a VM.
    """
    if sys.platform != 'win32':
        return False
    
    vm_indicators = [
        "vmware",
        "virtualbox",
        "vbox",
        "qemu",
        "xen",
        "hyper-v",
    ]
    
    try:
        import subprocess
        result = subprocess.run(
            ['systeminfo'],
            capture_output=True,
            text=True,
            timeout=10
        )
        output_lower = result.stdout.lower()
        
        for indicator in vm_indicators:
            if indicator in output_lower:
                return True
        return False
    except Exception:
        return False


def get_system_uptime_ms() -> int:
    """
    Get system uptime in milliseconds.
    Very low uptime can indicate fresh VM or suspicious behavior.
    """
    if sys.platform != 'win32':
        return 999999999
    
    try:
        return ctypes.windll.kernel32.GetTickCount64()
    except Exception:
        return 999999999


def is_system_freshly_booted(threshold_minutes: int = 5) -> bool:
    """
    Check if system was booted very recently (suspicious for anti-cheat).
    """
    uptime_ms = get_system_uptime_ms()
    uptime_minutes = uptime_ms / (1000 * 60)
    return uptime_minutes < threshold_minutes


class IntegrityChecker:
    """
    Monitors for tampering with the running process.
    """
    
    def __init__(self):
        self._checkpoints = {}
        
    def set_checkpoint(self, name: str, value: any):
        """Store a value that shouldn't change."""
        self._checkpoints[name] = hash(str(value))
        
    def verify_checkpoint(self, name: str, value: any) -> bool:
        """Verify a value hasn't changed."""
        if name not in self._checkpoints:
            return True
        return self._checkpoints[name] == hash(str(value))
    
    def verify_all(self, values: dict) -> bool:
        """Verify multiple checkpoints at once."""
        for name, value in values.items():
            if not self.verify_checkpoint(name, value):
                return False
        return True


# Global integrity checker
integrity_checker = IntegrityChecker()


def add_execution_noise():
    """
    Add random noise to execution to avoid timing patterns.
    Call this periodically throughout main loops.
    """
    if random.random() < 0.1:  # 10% chance
        dummy_operation()
    
    if random.random() < 0.05:  # 5% chance
        obfuscated_sleep(random.uniform(1, 5))


def generate_fake_activity():
    """
    Generate fake system activity to blend in.
    """
    operations = [
        lambda: os.path.exists(f"C:\\Windows\\System32\\{random.choice(['kernel32.dll', 'user32.dll', 'ntdll.dll'])}"),
        lambda: os.getcwd(),
        lambda: os.getpid(),
        lambda: time.time(),
    ]
    random.choice(operations)()
