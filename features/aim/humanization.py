"""
Humanization Module - Enhanced Pattern Detection Evasion
=========================================================

This module provides the secondary layer of humanization that integrates
with the core mouse_humanizer system. It handles:

1. Movement-level humanization (applied to individual movements)
2. Session profile management
3. Integration bridges with the aim system
4. Legacy compatibility functions

For the core path generation and timing, see: core/mouse_humanizer.py
"""

import random
import math
import time
from typing import Tuple, List, Optional
from dataclasses import dataclass


# ============================================================================
# CONSTANTS
# ============================================================================

# Human reaction time parameters (milliseconds) - for legacy compatibility
HUMAN_REACTION_MIN_MS = 140
HUMAN_REACTION_MAX_MS = 320
HUMAN_REACTION_MEAN_MS = 215
HUMAN_REACTION_STD_MS = 40

# Mouse movement parameters
MICRO_ADJUSTMENT_MAX_PX = 3
MOVEMENT_SPEED_VARIANCE = 0.20

# Miss chance parameters
INTENTIONAL_MISS_CHANCE = 0.025
MISS_OFFSET_MAX_PX = 6

# Frame skip chance
FRAME_SKIP_CHANCE = 0.018


# ============================================================================
# ENHANCED SESSION PROFILE
# ============================================================================

@dataclass  
class HumanizationProfile:
    """
    Enhanced per-session humanization profile.
    
    This creates a unique behavioral fingerprint for each session,
    preventing the anti-cheat from building a consistent signature.
    """
    
    # Timing offsets
    reaction_offset_ms: float = 0.0
    click_duration_offset_ms: float = 0.0
    
    # Movement modifiers
    tremor_intensity: float = 1.0
    speed_tendency: float = 1.0
    smoothness_factor: float = 1.0
    
    # Behavioral modifiers
    miss_rate_modifier: float = 1.0
    skip_frame_modifier: float = 1.0
    overshoot_tendency: float = 1.0
    
    # Path characteristics
    curve_preference: float = 1.0  # Preference for curved vs straighter paths
    acceleration_style: float = 1.0  # Ease-in/out intensity
    
    def __post_init__(self):
        """Initialize with random values on creation"""
        self.reaction_offset_ms = random.gauss(0, 25)
        self.click_duration_offset_ms = random.gauss(0, 15)
        self.tremor_intensity = random.uniform(0.7, 1.4)
        self.speed_tendency = random.uniform(0.88, 1.12)
        self.smoothness_factor = random.uniform(0.85, 1.15)
        self.miss_rate_modifier = random.uniform(0.5, 1.5)
        self.skip_frame_modifier = random.uniform(0.7, 1.3)
        self.overshoot_tendency = random.uniform(0.6, 1.5)
        self.curve_preference = random.uniform(0.8, 1.2)
        self.acceleration_style = random.uniform(0.85, 1.15)
    
    def apply_to_delay(self, delay_ms: float) -> float:
        """Apply session-specific reaction time offset"""
        adjusted = delay_ms + self.reaction_offset_ms
        # Ensure reasonable bounds
        return max(HUMAN_REACTION_MIN_MS * 0.8, 
                   min(HUMAN_REACTION_MAX_MS * 1.2, adjusted))
    
    def apply_to_tremor(self, tremor: Tuple[int, int]) -> Tuple[int, int]:
        """Apply session-specific tremor intensity"""
        return (
            int(tremor[0] * self.tremor_intensity),
            int(tremor[1] * self.tremor_intensity)
        )
    
    def apply_to_movement(self, dx: int, dy: int) -> Tuple[int, int]:
        """Apply session-specific speed tendency"""
        return (
            int(dx * self.speed_tendency),
            int(dy * self.speed_tendency)
        )
    
    def should_skip_frame(self) -> bool:
        """Determine if this frame should be skipped based on profile"""
        adjusted_chance = FRAME_SKIP_CHANCE * self.skip_frame_modifier
        return random.random() < adjusted_chance
    
    def should_miss(self) -> bool:
        """Determine if we should intentionally miss based on profile"""
        adjusted_chance = INTENTIONAL_MISS_CHANCE * self.miss_rate_modifier
        return random.random() < adjusted_chance


# Global session profile (recreated each session)
session_profile = HumanizationProfile()


def regenerate_session_profile():
    """
    Generate a new session profile.
    Call this between games/matches to change behavioral fingerprint.
    """
    global session_profile
    session_profile = HumanizationProfile()
    return session_profile


# ============================================================================
# TIMING FUNCTIONS
# ============================================================================

def get_humanized_delay(base_delay_ms: float) -> float:
    """
    Add gaussian noise to a base delay.
    
    Args:
        base_delay_ms: Base delay in milliseconds
        
    Returns:
        Humanized delay in seconds
    """
    # Add gaussian noise
    variance = base_delay_ms * 0.15
    humanized_ms = random.gauss(base_delay_ms, variance)
    
    # Apply session profile
    humanized_ms = session_profile.apply_to_delay(humanized_ms)
    
    # Clamp to reasonable bounds
    min_delay = max(1, base_delay_ms * 0.5)
    max_delay = base_delay_ms * 2.0
    humanized_ms = max(min_delay, min(max_delay, humanized_ms))
    
    return humanized_ms / 1000.0


def get_reaction_delay() -> float:
    """
    Generate a human-like reaction time delay.
    Uses configurable settings from the UI.
    
    Returns:
        Delay in seconds
    """
    # Try to use configurable settings from UI
    try:
        from core.humanizer_settings import get_humanizer_settings
        settings = get_humanizer_settings()
        mean_ms = settings.reaction_time_mean_ms
        min_ms = settings.reaction_time_min_ms
        max_ms = settings.reaction_time_max_ms
    except ImportError:
        # Fallback to hardcoded values
        mean_ms = HUMAN_REACTION_MEAN_MS
        min_ms = HUMAN_REACTION_MIN_MS
        max_ms = HUMAN_REACTION_MAX_MS
    
    delay_ms = random.gauss(mean_ms, HUMAN_REACTION_STD_MS)
    delay_ms = session_profile.apply_to_delay(delay_ms)
    delay_ms = max(min_ms, min(max_ms, delay_ms))
    return delay_ms / 1000.0


def get_humanized_click_duration() -> float:
    """
    Generate human-like mouse click hold duration.
    
    Returns:
        Duration in seconds
    """
    # Human click is typically 50-120ms
    duration_ms = random.gauss(75, 20)
    duration_ms += session_profile.click_duration_offset_ms
    duration_ms = max(35, min(160, duration_ms))
    return duration_ms / 1000.0


def get_pre_aim_delay() -> float:
    """
    Get a shorter delay for aim adjustments (not initial reaction).
    These should be faster than initial reactions.
    """
    delay_ms = random.gauss(60, 15)
    delay_ms = max(20, min(120, delay_ms))
    return delay_ms / 1000.0


# ============================================================================
# MOVEMENT HUMANIZATION
# ============================================================================

def add_micro_adjustment(dx: int, dy: int) -> Tuple[int, int]:
    """
    Add small random micro-adjustments to simulate hand tremor.
    
    This is a simpler version - for full tremor simulation use
    the TremorGenerator in mouse_humanizer.py
    """
    if abs(dx) < 2 and abs(dy) < 2:
        return (dx, dy)
    
    # Scale tremor by session profile
    max_tremor = int(MICRO_ADJUSTMENT_MAX_PX * session_profile.tremor_intensity)
    max_tremor = max(1, max_tremor)
    
    tremor_x = random.randint(-max_tremor, max_tremor)
    tremor_y = random.randint(-max_tremor, max_tremor)
    
    result = (dx + tremor_x, dy + tremor_y)
    return session_profile.apply_to_tremor(result)


def apply_intentional_miss(dx: int, dy: int) -> Tuple[int, int]:
    """
    Occasionally introduce a slight miss to appear more human.
    """
    if session_profile.should_miss():
        max_miss = int(MISS_OFFSET_MAX_PX * session_profile.miss_rate_modifier)
        max_miss = max(1, max_miss)
        
        miss_x = random.randint(-max_miss, max_miss)
        miss_y = random.randint(-max_miss, max_miss)
        return (dx + miss_x, dy + miss_y)
    return (dx, dy)


def humanize_movement(dx: int, dy: int, distance: float = None) -> Tuple[int, int]:
    """
    Apply all simple humanization techniques to a single movement.
    
    For full curved path humanization, use HumanizedMouseController.move_to_target()
    """
    # Apply micro-tremor
    dx, dy = add_micro_adjustment(dx, dy)
    
    # Apply occasional miss
    dx, dy = apply_intentional_miss(dx, dy)
    
    # Add slight speed variance
    speed_factor = 1.0 + random.uniform(-MOVEMENT_SPEED_VARIANCE, MOVEMENT_SPEED_VARIANCE)
    speed_factor *= session_profile.speed_tendency
    
    dx = int(dx * speed_factor)
    dy = int(dy * speed_factor)
    
    return (dx, dy)


# ============================================================================
# SMOOTHING FUNCTIONS
# ============================================================================

def get_variable_smoothing(base_factor: float, distance: float) -> float:
    """
    Calculate smoothing factor that varies based on distance.
    
    Closer targets = more smoothing (precise)
    Farther targets = less smoothing (snap faster)
    """
    # Add random variance
    variance = random.uniform(0.9, 1.1) * session_profile.smoothness_factor
    
    # Distance scaling
    if distance > 100:
        distance_scale = 0.75  # Snap faster to far targets
    elif distance > 50:
        distance_scale = 0.85
    elif distance > 25:
        distance_scale = 0.95
    else:
        distance_scale = 1.0  # Full smoothing for close targets
    
    result = base_factor * variance * distance_scale
    return min(1.0, max(0.1, result))


# ============================================================================
# FRAME MANAGEMENT
# ============================================================================

def should_skip_frame() -> bool:
    """
    Randomly skip processing some frames to avoid perfect consistency.
    """
    return session_profile.should_skip_frame()


# ============================================================================
# EASE FUNCTIONS
# ============================================================================

def ease_in_out(t: float, intensity: float = 1.0) -> float:
    """
    Ease-in-out timing function for natural acceleration.
    """
    power = 2.5 * intensity * session_profile.acceleration_style
    power = max(1.5, min(4.0, power))
    
    if t < 0.5:
        return 0.5 * pow(2 * t, power)
    else:
        return 1 - 0.5 * pow(2 - 2 * t, power)


def ease_out_cubic(t: float) -> float:
    """Deceleration curve - slows down at end"""
    return 1 - pow(1 - t, 3)


def ease_in_cubic(t: float) -> float:
    """Acceleration curve - speeds up from start"""
    return pow(t, 3)


# ============================================================================
# LEGACY BEZIER FUNCTIONS (kept for compatibility)
# ============================================================================

def bezier_point(t: float, p0: Tuple[float, float], p1: Tuple[float, float],
                 p2: Tuple[float, float], p3: Tuple[float, float]) -> Tuple[float, float]:
    """Calculate a point on a cubic Bézier curve"""
    u = 1 - t
    tt = t * t
    uu = u * u
    uuu = uu * u
    ttt = tt * t
    
    x = uuu * p0[0] + 3 * uu * t * p1[0] + 3 * u * tt * p2[0] + ttt * p3[0]
    y = uuu * p0[1] + 3 * uu * t * p1[1] + 3 * u * tt * p2[1] + ttt * p3[1]
    
    return (x, y)


def generate_bezier_path(start: Tuple[float, float], end: Tuple[float, float],
                         num_points: int = 10) -> List[Tuple[int, int]]:
    """
    Generate a curved path between two points.
    
    For advanced path generation, use BezierPathGenerator from mouse_humanizer.py
    """
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = math.sqrt(dx * dx + dy * dy)
    
    if distance < 2:
        return [(int(end[0]), int(end[1]))]
    
    # Control points with session-influenced variance
    variance = distance * 0.4 * session_profile.curve_preference
    
    cp1 = (
        start[0] + dx * 0.33 + random.uniform(-variance, variance),
        start[1] + dy * 0.33 + random.uniform(-variance, variance)
    )
    
    cp2 = (
        start[0] + dx * 0.67 + random.uniform(-variance * 0.7, variance * 0.7),
        start[1] + dy * 0.67 + random.uniform(-variance * 0.7, variance * 0.7)
    )
    
    path = []
    for i in range(num_points):
        t = i / (num_points - 1) if num_points > 1 else 1.0
        t_eased = ease_in_out(t)
        
        point = bezier_point(t_eased, start, cp1, cp2, end)
        path.append((int(round(point[0])), int(round(point[1]))))
    
    return path


# ============================================================================
# STRESS LEVEL CALCULATION
# ============================================================================

def calculate_stress_level(target_distance: float, 
                          target_velocity: float = 0.0,
                          time_since_last_shot: float = 999.0) -> float:
    """
    Calculate the current "stress level" which affects tremor and behavior.
    
    Higher stress = more tremor, faster reactions, more mistakes
    
    Args:
        target_distance: Distance to target in pixels
        target_velocity: How fast the target is moving
        time_since_last_shot: Seconds since last shot was fired
        
    Returns:
        Stress multiplier (1.0 = normal, >1 = stressed, <1 = relaxed)
    """
    stress = 1.0
    
    # Close targets increase stress
    if target_distance < 15:
        stress *= 1.6
    elif target_distance < 30:
        stress *= 1.35
    elif target_distance < 50:
        stress *= 1.15
    elif target_distance > 150:
        stress *= 0.85  # Relaxed for distant targets
    
    # Fast-moving targets increase stress
    if target_velocity > 10:
        stress *= 1.2
    elif target_velocity > 5:
        stress *= 1.1
    
    # Recent combat increases stress
    if time_since_last_shot < 0.5:
        stress *= 1.3
    elif time_since_last_shot < 1.0:
        stress *= 1.15
    elif time_since_last_shot > 5.0:
        stress *= 0.9  # Relaxed if no action
    
    # Apply session tendency
    stress *= session_profile.tremor_intensity
    
    return max(0.5, min(2.0, stress))


# ============================================================================
# MOVEMENT HISTORY TRACKING (for anti-pattern analysis)
# ============================================================================

class MovementHistoryTracker:
    """
    Tracks recent movements to ensure we don't create detectable patterns.
    
    Anti-cheat can detect if movements are too similar to each other,
    so we use this to add variance when movements would be too predictable.
    """
    
    def __init__(self, history_size: int = 50):
        self.history: List[Tuple[int, int, float]] = []  # (dx, dy, timestamp)
        self.history_size = history_size
        
    def add_movement(self, dx: int, dy: int):
        """Record a movement"""
        self.history.append((dx, dy, time.time()))
        
        # Trim old entries
        if len(self.history) > self.history_size:
            self.history = self.history[-self.history_size:]
    
    def get_variance_multiplier(self, proposed_dx: int, proposed_dy: int) -> float:
        """
        Check if proposed movement is too similar to recent ones.
        Returns a multiplier to add variance (1.0 = no change, >1 = add variance)
        """
        if len(self.history) < 5:
            return 1.0
        
        similar_count = 0
        for dx, dy, _ in self.history[-10:]:
            # Check if similar direction and magnitude
            if (abs(dx - proposed_dx) < 3 and abs(dy - proposed_dy) < 3):
                similar_count += 1
        
        # If too many similar movements, suggest more variance
        if similar_count >= 3:
            return 1.5  # Add 50% more variance
        elif similar_count >= 2:
            return 1.25
        
        return 1.0
    
    def get_average_magnitude(self) -> float:
        """Get average movement magnitude for pattern analysis"""
        if not self.history:
            return 0.0
        
        magnitudes = [math.sqrt(dx*dx + dy*dy) for dx, dy, _ in self.history]
        return sum(magnitudes) / len(magnitudes)


# Global movement tracker
movement_tracker = MovementHistoryTracker()


def track_and_adjust_movement(dx: int, dy: int) -> Tuple[int, int]:
    """
    Track the movement and adjust if it would create a detectible pattern.
    """
    # Check if we need extra variance
    variance_mult = movement_tracker.get_variance_multiplier(dx, dy)
    
    if variance_mult > 1.0:
        # Add extra randomness
        extra_variance = int((variance_mult - 1.0) * 5)
        dx += random.randint(-extra_variance, extra_variance)
        dy += random.randint(-extra_variance, extra_variance)
    
    # Record the movement
    movement_tracker.add_movement(dx, dy)
    
    return (dx, dy)
