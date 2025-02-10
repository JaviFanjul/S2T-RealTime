# Usamos una imagen base de Python 3.10
FROM python:3.10-slim-buster

# Instalamos dependencias necesarias
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Instalamos las librerías necesarias
RUN pip install faster-whisper

# Copiar la carpeta de audio desde la carpeta local /app/audio al contenedor /app/audio
COPY app/audio /app/audio

# Copiar el script Python desde la carpeta local /app al contenedor /app
COPY app/transcribe.py /app/transcribe.py

# Establecer el directorio de trabajo
WORKDIR /app

# Comando por defecto para ejecutar el script Python
CMD ["python", "transcribe.py"]
