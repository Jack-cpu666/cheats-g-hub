from flask import request, Response
from global_state import state
from utils.serialization import text_serialize_dict
import logging
import traceback

# Settings that require Full Access membership
FULL_ACCESS_ONLY_SETTINGS = {
    # Triggerbot settings
    'triggerbot_enabled', 'triggerbot_pixel_size', 'triggerbot_shoot_while_moving',
    'triggerbot_use_weapon_profiles', 'triggerbot_burst_mode', 'triggerbot_custom_fire_rate',
    'triggerbot_fire_rate_cooldown',
    # Anti-Recoil (RCS) settings
    'rcs_enabled', 'rcs_strength', 'rcs_horizontal_strength', 'rcs_smoothing',
    'rcs_pattern_compensation', 'rcs_spray_transfer',
    # Crosshair settings
    'crosshair_enabled', 'crosshair_style', 'crosshair_color', 'crosshair_size',
    'crosshair_thickness', 'crosshair_gap', 'crosshair_outline',
    # Anti-Detection / Advanced humanizer settings (modification - not viewing)
    'humanizer_amplitude', 'humanizer_frequency', 'humanizer_noise',
    'base_polling_rate', 'polling_jitter', 'path_curvature', 'min_path_points',
    'max_path_points', 'tremor_amplitude', 'tremor_frequency', 'stress_multiplier',
    'detection_grace_period', 'overshoot_enabled', 'deceleration_curve',
    'micro_corrections_enabled'
}

# Settings Regular users CAN change
REGULAR_ALLOWED_SETTINGS = {
    'aimbot_enabled', 'aimbot_pixel_size', 'aimbot_fov', 'aimbot_strength',
    'aimbot_smoothing', 'target_lock', 'activation_key', 'toggle_key',
    'aim_key', 'trigger_key', 'toggle_aim_key', 'panic_key',
    'detection_color', 'color_tolerance', 'sensitivity_multiplier',
    'horizontal_sensitivity', 'vertical_sensitivity'
}

def update_settings():
    try:
        form_data = request.form.to_dict()
        logging.debug(f"[API] Received update request with {len(form_data)} fields")
        
        # Check membership tier for restricted settings
        from auth.membership import get_membership_info, MembershipTier
        membership = get_membership_info()
        is_full_access = membership and membership.tier == MembershipTier.FULL_ACCESS
        
        # Filter out blocked settings for non-Full Access users
        blocked_settings = []
        if not is_full_access:
            for key in list(form_data.keys()):
                if key in FULL_ACCESS_ONLY_SETTINGS:
                    blocked_settings.append(key)
                    del form_data[key]
                    logging.warning(f"[API] Blocked setting '{key}' - requires Full Access membership")
        
        t = state.aimbot_thread
        if t:
            for k, v in form_data.items():
                setter_name = f"set_{k}"
                if hasattr(t, setter_name):
                    try:
                        # Smart type casting
                        val = v
                        if v.lower() in ['true', '1', 'on']: 
                            val = True
                        elif v.lower() in ['false', '0', 'off']: 
                            val = False
                        else:
                            # Try float first (handles decimals), then int
                            try:
                                if '.' in v:
                                    val = float(v)
                                elif v.lstrip('-').isdigit():
                                    val = int(v)
                                # else keep as string
                            except ValueError:
                                pass  # Keep as string
                        
                        logging.debug(f"[API] Setting {k} = {val} (type: {type(val).__name__})")
                        getattr(t, setter_name)(val)
                    except Exception as e:
                        logging.error(f"[API] Error setting {k}: {e}")
                        logging.error(traceback.format_exc())
                        
            # Handle start/stop logic based on flags
            should_run = t.aimbot_enabled or t.triggerbot_enabled
            if should_run and not t.running: 
                logging.info("[API] Starting scanning...")
                t.start_scanning()
            elif not should_run and t.running: 
                logging.info("[API] Stopping scanning...")
                t.stop_scanning()

        if blocked_settings:
            return Response(f"success=1&message=Settings updated (some require Full Access: {', '.join(blocked_settings[:3])}...)", mimetype='text/plain')
        
        return Response("success=1&message=Settings updated", mimetype='text/plain')
    
    except Exception as e:
        logging.error(f"[API] Critical error in update_settings: {e}")
        logging.error(traceback.format_exc())
        return Response(f"success=0&message=Error: {str(e)}", mimetype='text/plain')