
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QTabWidget,QComboBox, QWidget, QVBoxLayout

from Formulario import Formulario
from VentanaBox import CajaColor

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 400)
        self.setWindowTitle("Ejemplo de QTabWigget")

        cajaV = CajaV()
        contenedor = QWidget()
        contenedor.setLayout(cajaV)
        self.setCentralWidget(contenedor)

        self.show()

class CajaV(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.tab = Tabss()
        self.addWidget(self.tab)

        self.cBox = QComboBox()
        self.cBox.addItems(("Rojo", "Azul", "Verde", "Naranja"))
        self.cBox.setCurrentIndex(-1)

        self.cBox.currentIndexChanged.connect(self.on_ComboBox_Change)

        self.addWidget(self.cBox)

    def on_ComboBox_Change(self):

        (self.tab.setCurrentIndex(self.cBox.currentIndex()))


class Tabss(QTabWidget):

    def __init__(self):
        super().__init__()

        self.addTab(CajaColor("red"),"Rojo")
        self.addTab(CajaColor("blue"),"Azul")
        self.addTab(CajaColor("green"),"Verde")
        self.addTab(CajaColor("orange"), "Naranja")
        self.addTab(Formulario(),"Formulario")

        # self.setTabPosition(QTabWidget.TabPosition.West)
        self.setCurrentIndex(2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    app.exec()