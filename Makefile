# Nombre de la imagen
IMAGE_NAME=realtimes2t


#Se usa por si se utiliza docker desde powershell. Es un transcriptor de rutas.
ifeq ($(OS), Linux)
    AUDIO_VOLUME := $(shell pwd)/audiofiles
    CHUNKS_VOLUME := $(shell pwd)/audiochunks
    LOGS_VOLUME := $(shell pwd)/audio_transcription
else
    AUDIO_VOLUME := $(shell pwd | sed 's|^/c|C:|' | sed 's|/|\\|g')/audiofiles
    CHUNKS_VOLUME := $(shell pwd | sed 's|^/c|C:|' | sed 's|/|\\|g')/audiochunks
    LOGS_VOLUME := $(shell pwd | sed 's|^/c|C:|' | sed 's|/|\\|g')/audio_transcription
endif



# Construir la imagen
build:
	docker build -t $(IMAGE_NAME) .

# Correr un contenedor interactivo
run:
	 docker run --rm -it -v $(AUDIO_VOLUME):/audiofiles_volume -v $(CHUNKS_VOLUME):/audiochunks_volume -v $(LOGS_VOLUME):/audiotranscription_volume  $(IMAGE_NAME) python s2t.py ../audiofiles_volume/llamada.mp3

#Puede usarse para pruebas permite acceder al contendio del docker con la consola bash
run-bash:
	docker run --rm -it -v $(AUDIO_VOLUME):/audiofiles_volume -v $(CHUNKS_VOLUME):/audiochunks_volume -v $(LOGS_VOLUME):/audiotranscription_volume  $(IMAGE_NAME) bash

# Limpiar imágenes y contenedore
clean:
	docker system prune -f

