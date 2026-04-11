import ttkbootstrap as tb
from funciones import *

def play(panel):
    play_bt = tb.Button(panel, text="Play", style="success.TButton",command=reproducir)
    play_bt.grid(column=3, row=2, padx=5, pady=5)
    return play_bt

def pause(panel):
    pause_bt = tb.Button(panel, text="Pausa", style="secondary.TButton", command=pausar)
    pause_bt.grid(column=2, row=2, padx=5, pady=5)
    return pause_bt

def stop(panel):
    frenar_bt = tb.Button(panel, text="Stop", style="primary.TButton", command=frenar)
    frenar_bt.grid(column=1, row=2, padx=5, pady=5)
    return frenar_bt