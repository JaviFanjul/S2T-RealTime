from transformers import WhisperTokenizer
from faster_whisper import WhisperModel
from utils.config import whisper_model
def load_model():
        model = WhisperModel(whisper_model , device = "cpu", compute_type = "float32")  # Cambiar a "cuda" si usas GPU
        options = {
            "task": "transcribe",
            "language": "es"  
        }
        tokenizer = WhisperTokenizer.from_pretrained(f"openai/whisper-{whisper_model}")
        return model,options,tokenizer