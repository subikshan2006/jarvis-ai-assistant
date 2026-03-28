import asyncio
from edge_tts import Communicate

# 🗣️ Voice settings: Male, 25-ish tone
VOICE = "en-US-GuyNeural"

async def speak(text):
    try:
        communicate = Communicate(text=text, voice=VOICE)
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                with open("output.mp3", "ab") as f:
                    f.write(chunk["data"])
        # Play the audio
        import os
        os.system("start output.mp3")
    except Exception as e:
        print(f"Voice error: {e}")

def speak_to_user(text):
    print(f"🔊 Speaking: {text}")
    asyncio.run(speak(text))
