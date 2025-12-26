import mss
import numpy as np
import cv2

class ScreenCapture:
    def __init__(self, monitor_idx=1):
        self.sct = mss.mss()
        self.monitor_idx = monitor_idx
        self.monitors = self.sct.monitors
        self.update_monitor()

    def update_monitor(self):
        if 0 <= self.monitor_idx < len(self.monitors):
            self.monitor = self.monitors[self.monitor_idx]
        else:
            self.monitor = self.monitors[0]

    def set_monitor(self, index):
        self.monitor_idx = int(index)
        self.update_monitor()

    def grab_fov(self, fov_size):
        # Center logic
        cx, cy = self.monitor['width']//2, self.monitor['height']//2
        half = fov_size // 2
        box = {
            "top": self.monitor['top'] + max(0, cy - half),
            "left": self.monitor['left'] + max(0, cx - half),
            "width": fov_size,
            "height": fov_size
        }
        try:
            img = np.array(self.sct.grab(box), dtype=np.uint8)
            return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        except: return None