import ttkbootstrap as tb

def crear_ventana():
    root = tb.Window(themename="cyborg")
    root.title("SpotiMezzo")
    x = root.winfo_screenwidth()
    y = root.winfo_screenheight()
    root.geometry(f"{x-100}x{y-100}+0+0")
    root.resizable(False, False)
    return root