import cv2
import os
import collections
from datetime import datetime
from config.paths import RECORDING_SAVE_PATH

class VideoRecorder:
    def __init__(self, fps=60):
        if not os.path.exists(RECORDING_SAVE_PATH):
            os.makedirs(RECORDING_SAVE_PATH, exist_ok=True)
        self.writer = None
        self.is_recording = False
        self.fps = fps
        self.buffer = collections.deque(maxlen=60) # pre-roll

    def start(self, reason, width, height):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join(RECORDING_SAVE_PATH, f"clip_{ts}_{reason}.avi")
        self.writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'XVID'), self.fps, (width, height))
        self.is_recording = True
        
        # Write buffer
        for frame in list(self.buffer):
            self.writer.write(frame)

    def write_frame(self, frame):
        if self.is_recording and self.writer:
            self.writer.write(frame)
        else:
            self.buffer.append(frame)

    def stop(self):
        if self.writer:
            self.writer.release()
        self.is_recording = False