# pip install keyboard
# IMPORTANT: Run this script as administrator on Windows.

import keyboard
import time

print("This script will simulate a model outputting 'w' every frame by pressing and releasing 'w' in each loop.\nPress Ctrl+C to stop.")

# Countdown
for i in range(3, 0, -1):
    print(f"Starting in {i}...", end='\r')
    time.sleep(1)
print("Starting now!           ")

# --- Previous continuous hold logic  ---
# try:
#     toggle = True  # Start with 'a'
#     while True:
#         if toggle:
#             print("Pressing: A (W is held)")
#             keyboard.press('a')
#             keyboard.press('w')
#             keyboard.release('d')
#         else:
#             print("Pressing: D (W is held)")
#             keyboard.press('d')
#             keyboard.press('w')
#             keyboard.release('a')
#         time.sleep(1)
#         toggle = not toggle
# except KeyboardInterrupt:
#     print("\nSimulation stopped. Releasing all keys.")
#     for k in ['w', 'a', 'd']:
#         keyboard.release(k)

# --- New per-frame press/release logic ---
try:
    while True:
        keyboard.press('w')
        print("Frame: Pressed 'w'")
        time.sleep(0.05)  # Simulate frame duration (~20 FPS)
        keyboard.release('w')
        print("Frame: Released 'w'")
        # time.sleep(0.01)  # Small gap before next frame
except KeyboardInterrupt:
    print("\nSimulation stopped. Releasing 'w'.")
    keyboard.release('w')
