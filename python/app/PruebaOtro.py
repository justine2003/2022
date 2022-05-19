from tkinter import *
from codigo import *

ventana = Tk()

ventana.title("Prollecto")

boton = Button(ventana, text="Enviar", width=15, command=(lambda: Ejemplo()))
boton.grid(row=1, column=1)

ventana.mainloop()