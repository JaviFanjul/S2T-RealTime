import sys
#Archivo donde se definiran parametros de configuracion. 
#Contiene ruta del audio a transcribir, se pasa como argumento al crear el docker.
audiopath = sys.argv[1] 

 #Contiene la ruta del volumen dentro del docker donde se guardaran los chunks de audio.
chunkpath = "../audiochunks_volume"

#Contiene la ruta del volumen dentro del docker donde se encuentra el archvio donde se registran todos los logs de transcripcion
logpath  ="../audiotranscription_volume/audio_transcription.log"

#Indica cuanta duracion en ms tendra cada chunk de audio
chunk_length_ms = 10000 

#Indica el modelo de faster-whisper a utilizar
whisper_model = "medium"

threshold = 0.9
