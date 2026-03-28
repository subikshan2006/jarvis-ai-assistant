import os
import webbrowser
import datetime
import random
from voice_output import speak_to_user

def handle_intent(command: str) -> bool:
    command = command.lower()

    # 🕒 Time
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak_to_user(f"The current time is {now}")
        return True

    # 📅 Date
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak_to_user(f"Today is {today}")
        return True

    # 🎵 Music
    elif "play music" in command or "play a song" in command:
        os.startfile("C:\\Users\\admin\\Music")  # Or any music player
        speak_to_user("Playing your music.")
        return True

    # 🎭 Joke
    elif "joke" in command:
        jokes = [
            "Why did the computer go to the doctor? Because it had a virus!",
            "I'm not lazy, I'm just on energy-saving mode.",
            "Why do programmers hate nature? It has too many bugs."
        ]
        speak_to_user(random.choice(jokes))
        return True

    # 🧮 Calculator
    elif "calculator" in command:
        os.system("start calc")
        speak_to_user("Opening calculator.")
        return True

    # 🌤️ Weather
    elif "weather" in command:
        webbrowser.open("https://www.google.com/search?q=weather")
        speak_to_user("Here is the weather update.")
        return True

    # 🚫 No matched intent
    return False
