import keyboard

def get_pressed_keys():
    """Return a set of currently pressed keys among 'w', 'a', 'd'."""
    return {k for k in ['w', 'a', 'd'] if keyboard.is_pressed(k)}


def keys_to_output(keys):
    """
    Convert pressed keys to a 6-element output vector with priority:
    wa > wd > a > d > w > none
    [a, w, d, wa, wd, none]
    """
    if 'w' in keys and 'a' in keys:
        return [0, 0, 0, 1, 0, 0]  # wa
    elif 'w' in keys and 'd' in keys:
        return [0, 0, 0, 0, 1, 0]  # wd
    elif 'a' in keys:
        return [1, 0, 0, 0, 0, 0]  # a
    elif 'd' in keys:
        return [0, 0, 1, 0, 0, 0]  # d
    elif 'w' in keys:
        return [0, 1, 0, 0, 0, 0]  # w
    else:
        return [0, 0, 0, 0, 0, 1]  # none 