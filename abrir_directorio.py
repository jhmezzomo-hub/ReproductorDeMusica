import os
from tkinter import filedialog

canciones_guardadas = []
nombres_canciones_guardadas = []

def cargar_directorio():
    carpeta = filedialog.askdirectory(title="Seleccionar carpeta de música")

    if carpeta:
        archivos_carpeta = os.listdir(carpeta)

        for archivo in archivos_carpeta:
            if archivo.endswith(".mp3"):
                ruta_completa = os.path.join(carpeta, archivo)
                canciones_guardadas.append(ruta_completa)

def cargar_nombres():
    for ruta in canciones_guardadas:
        nombre_archivo = os.path.basename(ruta)
        nombre = os.path.splitext(nombre_archivo)[0]
        nombres_canciones_guardadas.append(nombre)