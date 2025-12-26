import os
import configparser
from config.paths import PROFILE_SAVE_PATH

# Generic section name for config files
_SECTION_NAME = "Configuration"  # Stealth: generic name

def save_profile(name, data_dict, rcs_profiles):
    path = os.path.join(PROFILE_SAVE_PATH, f"{name}.ini")
    config = configparser.ConfigParser()
    config[_SECTION_NAME] = {str(k):str(v) for k,v in data_dict.items()}
    
    for r_name, r_data in rcs_profiles.items():
        config[f'profile_{r_name}'] = r_data
        
    with open(path, 'w') as f: config.write(f)

def load_profile(name):
    path = os.path.join(PROFILE_SAVE_PATH, f"{name}.ini")
    if not os.path.exists(path): return {}
    config = configparser.ConfigParser()
    config.read(path)
    if _SECTION_NAME in config:
        return dict(config[_SECTION_NAME])
    # Fallback for old format
    if 'AscendancyProfile' in config:
        return dict(config['AscendancyProfile'])
    return {}