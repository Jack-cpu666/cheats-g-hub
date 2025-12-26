
import PyInstaller.__main__
import os
import sys

# Define base directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Data files to include
# Format: (source_path, destination_folder_inside_exe)
data_files = [
    (os.path.join(base_dir, 'crosshair', 'crosshairs.json'), 'crosshair'),
    (os.path.join(base_dir, 'crosshair', 'crosshairs_simple.json'), 'crosshair')
]

# Construct --add-data arguments
add_data_args = []
for src, dest in data_files:
    if os.path.exists(src):
        # PyInstaller separator is ; on Windows
        add_data_args.append(f'--add-data={src};{dest}')
    else:
        print(f"Warning: {src} not found, skipping.")

# PyInstaller arguments
args = [
    'main.py',                          # Entry point
    '--name=Ascendancy_Holiday_Edition', # Executable name
    '--onefile',                        # Bundle into single EXE
    '--console',                        # Keep console for license input
    '--clean',                          # Clean cache
    '--icon=icon.ico',                  # Holiday Icon
    '--hidden-import=engineio.async_drivers.threading', # SocketIO dependency
    '--hidden-import=flask_socketio',   
    '--hidden-import=pynput.keyboard._win32',
    '--hidden-import=pynput.mouse._win32',
    '--hidden-import=web.routes.api_v7',  # V7 API
    '--hidden-import=core.v7_anticheat',  # V7 Core
    '--hidden-import=core.mouse_humanizer', # Humanizer Engine
    '--log-level=INFO',
] + add_data_args

print("Starting PyInstaller build...")
print(f"Arguments: {args}")

try:
    PyInstaller.__main__.run(args)
    print("\nBuild completed successfully!")
    print(f"Executable should be in: {os.path.join(base_dir, 'dist', 'Ascendancy_Holiday_Edition.exe')}")
except Exception as e:
    print(f"\nBuild failed: {e}")
