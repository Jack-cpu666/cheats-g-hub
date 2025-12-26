"""
Advanced Mouse Humanization Engine - Anti-Detection System
===========================================================

This module implements sophisticated techniques to evade behavioral analysis
anti-cheat systems that analyze mouse input patterns over time.

Detection Vectors We Defend Against:
------------------------------------
1. Polling Rate Analysis - Detection of unnatural input timing patterns
2. Velocity Profiling - Detection of non-human acceleration curves
3. Path Linearity - Detection of unnaturally straight movements
4. Reaction Time Analysis - Detection of inhuman response times
5. Overshoot Detection - Humans overshoot and correct, bots don't
6. Micro-tremor Analysis - Human hands naturally tremor
7. Statistical Fingerprinting - Building behavioral profiles over time

Core Techniques:
---------------
1. Bézier Curve Path Generation - Natural curved movements
2. Gaussian Timing Jitter - Variable polling intervals
3. Perlin Noise Tremor - Smooth, natural hand shake
4. Velocity Profiling - Ease-in/ease-out acceleration
5. Overshoot Simulation - Intentional target overshoot with correction
6. Session Fingerprint Randomization - Unique behavior per session
7. Hardware Polling Emulation - Match real mouse polling signatures
"""

import time
import math
import random
import threading
from typing import Tuple, List, Optional, Callable
from dataclasses import dataclass, field
from collections import deque
import logging


# ============================================================================
# DYNAMIC SETTINGS - Read from humanizer_settings module (UI-configurable)
# ============================================================================

def _get_settings():
    """Get current settings from the configurable module"""
    try:
        from core.humanizer_settings import get_humanizer_settings
        return get_humanizer_settings()
    except ImportError:
        return None

def get_polling_rate_hz():
    s = _get_settings()
    return s.polling_rate_hz if s else 1000

def get_polling_jitter_percent():
    s = _get_settings()
    return s.polling_jitter_percent if s else 0.12

def get_bezier_deviation_factor():
    s = _get_settings()
    return s.bezier_deviation_factor if s else 0.35

def get_min_curve_points():
    s = _get_settings()
    return s.min_curve_points if s else 4

def get_max_curve_points():
    s = _get_settings()
    return s.max_curve_points if s else 25

def get_tremor_base_amplitude():
    s = _get_settings()
    return s.tremor_base_amplitude if s else 1.5

def get_tremor_frequency():
    s = _get_settings()
    return s.tremor_frequency if s else 8.0

def get_tremor_stress_multiplier():
    s = _get_settings()
    return s.tremor_stress_multiplier if s else 1.8

def get_overshoot_chance():
    s = _get_settings()
    return s.overshoot_chance if s else 0.35

def get_overshoot_amount_percent():
    s = _get_settings()
    return s.overshoot_amount_percent if s else 0.08

def get_overshoot_correction_delay_ms():
    s = _get_settings()
    return s.overshoot_correction_delay_ms if s else 25

def get_reaction_time_min_ms():
    s = _get_settings()
    return s.reaction_time_min_ms if s else 140

def get_reaction_time_max_ms():
    s = _get_settings()
    return s.reaction_time_max_ms if s else 350

def get_reaction_time_mean_ms():
    s = _get_settings()
    return s.reaction_time_mean_ms if s else 215

def get_miss_chance():
    s = _get_settings()
    return s.miss_chance if s else 0.025

def get_miss_offset_pixels():
    s = _get_settings()
    return s.miss_offset_pixels if s else 6

def get_frame_skip_chance():
    s = _get_settings()
    return s.frame_skip_chance if s else 0.018

# Static constants (not user-configurable)
CURVE_POINTS_PER_100PX = 8      # Points per 100 pixels of distance
OVERSHOOT_MIN_DISTANCE = 15     # Minimum distance (px) to consider overshoot  
OVERSHOOT_AMOUNT_VARIANCE = 0.05# ±5% variance on overshoot
VELOCITY_EASE_FACTOR = 2.5      # Controls the sharpness of ease-in/ease-out
VELOCITY_VARIANCE = 0.18        # ±18% velocity variance per segment
PATH_DEVIATION_FACTOR = 0.15    # 15% deviation from straight path
REACTION_TIME_STD_MS = 40       # Standard deviation



# ============================================================================
# PERLIN NOISE GENERATOR - For smooth, natural tremor
# ============================================================================

class PerlinNoise1D:
    """
    Simple 1D Perlin noise generator for smooth tremor simulation.
    This creates noise that varies smoothly over time, unlike random noise.
    """
    
    def __init__(self, seed: int = None):
        if seed is not None:
            random.seed(seed)
        # Generate permutation table
        self.p = list(range(256))
        random.shuffle(self.p)
        self.p = self.p + self.p  # Duplicate for overflow handling
        
    def _fade(self, t: float) -> float:
        """Fade function for smooth interpolation"""
        return t * t * t * (t * (t * 6 - 15) + 10)
    
    def _lerp(self, a: float, b: float, t: float) -> float:
        """Linear interpolation"""
        return a + t * (b - a)
    
    def _grad(self, hash_val: int, x: float) -> float:
        """Calculate gradient"""
        h = hash_val & 15
        grad = 1 + (h & 7)  # Gradient value 1-8
        if h & 8:
            grad = -grad
        return grad * x
    
    def noise(self, x: float) -> float:
        """
        Get Perlin noise value at position x.
        Returns value in range approximately [-1, 1]
        """
        # Find unit interval containing x
        X = int(math.floor(x)) & 255
        
        # Find relative x in interval
        x -= math.floor(x)
        
        # Compute fade curve
        u = self._fade(x)
        
        # Hash coordinates
        A = self.p[X]
        B = self.p[X + 1]
        
        # Interpolate
        return self._lerp(self._grad(self.p[A], x), self._grad(self.p[B], x - 1), u)


# ============================================================================
# SESSION FINGERPRINT - Unique behavioral profile per session
# ============================================================================

@dataclass
class SessionFingerprint:
    """
    Per-session behavioral fingerprint that creates unique but consistent
    movement patterns for each session. This prevents the anti-cheat from
    building a consistent "cheat signature" across sessions.
    """
    
    # Timing characteristics
    reaction_time_offset_ms: float = 0.0      # Offset from mean reaction time
    polling_rate_bias: float = 1.0            # Slight polling rate variation
    
    # Movement characteristics  
    speed_tendency: float = 1.0               # Slightly faster/slower than average
    smoothness_tendency: float = 1.0          # More/less smooth paths
    tremor_intensity: float = 1.0             # Hand tremor multiplier
    overshoot_tendency: float = 1.0           # More/less likely to overshoot
    
    # Path characteristics
    curve_tightness: float = 1.0              # Tighter/looser bezier curves
    path_deviation_tendency: float = 1.0      # More/less deviation from straight
    
    # Timing patterns
    micro_pause_frequency: float = 0.0        # Chance of tiny hesitations
    acceleration_style: float = 1.0           # Ease-in/out intensity
    
    @classmethod
    def generate_random(cls) -> 'SessionFingerprint':
        """Generate a random but realistic fingerprint for this session"""
        return cls(
            reaction_time_offset_ms=random.gauss(0, 25),  # ±25ms offset
            polling_rate_bias=random.uniform(0.92, 1.08),  # ±8% polling variation
            speed_tendency=random.uniform(0.88, 1.12),     # ±12% speed
            smoothness_tendency=random.uniform(0.85, 1.15),
            tremor_intensity=random.uniform(0.7, 1.4),     # Wide tremor variance
            overshoot_tendency=random.uniform(0.6, 1.5),
            curve_tightness=random.uniform(0.8, 1.2),
            path_deviation_tendency=random.uniform(0.7, 1.3),
            micro_pause_frequency=random.uniform(0.0, 0.03),  # 0-3% pause chance
            acceleration_style=random.uniform(0.85, 1.15)
        )
    
    def apply_to_reaction_time(self, base_ms: float) -> float:
        """Apply fingerprint to reaction time"""
        return max(get_reaction_time_min_ms(), 
                   min(get_reaction_time_max_ms(), 
                       base_ms + self.reaction_time_offset_ms))
    
    def apply_to_velocity(self, velocity: float) -> float:
        """Apply fingerprint to movement velocity"""
        return velocity * self.speed_tendency
    
    def apply_to_tremor(self, tremor: Tuple[float, float]) -> Tuple[float, float]:
        """Apply fingerprint to tremor values"""
        return (tremor[0] * self.tremor_intensity, 
                tremor[1] * self.tremor_intensity)


# ============================================================================
# POLLING RATE EMULATOR - Simulate realistic hardware timing
# ============================================================================

class PollingRateEmulator:
    """
    Emulates the timing characteristics of real mouse hardware.
    
    Real mice don't report at perfectly consistent intervals - there's
    natural USB timing jitter. This class simulates that jitter to avoid
    detection of unnaturally consistent polling.
    """
    
    def __init__(self, target_hz: int = 1000, fingerprint: SessionFingerprint = None):
        self.target_hz = target_hz
        self.base_interval_ms = 1000.0 / target_hz
        self.fingerprint = fingerprint or SessionFingerprint.generate_random()
        
        # History for pattern analysis resistance
        self.interval_history: deque = deque(maxlen=100)
        self.last_input_time = time.perf_counter()
        
        # Perlin noise for smooth jitter
        self._jitter_noise = PerlinNoise1D(seed=random.randint(0, 999999))
        self._noise_position = random.uniform(0, 1000)
        
    def get_next_interval(self) -> float:
        """
        Calculate the next input interval with realistic jitter.
        
        Returns:
            Interval in seconds
        """
        # Base interval with fingerprint bias
        base = self.base_interval_ms * self.fingerprint.polling_rate_bias
        
        # Add Perlin noise-based jitter (smooth, not random)
        self._noise_position += 0.1
        noise_value = self._jitter_noise.noise(self._noise_position)
        jitter_percent = noise_value * get_polling_jitter_percent()
        
        # Add occasional larger jitter (simulates USB timing hiccups)
        if random.random() < 0.02:  # 2% chance
            jitter_percent += random.uniform(-0.08, 0.15)  # Larger deviation
        
        interval_ms = base * (1.0 + jitter_percent)
        
        # Ensure minimum interval (can't be faster than hardware)
        interval_ms = max(0.5, interval_ms)
        
        # Record for analysis resistance
        self.interval_history.append(interval_ms)
        
        return interval_ms / 1000.0  # Return in seconds
    
    def wait_for_next_poll(self) -> float:
        """
        Wait until the next poll should occur.
        
        Returns:
            Actual time waited in seconds
        """
        target_interval = self.get_next_interval()
        elapsed = time.perf_counter() - self.last_input_time
        
        wait_time = max(0, target_interval - elapsed)
        if wait_time > 0:
            time.sleep(wait_time)
        
        actual_waited = time.perf_counter() - self.last_input_time
        self.last_input_time = time.perf_counter()
        
        return actual_waited
    
    def get_polling_statistics(self) -> dict:
        """Get statistics about polling pattern for debugging"""
        if len(self.interval_history) < 2:
            return {}
        
        intervals = list(self.interval_history)
        return {
            'mean_ms': sum(intervals) / len(intervals),
            'min_ms': min(intervals),
            'max_ms': max(intervals),
            'std_ms': self._std_dev(intervals),
            'sample_count': len(intervals)
        }
    
    @staticmethod
    def _std_dev(values: List[float]) -> float:
        """Calculate standard deviation"""
        if len(values) < 2:
            return 0.0
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return math.sqrt(variance)


# ============================================================================
# BÉZIER PATH GENERATOR - Human-like curved movements
# ============================================================================

class BezierPathGenerator:
    """
    Generates human-like curved movement paths using cubic Bézier curves.
    
    Humans don't move in straight lines - our muscle control creates
    natural curves. This generator creates paths that mimic that behavior.
    """
    
    def __init__(self, fingerprint: SessionFingerprint = None):
        self.fingerprint = fingerprint or SessionFingerprint.generate_random()
        self._perlin = PerlinNoise1D(seed=random.randint(0, 999999))
        self._noise_offset = random.uniform(0, 1000)
    
    def generate_path(self, 
                      start: Tuple[float, float], 
                      end: Tuple[float, float],
                      include_overshoot: bool = True) -> List[Tuple[int, int]]:
        """
        Generate a curved path from start to end point.
        
        Args:
            start: Starting position (x, y) - typically (0, 0) for relative
            end: Target position (x, y)
            include_overshoot: Whether to potentially add overshoot
            
        Returns:
            List of (dx, dy) integer deltas for each movement step
        """
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        distance = math.sqrt(dx * dx + dy * dy)
        
        # Very short movements - just return direct
        if distance < 3:
            if dx == 0 and dy == 0:
                return []
            return [(int(round(dx)), int(round(dy)))]
        
        # Calculate number of points based on distance
        num_points = int(min(get_max_curve_points(), 
                            max(get_min_curve_points(), 
                                distance * CURVE_POINTS_PER_100PX / 100)))
        
        # Apply fingerprint influence
        num_points = int(num_points * self.fingerprint.smoothness_tendency)
        num_points = max(get_min_curve_points(), min(get_max_curve_points(), num_points))
        
        # Generate control points with session-specific deviation
        deviation = distance * get_bezier_deviation_factor() * self.fingerprint.curve_tightness
        
        # Use Perlin noise for smooth, natural control point placement
        self._noise_offset += 0.3
        noise1 = self._perlin.noise(self._noise_offset)
        noise2 = self._perlin.noise(self._noise_offset + 100)
        
        # Control point 1 (~1/3 of the way)
        cp1 = (
            start[0] + dx * 0.33 + noise1 * deviation,
            start[1] + dy * 0.33 + random.uniform(-deviation * 0.5, deviation * 0.5)
        )
        
        # Control point 2 (~2/3 of the way)
        cp2 = (
            start[0] + dx * 0.67 + noise2 * deviation * 0.7,
            start[1] + dy * 0.67 + random.uniform(-deviation * 0.5, deviation * 0.5)
        )
        
        # Determine if we should overshoot
        actual_end = end
        overshoot_correction = None
        
        if (include_overshoot and 
            distance > OVERSHOOT_MIN_DISTANCE and 
            random.random() < get_overshoot_chance() * self.fingerprint.overshoot_tendency):
            
            # Calculate overshoot amount
            overshoot_percent = (get_overshoot_amount_percent() + 
                               random.uniform(-OVERSHOOT_AMOUNT_VARIANCE, 
                                            OVERSHOOT_AMOUNT_VARIANCE))
            overshoot_percent *= self.fingerprint.overshoot_tendency
            
            # Overshoot in the direction of movement
            actual_end = (
                end[0] + dx * overshoot_percent,
                end[1] + dy * overshoot_percent
            )
            
            # Calculate correction movement
            overshoot_correction = (
                end[0] - actual_end[0],
                end[1] - actual_end[1]
            )
        
        # Generate points along the Bézier curve
        raw_path = []
        for i in range(num_points):
            t = i / (num_points - 1) if num_points > 1 else 1.0
            
            # Apply ease-in-out for natural acceleration
            t_eased = self._ease_in_out(t, self.fingerprint.acceleration_style)
            
            # Calculate point on curve
            point = self._bezier_point(t_eased, start, cp1, cp2, actual_end)
            raw_path.append(point)
        
        # Convert to relative deltas
        deltas = self._path_to_deltas(raw_path)
        
        # Add overshoot correction if needed
        if overshoot_correction is not None:
            # Add a small pause point (will be handled by timing)
            deltas.append(('PAUSE', get_overshoot_correction_delay_ms()))
            # Add correction movement
            deltas.append((int(round(overshoot_correction[0])), 
                          int(round(overshoot_correction[1]))))
        
        return deltas
    
    def _bezier_point(self, t: float, 
                      p0: Tuple[float, float],
                      p1: Tuple[float, float], 
                      p2: Tuple[float, float],
                      p3: Tuple[float, float]) -> Tuple[float, float]:
        """Calculate point on cubic Bézier curve at parameter t"""
        u = 1 - t
        tt = t * t
        uu = u * u
        uuu = uu * u
        ttt = tt * t
        
        x = uuu * p0[0] + 3 * uu * t * p1[0] + 3 * u * tt * p2[0] + ttt * p3[0]
        y = uuu * p0[1] + 3 * uu * t * p1[1] + 3 * u * tt * p2[1] + ttt * p3[1]
        
        return (x, y)
    
    def _ease_in_out(self, t: float, intensity: float = 1.0) -> float:
        """
        Ease-in-out function for natural acceleration/deceleration.
        Humans accelerate at the start and decelerate at the end of movements.
        """
        power = VELOCITY_EASE_FACTOR * intensity
        if t < 0.5:
            return 0.5 * pow(2 * t, power)
        else:
            return 1 - 0.5 * pow(2 - 2 * t, power)
    
    def _path_to_deltas(self, path: List[Tuple[float, float]]) -> List[Tuple[int, int]]:
        """Convert absolute path points to relative movement deltas"""
        if len(path) < 2:
            if len(path) == 1:
                return [(int(round(path[0][0])), int(round(path[0][1])))]
            return []
        
        deltas = []
        cumulative_x = 0.0
        cumulative_y = 0.0
        
        for i in range(1, len(path)):
            # Calculate ideal delta from start
            target_x = path[i][0]
            target_y = path[i][1]
            
            # Calculate delta from current cumulative position
            delta_x = target_x - cumulative_x
            delta_y = target_y - cumulative_y
            
            # Round to integers
            int_dx = int(round(delta_x))
            int_dy = int(round(delta_y))
            
            # Skip zero movements
            if int_dx != 0 or int_dy != 0:
                deltas.append((int_dx, int_dy))
                cumulative_x += int_dx
                cumulative_y += int_dy
        
        return deltas


# ============================================================================
# TREMOR GENERATOR - Natural hand shake simulation
# ============================================================================

class TremorGenerator:
    """
    Generates realistic hand tremor using Perlin noise.
    
    Human hands naturally tremor, especially under stress (like in combat).
    This creates smooth, natural-looking micro-movements.
    """
    
    def __init__(self, fingerprint: SessionFingerprint = None):
        self.fingerprint = fingerprint or SessionFingerprint.generate_random()
        
        # Separate noise generators for X and Y (uncorrelated)
        self._noise_x = PerlinNoise1D(seed=random.randint(0, 999999))
        self._noise_y = PerlinNoise1D(seed=random.randint(0, 999999))
        
        # Time tracking for smooth progression
        self._time = random.uniform(0, 1000)
        
    def get_tremor(self, stress_level: float = 1.0) -> Tuple[float, float]:
        """
        Get current tremor offset.
        
        Args:
            stress_level: Multiplier for tremor intensity (1.0 = normal)
                         Higher during close combat, lower when relaxed
        
        Returns:
            (dx, dy) tremor offset in pixels
        """
        # Advance time
        self._time += 0.15  # Controls tremor frequency
        
        # Generate noise values
        noise_x = self._noise_x.noise(self._time * get_tremor_frequency())
        noise_y = self._noise_y.noise(self._time * get_tremor_frequency() + 50)
        
        # Calculate amplitude with stress and fingerprint modifiers
        amplitude = (get_tremor_base_amplitude() * 
                    stress_level * 
                    self.fingerprint.tremor_intensity)
        
        # Apply stress multiplier for close-range situations
        if stress_level > 1.0:
            amplitude *= get_tremor_stress_multiplier()
        
        # Generate tremor values
        tremor_x = noise_x * amplitude
        tremor_y = noise_y * amplitude
        
        # Track cumulative tremor to prevent drift
        if not hasattr(self, '_cumulative_tremor'):
            self._cumulative_tremor = [0.0, 0.0]
        
        self._cumulative_tremor[0] += tremor_x
        self._cumulative_tremor[1] += tremor_y
        
        # Apply drift correction - gradually pull back toward zero
        drift_correction_x = -self._cumulative_tremor[0] * 0.1
        drift_correction_y = -self._cumulative_tremor[1] * 0.1
        
        tremor_x += drift_correction_x
        tremor_y += drift_correction_y
        
        # Decay the cumulative tracker
        self._cumulative_tremor[0] *= 0.95
        self._cumulative_tremor[1] *= 0.95
        
        return self.fingerprint.apply_to_tremor((tremor_x, tremor_y))


# ============================================================================
# VELOCITY PROFILER - Natural movement speed curves
# ============================================================================

class VelocityProfiler:
    """
    Manages velocity profiles for movements.
    
    Humans have characteristic velocity curves:
    - Slow acceleration at start
    - Peak velocity in middle
    - Deceleration as approaching target
    
    This is different from constant-velocity bot movements.
    """
    
    def __init__(self, fingerprint: SessionFingerprint = None):
        self.fingerprint = fingerprint or SessionFingerprint.generate_random()
        
    def get_velocity_multiplier(self, progress: float, distance: float) -> float:
        """
        Get velocity multiplier for current position in movement.
        
        Args:
            progress: 0.0 to 1.0, how far along the movement
            distance: Total movement distance in pixels
            
        Returns:
            Velocity multiplier (1.0 = normal speed)
        """
        # Base bell-curve velocity profile
        # Peak at middle, slow at start and end
        base_velocity = math.sin(progress * math.pi)
        
        # Smooth it out so we don't start at exactly 0
        base_velocity = 0.3 + (base_velocity * 0.7)
        
        # Add variance
        variance = 1.0 + random.uniform(-VELOCITY_VARIANCE, VELOCITY_VARIANCE)
        
        # Apply fingerprint speed tendency
        final = base_velocity * variance * self.fingerprint.speed_tendency
        
        # Ensure reasonable bounds
        return max(0.2, min(2.0, final))
    
    def get_segment_delays(self, num_segments: int, 
                           total_distance: float) -> List[float]:
        """
        Calculate delay for each movement segment.
        
        Args:
            num_segments: Number of movement segments
            total_distance: Total distance in pixels
            
        Returns:
            List of delays in seconds for each segment
        """
        if num_segments <= 0:
            return []
        
        delays = []
        
        # Base time per segment (assuming 1000Hz polling)
        base_delay = 0.001  # 1ms base
        
        for i in range(num_segments):
            progress = i / max(1, num_segments - 1)
            velocity_mult = self.get_velocity_multiplier(progress, total_distance)
            
            # Slower velocity = longer delay
            segment_delay = base_delay / max(0.1, velocity_mult)
            
            # Add slight noise
            segment_delay *= 1.0 + random.uniform(-0.1, 0.1)
            
            delays.append(segment_delay)
        
        return delays


# ============================================================================
# HUMANIZED MOUSE CONTROLLER - The main interface
# ============================================================================

class HumanizedMouseController:
    """
    Main controller that coordinates all humanization systems.
    
    This is the class that should be used to execute mouse movements.
    It combines all the anti-detection techniques into a single interface.
    
    Usage:
        controller = HumanizedMouseController(driver)
        controller.move_to_target(dx, dy)
    """
    
    def __init__(self, mouse_driver, regenerate_fingerprint: bool = True):
        """
        Initialize the controller.
        
        Args:
            mouse_driver: The raw mouse driver (e.g., RZCONTROL instance)
            regenerate_fingerprint: If True, generate new fingerprint each session
        """
        self.driver = mouse_driver
        
        # Generate session fingerprint
        self.fingerprint = SessionFingerprint.generate_random() if regenerate_fingerprint else SessionFingerprint()
        
        # Initialize sub-systems with shared fingerprint
        self.polling_emulator = PollingRateEmulator(fingerprint=self.fingerprint)
        self.path_generator = BezierPathGenerator(fingerprint=self.fingerprint)
        self.tremor_generator = TremorGenerator(fingerprint=self.fingerprint)
        self.velocity_profiler = VelocityProfiler(fingerprint=self.fingerprint)
        
        # State tracking
        self._last_move_time = time.perf_counter()
        self._movement_history: deque = deque(maxlen=500)
        self._is_in_combat = False
        
        # Auto-regeneration settings (every 3 minutes)
        self._fingerprint_lifetime_seconds = 180  # 3 minutes
        self._fingerprint_created_at = time.time()
        self._regeneration_count = 0
        
        # Statistics
        self.stats = {
            'total_movements': 0,
            'total_distance': 0.0,
            'overshoots': 0,
            'corrections': 0,
            'frame_skips': 0,
            'fingerprint_regenerations': 0
        }
        
        logging.info(f"[HumanizedMouse] Initialized with fingerprint: "
                    f"speed={self.fingerprint.speed_tendency:.2f}, "
                    f"tremor={self.fingerprint.tremor_intensity:.2f}, "
                    f"overshoot={self.fingerprint.overshoot_tendency:.2f}"
                    f" (auto-regen every {self._fingerprint_lifetime_seconds}s)")
    
    def move_to_target(self, dx: int, dy: int, 
                       stress_level: float = 1.0,
                       use_curve: bool = True,
                       add_tremor: bool = True) -> bool:
        """
        Execute a humanized mouse movement to the target offset.
        
        Args:
            dx: Target X offset from current position
            dy: Target Y offset from current position  
            stress_level: Stress multiplier (affects tremor, >1 for close combat)
            use_curve: If True, use Bézier curves (disable for tiny movements)
            add_tremor: If True, add hand tremor
            
        Returns:
            True if movement was executed, False if skipped
        """
        # Auto-regenerate fingerprint every 3 minutes
        self._check_fingerprint_age()
        
        # Attention lapse simulation - occasionally skip frames
        if random.random() < get_frame_skip_chance():
            self.stats['frame_skips'] += 1
            return False
        
        # Micro-pause simulation
        if random.random() < self.fingerprint.micro_pause_frequency:
            time.sleep(random.uniform(0.005, 0.020))  # 5-20ms micro-pause
        
        distance = math.sqrt(dx * dx + dy * dy)
        
        # Very small movements - just do them directly with tremor
        if distance < 3 or not use_curve:
            return self._execute_simple_move(dx, dy, add_tremor, stress_level)
        
        # Generate curved path
        path = self.path_generator.generate_path((0, 0), (dx, dy), include_overshoot=True)
        
        if not path:
            return False
        
        # Execute path with proper timing
        self._execute_path(path, distance, stress_level, add_tremor)
        
        # Update statistics
        self.stats['total_movements'] += 1
        self.stats['total_distance'] += distance
        
        return True
    
    def _execute_simple_move(self, dx: int, dy: int, 
                             add_tremor: bool, stress_level: float) -> bool:
        """Execute a simple direct movement (for small distances)"""
        final_dx, final_dy = dx, dy
        
        if add_tremor:
            tremor = self.tremor_generator.get_tremor(stress_level)
            final_dx += int(round(tremor[0]))
            final_dy += int(round(tremor[1]))
        
        # Apply intentional miss occasionally
        if random.random() < get_miss_chance():
            miss_x = random.randint(-get_miss_offset_pixels(), get_miss_offset_pixels())
            miss_y = random.randint(-get_miss_offset_pixels(), get_miss_offset_pixels())
            final_dx += miss_x
            final_dy += miss_y
        
        if final_dx != 0 or final_dy != 0:
            self._raw_move(final_dx, final_dy)
            return True
        return False
    
    def _execute_path(self, path: List, distance: float, 
                      stress_level: float, add_tremor: bool):
        """Execute a full curved path with proper timing"""
        
        # Filter out pause markers and count actual movements
        movements = [p for p in path if not isinstance(p, tuple) or p[0] != 'PAUSE']
        pauses = [(i, p[1]) for i, p in enumerate(path) 
                  if isinstance(p, tuple) and len(p) == 2 and p[0] == 'PAUSE']
        
        # Get timing for each segment
        delays = self.velocity_profiler.get_segment_delays(len(movements), distance)
        
        move_index = 0
        for i, item in enumerate(path):
            # Check for pause marker
            if isinstance(item, tuple) and len(item) == 2 and item[0] == 'PAUSE':
                pause_duration = item[1] / 1000.0  # Convert ms to seconds
                time.sleep(pause_duration * random.uniform(0.8, 1.2))
                self.stats['corrections'] += 1
                continue
            
            dx, dy = item
            
            # Add tremor to each segment
            if add_tremor:
                tremor = self.tremor_generator.get_tremor(stress_level)
                dx += int(round(tremor[0]))
                dy += int(round(tremor[1]))
            
            # Execute the movement
            if dx != 0 or dy != 0:
                self._raw_move(dx, dy)
            
            # Wait for next poll with proper timing
            if move_index < len(delays):
                delay = delays[move_index]
                # Add polling jitter
                delay *= self.polling_emulator.fingerprint.polling_rate_bias
                delay *= 1.0 + random.uniform(-0.1, 0.1)
                
                if delay > 0.0001:
                    time.sleep(delay)
            
            move_index += 1
        
        # Check if overshoot occurred
        if any(isinstance(p, tuple) and len(p) == 2 and p[0] == 'PAUSE' for p in path):
            self.stats['overshoots'] += 1
    
    def _raw_move(self, dx: int, dy: int):
        """Execute the raw mouse movement through the driver"""
        if self.driver is not None:
            self.driver.mouse_move(dx, dy, True)
            
            # Record for history
            self._movement_history.append({
                'time': time.perf_counter(),
                'dx': dx,
                'dy': dy
            })
            self._last_move_time = time.perf_counter()
    
    def set_combat_state(self, in_combat: bool):
        """Set whether we're currently in close combat (affects tremor)"""
        self._is_in_combat = in_combat
    
    def get_stress_level(self, target_distance: float) -> float:
        """Calculate stress level based on target proximity"""
        # Closer targets = more stress = more tremor
        if target_distance < 20:
            return 1.5
        elif target_distance < 50:
            return 1.2
        elif target_distance < 100:
            return 1.0
        else:
            return 0.9  # Relaxed for distant targets
    
    def regenerate_fingerprint(self):
        """Generate a new session fingerprint (call between matches)"""
        self.fingerprint = SessionFingerprint.generate_random()
        self.polling_emulator.fingerprint = self.fingerprint
        self.path_generator.fingerprint = self.fingerprint
        self.tremor_generator.fingerprint = self.fingerprint
        self.velocity_profiler.fingerprint = self.fingerprint
        
        # Reset the timer
        self._fingerprint_created_at = time.time()
        self._regeneration_count += 1
        self.stats['fingerprint_regenerations'] = self._regeneration_count
        
        logging.info(f"[HumanizedMouse] Regenerated fingerprint #{self._regeneration_count}: "
                    f"speed={self.fingerprint.speed_tendency:.2f}, "
                    f"tremor={self.fingerprint.tremor_intensity:.2f}")
    
    def _check_fingerprint_age(self):
        """Check if fingerprint needs auto-regeneration (every 3 minutes)"""
        age = time.time() - self._fingerprint_created_at
        if age >= self._fingerprint_lifetime_seconds:
            logging.info(f"[HumanizedMouse] Auto-regenerating fingerprint (age: {age:.1f}s)")
            self.regenerate_fingerprint()
    
    def get_statistics(self) -> dict:
        """Get movement statistics for debugging"""
        return {
            **self.stats,
            'avg_distance': (self.stats['total_distance'] / 
                           max(1, self.stats['total_movements'])),
            'overshoot_rate': (self.stats['overshoots'] / 
                              max(1, self.stats['total_movements'])),
            'polling_stats': self.polling_emulator.get_polling_statistics()
        }


# ============================================================================
# REACTION TIME GENERATOR - Human-like response delays
# ============================================================================

class ReactionTimeGenerator:
    """
    Generates human-realistic reaction time delays.
    
    Uses a skewed normal distribution to match real human reaction times,
    with session-specific variation.
    """
    
    def __init__(self, fingerprint: SessionFingerprint = None):
        self.fingerprint = fingerprint or SessionFingerprint.generate_random()
        
        # Track recent reactions to avoid patterns
        self._recent_reactions: deque = deque(maxlen=20)
    
    def get_reaction_time(self) -> float:
        """
        Get a human-like reaction time.
        
        Returns:
            Delay in seconds
        """
        # Base reaction time from gaussian distribution
        base_ms = random.gauss(get_reaction_time_mean_ms(), REACTION_TIME_STD_MS)
        
        # Apply session fingerprint offset
        base_ms = self.fingerprint.apply_to_reaction_time(base_ms)
        
        # Clamp to realistic range
        base_ms = max(get_reaction_time_min_ms(), min(get_reaction_time_max_ms(), base_ms))
        
        # Avoid too-similar consecutive reactions
        if self._recent_reactions:
            avg_recent = sum(self._recent_reactions) / len(self._recent_reactions)
            # If too close to average, add some variance
            if abs(base_ms - avg_recent) < 15:
                base_ms += random.uniform(-25, 25)
                base_ms = max(get_reaction_time_min_ms(), min(get_reaction_time_max_ms(), base_ms))
        
        self._recent_reactions.append(base_ms)
        
        return base_ms / 1000.0  # Return in seconds
    
    def get_pre_aim_delay(self) -> float:
        """Get a shorter delay for aim adjustments (not initial reaction)"""
        # Aim adjustments are faster than initial reactions
        delay_ms = random.gauss(80, 20)  # ~80ms average
        delay_ms = max(30, min(150, delay_ms))
        return delay_ms / 1000.0


# ============================================================================
# GLOBAL INSTANCE MANAGEMENT
# ============================================================================

# Global humanized controller instance (initialized on first use)
_humanized_controller: Optional[HumanizedMouseController] = None
_reaction_generator: Optional[ReactionTimeGenerator] = None


def get_humanized_controller(driver=None) -> Optional[HumanizedMouseController]:
    """Get or create the global humanized mouse controller"""
    global _humanized_controller
    
    if _humanized_controller is None and driver is not None:
        _humanized_controller = HumanizedMouseController(driver)
    
    return _humanized_controller


def get_reaction_generator() -> ReactionTimeGenerator:
    """Get or create the global reaction time generator"""
    global _reaction_generator
    
    if _reaction_generator is None:
        _reaction_generator = ReactionTimeGenerator()
    
    return _reaction_generator


def initialize_humanization(driver) -> HumanizedMouseController:
    """
    Initialize the humanization system with a mouse driver.
    Call this once at startup.
    
    Args:
        driver: The mouse driver instance (e.g., RZCONTROL)
        
    Returns:
        The initialized HumanizedMouseController
    """
    global _humanized_controller, _reaction_generator
    
    _humanized_controller = HumanizedMouseController(driver)
    _reaction_generator = ReactionTimeGenerator(
        fingerprint=_humanized_controller.fingerprint
    )
    
    return _humanized_controller
