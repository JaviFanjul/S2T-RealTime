import re
import tiktoken
from utils.config import max_tokens
def load_previous_transcriptions(log_file , prompt_inicial):
    
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            log_content =  f.read().strip()
            return trim_context(f"{prompt_inicial} {clean_transcription(log_content)}", max_tokens)
    except FileNotFoundError:
        return ""  # Si el archivo no existe, empezamos sin contexto
    
def clean_transcription(log_content):
    lines = log_content.split("\n")  # Separar líneas
    cleaned_lines = []
    
    for line in lines:
        # Expresión regular para eliminar timestamps y datos del log
        clean_text = re.sub(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+ - INFO - \[\d+\.\d+s -> \d+\.\d+s\] ", "", line)
        if clean_text.strip():  # Evitar líneas vacías
            cleaned_lines.append(clean_text)

    return " ".join(cleaned_lines)  # Unir todo en un solo string limpio


def count_tokens(text):
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    return len(tokens)

def trim_context(context, max_tokens):
    """Recorta el contexto si excede el límite de tokens"""
    num_tokens = count_tokens(context)
    
    # Si el número de tokens excede el máximo permitido, recortar el contexto
    if num_tokens > max_tokens:
        enc = tiktoken.get_encoding("cl100k_base")
        tokens = enc.encode(context)
        
        # Mantener solo los últimos tokens hasta el límite permitido
        tokens = tokens[-max_tokens:]  # Mantener solo los últimos `max_tokens` tokens
        
        # Decodificar nuevamente a texto
        trimmed_context = enc.decode(tokens)
        return trimmed_context
    
    return context  # Si el contexto no excede el límite, regresarlo tal cual
