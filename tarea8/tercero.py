import tkinter as tk

def mostrar_saludo():
    mensaje_label.config(text="Buenos días para Todos")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Saludo App")
ventana.geometry("300x100")

# Etiqueta para mostrar el mensaje
mensaje_label = tk.Label(ventana, text="", font=("Arial", 14))

# Botón para mostrar el saludo
boton_saludo = tk.Button(ventana, text="Saludo", command=mostrar_saludo)

# Posicionar la etiqueta y el botón en la ventana
mensaje_label.pack(pady=20)
boton_saludo.pack()

# Iniciar el bucle de eventos
ventana.mainloop()
