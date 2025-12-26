from global_state import state
from pynput.mouse import Button

def on_mouse_click(x, y, button, pressed):
    try:
        t = state.aimbot_thread
        
        # Track left/right mouse buttons
        if button == Button.left:
            state.mouse_buttons['left'] = pressed
        elif button == Button.right:
            state.mouse_buttons['right'] = pressed
        
        # Check for mouse button keybinds (Mouse4, Mouse5, etc.)
        if t:
            button_name = None
            if button == Button.left:
                button_name = 'mouse1'
            elif button == Button.right:
                button_name = 'mouse2'
            elif button == Button.middle:
                button_name = 'mouse3'
            elif hasattr(button, 'name'):
                # Handle x1, x2 buttons (mouse4, mouse5)
                if button.name == 'x1':
                    button_name = 'mouse4'
                elif button.name == 'x2':
                    button_name = 'mouse5'
            
            if button_name:
                # Check aimbot custom keybind
                if t.aimbot_custom_bind_key:
                    keybind = t.aimbot_custom_bind_key.lower().strip()
                    if keybind == button_name or keybind == button_name.replace('mouse', 'mouse_'):
                        state.aimbot_custom_key_active = pressed
                
                # Check triggerbot custom keybind
                if t.triggerbot_custom_bind_key:
                    keybind = t.triggerbot_custom_bind_key.lower().strip()
                    if keybind == button_name or keybind == button_name.replace('mouse', 'mouse_'):
                        state.triggerbot_custom_key_active = pressed
                        
    except Exception:
        pass