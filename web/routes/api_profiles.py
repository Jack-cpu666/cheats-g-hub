import os
import re
from flask import request, Response
from global_state import state
from config.paths import PROFILE_SAVE_PATH
from configparser import ConfigParser

# Generic section name for stealth
_SECTION_NAME = "Configuration"

def _create_response_text(data_dict):
    """Convert dictionary to text format: key1=value1&key2=value2"""
    return "&".join([f"{k}={v}" for k, v in data_dict.items()])

def list_profiles():
    """List all saved profiles"""
    try:
        if not os.path.exists(PROFILE_SAVE_PATH):
            os.makedirs(PROFILE_SAVE_PATH, exist_ok=True)
        profiles = [f.replace('.ini', '') for f in os.listdir(PROFILE_SAVE_PATH) if f.endswith('.ini')]
        return Response('\n'.join(profiles), mimetype='text/plain')
    except Exception as e:
        return Response(f"Error listing profiles: {e}", status=500)

def save_profile():
    """Save current settings to a profile"""
    profile_name = request.form.get('profile_name')
    if not profile_name:
        return Response(_create_response_text({"success": "0", "message": "Profile name is required."}), mimetype='text/plain', status=400)
    try:
        if not re.match(r"^[a-zA-Z0-9_-]+$", profile_name):
            raise ValueError("Profile name contains invalid characters.")
        
        if not os.path.exists(PROFILE_SAVE_PATH):
            os.makedirs(PROFILE_SAVE_PATH, exist_ok=True)
        
        aimbot_thread = state.aimbot_thread
        if not aimbot_thread:
            raise ValueError("Aimbot thread not initialized.")
        
        config = ConfigParser()
        config[_SECTION_NAME] = {}
        
        # Get savable settings
        settings = {
            'aimbot_enabled': str(aimbot_thread.aimbot_enabled),
            'aimbot_pixel_size': str(aimbot_thread.aimbot_pixel_size),
            'triggerbot_enabled': str(aimbot_thread.triggerbot_enabled),
            'triggerbot_pixel_size': str(aimbot_thread.triggerbot_pixel_size),
            'sensitivity_multiplier': str(aimbot_thread.sensitivity_multiplier),
            'move_scale': str(aimbot_thread.move_scale),
            'aim_offset_x': str(aimbot_thread.aim_offset_x),
            'aim_offset_y': str(aimbot_thread.aim_offset_y),
            'left_sensitivity': str(aimbot_thread.left_sensitivity),
            'right_sensitivity': str(aimbot_thread.right_sensitivity),
            'enemy_color': str(aimbot_thread.enemy_color),
            'smoothing_enabled': str(aimbot_thread.smoothing_enabled),
            'smoothing_factor': str(aimbot_thread.smoothing_factor),
            'flick_shot_enabled': str(aimbot_thread.flick_shot_enabled),
            'flick_overshoot_factor': str(aimbot_thread.flick_overshoot_factor),
            'rcs_enabled': str(aimbot_thread.rcs_enabled),
            'rcs_current_profile_name': str(aimbot_thread.rcs_current_profile_name),
            'rcs_vertical_strength': str(aimbot_thread.rcs_vertical_strength),
            'rcs_horizontal_strength': str(aimbot_thread.rcs_horizontal_strength),
        }
        
        for key, value in settings.items():
            config[_SECTION_NAME][key] = value
        
        # Save RCS profiles
        for name, data in aimbot_thread.rcs_gun_profiles.items():
            section_name = f'rcs_profile_{name}'
            config[section_name] = {
                'points': data.get('points', ''),
                'delay_ms': str(data.get('delay_ms', 100))
            }
        
        profile_path = os.path.join(PROFILE_SAVE_PATH, f"{profile_name}.ini")
        with open(profile_path, 'w') as configfile:
            config.write(configfile)
        
        return Response(_create_response_text({"success": "1", "message": f"Profile '{profile_name}' saved."}), mimetype='text/plain')
    except Exception as e:
        return Response(_create_response_text({"success": "0", "message": str(e)}), mimetype='text/plain', status=500)

def load_profile():
    """Load settings from a profile"""
    profile_name = request.form.get('profile_name')
    if not profile_name:
        return Response(_create_response_text({"success": "0", "message": "Profile name is required."}), mimetype='text/plain', status=400)
    try:
        if not re.match(r"^[a-zA-Z0-9_-]+$", profile_name):
            raise ValueError("Profile name contains invalid characters.")
        
        profile_path = os.path.join(PROFILE_SAVE_PATH, f"{profile_name}.ini")
        if not os.path.exists(profile_path):
            raise FileNotFoundError(f"Profile '{profile_name}' not found.")
        
        aimbot_thread = state.aimbot_thread
        if not aimbot_thread:
            raise ValueError("Aimbot thread not initialized.")
        
        config = ConfigParser()
        config.read(profile_path)
        
        # Support both new and old format
        section = _SECTION_NAME if _SECTION_NAME in config else 'AscendancyProfile'
        if section not in config:
            raise ValueError("Invalid profile file format.")
        
        settings_dict = dict(config[section])
        
        # Apply settings
        if 'aimbot_enabled' in settings_dict:
            aimbot_thread.aimbot_enabled = settings_dict['aimbot_enabled'].lower() == 'true'
        if 'aimbot_pixel_size' in settings_dict:
            aimbot_thread.aimbot_pixel_size = int(settings_dict['aimbot_pixel_size'])
        if 'triggerbot_enabled' in settings_dict:
            aimbot_thread.triggerbot_enabled = settings_dict['triggerbot_enabled'].lower() == 'true'
        if 'triggerbot_pixel_size' in settings_dict:
            aimbot_thread.triggerbot_pixel_size = int(settings_dict['triggerbot_pixel_size'])
        if 'sensitivity_multiplier' in settings_dict:
            aimbot_thread.sensitivity_multiplier = float(settings_dict['sensitivity_multiplier'])
        if 'move_scale' in settings_dict:
            aimbot_thread.move_scale = float(settings_dict['move_scale'])
        if 'aim_offset_x' in settings_dict:
            aimbot_thread.aim_offset_x = int(settings_dict['aim_offset_x'])
        if 'aim_offset_y' in settings_dict:
            aimbot_thread.aim_offset_y = int(settings_dict['aim_offset_y'])
        if 'left_sensitivity' in settings_dict:
            aimbot_thread.left_sensitivity = float(settings_dict['left_sensitivity'])
        if 'right_sensitivity' in settings_dict:
            aimbot_thread.right_sensitivity = float(settings_dict['right_sensitivity'])
        if 'enemy_color' in settings_dict:
            aimbot_thread.enemy_color = settings_dict['enemy_color']
        if 'smoothing_enabled' in settings_dict:
            aimbot_thread.smoothing_enabled = settings_dict['smoothing_enabled'].lower() == 'true'
        if 'smoothing_factor' in settings_dict:
            aimbot_thread.smoothing_factor = float(settings_dict['smoothing_factor'])
        if 'flick_shot_enabled' in settings_dict:
            aimbot_thread.flick_shot_enabled = settings_dict['flick_shot_enabled'].lower() == 'true'
        if 'flick_overshoot_factor' in settings_dict:
            aimbot_thread.flick_overshoot_factor = float(settings_dict['flick_overshoot_factor'])
        if 'rcs_enabled' in settings_dict:
            aimbot_thread.rcs_enabled = settings_dict['rcs_enabled'].lower() == 'true'
        if 'rcs_current_profile_name' in settings_dict:
            aimbot_thread.rcs_current_profile_name = settings_dict['rcs_current_profile_name']
        if 'rcs_vertical_strength' in settings_dict:
            aimbot_thread.rcs_vertical_strength = float(settings_dict['rcs_vertical_strength'])
        if 'rcs_horizontal_strength' in settings_dict:
            aimbot_thread.rcs_horizontal_strength = float(settings_dict['rcs_horizontal_strength'])
        
        # Load RCS profiles
        for section in config.sections():
            if section.startswith('rcs_profile_'):
                name = section[len('rcs_profile_'):]
                points_str = config.get(section, 'points', fallback='')
                delay_ms = config.getint(section, 'delay_ms', fallback=100)
                aimbot_thread.rcs_gun_profiles[name] = {"points": points_str, "delay_ms": delay_ms}
        
        return Response(_create_response_text({"success": "1", "message": f"Profile '{profile_name}' loaded."}), mimetype='text/plain')
    except Exception as e:
        return Response(_create_response_text({"success": "0", "message": str(e)}), mimetype='text/plain', status=500)

def delete_profile():
    """Delete a saved profile"""
    profile_name = request.form.get('profile_name')
    if not profile_name:
        return Response(_create_response_text({"success": "0", "message": "Profile name required."}), mimetype='text/plain', status=400)
    try:
        if not re.match(r"^[a-zA-Z0-9_-]+$", profile_name):
            raise ValueError("Invalid profile name format.")
        profile_path = os.path.join(PROFILE_SAVE_PATH, f"{profile_name}.ini")
        if os.path.exists(profile_path):
            os.remove(profile_path)
            return Response(_create_response_text({"success": "1", "message": f"Profile '{profile_name}' deleted."}), mimetype='text/plain')
        else:
            return Response(_create_response_text({"success": "0", "message": "Profile not found."}), mimetype='text/plain', status=404)
    except Exception as e:
        return Response(_create_response_text({"success": "0", "message": str(e)}), mimetype='text/plain', status=500)


# RCS Profile Management
def list_rcs_profiles():
    """List all RCS profiles"""
    try:
        aimbot_thread = state.aimbot_thread
        if not aimbot_thread:
            return Response("Aimbot thread not initialized.", status=500)
        
        result_parts = []
        for name, data in aimbot_thread.rcs_gun_profiles.items():
            result_parts.append(f"{name}={data.get('points', '')}")
        result_parts.append(f"current={aimbot_thread.rcs_current_profile_name}")
        return Response("&".join(result_parts), mimetype='text/plain')
    except Exception as e:
        return Response(f"Error: {e}", status=500)

def get_rcs_profile():
    """Get a specific RCS profile"""
    profile_name = request.args.get('profile_name')
    aimbot_thread = state.aimbot_thread
    if not aimbot_thread:
        return Response(_create_response_text({"success": "0", "message": "Aimbot thread not initialized."}), mimetype='text/plain', status=500)
    
    profile_data = aimbot_thread.rcs_gun_profiles.get(profile_name)
    if profile_data:
        response_data = {
            "success": "1",
            "points": profile_data.get('points', ''),
            "delay_ms": str(profile_data.get('delay_ms', 100))
        }
        return Response(_create_response_text(response_data), mimetype='text/plain')
    response_data = {"success": "0", "message": "Profile not found."}
    return Response(_create_response_text(response_data), mimetype='text/plain', status=404)

def save_rcs_profile():
    """Save or update an RCS profile"""
    profile_name = request.form.get('profile_name')
    points_str = request.form.get('points', '')
    delay_ms = request.form.get('delay_ms', '100')
    
    if not profile_name or not re.match(r'^[a-zA-Z0-9_-]+$', profile_name):
        response_data = {"success": "0", "message": "Invalid profile name."}
        return Response(_create_response_text(response_data), mimetype='text/plain', status=400)
    
    aimbot_thread = state.aimbot_thread
    if not aimbot_thread:
        return Response(_create_response_text({"success": "0", "message": "Aimbot thread not initialized."}), mimetype='text/plain', status=500)
    
    try:
        delay = int(delay_ms)
        aimbot_thread.rcs_gun_profiles[profile_name] = {"points": points_str, "delay_ms": delay}
        response_data = {"success": "1", "message": f"Profile '{profile_name}' saved."}
        return Response(_create_response_text(response_data), mimetype='text/plain')
    except Exception as e:
        response_data = {"success": "0", "message": f"Failed to save profile: {str(e)}"}
        return Response(_create_response_text(response_data), mimetype='text/plain', status=400)

def delete_rcs_profile():
    """Delete an RCS profile"""
    profile_name = request.form.get('profile_name')
    if not profile_name:
        response_data = {"success": "0", "message": "Profile name missing."}
        return Response(_create_response_text(response_data), mimetype='text/plain', status=400)
    
    aimbot_thread = state.aimbot_thread
    if not aimbot_thread:
        return Response(_create_response_text({"success": "0", "message": "Aimbot thread not initialized."}), mimetype='text/plain', status=500)
    
    # Don't allow deleting default profiles
    default_profiles = ["Valorant_Vandal", "CS2_AK47", "Simple_Down"]
    if profile_name in default_profiles:
        response_data = {"success": "0", "message": "Cannot delete default profiles."}
        return Response(_create_response_text(response_data), mimetype='text/plain', status=400)
    
    if profile_name in aimbot_thread.rcs_gun_profiles:
        del aimbot_thread.rcs_gun_profiles[profile_name]
        if aimbot_thread.rcs_current_profile_name == profile_name:
            aimbot_thread.rcs_current_profile_name = "Valorant_Vandal"
        response_data = {"success": "1", "message": f"Profile '{profile_name}' deleted."}
        return Response(_create_response_text(response_data), mimetype='text/plain')
    else:
        response_data = {"success": "0", "message": "Profile not found."}
        return Response(_create_response_text(response_data), mimetype='text/plain', status=404)
