import os
from tkinter import filedialog

canciones_guardadas = []
nombres_canciones_guardadas = []

def cargar_directorio():
    carpeta = filedialog.askdirectory(title="Seleccionar carpeta de música")

    if carpeta:
        canciones_guardadas.clear()
        nombres_canciones_guardadas.clear()
        archivos_carpeta = os.listdir(carpeta)

        for archivo in archivos_carpeta:
            if archivo.endswith(".mp3"):
                ruta_completa = os.path.join(carpeta, archivo)
                canciones_guardadas.append(ruta_completa)
                nombre = os.path.splitext(archivo)[0]
                nombres_canciones_guardadas.append(nombre)
        return True
    return False