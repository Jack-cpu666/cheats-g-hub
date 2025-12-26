import cv2
import numpy as np

enemy_hsv_thresholds = {
    "yellow": {"lower": np.array([22, 90, 200]), "upper": np.array([35, 255, 255]), "display_color": "#ffeb3b"},
    "purple": {"lower": np.array([140, 70, 150]), "upper": np.array([160, 255, 255]), "display_color": "#9c27b0"},
    "red": {"lower1": np.array([0, 80, 120]), "upper1": np.array([10, 255, 255]), "lower2": np.array([165, 80, 120]), "upper2": np.array([179, 255, 255]), "display_color": "#f44336"},
    # Add others as needed from original
}

def is_enemy_color(screenshot, color_profile_name):
    # Returns mask
    try:
        hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)
        thresh = enemy_hsv_thresholds.get(color_profile_name, enemy_hsv_thresholds["purple"])
        if color_profile_name == "red":
            m1 = cv2.inRange(hsv, thresh["lower1"], thresh["upper1"])
            m2 = cv2.inRange(hsv, thresh["lower2"], thresh["upper2"])
            return cv2.bitwise_or(m1, m2).astype(bool)
        else:
            return cv2.inRange(hsv, thresh["lower"], thresh["upper"]).astype(bool)
    except Exception: return np.zeros((1,1), dtype=bool)