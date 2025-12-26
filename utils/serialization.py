# Helpers for API data
def text_serialize_dict(data_dict):
    if not isinstance(data_dict, dict): return ""
    return "&".join([f"{k}={v}" for k, v in data_dict.items()])

def text_deserialize_dict(text_data):
    result = {}
    if not text_data: return result
    try:
        pairs = text_data.split("&")
        for pair in pairs:
            if "=" in pair:
                k, v = pair.split("=", 1)
                result[k] = v
    except Exception: pass
    return result

def text_deserialize_points(text_data):
    if not text_data: return []
    try:
        points = []
        point_strs = text_data.split("|")
        for point_str in point_strs:
            if ";" in point_str:
                x_str, y_str = point_str.split(";", 1)
                points.append([int(x_str), int(y_str)])
        return points
    except Exception: return []

def text_serialize_gun_profiles(profiles_dict):
    # Logic from original script
    if not isinstance(profiles_dict, dict): return ""
    result_parts = []
    for gun_name, profile in profiles_dict.items():
        if isinstance(profile, dict):
            profile_parts = []
            for key, value in profile.items():
                if key == "recoil_pattern" and isinstance(value, list):
                    # Manual point serialization
                    pt_text = "|".join([f"{p[0]};{p[1]}" for p in value if len(p)>=2])
                    profile_parts.append(f"{key}:{pt_text}")
                else:
                    profile_parts.append(f"{key}:{value}")
            result_parts.append(f"{gun_name}#{{'|'.join(profile_parts)}}")
    return "||".join(result_parts)