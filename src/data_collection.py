# Data Collection
# Run as administrator for global keyboard capture

import numpy as np
import cv2
import keyboard
import time
import os
from utils.capture_screen import capture_screen
from utils.keyboard_handler import get_pressed_keys, keys_to_output

SAVE_EVERY = 1000
OUTPUT_FILE = '../data/training_data.npy'
REGION = {'top': 40, 'left': 0, 'width': 800, 'height': 600}
IMG_SIZE = (160, 120)  # (width, height)

def main():
    # 3-second countdown
    for i in range(3, 0, -1):
        print(f"Starting in {i}...", end='\r')
        time.sleep(1)
    print("Starting now!           ")

    # Load existing data if file exists
    if os.path.isfile(OUTPUT_FILE):
        print(f"File {OUTPUT_FILE} exists, loading previous data!")
        training_data = list(np.load(OUTPUT_FILE, allow_pickle=True))
    else:
        print(f"File {OUTPUT_FILE} does not exist, starting fresh!")
        training_data = []

    paused = False
    frame_count = 0
    start_time = time.time()

    while True:
        if not paused:
            frame_start = time.time()
            img = capture_screen(REGION, IMG_SIZE)
            keys = get_pressed_keys()
            output = keys_to_output(keys)
            training_data.append([img, output])
            frame_count += 1

            # FPS and timing
            frame_time = time.time() - frame_start
            elapsed = time.time() - start_time
            fps = frame_count / elapsed if elapsed > 0 else 0
            print(f"Frame: {frame_count} | Time: {frame_time:.4f}s | FPS: {fps:.2f} | Output: {output}    ", end='\r')

            # Periodic save
            if frame_count % SAVE_EVERY == 0:
                np.save(OUTPUT_FILE, np.array(training_data, dtype=object))
                print(f"\nSaved {len(training_data)} frames to {OUTPUT_FILE}")

        # Pause/resume with 't' 
        if keyboard.is_pressed('t'):
            paused = not paused
            print("\nPaused. Press 't' to resume." if paused else "\nResumed.")
            time.sleep(1)  # Debounce

        # Quit with 'q' 
        if keyboard.is_pressed('q'):
            print("\nQuitting and saving data...")
            break

    # Final save
    np.save(OUTPUT_FILE, np.array(training_data, dtype=object))
    print(f"Saved {len(training_data)} frames to {OUTPUT_FILE}. Done.")
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 