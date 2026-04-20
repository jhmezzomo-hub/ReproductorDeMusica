import os
import re
from tkinter import filedialog

canciones_guardadas = []
nombres_canciones_guardadas = []

def cargar_directorio():
    carpeta = filedialog.askdirectory(title="Seleccionar carpeta de música")

    if carpeta:
        canciones_guardadas.clear()
        nombres_canciones_guardadas.clear()
        for ruta_actual, subcarpetas, archivos in os.walk(carpeta):
            for archivo in archivos:
                if archivo.lower().endswith(".mp3"):
                    ruta_completa = os.path.join(ruta_actual, archivo)
                    canciones_guardadas.append(ruta_completa)
                    nombre = os.path.splitext(archivo)[0]
                    
                    # Limpieza: Quitar números al inicio, contenido entre () o [] y espacios extra
                    nombre = re.sub(r'^\d+[\s.\-_]*', '', nombre)
                    nombre = re.sub(r'\[.*?\]|\(.*?\)', '', nombre).strip()
                    
                    nombres_canciones_guardadas.append(nombre)
        return True
    return False