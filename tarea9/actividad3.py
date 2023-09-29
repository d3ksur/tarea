import tkinter as tk

def show_selection():
    label.config(text=radio_var.get())

def reset_selection():
    radio_var.set(None)

root = tk.Tk()
root.title("Botones radiales")

radio_var = tk.IntVar()

r1 = tk.Radiobutton(root, text="Opción 1", variable=radio_var, value=1)
r2 = tk.Radiobutton(root, text="Opción 2", variable=radio_var, value=2)
r3 = tk.Radiobutton(root, text="Opción 3", variable=radio_var, value=3)

r1.grid(row=0, column=0)
r2.grid(row=0, column=1)
r3.grid(row=0, column=2)

label = tk.Label(root, text="")
label.grid(row=1, column=0, columnspan=3)

btn_show = tk.Button(root, text="Mostrar selección", command=show_selection)
btn_show.grid(row=2, column=0, columnspan=3)

btn_reset = tk.Button(root, text="Resetear selección", command=reset_selection)
btn_reset.grid(row=3, column=0, columnspan=3)

root.mainloop()
