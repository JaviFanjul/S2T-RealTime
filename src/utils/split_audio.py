import logging
import shutil
import os
from pydub import AudioSegment

#Informacion de configuracion
from utils.config import chunk_length_ms
from utils.config import overlap
from utils.remove_chunks import borrar_contenido_excepto_gitkeep

# Configuración básica del logging (solo muestro por consola)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def split_audio(audiopath, output_folder):
    #Funcion que divide un archivo de audio en fragmentos de duracion especificada y los exporta en formato wav.
    logging.info("Dividiendo audio en fragmentos ...")

    #Borra contenido del volumen de chunks en caso de que haya restos de otra conversion.
    borrar_contenido_excepto_gitkeep(output_folder)

    #Cargo audio en formato wav
    audio = AudioSegment.from_file(audiopath)
   #Bucle que divide el audio en fragmentos de duracion especificada y los exporta en formato wav.
    try:
        for i, start in enumerate(range(0, len(audio), chunk_length_ms)):
            end = min(start + chunk_length_ms, len(audio))
            chunk = audio[start:end]
            chunk.export(os.path.join(output_folder, f"chunk_{i}.wav"), format="wav")
            logging.info(f"Fragmento {i} exportado exitosamente.")

        logging.info("Audio dividido en fragmentos exitosamente.")
    except Exception as e:
        # Captura cualquier error durante la división o exportación de los fragmentos
        logging.error(f"Error al dividir el audio: {e}")