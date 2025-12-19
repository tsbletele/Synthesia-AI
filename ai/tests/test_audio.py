import librosa
import numpy as np

# Load audio file
audio_path = "ai/audio/test_piano.mp3"
y, sr = librosa.load(audio_path)

print(f"Sample rate: {sr}")
print(f"Audio length: {len(y) / sr:.2f} seconds")

# Pitch detection using librosa's YIN algorithm
pitches = librosa.yin(
    y,
    fmin=librosa.note_to_hz('A0'),
    fmax=librosa.note_to_hz('C8')
)

times = librosa.times_like(pitches, sr=sr)

# Convert frequencies to note names
for time, pitch in zip(times, pitches):
    if pitch > 0:
        note = librosa.hz_to_note(pitch)
        print(f"{time:.2f}s → {note}")
