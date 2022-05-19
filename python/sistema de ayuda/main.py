from tkinter import *
from PIL import ImageTk, Image
import time

windows = Tk()

#Ajustes de ventana
windows.title("App")
windows.geometry('900x500')

#Dreclaracion de variables

#Codigo de apertura del menu Progra
def progra():
    PrograFrame=Frame(windows,bg="Yellow",width=900,height=500)
    PrograFrame.place(x=0,y=0)

    def deleProgra():
        PrograFrame.destroy()

    global ralla
    ralla = ImageTk.PhotoImage(Image.open("Image/lineas.png").resize((30, 30)))
    rallas = Button(windows, bg="Blue", text="Open", image=ralla, activebackground="Red", command=toggle).place(x=5,y=5)

    #Codigo y botones que van dentro del menu de progra


#Menu desplegable
def toggle():
    menu =Frame(windows, bg="Black",width=300,height=500)
    menu.place(x=0, y=0)

    def deleteMenu():
        menu.destroy()

    global X
    X = ImageTk.PhotoImage(Image.open("Image/X.png").resize((30,30)))
    Button(menu,text="Close",image=X,bg="Blue",activebackground="Red",command=deleteMenu).place(x=5.5,y=5.5)


    #botones del menu
    Button(menu,text="Inicio",width=30,height=2).place(x=30,y=70)
    Button(menu,text="Progra",width=30,height=2,command=progra).place(x=30,y=130)

ralla = ImageTk.PhotoImage(Image.open("Image/lineas.png").resize((30,30)))
rallas = Button(windows,bg="Blue",text="Open",image=ralla,activebackground="Red",command=toggle).place(x=5,y=5)

#Corredor de codigo
windows.mainloop()