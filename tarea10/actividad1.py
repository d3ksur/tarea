import tkinter as tk

def show_text():
    text = entry.get()
    label.config(text=text)

root = tk.Tk()
root.title("LabelFrame")

frame = tk.LabelFrame(root, text="Entrada")
frame.pack()

entry = tk.Entry(frame)
entry.pack()

button = tk.Button(frame, text="Mostrar", command=show_text)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
