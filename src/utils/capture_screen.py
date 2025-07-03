import mss
import numpy as np
import cv2

def capture_screen(region, img_size):
    """
    Capture a region of the screen, convert to grayscale, resize, and return as numpy array.
    region: dict with 'top', 'left', 'width', 'height'
    img_size: (width, height) tuple for resizing
    """
    with mss.mss() as sct:
        img_color = np.array(sct.grab(region))
    img = cv2.cvtColor(img_color, cv2.COLOR_BGRA2GRAY)
    img = cv2.resize(img, img_size)
    return img