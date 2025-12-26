"""
Debug Prints Control Module
============================

Controls all console output for the application.
Set DEBUG_ENABLED to False to silence all prints.
"""

# ============================================
# MASTER DEBUG TOGGLE
# ============================================
# Set to False to disable ALL console output
DEBUG_ENABLED = True
# ============================================

import sys
import logging
from functools import wraps


class SilentPrint:
    """Replacement for print that does nothing when debug is disabled"""
    
    def __init__(self, enabled=True):
        self.enabled = enabled
        self._original_print = None
        self._original_stdout = None
        self._original_stderr = None
    
    def __call__(self, *args, **kwargs):
        if self.enabled:
            if self._original_print:
                self._original_print(*args, **kwargs)
            else:
                __builtins__['print'](*args, **kwargs)
    
    def write(self, text):
        if self.enabled:
            if self._original_stdout:
                self._original_stdout.write(text)
    
    def flush(self):
        if self.enabled and self._original_stdout:
            self._original_stdout.flush()


class NullWriter:
    """A writer that discards all output"""
    def write(self, text):
        pass
    
    def flush(self):
        pass


def configure_output():
    """
    Configure stdout/stderr and logging based on DEBUG_ENABLED.
    Call this at the very start of your application.
    """
    global DEBUG_ENABLED
    
    if not DEBUG_ENABLED:
        # Suppress all console output
        sys.stdout = NullWriter()
        sys.stderr = NullWriter()
        
        # Suppress all logging
        logging.disable(logging.CRITICAL)
        
        # Also suppress werkzeug (Flask's logger)
        log = logging.getLogger('werkzeug')
        log.disabled = True
        log.setLevel(logging.CRITICAL)
    else:
        # Ensure logging is enabled
        logging.disable(logging.NOTSET)


def debug_print(*args, **kwargs):
    """
    Print function that respects DEBUG_ENABLED.
    Use this instead of print() for debug messages.
    """
    if DEBUG_ENABLED:
        print(*args, **kwargs)


def silent_mode():
    """Check if we're in silent mode"""
    return not DEBUG_ENABLED


# ============================================
# DECORATORS
# ============================================

def debug_only(func):
    """Decorator to only run a function when debug is enabled"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if DEBUG_ENABLED:
            return func(*args, **kwargs)
        return None
    return wrapper


def suppress_output(func):
    """Decorator to suppress all output from a function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = NullWriter()
        sys.stderr = NullWriter()
        try:
            return func(*args, **kwargs)
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr
    return wrapper


# ============================================
# USAGE EXAMPLE:
# ============================================
# 
# # At the TOP of main.py, before any other imports:
# from debugprints import configure_output, debug_print, DEBUG_ENABLED
# configure_output()
#
# # Then use debug_print instead of print:
# debug_print("This only shows when DEBUG_ENABLED = True")
#
# # Or use the decorator:
# @debug_only
# def verbose_function():
#     print("This only runs when debug is on")
#
