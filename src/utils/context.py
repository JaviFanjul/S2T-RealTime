import re


def load_previous_transcriptions(log_file,tokenizer):
    
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            log_content =  f.read().strip()
            return clean_transcription(log_content,tokenizer)
    except FileNotFoundError:
        return ""  # Si el archivo no existe, empezamos sin contexto
    
def clean_transcription(log_content,tokenizer):
    lines = log_content.split("\n")  # Separar líneas
    cleaned_lines = []
    max_tokens = tokenizer.model_max_length

    for line in lines:
        # Expresión regular para eliminar timestamps y datos del log
        clean_text = re.sub(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+ - INFO - \[\d+\.\d+s -> \d+\.\d+s\] ", "", line)
        if clean_text.strip():  # Evitar líneas vacías
            cleaned_lines.append(clean_text)

    context =  " ".join(cleaned_lines)  # Unir todo en un solo string limpio
    tokens = tokenizer.encode(context)
    
    if(len(tokens) > max_tokens):
        tokens_recortados = tokens[-max_tokens:]
        context = tokenizer.decode(tokens_recortados).replace("<|endoftext|>", "")
        return context
    else:
        return context
    



