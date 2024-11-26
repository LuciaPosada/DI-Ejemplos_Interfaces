
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QTableView, QHBoxLayout, QLineEdit, \
    QComboBox, QCheckBox, QPushButton

from Modelo_Tabla import ModeloTabla

class EjQTableView (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QTableView")
        self.setFixedSize(435, 250)

        datos = [["Nombre","DNI","Genero","Fallecido"],
                 ["Ana Perez","54321111L","Mujer",False],
                 ["Paco Torras","12345679P","Hombre",True],
                 ["Roque Vila","33533213M","Hombre",False],
                 ["Lina Saiz","45463826Q","Mujer",False]]

        self.modelo = ModeloTabla(datos)

        self.tvwTabla = QTableView()
        self.tvwTabla.setModel(self.modelo)
        self.tvwTabla.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        self.tvwTabla.selectionModel().selectionChanged.connect(self.on_Tabla_Select)

        cajaH = QHBoxLayout()

        self.txtNombre = QLineEdit()
        self.txtDni = QLineEdit()
        self.cmbGenero = QComboBox()
        self.cmbGenero.setCurrentIndex(-1)
        self.chkFallecido = QCheckBox()

        self.cmbGenero.addItems(('Hombre','Mujer','Otro'))

        cajaH.addWidget(self.txtNombre)
        cajaH.addWidget(self.txtDni)
        cajaH.addWidget(self.cmbGenero)
        cajaH.addWidget(self.chkFallecido)

        cajaH2 = QHBoxLayout()
        self.btnAceptar = QPushButton("Apceptar")
        self.btnAceptar.clicked.connect(self.on_btnAceptar_clicked)
        self.btnCancelar = QPushButton("Cancelar")
        self.btnCancelar.clicked.connect(self.on_btnCancelar_clicked)

        cajaH2.addWidget(self.btnAceptar)
        cajaH2.addWidget(self.btnCancelar)

        cajaV = QVBoxLayout()
        cajaV.addWidget(self.tvwTabla)
        cajaV.addLayout(cajaH)
        cajaV.addLayout(cajaH2)

        contenedor = QWidget()
        contenedor.setLayout(cajaV)
        self.setCentralWidget(contenedor)

        self.show()

    def on_Tabla_Select(self):

        indice = self.tvwTabla.selectedIndexes()

        if indice != []:
            self.txtNombre.setText(self.modelo.tabla[indice[0].row()][0])
            self.txtDni.setText(self.modelo.tabla[indice[0].row()][1])
            for i in range(self.cmbGenero.count()):
                if self.modelo.tabla[indice[0].row()][2] == self.cmbGenero.itemText(i):
                    self.cmbGenero.setCurrentIndex(i)
            if self.modelo.tabla[indice[0].row()][3]:
                self.chkFallecido.setChecked(True)
            else:
                self.chkFallecido.setChecked(False)

    def on_btnCancelar_clicked(self):
        self.txtNombre.clear()
        self.txtDni.clear()
        self.cmbGenero.setCurrentIndex(-1)
        self.chkFallecido.setChecked(False)

    def on_btnAceptar_clicked(self):
        indice = self.tvwTabla.selectedIndexes()

        if indice != []:
            if self.txtNombre.text() == '' or self.txtDni.text() == '' or self.cmbGenero.currentIndex() == -1:
                print ("Faltan datos")
            else:
                self.modelo.tabla[indice[0].row()][0] = self.txtNombre.text()
                self.modelo.tabla[indice[0].row()][1] = self.txtDni.text()
                self.modelo.tabla[indice[0].row()][2] = self.cmbGenero.currentText()
                self.modelo.tabla[indice[0].row()][3] = True if self.chkFallecido.isChecked else False

                self.modelo.layoutChanged.emit()
                self.on_btnCancelar_clicked()
        else:
            if self.txtNombre.text() == '' or self.txtDni.text() == '' or self.cmbGenero.currentIndex() == -1:
                print ("Faltan datos")
            else:
                self.modelo.tabla.append((self.txtNombre.text(),self.txtDni.text(),self.cmbGenero.currentText(),True if self.chkFallecido.isChecked else False))

                self.modelo.layoutChanged.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = EjQTableView()
    app.exec()