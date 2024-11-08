import sys
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QHBoxLayout, QStackedLayout, QVBoxLayout, QRadioButton, QButtonGroup
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

class CajaH(QHBoxLayout):
    def __init__(self, stack):
        super().__init__()

        self.stk = stack  # Sttaked layout

        self.rdBtnRojo = QRadioButton("Rojo")
        self.rdBtnRojo.clicked.connect(self.on_Boton_Click)

        self.rdBtnAzul = QRadioButton("Azul")
        self.rdBtnAzul.clicked.connect(self.on_Boton_Click)

        self.rdBtnVerde = QRadioButton("Verde")
        self.rdBtnVerde.clicked.connect(self.on_Boton_Click)

        self.rdBtnNaranja = QRadioButton("Naranja")
        self.rdBtnNaranja.clicked.connect(self.on_Boton_Click)

        self.rdBtnFormulario = QRadioButton("Formulario")
        self.rdBtnFormulario.clicked.connect(self.on_Boton_Click)

        # Grupo de Botones
        self.grupoBtn = QButtonGroup()
        self.grupoBtn.addButton(self.rdBtnRojo, 0)
        self.grupoBtn.addButton(self.rdBtnAzul, 1)
        self.grupoBtn.addButton(self.rdBtnVerde, 2)
        self.grupoBtn.addButton(self.rdBtnNaranja, 3)
        self.grupoBtn.addButton(self.rdBtnFormulario, 4)

        # Añadidos al layout
        self.addWidget(self.rdBtnRojo)
        self.addWidget(self.rdBtnAzul)
        self.addWidget(self.rdBtnVerde)
        self.addWidget(self.rdBtnNaranja)
        self.addWidget(self.rdBtnFormulario)

    def on_Boton_Click(self):

        botonPresionado = self.sender()

        self.stk.setCurrentIndex(self.grupoBtn.id(botonPresionado))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    app.exec()
