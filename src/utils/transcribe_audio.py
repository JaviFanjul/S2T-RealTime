from faster_whisper import WhisperModel
import os
import logging


# Configuración del registro (logging)
# Logger que se usare para la transcripcuion de los fragmentos
transcription_logger = logging.getLogger('transcription')
transcription_logger.setLevel(logging.INFO)

# Desactivar la propagación a los handlers globales (Evito que se muestre dos veces por consola el loggind de la transcripcion)
transcription_logger.propagate = False


# Handler para escribir los logs en un archivo
transcription_file_handler = logging.FileHandler("../audiologs_volume/audio_transcription.log", mode='a')
transcription_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Handler para imprimir los logs en consola
transcription_console_handler = logging.StreamHandler()
transcription_console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Añadir ambos handlers al logger
transcription_logger.addHandler(transcription_file_handler)
transcription_logger.addHandler(transcription_console_handler)


def transcribe_audio(output_folder):
    try:
        
        # Cargar el modelo
        model = WhisperModel("small", device = "cpu", compute_type = "float32")  # Cambiar a "cuda" si usas GPU
        options = {"task": "transcribe"}
        #A pesar de que en la maquina local se muestren por orden, en el volumen dentro del docker pueden
        #desordenarse. Con esto me aseguro de que los chunks esten ordenados de cara a la transcripcion.  
        chunks = sorted([f for f in os.listdir(output_folder) if f.endswith('.wav')],
                key=lambda x: int(x.split('_')[1].split('.')[0]))


        # Transcribir cada fragmento
        for chunk_file in chunks:
            if chunk_file.endswith(".wav"):
                chunk_path = os.path.join(output_folder, chunk_file)
                logging.info(f"Transcribiendo {chunk_path}...")
                segments, _ = model.transcribe(chunk_path , **options)
                
                # Registrar la transcripción en el archivo de log y consola
                for segment in segments:
                    transcription_logger.info(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
    
    except FileNotFoundError as e:
        logging.error(f"Error: {e}")
    except ValueError as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.error(f"Error inesperado: {e}")

