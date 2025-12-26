import mss
from flask import render_template_string
from web.ui_template import HTML_TEMPLATE
from web.license_template import LICENSE_TEMPLATE
from config.constants import APP_NAME, APP_VERSION
from config.paths import PROFILE_SAVE_PATH, RECORDING_SAVE_PATH
from global_state import state
from utils.serialization import text_serialize_gun_profiles
from features.aim.colors import enemy_hsv_thresholds


def index():
    """
    Main view handler.
    Shows license activation page if no valid license,
    otherwise shows the main dashboard.
    """
    
    # Check if user has a valid license
    from auth.membership import get_membership_info, get_hwid, MembershipTier
    membership = get_membership_info()
    
    # If no valid membership, show license activation page
    if membership.tier == MembershipTier.NONE:
        return render_template_string(LICENSE_TEMPLATE, 
            APP_NAME=APP_NAME,
            APP_VERSION=APP_VERSION,
            HWID=get_hwid()
        )
    
    # Valid license - show main dashboard
    t = state.aimbot_thread
    if not t: 
        return "Loading..."
    
    ctx = t.__dict__.copy()
    
    # Add Missing Static Variables
    ctx['APP_NAME'] = APP_NAME
    ctx['APP_VERSION'] = APP_VERSION
    ctx['log_filename'] = 'svchost_runtime.log'  # Generic log name
    ctx['enemy_hsv_thresholds'] = enemy_hsv_thresholds
    
    # Paths
    ctx['profile_save_path'] = PROFILE_SAVE_PATH
    ctx['recording_save_path'] = RECORDING_SAVE_PATH
    ctx['aimbot_thread_running'] = t.running

    # Add membership info to context
    ctx['membership'] = membership.to_dict()
    ctx['can_modify_humanizer'] = membership.can_modify_humanizer
    ctx['can_regenerate_fingerprint'] = membership.can_regenerate_fingerprint

    # Serialize gun profiles for the JS to read
    # The original file called this 'valorant_gun_profiles_text' in get_current_settings
    ctx['valorant_gun_profiles_text'] = text_serialize_gun_profiles(t.valorant_gun_profiles)
    ctx['valorant_gun_profiles_dict'] = t.valorant_gun_profiles

    # Monitor List
    try:
        with mss.mss() as sct:
            ctx['monitors'] = sct.monitors
    except Exception:
        ctx['monitors'] = []

    return render_template_string(HTML_TEMPLATE, **ctx)