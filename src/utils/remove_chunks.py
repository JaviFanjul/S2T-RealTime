import os
import shutil

def borrar_contenido_excepto_gitkeep(output_folder):
    # Itera sobre todos los archivos y carpetas dentro del directorio
    for root, dirs, files in os.walk(output_folder, topdown=False):
        for name in files:
            # Verifica si el archivo no es 'gitkeep'
            if name != '.gitkeep':
                os.remove(os.path.join(root, name))  # Borra el archivo
        for name in dirs:
            # Verifica si la carpeta no es '.gitkeep'
            if name != '.gitkeep':
                shutil.rmtree(os.path.join(root, name), ignore_errors=True)  # Borra la carpeta

