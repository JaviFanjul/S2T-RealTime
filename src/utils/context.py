import re
import logging
#Archivo que contiene todas las funciones relacionadas con el procesado de contexto
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def load_previous_transcriptions(log_file,tokenizer):
#Funcion que va acumulando todo el contexto
    try:
        #Lee el archivo log para obtener las transcripciones anteriores
        with open(log_file, "r", encoding="utf-8") as f:
            log_content =  f.read().strip()

            #Llama a funcion clean_transcription para limpiar los logs y solo quedarse con el texto.
            return clean_transcription(log_content,tokenizer)
        
    except FileNotFoundError:
        logging.warning("No se encontró el archivo de logs. Empezando sin contexto.")
        # Si el archivo no existe, empezamos sin contexto
        return ""  
    
def clean_transcription(log_content,tokenizer):
    #Funcion que limpia los logs y devuelve solo el texto, ademas se encarga de controlar el tamaño del contexto
    #para que no exceda el tamaño maximo permitido por el modelo.
    try:
        #Divide el log en lineas y se define variable para almacenar las lineas limpias
        lines = log_content.split("\n")  
        cleaned_lines = []

        #Obtiene el tamaño maximo permitido por el modelo
        max_tokens = tokenizer.model_max_length

        for line in lines:
            # Bucle donde se eliminan los prefijos de los logs y se almacena solo el texto
            clean_text = re.sub(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+ - INFO - \[\d+\.\d+s -> \d+\.\d+s\] ", "", line)
            if clean_text.strip():  # Evitar líneas vacías
                cleaned_lines.append(clean_text)

        #Se obtiene el contexto limpio y se tokeniza para obtener el tamaño en tokens
        context =  " ".join(cleaned_lines)  
        tokens = tokenizer.encode(context)
        
        #Se controla que el tamaño del contexto no exceda el tamaño maximo permitido por el modelo
        if(len(tokens) > max_tokens):

            #Si el tamaño es superior al maximo permitido, se recorta el contexto
            tokens_recortados = tokens[-max_tokens:]
            
            #Se elimina etiqueta de fin de texto y se devuelve el contexto recortado
            context = tokenizer.decode(tokens_recortados).replace("<|endoftext|>", "")
            return context
        else:

            #Si el tamaño es inferior al maximo permitido, se devuelve el contexto sin cambios
            return context
    except Exception as e:
        logging.warning(f"Error al limpiar la transcripcion para usar como contexto: {e}, Se procede a transcribir sin contexto.")
        return ""



