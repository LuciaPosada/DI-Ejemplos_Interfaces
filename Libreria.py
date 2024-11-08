
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout


class CajaColor(QWidget):

    def __init__(self ,color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)

class LayoutBox (QHBoxLayout):

    def __init__(self):
        super().__init__()

        caja1 = QVBoxLayout()
        caja1.addWidget(CajaColor("blue"))
        caja1.addWidget(CajaColor("green"))
        caja1.addWidget(CajaColor("pink"))

        caja2 = QVBoxLayout()
        caja2.addWidget(CajaColor("yellow"))
        caja2.addWidget(CajaColor("grey"))

        self.addLayout(caja1)
        self.addWidget(CajaColor("green"))
        self.addLayout(caja2)