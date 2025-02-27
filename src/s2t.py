from utils.split_audio import split_audio
from utils.transcribe_audio import transcribe_audio
from utils.config import audiopath , chunkpath , chunk_length_ms
from utils.clean_audio import limpiar_audio
#Script principal desde donde se incia la divison y la transcripion de los chunks de audio.
buffer =limpiar_audio(audiopath)
split_audio(buffer, chunkpath)
transcribe_audio(chunkpath)