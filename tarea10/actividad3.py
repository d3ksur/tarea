import tkinter as tk

window = tk.Tk()
window.title("Item")

def perform_operation(operation):
    print("Operacion seleccionada: ", operation)

wheat_frame = tk.LabelFrame(window, text="Item", labelanchor="n", bg="Wheat", padx=10, pady=10)
light_blue_frame = tk.LabelFrame(window, text="Operaciones", labelanchor="n", bg="LightBlue", padx=10, pady=10)

item_code_label = tk.Label(wheat_frame, text="Codigo del item:")
item_description_label = tk.Label(wheat_frame, text="Descripcion:")
item_price_label = tk.Label(wheat_frame, text="Precio:")

item_code_entry = tk.Entry(wheat_frame)
item_description_entry = tk.Entry(wheat_frame)
item_price_entry = tk.Entry(wheat_frame)

create_button = tk.Button(light_blue_frame, text="Crear", command=lambda: perform_operation("Crear"))
delete_button = tk.Button(light_blue_frame, text="Eliminar", command=lambda: perform_operation("Eliminar"))
modify_button = tk.Button(light_blue_frame, text="Modificar", command=lambda: perform_operation("Modificar"))

wheat_frame.grid(row=0, column=0, padx=10, pady=10)
light_blue_frame.grid(row=3, column=0, padx=10, pady=10)

item_code_label.grid(row=0, column=0, sticky="w")
item_description_label.grid(row=1, column=0, sticky="w")
item_price_label.grid(row=2, column=0, sticky="w")

item_code_entry.grid(row=0, column=1)
item_description_entry.grid(row=1, column=1)
item_price_entry.grid(row=2, column=1)

create_button.grid(row=0, column=0, padx=5, pady=5)
delete_button.grid(row=0, column=4, padx=5, pady=5)
modify_button.grid(row=0, column=8, padx=5, pady=5)

window.mainloop()
