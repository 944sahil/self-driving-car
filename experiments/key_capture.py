# pip install keyboard
# IMPORTANT: Run this script as administrator on Windows.

import keyboard
import time

KEYS = ['a', 'w', 'd']

print("Press 'q' to quit.")

while True:
    key_array = [1 if keyboard.is_pressed(k) else 0 for k in KEYS]
    print(f"Keys pressed [A, W, D]: {key_array}", end='\r')
    if keyboard.is_pressed('q'):
        print("\nExiting.")
        break
    time.sleep(0.05) 