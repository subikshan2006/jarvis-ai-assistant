import pvporcupine
import pyaudio
import struct

def wait_for_wake_word():
    porcupine = pvporcupine.create(keywords=["jarvis"])

    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("🎧 Jarvis is listening... Say 'Hey Jarvis'")

    try:
        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm_unpacked = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm_unpacked)
            if keyword_index >= 0:
                print("🎙️ Wake word detected!")
                break

    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()
