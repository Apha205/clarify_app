import pyttsx3
import tempfile
import os
import io

def generate_speech(text: str) -> dict:
    engine = pyttsx3.init()
    timings = []

    def on_word(name, location, length):
        timings.append({"start": location, "end": location + length})

    engine.connect('started-word', on_word)

    # Generate audio to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as f:
        temp_path = f.name

    engine.save_to_file(text, temp_path)
    engine.runAndWait()

    # Read audio data
    with open(temp_path, 'rb') as f:
        audio_data = f.read()

    os.unlink(temp_path)

    return {
        "audio": audio_data,
        "timings": timings if timings else None
    }