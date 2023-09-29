import tkinter as tk

def show_selection():
    print(radio_var.get())

root = tk.Tk()
root.title("Radiobutton")

radio_var = tk.IntVar()

r1 = tk.Radiobutton(root, text="Opción 1", variable=radio_var, value=1)
r2 = tk.Radiobutton(root, text="Opción 2", variable=radio_var, value=2)
r3 = tk.Radiobutton(root, text="Opción 3", variable=radio_var, value=3)
r4 = tk.Radiobutton(root, text="Opción 4", variable=radio_var, value=4)

r1.grid(row=0, column=0)
r2.grid(row=0, column=1)
r3.grid(row=1, column=0)
r4.grid(row=1, column=1)

btn_show = tk.Button(root, text="Mostrar selección", command=show_selection)
btn_show.grid(row=2, column=0, columnspan=2)

root.mainloop()
