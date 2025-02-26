from transformers import WhisperTokenizer
from faster_whisper import WhisperModel
from utils.config import whisper_model

def load_model():
    #Funcion que carga el modelo de faster-whisper y crea el tokenizador asociado. 
    #Dentro del modelo, se especifican opciones como el idioma y la tarea a realizar.
        model = WhisperModel(whisper_model , device = "cpu", compute_type = "float32")  # Cambiar a "cuda" si usas GPU
        options = {
            "task": "transcribe",
            "language": "es"  
        }

        #Se crea el tokenizador asociado al modelo
        tokenizer = WhisperTokenizer.from_pretrained(f"openai/whisper-{whisper_model}")

        #Se devuelven el modelo, las opciones y el tokenizador
        return model,options,tokenizer