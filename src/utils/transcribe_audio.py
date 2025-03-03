
import os
import logging
from utils.context import load_previous_transcriptions
from utils.config import logpath
from utils.model import load_model
from utils.solapamiento_audio import eliminar_solapamiento
from utils.voice_detection import is_voice


# Configuración del registro (logging)
# Logger que se usare para la transcripcuion de los fragmentos
transcription_logger = logging.getLogger('transcription')
transcription_logger.setLevel(logging.INFO)

# Desactivar la propagación a los handlers globales (Evito que se muestre dos veces por consola el loggind de la transcripcion)
transcription_logger.propagate = False


# Handler para escribir los logs en un archivo
transcription_file_handler = logging.FileHandler(logpath, mode='a')
transcription_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Handler para imprimir los logs en consola
transcription_console_handler = logging.StreamHandler()
transcription_console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Añadir ambos handlers al logger
transcription_logger.addHandler(transcription_file_handler)
transcription_logger.addHandler(transcription_console_handler)


def transcribe_audio(output_folder):
    try:
        #Funcion que transcribe chunks de audio y guarda las transcripciones en un archivo de log.

        #Borrar restos del log de transcripcion anterior
        open(logpath, "w", encoding="utf-8").close()  # Borra el contenido del log

        # Cargar el modelo, opciones y tokenizador
        model,options,tokenizer = load_model()

        #Ordenada los chunks de audio para procesarlos en orden
        chunks = sorted([f for f in os.listdir(output_folder) if f.endswith('.wav')],
                key=lambda x: int(x.split('_')[1].split('.')[0]))

        prev_text = ""
        
        # Transcribir cada fragmento
        for chunk_file in chunks:
            if chunk_file.endswith(".wav"):
                chunk_path = os.path.join(output_folder, chunk_file)
                if(is_voice(chunk_path)):
                    #Se carga contexto apoyandose en transcripciones de chunks anteriores
                    context = load_previous_transcriptions(logpath, tokenizer)
                    logging.info(f"Transcribiendo {chunk_path}...")
                    segments, _ = model.transcribe(chunk_path ,initial_prompt = context,  **options)
                    text = " ".join(segment.text for segment in segments)
                    #Elimino transcripcion repetida debido a solapamiento
                    texto_sin_solapamiento = eliminar_solapamiento(prev_text,text)
                    prev_text = text
                    transcription_logger.info(texto_sin_solapamiento)
    
    except FileNotFoundError as e:
        logging.error(f"Error: {e}")
    except ValueError as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.error(f"Error inesperado: {e}")