import sys
import re
from PySide2 import QtGui, QtCore, QtWidgets

from resource import cus_cal_ui as cal


class CustomCalculator(QtWidgets.QMainWindow, cal.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

        # 초기 설정
        self.result = '0'
        self.lineEdit__res.setText(self.result)

        self.sig_slot()

    def sig_slot(self):
        # TODO 다른 방법도 찾아보자
        self.pushButton_1.clicked.connect(self.num1)
        self.pushButton_2.clicked.connect(self.num2)
        self.pushButton_3.clicked.connect(self.num3)
        self.pushButton_4.clicked.connect(self.num4)
        self.pushButton_5.clicked.connect(self.num5)
        self.pushButton_6.clicked.connect(self.num6)
        self.pushButton_7.clicked.connect(self.num7)
        self.pushButton_8.clicked.connect(self.num8)
        self.pushButton_9.clicked.connect(self.num9)
        self.pushButton_0.clicked.connect(self.num0)

        self.pushButton__add.clicked.connect(self.add)
        self.pushButton__sub.clicked.connect(self.sub)
        self.pushButton__mul.clicked.connect(self.mul)
        self.pushButton__div.clicked.connect(self.div)

        self.pushButton__res.clicked.connect(self.res)
        self.pushButton__clear.clicked.connect(self.clear)

    # todo key press event랑 push button 함수를 따로 만드는거 맞는 듯
    # key event는 따로 호출하지 않아도 함수가 적용이 되어버림
    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == QtCore.Qt.Key_1:
            self.num1()

        if event.key() == QtCore.Qt.Key_2:
            self.num2()

        if event.key() == QtCore.Qt.Key_3:
            self.num3()

        if event.key() == QtCore.Qt.Key_4:
            self.num4()

        if event.key() == QtCore.Qt.Key_5:
            self.num5()

        if event.key() == QtCore.Qt.Key_6:
            self.num6()

        if event.key() == QtCore.Qt.Key_7:
            self.num7()

        if event.key() == QtCore.Qt.Key_8:
            self.num8()

        if event.key() == QtCore.Qt.Key_9:
            self.num9()

        if event.key() == QtCore.Qt.Key_0:
            self.num0()

        if event.key() == QtCore.Qt.Key_Plus:
            self.add()

        if event.key() == QtCore.Qt.Key_Minus:
            self.sub()

        # Multiply -> [*, x]
        if event.key() == QtCore.Qt.Key_Asterisk or event.key() == QtCore.Qt.Key_X:
            self.mul()

        if event.key() == QtCore.Qt.Key_Slash:
            self.div()

        # Delete last char -> D
        if event.key() == QtCore.Qt.Key_D or event.key() == QtCore.Qt.Key_Delete:
            self.result = self.result[:-1]
            # res = ''
            # self.result = list(map(lambda x: x.split(), self.result))[0:-1]
            # for i in self.result:
            #     res += ''.join(i)
            # self.result = res
            self.lineEdit__res.setText(self.result)

        if event.key() == QtCore.Qt.Key_C:
            self.clear()

        # Result -> [return, =]
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Equal:
            self.res()

        else:
            # + or *를 하려면 shift를 눌러야하는데, 그때 0으로 변환되는 오류가 생김
            #  shift 를 눌렀을 때 지정한대로(부모함수) 동작하도록 하기 위해서 super를 써버리면 self.result가 유지된다
            super().keyPressEvent(event)


    def num1(self):
        if self.result == '0':
            self.result = ''
        self.result += '1'
        self.lineEdit__res.setText(self.result)

    def num2(self):
        if self.result == '0':
            self.result = ''
        self.result += '2'
        self.lineEdit__res.setText(self.result)

    def num3(self):
        if self.result == '0':
            self.result = ''
        self.result += '3'
        self.lineEdit__res.setText(self.result)

    def num4(self):
        if self.result == '0':
            self.result = ''
        self.result += '4'
        self.lineEdit__res.setText(self.result)

    def num5(self):
        if self.result == '0':
            self.result = ''
        self.result += '5'
        self.lineEdit__res.setText(self.result)

    def num6(self):
        if self.result == '0':
            self.result = ''
        self.result += '6'
        self.lineEdit__res.setText(self.result)

    def num7(self):
        if self.result == '0':
            self.result = ''
        self.result += '7'
        self.lineEdit__res.setText(self.result)

    def num8(self):
        if self.result == '0':
            self.result = ''
        self.result += '8'
        self.lineEdit__res.setText(self.result)

    def num9(self):
        if self.result == '0':
            self.result = ''
        self.result += '9'
        self.lineEdit__res.setText(self.result)

    def num0(self):
        if self.result == '0':
            self.result = ''
        self.result += '0'
        self.lineEdit__res.setText(self.result)

    def add(self):
        self.result += '+'
        self.lineEdit__res.setText(self.result)

    def sub(self):
        self.result += '-'
        self.lineEdit__res.setText(self.result)

    def mul(self):
        self.result += 'x'
        self.lineEdit__res.setText(self.result)

    def div(self):
        self.result += '/'
        self.lineEdit__res.setText(self.result)

    # x -> * 로 변경 후, eval 적용
    def res(self):
        self.result = re.sub('x', '*', self.result)
        # self.result = re.sub(r'(\d+)[x](\d+)', r'\g<1>*\g<2>', self.result)
        self.lineEdit__res.setText(str(eval(self.result)))
        self.result = '0'

    def clear(self):
        self.result = '0'
        self.lineEdit__res.setText(self.result)


# %s/<찾을문자열>/<변경할문자열>/g
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cc = CustomCalculator()
    cc.show()
    sys.exit(app.exec_())
