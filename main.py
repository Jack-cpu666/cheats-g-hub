# ============================================
# Debug control - MUST BE FIRST
# Set DEBUG_ENABLED in debugprints.py to False for silent mode
# ============================================
from debugprints import configure_output, debug_print, DEBUG_ENABLED
configure_output()

import sys
import time
import threading
import logging
import random
import webbrowser
import socket
from config.logger_config import setup_logging
from config.constants import APP_NAME, APP_VERSION
from global_state import state
from startup.initialization import initialize_drivers, setup_listeners
from core.thread import AimbotTriggerbotThread
from web.flask_app import create_app
from startup.cleanup import setup_signal_handlers
from core.security import set_process_name, check_debugger, randomize_memory_footprint
from core.advanced_security import (
    is_capture_software_running,
    is_anticheat_window_visible,
    clean_traces,
    add_execution_noise,
    is_system_freshly_booted,
    check_virtual_machine,
    integrity_checker,
    dummy_operation
)
from core.v7_anticheat import init_v7_protection, get_v7_protection


def get_local_ip():
    """Get the local IP address for LAN access"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"


def perform_security_checks() -> bool:
    """
    Perform all security checks before starting.
    Returns False if environment is unsafe.
    """
    # Check for debuggers
    if check_debugger():
        return False
    
    # Check for capture software (optional warning)
    if is_capture_software_running():
        logging.warning("Screen capture software detected - proceed with caution")
    
    # Check for very fresh boot (suspicious)
    if is_system_freshly_booted(threshold_minutes=3):
        logging.warning("System freshly booted - delaying startup")
        time.sleep(random.uniform(5, 15))
    
    # VM check (just log, don't block)
    if check_virtual_machine():
        logging.info("Virtual machine detected")
    
    return True


def start_flask_with_license():
    """Start Flask server with HWID-based membership validation"""
    from flask import Flask, request, redirect, jsonify
    from web.flask_app import create_app
    from auth.membership import get_membership_info, MembershipTier
    
    app = create_app()
    
    # Check for valid membership before accessing main app
    @app.before_request
    def check_membership():
        # Allow these paths without valid membership
        allowed_paths = [
            '/license',
            '/api/membership',
            '/payment',
            '/static'
        ]
        
        # Check if path is allowed
        for path in allowed_paths:
            if request.path.startswith(path):
                return None
        
        # Check membership status (reads from encrypted file)
        membership = get_membership_info()
        
        if membership.tier == MembershipTier.NONE:
            # No valid membership - redirect to purchase page
            return redirect('/license')
        
        return None
    
    # Purchase/Subscription page
    @app.route('/license')
    def license_page():
        from web.license_template import LICENSE_TEMPLATE
        from flask import render_template_string
        from auth.membership import get_hwid
        
        return render_template_string(LICENSE_TEMPLATE,
            APP_NAME=APP_NAME,
            APP_VERSION=APP_VERSION,
            HWID=get_hwid()
        )
    
    # Get the local IP
    local_ip = get_local_ip()
    port = 5000
    
    debug_print(f"\n{'='*50}")
    debug_print(f"  {APP_NAME} v{APP_VERSION}")
    debug_print(f"{'='*50}")
    debug_print(f"  Web UI: http://{local_ip}:{port}")
    debug_print(f"{'='*50}\n")
    
    # Auto-open browser
    webbrowser.open(f'http://{local_ip}:{port}')
    
    # Run Flask (suppress output if debug disabled)
    if DEBUG_ENABLED:
        app.run(host="0.0.0.0", port=port, use_reloader=False)
    else:
        # Suppress werkzeug logging
        import logging as log
        log.getLogger('werkzeug').disabled = True
        app.run(host="0.0.0.0", port=port, use_reloader=False)


def main():
    # Stealth: Rename process immediately
    set_process_name()
    randomize_memory_footprint()
    
    # Add some execution noise
    for _ in range(random.randint(2, 5)):
        dummy_operation()
    
    # Perform security checks
    if not perform_security_checks():
        sys.exit(0)
    
    # Clean any traces from previous runs
    clean_traces()
    
    setup_logging()
    logging.info(f"Starting System Service v{APP_VERSION}")

    # Set integrity checkpoints
    integrity_checker.set_checkpoint("version", APP_VERSION)
    integrity_checker.set_checkpoint("pid", sys.executable)

    # V7: Initialize enhanced anti-detection
    logging.info("Initializing V7 protection system...")
    v7 = init_v7_protection()
    status = v7.get_status()
    logging.info(f"V7 Status: Threat Level={status['threat_level']}, Hooks Safe={status['hooks_safe']}")
    
    if status['debugger_detected']:
        logging.error("Debugger detected - exiting")
        sys.exit(0)
    
    add_execution_noise()
    initialize_drivers()

    # Init Core Logic Thread
    aimbot_thread = AimbotTriggerbotThread()
    state.aimbot_thread = aimbot_thread

    # Setup Inputs
    setup_listeners()
    setup_signal_handlers()

    # Start Core Thread
    aimbot_thread.start_scanning()
    
    # Start Web Server with License Validation (in separate thread)
    logging.info("Starting Web Interface with License Validation...")
    flask_thread = threading.Thread(target=start_flask_with_license, name="FlaskServerThread", daemon=True)
    flask_thread.start()

    # Main Keep-Alive Loop with periodic security checks
    last_security_check = time.time()
    security_check_interval = 30  # Check every 30 seconds
    
    try:
        while not state.shutdown_event.is_set():
            current_time = time.time()
            
            # Periodic security checks
            if current_time - last_security_check > security_check_interval:
                last_security_check = current_time
                
                # Debugger check
                if check_debugger():
                    logging.warning("Debugger detected during runtime")
                    state.shutdown_event.set()
                    break
                
                # Add some execution noise
                add_execution_noise()
                
                # Randomize memory
                randomize_memory_footprint()
                
                # Verify integrity
                if not integrity_checker.verify_checkpoint("version", APP_VERSION):
                    logging.warning("Integrity check failed")
                    state.shutdown_event.set()
                    break

            # Check thread health with debug logging
            aimbot_alive = aimbot_thread.is_alive()
            flask_alive = flask_thread.is_alive()
            
            if not aimbot_alive:
                logging.error("CRITICAL: Aimbot thread died!")
                state.shutdown_event.set()
                break
            if not flask_alive:
                logging.error("CRITICAL: Flask thread died!")
                state.shutdown_event.set()
                break
            
            # Variable sleep to avoid timing patterns
            time.sleep(random.uniform(0.4, 0.6))
            
    except KeyboardInterrupt:
        logging.info("KeyboardInterrupt received, shutting down...")
        state.shutdown_event.set()
    except Exception as e:
        logging.error(f"CRITICAL ERROR in main loop: {e}")
        import traceback
        logging.error(traceback.format_exc())
        state.shutdown_event.set()

    # Cleanup
    logging.info("Shutting down...")
    aimbot_thread.stop_scanning()
    clean_traces()
    
    # Only wait for input if debug is enabled
    if DEBUG_ENABLED:
        input("Press Enter to exit...")
    
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        if DEBUG_ENABLED:
            import traceback
            print(f"\n\nCRITICAL ERROR: {e}")
            print(traceback.format_exc())
            input("Press Enter to exit...")