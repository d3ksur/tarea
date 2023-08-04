import tkinter as tk

def sumar():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        resultado.set(num1 + num2)
    except ValueError:
        resultado.set("Error")

def restar():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        resultado.set(num1 - num2)
    except ValueError:
        resultado.set("Error")

def multiplicar():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        resultado.set(num1 * num2)
    except ValueError:
        resultado.set("Error")

def dividir():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        if num2 == 0:
            resultado.set("Error")
        else:
            resultado.set(num1 / num2)
    except ValueError:
        resultado.set("Error")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x200")

# Variables para almacenar los números y el resultado
num1_entry = tk.Entry(ventana)
num2_entry = tk.Entry(ventana)
resultado = tk.StringVar()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, textvariable=resultado)

# Botones para las operaciones
sumar_btn = tk.Button(ventana, text="Sumar", command=sumar)
restar_btn = tk.Button(ventana, text="Restar", command=restar)
multiplicar_btn = tk.Button(ventana, text="Multiplicar", command=multiplicar)
dividir_btn = tk.Button(ventana, text="Dividir", command=dividir)

# Posicionar los elementos en la ventana
num1_entry.pack()
num2_entry.pack()
sumar_btn.pack()
restar_btn.pack()
multiplicar_btn.pack()
dividir_btn.pack()
resultado_label.pack()

# Iniciar el bucle de eventos
ventana.mainloop()
