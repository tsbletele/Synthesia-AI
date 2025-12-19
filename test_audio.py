import librosa

y, sr = librosa.load(librosa.ex('trumpet'))
print("Loaded audio with sample rate:", sr)
