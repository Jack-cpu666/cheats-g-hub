"""
Humanizer Settings - Configurable Anti-Detection Parameters
============================================================

This module stores the configurable humanizer settings that can be
modified from the web UI. The mouse_humanizer.py reads from here
instead of using hardcoded constants.
"""

import threading
from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class HumanizerSettings:
    """
    Configurable humanizer settings.
    These are modified by the Anti-Detection UI tab.
    """
    
    # Polling Rate Settings
    polling_rate_hz: int = 1000
    polling_jitter_percent: float = 0.12
    
    # Path Generation (Bézier)
    bezier_deviation_factor: float = 0.35
    min_curve_points: int = 4
    max_curve_points: int = 25
    
    # Hand Tremor
    tremor_base_amplitude: float = 1.5
    tremor_frequency: float = 8.0
    tremor_stress_multiplier: float = 1.8
    
    # Overshoot
    overshoot_chance: float = 0.35
    overshoot_amount_percent: float = 0.08
    overshoot_correction_delay_ms: int = 25
    
    # Reaction Time
    reaction_time_min_ms: int = 140
    reaction_time_max_ms: int = 350
    reaction_time_mean_ms: int = 215
    
    # Miss/Accuracy
    miss_chance: float = 0.025
    miss_offset_pixels: int = 6
    
    # Frame Skip
    frame_skip_chance: float = 0.018
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert settings to dictionary"""
        return {
            'polling_rate_hz': self.polling_rate_hz,
            'polling_jitter_percent': self.polling_jitter_percent,
            'bezier_deviation_factor': self.bezier_deviation_factor,
            'min_curve_points': self.min_curve_points,
            'max_curve_points': self.max_curve_points,
            'tremor_base_amplitude': self.tremor_base_amplitude,
            'tremor_frequency': self.tremor_frequency,
            'tremor_stress_multiplier': self.tremor_stress_multiplier,
            'overshoot_chance': self.overshoot_chance,
            'overshoot_amount_percent': self.overshoot_amount_percent,
            'overshoot_correction_delay_ms': self.overshoot_correction_delay_ms,
            'reaction_time_min_ms': self.reaction_time_min_ms,
            'reaction_time_max_ms': self.reaction_time_max_ms,
            'reaction_time_mean_ms': self.reaction_time_mean_ms,
            'miss_chance': self.miss_chance,
            'miss_offset_pixels': self.miss_offset_pixels,
            'frame_skip_chance': self.frame_skip_chance
        }
    
    def update_from_dict(self, data: Dict[str, Any]):
        """Update settings from dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                # Convert to correct type
                current = getattr(self, key)
                if isinstance(current, int):
                    setattr(self, key, int(value))
                elif isinstance(current, float):
                    setattr(self, key, float(value))
                else:
                    setattr(self, key, value)


# Global settings instance (thread-safe access)
_settings_lock = threading.Lock()
_humanizer_settings = HumanizerSettings()


def get_humanizer_settings() -> HumanizerSettings:
    """Get the current humanizer settings (read-only access)"""
    return _humanizer_settings


def update_humanizer_settings(updates: Dict[str, Any]) -> HumanizerSettings:
    """Thread-safe update of humanizer settings"""
    with _settings_lock:
        _humanizer_settings.update_from_dict(updates)
    return _humanizer_settings


def get_setting(name: str, default=None):
    """Get a single setting value"""
    return getattr(_humanizer_settings, name, default)


# ============================================
# UI Field Mapping
# Maps UI field names to settings field names
# ============================================

UI_TO_SETTINGS_MAP = {
    'humanizer_polling_rate': 'polling_rate_hz',
    'humanizer_polling_jitter': ('polling_jitter_percent', lambda x: float(x) / 100),  # UI is %, stored as decimal
    'humanizer_bezier_deviation': 'bezier_deviation_factor',
    'humanizer_min_points': 'min_curve_points',
    'humanizer_max_points': 'max_curve_points',
    'humanizer_tremor_amplitude': 'tremor_base_amplitude',
    'humanizer_tremor_frequency': 'tremor_frequency',
    'humanizer_stress_multiplier': 'tremor_stress_multiplier',
    'humanizer_overshoot_chance': ('overshoot_chance', lambda x: float(x) / 100),  # UI is %, stored as decimal
    'humanizer_overshoot_amount': ('overshoot_amount_percent', lambda x: float(x) / 100),
    'humanizer_correction_delay': 'overshoot_correction_delay_ms',
    'humanizer_reaction_min': 'reaction_time_min_ms',
    'humanizer_reaction_mean': 'reaction_time_mean_ms',
    'humanizer_miss_chance': ('miss_chance', lambda x: float(x) / 100),
    'humanizer_miss_offset': 'miss_offset_pixels',
    'humanizer_frame_skip': ('frame_skip_chance', lambda x: float(x) / 100),
}


def update_from_ui(ui_field: str, value) -> bool:
    """
    Update a setting from a UI field.
    Returns True if the field was recognized and updated.
    """
    if ui_field not in UI_TO_SETTINGS_MAP:
        return False
    
    mapping = UI_TO_SETTINGS_MAP[ui_field]
    
    if isinstance(mapping, tuple):
        # Has a converter function
        field_name, converter = mapping
        converted_value = converter(value)
    else:
        field_name = mapping
        converted_value = value
    
    update_humanizer_settings({field_name: converted_value})
    return True
