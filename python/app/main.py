from tkinter import *

raiz = Tk()

#base
raiz.title("App")
#raiz.resizable(False,False)
#raiz.geometry("600x600")
#raiz.config(background="black")

#Pantalla
mlFrame=Frame()
#mlFrame.pack(side="left", anchor="s")
mlFrame.pack(fill="both", expand="True")
mlFrame.config(background="black")
mlFrame.config(width="600",height="600")

raiz.mainloop()