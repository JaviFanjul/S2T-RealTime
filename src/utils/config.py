import sys
audiopath = sys.argv[1]
chunkpath = "../audiochunks_volume"
chunk_length_ms = 5000
logpath  ="../audiologs_volume/audio_transcription.log"
prompt_inicial = "Esta es una conversacion entre un teleoperador y un cliente de una compañia de servicios telefonicos. Ten en cuenta que podran haber palabras o tecnicismos en ingles, pero la conversacion es en español"
max_tokens = 25000