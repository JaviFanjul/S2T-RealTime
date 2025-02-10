# Nombre de la imagen
IMAGE_NAME=faster-whisper

# Construir la imagen
build:
	docker build -t $(IMAGE_NAME) .

# Correr un contenedor interactivo
run:
	docker run --rm -it $(IMAGE_NAME)

# Limpiar imágenes y contenedores
clean:
	docker system prune -f
