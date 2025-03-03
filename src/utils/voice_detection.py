import librosa
import numpy as np

# Función para extraer características básicas de un archivo de audio
def extract_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)  # Cargar el audio
    zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(y))  # Tasa de cruce por cero
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))  # Centro espectral
    return zero_crossing_rate, spectral_centroid

# Función para clasificar el audio (voz o música)
def is_voice(audio_path):
    zero_crossing_rate, spectral_centroid = extract_features(audio_path)

    # Umbrales sencillos basados en la experiencia
    if zero_crossing_rate > 0.1 and spectral_centroid > 3000:
        return False  # Si es música, devolver False
    else:
        return True   # Si es voz, devolver True


