Valor = True
Num = 0
TipoPelicula = ""
Lasiento = []
datoP = []
NumF = 0
listac = []

def validacion(Lusauario,Lcontra):
    datos = []
    global usuario
    usuario = Lusauario

    try:
     with open("DatosCliente/"+Lusauario+".txt") as fname:
         lineas = fname.readlines()
         for linea in lineas:
             datos.append(linea.strip('\n'))
             
         if datos[0] == Lusauario:
                  if datos[1] == Lcontra:
                              global Valor
                              Valor = True
                  else:
                      Valor = False
         else:
                Valor = False
    except:
        Valor = False

def NumclienteC(Tipo):
    global datoP
    global Num

    if Tipo == "Batman":
        
        with open("Config/Batman.txt", "r") as fnum:
            lineas = fnum.readlines()
            for linea in lineas:
                datoP.append(linea.strip('\n'))

        n = int(datoP[0])
        Num = n+1
        NumClienteB()

    elif Tipo == "Uncharted":
        
        with open("Config/Uncharted.txt", "r") as fnum:
            lineas = fnum.readlines()
            for linea in lineas:
                datoP.append(linea.strip('\n'))
        
        n = int(datoP[0])
        Num = n+1
        NumClienteU()

    elif Tipo == "Morvious":

        with open("Config/Morvious.txt", "r") as fnum:
            lineas = fnum.readlines()
            for linea in lineas:
                datoP.append(linea.strip('\n'))

        n = int(datoP[0])
        Num = n+1
        NumClienteM()

def NumClienteB():
    with open("Config/Batman.txt", "w") as f:
        global Num
        Total = str(Num)
        f.write(Total)

def NumClienteM():
     with open("Config/Morvious.txt", "w") as f:
        global Num
        Total = str(Num)
        f.write(Total)


def NumClienteU():
        with open("Config/Uncharted.txt", "w") as f:
            global Num
            Total = str(Num)
            f.write(Total)


def NumC():
    fichero = open("Config/Numfactura.txt", 'rt')
    lineas = fichero.readline()
    n = int(lineas)
    global NumF
    NumF = n+1
    NumR()

def NumR():
    with open("Config/Numfactura.txt", "w") as f:
        global NumF
        Total = str(NumF)
        f.write(Total)