import os
import shutil

def borrar_contenido_excepto_gitkeep(output_folder):
    # Funcion que borra los chunks de transcripciones anteriores, excepto el archivo '.gitkeep'
    for name in os.listdir(output_folder):
        #Bucle que recorre los archivos en la carpeta de chunks y los borra
        file_path = os.path.join(output_folder, name)

        #Comprueba si el archivo es un archivo y si no es el archivo '.gitkeep' lo borra
        if os.path.isfile(file_path) and name != '.gitkeep':  
            os.remove(file_path)