from voice_input import listen_to_user
from voice_output import speak_to_user
from brain import ask_brain
from web_search import search_web
from memory import remember, recall, add_to_autolearning_history
from learn import learn_from_file, ask_about_file
from system_control import control_pc
from reminder import add_reminder, start_reminder_loop
from intent_router import handle_intent
from face_auth import verify_user
from wake_listener import wait_for_wake_word
from pdf_reader import learn_pdf
from cleanup import auto_cleanup
from system_status import get_system_info
from image_reader import extract_text_from_image
from file_manager import list_files_in_folder, open_file, delete_file

import threading
import time

def run_jarvis():
    start_reminder_loop()

    while True:
        wait_for_wake_word()

        query = listen_to_user().lower()
        print(f"📥 Heard: {query}")

        if not query.strip():
            print("🛑 I didn't catch that. Try again...")
            continue

        # 🖥️ System control
        control_result = control_pc(query)
        if control_result:
            speak_to_user(control_result)
            continue

        # 🧠 Manual memory
        if query.startswith("remember that"):
            parts = query.replace("remember that", "").strip().split(" is ")
            if len(parts) == 2:
                key, value = parts
                remember(key.strip(), value.strip())
                speak_to_user(f"Got it. I will remember that {key.strip()} is {value.strip()}.")
            else:
                speak_to_user("Sorry, I didn't understand what to remember.")
            continue

        # 🧠 Recall
        if query.startswith("what is") or query.startswith("who is"):
            key = query.replace("what is", "").replace("who is", "").strip()
            value = recall(key)
            if value:
                speak_to_user(f"{key} is {value}")
            else:
                speak_to_user(f"I don't know who or what {key} is.")
            continue

        # 📂 Learn from file
        if query.startswith("learn file"):
            file_path = query.replace("learn file", "").strip().strip('"').strip("'")
            response = learn_from_file(file_path)
            speak_to_user(response)
            continue

        # ❓ Ask about learned file
        if query.startswith("ask file"):
            try:
                parts = query.replace("ask file", "").strip().split("about")
                if len(parts) == 2:
                    file_name = parts[0].strip()
                    question = parts[1].strip()
                    response = ask_about_file(file_name, question)
                    speak_to_user(response)
                else:
                    speak_to_user("Please say: ask file [filename] about [question]")
            except:
                speak_to_user("Something went wrong while answering from file.")
            continue

        # 📄 Learn from PDF
        if query.startswith("read pdf"):
            file_path = query.replace("read pdf", "").strip().strip('"').strip("'")
            response = learn_pdf(file_path)
            speak_to_user(response)
            continue

        # 🖼️ Read text from image (OCR)
        if query.startswith("read image"):
            try:
                file_path = query.replace("read image", "").strip().strip('"').strip("'")
                text = extract_text_from_image(image_path)
                speak_to_user("Here's what I found in the image:")
                speak_to_user(response)
            except Exception as e:
                speak_to_user(f"Something went wrong while reading the image: {str(e)}")
            continue

        # ⏰ Reminders
        if query.startswith("remind me to"):
            try:
                task = query.replace("remind me to", "").strip()
                if " at " in task:
                    task_text, time_str = task.split(" at ")
                    add_reminder(task_text.strip(), time_str.strip())
                    speak_to_user(f"Okay, I will remind you to {task_text.strip()} at {time_str.strip()}")
                else:
                    speak_to_user("Please say it like: remind me to [task] at [HH:MM]")
            except:
                speak_to_user("Something went wrong while setting the reminder.")
            continue

        # 🧹 Auto cleanup
        if "clean junk" in query or "clean system" in query:
            response = auto_cleanup()
            speak_to_user(response)
            continue

        # 🧠 System info
        if "cpu" in query or "ram" in query or "disk" in query or "battery" in query or "network" in query:
            response = get_system_info(query)
            speak_to_user(response)
            continue

        # 📁 List folder files
        if query.startswith("list folder"):
            folder_path = query.replace("list folder", "").strip().strip('"').strip("'")
            response = list_files_in_folder(folder_path)
            speak_to_user(response)
            continue

        # 📂 Open file
        if query.startswith("open file"):
            file_path = query.replace("open file", "").strip().strip('"').strip("'")
            response = open_file(file_path)
            speak_to_user(response)
            continue

        # 🗑️ Delete file
        if query.startswith("delete file"):
            file_path = query.replace("delete file", "").strip().strip('"').strip("'")
            response = delete_file(file_path)
            speak_to_user(response)
            continue

        # 🧠 Intent router
        if handle_intent(query):
            continue

        # 🌐 Web search fallback or LLM
        if "search" in query or "look up" in query:
            response = search_web(query)
        else:
            response = ask_brain(query)

        print(f"Jarvis: {response}")
        speak_to_user(response)

        # 🧠 Learning log
        add_to_autolearning_history(query, response)

if __name__ == "__main__":
    # 🔐 Face authentication
    if not verify_user():
        print("❌ Access denied. Exiting...")
        exit()

    # 🔁 Run JARVIS loop
    reminder_thread = threading.Thread(target=run_jarvis)
    reminder_thread.start()

    while True:
        time.sleep(1)
