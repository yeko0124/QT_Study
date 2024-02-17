import sys
import re
from PySide2 import QtGui, QtCore, QtWidgets

from resource import cus_cal_ui as cal


class CustomCalculator(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.vlayout = QtWidgets.QVBoxLayout(self)
        self.grid_layout = QtWidgets.QGridLayout()
        self.line_edit = QtWidgets.QLineEdit()

        self.set_ui_btn()

        self.vlayout.addWidget(self.line_edit)
        self.vlayout.addLayout(self.grid_layout)

        self.setLayout(self.vlayout)

    def set_ui_lnedit(self):
        pass

    def set_ui_btn(self):
        for i in range(0, 12):
            if i == 9:
                btn = QtWidgets.QPushButton('C')
            elif i == 10:
                btn = QtWidgets.QPushButton('0')
            elif i == 11:
                btn = QtWidgets.QPushButton('=')
            else:
                btn = QtWidgets.QPushButton(str(i+1))
            btn.clicked.connect(self.slot_clicked_btn)
            self.grid_layout.addWidget(btn, int(i//3), int(i % 3))

    def slot_clicked_btn(self):
        data: QtWidgets.QPushButton = self.sender()
        res = self.line_edit.text().strip()
        self.line_edit.setText(res + data.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    cc = CustomCalculator()
    cc.show()
    sys.exit(app.exec_())
