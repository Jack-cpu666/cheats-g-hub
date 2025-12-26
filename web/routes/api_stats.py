from flask import Response
from global_state import state
import json

def get_stats():
    t = state.aimbot_thread
    data = {
        "fps": f"{t.current_fps:.1f}" if t else "0",
        "running": "1" if (t and t.running) else "0"
    }
    # Used custom serialization in V6, replicating text output
    return Response(f"fps={data['fps']}&is_running={data['running']}", mimetype='text/plain')