from tkinter import *
from PIL import ImageTk, Image
import subprocess as sub
import time

windows = Tk()

#Ajustes de ventana
windows.title("App")
windows.geometry('900x500')

#Codigo de apertura del diseño 
def diseño():
    disenoFrame = Frame(windows,bg="Blue",width=900,height=500).place(x=0, y=0)

    global ralla
    ralla = ImageTk.PhotoImage(Image.open("Image/icons/lineas.png").resize((30, 30)))
    rallas = Button(windows, bg="Blue", image=ralla, activebackground="Red", command=toggle).place(x=5,y=5)

    #Codigo de botones

#Codigo de apertura de Office
def office():
    officeFrame = Frame(windows,bg="Red",width=900,height=500).place(x=0,y=0)

    global ralla
    ralla = ImageTk.PhotoImage(Image.open("Image/icons/lineas.png").resize((30, 30)))
    rallas = Button(windows, bg="Blue", image=ralla, activebackground="Red", command=toggle).place(x=5,y=5)

    #codigo y botones que van dentro del menu office

#Codigo de apertura del menu Progra
def progra():
    PrograFrame=Frame(windows,bg="Yellow",width=900,height=500).place(x=0,y=0)

    global ralla
    ralla = ImageTk.PhotoImage(Image.open("Image/icons/lineas.png").resize((30, 30)))
    rallas = Button(windows, bg="Blue",image=ralla, activebackground="Red", command=toggle).place(x=5,y=5)

    #Codigo y botones que van dentro del menu de progra
    def visual():
        sub.Popen(r"C:\Users\justi\AppData\Local\Programs\Microsoft VS Code\Code.exe")

    Button(PrograFrame,text="visual",command=visual).place(x=300,y=200)

    
def Inicio():
    InicioFrame = Frame(windows,width=900,height=500).place(x=0,y=0)

    global ralla
    ralla = ImageTk.PhotoImage(Image.open("Image/icons/lineas.png").resize((30, 30)))
    rallas = Button(windows, bg="Blue",image=ralla, activebackground="Red", command=toggle).place(x=5,y=5)

#Menu desplegable
def toggle():
    menu =Frame(windows, bg="Black",width=300,height=500)
    menu.place(x=0, y=0)

    def deleteMenu():
        menu.destroy()

    global X
    X = ImageTk.PhotoImage(Image.open("Image/icons/X.png").resize((30,30)))
    Button(menu,text="Close",image=X,bg="Blue",activebackground="Red",command=deleteMenu).place(x=5.5,y=5.5)


    #botones del menu
    Button(menu,text="Inicio",width=30,height=2,command=Inicio).place(x=30,y=50)
    Button(menu,text="Progra",width=30,height=2,command=progra).place(x=30,y=100)
    Button(menu,text="Office",width=30,height=2,command=office).place(x=30,y=150)
    Button(menu,text="Diseño",width=30,height=2,command=diseño).place(x=30,y=200)
    Button(menu,width=30,height=10).place(x=30,y=280)

ralla = ImageTk.PhotoImage(Image.open("Image/icons/lineas.png").resize((30,30)))
rallas = Button(windows,bg="Blue",image=ralla,activebackground="Red",command=toggle).place(x=5,y=5)

#Corredor de codigo
windows.mainloop()