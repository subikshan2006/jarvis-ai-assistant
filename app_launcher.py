import os
import json
import subprocess

APP_INDEX_FILE = "app_index.json"
SEARCH_DIRS = [
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    os.path.expanduser("~\\AppData\\Local\\Programs"),
    os.path.expanduser("~\\AppData\\Roaming"),
]

def build_app_index():
    print("🧠 Scanning apps, please wait...")
    app_index = {}

    for folder in SEARCH_DIRS:
        for root, _, files in os.walk(folder):
            for file in files:
                if file.lower().endswith(".exe"):
                    app_name = file.lower().replace(".exe", "")
                    full_path = os.path.join(root, file)
                    app_index[app_name] = full_path

    with open(APP_INDEX_FILE, "w") as f:
        json.dump(app_index, f)

    print(f"✅ App index built: {len(app_index)} apps found")

def load_app_index():
    if not os.path.exists(APP_INDEX_FILE):
        build_app_index()
    with open(APP_INDEX_FILE, "r") as f:
        return json.load(f)

def open_application(command_text):
    apps = load_app_index()
    command_text = command_text.lower()

    for app_name, app_path in apps.items():
        if app_name in command_text:
            try:
                subprocess.Popen(app_path)
                return f"Opening {app_name}."
            except Exception as e:
                return f"Failed to open {app_name}: {str(e)}"

    return "❌ Sorry, I couldn't find that application."
