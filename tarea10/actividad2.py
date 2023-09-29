import tkinter as tk

def show_text():
    text = entry.get()
    label.config(text=text)

root = tk.Tk()
root.title("LabelFrames")

frame_entry = tk.LabelFrame(root, text="Entry", padx=10, pady=10)
frame_entry.pack()

entry = tk.Entry(frame_entry, width=20)
entry.pack()

frame_button = tk.LabelFrame(root, text="Botón", padx=10, pady=10)
frame_button.pack()

button = tk.Button(frame_button, text="Mostrar", command=show_text)
button.pack()

label = tk.Label(root, text="", width=20)
label.pack()

root.mainloop()
