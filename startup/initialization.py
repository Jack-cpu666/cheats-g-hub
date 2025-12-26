import sys
import requests
from global_state import state
from drivers.ghub_core import GHUB
from utils.system_id import get_windows_uuid
from config.constants import AUTH_SERVER_URL

def validate_auth():
    print("Bypassing Auth...") 
    pass

def initialize_drivers():
    ghub = GHUB()
    if ghub.init():
        state.rzcontrol = ghub  # Keep same state key for compatibility
        print("G Hub Driver Initialized.")
        
        # Initialize the advanced mouse humanizer
        try:
            from core.mouse_humanizer import initialize_humanization
            controller = initialize_humanization(ghub)
            if controller:
                print(f"Anti-Detection Humanizer Active (Fingerprint: {controller.fingerprint.speed_tendency:.2f}x speed)")
        except Exception as e:
            print(f"Humanizer init warning: {e}")
    else:
        print("G Hub driver init failed - Is Logitech G Hub installed and running?")
        
def setup_listeners():
    from pynput.keyboard import Listener as KListener, Key
    from pynput.mouse import Listener as MListener, Button
    from inputs.keyboard import on_key_press, on_key_release
    from inputs.mouse import on_mouse_click
    
    kb = KListener(on_press=on_key_press, on_release=on_key_release)
    kb.start()
    
    ms = MListener(on_click=on_mouse_click)
    ms.start()