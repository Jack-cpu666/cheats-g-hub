# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\khjb\\Desktop\\v6\\Ascendancy_V6_Refactored\\crosshair\\crosshairs.json', 'crosshair'), ('C:\\Users\\khjb\\Desktop\\v6\\Ascendancy_V6_Refactored\\crosshair\\crosshairs_simple.json', 'crosshair')],
    hiddenimports=['engineio.async_drivers.threading', 'flask_socketio', 'pynput.keyboard._win32', 'pynput.mouse._win32', 'web.routes.api_v7', 'core.v7_anticheat', 'core.mouse_humanizer'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Ascendancy_Holiday_Edition',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
