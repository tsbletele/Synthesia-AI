import librosa
import numpy as np

def load_audio(path):
    """
    Load an audio file and return waveform + metadata
    """
    audio, sample_rate = librosa.load(path, sr=None, mono=True)

    return {
        "waveform": audio,
        "sample_rate": sample_rate,
        "duration": len(audio) / sample_rate
    }
