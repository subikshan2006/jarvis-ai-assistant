import pyautogui
from datetime import datetime
import os

def take_screenshot():
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"screenshot_{now}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(path)
    return f"Screenshot saved to {path}"
