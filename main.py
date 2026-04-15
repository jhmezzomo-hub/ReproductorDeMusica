import ttkbootstrap as tb
from crear_venntana import crear_ventana
from paneles import *
from btotones_musica import *
from botones_buscador import *
from cargar_imagen import imagen

def main():
    root = crear_ventana()
    busca = panel_busqueda(root)
    vista = panel_musica(root)

    inciar = play(vista)
    pausa = pause(vista)
    frenar = stop(vista)
    image = imagen(vista, imagen="album_predeterminado.png")

    barra_busca = barra_busqueda(busca)

    root.mainloop()

if __name__ == "__main__":
    main()