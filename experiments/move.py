import win32gui
import win32con

def move_gta_to_corner():
    hwnd = win32gui.FindWindow(None, "Grand Theft Auto V") 
    if hwnd == 0:
        print("GTA window not found.")
        return

    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # Restore if minimized

    # Get current window size
    rect = win32gui.GetWindowRect(hwnd)
    width = rect[2] - rect[0]
    height = rect[3] - rect[1]

    # Move to top-left corner (0,0)
    win32gui.MoveWindow(hwnd, -2, 6, width, height, True)

    print(f"Moved GTA window to (0,0) with original size {width}x{height}")

move_gta_to_corner()
