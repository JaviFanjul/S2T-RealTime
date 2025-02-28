import logging
from pydub import AudioSegment
import shutil
from pydub.silence import split_on_silence

from utils.config import min_silence_len, silence_thresh


# Configuración básica del logging (solo muestro por consola)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def split_audio(buffer, output_folder):
    #Funcion que divide un archivo de audio en fragmentos de duracion especificada y los exporta en formato wav.
    logging.info("Dividiendo audio en fragmentos ...")
    #Borra contenido del volumen de chunks en caso de que haya restos de otra conversion.
    shutil.rmtree(output_folder, ignore_errors=True)
    #Cargo audio en formato wav
    audio = AudioSegment.from_file(buffer, format="wav")
    #Divido audio en chunks en funcion del silencio
    chunks = split_on_silence(
        audio,
        min_silence_len=min_silence_len,  # en milisegundos
        silence_thresh=silence_thresh  # en dB
    )
   #Bucle que divide el audio en fragmentos de duracion especificada y los exporta en formato wav.
    i=0
    try:
        for chunk in chunks:
            chunk.export(f"{output_folder}/chunk_{i}.wav", format="wav")
            logging.info(f"Fragmento {i} exportado exitosamente.")
            i+= 1
        logging.info("Audio dividido en fragmentos exitosamente.")
    except Exception as e:
        # Captura cualquier error durante la división o exportación de los fragmentos
        logging.error(f"Error al dividir el audio: {e}")