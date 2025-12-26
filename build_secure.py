import os
import subprocess
import sys
import multiprocessing

def install_nuitka():
    print("Installing Nuitka and dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nuitka", "zstandard", "ordered-set"])

def build():
    # Base directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Use half the CPU cores to avoid memory pressure and context switching
    cpu_count = max(1, multiprocessing.cpu_count() // 2)
    print(f"Using {cpu_count} parallel jobs (half cores to avoid memory pressure)")
    
    # Check if Nuitka is installed
    try:
        import nuitka
    except ImportError:
        install_nuitka()

    print("Starting Optimized Secure Build with Nuitka...")
    
    # Main entry point
    main_script = os.path.join(base_dir, "main.py")
    
    # Construct Nuitka command with OPTIMIZATIONS for yt-dlp
    cmd = [
        sys.executable, "-m", "nuitka",
        "--onefile",                        # Create a single executable
        "--standalone",                     # Include all dependencies
        "--windows-console-mode=disable",   # NO console window - GUI only (new syntax)
        "--windows-icon-from-ico=icon.ico", # Icon
        "--enable-plugin=tk-inter",         # Tkinter support
        
        # OPTIMAL parallel jobs (half cores to reduce contention)
        f"--jobs={cpu_count}",
        
        # Core hidden imports
        "--include-module=flask_socketio",
        "--include-module=engineio.async_drivers.threading",
        "--include-module=pynput.keyboard._win32",
        "--include-module=pynput.mouse._win32",
        "--include-module=web.routes.spotify",
        
        # yt-dlp: Use include-package ONLY (not both include-module AND include-package)
        "--include-package=yt_dlp",
        
        # CRITICAL: Prevent Nuitka from deep-optimizing the massive lazy_extractors module
        # This is where most of the slowdown comes from
        "--nofollow-import-to=yt_dlp.extractor.lazy_extractors",
        
        # Include data files
        f"--include-data-file={os.path.join(base_dir, 'crosshair', 'crosshairs.json')}=crosshair/crosshairs.json",
        f"--include-data-file={os.path.join(base_dir, 'crosshair', 'crosshairs_simple.json')}=crosshair/crosshairs_simple.json",
        
        # Output directory
        "--output-dir=dist_secure",
        "--output-filename=Ascendancy_GHub.exe",
        
        # DISABLED LTO - minimal benefit for Python apps, huge compile time cost
        # "--lto=yes",
        
        # Auto-download required tools
        "--assume-yes-for-downloads",
        
        # Show progress
        "--show-progress",
        
        main_script
    ]
    
    print("\n" + "="*60)
    print("OPTIMIZATIONS APPLIED:")
    print("="*60)
    print("✓ Disabled LTO (saves significant compile time)")
    print("✓ nofollow-import for lazy_extractors (prevents deep analysis)")
    print("✓ Removed redundant yt_dlp includes")
    print(f"✓ Using {cpu_count} jobs (optimal for memory)")
    print("✓ G Hub driver integration")
    print("="*60 + "\n")
    
    print("Command:", " ".join(cmd))
    print("\nRunning optimized compilation...\n")
    
    try:
        subprocess.check_call(cmd)
        print("\n" + "="*60)
        print("[+] BUILD SUCCESS!")
        print("="*60)
        print("Your standalone executable is in: dist_secure/Ascendancy_GHub.exe")
        print("Everything is bundled - no external dependencies needed!")
        print("\nRemember: Users need Logitech G Hub 2021.3.5164 installed!")
    except subprocess.CalledProcessError as e:
        print(f"\n[-] Build Failed with error code {e.returncode}")
        print("Tip: You may need to install a C compiler if Nuitka prompts you.")

if __name__ == "__main__":
    build()
