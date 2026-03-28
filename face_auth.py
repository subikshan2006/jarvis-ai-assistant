from voice_input import listen_to_user
from voice_output import speak_to_user

# 🔐 Your custom passphrase
PASSWORD = "jarvis"  # You can change this

def verify_user():
    speak_to_user("🔐 Please say your password to continue.")
    print("🎤 Awaiting voice password...")

    try:
        user_input = listen_to_user()
        print(f"🧠 You said: {user_input}")

        if PASSWORD.lower() in user_input.lower():
            speak_to_user("✅ Access granted. Welcome back, Subikshan.")
            return True
        else:
            speak_to_user("❌ Access denied. Incorrect password.")
            return False

    except Exception as e:
        speak_to_user(f"⚠️ Error during verification: {str(e)}")
        return False
