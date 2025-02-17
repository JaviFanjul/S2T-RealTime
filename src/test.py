import threading
import sys
audio_path = sys.argv[1]
output_folder = "../audiochunks_volume"
from utils.split_audio import split_audio
from utils.transcribe_audio import transcribe_audio

split_audio(audio_path , output_folder)
transcribe_audio(output_folder)