import sys

from PyQt6.QtWidgets import QWidget,QMainWindow,QApplication,QGridLayout,QLabel,QPushButton,QLineEdit,QVBoxLayout

class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ñ")

        self.setCentralWidget(Formulario())

        self.show()

class Formulario(QWidget):
    def __init__(self):
        super().__init__()

        maya = QGridLayout()
        maya.addLayout(CuadrosTexto(), 0, 1, 1, 1)
        maya.addLayout(EtiquetasTexto(), 0, 0, 1, 1)

        contenedor1 = QWidget()
        contenedor1.setLayout(maya)

        maya2 = QVBoxLayout()
        maya2.addWidget(contenedor1)
        maya2.addLayout(Botonera())

        self.setLayout(maya2)

class Botonera(QGridLayout):

    def __init__(self):
        super().__init__()

        self.btnEditar = QPushButton("Editar")
        self.btnAceptar = QPushButton("Aceptar")
        self.btnCancelar = QPushButton("Cancelar")

        self.addWidget(self.btnEditar, 0, 0)
        self.addWidget(self.btnAceptar, 0, 1)
        self.addWidget(self.btnCancelar, 0, 2)

class EtiquetasTexto(QGridLayout):

    def __init__(self):
        super().__init__()

        self.etNome  = QLabel("Nombre")
        self.etApel = QLabel("Apellido")
        self.etDni = QLabel("DNI")
        self.etEdad = QLabel("Edad")

        self.addWidget(self.etNome)
        self.addWidget(self.etApel)
        self.addWidget(self.etDni)
        self.addWidget(self.etEdad)

class CuadrosTexto(QGridLayout):

    def __init__(self):
        super().__init__()

        self.textNome = QLineEdit()
        self.textNome.setPlaceholderText("Nombre")

        self.textApel = QLineEdit()
        self.textApel.setPlaceholderText("Apellido")

        self.textDni = QLineEdit()
        self.textDni.setPlaceholderText("DNI")

        self.textEdad = QLineEdit()
        self.textEdad.setPlaceholderText("Edad")

        self.addWidget(self.textNome)
        self.addWidget(self.textApel)
        self.addWidget(self.textDni)
        self.addWidget(self.textEdad)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    app.exec()
