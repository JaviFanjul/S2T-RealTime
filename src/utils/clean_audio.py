import librosa
import noisereduce as nr
import numpy as np
from scipy.signal import butter, lfilter
from pydub import AudioSegment
import io
import soundfile as sf

from utils.config import noise_duration, cutoff_freq

def highpass_filter(data, cutoff, fs, order=5):
    #Aplica filto paso alto para eliminar frecuencias no deseadas
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return lfilter(b, a, data)

def limpiar_audio(audio_path):
    #Limpia el audio de ruido y aplica un filtro pasaaltos.
    # Cargar el audio
    y, sr = librosa.load(audio_path, sr=None)

    # Reducción de ruido
    noise_sample = y[:int(sr * noise_duration)]  # Tomar los primeros segundos como referencia de ruido
    y_denoised = nr.reduce_noise(y=y, sr=sr, y_noise=noise_sample, prop_decrease=0.8)

    #Aplicar filtro pasaaltos
    y_filtered = highpass_filter(y_denoised, cutoff=cutoff_freq, fs=sr)

    #Convertir a formato de pydub para normalización
    buffer = io.BytesIO()
    sf.write(buffer, y_filtered, sr, format="wav")
    buffer.seek(0)

    audio = AudioSegment.from_file(buffer, format="wav")

    #Normalizar volumen
    normalized_audio = audio.apply_gain(-audio.dBFS)

    #Guardar el audio final en un buffer
    normalized_buffer = io.BytesIO()
    normalized_audio.export(normalized_buffer, format="wav")
    normalized_buffer.seek(0)

    return normalized_buffer

