import tkinter as tk

def show_text():
    name = name_entry.get()
    age = age_entry.get()
    text = "Mi nombre es ", name, ". " "Tengo ", age, " años."
    results_label.config(text=text)

app = tk.Tk()
app.title("Data personal.")

name_label = tk.Label(app, text="Nombre:")
name_label.pack()

name_entry = tk.Entry(app)
name_entry.pack()

age_label = tk.Label(app, text="Edad")
age_label.pack()

age_entry = tk.Entry(app)
age_entry.pack()

show_button = tk.Button(app, text="Mostrar", command=show_text)
show_button.pack()

results_label = tk.Label(app, text="")
results_label.pack()

app.mainloop()
