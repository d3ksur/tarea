from tkinter import *

window = Tk()
window.geometry("400x200+10+10")

label = Label(window, text="Hola Mundo").place(x = 10, y = 10)

button = Button(window, text="Salir de la ventana", command=window.destroy).place(x = 10, y = 50)

window.mainloop()
