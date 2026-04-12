import ttkbootstrap as tb
from funciones import *
from cargar_imagen import cargar_imagen
from PIL import ImageTk

def play(panel):
    play_bt = tb.Button(panel, text="Play", style="success.TButton",command=reproducir)
    play_bt.grid(column=2, row=2, padx=10, pady=10, ipadx=5, ipady=5)
    return play_bt

def pause(panel):
    pause_bt = tb.Button(panel, text="Pausa", style="secondary.TButton", command=pausar)
    pause_bt.grid(column=1, row=2, sticky="nswe", padx=10, pady=10, ipadx=5, ipady=5)
    return pause_bt

def stop(panel):
    frenar_bt = tb.Button(panel, text="Stop", style="primary.TButton", command=frenar)
    frenar_bt.grid(column=0, row=2, sticky="nswe", padx=10, pady=10, ipadx=5, ipady=5)
    return frenar_bt

def imagen(panel):
    portada = cargar_imagen()
    portada = ImageTk.PhotoImage(portada)
    img = tb.Canvas(panel, relief="raised", background="white", width=300, height=300, bd=15)
    img.create_image(0, 0, anchor="nw", image=portada)
    img.grid(column=0, row=0, columnspan=3)
    img.reference = portada
    return img