"""
V7 Security API Endpoints
"""

from flask import Blueprint, jsonify
from core.v7_anticheat import get_v7_protection

api_v7 = Blueprint('api_v7', __name__)


@api_v7.route('/api/v7/status', methods=['GET'])
def get_v7_status():
    """Get V7 protection status."""
    v7 = get_v7_protection()
    
    if v7 is None:
        return jsonify({
            "initialized": False,
            "error": "V7 protection not initialized"
        })
    
    status = v7.get_status()
    return jsonify(status)


@api_v7.route('/api/v7/scan', methods=['POST'])
def run_security_scan():
    """Run a security scan."""
    v7 = get_v7_protection()
    
    if v7 is None:
        return jsonify({"error": "V7 protection not initialized"})
    
    # Check for hooks
    hooked = v7.hooks.detect_hooks()
    
    # Scan for anti-cheats
    anticheats = v7.scanner.scan()
    
    # Check debugger
    debugger = v7.antidebug.is_debugger_present()
    
    return jsonify({
        "hooked_apis": hooked,
        "detected_anticheats": anticheats,
        "debugger_detected": debugger,
        "threat_level": v7.scanner.get_threat_level(),
        "memory_allocations": len(v7.memory.allocations)
    })


@api_v7.route('/api/v7/shuffle', methods=['POST'])
def shuffle_memory():
    """Shuffle memory allocations."""
    v7 = get_v7_protection()
    
    if v7 is None:
        return jsonify({"error": "V7 protection not initialized"})
    
    v7.memory.shuffle_allocations()
    
    return jsonify({
        "success": True,
        "allocations": len(v7.memory.allocations)
    })
