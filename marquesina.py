def marquesina(label, text, ancho=20):
    if len(text) <= ancho:
        label.config(text=text)
        return
    
    text_con_espacios = text + "   •   " 

    def mover(actual_text):
        label.config(text=actual_text)

        siguiente_texto = actual_text[1:] + actual_text[0]

        label.after(200, mover, siguiente_texto)

    mover(text_con_espacios)