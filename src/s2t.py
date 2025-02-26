from utils.split_audio import split_audio
from utils.transcribe_audio import transcribe_audio
from utils.config import audiopath , chunkpath , chunk_length_ms
#Script principal desde donde se incia la divison y la transcripion de los chunks de audio.
split_audio(audiopath , chunkpath , chunk_length_ms)
transcribe_audio(chunkpath)