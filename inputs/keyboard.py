from global_state import state
from pynput.keyboard import Key, KeyCode

# Map key names to pynput Key objects
SPECIAL_KEYS = {
    'f1': Key.f1, 'f2': Key.f2, 'f3': Key.f3, 'f4': Key.f4,
    'f5': Key.f5, 'f6': Key.f6, 'f7': Key.f7, 'f8': Key.f8,
    'f9': Key.f9, 'f10': Key.f10, 'f11': Key.f11, 'f12': Key.f12,
    'ctrl': Key.ctrl, 'control': Key.ctrl,
    'shift': Key.shift, 'alt': Key.alt,
    'caps': Key.caps_lock, 'caps_lock': Key.caps_lock,
    'tab': Key.tab, 'space': Key.space,
    'enter': Key.enter, 'esc': Key.esc, 'escape': Key.esc,
}

def key_matches(pressed_key, keybind_name):
    """Check if a pressed key matches a keybind name"""
    if not keybind_name:
        return False
    
    keybind_lower = keybind_name.lower().strip()
    
    # Handle special keys
    if keybind_lower in SPECIAL_KEYS:
        return pressed_key == SPECIAL_KEYS[keybind_lower]
    
    # Handle single character keys
    if len(keybind_lower) == 1:
        if hasattr(pressed_key, 'char') and pressed_key.char:
            return pressed_key.char.lower() == keybind_lower
    
    # Handle key names like 'Key.f5'
    if keybind_lower.startswith('key.'):
        key_name = keybind_lower[4:]
        if key_name in SPECIAL_KEYS:
            return pressed_key == SPECIAL_KEYS[key_name]
    
    # Handle mouse buttons in keybind (mouse4, mouse5, etc.)
    if keybind_lower.startswith('mouse'):
        return False  # Mouse buttons handled in mouse.py
    
    return False

def on_key_press(key):
    try:
        t = state.aimbot_thread
        if not t:
            return
        
        # Check aimbot custom keybind
        if t.aimbot_custom_bind_key and key_matches(key, t.aimbot_custom_bind_key):
            state.aimbot_custom_key_active = True
        
        # Check triggerbot custom keybind
        if t.triggerbot_custom_bind_key and key_matches(key, t.triggerbot_custom_bind_key):
            state.triggerbot_custom_key_active = True
            
        # Track movement keys (WASD)
        if hasattr(key, 'char') and key.char:
            if key.char.lower() in ['w', 'a', 's', 'd']:
                state.movement_keys.add(key.char.lower())
                
    except Exception:
        pass

def on_key_release(key):
    try:
        t = state.aimbot_thread
        
        # F10 to shutdown
        if key == Key.f10:
            state.shutdown_event.set()
            return
        
        if not t:
            return
        
        # Release aimbot custom keybind
        if t.aimbot_custom_bind_key and key_matches(key, t.aimbot_custom_bind_key):
            state.aimbot_custom_key_active = False
        
        # Release triggerbot custom keybind
        if t.triggerbot_custom_bind_key and key_matches(key, t.triggerbot_custom_bind_key):
            state.triggerbot_custom_key_active = False
        
        # Track movement keys (WASD)
        if hasattr(key, 'char') and key.char:
            if key.char.lower() in ['w', 'a', 's', 'd']:
                state.movement_keys.discard(key.char.lower())
                
    except Exception:
        pass