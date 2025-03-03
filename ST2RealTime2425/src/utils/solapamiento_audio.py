
from difflib import SequenceMatcher
from utils.config import umbral
def eliminar_solapamiento(texto_anterior, texto_actual):
    matcher = SequenceMatcher(None, texto_anterior, texto_actual)
    match = matcher.find_longest_match(0, len(texto_anterior), 0, len(texto_actual))
    
    if match.size > umbral:  # Ajusta el umbral según el caso
        texto_actual = texto_actual[match.b+match.size:]  # Elimina la parte repetida
    
    return texto_actual