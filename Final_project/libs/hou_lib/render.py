import hou
import re

from PySide2 import QtWidgets
from libs.db import DBVersionUp


class HRender(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__db = DBVersionUp()

        w = QtWidgets.QWidget()
        self.h = QtWidgets.QHBoxLayout()
        self.v = QtWidgets.QVBoxLayout()

        self.render = QtWidgets.QPushButton('render')
        self.h.addWidget(self.render)

        w.setLayout(self.h)
        self.setCentralWidget(w)

        self.ver_ctn = 0
        self.render.clicked.connect(self.slot_render_btn)

    def slot_render_btn(self):
        self.ver_ctn = (self.read_file_version_cnt())
        print(f'ver_{self.ver_ctn}')
        self.read_usd_rop()

    def read_usd_rop(self):
        # todo usd node가 여러개 있을 땐, 선택한 것만 render가 되도록 할 수는 없는걸까?
        for item in hou.node("/stage").children():
            if item.type().name() == 'usd_rop':
                rop_name = item.name()  # 사용자가 설정한 usd_rop name
                postrender_expression = self.make_post_file(rop_name)
                item.parm('postrender').set(postrender_expression)
                item.parm('tpostrender').set(True)
                item.parm('tprerender').set(False)
                item.parm('tpostframe').set(False)
                item.parm('tpreframe').set(False)
                # render start
                item.parm('execute').pressButton()

    # usd(rop)name의 파일이 이미 존재할 경우,
    # 파일의 개수를 읽어와서 version 카운트 이어갈 수 있기 위한 메서드
    def read_file_version_cnt(self) -> int:
        name = self.read_rop_name()
        ver_ctn = self.__db.count_cache_by_name(name) + 1
        print('version:', ver_ctn)
        return ver_ctn

    def make_post_file(self, usd_name) -> str:
        with open('/Users/yeko/Desktop/netflix_TD/Final_project/libs/hou_lib/no_symlink_post_render_pre_input.py', 'r') as original_file:
            file_contents = original_file.read()
        # replace version count
        modified_version = re.sub(r'version', f'v00{self.ver_ctn}', file_contents)
        # replace usd_name(rop_name)
        modified_contents = re.sub(r'input', usd_name, modified_version)
        with open('/Users/yeko/Desktop/netflix_TD/Final_project/libs/hou_lib/post_render.py', 'w') as new_file:
            new_file.write(modified_contents)
        return modified_contents

    @staticmethod
    def read_rop_name():
        for item in hou.node("/stage").children():
            if item.type().name() == 'usd_rop':
                rop_name = item.name()
                return rop_name


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ht= HRender()
    ht.show()
    app.exec_()
