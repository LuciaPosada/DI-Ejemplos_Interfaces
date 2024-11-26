
import sys

from PyQt6.QtGui import QImage

tick = QImage('tick.png')
x = QImage('x.png')

from PyQt6.QtCore import Qt, QAbstractListModel

class ModeloTareas (QAbstractListModel):
    def __init__(self, tareas=None):
        super().__init__()
        self.tareas = tareas or []

    def data(self,indice,rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            _,texto = self.tareas [indice.row()]
            return texto
        if rol == Qt.ItemDataRole.DecorationRole:
            estado,_ = self.tareas [indice.row()]
            if estado == True:
                return tick
            if estado == False:
                return x

    def rowCount(self, indice):
        return len (self.tareas)
