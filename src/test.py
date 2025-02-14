import threading
import sys
audio_path = sys.argv[1]
output_folder = "../audiochunks_volume"
from utils.split_audio import split_audio
from utils.transcribe import transcribe_audio

# Hilo 1: División de audio
split_thread = threading.Thread(target=split_audio, args=(audio_path))

# Hilo 2: Monitorización y transcripción
monitor_thread = threading.Thread(target=transcribe_audio, args=(audio_path,output_folder,))

split_thread.start()
monitor_thread.start()

split_thread.join()
monitor_thread.join()
