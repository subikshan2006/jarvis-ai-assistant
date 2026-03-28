from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np
import tempfile
import soundfile as sf
import os

model = WhisperModel("base.en", compute_type="int8")

def record_audio(duration=8, fs=16000):
    print("🎙️ Speak now...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    return np.squeeze(audio)

def listen_to_user():
    audio = record_audio()
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        sf.write(f.name, audio, 16000)
        segments, _ = model.transcribe(f.name)
    os.remove(f.name)

    full_text = ""
    for segment in segments:
        print("🧾 Segment:", segment.text)
        full_text += segment.text.strip() + " "

    return full_text.strip()
