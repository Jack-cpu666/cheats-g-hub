"""
Aim Mathematics Module - Advanced Humanized Mouse Movement
============================================================

This module handles converting screen-space target coordinates into
humanized mouse movements that evade behavioral pattern detection.

The module integrates with:
- core/mouse_humanizer.py - For Bézier paths, polling emulation, tremor
- features/aim/humanization.py - For session profiles and timing

Detection Bypass Features:
--------------------------
1. Curved Bézier paths (not straight lines)
2. Variable velocity profiles (ease-in/out)
3. Genuine hand tremor simulation (Perlin noise)
4. Realistic polling rate jitter
5. Overshoot and correction movements
6. Session-unique behavioral fingerprints
7. Stress-based behavior modification
8. Pattern repetition avoidance
"""

import time
import math
import random
import logging
from typing import Tuple, Optional
from global_state import state
from features.aim.humanization import (
    humanize_movement, 
    get_variable_smoothing,
    should_skip_frame,
    get_humanized_delay,
    get_pre_aim_delay,
    session_profile,
    add_micro_adjustment,
    calculate_stress_level,
    track_and_adjust_movement,
    movement_tracker
)


# Try to import the advanced humanizer
try:
    from core.mouse_humanizer import (
        HumanizedMouseController,
        get_humanized_controller,
        initialize_humanization,
        get_reaction_generator
    )
    ADVANCED_HUMANIZER_AVAILABLE = True
except ImportError:
    ADVANCED_HUMANIZER_AVAILABLE = False
    logging.warning("[AimMaths] Advanced humanizer not available, using basic mode")


# ============================================================================
# STATE TRACKING
# ============================================================================

# Track last shot time for stress calculation
_last_shot_time = 0.0
_last_target_position: Optional[Tuple[float, float]] = None
_target_velocity = 0.0


def update_target_tracking(current_target: Tuple[float, float]):
    """Update target velocity tracking"""
    global _last_target_position, _target_velocity
    
    if _last_target_position is not None:
        dx = current_target[0] - _last_target_position[0]
        dy = current_target[1] - _last_target_position[1]
        _target_velocity = math.sqrt(dx * dx + dy * dy)
    
    _last_target_position = current_target


def record_shot():
    """Record that a shot was fired (for stress calculation)"""
    global _last_shot_time
    _last_shot_time = time.time()


# ============================================================================
# MAIN AIM FUNCTION
# ============================================================================

def aim_at_target(dx: float, dy: float, 
                  left_pressed: bool, right_pressed: bool,
                  base_left_sens: float, base_right_sens: float,
                  settings, 
                  current_target_coords: Optional[Tuple[int, int]]) -> Tuple[int, int]:
    """
    Calculate and execute humanized mouse movement to target.
    
    This is the main entry point for aim calculations. It applies:
    - Sensitivity scaling
    - Smoothing (if enabled)
    - Full humanization pipeline
    
    Args:
        dx, dy: Raw pixel offset to target
        left_pressed, right_pressed: Mouse button states
        base_left_sens, base_right_sens: Base sensitivity values
        settings: Settings object with aim configuration
        current_target_coords: Previous target coords for smoothing
        
    Returns:
        (final_dx, final_dy) - The actual movement applied
    """
    
    if not state.rzcontrol: 
        return (0, 0)
    
    # Calculate distance for adaptive behaviors
    distance = math.sqrt(dx * dx + dy * dy)
    
    # Update target tracking
    update_target_tracking((dx, dy))
    
    # Calculate stress level based on context
    time_since_shot = time.time() - _last_shot_time if _last_shot_time > 0 else 999.0
    stress_level = calculate_stress_level(distance, _target_velocity, time_since_shot)
    
    # Humanization: Randomly skip frames to avoid perfect consistency
    if should_skip_frame():
        return current_target_coords if current_target_coords else (0, 0)
    
    # Very small movements - add more randomness or skip
    if distance < 2:
        if random.random() < 0.5:  # 50% chance to ignore tiny movements
            return current_target_coords if current_target_coords else (0, 0)
    
    # Determine base sensitivity
    base_sensitivity = base_right_sens if right_pressed else base_left_sens
    if base_sensitivity < 1e-6: 
        base_sensitivity = 0.01

    effective_sens = base_sensitivity * settings.sensitivity_multiplier
    
    # Apply session-specific speed tendency
    speed_factor = session_profile.speed_tendency
    
    # Add slight random variance to sensitivity per-frame
    sens_variance = 1.0 + random.uniform(-0.06, 0.06)  # ±6% variance
    effective_sens *= sens_variance * speed_factor
    
    # Calculate raw movement
    raw_dx = dx * settings.move_scale * effective_sens
    raw_dy = dy * settings.move_scale * effective_sens

    final_dx = int(raw_dx + settings.aim_offset_x)
    final_dy = int(raw_dy + settings.aim_offset_y)

    # Humanized smoothing - apply dampening to large movements
    # Note: We smooth the CURRENT frame's movement only, not accumulate with previous
    if settings.smoothing_enabled:
        smoothing = get_variable_smoothing(settings.smoothing_factor, distance)
        # Apply smoothing as a dampening factor (0.5 smoothing = 50% of intended movement)
        final_dx = int(final_dx * smoothing)
        final_dy = int(final_dy * smoothing)

    # Skip if no movement needed
    if final_dx == 0 and final_dy == 0:
        return (0, 0)

    # Check for pattern repetition and adjust if needed
    final_dx, final_dy = track_and_adjust_movement(final_dx, final_dy)

    # ========================================================================
    # EXECUTE MOVEMENT - Use advanced humanizer if available
    # ========================================================================
    
    if ADVANCED_HUMANIZER_AVAILABLE:
        return _execute_with_advanced_humanizer(
            final_dx, final_dy, distance, stress_level, settings
        )
    else:
        return _execute_with_basic_humanizer(
            final_dx, final_dy, distance, stress_level, settings
        )


def _execute_with_advanced_humanizer(final_dx: int, final_dy: int,
                                     distance: float, stress_level: float,
                                     settings) -> Tuple[int, int]:
    """
    Execute movement using the full advanced humanization system.
    Uses Bézier curves, polling emulation, tremor, etc.
    """
    # Get or initialize the humanized controller
    controller = get_humanized_controller(state.rzcontrol)
    
    if controller is None:
        # Fallback to basic if controller unavailable
        return _execute_with_basic_humanizer(final_dx, final_dy, distance, stress_level, settings)
    
    # Determine if we should use curved path based on distance and settings
    use_curve = distance > 5 and not settings.flick_shot_enabled
    
    # Execute the humanized movement
    success = controller.move_to_target(
        final_dx, final_dy,
        stress_level=stress_level,
        use_curve=use_curve,
        add_tremor=True
    )
    
    if success:
        return (final_dx, final_dy)
    else:
        return (0, 0)


def _execute_with_basic_humanizer(final_dx: int, final_dy: int,
                                  distance: float, stress_level: float,
                                  settings) -> Tuple[int, int]:
    """
    Execute movement using basic humanization (fallback mode).
    Still applies tremor and other simple techniques.
    """
    # Apply humanization (tremor, occasional miss, speed variance)
    final_dx, final_dy = humanize_movement(final_dx, final_dy, distance)
    
    # Apply session profile tremor with stress modifier
    tremor = add_micro_adjustment(0, 0)
    tremor = session_profile.apply_to_tremor(tremor)
    
    # Scale tremor by stress level
    tremor = (int(tremor[0] * stress_level), int(tremor[1] * stress_level))
    
    final_dx += tremor[0]
    final_dy += tremor[1]

    if final_dx == 0 and final_dy == 0:
        return (0, 0)

    # Execute flick shot or normal movement
    if settings.flick_shot_enabled and distance > 15:
        return _execute_flick_shot(final_dx, final_dy, settings)
    else:
        # Direct movement
        state.rzcontrol.mouse_move(final_dx, final_dy, True)
        return (final_dx, final_dy)


def _execute_flick_shot(final_dx: int, final_dy: int, settings) -> Tuple[int, int]:
    """
    Execute a flick shot with overshoot and correction.
    """
    # Humanized flick: variable overshoot with correction
    overshoot_variance = random.uniform(0.8, 1.2)
    overshoot = settings.flick_overshoot_factor * overshoot_variance
    
    # Apply session overshoot tendency
    overshoot *= session_profile.overshoot_tendency
    
    f_dx = int(final_dx * (1 + overshoot))
    f_dy = int(final_dy * (1 + overshoot))
    
    # Execute overshoot movement
    state.rzcontrol.mouse_move(f_dx, f_dy, True)
    
    # Variable delay for correction movement
    correction_delay = get_humanized_delay(15)  # ~15ms with variance
    time.sleep(correction_delay)
    
    # Correction with slight imperfection
    correction_dx = final_dx - f_dx
    correction_dy = final_dy - f_dy
    correction_dx, correction_dy = add_micro_adjustment(correction_dx, correction_dy)
    
    state.rzcontrol.mouse_move(correction_dx, correction_dy, True)
    
    return (final_dx, final_dy)


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_aim_delay_for_distance(distance: float) -> float:
    """
    Get an appropriate aim delay based on distance.
    Shorter distances = faster aiming (like a real human reflex)
    """
    if distance < 10:
        base_delay = 10  # Very fast for micro-corrections
    elif distance < 30:
        base_delay = 25
    elif distance < 60:
        base_delay = 40
    elif distance < 100:
        base_delay = 60
    else:
        base_delay = 80  # Slower for large movements
    
    return get_humanized_delay(base_delay)


def should_use_curved_path(distance: float, settings) -> bool:
    """
    Determine if we should use a curved Bézier path for this movement.
    """
    # Don't use curves for tiny movements
    if distance < 5:
        return False
    
    # Don't use curves for flick shots (they should be fast)
    if settings.flick_shot_enabled:
        return False
    
    # Use curves for medium-large movements
    return distance > 8


def get_movement_point_count(distance: float) -> int:
    """
    Calculate how many points to use for curved movement.
    More points = smoother curve but more time.
    """
    if distance < 10:
        return 3
    elif distance < 30:
        return 5
    elif distance < 60:
        return 8
    elif distance < 100:
        return 12
    else:
        return 15


# ============================================================================
# INITIALIZATION
# ============================================================================

def initialize_aim_system():
    """
    Initialize the aim system and advanced humanizer.
    Call this once at startup after driver is ready.
    """
    if ADVANCED_HUMANIZER_AVAILABLE and state.rzcontrol:
        try:
            controller = initialize_humanization(state.rzcontrol)
            logging.info(f"[AimMaths] Advanced humanizer initialized with fingerprint")
            return controller
        except Exception as e:
            logging.error(f"[AimMaths] Failed to initialize advanced humanizer: {e}")
    
    logging.info("[AimMaths] Using basic humanization mode")
    return None


def regenerate_fingerprints():
    """
    Regenerate all behavioral fingerprints.
    Call this between matches to change behavioral signature.
    """
    from features.aim.humanization import regenerate_session_profile
    regenerate_session_profile()
    
    if ADVANCED_HUMANIZER_AVAILABLE:
        controller = get_humanized_controller()
        if controller:
            controller.regenerate_fingerprint()
    
    logging.info("[AimMaths] Behavioral fingerprints regenerated")