import threading
import time
import numpy as np
import random
import cv2
import logging
from global_state import state
from features.aim.maths import aim_at_target
from features.aim.colors import is_enemy_color
from core.capture import ScreenCapture
from features.recoil.profiles import valorant_gun_profiles
from features.shared import MOUSE_LEFT_DOWN, MOUSE_LEFT_UP
# RCS import removed - Coming Soon
from features.aim.humanization import (
    get_humanized_delay, 
    get_reaction_delay, 
    get_humanized_click_duration,
    should_skip_frame
)
from core.v7_anticheat import get_v7_protection

class AimbotTriggerbotThread:
    """Main aimbot/triggerbot controller - uses internal thread for restartability"""
    INSTANCE = None

    def __init__(self):
        AimbotTriggerbotThread.INSTANCE = self
        self.running = False
        self._stop_event = threading.Event()
        self._thread = None  # Internal thread (can be recreated)
        
        # Default Settings
        self.aimbot_enabled = False
        self.triggerbot_enabled = False
        self.aimbot_pixel_size = 50
        self.triggerbot_pixel_size = 4
        self.enemy_color = "purple"
        self.aim_offset_x = 0
        self.aim_offset_y = -3
        self.sensitivity_multiplier = 4.0
        self.move_scale = 0.6
        self.left_sensitivity = 0.25
        self.right_sensitivity = 0.25
        self.selected_monitor = 1  # Default monitor index
        
        # Aimbot Activation Mode Settings
        self.aimbot_activation_mode = "mouse_hold"  # "always_on", "mouse_hold", "custom_bind"
        self.aimbot_custom_bind_key = ""
        self.aimbot_remove_mouse_left = False
        self.aimbot_remove_mouse_right = False
        
        # Triggerbot specific
        self.triggerbot_activation_mode = "always_on"  # "always_on", "mouse_hold", "custom_bind"
        self.triggerbot_custom_bind_key = ""
        self.triggerbot_custom_cooldown = 0.15
        self.triggerbot_use_profile_cooldown = True
        self.shoot_while_moving = False
        self.valorant_gun_profiles = valorant_gun_profiles
        self.selected_valorant_gun = "Custom"
        
        # Feature Flags
        self.flick_shot_enabled = False
        self.flick_overshoot_factor = 0.3
        self.smoothing_enabled = False
        self.smoothing_factor = 0.5
        
        # RCS Flags (Coming Soon - placeholder only)
        self.rcs_enabled = False
        
        # State vars
        self.last_shot_time = 0
        self.current_fps = 0.0
        self._current_aim_target_coords = (0,0)
        
        # Stats
        self.last_capture_time_ms = 0
        self.last_processing_time_ms = 0

    def is_alive(self):
        """Check if internal thread is alive"""
        return self._thread is not None and self._thread.is_alive()

    def start_scanning(self):
        """Start or restart the scanning thread"""
        if self.running and self.is_alive():
            logging.debug("[Thread] Already running, skipping start")
            return
            
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run_loop, name="MainCoreThread", daemon=True)
        self._thread.start()
        self.running = True
        logging.info("[Thread] Scanning started")

    def stop_scanning(self):
        """Stop the scanning thread"""
        self.running = False
        self._stop_event.set()
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=2.0)
        logging.info("[Thread] Scanning stopped")

    # Setter methods
    def set_aimbot_enabled(self, v): self.aimbot_enabled = bool(v)
    def set_triggerbot_enabled(self, v): self.triggerbot_enabled = bool(v)
    def set_aimbot_pixel_size(self, v): self.aimbot_pixel_size = max(1, int(v))
    def set_triggerbot_pixel_size(self, v): self.triggerbot_pixel_size = max(1, int(v))
    def set_aimbot_activation_mode(self, v): self.aimbot_activation_mode = str(v)
    def set_aimbot_custom_bind_key(self, v): self.aimbot_custom_bind_key = str(v)
    def set_aimbot_remove_mouse_left(self, v): self.aimbot_remove_mouse_left = bool(v)
    def set_aimbot_remove_mouse_right(self, v): self.aimbot_remove_mouse_right = bool(v)
    def set_triggerbot_activation_mode(self, v): self.triggerbot_activation_mode = str(v)
    def set_triggerbot_custom_bind_key(self, v): self.triggerbot_custom_bind_key = str(v)
    def set_triggerbot_custom_cooldown(self, v): self.triggerbot_custom_cooldown = max(0.0, float(v))
    def set_triggerbot_use_profile_cooldown(self, v): self.triggerbot_use_profile_cooldown = bool(v)
    def set_shoot_while_moving(self, v): self.shoot_while_moving = bool(v)
    def set_selected_valorant_gun(self, v): self.selected_valorant_gun = str(v) if v in self.valorant_gun_profiles else "Custom"
    def set_flick_shot_enabled(self, v): self.flick_shot_enabled = bool(v)
    def set_flick_overshoot_factor(self, v): self.flick_overshoot_factor = float(v)
    def set_smoothing_enabled(self, v): self.smoothing_enabled = bool(v)
    def set_smoothing_factor(self, v): self.smoothing_factor = float(v)
    def set_left_sensitivity(self, v): self.left_sensitivity = max(0.01, float(v))
    def set_right_sensitivity(self, v): self.right_sensitivity = max(0.01, float(v))
    def set_sensitivity_multiplier(self, v): self.sensitivity_multiplier = max(0.1, float(v))
    def set_move_scale(self, v): self.move_scale = max(0.1, min(2.0, float(v)))
    def set_aim_offset_x(self, v): self.aim_offset_x = int(v)
    def set_aim_offset_y(self, v): self.aim_offset_y = int(v)
    def set_enemy_color(self, v): self.enemy_color = str(v)
    def set_rcs_enabled(self, v): self.rcs_enabled = bool(v)  # Placeholder for Coming Soon
    def set_selected_monitor(self, v):
        self.selected_monitor = int(v)
        if hasattr(self, 'capturer') and self.capturer:
            self.capturer.set_monitor(self.selected_monitor)
    
    
    def reset_settings(self):
        """Reset all user adjustable settings to defaults"""
        self.aimbot_enabled = False
        self.triggerbot_enabled = False
        self.aimbot_pixel_size = 50
        self.triggerbot_pixel_size = 4
        self.aimbot_activation_mode = "mouse_5"
        self.triggerbot_activation_mode = "mouse_5"
        self.shoot_while_moving = False
        self.selected_valorant_gun = "Vandal"
        self.flick_shot_enabled = False
        self.flick_overshoot_factor = 1.2
        self.smoothing_enabled = True
        self.smoothing_factor = 0.5
        self.sensitivity_multiplier = 1.0
        self.enemy_color = 'purple'
        self.aim_offset_x = 0
        self.aim_offset_y = -3  # Default offset to compensate for system
        # Reset sensitivities to safe defaults
        self.left_sensitivity = 0.25
        self.right_sensitivity = 0.25
        self.move_scale = 1.0
        self.selected_monitor = 1

    
    def _run_loop(self):
        self.capturer = ScreenCapture(self.selected_monitor)
        # Use local ref for speed if needed, but self.capturer allows updates
        capturer = self.capturer 
        v7 = get_v7_protection()  # V7: Get protection instance
        frame_count = 0
        
        try:
            while not self._stop_event.is_set():
                t0 = time.perf_counter()
                
                # V7: Pre-operation hook (timing obfuscation)
                if v7 and frame_count % 10 == 0:  # Every 10 frames
                    v7.pre_operation()
                
                if not (self.aimbot_enabled or self.triggerbot_enabled):
                    time.sleep(0.05)
                    continue
                    
                frame = capturer.grab_fov(max(self.aimbot_pixel_size, self.triggerbot_pixel_size))
                self.last_capture_time_ms = (time.perf_counter() - t0) * 1000
                
                t1 = time.perf_counter()
                if frame is not None and frame.size > 0:
                    mask = is_enemy_color(frame, self.enemy_color)
                    has_enemy = np.any(mask)
                    frame_count += 1
                    
                    # Aimbot Logic
                    if self.aimbot_enabled and has_enemy:
                        indices = np.argwhere(mask)
                        if indices.size > 0:
                            cy, cx = np.mean(indices, axis=0)
                            dx = cx - (frame.shape[1] // 2)
                            dy = cy - (frame.shape[0] // 2)
                            
                            # Check activation mode properly
                            should_aim = False
                            if self.aimbot_activation_mode == "always_on":
                                should_aim = True
                            elif self.aimbot_activation_mode == "mouse_hold":
                                # Only activate if mouse button is held (and not excluded)
                                if not self.aimbot_remove_mouse_left and state.mouse_buttons["left"]:
                                    should_aim = True
                                if not self.aimbot_remove_mouse_right and state.mouse_buttons["right"]:
                                    should_aim = True
                            elif self.aimbot_activation_mode == "custom_bind":
                                if state.aimbot_custom_key_active:
                                    should_aim = True
                            
                            if should_aim:
                                # Calculate FPS BEFORE humanization delays (for accurate display)
                                self.last_processing_time_ms = (time.perf_counter() - t1) * 1000
                                self.current_fps = 1.0 / (time.perf_counter() - t0 + 0.0001)
                                
                                self._current_aim_target_coords = aim_at_target(
                                    dx, dy, 
                                    state.mouse_buttons['left'], state.mouse_buttons['right'],
                                    self.left_sensitivity, self.right_sensitivity,
                                    self, self._current_aim_target_coords
                                )
                                continue  # Skip FPS calculation at end (already done)
                    else:
                        # Reset aim coords when no target
                        self._current_aim_target_coords = (0, 0)

                    # Triggerbot Logic
                    if self.triggerbot_enabled and state.rzcontrol:
                        # Calculate center region
                        h, w = mask.shape
                        tz = self.triggerbot_pixel_size // 2
                        tb_top = max(0, h//2 - tz)
                        tb_bottom = min(h, h//2 + tz)
                        tb_left = max(0, w//2 - tz)
                        tb_right = min(w, w//2 + tz)
                        center_chunk = mask[tb_top:tb_bottom, tb_left:tb_right]
                        
                        if np.any(center_chunk):
                            now = time.perf_counter()
                            
                            # Get fire rate from gun profile (Patch 11.08 compatible)
                            gun_profile = self.valorant_gun_profiles.get(self.selected_valorant_gun, self.valorant_gun_profiles.get("Custom", {"cooldown": 0.15}))
                            fire_rate = gun_profile.get('cooldown', 0.15) if self.triggerbot_use_profile_cooldown else self.triggerbot_custom_cooldown
                            ready_to_fire = (now - self.last_shot_time) >= fire_rate
                            
                            # Check activation mode
                            trigger_activated = False
                            if self.triggerbot_activation_mode == "always_on":
                                trigger_activated = True
                            elif self.triggerbot_activation_mode == "mouse_hold":
                                if state.mouse_buttons["left"] or state.mouse_buttons["right"]:
                                    trigger_activated = True
                            elif self.triggerbot_activation_mode == "custom_bind":
                                if state.triggerbot_custom_key_active:
                                    trigger_activated = True
                            
                            # Check shoot while moving
                            if not self.shoot_while_moving and len(state.movement_keys) > 0:
                                trigger_activated = False
                            
                            if trigger_activated and ready_to_fire:
                                # Calculate FPS BEFORE humanization delays (for accurate display)
                                self.last_processing_time_ms = (time.perf_counter() - t1) * 1000
                                self.current_fps = 1.0 / (time.perf_counter() - t0 + 0.0001)
                                
                                # Humanized reaction delay before firing
                                reaction_delay = get_reaction_delay()
                                time.sleep(reaction_delay * 0.1)  # Reduced reaction (already past detection)
                                
                                state.rzcontrol.mouse_click(MOUSE_LEFT_DOWN)
                                
                                # Humanized click hold duration
                                click_duration = get_humanized_click_duration()
                                time.sleep(click_duration)
                                
                                state.rzcontrol.mouse_click(MOUSE_LEFT_UP)
                                self.last_shot_time = time.perf_counter()  # Update after delays
                                continue  # Skip FPS calculation at end (already done)

                self.last_processing_time_ms = (time.perf_counter() - t1) * 1000
                self.current_fps = 1.0 / (time.perf_counter() - t0 + 0.0001)
                
        except Exception as e:
            import traceback
            logging.error(f"CRITICAL: Aimbot thread crashed: {e}")
            logging.error(traceback.format_exc())
            # Don't re-raise - let thread die gracefully