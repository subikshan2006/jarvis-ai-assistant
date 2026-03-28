import schedule
import time
import datetime
import json
import os
from voice_output import speak_to_user

REMINDER_FILE = "reminders.json"

# Load saved reminders
def load_reminders():
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Save reminder list
def save_reminders(reminders):
    with open(REMINDER_FILE, "w", encoding="utf-8") as f:
        json.dump(reminders, f, indent=4)

# Add a new reminder
def add_reminder(task, time_str):
    reminders = load_reminders()
    reminders.append({"task": task, "time": time_str})
    save_reminders(reminders)

# Check and alert on due reminders
def check_reminders():
    reminders = load_reminders()
    now = datetime.datetime.now().strftime("%H:%M")
    new_reminders = []
    for reminder in reminders:
        if reminder["time"] == now:
            speak_to_user(f"⏰ Reminder: {reminder['task']}")
        else:
            new_reminders.append(reminder)
    save_reminders(new_reminders)

# Speak hourly update + reminder status
def hourly_announcement():
    now = datetime.datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        greet = "Good morning"
    elif 12 <= hour < 17:
        greet = "Good afternoon"
    elif 17 <= hour < 22:
        greet = "Good evening"
    else:
        greet = "Working late?"

    speak_to_user(f"{greet}, Subikshan. Here's your update.")

    reminders = load_reminders()
    if reminders:
        speak_to_user(f"You have {len(reminders)} reminder(s) left.")
        for r in reminders[:2]:  # Only read 2 reminders max
            speak_to_user(f"{r['task']} at {r['time']}")
    else:
        speak_to_user("No pending reminders at this moment.")

# Start background reminder schedule
def start_reminder_loop():
    schedule.every().minute.do(check_reminders)
    schedule.every().hour.at(":00").do(hourly_announcement)
