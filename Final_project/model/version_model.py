

from PySide2 import QtWidgets, QtGui, QtCore


class VersionModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.__data = data