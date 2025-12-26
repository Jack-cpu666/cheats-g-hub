import threading

class GlobalState:
    def __init__(self):
        self.rzcontrol = None
        self.aimbot_thread = None
        self.movement_keys = set()
        self.mouse_buttons = {"left": False, "right": False}
        self.shutdown_event = threading.Event()
        
        # Flags for custom keybind monitoring
        self.aimbot_custom_key_active = False
        self.triggerbot_custom_key_active = False

state = GlobalState()