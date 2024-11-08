
import sys

from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication,QPushButton,QStackedLayout, QVBoxLayout

from Formulario import Formulario
from VentanaBox import CajaColor

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 400)
        self.setWindowTitle("Ejemplo de StackedLayout con Qt")

        cajaV = CajaV()

        contenedor = QWidget()
        contenedor.setLayout(cajaV)
        self.setCentralWidget(contenedor)

        self.show()

class CajaV(QVBoxLayout):
    def __init__(self):
        super().__init__()

        stack = QStackedLayout()

        stack.addWidget(CajaColor("red"))
        stack.addWidget(CajaColor("blue"))
        stack.addWidget(CajaColor("green"))
        stack.addWidget(CajaColor("orange"))
        stack.addWidget(Formulario())

        stack.setCurrentIndex(3)

        cajaH = CajaH(stack)

        self.addLayout(stack)
        self.addLayout(cajaH)

class CajaH(QVBoxLayout):
    def __init__(self,stack):
        super().__init__()

        self.stk = stack

        self.btnRojo = QPushButton("Rojo")
        self.btnRojo.pressed.connect(self.on_Boton_Click)
        self.addWidget(self.btnRojo)

        self.btnAzul = QPushButton("Azul")
        self.btnAzul.pressed.connect(self.on_Boton_Click)
        self.addWidget(self.btnAzul)

        self.btnVerde = QPushButton("Verde")
        self.btnVerde.pressed.connect(self.on_Boton_Click)
        self.addWidget(self.btnVerde)

        self.btnNaranja = QPushButton("Naranja")
        self.btnNaranja.pressed.connect(self.on_Boton_Click)
        self.addWidget(self.btnNaranja)

        self.btnFormulario = QPushButton("Formulario")
        self.btnFormulario.pressed.connect(self.on_Boton_Click)
        self.addWidget(self.btnFormulario)

    def on_Boton_Click(self):

        botonPresionado = self.sender() # Recoje el boton que a enviado la señal

        if botonPresionado == self.btnRojo:
            self.stk.setCurrentIndex(0)
        elif botonPresionado == self.btnAzul:
            self.stk.setCurrentIndex(1)
        elif botonPresionado == self.btnVerde:
            self.stk.setCurrentIndex(2)
        elif botonPresionado == self.btnNaranja:
            self.stk.setCurrentIndex(3)
        elif botonPresionado == self.btnFormulario:
            self.stk.setCurrentIndex(4)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    app.exec()