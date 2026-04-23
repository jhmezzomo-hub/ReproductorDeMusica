from abrir_directorio import canciones_guardadas
from random import choice

def reproducir_aleatorio(cancion_actual):
    if len(canciones_guardadas) <= 1:
        return cancion_actual

    seleccion = choice(canciones_guardadas)
    # Evitamos que repita la misma canción si hay más opciones
    while seleccion == cancion_actual:
        seleccion = choice(canciones_guardadas)
    return seleccion