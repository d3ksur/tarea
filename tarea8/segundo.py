import tkinter as tk

def change_color(color):
    window.config(bg=color)

# Crear la window principal
window = tk.Tk()
window.title("Mis primeros pasos")
window.geometry("780x400")

# Botones para cambiar el color de la pantalla
rojo_btn = tk.Button(window, text="Rojo", command=lambda: change_color("red"))
amarillo_btn = tk.Button(window, text="Amarillo", command=lambda: change_color("yellow"))
verde_btn = tk.Button(window, text="Verde", command=lambda: change_color("green"))

# Posicionar los botones
rojo_btn.pack()
amarillo_btn.pack()
verde_btn.pack()

# Iniciar el bucle de eventos
window.mainloop()
