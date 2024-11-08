
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication,QTabWidget

from Formulario import Formulario
from VentanaBox import CajaColor

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 400)
        self.setWindowTitle("Ejemplo de QTabWigget")

        tabbs = Tabss()

        self.setCentralWidget(tabbs)

        self.show()

class Tabss(QTabWidget):

    def __init__(self):
        super().__init__()

        self.addTab(CajaColor("red"),"Rojo")
        self.addTab(CajaColor("blue"),"Azul")
        self.addTab(CajaColor("green"),"Verde")
        self.addTab(CajaColor("orange"), "Naranja")
        self.addTab(Formulario(),"Formulario")

        self.setCurrentIndex(2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    app.exec()