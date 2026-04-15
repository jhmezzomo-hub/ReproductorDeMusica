import ttkbootstrap as tb
from pathlib import Path
from btotones_musica import cargar_vista

labels_resultados = []

def buscar_similitudes(buscador, panel):
    for label in labels_resultados:
        label.destroy()
    labels_resultados.clear()

    entrada = buscador.get().lower()
    if entrada == "":
        return

    try:
        with open("canciones_disponibles.txt", "r") as e:
            for i in e:
                if entrada in i:
                    print(f"Encontre una coincidencia: {i}")
                    opcion = tb.Label(panel, text=i, bootstyle="warning", font=("Roboto", 13, "bold"), cursor="hand2")
                    opcion.pack(side="top", fill="x", padx=5, pady=5)

                    opcion.bind("<Button-1>", lambda nombre=i: cargar_vista(nombre))

                    labels_resultados.append(opcion)

    except Exception as error:
        print(error)

def barra_busqueda(panel):
    buscador = tb.Entry(panel, bootstyle="info", textvariable="text")
    buscador.pack(side="top", fill="x", padx=5, pady=5)

    buscador.bind("<KeyRelease>", lambda e: buscar_similitudes(buscador, panel))
    return buscador