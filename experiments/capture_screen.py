# pip install mss opencv-python numpy

import cv2
import numpy as np
from mss import mss
import time

def capture_screen(region=None):
    """
    Capture a region of the screen using mss and return as a numpy array in RGB format (no alpha channel).
    :param region: dict with keys 'top', 'left', 'width', 'height' or None for full screen
    :return: numpy array (H, W, 3) in RGB
    """
    with mss() as sct:
        screenshot = sct.grab(region) if region else sct.grab(sct.monitors[1])
        img = np.array(screenshot)
        # Remove alpha channel if present
        if img.shape[2] == 4:
            img = img[:, :, :3]
        # Convert BGR to RGB
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img

if __name__ == "__main__":
    try:
        region = {'top': 40, 'left': 0, 'width': 800, 'height': 600}
        print("Press 'q' in the image window to quit.")
        while True:
            start_time = time.time()
            img = capture_screen(region)
            cv2.imshow('Captured Screen', img)
            elapsed = time.time() - start_time
            fps = 1.0 / elapsed if elapsed > 0 else float('inf')
            print(f"Loop time: {elapsed:.4f} s, FPS: {fps:.2f}")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"An error occurred: {e}")