import tkinter as tk

def saludar():
    name = name_entry.get()
    label.config(text="Hola," + name + "!")

root = tk.Tk()
root.title("Saludo")

frame_entry = tk.LabelFrame(root, text="Nombre", padx=10, pady=10)
frame_entry.pack(side="top", anchor="n")

name_entry = tk.Entry(frame_entry)
name_entry.pack()

frame_button = tk.LabelFrame(root, text="Saludar", padx=10, pady=10)
frame_button.pack(side="top", anchor="n")

button = tk.Button(frame_button, text="Saludar", command=saludar)
button.pack()

frame_label = tk.LabelFrame(root, text="Saludo", padx=10, pady=10)
frame_label.pack(side="top", anchor="n")

label = tk.Label(frame_label, text="")
label.pack()

root.mainloop()
