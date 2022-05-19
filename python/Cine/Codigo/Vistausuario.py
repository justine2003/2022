from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk, Image
import funcionesLlamda as fl 
import os

windowsFrame1 = Tk()


#Ajustes de ventana
windowsFrame1.geometry('900x500')
windowsFrame1.title("Fidecines")

#Imajen de fondo ------------------------------------------------------------------
fondo = ImageTk.PhotoImage(Image.open("Imagenes\Background.jpeg").resize((900,500)))
Label(windowsFrame1,image=fondo).place(x=0,y=0)
#-----------------------------------------------------------------------------------

#Imagenes de Portada de Peliculas
PBatman = ImageTk.PhotoImage(Image.open("Imagenes/Portadas/Batman.jpg").resize((200,300)))
Puncharted = ImageTk.PhotoImage(Image.open("Imagenes/Portadas/Uncharted.jpg").resize((200,300)))
Pmorvious = ImageTk.PhotoImage(Image.open("Imagenes/Portadas/morbius.jpg").resize((200,300)))
#-------------------------------

#Imagenes de las palomitas--------------
Pgrandes = ImageTk.PhotoImage(Image.open("Imagenes/comida/Pgrandes.jpeg").resize((200,300)))
Pmedianas = ImageTk.PhotoImage(Image.open("Imagenes/comida/Pmedianas.jpeg").resize((200,300)))
Ppequenas = ImageTk.PhotoImage(Image.open("Imagenes/comida/Ppequena.jpeg").resize((200,300)))
#---------------------------------------

#Declaracion de inico de Login

LUsuario = StringVar()
LContra = StringVar()

#==============================

#Declaracion de inicios Registro
RNombre = StringVar()
RContra = StringVar()
RCedula = StringVar()
RNT = StringVar()
RCorreo = StringVar()
RDireccion = StringVar()
RTipoPersona = StringVar()
RClase = StringVar()
#-------------------------

#Declaracion de factura
DiaF = StringVar()
HoraF = StringVar()
NumF = IntVar()
CovidF = IntVar()
#----------------------

#Seleccion de colores
NA1 = 0
NA2 = 0
NA3 = 0
NA4 = 0
NA5 = 0
NA6 = 0
NA7 = 0
NA8 = 0
NB1 = 0
NB2 = 0
NB3 = 0
NB4 = 0
NB5 = 0
NB6 = 0
NB7 = 0
NB8 = 0
NC1 = 0
NC2 = 0
NC3 = 0
NC4 = 0
NC5 = 0
NC6 = 0
NC7 = 0
NC8 = 0
ND1 = 0
ND2 = 0
ND3 = 0
ND4 = 0
ND5 = 0
ND6 = 0
ND7 = 0
ND8 = 0
NE1 = 0
NE2 = 0
NE3 = 0
NE4 = 0
NE5 = 0
NE6 = 0
NE7 = 0
NE8 = 0
NF1 = 0
NF2 = 0
NF3 = 0
NF4 = 0
NF5 = 0
NF6 = 0
NF7 = 0
NF8 = 0
NG1 = 0
NG2 = 0
NG3 = 0
NG4 = 0
NG5 = 0
NG6 = 0
NG7 = 0
NG8 = 0
NH1 = 0
NH2 = 0
NH3 = 0
NH4 = 0
NH5 = 0
NH6 = 0
NH7 = 0
NH8 = 0
#--------------------

#Validacion de Registro
def Registro():
  if RNombre.get() == "" or RCedula.get() == "" or RNT.get() == "" or RCorreo.get() =="" or RDireccion.get() == "" or RTipoPersona.get() == "" or RClase.get() == "" :
    messagebox.showerror("Error","No puede haber cajas vacias")
  else:
   archivo = open("DatosCliente/"+RNombre.get()+".txt","w")
   archivo.write(RNombre.get()+"\n")
   archivo.write(RContra.get()+"\n")
   archivo.write(RCedula.get()+"\n")
   archivo.write(RNT.get()+"\n")
   archivo.write(RCorreo.get()+"\n")
   archivo.write(RDireccion.get()+"\n") 
   archivo.write(RTipoPersona.get()+"\n")
   archivo.write(RClase.get())
   
   messagebox.showinfo("Informacion","Registro exitoso")
#----------------------------------------------------------------------------------------------------------------------------


#Validacion del Login
def Login():
  fl.validacion(LUsuario.get(),LContra.get())

  if fl.Valor == True: 
    main()
  else:
    messagebox.showerror("Error","Usurio o contraseña no validos")
#--------------------


#Pagina de impresion--------------------------------
def Imprimir():
  fl.NumclienteC(fl.TipoPelicula)
  fl.NumC()

  ruta = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
  ruta = ruta+"\Facturas "+str(fl.NumF)+".txt"

  file = open(ruta,"w")

  file.write("---------------------------"+'\n')
  file.write("Numero de Factura:"+str(fl.NumF)+'\n')
  file.write("Nombre del cliente"+str(LUsuario.get())+'\n')
  file.write("Fecha: "+DiaF.get()+'\n')
  file.write("Hora: "+HoraF.get()+'\n')
  file.write("Nombre de la pelicula: "+str(fl.TipoPelicula)+'\n')
  file.write("Numero de personas: "+str(NumF.get())+'\n')

  if CovidF.get() == 1:file.write("Modo Covid Si"+'\n')

  file.write("Combo de palomitas:"+str(fl.listac)+'\n')

  Total = NumF.get() * 3000
  TotalIVA = float(Total) * 0.13
  TotalF = TotalIVA + float(Total) 

  file.write("Asientos: "+str(fl.Lasiento)+'\n')
  file.write("Precio: "+str(Total)+'\n')
  file.write("Iva: "+str(TotalIVA)+'\n')
  file.write("Precio con IVA: "+str(TotalF)+'\n')
  file.write("-----------------------------"+'\n')
  file.close()
   
  if CovidF.get() == 1:
     messagebox.showinfo("Informacion","Numero de factura: "+str(fl.NumF)+'\n'+"Nombre del cliente: "+str(LUsuario.get())+'\n'+"Fecha: "+DiaF.get()+'\n'+"Hora: "+HoraF.get()+'\n'+"Nombre de la pelicula: "+str(fl.TipoPelicula)+'\n'+"Numero de personas: "+str(NumF.get())+'\n'+"Modo Covid si"+'\n'+"Combo de palomitas: "+str(fl.listac)+'\n'+"Asientos: "+str(fl.Lasiento)+'\n'+"Precio: "+str(Total)+'\n'+"Iva: "+str(TotalIVA)+'\n'+"Precio con IVA: "+str(TotalF))
  else:
     messagebox.showinfo("Informacion","Numero de factura: "+str(fl.NumF)+'\n'+"Nombre del cliente: "+str(LUsuario.get())+'\n'+"Fecha: "+DiaF.get()+'\n'+"Hora: "+HoraF.get()+'\n'+"Nombre de la pelicula: "+str(fl.TipoPelicula)+'\n'+"Numero de personas: "+str(NumF.get())+'\n'+"Combo de palomitas: "+str(fl.listac)+'\n'+"Asientos: "+str(fl.Lasiento)+'\n'+"Precio: "+str(Total)+'\n'+"Iva: "+str(TotalIVA)+'\n'+"Precio con IVA: "+str(TotalF))
#-----------------------------------------------------

def comida():
  fl.listac = []
  FrameC = Frame(windowsFrame1,width=900,height=500)
  FrameC.place(x=0,y=0)
  
  Label(FrameC,image=fondo).place(x=0,y=0)
  
  def PG():
    fl.listac.append("Palomitas Grandes")

  def PM():
    fl.listac.append("Palomitas Medianas")

  def PC():
    fl.listac.append("Palomitas Chicas")

  def delete():
    FrameC.destroy()

  Label(FrameC,text="Combo de palomitas grandes",font=("Arial",11)).place(x=105,y=50)
  Button(FrameC,text="Combo de palomitas grandes",command = PG,width=200,height=300,image=Pgrandes).place(x=100,y=80)
  
  Label(FrameC,text="Combo de palomitas medianas",font=("Arial",11)).place(x=350,y=50)
  Button(FrameC,text="Combo de palomitas medianas",command = PM,width=200,height=300,image=Pmedianas).place(x=350,y=80)
  
  Label(FrameC,text="Combo de palomitas chicas",font=("Arial",11)).place(x=607,y=50)
  Button(FrameC,text="Combo de palomitas chicas",command = PC,width=200,height=300,image=Ppequenas).place(x=600,y=80)
  
  Button(FrameC,text="Siguiente",command = Imprimir).place(x=430,y=450)
  Button(FrameC,text="Atras",command=delete).place(x=390,y=450)
  

#Llammada de Peliculas
def Batman():
  frameB = Frame(windowsFrame1,width=900,height=500)
  frameB.place(x=0,y=0)

  fl.TipoPelicula = "Batman"
  fl.Lasiento.clear()
  
  #imajen de fondo de---------------------------
  Label(frameB,image=fondo).place(x=0,y=0)
  #----------------------------------------------
    
  Label(frameB,text="Tanda",bg="#CDC2BF",font=("Arial",45),).place(x=350,y=0)

  comboF=ttk.Combobox(frameB,value=["Dia","15/04","17/04","19/04","20/04"],state="readonly",justify=CENTER,textvariable=DiaF)
  comboF.current(0)
  comboF.place(x=20,y=70)
  
  comboH = ttk.Combobox(frameB,value=["Hora","2:30","5:00","8:00","8:30"],state="readonly",justify=CENTER,textvariable=HoraF)
  comboH.current(0)
  comboH.place(x=170,y=70)

  numP = Entry(frameB,width=23,justify=CENTER,textvariable=NumF)
  numP.insert(0,"Numero de personas")
  numP.place(x=20,y=100)

  Checkbutton(frameB,bg="#CDC2BF",text="Modo covid",variable=CovidF).place(x=170,y=99)

  def A1():
    global NA1
    if NA1 == 0:
      CA1.config(bg="Red")
      NA1 = 1
      fl.Lasiento.append("A1")
    else:
      CA1.config(bg="Blue")
      NA1 = 0
      fl.Lasiento.remove("A1")

  def A2():
    global NA2
    if NA2 == 0:
      CA2.config(bg="Red")
      NA2 = 1
      fl.Lasiento.append("A2")
    else:
      CA2.config(bg="Blue")
      NA2 = 0
      fl.Lasiento.remove("A2")
 
  def A3():
    global NA3
    if NA3 == 0:
       CA3.config(bg="Red")
       NA3 = 1
       fl.Lasiento.append("A3")
    else:
      CA3.config(bg="Blue")
      NA3 = 0
      fl.Lasiento.remove("A3")

  def A4():
    global NA4
    if NA4 == 0: 
       CA4.config(bg="Red")
       NA4 = 1
       fl.Lasiento.append("A4")
    else:
      CA4.config(bg="Blue")
      NA4 = 0
      fl.Lasiento.remove("A4")

  def A5():
    global NA5
    if NA5 == 0: 
       CA5.config(bg="Red")
       NA5 = 1
       fl.Lasiento.append("A5")
    else:
      CA5.config(bg="Blue")
      NA5 = 0 
      fl.Lasiento.remove("A5")

  def A6():
    global NA6
    if NA6 == 0: 
       CA6.config(bg="Red")
       NA6 = 1
       fl.Lasiento.append("A6")
    else:
      CA6.config(bg="Blue")
      NA6 = 0
      fl.Lasiento.remove("A6")

  def A7():
    global NA7 
    if  NA7 == 0: 
        CA7.config(bg="Red")
        NA7 = 1
        fl.Lasiento.append("A7")
    else: 
      CA7.config(bg="Blue")
      NA7 = 0
      fl.Lasiento.remove("A7")

  def A8():
    global NA8
    if NA8 == 0:
       CA8.config(bg="Red")
       NA8 = 1
       fl.Lasiento.append("A8")
    else:
      CA8.config(bg="Blue")
      NA8 = 0
      fl.Lasiento.remove("A8")
  
  def B1():
    global NB1
    if NB1 == 0:
       CB1.config(bg="Red")
       NB1 = 1
       fl.Lasiento.append("B1")
    else:
      CB1.config(bg="Blue")
      NB1 = 0
      fl.Lasiento.remove("B1")
    
  def B2():
    global NB2
    if NB2 == 0:
       CB2.config(bg="Red")
       NB2 = 1
       fl.Lasiento.append("B2")
    else:
      CB2.config(bg="Blue")
      NB2 = 0
      fl .Lasiento.remove("B2")

  def B3():
    global NB3
    if NB3 == 0:
       CB3.config(bg="Red")
       NB3 = 1
       fl.Lasiento.append("B3")
    else:
      CB3.config(bg="Blue")
      NB3 = 0
      fl .Lasiento.remove("B3")

  def B4():
    global NB4
    if NB4 == 0:
      CB4.config(bg="Red")
      NB4 = 1
      fl.Lasiento.append("B4")
    else:
      CB4.config(bg="Blue")
      NB4 = 0
      fl.Lasiento.remove("B4")
  
  def B5():
    global NB5
    if NB5 == 0:
       CB5.config(bg="Red")
       NB5 = 1
       fl.Lasiento.append("B5")
    else:
      CB5.config(bg="Blue")
      NB5 = 0
      fl.Lasiento.remove("B5")

  def B6():
    global NB6
    if NB6 == 0:
       CB6.config(bg="Red")
       NB6 = 1
       fl.Lasiento.append("B6")
    else:
      CB6.config(bg="Blue")
      NB6 = 0
      fl.Lasiento.remove("B6")

  def B7():
    global NB7
    if NB7 == 0:
       CB7.config(bg="Red")
       NB7 = 1
       fl.Lasiento.append("B7")
    else:
      CB7.config(bg="Blue")
      NB7 = 0
      fl.Lasiento.remove("B7")

  def B8():
    global NB8
    if NB8 == 0:
       CB8.config(bg="Red")
       NB8 = 1
       fl.Lasiento.append("B8")
    else:
      CB8.config(bg="Blue")
      NB8 = 0
      fl.Lasiento.remove("B8")

  def C1():
    global NC1
    if NC1 == 0:
        CC1.config(bg="Red")
        NC1 = 1
        fl.Lasiento.append("C1")
    else:
      CC1.config(bg="Blue")
      NC1 = 0
      fl.Lasiento.remove("C2")

  def C2():
    global NC2
    if NC2 == 0:
      CC2.config(bg="Red")
      NC2 = 1
      fl.Lasiento.append("C3")
    else:
      CC2.config(bg="Blue")
      NC2 = 0
      fl.Lasiento.remove("C3")

  def C3():
    global NC3
    if NC3 == 0:
       CC3.config(bg="Red")
       NC3 = 1
       fl.Lasiento.append("C3")
    else:
      CC3.config(bg="Blue")
      NC3 = 0
      fl.Lasiento.append("C3")

  def C4():
    global NC4
    if NC4 == 0:
      CC4.config(bg="Red")
      NC4 = 1
      fl.Lasiento.append("C4")
    else:
      CC4.config(bg="Blue")
      NC4 = 0
      fl.Lasiento.append("C4")

  def C5():
    global NC5
    if NC5 == 0:
        CC5.config(bg="Red")
        NC5 = 1
        fl.Lasiento.append("C5")
    else:
      CC5.config(bg="Blue")
      NC5 = 0
      fl.Lasiento.remove("C5")

  def C6():
    global NC6
    if NC6 == 0:
      CC6.config(bg="Red")
      NC6 = 1
      fl.Lasiento.append("C6")
    else:
      CC6.config(bg="Blue")
      NC6 = 0
      fl.Lasiento.remove("C6")

  def C7():
    global NC7
    if NC7 == 0:
       CC7.config(bg="Red")
       NC7 = 1
       fl.Lasiento.append("C7")
    else:
      CC7.config(bg="Blue")
      NC7 = 0
      fl.Lasiento.remove("C7")

  def C8():
    global NC8
    if NC8 == 0:
       CC8.config(bg="Red")
       NC8 = 1
       fl.Lasiento.append("C8")
    else:
      CC8.config(bg="Blue")
      NC8 = 0
      fl.Lasiento.remove("C8")

  def D1():
    global ND1
    if ND1 == 0:
      CD1.config(bg="Red")
      ND1 = 1
      fl.Lasiento.append("D1")
    else:
      CD1.config(bg="Blue")
      ND1 = 0
      fl.Lasiento.remove("D1")

  def D2():
    global ND2
    if ND2 == 0:
       CD2.config(bg="Red")
       ND2 = 1
       fl.Lasiento.append("D2")
    else:
      CD2.config(bg="Blue")
      ND2 = 0
      fl.Lasiento.remove("D2")

  def D3():
    global ND3
    if ND3 == 0:
        CD3.config(bg="Red")
        ND3 = 1
        fl.Lasiento.append("D3")
    else:
      CD3.config(bg="Blue")
      ND3 = 0
      fl.Lasiento.remove("D3")

  def D4():
    global ND4
    if ND4 == 0:
      CD4.config(bg="Red")
      ND4 = 1
      fl.Lasiento.append("D4")
    else:
      CD4.config(bg="Blue")
      ND4 = 0
      fl.Lasiento.remove("D4")

  def D5():
    global ND5
    if ND5 == 0:
       CD5.config(bg="Red")
       ND5 = 1 
       fl.Lasiento.append("D5")
    else:
      CD5.config(bg="Blue")
      ND5 = 0
      fl.Lasiento.remove("D5")

  def D6():
    global ND6
    if ND6 == 0:
      CD6.config(bg="Red")
      ND6 = 1 
      fl.Lasiento.append("D6")
    else:
      CD6.config(bg="Blue")
      ND6 = 0
      fl.Lasiento.remove("D6")

  def D7():
    global ND7
    if ND7 == 0:
      CD7.config(bg="Red")
      ND7 = 1
      fl.Lasiento.append("D7")
    else:
      CD7.config(bg="Blue")
      ND7 = 0
      fl.Lasiento.remove("D7")

  def D8():
    global ND8
    if ND8 == 0:
      CD8.config(bg="Red")
      ND8 = 1
      fl.Lasiento.append("D8")
    else:
      CD8.config(bg="Blue")
      ND8 = 0
      fl.Lasiento.remove("D8")

  def E1():
    global NE1
    if NE1 == 0:
       CE1.config(bg="Red")
       NE1 = 1
       fl.Lasiento.append("E1")
    else:
      CE1.config(bg="Blue")
      NE1 = 0
      fl.Lasiento.remove("E1")

  def E2():
    global NE2
    if NE2 == 0:
      CE2.config(bg="Red")
      NE2 = 1
      fl.Lasiento.append("E2")
    else:
      CE2.config(bg="Blue")
      NE2 = 0
      fl.Lasiento.remove("E2")

  def E3():
    global NE3
    if NE3 == 0:
      CE3.config(bg="Red")
      NE3 = 1
      fl.Lasiento.append("E3")
    else:
      CE3.config(bg="Blue")
      NE3 = 0
      fl.Lasiento.remove("E3")

  def E4():
    global NE4
    if NE4 == 0:
      CE4.config(bg="Red")
      NE4 = 1
    else:
      CE4.config(bg="Blue")
      NE4 = 0
      fl.Lasiento.remove("E4")

  def E5():
    global NE5
    if NE5 == 0:
      CE5.config(bg="Red")
      NE5 = 1 
      fl.Lasiento.append("E5")
    else:
      CE5.config(bg="Blue")
      NE5 = 0
      fl.Lasiento.remove("E5")

  def E6():
    global NE6
    if NE6 == 0:
       CE6.config(bg="Red")
       NE6 = 1
       fl.Lasiento.append("E6")
    else:
      CE6.config(bg="Blue")
      NE6 = 0
      fl.Lasiento.remove("E6")

  def E7():
    global NE7
    if NE7 == 0:
      CE7.config(bg="Red")
      NE7 = 1
      fl.Lasiento.append("E7")
    else:
      CE7.config(bg="Blue")
      NE7 = 0
      fl.Lasiento.remove("E7")

  def E8():
    global NE8
    if NE8 == 0:
      CE8.config(bg="Red")
      NE8 = 1
      fl.Lasiento.append("E8")
    else:
      CE8.config(bg="Blue")
      NE8 = 0
      fl.Lasiento.remove("E8")

  def F1():
    global NF1
    if NF1 == 0:
      CF1.config(bg="Red")
      NF1 = 1
      fl.Lasiento.append("F1")
    else:
      CF1.config(bg="Blue")
      NF1 = 0
      fl.Lasiento.remove("F1")

  def F2():
    global NF2
    if NF2 == 0:
      CF2.config(bg="Red")
      NF2 = 1
      fl.Lasiento.append("F2")
    else:
      CF3.config(bg="Blue")
      NF2 = 0
      fl.Lasiento.remove("F2")

  def F3():
    global NF3
    if NF3 == 0:
      CF3.config(bg="Red")
      NF3 = 1
      fl.Lasiento.append("F3")

  def F4():
    global NF4
    if NF4 == 0:
      CF4.config(bg="Red")
      NF4 = 1
      fl.Lasiento.append("F4")
    else:
      CF4.config(bg="Blue")
      NF4 = 0
      fl.Lasiento.append("F4")

  def F5():
    global NF5
    if NF5 == 0:
      CF5.config(bg="Red")
      NF5 = 1
      fl.Lasiento.append("F5")
    else:
      CF5.config(bg="Blue")
      NF5 = 0
      fl.Lasiento.remove("F5")

  def F6():
    global NF6
    if NF6 == 0:
      CF6.config(bg="Red")
      NF6 = 1
      fl.Lasiento.append("F6")
    else:
      CF6.config(bg="Blue")
      NF6 = 0
      fl.Lasiento.remove("F6")

  def F7():
    global NF7
    if NF7 == 0:
      CF7.config(bg="Red")
      NF7 = 1
      fl.Lasiento.append("F7")
    else:
      CF7.config(bg="Blue")
      NF7 = 0
      fl.Lasiento.remove("F7")

  def F8():
    global NF8
    if NF8 == 0:
      CF8.config(bg="Red")
      NF8 = 1
      fl.Lasiento.append("F8")
    else:
      CF8.config(bg="Blue")
      NF8 = 0
      fl.Lasiento.remove("F8")

  def G1():
    global NG1
    if NG1 == 0:
      CG1.config(bg="Red")
      NG1 = 1
      fl.Lasiento.append("G1")
    else:
      CG1.config(bg="Blue")
      NG1 = 0
      fl.Lasiento.remove("G1")

  def G2():
    global NG2
    if NG2 == 0:
      CG2.config(bg="Red")
      NG2 = 1
      fl.Lasiento.append("G2")
    else:
      CG2.config(bg="Blue")
      NG2 = 0
      fl.Lasiento.remove("G2")

  def G3():
    global  NG3
    if NG3 == 0:
      CG3.config(bg="Red")
      NG3 = 1
      fl.Lasiento.append("G3")
    else:
      CG3.config(bg="Blue")
      NG3 = 0
      fl.Lasiento.remove("G3")

  def G4():
    global NG4
    if NG4 == 0:
      CG4.config(bg="Red")
      NG4 = 1
      fl.Lasiento.append("G4")
    else:
      CG4.config(bg="Blue")
      NG4 = 0
      fl.Lasiento.remove("G4")

  def G5():
    global NG5
    if NG5 == 0:
      CG5.config(bg="Red")
      NG5 = 1
      fl.Lasiento.append("G5")
    else:
      CG5.config(bg="Blue")
      NG5 = 0
      fl.Lasiento.remove("G5")

  def G6():
    global NG6
    if NG6 == 0:
      CG6.config(bg="Red")
      NG6 = 1
      fl.Lasiento.append("G6")
    else:
      CG6.config(bg="Blue")
      NG6 = 0
      fl.Lasiento.remove("G6")

  def G7():
    global NG7
    if NG7 == 0:
      CG7.config(bg="Red")
      NG7 = 1
      fl.Lasiento.append("G7")
    else:
      CG7.config(bg="Blue")
      NG7 = 0
      fl.Lasiento.remove("G7")

  def G8():
    global NG8
    if NG8 == 0:
      CG8.config(bg="Red")
      NG8 = 1
      fl.Lasiento.append("G8")
    else:
      CG8.config(bg="Blue")
      NG8 = 0
      fl.Lasiento.remove("G8")

  def H1():
    global NH1
    if NH1 == 0:
      CH1.config(bg="Red")
      NH1 = 1
      fl.Lasiento.append("H1")
    else:
      CG1.config(bg="Blue")
      NH1 = 0
      fl.Lasiento.remove("H1")

  def H2():
    global NH2
    if NH2 == 0:
      CH2.config(bg="Red")
      NH2 = 1
      fl.Lasiento.append("H2")
    else:
      CG2.config(bg="Blue")
      NH2 = 0
      fl.Lasiento.remove("H2")

  def H3():
    global NH3
    if NH3 == 0:
      CH3.config(bg="Red")
      NH3 = 1
      fl.Lasiento.append("H3")
    else:
      CH3.config(bg="Blue")
      NH3 = 0
      fl.Lasiento.remove("H3")

  def H4():
    global NH4
    if NH4 == 0:
      CH4.config(bg="Red")
      NH4 = 1
      fl.Lasiento.append("H4")
    else:
      CH4.config(bg="Blue")
      NH4 = 0
      fl.Lasiento.remove("H4")

  def H5():
    global NH5
    if NH5 == 0:
      CH5.config(bg="Red")
      NH5 = 1
      fl.Lasiento.append("H5")
    else:
      CH5.config(bg="Blue")
      NH5 = 0 
      fl.Lasiento.remove("H5")

  def H6():
    global NH6
    if NH6 == 0:
      CH6.config(bg="Red")
      NH6 = 1
      fl.Lasiento.append("H6")
    else:
      CH6.config(bg="Blue")
      NH6 = 0 
      fl.Lasiento.remove("H6")

  def H7():
    global NH7
    if NH7 == 0:
      CH7.config(bg="Red")
      NH7 = 1
      fl.Lasiento.append("H7")
    else:
      CH7.config(bg="Blue")
      NH7 = 0
      fl.Lasiento.remove("H7")

  def H8():
    global NH8 
    if NH8 == 0:
      CH8.config(bg="Red")
      NH8 = 1
      fl.Lasiento.append("H8")
    else:
      CH8.config(bg="Blue")
      NH8 = 0
      fl.Lasiento.remove("H8")

  Label(frameB,bg="Black",width=53,height=1).place(x=200,y=190)
   
  CA1 = Button(frameB,text="A1",command=A1,bg="Blue")
  CA1.place(x=200,y=220)
  CA2 = Button(frameB,text="A2",command=A2,bg="Blue")
  CA2.place(x=250,y=220)
  CA3 = Button(frameB,text="A3",command=A3,bg="Blue")
  CA3.place(x=300,y=220)
  CA4 = Button(frameB,text="A4",command=A4,bg="Blue")
  CA4.place(x=350,y=220)
  CA5 = Button(frameB,text="A5",command=A5,bg="Blue")
  CA5.place(x=400,y=220)
  CA6 = Button(frameB,text="A6",command=A6,bg="Blue")
  CA6.place(x=450,y=220)
  CA7 = Button(frameB,text="A7",command=A7,bg="Blue")
  CA7.place(x=500,y=220)
  CA8 = Button(frameB,text="A8",command=A8,bg="Blue")
  CA8.place(x=550,y=220)

  CB1 = Button(frameB,text="B1",command=B1,bg="Blue")
  CB1.place(x=200,y=250)
  CB2 = Button(frameB,text="B2",command=B2,bg="Blue")
  CB2.place(x=250,y=250)
  CB3 = Button(frameB,text="B3",command=B3,bg="Blue")
  CB3.place(x=300,y=250)
  CB4 = Button(frameB,text="B4",command=B4,bg="Blue")
  CB4.place(x=350,y=250)
  CB5 = Button(frameB,text="B5",command=B5,bg="Blue")
  CB5.place(x=400,y=250)
  CB6 = Button(frameB,text="B6",command=B6,bg="Blue")
  CB6.place(x=450,y=250)
  CB7 = Button(frameB,text="B7",command=B7,bg="Blue")
  CB7.place(x=500,y=250)
  CB8 = Button(frameB,text="B8",command=B8,bg="Blue")
  CB8.place(x=550,y=250)

  CC1 = Button(frameB,text="C1",command=C1,bg="Blue")
  CC1.place(x=200,y=280)
  CC2 = Button(frameB,text="C2",command=C2,bg="Blue")
  CC2.place(x=250,y=280)
  CC3 = Button(frameB,text="C3",command=C3,bg="Blue")
  CC3.place(x=300,y=280)
  CC4 = Button(frameB,text="C4",command=C4,bg="Blue")
  CC4.place(x=350,y=280)
  CC5 = Button(frameB,text="C5",command=C5,bg="Blue")
  CC5.place(x=400,y=280)
  CC6 = Button(frameB,text="C6",command=C6,bg="Blue")
  CC6.place(x=450,y=280)
  CC7 = Button(frameB,text="C7",command=C7,bg="Blue")
  CC7.place(x=500,y=280)
  CC8 = Button(frameB,text="C8",command=C8,bg="Blue")
  CC8.place(x=550,y=280)

  CD1 = Button(frameB,text="D1",command=D1,bg="Blue")
  CD1.place(x=200,y=310)
  CD2 = Button(frameB,text="D2",command=D2,bg="Blue")
  CD2.place(x=250,y=310)
  CD3 = Button(frameB,text="D3",command=D3,bg="Blue")
  CD3.place(x=300,y=310)
  CD4 = Button(frameB,text="D4",command=D4,bg="Blue")
  CD4.place(x=350,y=310)
  CD5 = Button(frameB,text="D5",command=D5,bg="Blue")
  CD5.place(x=400,y=310)
  CD6 = Button(frameB,text="D6",command=D6,bg="Blue")
  CD6.place(x=450,y=310)
  CD7 = Button(frameB,text="D7",command=D7,bg="Blue")
  CD7.place(x=500,y=310)
  CD8 = Button(frameB,text="D8",command=D8,bg="Blue")
  CD8.place(x=550,y=310)

  CE1 = Button(frameB,text="E1",command=E1,bg="Blue")
  CE1.place(x=200,y=340)
  CE2 = Button(frameB,text="E2",command=E2,bg="Blue")
  CE2.place(x=250,y=340)
  CE3 = Button(frameB,text="E3",command=E3,bg="Blue")
  CE3.place(x=300,y=340)
  CE4 = Button(frameB,text="E4",command=E4,bg="Blue")
  CE4.place(x=350,y=340)
  CE5 = Button(frameB,text="E5",command=E5,bg="Blue")
  CE5.place(x=400,y=340)
  CE6 = Button(frameB,text="E6",command=E6,bg="Blue")
  CE6.place(x=450,y=340)
  CE7 = Button(frameB,text="E7",command=E7,bg="Blue")
  CE7.place(x=500,y=340)
  CE8 = Button(frameB,text="E8",command=E8,bg="Blue")
  CE8.place(x=550,y=340)

  CF1 = Button(frameB,text="F1",command=F1,bg="Blue")
  CF1.place(x=200,y=370)
  CF2 = Button(frameB,text="F2",command=F2,bg="Blue")
  CF2.place(x=250,y=370)
  CF3 = Button(frameB,text="F3",command=F3,bg="Blue")
  CF3.place(x=300,y=370)
  CF4 = Button(frameB,text="F4",command=F4,bg="Blue")
  CF4.place(x=350,y=370)
  CF5 = Button(frameB,text="F5",command=F5,bg="Blue")
  CF5.place(x=400,y=370) 
  CF6 = Button(frameB,text="F6",command=F6,bg="Blue")
  CF6.place(x=450,y=370)
  CF7 = Button(frameB,text="F7",command=F7,bg="Blue")
  CF7.place(x=500,y=370)
  CF8 = Button(frameB,text="F8",command=F8,bg="Blue")
  CF8.place(x=550,y=370)
  
  CG1 = Button(frameB,text="G1",command=G1,bg="Blue")
  CG1.place(x=200,y=400)
  CG2 = Button(frameB,text="G2",command=G2,bg="Blue")
  CG2.place(x=250,y=400)
  CG3 = Button(frameB,text="G3",command=G3,bg="Blue")
  CG3.place(x=300,y=400)
  CG4 = Button(frameB,text="G4",command=G4,bg="Blue")
  CG4.place(x=350,y=400)
  CG5 = Button(frameB,text="G5",command=G5,bg="Blue")
  CG5.place(x=400,y=400)
  CG6 = Button(frameB,text="G6",command=G6,bg="Blue")
  CG6.place(x=450,y=400)
  CG7 = Button(frameB,text="G7",command=G7,bg="Blue")
  CG7.place(x=500,y=400)
  CG8 = Button(frameB,text="G8",command=G8,bg="Blue")
  CG8.place(x=550,y=400)

  CH1 = Button(frameB,text="H1",command=H1,bg="Blue")
  CH1.place(x=200,y=430)
  CH2 = Button(frameB,text="H2",command=H2,bg="Blue")
  CH2.place(x=250,y=430)
  CH3 = Button(frameB,text="H3",command=H3,bg="Blue")
  CH3.place(x=300,y=430)
  CH4 = Button(frameB,text="H4",command=H4,bg="Blue")
  CH4.place(x=350,y=430)
  CH5 = Button(frameB,text="H5",command=H5,bg="Blue")
  CH5.place(x=400,y=430)
  CH6 = Button(frameB,text="H6",command=H6,bg="Blue")
  CH6.place(x=450,y=430)
  CH7 = Button(frameB,text="H7",command=H7,bg="Blue")
  CH7.place(x=500,y=430)
  CH8 = Button(frameB,text="H8",command=H8,bg="Blue")
  CH8.place(x=550,y=430)

  def back():
    frameB.destroy()

  def Balidar():
    if len(fl.Lasiento) == int(numP.get()):
        comida() 
    else:
       messagebox.showinfo("Error","Seleccione la cantidad correcta de campos")

  Button(frameB,text="siguiente",command=Balidar).place(x=400,y=465)
  Button(frameB,text="Atras",command=back).place(x=350,y=465)



def Uncharted():
  frameU = Frame(windowsFrame1,width=900,height=500)
  frameU.place(x=0,y=0)

  fl.TipoPelicula = "Uncharted"
  fl.Lasiento.clear()
  
  #imajen de fondo de---------------------------
  Label(frameU,image=fondo).place(x=0,y=0)
  #----------------------------------------------
    
  Label(frameU,text="Tanda",bg="#CDC2BF",font=("Arial",45),).place(x=350,y=0)

  comboF=ttk.Combobox(frameU,value=["Dia","15/04","17/04","19/04","20/04"],state="readonly",justify=CENTER,textvariable=DiaF)
  comboF.current(0)
  comboF.place(x=20,y=70)
  
  comboH = ttk.Combobox(frameU,value=["Hora","2:30","5:00","8:00","8:30"],state="readonly",justify=CENTER,textvariable=HoraF)
  comboH.current(0)
  comboH.place(x=170,y=70)
   
  numP = Entry(frameU,width=23,justify=CENTER,textvariable=NumF)
  numP.insert(0,"Numero de personas")
  numP.place(x=20,y=100)

  Checkbutton(frameU,bg="#CDC2BF",text="Modo covid",variable=CovidF).place(x=170,y=99)

  def A1():
    global NA1
    if NA1 == 0:
      CA1.config(bg="Red")
      NA1 = 1
      fl.Lasiento.append("A1")
    else:
      CA1.config(bg="Blue")
      NA1 = 0
      fl.Lasiento.remove("A1")

  def A2():
    global NA2
    if NA2 == 0:
      CA2.config(bg="Red")
      NA2 = 1
      fl.Lasiento.append("A2")
    else:
      CA2.config(bg="Blue")
      NA2 = 0
      fl.Lasiento.remove("A2")
 
  def A3():
    global NA3
    if NA3 == 0:
       CA3.config(bg="Red")
       NA3 = 1
       fl.Lasiento.append("A3")
    else:
      CA3.config(bg="Blue")
      NA3 = 0
      fl.Lasiento.remove("A3")

  def A4():
    global NA4
    if NA4 == 0: 
       CA4.config(bg="Red")
       NA4 = 1
       fl.Lasiento.append("A4")
    else:
      CA4.config(bg="Blue")
      NA4 = 0
      fl.Lasiento.remove("A4")

  def A5():
    global NA5
    if NA5 == 0: 
       CA5.config(bg="Red")
       NA5 = 1
       fl.Lasiento.append("A5")
    else:
      CA5.config(bg="Blue")
      NA5 = 0 
      fl.Lasiento.remove("A5")

  def A6():
    global NA6
    if NA6 == 0: 
       CA6.config(bg="Red")
       NA6 = 1
       fl.Lasiento.append("A6")
    else:
      CA6.config(bg="Blue")
      NA6 = 0
      fl.Lasiento.remove("A6")

  def A7():
    global NA7 
    if  NA7 == 0: 
        CA7.config(bg="Red")
        NA7 = 1
        fl.Lasiento.append("A7")
    else: 
      CA7.config(bg="Blue")
      NA7 = 0
      fl.Lasiento.remove("A7")

  def A8():
    global NA8
    if NA8 == 0:
       CA8.config(bg="Red")
       NA8 = 1
       fl.Lasiento.append("A8")
    else:
      CA8.config(bg="Blue")
      NA8 = 0
      fl.Lasiento.remove("A8")
  
  def B1():
    global NB1
    if NB1 == 0:
       CB1.config(bg="Red")
       NB1 = 1
       fl.Lasiento.append("B1")
    else:
      CB1.config(bg="Blue")
      NB1 = 0
      fl.Lasiento.remove("B1")
    
  def B2():
    global NB2
    if NB2 == 0:
       CB2.config(bg="Red")
       NB2 = 1
       fl.Lasiento.append("B2")
    else:
      CB2.config(bg="Blue")
      NB2 = 0
      fl .Lasiento.remove("B2")

  def B3():
    global NB3
    if NB3 == 0:
       CB3.config(bg="Red")
       NB3 = 1
       fl.Lasiento.append("B3")
    else:
      CB3.config(bg="Blue")
      NB3 = 0
      fl .Lasiento.remove("B3")

  def B4():
    global NB4
    if NB4 == 0:
      CB4.config(bg="Red")
      NB4 = 1
      fl.Lasiento.append("B4")
    else:
      CB4.config(bg="Blue")
      NB4 = 0
      fl.Lasiento.remove("B4")
  
  def B5():
    global NB5
    if NB5 == 0:
       CB5.config(bg="Red")
       NB5 = 1
       fl.Lasiento.append("B5")
    else:
      CB5.config(bg="Blue")
      NB5 = 0
      fl.Lasiento.remove("B5")

  def B6():
    global NB6
    if NB6 == 0:
       CB6.config(bg="Red")
       NB6 = 1
       fl.Lasiento.append("B6")
    else:
      CB6.config(bg="Blue")
      NB6 = 0
      fl.Lasiento.remove("B6")

  def B7():
    global NB7
    if NB7 == 0:
       CB7.config(bg="Red")
       NB7 = 1
       fl.Lasiento.append("B7")
    else:
      CB7.config(bg="Blue")
      NB7 = 0
      fl.Lasiento.remove("B7")

  def B8():
    global NB8
    if NB8 == 0:
       CB8.config(bg="Red")
       NB8 = 1
       fl.Lasiento.append("B8")
    else:
      CB8.config(bg="Blue")
      NB8 = 0
      fl.Lasiento.remove("B8")

  def C1():
    global NC1
    if NC1 == 0:
        CC1.config(bg="Red")
        NC1 = 1
        fl.Lasiento.append("C1")
    else:
      CC1.config(bg="Blue")
      NC1 = 0
      fl.Lasiento.remove("C2")

  def C2():
    global NC2
    if NC2 == 0:
      CC2.config(bg="Red")
      NC2 = 1
      fl.Lasiento.append("C3")
    else:
      CC2.config(bg="Blue")
      NC2 = 0
      fl.Lasiento.remove("C3")

  def C3():
    global NC3
    if NC3 == 0:
       CC3.config(bg="Red")
       NC3 = 1
       fl.Lasiento.append("C3")
    else:
      CC3.config(bg="Blue")
      NC3 = 0
      fl.Lasiento.append("C3")

  def C4():
    global NC4
    if NC4 == 0:
      CC4.config(bg="Red")
      NC4 = 1
      fl.Lasiento.append("C4")
    else:
      CC4.config(bg="Blue")
      NC4 = 0
      fl.Lasiento.append("C4")

  def C5():
    global NC5
    if NC5 == 0:
        CC5.config(bg="Red")
        NC5 = 1
        fl.Lasiento.append("C5")
    else:
      CC5.config(bg="Blue")
      NC5 = 0
      fl.Lasiento.remove("C5")

  def C6():
    global NC6
    if NC6 == 0:
      CC6.config(bg="Red")
      NC6 = 1
      fl.Lasiento.append("C6")
    else:
      CC6.config(bg="Blue")
      NC6 = 0
      fl.Lasiento.remove("C6")

  def C7():
    global NC7
    if NC7 == 0:
       CC7.config(bg="Red")
       NC7 = 1
       fl.Lasiento.append("C7")
    else:
      CC7.config(bg="Blue")
      NC7 = 0
      fl.Lasiento.remove("C7")

  def C8():
    global NC8
    if NC8 == 0:
       CC8.config(bg="Red")
       NC8 = 1
       fl.Lasiento.append("C8")
    else:
      CC8.config(bg="Blue")
      NC8 = 0
      fl.Lasiento.remove("C8")

  def D1():
    global ND1
    if ND1 == 0:
      CD1.config(bg="Red")
      ND1 = 1
      fl.Lasiento.append("D1")
    else:
      CD1.config(bg="Blue")
      ND1 = 0
      fl.Lasiento.remove("D1")

  def D2():
    global ND2
    if ND2 == 0:
       CD2.config(bg="Red")
       ND2 = 1
       fl.Lasiento.append("D2")
    else:
      CD2.config(bg="Blue")
      ND2 = 0
      fl.Lasiento.remove("D2")

  def D3():
    global ND3
    if ND3 == 0:
        CD3.config(bg="Red")
        ND3 = 1
        fl.Lasiento.append("D3")
    else:
      CD3.config(bg="Blue")
      ND3 = 0
      fl.Lasiento.remove("D3")

  def D4():
    global ND4
    if ND4 == 0:
      CD4.config(bg="Red")
      ND4 = 1
      fl.Lasiento.append("D4")
    else:
      CD4.config(bg="Blue")
      ND4 = 0
      fl.Lasiento.remove("D4")

  def D5():
    global ND5
    if ND5 == 0:
       CD5.config(bg="Red")
       ND5 = 1 
       fl.Lasiento.append("D5")
    else:
      CD5.config(bg="Blue")
      ND5 = 0
      fl.Lasiento.remove("D5")

  def D6():
    global ND6
    if ND6 == 0:
      CD6.config(bg="Red")
      ND6 = 1 
      fl.Lasiento.append("D6")
    else:
      CD6.config(bg="Blue")
      ND6 = 0
      fl.Lasiento.remove("D6")

  def D7():
    global ND7
    if ND7 == 0:
      CD7.config(bg="Red")
      ND7 = 1
      fl.Lasiento.append("D7")
    else:
      CD7.config(bg="Blue")
      ND7 = 0
      fl.Lasiento.remove("D7")

  def D8():
    global ND8
    if ND8 == 0:
      CD8.config(bg="Red")
      ND8 = 1
      fl.Lasiento.append("D8")
    else:
      CD8.config(bg="Blue")
      ND8 = 0
      fl.Lasiento.remove("D8")

  def E1():
    global NE1
    if NE1 == 0:
       CE1.config(bg="Red")
       NE1 = 1
       fl.Lasiento.append("E1")
    else:
      CE1.config(bg="Blue")
      NE1 = 0
      fl.Lasiento.remove("E1")

  def E2():
    global NE2
    if NE2 == 0:
      CE2.config(bg="Red")
      NE2 = 1
      fl.Lasiento.append("E2")
    else:
      CE2.config(bg="Blue")
      NE2 = 0
      fl.Lasiento.remove("E2")

  def E3():
    global NE3
    if NE3 == 0:
      CE3.config(bg="Red")
      NE3 = 1
      fl.Lasiento.append("E3")
    else:
      CE3.config(bg="Blue")
      NE3 = 0
      fl.Lasiento.remove("E3")

  def E4():
    global NE4
    if NE4 == 0:
      CE4.config(bg="Red")
      NE4 = 1
    else:
      CE4.config(bg="Blue")
      NE4 = 0
      fl.Lasiento.remove("E4")

  def E5():
    global NE5
    if NE5 == 0:
      CE5.config(bg="Red")
      NE5 = 1 
      fl.Lasiento.append("E5")
    else:
      CE5.config(bg="Blue")
      NE5 = 0
      fl.Lasiento.remove("E5")

  def E6():
    global NE6
    if NE6 == 0:
       CE6.config(bg="Red")
       NE6 = 1
       fl.Lasiento.append("E6")
    else:
      CE6.config(bg="Blue")
      NE6 = 0
      fl.Lasiento.remove("E6")

  def E7():
    global NE7
    if NE7 == 0:
      CE7.config(bg="Red")
      NE7 = 1
      fl.Lasiento.append("E7")
    else:
      CE7.config(bg="Blue")
      NE7 = 0
      fl.Lasiento.remove("E7")

  def E8():
    global NE8
    if NE8 == 0:
      CE8.config(bg="Red")
      NE8 = 1
      fl.Lasiento.append("E8")
    else:
      CE8.config(bg="Blue")
      NE8 = 0
      fl.Lasiento.remove("E8")

  def F1():
    global NF1
    if NF1 == 0:
      CF1.config(bg="Red")
      NF1 = 1
      fl.Lasiento.append("F1")
    else:
      CF1.config(bg="Blue")
      NF1 = 0
      fl.Lasiento.remove("F1")

  def F2():
    global NF2
    if NF2 == 0:
      CF2.config(bg="Red")
      NF2 = 1
      fl.Lasiento.append("F2")
    else:
      CF3.config(bg="Blue")
      NF2 = 0
      fl.Lasiento.remove("F2")

  def F3():
    global NF3
    if NF3 == 0:
      CF3.config(bg="Red")
      NF3 = 1
      fl.Lasiento.append("F3")

  def F4():
    global NF4
    if NF4 == 0:
      CF4.config(bg="Red")
      NF4 = 1
      fl.Lasiento.append("F4")
    else:
      CF4.config(bg="Blue")
      NF4 = 0
      fl.Lasiento.append("F4")

  def F5():
    global NF5
    if NF5 == 0:
      CF5.config(bg="Red")
      NF5 = 1
      fl.Lasiento.append("F5")
    else:
      CF5.config(bg="Blue")
      NF5 = 0
      fl.Lasiento.remove("F5")

  def F6():
    global NF6
    if NF6 == 0:
      CF6.config(bg="Red")
      NF6 = 1
      fl.Lasiento.append("F6")
    else:
      CF6.config(bg="Blue")
      NF6 = 0
      fl.Lasiento.remove("F6")

  def F7():
    global NF7
    if NF7 == 0:
      CF7.config(bg="Red")
      NF7 = 1
      fl.Lasiento.append("F7")
    else:
      CF7.config(bg="Blue")
      NF7 = 0
      fl.Lasiento.remove("F7")

  def F8():
    global NF8
    if NF8 == 0:
      CF8.config(bg="Red")
      NF8 = 1
      fl.Lasiento.append("F8")
    else:
      CF8.config(bg="Blue")
      NF8 = 0
      fl.Lasiento.remove("F8")

  def G1():
    global NG1
    if NG1 == 0:
      CG1.config(bg="Red")
      NG1 = 1
      fl.Lasiento.append("G1")
    else:
      CG1.config(bg="Blue")
      NG1 = 0
      fl.Lasiento.remove("G1")

  def G2():
    global NG2
    if NG2 == 0:
      CG2.config(bg="Red")
      NG2 = 1
      fl.Lasiento.append("G2")
    else:
      CG2.config(bg="Blue")
      NG2 = 0
      fl.Lasiento.remove("G2")

  def G3():
    global  NG3
    if NG3 == 0:
      CG3.config(bg="Red")
      NG3 = 1
      fl.Lasiento.append("G3")
    else:
      CG3.config(bg="Blue")
      NG3 = 0
      fl.Lasiento.remove("G3")

  def G4():
    global NG4
    if NG4 == 0:
      CG4.config(bg="Red")
      NG4 = 1
      fl.Lasiento.append("G4")
    else:
      CG4.config(bg="Blue")
      NG4 = 0
      fl.Lasiento.remove("G4")

  def G5():
    global NG5
    if NG5 == 0:
      CG5.config(bg="Red")
      NG5 = 1
      fl.Lasiento.append("G5")
    else:
      CG5.config(bg="Blue")
      NG5 = 0
      fl.Lasiento.remove("G5")

  def G6():
    global NG6
    if NG6 == 0:
      CG6.config(bg="Red")
      NG6 = 1
      fl.Lasiento.append("G6")
    else:
      CG6.config(bg="Blue")
      NG6 = 0
      fl.Lasiento.remove("G6")

  def G7():
    global NG7
    if NG7 == 0:
      CG7.config(bg="Red")
      NG7 = 1
      fl.Lasiento.append("G7")
    else:
      CG7.config(bg="Blue")
      NG7 = 0
      fl.Lasiento.remove("G7")

  def G8():
    global NG8
    if NG8 == 0:
      CG8.config(bg="Red")
      NG8 = 1
      fl.Lasiento.append("G8")
    else:
      CG8.config(bg="Blue")
      NG8 = 0
      fl.Lasiento.remove("G8")

  def H1():
    global NH1
    if NH1 == 0:
      CH1.config(bg="Red")
      NH1 = 1
      fl.Lasiento.append("H1")
    else:
      CG1.config(bg="Blue")
      NH1 = 0
      fl.Lasiento.remove("H1")

  def H2():
    global NH2
    if NH2 == 0:
      CH2.config(bg="Red")
      NH2 = 1
      fl.Lasiento.append("H2")
    else:
      CG2.config(bg="Blue")
      NH2 = 0
      fl.Lasiento.remove("H2")

  def H3():
    global NH3
    if NH3 == 0:
      CH3.config(bg="Red")
      NH3 = 1
      fl.Lasiento.append("H3")
    else:
      CH3.config(bg="Blue")
      NH3 = 0
      fl.Lasiento.remove("H3")

  def H4():
    global NH4
    if NH4 == 0:
      CH4.config(bg="Red")
      NH4 = 1
      fl.Lasiento.append("H4")
    else:
      CH4.config(bg="Blue")
      NH4 = 0
      fl.Lasiento.remove("H4")

  def H5():
    global NH5
    if NH5 == 0:
      CH5.config(bg="Red")
      NH5 = 1
      fl.Lasiento.append("H5")
    else:
      CH5.config(bg="Blue")
      NH5 = 0 
      fl.Lasiento.remove("H5")

  def H6():
    global NH6
    if NH6 == 0:
      CH6.config(bg="Red")
      NH6 = 1
      fl.Lasiento.append("H6")
    else:
      CH6.config(bg="Blue")
      NH6 = 0 
      fl.Lasiento.remove("H6")

  def H7():
    global NH7
    if NH7 == 0:
      CH7.config(bg="Red")
      NH7 = 1
      fl.Lasiento.append("H7")
    else:
      CH7.config(bg="Blue")
      NH7 = 0
      fl.Lasiento.remove("H7")

  def H8():
    global NH8 
    if NH8 == 0:
      CH8.config(bg="Red")
      NH8 = 1
      fl.Lasiento.append("H8")
    else:
      CH8.config(bg="Blue")
      NH8 = 0
      fl.Lasiento.remove("H8")

  Label(frameU,bg="Black",width=53,height=1).place(x=200,y=190)
   
  CA1 = Button(frameU,text="A1",command=A1,bg="Blue")
  CA1.place(x=200,y=220)
  CA2 = Button(frameU,text="A2",command=A2,bg="Blue")
  CA2.place(x=250,y=220)
  CA3 = Button(frameU,text="A3",command=A3,bg="Blue")
  CA3.place(x=300,y=220)
  CA4 = Button(frameU,text="A4",command=A4,bg="Blue")
  CA4.place(x=350,y=220)
  CA5 = Button(frameU,text="A5",command=A5,bg="Blue")
  CA5.place(x=400,y=220)
  CA6 = Button(frameU,text="A6",command=A6,bg="Blue")
  CA6.place(x=450,y=220)
  CA7 = Button(frameU,text="A7",command=A7,bg="Blue")
  CA7.place(x=500,y=220)
  CA8 = Button(frameU,text="A8",command=A8,bg="Blue")
  CA8.place(x=550,y=220)

  CB1 = Button(frameU,text="B1",command=B1,bg="Blue")
  CB1.place(x=200,y=250)
  CB2 = Button(frameU,text="B2",command=B2,bg="Blue")
  CB2.place(x=250,y=250)
  CB3 = Button(frameU,text="B3",command=B3,bg="Blue")
  CB3.place(x=300,y=250)
  CB4 = Button(frameU,text="B4",command=B4,bg="Blue")
  CB4.place(x=350,y=250)
  CB5 = Button(frameU,text="B5",command=B5,bg="Blue")
  CB5.place(x=400,y=250)
  CB6 = Button(frameU,text="B6",command=B6,bg="Blue")
  CB6.place(x=450,y=250)
  CB7 = Button(frameU,text="B7",command=B7,bg="Blue")
  CB7.place(x=500,y=250)
  CB8 = Button(frameU,text="B8",command=B8,bg="Blue")
  CB8.place(x=550,y=250)

  CC1 = Button(frameU,text="C1",command=C1,bg="Blue")
  CC1.place(x=200,y=280)
  CC2 = Button(frameU,text="C2",command=C2,bg="Blue")
  CC2.place(x=250,y=280)
  CC3 = Button(frameU,text="C3",command=C3,bg="Blue")
  CC3.place(x=300,y=280)
  CC4 = Button(frameU,text="C4",command=C4,bg="Blue")
  CC4.place(x=350,y=280)
  CC5 = Button(frameU,text="C5",command=C5,bg="Blue")
  CC5.place(x=400,y=280)
  CC6 = Button(frameU,text="C6",command=C6,bg="Blue")
  CC6.place(x=450,y=280)
  CC7 = Button(frameU,text="C7",command=C7,bg="Blue")
  CC7.place(x=500,y=280)
  CC8 = Button(frameU,text="C8",command=C8,bg="Blue")
  CC8.place(x=550,y=280)

  CD1 = Button(frameU,text="D1",command=D1,bg="Blue")
  CD1.place(x=200,y=310)
  CD2 = Button(frameU,text="D2",command=D2,bg="Blue")
  CD2.place(x=250,y=310)
  CD3 = Button(frameU,text="D3",command=D3,bg="Blue")
  CD3.place(x=300,y=310)
  CD4 = Button(frameU,text="D4",command=D4,bg="Blue")
  CD4.place(x=350,y=310)
  CD5 = Button(frameU,text="D5",command=D5,bg="Blue")
  CD5.place(x=400,y=310)
  CD6 = Button(frameU,text="D6",command=D6,bg="Blue")
  CD6.place(x=450,y=310)
  CD7 = Button(frameU,text="D7",command=D7,bg="Blue")
  CD7.place(x=500,y=310)
  CD8 = Button(frameU,text="D8",command=D8,bg="Blue")
  CD8.place(x=550,y=310)

  CE1 = Button(frameU,text="E1",command=E1,bg="Blue")
  CE1.place(x=200,y=340)
  CE2 = Button(frameU,text="E2",command=E2,bg="Blue")
  CE2.place(x=250,y=340)
  CE3 = Button(frameU,text="E3",command=E3,bg="Blue")
  CE3.place(x=300,y=340)
  CE4 = Button(frameU,text="E4",command=E4,bg="Blue")
  CE4.place(x=350,y=340)
  CE5 = Button(frameU,text="E5",command=E5,bg="Blue")
  CE5.place(x=400,y=340)
  CE6 = Button(frameU,text="E6",command=E6,bg="Blue")
  CE6.place(x=450,y=340)
  CE7 = Button(frameU,text="E7",command=E7,bg="Blue")
  CE7.place(x=500,y=340)
  CE8 = Button(frameU,text="E8",command=E8,bg="Blue")
  CE8.place(x=550,y=340)

  CF1 = Button(frameU,text="F1",command=F1,bg="Blue")
  CF1.place(x=200,y=370)
  CF2 = Button(frameU,text="F2",command=F2,bg="Blue")
  CF2.place(x=250,y=370)
  CF3 = Button(frameU,text="F3",command=F3,bg="Blue")
  CF3.place(x=300,y=370)
  CF4 = Button(frameU,text="F4",command=F4,bg="Blue")
  CF4.place(x=350,y=370)
  CF5 = Button(frameU,text="F5",command=F5,bg="Blue")
  CF5.place(x=400,y=370) 
  CF6 = Button(frameU,text="F6",command=F6,bg="Blue")
  CF6.place(x=450,y=370)
  CF7 = Button(frameU,text="F7",command=F7,bg="Blue")
  CF7.place(x=500,y=370)
  CF8 = Button(frameU,text="F8",command=F8,bg="Blue")
  CF8.place(x=550,y=370)
  
  CG1 = Button(frameU,text="G1",command=G1,bg="Blue")
  CG1.place(x=200,y=400)
  CG2 = Button(frameU,text="G2",command=G2,bg="Blue")
  CG2.place(x=250,y=400)
  CG3 = Button(frameU,text="G3",command=G3,bg="Blue")
  CG3.place(x=300,y=400)
  CG4 = Button(frameU,text="G4",command=G4,bg="Blue")
  CG4.place(x=350,y=400)
  CG5 = Button(frameU,text="G5",command=G5,bg="Blue")
  CG5.place(x=400,y=400)
  CG6 = Button(frameU,text="G6",command=G6,bg="Blue")
  CG6.place(x=450,y=400)
  CG7 = Button(frameU,text="G7",command=G7,bg="Blue")
  CG7.place(x=500,y=400)
  CG8 = Button(frameU,text="G8",command=G8,bg="Blue")
  CG8.place(x=550,y=400)

  CH1 = Button(frameU,text="H1",command=H1,bg="Blue")
  CH1.place(x=200,y=430)
  CH2 = Button(frameU,text="H2",command=H2,bg="Blue")
  CH2.place(x=250,y=430)
  CH3 = Button(frameU,text="H3",command=H3,bg="Blue")
  CH3.place(x=300,y=430)
  CH4 = Button(frameU,text="H4",command=H4,bg="Blue")
  CH4.place(x=350,y=430)
  CH5 = Button(frameU,text="H5",command=H5,bg="Blue")
  CH5.place(x=400,y=430)
  CH6 = Button(frameU,text="H6",command=H6,bg="Blue")
  CH6.place(x=450,y=430)
  CH7 = Button(frameU,text="H7",command=H7,bg="Blue")
  CH7.place(x=500,y=430)
  CH8 = Button(frameU,text="H8",command=H8,bg="Blue")
  CH8.place(x=550,y=430)

  def back():
    frameU.destroy()

  def Balidar():
    if len(fl.Lasiento) == int(numP.get()):
        comida() 
    else:
       messagebox.showinfo("Error","Seleccione la cantidad correcta de campos")

  Button(frameU,text="siguiente",command=Balidar).place(x=400,y=465)
  Button(frameU,text="Atras",command=back).place(x=350,y=465)

def Morvious():
  frameM = Frame(windowsFrame1,width=900,height=500)
  frameM.place(x=0,y=0)

  fl.TipoPelicula = "Morvious"
  fl.Lasiento.clear()
  
  #imajen de fondo de---------------------------
  Label(frameM,image=fondo).place(x=0,y=0)
  #----------------------------------------------
    
  Label(frameM,text="Tanda",bg="#CDC2BF",font=("Arial",45),).place(x=350,y=0)

  comboF=ttk.Combobox(frameM,value=["Dia","15/04","17/04","19/04","20/04"],state="readonly",justify=CENTER,textvariable=DiaF)
  comboF.current(0)
  comboF.place(x=20,y=70)
  
  comboH = ttk.Combobox(frameM,value=["Hora","2:30","5:00","8:00","8:30"],state="readonly",justify=CENTER,textvariable=HoraF)
  comboH.current(0)
  comboH.place(x=170,y=70)
   
  numP = Entry(frameM,width=23,justify=CENTER,textvariable=NumF)
  numP.insert(0,"Numero de personas")
  numP.place(x=20,y=100)

  Checkbutton(frameM,bg="#CDC2BF",text="Modo covid",variable=CovidF).place(x=170,y=99)

  def A1():
    global NA1
    if NA1 == 0:
      CA1.config(bg="Red")
      NA1 = 1
      fl.Lasiento.append("A1")
    else:
      CA1.config(bg="Blue")
      NA1 = 0
      fl.Lasiento.remove("A1")

  def A2():
    global NA2
    if NA2 == 0:
      CA2.config(bg="Red")
      NA2 = 1
      fl.Lasiento.append("A2")
    else:
      CA2.config(bg="Blue")
      NA2 = 0
      fl.Lasiento.remove("A2")
 
  def A3():
    global NA3
    if NA3 == 0:
       CA3.config(bg="Red")
       NA3 = 1
       fl.Lasiento.append("A3")
    else:
      CA3.config(bg="Blue")
      NA3 = 0
      fl.Lasiento.remove("A3")

  def A4():
    global NA4
    if NA4 == 0: 
       CA4.config(bg="Red")
       NA4 = 1
       fl.Lasiento.append("A4")
    else:
      CA4.config(bg="Blue")
      NA4 = 0
      fl.Lasiento.remove("A4")

  def A5():
    global NA5
    if NA5 == 0: 
       CA5.config(bg="Red")
       NA5 = 1
       fl.Lasiento.append("A5")
    else:
      CA5.config(bg="Blue")
      NA5 = 0 
      fl.Lasiento.remove("A5")

  def A6():
    global NA6
    if NA6 == 0: 
       CA6.config(bg="Red")
       NA6 = 1
       fl.Lasiento.append("A6")
    else:
      CA6.config(bg="Blue")
      NA6 = 0
      fl.Lasiento.remove("A6")

  def A7():
    global NA7 
    if  NA7 == 0: 
        CA7.config(bg="Red")
        NA7 = 1
        fl.Lasiento.append("A7")
    else: 
      CA7.config(bg="Blue")
      NA7 = 0
      fl.Lasiento.remove("A7")

  def A8():
    global NA8
    if NA8 == 0:
       CA8.config(bg="Red")
       NA8 = 1
       fl.Lasiento.append("A8")
    else:
      CA8.config(bg="Blue")
      NA8 = 0
      fl.Lasiento.remove("A8")
  
  def B1():
    global NB1
    if NB1 == 0:
       CB1.config(bg="Red")
       NB1 = 1
       fl.Lasiento.append("B1")
    else:
      CB1.config(bg="Blue")
      NB1 = 0
      fl.Lasiento.remove("B1")
    
  def B2():
    global NB2
    if NB2 == 0:
       CB2.config(bg="Red")
       NB2 = 1
       fl.Lasiento.append("B2")
    else:
      CB2.config(bg="Blue")
      NB2 = 0
      fl .Lasiento.remove("B2")

  def B3():
    global NB3
    if NB3 == 0:
       CB3.config(bg="Red")
       NB3 = 1
       fl.Lasiento.append("B3")
    else:
      CB3.config(bg="Blue")
      NB3 = 0
      fl .Lasiento.remove("B3")

  def B4():
    global NB4
    if NB4 == 0:
      CB4.config(bg="Red")
      NB4 = 1
      fl.Lasiento.append("B4")
    else:
      CB4.config(bg="Blue")
      NB4 = 0
      fl.Lasiento.remove("B4")
  
  def B5():
    global NB5
    if NB5 == 0:
       CB5.config(bg="Red")
       NB5 = 1
       fl.Lasiento.append("B5")
    else:
      CB5.config(bg="Blue")
      NB5 = 0
      fl.Lasiento.remove("B5")

  def B6():
    global NB6
    if NB6 == 0:
       CB6.config(bg="Red")
       NB6 = 1
       fl.Lasiento.append("B6")
    else:
      CB6.config(bg="Blue")
      NB6 = 0
      fl.Lasiento.remove("B6")

  def B7():
    global NB7
    if NB7 == 0:
       CB7.config(bg="Red")
       NB7 = 1
       fl.Lasiento.append("B7")
    else:
      CB7.config(bg="Blue")
      NB7 = 0
      fl.Lasiento.remove("B7")

  def B8():
    global NB8
    if NB8 == 0:
       CB8.config(bg="Red")
       NB8 = 1
       fl.Lasiento.append("B8")
    else:
      CB8.config(bg="Blue")
      NB8 = 0
      fl.Lasiento.remove("B8")

  def C1():
    global NC1
    if NC1 == 0:
        CC1.config(bg="Red")
        NC1 = 1
        fl.Lasiento.append("C1")
    else:
      CC1.config(bg="Blue")
      NC1 = 0
      fl.Lasiento.remove("C2")

  def C2():
    global NC2
    if NC2 == 0:
      CC2.config(bg="Red")
      NC2 = 1
      fl.Lasiento.append("C3")
    else:
      CC2.config(bg="Blue")
      NC2 = 0
      fl.Lasiento.remove("C3")

  def C3():
    global NC3
    if NC3 == 0:
       CC3.config(bg="Red")
       NC3 = 1
       fl.Lasiento.append("C3")
    else:
      CC3.config(bg="Blue")
      NC3 = 0
      fl.Lasiento.append("C3")

  def C4():
    global NC4
    if NC4 == 0:
      CC4.config(bg="Red")
      NC4 = 1
      fl.Lasiento.append("C4")
    else:
      CC4.config(bg="Blue")
      NC4 = 0
      fl.Lasiento.append("C4")

  def C5():
    global NC5
    if NC5 == 0:
        CC5.config(bg="Red")
        NC5 = 1
        fl.Lasiento.append("C5")
    else:
      CC5.config(bg="Blue")
      NC5 = 0
      fl.Lasiento.remove("C5")

  def C6():
    global NC6
    if NC6 == 0:
      CC6.config(bg="Red")
      NC6 = 1
      fl.Lasiento.append("C6")
    else:
      CC6.config(bg="Blue")
      NC6 = 0
      fl.Lasiento.remove("C6")

  def C7():
    global NC7
    if NC7 == 0:
       CC7.config(bg="Red")
       NC7 = 1
       fl.Lasiento.append("C7")
    else:
      CC7.config(bg="Blue")
      NC7 = 0
      fl.Lasiento.remove("C7")

  def C8():
    global NC8
    if NC8 == 0:
       CC8.config(bg="Red")
       NC8 = 1
       fl.Lasiento.append("C8")
    else:
      CC8.config(bg="Blue")
      NC8 = 0
      fl.Lasiento.remove("C8")

  def D1():
    global ND1
    if ND1 == 0:
      CD1.config(bg="Red")
      ND1 = 1
      fl.Lasiento.append("D1")
    else:
      CD1.config(bg="Blue")
      ND1 = 0
      fl.Lasiento.remove("D1")

  def D2():
    global ND2
    if ND2 == 0:
       CD2.config(bg="Red")
       ND2 = 1
       fl.Lasiento.append("D2")
    else:
      CD2.config(bg="Blue")
      ND2 = 0
      fl.Lasiento.remove("D2")

  def D3():
    global ND3
    if ND3 == 0:
        CD3.config(bg="Red")
        ND3 = 1
        fl.Lasiento.append("D3")
    else:
      CD3.config(bg="Blue")
      ND3 = 0
      fl.Lasiento.remove("D3")

  def D4():
    global ND4
    if ND4 == 0:
      CD4.config(bg="Red")
      ND4 = 1
      fl.Lasiento.append("D4")
    else:
      CD4.config(bg="Blue")
      ND4 = 0
      fl.Lasiento.remove("D4")

  def D5():
    global ND5
    if ND5 == 0:
       CD5.config(bg="Red")
       ND5 = 1 
       fl.Lasiento.append("D5")
    else:
      CD5.config(bg="Blue")
      ND5 = 0
      fl.Lasiento.remove("D5")

  def D6():
    global ND6
    if ND6 == 0:
      CD6.config(bg="Red")
      ND6 = 1 
      fl.Lasiento.append("D6")
    else:
      CD6.config(bg="Blue")
      ND6 = 0
      fl.Lasiento.remove("D6")

  def D7():
    global ND7
    if ND7 == 0:
      CD7.config(bg="Red")
      ND7 = 1
      fl.Lasiento.append("D7")
    else:
      CD7.config(bg="Blue")
      ND7 = 0
      fl.Lasiento.remove("D7")

  def D8():
    global ND8
    if ND8 == 0:
      CD8.config(bg="Red")
      ND8 = 1
      fl.Lasiento.append("D8")
    else:
      CD8.config(bg="Blue")
      ND8 = 0
      fl.Lasiento.remove("D8")

  def E1():
    global NE1
    if NE1 == 0:
       CE1.config(bg="Red")
       NE1 = 1
       fl.Lasiento.append("E1")
    else:
      CE1.config(bg="Blue")
      NE1 = 0
      fl.Lasiento.remove("E1")

  def E2():
    global NE2
    if NE2 == 0:
      CE2.config(bg="Red")
      NE2 = 1
      fl.Lasiento.append("E2")
    else:
      CE2.config(bg="Blue")
      NE2 = 0
      fl.Lasiento.remove("E2")

  def E3():
    global NE3
    if NE3 == 0:
      CE3.config(bg="Red")
      NE3 = 1
      fl.Lasiento.append("E3")
    else:
      CE3.config(bg="Blue")
      NE3 = 0
      fl.Lasiento.remove("E3")

  def E4():
    global NE4
    if NE4 == 0:
      CE4.config(bg="Red")
      NE4 = 1
    else:
      CE4.config(bg="Blue")
      NE4 = 0
      fl.Lasiento.remove("E4")

  def E5():
    global NE5
    if NE5 == 0:
      CE5.config(bg="Red")
      NE5 = 1 
      fl.Lasiento.append("E5")
    else:
      CE5.config(bg="Blue")
      NE5 = 0
      fl.Lasiento.remove("E5")

  def E6():
    global NE6
    if NE6 == 0:
       CE6.config(bg="Red")
       NE6 = 1
       fl.Lasiento.append("E6")
    else:
      CE6.config(bg="Blue")
      NE6 = 0
      fl.Lasiento.remove("E6")

  def E7():
    global NE7
    if NE7 == 0:
      CE7.config(bg="Red")
      NE7 = 1
      fl.Lasiento.append("E7")
    else:
      CE7.config(bg="Blue")
      NE7 = 0
      fl.Lasiento.remove("E7")

  def E8():
    global NE8
    if NE8 == 0:
      CE8.config(bg="Red")
      NE8 = 1
      fl.Lasiento.append("E8")
    else:
      CE8.config(bg="Blue")
      NE8 = 0
      fl.Lasiento.remove("E8")

  def F1():
    global NF1
    if NF1 == 0:
      CF1.config(bg="Red")
      NF1 = 1
      fl.Lasiento.append("F1")
    else:
      CF1.config(bg="Blue")
      NF1 = 0
      fl.Lasiento.remove("F1")

  def F2():
    global NF2
    if NF2 == 0:
      CF2.config(bg="Red")
      NF2 = 1
      fl.Lasiento.append("F2")
    else:
      CF3.config(bg="Blue")
      NF2 = 0
      fl.Lasiento.remove("F2")

  def F3():
    global NF3
    if NF3 == 0:
      CF3.config(bg="Red")
      NF3 = 1
      fl.Lasiento.append("F3")

  def F4():
    global NF4
    if NF4 == 0:
      CF4.config(bg="Red")
      NF4 = 1
      fl.Lasiento.append("F4")
    else:
      CF4.config(bg="Blue")
      NF4 = 0
      fl.Lasiento.append("F4")

  def F5():
    global NF5
    if NF5 == 0:
      CF5.config(bg="Red")
      NF5 = 1
      fl.Lasiento.append("F5")
    else:
      CF5.config(bg="Blue")
      NF5 = 0
      fl.Lasiento.remove("F5")

  def F6():
    global NF6
    if NF6 == 0:
      CF6.config(bg="Red")
      NF6 = 1
      fl.Lasiento.append("F6")
    else:
      CF6.config(bg="Blue")
      NF6 = 0
      fl.Lasiento.remove("F6")

  def F7():
    global NF7
    if NF7 == 0:
      CF7.config(bg="Red")
      NF7 = 1
      fl.Lasiento.append("F7")
    else:
      CF7.config(bg="Blue")
      NF7 = 0
      fl.Lasiento.remove("F7")

  def F8():
    global NF8
    if NF8 == 0:
      CF8.config(bg="Red")
      NF8 = 1
      fl.Lasiento.append("F8")
    else:
      CF8.config(bg="Blue")
      NF8 = 0
      fl.Lasiento.remove("F8")

  def G1():
    global NG1
    if NG1 == 0:
      CG1.config(bg="Red")
      NG1 = 1
      fl.Lasiento.append("G1")
    else:
      CG1.config(bg="Blue")
      NG1 = 0
      fl.Lasiento.remove("G1")

  def G2():
    global NG2
    if NG2 == 0:
      CG2.config(bg="Red")
      NG2 = 1
      fl.Lasiento.append("G2")
    else:
      CG2.config(bg="Blue")
      NG2 = 0
      fl.Lasiento.remove("G2")

  def G3():
    global  NG3
    if NG3 == 0:
      CG3.config(bg="Red")
      NG3 = 1
      fl.Lasiento.append("G3")
    else:
      CG3.config(bg="Blue")
      NG3 = 0
      fl.Lasiento.remove("G3")

  def G4():
    global NG4
    if NG4 == 0:
      CG4.config(bg="Red")
      NG4 = 1
      fl.Lasiento.append("G4")
    else:
      CG4.config(bg="Blue")
      NG4 = 0
      fl.Lasiento.remove("G4")

  def G5():
    global NG5
    if NG5 == 0:
      CG5.config(bg="Red")
      NG5 = 1
      fl.Lasiento.append("G5")
    else:
      CG5.config(bg="Blue")
      NG5 = 0
      fl.Lasiento.remove("G5")

  def G6():
    global NG6
    if NG6 == 0:
      CG6.config(bg="Red")
      NG6 = 1
      fl.Lasiento.append("G6")
    else:
      CG6.config(bg="Blue")
      NG6 = 0
      fl.Lasiento.remove("G6")

  def G7():
    global NG7
    if NG7 == 0:
      CG7.config(bg="Red")
      NG7 = 1
      fl.Lasiento.append("G7")
    else:
      CG7.config(bg="Blue")
      NG7 = 0
      fl.Lasiento.remove("G7")

  def G8():
    global NG8
    if NG8 == 0:
      CG8.config(bg="Red")
      NG8 = 1
      fl.Lasiento.append("G8")
    else:
      CG8.config(bg="Blue")
      NG8 = 0
      fl.Lasiento.remove("G8")

  def H1():
    global NH1
    if NH1 == 0:
      CH1.config(bg="Red")
      NH1 = 1
      fl.Lasiento.append("H1")
    else:
      CG1.config(bg="Blue")
      NH1 = 0
      fl.Lasiento.remove("H1")

  def H2():
    global NH2
    if NH2 == 0:
      CH2.config(bg="Red")
      NH2 = 1
      fl.Lasiento.append("H2")
    else:
      CG2.config(bg="Blue")
      NH2 = 0
      fl.Lasiento.remove("H2")

  def H3():
    global NH3
    if NH3 == 0:
      CH3.config(bg="Red")
      NH3 = 1
      fl.Lasiento.append("H3")
    else:
      CH3.config(bg="Blue")
      NH3 = 0
      fl.Lasiento.remove("H3")

  def H4():
    global NH4
    if NH4 == 0:
      CH4.config(bg="Red")
      NH4 = 1
      fl.Lasiento.append("H4")
    else:
      CH4.config(bg="Blue")
      NH4 = 0
      fl.Lasiento.remove("H4")

  def H5():
    global NH5
    if NH5 == 0:
      CH5.config(bg="Red")
      NH5 = 1
      fl.Lasiento.append("H5")
    else:
      CH5.config(bg="Blue")
      NH5 = 0 
      fl.Lasiento.remove("H5")

  def H6():
    global NH6
    if NH6 == 0:
      CH6.config(bg="Red")
      NH6 = 1
      fl.Lasiento.append("H6")
    else:
      CH6.config(bg="Blue")
      NH6 = 0 
      fl.Lasiento.remove("H6")

  def H7():
    global NH7
    if NH7 == 0:
      CH7.config(bg="Red")
      NH7 = 1
      fl.Lasiento.append("H7")
    else:
      CH7.config(bg="Blue")
      NH7 = 0
      fl.Lasiento.remove("H7")

  def H8():
    global NH8 
    if NH8 == 0:
      CH8.config(bg="Red")
      NH8 = 1
      fl.Lasiento.append("H8")
    else:
      CH8.config(bg="Blue")
      NH8 = 0
      fl.Lasiento.remove("H8")

  Label(frameM,bg="Black",width=53,height=1).place(x=200,y=190)
   
  CA1 = Button(frameM,text="A1",command=A1,bg="Blue")
  CA1.place(x=200,y=220)
  CA2 = Button(frameM,text="A2",command=A2,bg="Blue")
  CA2.place(x=250,y=220)
  CA3 = Button(frameM,text="A3",command=A3,bg="Blue")
  CA3.place(x=300,y=220)
  CA4 = Button(frameM,text="A4",command=A4,bg="Blue")
  CA4.place(x=350,y=220)
  CA5 = Button(frameM,text="A5",command=A5,bg="Blue")
  CA5.place(x=400,y=220)
  CA6 = Button(frameM,text="A6",command=A6,bg="Blue")
  CA6.place(x=450,y=220)
  CA7 = Button(frameM,text="A7",command=A7,bg="Blue")
  CA7.place(x=500,y=220)
  CA8 = Button(frameM,text="A8",command=A8,bg="Blue")
  CA8.place(x=550,y=220)

  CB1 = Button(frameM,text="B1",command=B1,bg="Blue")
  CB1.place(x=200,y=250)
  CB2 = Button(frameM,text="B2",command=B2,bg="Blue")
  CB2.place(x=250,y=250)
  CB3 = Button(frameM,text="B3",command=B3,bg="Blue")
  CB3.place(x=300,y=250)
  CB4 = Button(frameM,text="B4",command=B4,bg="Blue")
  CB4.place(x=350,y=250)
  CB5 = Button(frameM,text="B5",command=B5,bg="Blue")
  CB5.place(x=400,y=250)
  CB6 = Button(frameM,text="B6",command=B6,bg="Blue")
  CB6.place(x=450,y=250)
  CB7 = Button(frameM,text="B7",command=B7,bg="Blue")
  CB7.place(x=500,y=250)
  CB8 = Button(frameM,text="B8",command=B8,bg="Blue")
  CB8.place(x=550,y=250)

  CC1 = Button(frameM,text="C1",command=C1,bg="Blue")
  CC1.place(x=200,y=280)
  CC2 = Button(frameM,text="C2",command=C2,bg="Blue")
  CC2.place(x=250,y=280)
  CC3 = Button(frameM,text="C3",command=C3,bg="Blue")
  CC3.place(x=300,y=280)
  CC4 = Button(frameM,text="C4",command=C4,bg="Blue")
  CC4.place(x=350,y=280)
  CC5 = Button(frameM,text="C5",command=C5,bg="Blue")
  CC5.place(x=400,y=280)
  CC6 = Button(frameM,text="C6",command=C6,bg="Blue")
  CC6.place(x=450,y=280)
  CC7 = Button(frameM,text="C7",command=C7,bg="Blue")
  CC7.place(x=500,y=280)
  CC8 = Button(frameM,text="C8",command=C8,bg="Blue")
  CC8.place(x=550,y=280)

  CD1 = Button(frameM,text="D1",command=D1,bg="Blue")
  CD1.place(x=200,y=310)
  CD2 = Button(frameM,text="D2",command=D2,bg="Blue")
  CD2.place(x=250,y=310)
  CD3 = Button(frameM,text="D3",command=D3,bg="Blue")
  CD3.place(x=300,y=310)
  CD4 = Button(frameM,text="D4",command=D4,bg="Blue")
  CD4.place(x=350,y=310)
  CD5 = Button(frameM,text="D5",command=D5,bg="Blue")
  CD5.place(x=400,y=310)
  CD6 = Button(frameM,text="D6",command=D6,bg="Blue")
  CD6.place(x=450,y=310)
  CD7 = Button(frameM,text="D7",command=D7,bg="Blue")
  CD7.place(x=500,y=310)
  CD8 = Button(frameM,text="D8",command=D8,bg="Blue")
  CD8.place(x=550,y=310)

  CE1 = Button(frameM,text="E1",command=E1,bg="Blue")
  CE1.place(x=200,y=340)
  CE2 = Button(frameM,text="E2",command=E2,bg="Blue")
  CE2.place(x=250,y=340)
  CE3 = Button(frameM,text="E3",command=E3,bg="Blue")
  CE3.place(x=300,y=340)
  CE4 = Button(frameM,text="E4",command=E4,bg="Blue")
  CE4.place(x=350,y=340)
  CE5 = Button(frameM,text="E5",command=E5,bg="Blue")
  CE5.place(x=400,y=340)
  CE6 = Button(frameM,text="E6",command=E6,bg="Blue")
  CE6.place(x=450,y=340)
  CE7 = Button(frameM,text="E7",command=E7,bg="Blue")
  CE7.place(x=500,y=340)
  CE8 = Button(frameM,text="E8",command=E8,bg="Blue")
  CE8.place(x=550,y=340)

  CF1 = Button(frameM,text="F1",command=F1,bg="Blue")
  CF1.place(x=200,y=370)
  CF2 = Button(frameM,text="F2",command=F2,bg="Blue")
  CF2.place(x=250,y=370)
  CF3 = Button(frameM,text="F3",command=F3,bg="Blue")
  CF3.place(x=300,y=370)
  CF4 = Button(frameM,text="F4",command=F4,bg="Blue")
  CF4.place(x=350,y=370)
  CF5 = Button(frameM,text="F5",command=F5,bg="Blue")
  CF5.place(x=400,y=370) 
  CF6 = Button(frameM,text="F6",command=F6,bg="Blue")
  CF6.place(x=450,y=370)
  CF7 = Button(frameM,text="F7",command=F7,bg="Blue")
  CF7.place(x=500,y=370)
  CF8 = Button(frameM,text="F8",command=F8,bg="Blue")
  CF8.place(x=550,y=370)
  
  CG1 = Button(frameM,text="G1",command=G1,bg="Blue")
  CG1.place(x=200,y=400)
  CG2 = Button(frameM,text="G2",command=G2,bg="Blue")
  CG2.place(x=250,y=400)
  CG3 = Button(frameM,text="G3",command=G3,bg="Blue")
  CG3.place(x=300,y=400)
  CG4 = Button(frameM,text="G4",command=G4,bg="Blue")
  CG4.place(x=350,y=400)
  CG5 = Button(frameM,text="G5",command=G5,bg="Blue")
  CG5.place(x=400,y=400)
  CG6 = Button(frameM,text="G6",command=G6,bg="Blue")
  CG6.place(x=450,y=400)
  CG7 = Button(frameM,text="G7",command=G7,bg="Blue")
  CG7.place(x=500,y=400)
  CG8 = Button(frameM,text="G8",command=G8,bg="Blue")
  CG8.place(x=550,y=400)

  CH1 = Button(frameM,text="H1",command=H1,bg="Blue")
  CH1.place(x=200,y=430)
  CH2 = Button(frameM,text="H2",command=H2,bg="Blue")
  CH2.place(x=250,y=430)
  CH3 = Button(frameM,text="H3",command=H3,bg="Blue")
  CH3.place(x=300,y=430)
  CH4 = Button(frameM,text="H4",command=H4,bg="Blue")
  CH4.place(x=350,y=430)
  CH5 = Button(frameM,text="H5",command=H5,bg="Blue")
  CH5.place(x=400,y=430)
  CH6 = Button(frameM,text="H6",command=H6,bg="Blue")
  CH6.place(x=450,y=430)
  CH7 = Button(frameM,text="H7",command=H7,bg="Blue")
  CH7.place(x=500,y=430)
  CH8 = Button(frameM,text="H8",command=H8,bg="Blue")
  CH8.place(x=550,y=430)

  def back():
    frameM.destroy()

  def Balidar():
    if len(fl.Lasiento) == int(numP.get()):
        comida() 
    else:
       messagebox.showinfo("Error","Seleccione la cantidad correcta de campos")

  Button(frameM,text="siguiente",command=Balidar).place(x=400,y=465)
  Button(frameM,text="Atras",command=back).place(x=350,y=465)


#Funcion para llamar el metodo Main-------------------------------------------------------------------
def main():
  frameMain = Frame(windowsFrame1,width=900,height=500)
  frameMain.place(x=0,y=0)
  
  #imajen de fondo de----------------------------------------------------------------------------------
  Label(frameMain,image=fondo).place(x=0,y=0)
  #-----------------------------------------------------------------------------------------------------

  Label(frameMain,text="Tanda",font=("Arial",45),bg="#CDC2BF").place(x=350,y=0)

  Button(frameMain,text="Batman",width=200,height=300,command=Batman,image=PBatman).place(x=100,y=80)
  Button(frameMain,text="Uncharted",width=200,height=300,command=Uncharted,image=Puncharted).place(x=350,y=80)
  Button(frameMain,text="Morvious",width=200,height=300,command=Morvious,image=Pmorvious).place(x=600,y=80)

  def back():
    frameMain.destroy()

  Button(frameMain,text="Volver",command=back).place(x=430,y=450)
#------------------------------------------------------------------------------------------------------

#Menu de registro
def Menuregistro():
    frameRegistro = Frame(windowsFrame1,width=900,height=500)
    frameRegistro.place(x=0,y=0)

    #imajen de fondo de---------------------------
    Label(frameRegistro,image=fondo).place(x=0,y=0)
    #----------------------------------------------

    Label(frameRegistro,text="Nombre",bg="#CDC2BF").place(x=400,y=5)

    Entry(frameRegistro,textvariable=RNombre,justify=CENTER).place(x=365,y=21)

    Label(frameRegistro,text="Contraseña",bg="#CDC2BF").place(x=388,y=45)

    Entry(frameRegistro,textvariable=RContra,justify=CENTER,show="*").place(x=365,y=65)

    Label(frameRegistro,text="Cedula",bg="#CDC2BF").place(x=400,y=85)

    Entry(frameRegistro,justify=CENTER,textvariable=RCedula).place(x=365,y=105)

    Label(frameRegistro,text="Numero de telefono",bg="#CDC2BF").place(x=365,y=130)

    Entry(frameRegistro,justify=CENTER,textvariable=RNT).place(x=365,y=150)

    Label(frameRegistro,text="Correo",bg="#CDC2BF").place(x=399,y=173)

    Entry(frameRegistro,justify=CENTER,textvariable=RCorreo).place(x=365,y=190)

    Label(frameRegistro,text="Direccion",bg="#CDC2BF").place(x=399,y=210)

    Entry(frameRegistro,justify=CENTER,textvariable=RDireccion).place(x=365,y=230)

    Label(frameRegistro,text="Tipo de persona",bg="#CDC2BF").place(x=380,y=260)

    ttk.Combobox(frameRegistro,value=["Nacional","Extranjero"],state="readonly",width=18,justify=CENTER,textvariable=RTipoPersona).place(x=365,y=280)

    Label(frameRegistro,text="Clase",bg="#CDC2BF").place(x=410,y=315) 

    ttk.Combobox(frameRegistro,value=["Niño","Adulto"],state="readonly",width=18,justify=CENTER,textvariable=RClase).place(x=365,y=335)

    Button(frameRegistro,text="Registrarce",width="17",height="2",command=Registro).place(x=425,y=385)

    #----------------------------------------------------------------------------------------------------------------------------------------

    #Volver al frame principal

    def fvolver():
      frameRegistro.destroy()

    #========================

    Button(frameRegistro,text="Volver",command=fvolver,width="17",height="2").place(x=290,y=385)


#Pertenece al login-----------------------------------------------------------------------------------
Label(windowsFrame1,text="Usuario",bg="#CDC2BF").place(x=400,y=60)

Entry(windowsFrame1,textvariable=LUsuario,justify=CENTER).place(x=365,y=90)

Label(windowsFrame1,text="Contraseña",bg="#CDC2BF").place(x=400,y=160)

Entry(windowsFrame1,textvariable=LContra,justify=CENTER,show="*").place(x=365,y=200)

Button(windowsFrame1,text="Login",width="17",height="2",command=Login).place(x=364,y=260)

Button(windowsFrame1,text="Registrarce", width="17",height="2",command=Menuregistro).place(x=364,y=330)
#-------------------------------------------------------------------------------------------------------

#Corredor de codigo 
windowsFrame1.mainloop()