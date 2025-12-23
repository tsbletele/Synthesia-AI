import librosa
import numpy as np
from scipy.signal import medfilt

audio_path = "ai/audio/test_piano.mp3"
y, sr = librosa.load(audio_path)

f0, voiced_flag, voiced_prob = librosa.pyin(
    y,
    fmin=librosa.note_to_hz('C2'),
    fmax=librosa.note_to_hz('C6'),
)

times = librosa.times_like(f0, sr=sr)

# Confidence filtering (remove silence & low-confidence guesses)
valid = (voiced_flag) & (voiced_prob > 0.8)
f0_clean = np.where(valid, f0, np.nan)

# Smooth pitch (reduced smoothing to preserve short notes like B)
f0_smooth = medfilt(f0_clean, kernel_size=3)

notes = []
current_note = None
start_time = None

MIN_DURATION = 0.08  # seconds

for time, pitch in zip(times, f0_smooth):

    if not np.isfinite(pitch) or pitch <= 0:
        continue

    midi = int(round(librosa.hz_to_midi(pitch)))

    # Piano range guard (A0 = 21, C8 = 108)
    if midi < 21 or midi > 108:
        continue

    note = librosa.midi_to_note(midi)

    if note != current_note:
        if current_note is not None:
            duration = time - start_time
            if duration >= MIN_DURATION:
                notes.append({
                    "note": current_note,
                    "start": round(start_time, 2),
                    "end": round(time, 2)
                })

        current_note = note
        start_time = time

# Close last note
if current_note is not None:
    duration = times[-1] - start_time
    if duration >= MIN_DURATION:
        notes.append({
            "note": current_note,
            "start": round(start_time, 2),
            "end": round(times[-1], 2)
        })

for n in notes:
    print(n)
