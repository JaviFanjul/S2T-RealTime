from utils.split_audio import split_audio
from utils.transcribe_audio import transcribe_audio
from utils.config import audiopath, chunkpath

split_audio(audiopath , chunkpath)
transcribe_audio(chunkpath)