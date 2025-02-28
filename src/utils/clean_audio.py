import librosa
import noisereduce as nr
import numpy as np
from scipy.signal import butter, lfilter
from pydub import AudioSegment
import io
import soundfile as sf
import logging

from utils.config import noise_duration, cutoff_freq , pop_decrease ,filter_type, order

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def highpass_filter(data, cutoff, fs):
    try:
        # Aplica filtro paso alto para eliminar frecuencias no deseadas
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype=filter_type, analog=False)
        return lfilter(b, a, data)
    except Exception as e:
        logging.error(f"Error en highpass_filter: {e}")
        raise

def limpiar_audio(audio_path):
    try:
        logging.info("Limpiando audio ...")
        # Limpia el audio de ruido y aplica un filtro pasaaltos.
        # Cargar el audio
        y, sr = librosa.load(audio_path, sr=None)

        # Reducción de ruido
        noise_sample = y[:int(sr * noise_duration)]  # Tomar los primeros segundos como referencia de ruido
        y_denoised = nr.reduce_noise(y=y, sr=sr, y_noise=noise_sample, prop_decrease=pop_decrease)

        # Aplicar filtro pasaaltos
        y_filtered = highpass_filter(y_denoised, cutoff=cutoff_freq, fs=sr)

        # Convertir a formato de pydub para normalización
        buffer = io.BytesIO()
        sf.write(buffer, y_filtered, sr, format="wav")
        buffer.seek(0)

        audio = AudioSegment.from_file(buffer, format="wav")

        # Normalizar volumen
        normalized_audio = audio.apply_gain(-audio.dBFS)

        # Guardar el audio final en un buffer
        normalized_buffer = io.BytesIO()
        normalized_audio.export(normalized_buffer, format="wav")
        normalized_buffer.seek(0)

        return normalized_buffer
    except Exception as e:
        logging.error(f"Error en limpiar_audio: {e}")
        raise