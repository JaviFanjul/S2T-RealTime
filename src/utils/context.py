import re


def load_previous_transcriptions(log_file , prompt_inicial):
    
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            log_content =  f.read().strip()
            return f"{prompt_inicial} {clean_transcription(log_content)}"
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



