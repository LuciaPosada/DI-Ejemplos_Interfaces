import sys
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QHBoxLayout, QStackedLayout, QVBoxLayout, QCheckBox, \
    QComboBox
from VentanaBox import CajaColor

class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 200)
        self.setWindowTitle("Ejemplo de StackedLayout con Qt")

        cajaV = CajaV()

        contenedor = QWidget()
        contenedor.setLayout(cajaV)
        self.setCentralWidget(contenedor)

class CajaV(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.stack = QStackedLayout()

        # Lista de colores
        colores = [
            "#ffffff","#ff0000", "#0000ff", "#00ff00", "#ff7b00"
        ]

        # blanco,rojo,azul,verde,naranja,

        for color in colores:
            self.stack.addWidget(CajaColor(color))

        self.stack.setCurrentIndex(0)

        self.addLayout(self.stack)
        self.addLayout(CajaH(self.stack))


class CajaH(QHBoxLayout):
    def __init__(self, stack):
        super().__init__()

        self.stack = stack

        self.cBox = QComboBox()
        self.cBox.addItems(("Blanco","Rojo", "Azul", "Verde", "Naranja"))
        self.cBox.setCurrentIndex(-1)
        # self.cBox.setEditable(True)

        self.cBox.currentIndexChanged.connect(self.on_ComboBox_Change)

        self.addWidget(self.cBox)

    def on_ComboBox_Change(self):

        self.stack.setCurrentIndex(self.cBox.currentIndex())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()  # Mostrar ventana principal
    sys.exit(app.exec())
