import sys
from tkinter.constants import HORIZONTAL

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QWidget,QMainWindow,QVBoxLayout,QApplication,QHBoxLayout

class Ventana (QMainWindow):

    def __init__(self):
        super().__init__()
        self.segundaVentana = None
        self.setWindowTitle("Color")
        self.setMinimumSize(700,400)

        cajaV = QHBoxLayout()

        cajaV.addWidget(CajaColorCon3Componentes("white"))
        cajaV.addWidget(CajaColor("green"))
        cajaV.addWidget(CajaColorCon2Componentes("white"))

        contenedor = QWidget()
        contenedor.setLayout(cajaV)

        self.setCentralWidget(contenedor)

        self.show()

class CajaColor (QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window,QColor(color))
        self.setPalette(paleta)

class CajaColorCon2Componentes (QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window,QColor(color))
        self.setPalette(paleta)

        cajaV = QVBoxLayout()

        cajaV.addWidget(CajaColor("blue"))
        cajaV.addWidget(CajaColor("red"))

        self.setLayout(cajaV)

class CajaColorCon3Componentes (QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window,QColor(color))
        self.setPalette(paleta)

        cajaV = QVBoxLayout()

        cajaV.addWidget(CajaColor("blue"))
        cajaV.addWidget(CajaColor("red"))
        cajaV.addWidget(CajaColor("green"))

        self.setLayout(cajaV)

if __name__ == "__main__":
    aplication = QApplication(sys.argv)
    ventana = Ventana()
    aplication.exec()