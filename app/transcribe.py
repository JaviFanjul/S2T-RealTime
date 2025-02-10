from faster_whisper import WhisperModel

# Cargar el modelo (puedes cambiar "medium" por "small" o "large-v2")
model = WhisperModel("medium", device="cpu")  # Cambiar a "cuda" si usas GPU

# Archivo de audio de prueba (asegúrate de tener uno en el contenedor)
AUDIO_FILE = "/app/audio/audio.mp3"

print(f"Transcribiendo {AUDIO_FILE}...")
segments, _ = model.transcribe(AUDIO_FILE)

# Mostrar la transcripción
for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
