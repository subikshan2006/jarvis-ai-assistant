import os
import subprocess
import pygetwindow as gw
import pyautogui

# 👇 Define your app launch paths here
APP_PATHS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad.exe",
    "cmd": "cmd.exe",
    "explorer": "explorer.exe",
    "vscode": r"C:\Users\admin\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "paint": "mspaint.exe",
}

def control_pc(query):
    query = query.lower()

    # 🎯 Open app
    for name in APP_PATHS:
        if f"open {name}" in query or f"start {name}" in query:
            try:
                subprocess.Popen(APP_PATHS[name])
                return f"✅ Opening {name}"
            except Exception as e:
                return f"❌ Failed to open {name}: {e}"

    # 🔫 Close app
    for name in APP_PATHS:
        if f"close {name}" in query or f"terminate {name}" in query:
            try:
                windows = gw.getWindowsWithTitle(name.capitalize())
                if windows:
                    for win in windows:
                        win.close()
                    return f"🛑 Closed {name}"
                else:
                    return f"⚠️ {name} not found"
            except Exception as e:
                return f"❌ Could not close {name}: {e}"

    return None
