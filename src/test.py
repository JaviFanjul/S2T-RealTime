
import sys
from utils.split_audio import split_audio
from utils.transcribe_audio import transcribe_audio

audio_path = sys.argv[1]
output_folder = "../audiochunks_volume"

split_audio(audio_path , output_folder)
transcribe_audio(output_folder)