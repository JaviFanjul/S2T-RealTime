
import os
import logging
from utils.context import load_previous_transcriptions
from utils.config import logpath
from utils.model import load_model
from utils.config import threshold


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
        
        # Transcribir cada fragmento
        for chunk in chunks:
                chunk_path = os.path.join(output_folder, chunk)
                #Se carga contexto apoyandose en transcripciones de chunks anteriores
                context = load_previous_transcriptions(logpath, tokenizer)
                segments, _ = model.transcribe(chunk_path ,initial_prompt = context, vad_filter = True, vad_parameters={"threshold": threshold} ,**options)
                for segment in segments:
                    transcription_logger.info(segment.text)
    
    except FileNotFoundError as e:
        logging.error(f"Error: {e}")
    except ValueError as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.error(f"Error inesperado: {e}")