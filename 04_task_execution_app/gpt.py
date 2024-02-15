import sys
import time
import re

from PySide2 import QtCore, QtGui, QtWidgets
from resource.ui import bomb_game_ui as bomb


class Signals(QtCore.QObject):
    progressBar_update = QtCore.Signal(int)
    time_update = QtCore.Signal(str)
    message = QtCore.Signal(str)


class UIThread(QtCore.QThread):
    def __init__(self, in_num: str):
        super().__init__()
        self.signals = Signals()
        self.input_num = in_num

        self.__is_start = False
        self.__is_cancel = True
        self.__is_pause = False

        self.__condition = QtCore.QWaitCondition()
        self.__mutex = QtCore.QMutex()

        self.pattern = re.compile(r'^\d+$')  # Only digits are allowed

    def resume(self):
        if self.__is_pause:
            self.__condition.wakeAll()

    @property
    def is_start(self):
        return self.__is_start

    @is_start.setter
    def is_start(self, flag: bool):
        self.__is_start = flag

    @property
    def is_cancel(self):
        return self.__is_cancel

    @is_cancel.setter
    def is_cancel(self, flag: bool):
        self.__is_cancel = flag

    @property
    def is_pause(self):
        return self.__is_pause

    @is_pause.setter
    def is_pause(self, flag: bool):
        self.__is_pause = flag

    def run(self):
        if not self.pattern.match(self.input_num):
            msg_sig = '숫자만 입력해야해요,, 안그러면 폭탄이 고장나요'
            self.signals.message.emit(msg_sig)
            return

        for x in range(int(self.input_num), -1, -1):
            seconds = x % 60
            minutes = int(x / 60)
            res_time = f'{minutes:02}:{seconds:02}'
            time.sleep(1)
            ratio = int((int(self.input_num) - x) / int(self.input_num) * 100)

            if self.__is_pause:
                self.__condition.wait(self.__mutex)

            if self.__is_cancel:
                return

            self.signals.progressBar_update.emit(ratio)
            self.signals.time_update.emit(res_time)

            if ratio == 100:
                msg_sig = '결국 폭탄이 터졌습니다!!!!'
                self.signals.message.emit(msg_sig)


class Bomb(QtWidgets.QGraphicsEllipseItem):
    def __init__(self):
        super().__init__()

    def create_bomb(self):
        self.setRect(50, 50, 50, 50)
        self.setBrush(QtGui.QColor('grey'))


class Main(QtWidgets.QMainWindow, bomb.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('BOMB BOMB BOMB')
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.__ui_thread = UIThread('')
        self.is_exist_bomb(False)

        self.init_set()

        self.pushButton__start.clicked.connect(self.slot_start)
        self.pushButton__cancle.clicked.connect(self.slot_cancel)
        self.pushButton__pause.clicked.connect(self.slot_pause)

        self.__ui_thread.signals.progressBar_update.connect(self.slot_update_progressbar)
        self.__ui_thread.signals.time_update.connect(self.slot_update_time)
        self.__ui_thread.signals.message.connect(self.slot_msg)

    def slot_msg(self, msg):
        if msg == '결국 폭탄이 터졌습니다!!!!' or msg == '숫자만 입력해야해요,, 안그러면 폭탄이 고장나요':
            self.lineEdit__input_text.setPlaceholderText(msg)
            self.lineEdit__input_text.setText('')
            self.lineEdit__input_text.setReadOnly(False)
            self.scene.removeItem(self.bb)
            self.is_input_err(msg != '결국 폭탄이 터졌습니다!!!!')

        if self.__ui_thread.isRunning():
            self.slot_start()

    def is_input_err(self, check=True):
        self.pushButton__start.setEnabled(check)
        self.pushButton__pause.setEnabled(False)
        self.pushButton__cancel.setEnabled(False)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == QtCore.Qt.Key_Space:
            self.bb.create_bomb()
            self.scene.addItem(self.bb)
            self.graphicsView.setScene(self.scene)
            self.is_exist_bomb()

    def is_exist_bomb(self, check=True):
        if check:
            self.lineEdit__input_text.setReadOnly(False)
            self.lineEdit__input_text.setText('')
            self.lineEdit__input_text.setPlaceholderText('폭탄을 몇 초 후에 터뜨릴까요? ex)120')
            self.pushButton__start.setEnabled(True)

    @QtCore.Slot(str)
    def slot_update_time(self, val):
        self.lcdNumber.display(val)

    @QtCore.Slot(int)
    def slot_update_progressbar(self, val):
        self.progressBar.setValue(val)

    def slot_start(self):
        self.pushButton__start.setEnabled(False)
        self.pushButton__cancle.setEnabled(True)
        self.pushButton__pause.setEnabled(True)
        in_sec = self.lineEdit__input_text.text()

        if not self.__ui_thread.isRunning():
            self.__ui_thread.is_start = True
            self.__ui_thread.is_cancel = False
            self.__ui_thread.is_pause = False

            self.__ui_thread.input_num = in_sec

            if len(self.lineEdit__input_text.text()):
                self.lineEdit__input_text.setPlaceholderText(in_sec)
                self.lineEdit__input_text.setText(
                    f'폭탄이 {in_sec}초만에 터질겁니다!!!으아아!')
                self.lineEdit__input_text.setReadOnly(True)

                self.__ui_thread.start()
                self.__ui_thread.daemon = True
            else:
                self.lineEdit__input_text.setPlaceholderText(
                    '입력해주세요. 폭탄을 몇 초 후에 터뜨릴까요? ex)120')

        else:
            if self.__ui_thread.is_pause:
                self.__ui_thread.resume()
                self.__ui_thread.is_pause = False

    def slot_cancel(self):
        self.pushButton__cancel.setEnabled(False)
        self.pushButton__start.setEnabled(True)
        self.pushButton__pause.setEnabled(False)

        self.__ui_thread.is_start = False

    def slot_cancel(self):
        self.pushButton__cancel.setEnabled(False)
        self.pushButton__start.setEnabled(True)
        self.pushButton__pause.setEnabled(False)

        self.__ui_thread.is_start = False
        self.__ui_thread.is_cancel = True
        self.lineEdit__input_text.setReadOnly(True)
        self.lineEdit__input_text.setPlaceholderText('폭탄을 철거합니다')
        self.scene.removeItem(self.bb)
        self.init_set()

    def slot_pause(self):
        self.pushButton__pause.setEnabled(False)
        self.pushButton__start.setEnabled(True)
        self.pushButton__cancel.setEnabled(True)

        self.__ui_thread.is_pause = True
        self.__ui_thread.is_cancel = False

    def init_set(self):
        self.progressBar.setValue(0)
        self.lcdNumber.display('00:00')
        self.lineEdit__input_text.setText('')

        self.bb = Bomb()
        self.scene = QtWidgets.QGraphicsScene()

        self.pushButton__pause.setEnabled(False)
        self.pushButton__cancle.setEnabled(False)
        self.pushButton__start.setEnabled(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    bg = Main()
    bg.show()
    sys.exit(app.exec_())
