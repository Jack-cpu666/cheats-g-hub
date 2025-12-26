# Valorant Gun Profiles - Updated for Patch 11.08 (October 2025)
# 
# Key Changes in Patch 11.08:
# - Vandal: Protected bullets 4→6, Yaw switch time 0.37s→0.6s, Yaw switch chance 6%→10%
# - Phantom: Protected bullets 6→8, Yaw switch time 0.37s→0.6s, Yaw switch chance 6%→10%
# - Bulldog: Yaw switch time 0.37s→0.6s, Yaw switch chance 6%→10%
# - Spectre: Protected bullets 4→5, Yaw switch time 0.18s→0.28s, Spread reduced 1.5→1.3
# - Stinger: More aggressive vertical recoil curve, Spread increased 1.3→1.5
#
# Profile Structure:
# - cooldown: Time between shots in seconds (1/fire_rate)
# - protected_bullets: Number of bullets before horizontal recoil kicks in
# - rcs_delay: Delay before RCS pattern starts (ms)
# - rcs_v_str: Vertical recoil strength multiplier
# - rcs_h_str: Horizontal recoil strength multiplier
# - rcs_dur: Total recoil compensation duration (ms)
# - yaw_switch_time: Time for horizontal direction change (seconds)
# - recoil_pattern: List of [horizontal_offset, vertical_offset] points

valorant_gun_profiles = {
    "Custom": {
        "cooldown": 0.15,
        "protected_bullets": 4,
        "rcs_delay": 0,
        "rcs_v_str": 5,
        "rcs_h_str": 0,
        "rcs_dur": 200,
        "yaw_switch_time": 0.4,
        "recoil_pattern": [[0, 5], [1, 10], [-1, 15], [2, 19], [-2, 22]]
    },
    
    # === RIFLES ===
    "Vandal": {
        "cooldown": 0.102,  # 9.75 rounds/sec
        "protected_bullets": 6,  # Updated from 4 in Patch 11.08
        "rcs_delay": 50,
        "rcs_v_str": 14,  # Slightly increased for new pattern
        "rcs_h_str": 4,   # Increased due to 10% yaw switch chance
        "rcs_dur": 700,
        "yaw_switch_time": 0.6,  # Updated from 0.37s in Patch 11.08
        # Pattern: First 6 bullets are protected (near-vertical), then horizontal kicks in
        "recoil_pattern": [
            [0, 6], [0, 10], [0, 14], [0, 18], [0, 22], [0, 26],  # Protected bullets (1-6)
            [-2, 30], [3, 33], [-4, 36], [5, 38], [-6, 40], [7, 42],  # Yaw switching starts
            [-5, 44], [4, 46], [-3, 48], [2, 50], [-1, 52], [0, 54]   # Continued spray
        ]
    },
    "Phantom": {
        "cooldown": 0.091,  # 11 rounds/sec
        "protected_bullets": 8,  # Updated from 6 in Patch 11.08
        "rcs_delay": 40,
        "rcs_v_str": 12,
        "rcs_h_str": 3,
        "rcs_dur": 650,
        "yaw_switch_time": 0.6,  # Updated from 0.37s in Patch 11.08
        # Pattern: First 8 bullets are protected, more forgiving than Vandal
        "recoil_pattern": [
            [0, 5], [0, 9], [0, 13], [0, 17], [0, 21], [0, 25], [0, 28], [0, 31],  # Protected (1-8)
            [-1, 34], [2, 36], [-3, 38], [4, 40], [-4, 42], [3, 44],  # Yaw switching
            [-2, 46], [1, 48], [0, 50], [-1, 52], [1, 54], [0, 56]    # Tail
        ]
    },
    "Bulldog": {
        "cooldown": 0.105,  # 9.5 rounds/sec
        "protected_bullets": 5,
        "rcs_delay": 35,
        "rcs_v_str": 9,
        "rcs_h_str": 4,
        "rcs_dur": 550,
        "yaw_switch_time": 0.6,  # Updated from 0.37s in Patch 11.08
        "recoil_pattern": [
            [0, 5], [0, 9], [0, 13], [0, 17], [0, 20],  # Protected
            [-2, 23], [3, 26], [-4, 28], [5, 30], [-6, 32], [5, 34],
            [-4, 36], [3, 38], [-2, 40], [1, 42]
        ]
    },
    "Guardian": {
        "cooldown": 0.190,  # 5.25 rounds/sec (semi-auto)
        "protected_bullets": 3,
        "rcs_delay": 30,
        "rcs_v_str": 11,
        "rcs_h_str": 2,
        "rcs_dur": 450,
        "yaw_switch_time": 0.5,
        "recoil_pattern": [
            [0, 9], [-1, 14], [2, 18], [-3, 21], [4, 24], [-3, 27], [2, 30]
        ]
    },
    
    # === SMGs ===
    "Spectre": {
        "cooldown": 0.075,  # 13.33 rounds/sec
        "protected_bullets": 5,  # Updated from 4 in Patch 11.08
        "rcs_delay": 30,
        "rcs_v_str": 7,
        "rcs_h_str": 5,
        "rcs_dur": 500,
        "yaw_switch_time": 0.28,  # Updated from 0.18s in Patch 11.08
        # Spread reduced 1.5→1.3, easier to control now
        "recoil_pattern": [
            [0, 4], [0, 7], [0, 10], [0, 13], [0, 16],  # Protected (5 bullets)
            [-2, 18], [3, 20], [-4, 22], [5, 24], [-6, 26], [5, 28],
            [-4, 30], [3, 32], [-2, 34], [1, 36], [0, 38]
        ]
    },
    "Stinger": {
        "cooldown": 0.056,  # 18 rounds/sec
        "protected_bullets": 5,
        "rcs_delay": 25,
        "rcs_v_str": 8,  # Increased for more aggressive vertical in Patch 11.08
        "rcs_h_str": 6,
        "rcs_dur": 400,
        "yaw_switch_time": 0.2,
        # Patch 11.08: More aggressive vertical recoil, spread accrues from bullet 6
        "recoil_pattern": [
            [0, 5], [-1, 8], [2, 11], [-3, 14], [4, 17],  # First 5 relatively stable
            [-5, 21], [6, 25], [-7, 29], [7, 33], [-6, 37],  # Aggressive climb
            [5, 40], [-4, 43], [3, 46], [-2, 48]
        ]
    },
    
    # === MACHINE GUNS ===
    "Ares": {
        "cooldown": 0.085,  # 10→13 rounds/sec (ramping), avg ~11.5
        "protected_bullets": 6,
        "rcs_delay": 100,
        "rcs_v_str": 10,
        "rcs_h_str": 5,
        "rcs_dur": 900,
        "yaw_switch_time": 0.4,
        "recoil_pattern": [
            [0, 6], [0, 10], [-1, 14], [2, 18], [-3, 22], [4, 26],
            [-5, 30], [6, 34], [-7, 38], [8, 42], [-7, 46], [6, 50],
            [-5, 54], [4, 58], [-3, 62], [2, 66], [-1, 70], [0, 74]
        ]
    },
    "Odin": {
        "cooldown": 0.070,  # 12→15.6 rounds/sec (ramping), avg ~13.8
        "protected_bullets": 5,
        "rcs_delay": 120,
        "rcs_v_str": 11,
        "rcs_h_str": 6,
        "rcs_dur": 1000,
        "yaw_switch_time": 0.35,
        "recoil_pattern": [
            [0, 7], [0, 12], [-2, 17], [3, 22], [-4, 27], [5, 32],
            [-6, 37], [7, 42], [-8, 47], [9, 52], [-8, 57], [7, 62],
            [-6, 67], [5, 72], [-4, 77], [3, 82], [-2, 87], [1, 92]
        ]
    },
    
    # === PISTOLS ===
    "Classic": {
        "cooldown": 0.149,  # ~6.7 rounds/sec
        "protected_bullets": 3,
        "rcs_delay": 10,
        "rcs_v_str": 4,
        "rcs_h_str": 2,
        "rcs_dur": 250,
        "yaw_switch_time": 0.3,
        "recoil_pattern": [[0, 3], [0, 5], [-1, 7], [1, 9], [-1, 11], [1, 13]]
    },
    "Shorty": {
        "cooldown": 0.33,  # 2-shot burst shotgun
        "protected_bullets": 2,
        "rcs_delay": 5,
        "rcs_v_str": 3,
        "rcs_h_str": 2,
        "rcs_dur": 150,
        "yaw_switch_time": 0.2,
        "recoil_pattern": [[0, 2], [-1, 4]]
    },
    "Frenzy": {
        "cooldown": 0.1,  # 10 rounds/sec
        "protected_bullets": 4,
        "rcs_delay": 15,
        "rcs_v_str": 5,
        "rcs_h_str": 4,
        "rcs_dur": 300,
        "yaw_switch_time": 0.25,
        "recoil_pattern": [
            [0, 4], [-1, 6], [2, 8], [-3, 10], [4, 12], [-5, 14], [4, 16], [-3, 18]
        ]
    },
    "Ghost": {
        "cooldown": 0.182,  # 5.5 rounds/sec
        "protected_bullets": 4,
        "rcs_delay": 25,
        "rcs_v_str": 7,
        "rcs_h_str": 2,
        "rcs_dur": 350,
        "yaw_switch_time": 0.4,
        "recoil_pattern": [[0, 6], [-1, 9], [2, 12], [-2, 15], [1, 18]]
    },
    "Sheriff": {
        "cooldown": 0.25,  # 4 rounds/sec
        "protected_bullets": 3,
        "rcs_delay": 20,
        "rcs_v_str": 10,
        "rcs_h_str": 2,
        "rcs_dur": 400,
        "yaw_switch_time": 0.5,
        "recoil_pattern": [[0, 10], [-2, 15], [3, 20], [-4, 24], [3, 28]]
    },
    
    # === SHOTGUNS ===
    "Bucky": {
        "cooldown": 0.833,  # ~1.2 rounds/sec
        "protected_bullets": 2,
        "rcs_delay": 20,
        "rcs_v_str": 8,
        "rcs_h_str": 4,
        "rcs_dur": 350,
        "yaw_switch_time": 0.4,
        "recoil_pattern": [[0, 8], [-3, 12], [4, 16]]
    },
    "Judge": {
        "cooldown": 0.285,  # ~3.5 rounds/sec
        "protected_bullets": 3,
        "rcs_delay": 15,
        "rcs_v_str": 6,
        "rcs_h_str": 3,
        "rcs_dur": 300,
        "yaw_switch_time": 0.35,
        "recoil_pattern": [[0, 5], [-2, 8], [3, 11], [-3, 14], [2, 17]]
    },
    
    # === SNIPERS ===
    "Marshal": {
        "cooldown": 0.95,  # ~1.05 rounds/sec
        "protected_bullets": 1,
        "rcs_delay": 0,
        "rcs_v_str": 7,
        "rcs_h_str": 1,
        "rcs_dur": 250,
        "yaw_switch_time": 0.6,
        "recoil_pattern": [[0, 7], [-1, 10]]
    },
    "Operator": {
        "cooldown": 1.5,  # ~0.67 rounds/sec
        "protected_bullets": 1,
        "rcs_delay": 0,
        "rcs_v_str": 3,
        "rcs_h_str": 0,
        "rcs_dur": 150,
        "yaw_switch_time": 0.8,
        "recoil_pattern": [[0, 3]]
    },
    "Outlaw": {
        "cooldown": 1.1,  # 2-shot burst sniper
        "protected_bullets": 2,
        "rcs_delay": 0,
        "rcs_v_str": 5,
        "rcs_h_str": 1,
        "rcs_dur": 200,
        "yaw_switch_time": 0.7,
        "recoil_pattern": [[0, 5], [-1, 8]]
    }
}