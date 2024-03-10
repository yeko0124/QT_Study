import functools
import os

from PySide2 import QtGui, QtWidgets, QtCore

import hou
import importlib
import pathlib

from model import version_model
from view import version_view

from libs import db
from ui import version_track_ui
importlib.reload(version_track_ui)


class TableWidget(QtWidgets.QWidget, version_track_ui.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__db = db.DBVersionUp()


class VersionTable(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        w = QtWidgets.QWidget()
        self.__vbox_layout = QtWidgets.QVBoxLayout()

        self.final_dir_btn = QtWidgets.QPushButton('Open Final Directory')
        self.__vbox_layout.addWidget(self.final_dir_btn)

        self.__widget_lst = list()
        self.__db = db.DBVersionUp()
        self.setup_widget()

        w.setLayout(self.__vbox_layout)
        self.setCentralWidget(w)

        self.final_dir_btn.clicked.connect(self.open_final_dir)

    def open_final_dir(self):
        final_dpath = '/Users/yeko/workspace/final'
        QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Open Dir', final_dpath)

    def setup_widget(self):
        f_name = self.__db.get_final_name()
        f_id = self.__db.get_final_id()
        for i, n in enumerate(f_name):
            label_name = n[0]
            widget = TableWidget()
            widget.label.setText(label_name)
            self.__vbox_layout.addWidget(widget)
            self.set_combobox(f_id[i])
            widget.comboBox.addItems(self.com_lst)

            widget.pushButton__reload.clicked.connect(functools.partial(self.reload_symbolic_link, f_id[i]))
            widget.pushButton__open.clicked.connect(functools.partial(self.open_link, f_id[i]))
            # widget.comboBox.
            self.__widget_lst.append(widget)

    def reload_symbolic_link(self, f_id):
        w: TableWidget = self.__widget_lst[f_id-1]
        v_num = w.comboBox.currentIndex()
        path = self.__db.get_one_cache_path(f_id)
        print(path[v_num][0])

        src_path = pathlib.Path(path[v_num][0])
        print(w.label.text())
        dst_final = pathlib.Path(f'/Users/yeko/workspace/final/{w.label.text()}')
        print(dst_final)
        if os.path.exists(dst_final):
            os.remove(dst_final)
            print('remove complete')

        print('link start!!!!')
        os.symlink(src_path, dst_final)
        print('complete')

    def open_link(self, f_id):
        w: TableWidget = self.__widget_lst[f_id-1]
        v_num = w.comboBox.currentIndex()
        path = self.__db.get_one_cache_path(f_id)
        print(path[v_num][0])

    def set_combobox(self, f_id):
        cnt = 1
        self.com_lst = list()
        fid = self.__db.get_cache_files()  # [1, 1, 2, 2, 2, 1, 3, 1, 3]
        for file_id in fid:
            if f_id == file_id:
                self.com_lst.append(f'version{cnt}')
                cnt += 1
            else:
                continue


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    version_table = VersionTable()
    version_table.show()
    app.exec_()