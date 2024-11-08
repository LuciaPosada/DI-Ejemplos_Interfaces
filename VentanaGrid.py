import sys

from PyQt6.QtWidgets import QWidget,QMainWindow,QApplication,QGridLayout
from Libreria import CajaColor,LayoutBox

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 400)

        self.setWindowTitle("Ejemplo de GridLayout con Qt")

        maya = QGridLayout()
        maya.addWidget(CajaColor("red"), 0, 0, 1, 1) # fila - columna
        maya.addWidget(CajaColor("blue"), 0, 1, 1, 2)
        maya.addWidget(CajaColor("green"), 1, 0, 2, 1)
        maya.addWidget(CajaColor("pink"), 1, 1, 1, 2)
        maya.addWidget(CajaColor("orange"), 2, 1, 1, 1)
        maya.addWidget(CajaColor("yellow"), 2, 2, 1, 1)
        maya.addLayout(LayoutBox(), 3, 0, 3, 3)

        contenedor = QWidget()
        contenedor.setLayout(maya)

        self.setCentralWidget(contenedor)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    app.exec()



