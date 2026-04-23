from pathlib import Path
from crear_venntana import crear_ventana
from paneles import *
from btotones_musica import *
from botones_buscador import *
from cargar_imagen import imagen
from abrir_directorio import cargar_playlist_original
from obtener_playlists import abrir_playlist
import json

def main():
    root = crear_ventana()
    busca = panel_busqueda(root)
    vista = panel_musica(root)
    playlists = panel_playlist(root)

    platlista = cargar_playlist_original()
    abrir_playlist()

    inciar = play(vista)
    pausa = pause(vista)
    frenar = stop(vista)
    next = siguiente(vista)
    previa = anterior(vista)
    primero = cargar_vista(vista)
    random = aleatorio(vista)
    looper = loop(vista)
    lista = opcion_playlist(vista, busca)
    vol = control_volumen(vista)

    barra_busca = barra_busqueda(busca, vista)
    previa = vista_previa(busca, vista)

    estado = obtener_estado(vista)

    agregar = agregar_cancion(vista, busca)
    crear = crear_playlist(vista, busca, playlists)

    root.mainloop()

if __name__ == "__main__":
    main()