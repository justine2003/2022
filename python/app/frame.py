from tkinter import *

raiz = Tk()

nombre =StringVar()

miFrame=Frame(raiz, width=800, height=400)
miFrame.pack()

nombreLabel=Label(miFrame ,text="User: ").grid(row=0, column=0)

cuadroUser=Entry(miFrame, textvariable=nombre).grid(row=0, column=1)

Contralabel=Label(miFrame, text="Pasword").grid(row=1, column=0)

CuadroPasword=Entry(miFrame,show="*").grid(row=1, column=1)

#Scroll
#CuadroComentario=Text(miFrame,width=16, height=5 )
#CuadroComentario.grid(row=2, column=1)
#Scroll=Scrollbar(miFrame, command=CuadroComentario.yview)
#Scroll.grid(row=2, column=2, sticky="nsew")
#CuadroComentario.config(yscrollcommand=Scroll.set)

def Codigo():
    nombre.set("Justin")

#Button
button=Button(raiz, text="Enviar",command=Codigo)
button
button.pack()



raiz.mainloop()

