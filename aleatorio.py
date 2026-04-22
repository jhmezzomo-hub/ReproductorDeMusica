from abrir_directorio import canciones_guardadas
from random import choice

def reproducir_aleatorio(cancion_actual):
    i = choice(canciones_guardadas)
    if i != cancion_actual:
        sig_cancion = i
    return sig_cancion