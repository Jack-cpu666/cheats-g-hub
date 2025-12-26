                                Technical Documentation

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [V7 Enhanced Protection](#v7-enhanced-protection)
3. [Mouse Humanization Engine](#mouse-humanization-engine)
4. [Detection Bypass Techniques](#detection-bypass-techniques)
5. [Configuration](#configuration)
6. [API Reference](#api-reference)
7. [Best Practices](#best-practices)

---

## Executive Summary

This document describes the **Ascendancy V6 Security Specification**, comprising two major subsystems:
1.  **V7 Enhanced Protection**: A kernel-aware security layer that prevents reverse engineering, debugging, and anti-cheat hooks.
2.  **Mouse Humanization Engine**: An advanced input simulation system that bypasses behavioral analysis (heuristic) anti-cheats like Vanguard.

---

## V7 Enhanced Protection

The V7 module (`core/v7_anticheat.py`) provides active defense against detection vectors beyond simple input analysis.

### Core Security Modules

| Module | Function |
|--------|----------|
| **Memory Randomizer** | Periodically reallocates heap memory to prevent signature scanning. |
| **API Hook Detector** | Checks critical Windows APIs (`ReadFile`, `DeviceIoControl`) for JMP hooks used by anti-cheats (e.g., Vanguard's user-mode hooks). |
| **Thread Cloaker** | Uses `NtSetInformationThread` (0x11) to hide execution threads from debuggers. |
| **Timing Obfuscator** | Adds randomized jitter (1-15ms) to execution loops to defeat timing-based detection. |
| **Syscall Obfuscator** | Adds noise before/after system calls to evade behavioral pattern matching. |
| **Process Scanner** | Actively scans for known anti-cheat processes (`vgc.exe`, `easyanticheat.exe`) and adjusts threat levels. |

### Status Levels

- **LOW**: No threats detected.
- **MEDIUM**: Suspicious activity or standard anti-cheat found.
- **HIGH**: Known kernel-level anti-cheat active (EAC/BattlEye).
- **CRITICAL**: Vanguard (vgk.sys/vgc.exe) detected. Maximum obfuscation enabled.

---

## Mouse Humanization Engine

The Humanizer (`core/mouse_humanizer.py`) mimics physical human hand usage characteristics.

### 1. Session Fingerprinting
Generates a unique "Bio-Signature" for each session to prevent cross-match correlation.
- **Randomized Variables**: Reaction time offset, tremor intensity, curve tightness, overshoot tendency.
- **Effect**: If you play two matches, your "aim signature" looks like two different (but skilled) players.

### 2. Polling Rate Emulation
Simulates the imperfect timing of physical USB hardware.
- **Real Mouse**: 1000Hz = ~1ms intervals with ±10% variance.
- **Our Emulator**: Adds Perlin-noise based jitter to match this physical imperfection, defeating "perfect interval" detection.

### 3. Bézier Path Generation
Replaces straight-line bot movement with cubic Bézier curves.
- **Control Points**: Randomized via Perlin noise.
- **Deviation**: Context-aware (strafing vs flicking).

---

## Detection Bypass Techniques

### Technique 1: Velocity Profiling
**Problem**: Bots accelerate instantly.
**Solution**: We implement **Ease-In/Ease-Out** acceleration.
```python
velocity = sin(progress * π) * 0.7 + 0.3
```
This creates natural "bell curve" velocity profiles indistinguishable from hand movement.

### Technique 2: Overshoot & Correction
**Problem**: Bots stop exactly on target pixel (0.0 error).
**Solution**: The system intentionally overshoots by ~8% in 35% of flicks, then corrects back after a human-like delay (~25ms).

### Technique 3: Hand Tremor
**Problem**: Bot aim is perfectly smooth.
**Solution**: **Perlin Noise Tremor** is layered on top of all movements.
- **Stress Multiplier**: Tremor increases during "close combat" or rapid movement (Adrenaline simulation).

---

## Configuration

Settings are adjustable via the Web UI (`core/humanizer_settings.py`).

| Setting | Recommended (Legit) | Recommended (Rage) |
|---------|-------------------|-------------------|
| Reaction Time | 220 ms | 150 ms |
| Tremor Amp | 1.5 px | 0.5 px |
| Smoothing | 0.15 | 0.05 |
| Overshoot % | 35% | 10% |

---

## API Reference

The application exposes a local REST API for the UI.

### Security & Stats

#### `POST /api/regenerate_fingerprint`
Forces generation of a new behavioral fingerprint. Call between matches.

#### `GET /api/humanizer_stats`
Returns current session statistics (overshoots, average speed, etc.).

#### `GET /api/stats`
Returns general application performance (FPS, thread health).

### Settings Management

#### `POST /api/update`
Update any setting (aimbot, triggerbot, humanizer).
**Body**: Form data (`key=value`).

#### `GET /api/humanizer_settings`
Retrieve current humanizer configuration.

#### `POST /api/reset_settings`
Factory reset all configuration.

---

## Best Practices

1.  **Vanguard Security**: When playing Valorant, ensure the "V7 Status" shows **CRITICAL** (meaning it successfully detects Vanguard is watching).
2.  **Fingerprint Rotation**: Click "Regenerate Fingerprint" after every match.
3.  **Visual Verification**: Use the "Anti-Detection" tab in the UI to visualize your current curve and tremor settings.
4.  **Hardware Match**: Set the "Polling Rate" in the humanizer tab to match your physical mouse (e.g., 1000Hz).

---

Jack
