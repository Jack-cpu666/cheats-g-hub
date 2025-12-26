"""
Recoil Control System Worker Thread - Humanized

Applies recoil compensation patterns with humanization to avoid detection.
"""

import time
import random
import threading
from global_state import state
from utils.serialization import text_deserialize_points
from features.aim.humanization import (
    get_humanized_delay,
    add_micro_adjustment,
    session_profile
)


def rcs_worker(profile_data, settings):
    """
    Separate thread worker for humanized recoil compensation.
    
    Humanization features:
    - Variable delay between compensation moves
    - Micro-tremor on each adjustment
    - Session-unique behavior
    - Occasional skipped adjustments
    """
    try:
        points = text_deserialize_points(profile_data.get('points', ''))
        base_delay_ms = int(profile_data.get('delay_ms', 100))
    except:
        return

    if not points:
        settings._rcs_is_compensating = False
        return

    last_x, last_y = 0, 0
    
    for i, point in enumerate(points):
        if not settings._rcs_is_compensating:
            break
        
        cur_x, cur_y = point
        dx = cur_x - last_x
        dy = cur_y - last_y
        
        # Apply strength multipliers
        comp_x = -dx * settings.rcs_horizontal_strength
        comp_y = dy * settings.rcs_vertical_strength
        
        # Humanization: Add micro-tremor
        tremor_x, tremor_y = add_micro_adjustment(0, 0)
        tremor_x, tremor_y = session_profile.apply_to_tremor((tremor_x, tremor_y))
        
        comp_x = int(comp_x) + tremor_x
        comp_y = int(comp_y) + tremor_y
        
        # Humanization: Occasionally skip a compensation (2% chance)
        if random.random() < 0.02:
            last_x, last_y = cur_x, cur_y
            continue
        
        # Apply compensation
        if (comp_x != 0 or comp_y != 0) and state.rzcontrol:
            state.rzcontrol.mouse_move(comp_x, comp_y, True)
        
        last_x, last_y = cur_x, cur_y
        
        # Humanized delay between adjustments
        if base_delay_ms > 0:
            humanized_delay = get_humanized_delay(base_delay_ms)
            time.sleep(humanized_delay)
    
    settings._rcs_is_compensating = False