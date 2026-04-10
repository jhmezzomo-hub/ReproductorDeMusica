import ttkbootstrap as tb
from paneles import *

def crear_ventana():
    root = tb.Window(themename="vapor")
    root.title("SpotiMezzo")
    x = root.winfo_screenwidth()
    y = root.winfo_screenheight()
    root.geometry(f"{x-100}x{y-125}+0+0")
    root.resizable(False, False)

    buscea = panel_busqueda(root)
    vista = panel_musica(root)

    root.mainloop()
    return root

crear_ventana()