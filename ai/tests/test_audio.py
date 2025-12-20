import librosa
import numpy as np

audio_path = "ai/audio/test_piano.mp3"
y, sr = librosa.load(audio_path)

pitches = librosa.yin(
    y,
    fmin=librosa.note_to_hz('A0'),
    fmax=librosa.note_to_hz('C8')
)

times = librosa.times_like(pitches, sr=sr)

notes = []
current_note = None
start_time = None

for time, pitch in zip(times, pitches):
    if pitch <= 0:
        continue

    note = librosa.hz_to_note(pitch)

    if note != current_note:
        if current_note is not None:
            notes.append({
                "note": current_note,
                "start": round(start_time, 2),
                "end": round(time, 2)
            })

        current_note = note
        start_time = time

# Close last note
if current_note is not None:
    notes.append({
        "note": current_note,
        "start": round(start_time, 2),
        "end": round(times[-1], 2)
    })

for n in notes:
    print(n)
