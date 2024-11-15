import sys
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QHBoxLayout, QStackedLayout, QVBoxLayout, QCheckBox
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

class CajaV(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.stack = QStackedLayout()

        # Lista de colores
        colores = [
            "#ffffff", "#ff0000", "#0000ff", "#00ff00", "#ff7b00", "#ff3e00",
            "#808000", "#800080", "#008080", "#803e80", "#80bd00", "#aa7e00",
            "#aa2955", "#555555", "#557e55", "#000000"
        ]

        # blanco,rojo,azul,verde,naranja,(r+n),(r+v),(r+a),(a+v),(a+n),(n+v),(r+n+v),(r+n+a),(r+v+a),(n+v+a),negro

        for color in colores:
            self.stack.addWidget(CajaColor(color))

        self.stack.setCurrentIndex(0)

        self.addLayout(self.stack)
        self.addLayout(CajaH(self.stack))


class CajaH(QHBoxLayout):
    def __init__(self, stack):
        super().__init__()

        self.stack = stack  # QStackedLayout recibido como parámetro

        self.chkBoxRojo = QCheckBox("Rojo")
        self.chkBoxRojo.clicked.connect(self.on_CheckBox_Click)

        self.chkBoxAzul = QCheckBox("Azul")
        self.chkBoxAzul.clicked.connect(self.on_CheckBox_Click)

        self.chkBoxVerde = QCheckBox("Verde")
        self.chkBoxVerde.clicked.connect(self.on_CheckBox_Click)

        self.chkBoxNaranja = QCheckBox("Naranja")
        self.chkBoxNaranja.clicked.connect(self.on_CheckBox_Click)

        self.addWidget(self.chkBoxRojo)
        self.addWidget(self.chkBoxAzul)
        self.addWidget(self.chkBoxVerde)
        self.addWidget(self.chkBoxNaranja)

    def on_CheckBox_Click(self):
        # tupla
        estado_checkbox = (
            self.chkBoxRojo.isChecked(),
            self.chkBoxAzul.isChecked(),
            self.chkBoxVerde.isChecked(),
            self.chkBoxNaranja.isChecked()
        )

        # diccionario con tuplas
        pestañas = {
            (False, False, False, False): 0,    # Ninguno (Blanco)
            (True, False, False, False): 1,     # Solo Rojo
            (False, True, False, False): 2,     # Solo Azul
            (False, False, True, False): 3,     # Solo Verde
            (False, False, False, True): 4,     # Solo Naranja
            (True, False, False, True): 5,      # Rojo + Naranja
            (True, False, True, False): 6,      # Rojo + Verde
            (True, True, False, False): 7,      # Rojo + Azul
            (False, True, True, False): 8,      # Azul + Verde
            (False, True, False, True): 9,      # Azul + Naranja
            (False, False, True, True): 10,     # Naranja + Verde
            (True, True, False, True): 11,      # Rojo + Azul + Naranja
            (True, False, True, True): 12,      # Rojo + Verde + Naranja
            (True, True, True, False): 13,      # Rojo + Verde + Azul
            (False, True, True, True): 14,      # Azul + Verde + Naranja
            (True, True, True, True): 15,       # Todos (Negro)
        }

        self.stack.setCurrentIndex(pestañas.get(estado_checkbox, 0))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()  # Mostrar ventana principal
    sys.exit(app.exec())
