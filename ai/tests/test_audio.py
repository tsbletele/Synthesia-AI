from preprocessing.audio_loader import load_audio

audio_data = load_audio("audio/test_piano.wav")

print("Sample Rate:", audio_data["sample_rate"])
print("Duration (seconds):", audio_data["duration"])
print("Waveform shape:", audio_data["waveform"].shape)
