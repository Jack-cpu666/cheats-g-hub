import os
import shutil
import subprocess
import sys
import time

def build_secure():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    temp_dir = os.path.join(base_dir, "temp_secure_build")
    dist_dir = os.path.join(base_dir, "dist")
    
    print("--- Ascendancy Secure Builder (PyArmor + PyInstaller) ---")
    
    # 1. Clean and Create Temp Directory
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    
    print(f"[1/5] Copying project to temporary build workspace: {temp_dir}")
    
    # Copy project files
    def ignore_patterns(path, names):
        return ['dist', 'build', '.git', '__pycache__', 'temp_secure_build', '*.spec']

    for item in os.listdir(base_dir):
        s = os.path.join(base_dir, item)
        d = os.path.join(temp_dir, item)
        if item in ['dist', 'build', '.git', '__pycache__', 'temp_secure_build'] or item.endswith('.spec'):
            continue
        
        if os.path.isdir(s):
            shutil.copytree(s, d, ignore=ignore_patterns)
        else:
            shutil.copy2(s, d)

    # 2. Obfuscate Code using PyArmor
    print("[2/5] Obfuscating source code with PyArmor...")
    
    # We need to run pyarmor on the temp dir
    # We exclude the build scripts themselves
    cmd_obfuscate = [
        sys.executable, "-m", "pyarmor.cli", "gen",
        "--recursive",
        "--output", temp_dir, # Overwrite files in temp_dir
        "--exclude", "build_exe.py",
        "--exclude", "build_secure.py",
        "--exclude", "build_secure_pyarmor.py",
        temp_dir # Source to obfuscate (the temp dir itself)
    ]
    
    try:
        # We need to run this command carefully. 
        # Pyarmor gen -O output path source path
        # If we want to overwrite, we usually do: gen -O temp_dir . (inside temp dir)
        
        subprocess.check_call(
            [sys.executable, "-m", "pyarmor.cli", "gen", "--recursive", "--output", ".", "."], 
            cwd=temp_dir
        )
        print("Obfuscation complete.")
    except subprocess.CalledProcessError as e:
        print(f"Error during obfuscation: {e}")
        return

    # 3. Patching main.py if necessary? 
    # PyArmor gen usually handles entry scripts correctly by inserting the protection code.
    
    # 4. Build EXE using existing build_exe.py
    print("[3/5] Building Executable with PyInstaller...")
    
    # We run the ORIGINAL build_exe.py which is now inside temp_dir
    # It will use the now-obfuscated files in temp_dir
    try:
        subprocess.check_call([sys.executable, "build_exe.py"], cwd=temp_dir)
    except subprocess.CalledProcessError as e:
        print(f"Error during PyInstaller build: {e}")
        return

    # 5. Retrieve Artifacts
    print("[4/5] Retrieving artifacts...")
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)
        
    built_exe_name = "Ascendancy_Holiday_Edition.exe" # Determined from build_exe.py
    src_exe = os.path.join(temp_dir, "dist", built_exe_name)
    dst_exe = os.path.join(dist_dir, "Ascendancy_Secure_Obfuscated.exe")
    
    if os.path.exists(src_exe):
        if os.path.exists(dst_exe):
            os.remove(dst_exe)
        shutil.move(src_exe, dst_exe)
        print(f"SUCCESS: Secure executable created at: {dst_exe}")
    else:
        print("ERROR: Constructed executable not found.")

    # 6. Cleanup
    print("[5/5] Cleaning up...")
    try:
       shutil.rmtree(temp_dir)
    except:
       print("Warning: Could not fully remove temp directory.")

if __name__ == "__main__":
    build_secure()
