import tkinter as tk

def show_selection():
    milk = milk_var.get()
    sugar = sugar_var.get()
    label.config(text="Café con {} {} azúcar".format(
        "leche" if milk else "sin leche",
        "y azúcar" if sugar else "y sin azúcar"
    ))

root = tk.Tk()
root.title("Café")

milk_var = tk.BooleanVar()
sugar_var = tk.BooleanVar()

milk_check = tk.Checkbutton(root, text="Leche", variable=milk_var)
sugar_check = tk.Checkbutton(root, text="Azúcar", variable=sugar_var)

milk_check.grid(row=0, column=0)
sugar_check.grid(row=1, column=0)

label = tk.Label(root, text="")
label.grid(row=2, column=0)

btn_show = tk.Button(root, text="Mostrar selección", command=show_selection)
btn_show.grid(row=3, column=0)

root.mainloop()
