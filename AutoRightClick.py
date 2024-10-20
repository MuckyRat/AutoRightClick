import threading
import time
from pynput.mouse import Button, Controller as MouseController
from pynput import keyboard

# Global variable to control the clicker
clicking = False

def click_right():
    global clicking
    mouse_controller = MouseController()
    while clicking:
        mouse_controller.click(Button.right)  # Perform right click
        time.sleep(0.05)  # 50 milliseconds

def toggle_clicking():
    global clicking
    clicking = not clicking  # Toggle the clicking state
    if clicking:
        threading.Thread(target=click_right, daemon=True).start()
        print("Started clicking.")
    else:
        print("Stopped clicking.")

def on_activate():
    toggle_clicking()

# Setting up the key listener
hotkey = keyboard.GlobalHotKeys({
    '<cmd>+z': on_activate  # Set Cmd + Z as the hotkey
})

# Start listening
hotkey.start()
print("Press Cmd + Z to start/stop right clicking.")
print("Press Ctrl + C to exit the program.")

# Keep the program running
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exiting...")
