'''
houdini calculator
[Make Chocolate]

계산에 맞게 sphere create and automatically dropping
(성공 시, bomb try)  >>> succeed
'''

import sys
import pathlib
import random
import re
from PySide2 import QtGui, QtCore, QtWidgets

import hou


class CustomCalculator(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__json_dir = pathlib.Path(
           '/Users/yeko/Desktop/netflix_TD/self_study/qt_study/03_calculator/resource')

        self.vlayout = QtWidgets.QVBoxLayout(self)
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout2 = QtWidgets.QGridLayout()
        self.line_edit = QtWidgets.QLineEdit()

        self.result_num = ''

        self.set_ui_btn()
        self.set_symbol_btn()

        self.vlayout.addWidget(self.line_edit)
        self.vlayout.addLayout(self.grid_layout)
        self.vlayout.addLayout(self.grid_layout2)

        self.setLayout(self.vlayout)

        hou.setFrame(1)
        self.refresh_item()

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

    def set_symbol_btn(self):
        for i in range(0, 4):
            if i == 0:
                btn = QtWidgets.QPushButton('+')
            elif i == 1:
                btn = QtWidgets.QPushButton('-')
            elif i == 2:
                btn = QtWidgets.QPushButton('//')
            elif i == 3:
                btn = QtWidgets.QPushButton('x')
            btn.clicked.connect(self.slot_clicked_btn)
            self.grid_layout2.addWidget(btn, 0, int(i%4))




    def slot_clicked_btn(self):
        data: QtWidgets.QPushButton = self.sender()
        if data.text() == '=':
            if 'x' in self.line_edit.text():
                a = self.line_edit.text()
                a = re.sub('x', '*', a)
                a = eval(a)
            else:
                a = eval(self.line_edit.text())
                self.sphere_res(a)
                hou.playbar.play()
            self.line_edit.setText(str(a))
            # self.result()
        elif data.text() == 'C':
            self.line_edit.setText('')
        else:
            res = self.line_edit.text().strip()
            self.line_edit.setText(res + data.text())

    # def set_node_pos(self, node, base_pos, add_x, add_y):
    #     node.setPosition((base_pos[0] + add_x, base_pos[1] + add_y))

    def sphere_res(self, q: int):
        h_obj = hou.node("/obj")
        h_geo = h_obj.createNode('geo', 'balls')
        y = 0
        x = 0

        # set node position for good-looking ?
        for i in range(q):
            sp = h_geo.createNode('sphere', f'ball{i+1}')
            if i % 3 == 0:
                x = 0
                y -= 1
            sp.setPosition((x, y))
            # sp.setColor(hou.Color((1, 0, 0)))
            x += 3

        # create merge node and set position
        h_merge = h_geo.createNode('merge')
        h_merge.setPosition((3, y-1))
        # h_merge.setDisplayFlag(True)
        nodes = h_geo.glob('ball*')
        for node in nodes:
            print(node)
            h_merge.setInput(q, node)
            node.parm('ty').set(random.randrange(15,30))
            node.parm('tx').set(random.randrange(-10,10))
            node.parm('tz').set(random.randrange(-10,10))

        color = h_geo.createNode('color')
        color.parm('colorr').set(0.08)
        color.parm('colorg').set(0.03)
        color.parm('colorb').set(0)
        color.setInput(0, h_merge)

        rbd = h_geo.createNode('rbdbulletsolver')
        rbd.parm('useground').set(True)
        rbd.setPosition((3*2, y-2))
        rbd.setDisplayFlag(True)
        rbd.setInput(0, color)

        cube = h_geo.createNode('box')
        cube.setPosition((9, y-1))
        cube.parm('sizex').set(10)
        cube.parm('sizez').set(15)
        cube.parm('rx').set(20)
        cube.parm('ry').set(4)
        cube.parm('rz').set(10)
        cube.parm('ty').set(10)
        # cube.parmTuple('r').set(10,4,5)
        rbd.setInput(3, cube)

    def refresh_item(self):
        for obj in hou.node("/obj").children():
            if obj.type().name() == 'geo':
                for child in obj.children():
                    if child.type().name() == 'sphere':
                        child.destroy()
                obj.destroy()

    def set_position(self, node):
        x = random.uniform(-5, 5)
        y = random.uniform(-5, 5)
        node.setPosition((x, y))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    cc = CustomCalculator()
    cc.show()
    sys.exit(app.exec_())

