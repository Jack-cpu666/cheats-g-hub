import signal
from global_state import state

def signal_handler(signum, frame):
    state.shutdown_event.set()

def setup_signal_handlers():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)