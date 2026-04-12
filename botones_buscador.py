import ttkbootstrap as tb

def barra_busqueda(panel):
    buscador = tb.Entry(panel, bootstyle="info", textvariable="text")
    buscador.pack(side="left", fill="x", expand=True, padx=5, pady=5)
    return buscador