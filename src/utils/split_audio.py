import logging
from pydub import AudioSegment
import shutil


# Configuración básica del logging (solo muestro por consola)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def split_audio(input_path, output_folder, chunk_length_ms):
    #Funcion que divide un archivo de audio en fragmentos de duracion especificada y los exporta en formato wav.

    #Borra contenido del volumen de chunks en caso de que haya restos de otra conversion.
    shutil.rmtree(output_folder, ignore_errors=True)

    #Se carga el archivo de audio y se guarda en variable audio
    try:
        # Intentar cargar el archivo de audio
        logging.info(f"Iniciando la división del archivo de audio: {input_path}")
        audio = AudioSegment.from_file(input_path)
    except Exception as e:
        # Captura cualquier error al cargar el archivo de audio
        logging.error(f"Error al cargar el archivo de audio {input_path}: {e}")
        return

   #Bucle que divide el audio en fragmentos de duracion especificada y los exporta en formato wav.
    try:
        for i, start in enumerate(range(0, len(audio), chunk_length_ms)):
            chunk = audio[start:start + chunk_length_ms]
            chunk.export(f"{output_folder}/chunk_{i}.wav", format="wav")
            logging.info(f"Fragmento {i} exportado exitosamente.")
        logging.info("Audio dividido en fragmentos exitosamente.")
    except Exception as e:
        # Captura cualquier error durante la división o exportación de los fragmentos
        logging.error(f"Error al dividir el audio: {e}")