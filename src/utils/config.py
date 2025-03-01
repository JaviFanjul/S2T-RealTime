import sys
#Archivo donde se definiran parametros de configuracion. 
#Contiene ruta del audio a transcribir, se pasa como argumento al crear el docker.
audiopath = sys.argv[1] 
 #Contiene la ruta del volumen dentro del docker donde se guardaran los chunks de audio.
chunkpath = "../audiochunks_volume"
#Contiene la ruta del volumen dentro del docker donde se encuentra el archvio donde se registran todos los logs de transcripcion
logpath  ="../audiotranscription_volume/audio_transcription.log"
#Indica cuanta duracion en ms tendra cada chunk de audio
chunk_length_ms = 5000  
#Indica el modelo de faster-whisper a utilizar
whisper_model = "medium"
#Opciones para el filtrado del audio
noise_duration = 0.5  # Duración del audio de ruido en segundos
cutoff_freq = 300   # Frecuencia de corte del filtro pasaaltos
pop_decrease = 0.8  # Factor de reducción de ruido
filter_type = "high"  # Tipo de filtro a aplicar
order = 5  # Orden del filtro
#Opciones para la deteccion de silencios en el divisor de audio
min_silence_len=750 # Duración mínima de un silencio en ms
silence_thresh=-40 # Umbral de silencio en dB