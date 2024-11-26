
import sys

from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QAbstractTableModel

class ModeloTabla (QAbstractTableModel):
    def __init__(self,tabla):
        super().__init__()
        self.tabla = tabla

    def data(self,indice,rol):
        if rol == Qt.ItemDataRole.EditRole or rol == Qt.ItemDataRole.DisplayRole:
            valor = self.tabla [indice.row()][indice.column()]
            return valor
        if rol == Qt.ItemDataRole.BackgroundRole:
            if self.tabla[indice.row()][2] == "Hombre":
                return QtGui.QColor('pink')
            elif self.tabla[indice.row()][2] == "Mujer":
                return QtGui.QColor('lightblue')
            elif self.tabla[indice.row()][2] == "Otro":
                return QtGui.QColor('orange')
        if rol == Qt.ItemDataRole.ForegroundRole:
            if self.tabla[indice.row()][3] == True:
                return QtGui.QColor('white')
                #if (indice.colum()==3):
                    #return QtGui.QColor('red')
        if rol == Qt.ItemDataRole.DecorationRole:
            if isinstance(self.tabla[indice.row()][indice.column()],bool):
                if self.tabla[indice.row()][indice.column()]:
                    return QtGui.QIcon('tick.png')

    def rowCount(self,indice):
        return len (self.tabla)

    def columnCount(self,indice):
        return len (self.tabla[0])
