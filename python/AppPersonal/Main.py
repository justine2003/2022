import sys
from Frame import *
import Asistente as asis
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import *

#Comando usado para transformar a py
#pyuic -x Frame.ui -o Frame.py

class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #incio por defecto
        self.ui.btnRestaurar.hide()

        #Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #sizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        #mover ventana
        self.ui.BarraHerramientas.mouseMoveEvent = self.mover_ventana

        #control barra de titulos
        self.ui.btnMinimisar.clicked.connect(self.control_bt_minimizar)
        self.ui.btnRestaurar.clicked.connect(self.control_bt_normal)
        self.ui.btnMaximisar.clicked.connect(self.control_bt_maximisar)
        self.ui.btnCerrar.clicked.connect(lambda: self.close())

        #Acceder a las paginas
        self.ui.Inicio.clicked.connect(lambda: self.ui.Masterpague.setCurrentWidget(self.ui.PgInicio))
        self.ui.Software.clicked.connect(lambda: self.ui.Masterpague.setCurrentWidget(self.ui.PgSoftware))
        self.ui.Diseno.clicked.connect(lambda: self.ui.Masterpague.setCurrentWidget(self.ui.PgDiseno))
        self.ui.Office.clicked.connect(lambda: self.ui.Masterpague.setCurrentWidget(self.ui.PgOffice))
        self.ui.Seguridad.clicked.connect(lambda: self.ui.Masterpague.setCurrentWidget(self.ui.PgSeguridad))

        self.ui.Asistente.clicked.connect(self.Asistente)

        #Ocutar el menu
        self.ui.btnMenu.clicked.connect(self.ocultar_menu)

    #mover ventana
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False:		
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()	
        
        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

	#Barra de heramientas
    def control_bt_minimizar(self):
        self.showMinimized()		

    def control_bt_normal(self): 
        self.showNormal()		
        self.ui.btnRestaurar.hide()
        self.ui.btnMaximisar.show()

    def control_bt_maximisar(self):
        self.showMaximized()
        self.ui.btnRestaurar.show()
        self.ui.btnMaximisar.hide()

    #Ocultar y mostar el menu para
    def ocultar_menu(self):
        if True:			
            width = self.ui.Menu.width()
            normal = 0
            if width==0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.ui.Menu, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()


    def Asistente(self):
        asis.Ayuda()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = MiApp()
    menu.show()
    sys.exit(app.exec_())