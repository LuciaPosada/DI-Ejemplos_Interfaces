
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QListView, QWidget, QHBoxLayout, QPushButton, QLineEdit

from Modelo_ListaTareas import ModeloTareas

class EjQListView (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QListView")
        self.setFixedSize(250, 300)

        listTareas = [(False,"Ir al gym"),(False,"Hacer la compra"),(False,"Lavar la loza"),(False,"Hacer la comida")]

        self.modelo = ModeloTareas(listTareas)

        self.lvTareas = QListView()
        self.lvTareas.setModel(self.modelo)
        self.lvTareas.setSelectionMode(QListView.SelectionMode.MultiSelection)

        self.botonera = Botonera(self)

        self.linEditTexto = QLineEdit()

        self.btnToDo = QPushButton("Add ToDo")
        self.btnToDo.pressed.connect(self.on_btnToDo_clicked)

        cajaV = QVBoxLayout()
        cajaV.addWidget(self.lvTareas)
        cajaV.addWidget(self.botonera)
        cajaV.addWidget(self.linEditTexto)
        cajaV.addWidget(self.btnToDo)

        contenedor = QWidget()
        contenedor.setLayout(cajaV)
        self.setCentralWidget(contenedor)

        self.show()

    def on_btnToDo_clicked(self):
        texto = self.linEditTexto.text().strip()
        if texto:
            self.modelo.tareas.append((False,texto))
            self.modelo.layoutChanged.emit()
            self.linEditTexto.clear()

    def on_Botonera_Btn_clciked(self):
        indices = self.lvTareas.selectedIndexes()
        botonPresionado = self.sender()

        if botonPresionado == self.botonera.btnBorrar:
            for indice in sorted (indices, reverse=True):
                del self.modelo.tareas[indice.row()]
            self.modelo.layoutChanged.emit()
            self.lvTareas.clearSelection()
        if botonPresionado == self.botonera.btnCompletar:
            for indice in indices:
                _,texto = self.modelo.tareas[indice.row()]
                self.modelo.tareas[indice.row()] = (True,texto)
            self.modelo.dataChanged.emit(indice,indice)
            self.lvTareas.clearSelection()

class Botonera(QWidget):

    def __init__(self,parent):
        super().__init__()
        self.parent = parent

        layout = QHBoxLayout()

        #nomBtn = ["Delete","Complete"]

        #for nombre in nomBtn:
            #layout.addWidget(QPushButton(nombre))

        self.btnBorrar = QPushButton("Delete")
        self.btnBorrar.pressed.connect(self.parent.on_Botonera_Btn_clciked)

        self.btnCompletar = QPushButton("Complete")
        self.btnCompletar.pressed.connect(self.parent.on_Botonera_Btn_clciked)

        layout.addWidget(self.btnBorrar)
        layout.addWidget(self.btnCompletar)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = EjQListView()
    app.exec()