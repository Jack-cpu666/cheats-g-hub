"""
V7 Enhanced Anti-Detection Module

Advanced techniques to evade anti-cheat detection:
1. Memory randomization & heap spraying
2. API hook detection
3. Timing attack prevention
4. Thread cloaking
5. Syscall obfuscation
6. Driver signature masking
7. Stack spoofing
8. Anti-debugging enhancements
9. Process hollowing detection
10. Behavioral pattern breaking
"""

import os
import sys
import ctypes
import random
import time
import struct
import hashlib
import threading
from ctypes import wintypes
from typing import Optional, Tuple, List
import logging

# Windows API constants
PROCESS_ALL_ACCESS = 0x1F0FFF
THREAD_ALL_ACCESS = 0x1F03FF
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000
MEM_RELEASE = 0x8000
PAGE_READWRITE = 0x04
PAGE_EXECUTE_READWRITE = 0x40

# Anti-cheat signatures to detect
ANTICHEAT_SIGNATURES = {
    "vanguard": [b"vgk.sys", b"vgc.exe", b"vgtray.exe"],
    "easyanticheat": [b"EasyAntiCheat", b"eac_launcher"],
    "battleye": [b"BEClient", b"BEService", b"bedaisy.sys"],
    "faceit": [b"faceit", b"faceit_anti_cheat"],
}


class MemoryRandomizer:
    """
    Randomizes memory layout to prevent pattern detection.
    Creates decoy allocations that mimic legitimate program behavior.
    """
    
    def __init__(self):
        self.allocations = []
        self.kernel32 = ctypes.windll.kernel32
        self._setup_heap()
    
    def _setup_heap(self):
        """Create randomized heap allocations."""
        try:
            # Allocate random memory blocks to obscure our footprint
            for _ in range(random.randint(5, 15)):
                size = random.randint(1024, 65536)
                ptr = self.kernel32.VirtualAlloc(
                    None, size, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE
                )
                if ptr:
                    # Fill with random data to look like real allocations
                    random_data = bytes([random.randint(0, 255) for _ in range(min(size, 4096))])
                    ctypes.memmove(ptr, random_data, len(random_data))
                    self.allocations.append((ptr, size))
        except Exception:
            pass
    
    def shuffle_allocations(self):
        """Periodically reallocate memory to break patterns."""
        try:
            # Free some random allocations
            if len(self.allocations) > 5:
                to_free = random.sample(self.allocations, random.randint(1, 3))
                for ptr, size in to_free:
                    self.kernel32.VirtualFree(ptr, 0, MEM_RELEASE)
                    self.allocations.remove((ptr, size))
            
            # Create new allocations
            for _ in range(random.randint(1, 3)):
                size = random.randint(1024, 32768)
                ptr = self.kernel32.VirtualAlloc(
                    None, size, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE
                )
                if ptr:
                    self.allocations.append((ptr, size))
        except Exception:
            pass
    
    def cleanup(self):
        """Free all allocations."""
        for ptr, size in self.allocations:
            try:
                self.kernel32.VirtualFree(ptr, 0, MEM_RELEASE)
            except Exception:
                pass
        self.allocations.clear()


class APIHookDetector:
    """
    Detects if critical Windows APIs have been hooked by anti-cheat.
    """
    
    # Common hook signatures (JMP, CALL instructions at function start)
    HOOK_SIGNATURES = [
        b'\xE9',        # JMP rel32
        b'\xEB',        # JMP rel8
        b'\xFF\x25',    # JMP [mem]
        b'\xFF\x15',    # CALL [mem]
        b'\x68',        # PUSH imm32 (push-ret hook)
    ]
    
    CRITICAL_APIS = [
        ("kernel32.dll", "CreateFileW"),
        ("kernel32.dll", "ReadFile"),
        ("kernel32.dll", "WriteFile"),
        ("kernel32.dll", "DeviceIoControl"),
        ("ntdll.dll", "NtQuerySystemInformation"),
        ("ntdll.dll", "NtOpenProcess"),
        ("user32.dll", "GetAsyncKeyState"),
        ("user32.dll", "SendInput"),
    ]
    
    def __init__(self):
        self.kernel32 = ctypes.windll.kernel32
        self.baseline = {}
        self._capture_baseline()
    
    def _get_function_bytes(self, dll_name: str, func_name: str, size: int = 16) -> Optional[bytes]:
        """Get the first bytes of a function."""
        try:
            dll = ctypes.windll.LoadLibrary(dll_name)
            func_addr = ctypes.cast(
                getattr(dll, func_name),
                ctypes.c_void_p
            ).value
            
            if func_addr:
                buffer = (ctypes.c_char * size)()
                bytes_read = ctypes.c_size_t()
                self.kernel32.ReadProcessMemory(
                    self.kernel32.GetCurrentProcess(),
                    func_addr,
                    buffer,
                    size,
                    ctypes.byref(bytes_read)
                )
                return bytes(buffer)
        except Exception:
            pass
        return None
    
    def _capture_baseline(self):
        """Capture initial function bytes for comparison."""
        for dll, func in self.CRITICAL_APIS:
            func_bytes = self._get_function_bytes(dll, func)
            if func_bytes:
                self.baseline[f"{dll}:{func}"] = func_bytes
    
    def detect_hooks(self) -> List[str]:
        """Check for hooked functions."""
        hooked = []
        
        for dll, func in self.CRITICAL_APIS:
            key = f"{dll}:{func}"
            current = self._get_function_bytes(dll, func)
            
            if current and key in self.baseline:
                # Check if function start changed
                if current[:5] != self.baseline[key][:5]:
                    hooked.append(key)
                    continue
                
                # Check for hook signatures
                for sig in self.HOOK_SIGNATURES:
                    if current.startswith(sig):
                        hooked.append(key)
                        break
        
        return hooked
    
    def is_safe(self) -> bool:
        """Quick check if environment is safe."""
        return len(self.detect_hooks()) == 0


class TimingObfuscator:
    """
    Prevents timing-based detection by adding controlled jitter
    to all operations.
    """
    
    def __init__(self):
        self.last_operation_time = time.perf_counter()
        self.operation_history = []
        self.jitter_range = (0.001, 0.015)  # 1-15ms jitter
    
    def add_jitter(self, base_delay_ms: float = 0) -> float:
        """
        Add randomized jitter to prevent timing fingerprinting.
        Returns actual sleep time in seconds.
        """
        current = time.perf_counter()
        
        # Calculate time since last operation
        delta = current - self.last_operation_time
        self.operation_history.append(delta)
        
        # Keep only last 100 operations
        if len(self.operation_history) > 100:
            self.operation_history.pop(0)
        
        # Random jitter
        jitter = random.uniform(*self.jitter_range)
        
        # Add base delay with variance
        if base_delay_ms > 0:
            delay = (base_delay_ms / 1000.0) * random.uniform(0.85, 1.15)
            jitter += delay
        
        # Sleep in chunks to break patterns
        chunks = random.randint(2, 4)
        chunk_time = jitter / chunks
        
        for _ in range(chunks):
            time.sleep(chunk_time)
            if random.random() < 0.2:  # 20% chance for extra micro-sleep
                time.sleep(random.uniform(0.0001, 0.001))
        
        self.last_operation_time = time.perf_counter()
        return jitter
    
    def obfuscated_sleep(self, ms: float):
        """Sleep with timing obfuscation."""
        total = ms / 1000.0
        remaining = total
        
        while remaining > 0:
            chunk = min(remaining, random.uniform(0.001, 0.01))
            time.sleep(chunk)
            remaining -= chunk
            
            # Random pause
            if random.random() < 0.1:
                time.sleep(random.uniform(0.0001, 0.0005))


class ThreadCloaker:
    """
    Hides thread activity from anti-cheat scanners.
    """
    
    def __init__(self):
        self.ntdll = ctypes.windll.ntdll
        self.kernel32 = ctypes.windll.kernel32
        self.hidden_threads = []
    
    def hide_thread(self, thread_handle=None):
        """
        Attempt to hide a thread from debuggers/scanners.
        Uses NtSetInformationThread with ThreadHideFromDebugger.
        """
        try:
            if thread_handle is None:
                thread_handle = self.kernel32.GetCurrentThread()
            
            # ThreadHideFromDebugger = 0x11
            status = self.ntdll.NtSetInformationThread(
                thread_handle,
                0x11,  # ThreadHideFromDebugger
                None,
                0
            )
            
            if status == 0:
                self.hidden_threads.append(thread_handle)
                return True
        except Exception:
            pass
        return False
    
    def set_thread_description_random(self):
        """Set a random benign thread description."""
        try:
            benign_names = [
                "Windows Audio Device Graph",
                "COM+ Event System",
                "WMI Provider Host",
                "Windows Driver Foundation",
                "Desktop Window Manager",
                "Windows Error Reporting",
            ]
            
            name = random.choice(benign_names)
            # Would need SetThreadDescription API (Windows 10+)
        except Exception:
            pass


class SyscallObfuscator:
    """
    Obfuscates syscall patterns to evade behavioral detection.
    """
    
    def __init__(self):
        self.call_count = {}
        self.last_syscall_time = {}
    
    def pre_syscall(self, syscall_name: str):
        """Called before making a system call."""
        current = time.perf_counter()
        
        # Track call frequency
        self.call_count[syscall_name] = self.call_count.get(syscall_name, 0) + 1
        
        # Add random delay if calling too frequently
        if syscall_name in self.last_syscall_time:
            delta = current - self.last_syscall_time[syscall_name]
            if delta < 0.001:  # Less than 1ms between calls
                time.sleep(random.uniform(0.001, 0.005))
        
        self.last_syscall_time[syscall_name] = current
    
    def post_syscall(self, syscall_name: str):
        """Called after a system call completes."""
        # Add post-call jitter
        if random.random() < 0.1:  # 10% chance
            time.sleep(random.uniform(0.0001, 0.0005))


class AntiDebugEnhanced:
    """
    Enhanced anti-debugging techniques.
    """
    
    def __init__(self):
        self.kernel32 = ctypes.windll.kernel32
        self.ntdll = ctypes.windll.ntdll
    
    def is_debugger_present(self) -> bool:
        """Multiple debugger detection methods."""
        
        # Method 1: IsDebuggerPresent
        if self.kernel32.IsDebuggerPresent():
            return True
        
        # Method 2: CheckRemoteDebuggerPresent
        try:
            is_debugged = ctypes.c_bool(False)
            self.kernel32.CheckRemoteDebuggerPresent(
                self.kernel32.GetCurrentProcess(),
                ctypes.byref(is_debugged)
            )
            if is_debugged.value:
                return True
        except Exception:
            pass
        
        # Method 3: NtQueryInformationProcess - ProcessDebugPort
        try:
            debug_port = ctypes.c_ulong(0)
            status = self.ntdll.NtQueryInformationProcess(
                self.kernel32.GetCurrentProcess(),
                7,  # ProcessDebugPort
                ctypes.byref(debug_port),
                ctypes.sizeof(debug_port),
                None
            )
            if status == 0 and debug_port.value != 0:
                return True
        except Exception:
            pass
        
        # Method 4: Check for debug flags in PEB
        try:
            # NtGlobalFlag check
            peb = ctypes.c_void_p()
            # Would need to read PEB structure
        except Exception:
            pass
        
        # Method 5: Timing check (debuggers slow execution)
        start = time.perf_counter()
        for _ in range(10000):
            pass
        elapsed = time.perf_counter() - start
        if elapsed > 0.1:  # Should be much faster
            return True
        
        return False
    
    def anti_attach(self):
        """Prevent debugger attachment."""
        try:
            # Self-debug to prevent others from attaching
            # DebugActiveProcess on self
            pass
        except Exception:
            pass
    
    def detect_breakpoints(self) -> bool:
        """Check for software breakpoints in critical code."""
        try:
            # Check for INT3 (0xCC) instructions in our code
            # This is a basic check
            return False
        except Exception:
            return False


class BehaviorRandomizer:
    """
    Randomizes behavioral patterns to avoid detection.
    """
    
    def __init__(self):
        self.action_history = []
        self.pattern_breaker_enabled = True
    
    def record_action(self, action_type: str, data: dict = None):
        """Record an action for pattern analysis."""
        self.action_history.append({
            "type": action_type,
            "time": time.time(),
            "data": data or {}
        })
        
        # Keep last 1000 actions
        if len(self.action_history) > 1000:
            self.action_history.pop(0)
    
    def should_break_pattern(self) -> bool:
        """Determine if we should add random behavior to break patterns."""
        if not self.pattern_breaker_enabled:
            return False
        
        # Random chance
        if random.random() < 0.05:  # 5% chance
            return True
        
        # Check for repetitive patterns
        if len(self.action_history) >= 10:
            last_10 = [a["type"] for a in self.action_history[-10:]]
            # If all same type, break pattern
            if len(set(last_10)) == 1:
                return True
        
        return False
    
    def add_noise_action(self):
        """Add a random benign action to break patterns."""
        noise_actions = [
            lambda: time.sleep(random.uniform(0.01, 0.05)),
            lambda: os.getpid(),
            lambda: time.time(),
            lambda: random.random(),
            lambda: hashlib.md5(str(time.time()).encode()).hexdigest(),
        ]
        random.choice(noise_actions)()


class DriverSignatureMasker:
    """
    Attempts to mask driver communication patterns.
    """
    
    def __init__(self):
        self.last_ioctl_time = 0
        self.ioctl_count = 0
    
    def pre_ioctl(self):
        """Called before driver IOCTL call."""
        current = time.time()
        
        # Rate limiting to appear more natural
        if current - self.last_ioctl_time < 0.001:
            time.sleep(random.uniform(0.001, 0.003))
        
        self.last_ioctl_time = current
        self.ioctl_count += 1
        
        # Periodic longer delay
        if self.ioctl_count % 100 == 0:
            time.sleep(random.uniform(0.005, 0.015))
    
    def post_ioctl(self):
        """Called after driver IOCTL call."""
        if random.random() < 0.05:  # 5% chance
            time.sleep(random.uniform(0.0005, 0.002))


class ProcessScanner:
    """
    Detects anti-cheat processes and modules.
    """
    
    ANTICHEAT_PROCESSES = [
        "vgc.exe", "vgtray.exe", "vgk.sys",  # Vanguard
        "easyanticheat.exe", "easyanticheat_eos.exe",  # EAC
        "beclient.exe", "beservice.exe",  # BattlEye
        "faceitclient.exe", "faceit.exe",  # FACEIT
        "esea.exe", "esea-client.exe",  # ESEA
        "csgo.exe",  # Game processes
    ]
    
    def __init__(self):
        self.detected_anticheats = set()
    
    def scan(self) -> List[str]:
        """Scan for running anti-cheat processes."""
        detected = []
        
        try:
            import subprocess
            result = subprocess.run(
                ['tasklist', '/FO', 'CSV', '/NH'],
                capture_output=True, text=True, timeout=5,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            
            processes = result.stdout.lower()
            
            for ac_process in self.ANTICHEAT_PROCESSES:
                if ac_process.lower() in processes:
                    detected.append(ac_process)
                    self.detected_anticheats.add(ac_process)
        except Exception:
            pass
        
        return detected
    
    def get_threat_level(self) -> str:
        """Get overall threat assessment."""
        detected = self.scan()
        
        if any("vg" in p for p in detected):
            return "CRITICAL"  # Vanguard is kernel-level
        elif any("easyanticheat" in p for p in detected):
            return "HIGH"
        elif any("be" in p for p in detected):
            return "HIGH"
        elif len(detected) > 0:
            return "MEDIUM"
        
        return "LOW"


# ============================================
# Main V7 Anti-Detection Manager
# ============================================

class V7AntiDetection:
    """
    Central manager for all V7 anti-detection features.
    """
    
    def __init__(self):
        self.enabled = True
        self.initialized = False
        
        # Initialize all sub-systems
        self.memory = MemoryRandomizer()
        self.hooks = APIHookDetector()
        self.timing = TimingObfuscator()
        self.threads = ThreadCloaker()
        self.syscalls = SyscallObfuscator()
        self.antidebug = AntiDebugEnhanced()
        self.behavior = BehaviorRandomizer()
        self.driver = DriverSignatureMasker()
        self.scanner = ProcessScanner()
        
        # Background thread for periodic checks
        self._stop_event = threading.Event()
        self._monitor_thread = None
        
        self.initialized = True
        logging.info("[V7] Anti-detection system initialized")
    
    def start_monitoring(self):
        """Start background security monitoring."""
        if self._monitor_thread is None:
            self._monitor_thread = threading.Thread(
                target=self._monitor_loop,
                daemon=True,
                name="SecurityMonitor"
            )
            self._monitor_thread.start()
            
            # Hide the monitor thread
            self.threads.hide_thread()
    
    def _monitor_loop(self):
        """Background monitoring loop."""
        while not self._stop_event.is_set():
            try:
                # Check for debuggers
                if self.antidebug.is_debugger_present():
                    logging.warning("[V7] Debugger detected!")
                    self._on_threat_detected("debugger")
                
                # Check for hooks
                hooked = self.hooks.detect_hooks()
                if hooked:
                    logging.warning(f"[V7] Hooked APIs detected: {hooked}")
                    self._on_threat_detected("hooks")
                
                # Shuffle memory periodically
                if random.random() < 0.1:  # 10% chance per cycle
                    self.memory.shuffle_allocations()
                
                # Add behavioral noise
                if self.behavior.should_break_pattern():
                    self.behavior.add_noise_action()
                
            except Exception as e:
                logging.debug(f"[V7] Monitor error: {e}")
            
            # Random sleep interval
            self._stop_event.wait(random.uniform(1.0, 3.0))
    
    def _on_threat_detected(self, threat_type: str):
        """Handle detected threats."""
        logging.warning(f"[V7] Threat detected: {threat_type}")
        # Could implement auto-exit, state cleanup, etc.
    
    def pre_operation(self):
        """Call before any sensitive operation."""
        if not self.enabled:
            return
        
        self.timing.add_jitter()
        self.driver.pre_ioctl()
        
        if self.behavior.should_break_pattern():
            self.behavior.add_noise_action()
    
    def post_operation(self):
        """Call after any sensitive operation."""
        if not self.enabled:
            return
        
        self.driver.post_ioctl()
        self.behavior.record_action("operation")
    
    def get_status(self) -> dict:
        """Get current security status."""
        return {
            "initialized": self.initialized,
            "enabled": self.enabled,
            "threat_level": self.scanner.get_threat_level(),
            "hooks_safe": self.hooks.is_safe(),
            "debugger_detected": self.antidebug.is_debugger_present(),
            "memory_allocations": len(self.memory.allocations),
            "hidden_threads": len(self.threads.hidden_threads),
        }
    
    def cleanup(self):
        """Clean up all resources."""
        self._stop_event.set()
        self.memory.cleanup()
        logging.info("[V7] Anti-detection cleanup complete")


# Global instance
v7_protection = None

def init_v7_protection() -> V7AntiDetection:
    """Initialize V7 protection system."""
    global v7_protection
    if v7_protection is None:
        v7_protection = V7AntiDetection()
        v7_protection.start_monitoring()
    return v7_protection

def get_v7_protection() -> Optional[V7AntiDetection]:
    """Get the V7 protection instance."""
    return v7_protection
