import ttkbootstrap as tb
from funciones import *

def play(panel):
    iniciar = tb.Button(panel, text="Play", style="primary.TButton",command=reproducir)
    iniciar.grid(column=3, row=2, padx=5, pady=5)
    return iniciar