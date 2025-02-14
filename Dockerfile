# Usamos una imagen base de Python 3.10
FROM python:3.10-slim-buster

# Instalamos dependencias necesarias
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copiamos requirements en contenedor e instalamos las librerías necesarias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar la carpeta local audiofiles en el contenedor /audiofiles. Esta carpeta contiene los audios a transcribir
#COPY audiofiles /audiofiles

# Copiar la carpeta local src en el contenedor /src
COPY src /src

# Establecer el directorio de trabajo
WORKDIR /src

# Comando por defecto para ejecutar el script Python
CMD ["python", "transcribe.py"]
