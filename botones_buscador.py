import ttkbootstrap as tb
from pathlib import Path
from btotones_musica import cargar_vista
from abrir_directorio import nombres_canciones_guardadas, cargar_directorio, canciones_guardadas

labels_resultados = []

def buscar_similitudes(buscador, panel):
    for label in labels_resultados:
        label.destroy()
    labels_resultados.clear()

    entrada = buscador.get().lower()
    if entrada == "":
        return

    try:
        for i in canciones_guardadas:
            for e in nombres_canciones_guardadas:
                if entrada in i:
                    print(f"Encontre una coincidencia: {i}")
                    opcion = tb.Label(panel, text=e, bootstyle="warning", font=("Roboto", 13, "bold"), cursor="hand2")
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

def vista_previa(panel):
    if nombres_canciones_guardadas:
        for i, canciones in enumerate(nombres_canciones_guardadas):
            if i >= 10:
                opcion = tb.Label(panel, text=canciones, bootstyle="warning", font=("Roboto", 13, "bold"), cursor="hand2")
                opcion.pack(side="top", fill="x", padx=5, pady=5)
            else:
                break
    else:
        mostrar = tb.Label(panel, text="No hay ninguna cancion cargada en este momento", bootstyle="danger", font=("Roboto", 25, "bold", "underline"), justify="center")
        mostrar.pack(side="top", fill="x", padx=30, pady=(200,20))

        abrir = tb.Button(panel, text="Abrir directorio", style="primary.TButton", command=lambda: cargar_directorio())
        abrir.pack(side="top", pady=5, padx=5 , ipadx=15, ipady=15)