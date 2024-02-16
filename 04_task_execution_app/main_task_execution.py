
"""
시작 버튼 클릭하면, 명령 실행 예약 타이머 시작
정지 버튼 클릭하면, 명령 실행 예약 타이머 정지(종료)
일시 정지 버튼 클릭하면, 명령 실행 예약 타이머 일시 정지

타이머 UI
시작, 중단, 일시 정지 기능 (예약 타이머)
입력한 시간에 도달하면 특정 명령 실행 (명령은 알아서 아무거나)
명령 실행도 Thread 이용
5분을 입력하면 5분 후에 특정 명령 실행
-------------

--------- <숙제 성공하면> ----------------------
<폭탄 설치 게임>
방향키로 돌아다니다가, 스페이스바를 누르면 폭탄을 그 자리에 놓으면, 몇 분후 터트릴건지 물어봄. (min, sec)
-> 이건 후디니api로 해볼까. 폭탄이 cube

폭탄을 설치하면(스페이스바) -> 몇초 후 터트릴건지 타이머 설정(input)
-> 시작버튼(빨간색)누르면 폭탄 타이머 시작 (
-> 정지버튼(회색) 누르면 폭탄 타이머 종료(정지)
-> 일시정지버튼(노란색) 누르면 폭탄 타이머 일시정지
시간에 도달하면, 폭탄 터지는 그림(or gif?)
++ 시간 도달 10초 전에 카운트다운 10, 9, 8----0 타이머 셀 수 있도록 하면 재밌을 듯 ++
"""
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

        # self.pattern = re.compile('^\d+$')  # 숫자만 넣어야 함

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
        # if not self.pattern.match(self.input_num):
        #     msg_sig = '숫자만 입력해야해요,, 안그러면 폭탄이 고장나요'
        #     self.signals.message.emit(msg_sig)
        #     raise ValueError('숫자 입력!')

        for x in range(int(self.input_num), -1, -1):
            seconds = x % 60
            minutes = int(x / 60)
            res_time = f'{minutes:02}:{seconds:02}'
            time.sleep(1)
            ratio = int((int(self.input_num) - x) / int(self.input_num) * 100)

            if self.__is_pause:
                self.__condition.wait(self.__mutex)

            if self.__is_cancel:
                break

            self.signals.progressBar_update.emit(ratio)
            self.signals.time_update.emit(res_time)
            # print(res_time)

            if ratio == 100:
                msg_sig = '결국 폭탄이 터졌습니다!!!!'
                self.signals.message.emit(msg_sig)


# class User(QtWidgets.QGraphicsEllipseItem):
#     def __init__(self):
#         super().__init__()
#
#     def create_user(self):
#         self.setRect(20, 20, 20, 20)
#         self.setBrush(QtGui.QColor('brown'))
#         self.setRect(20, 5, 10, 5)


class Bomb(QtWidgets.QGraphicsEllipseItem):
    def __init__(self):
        super().__init__()

    def create_bomb(self):
        self.setRect(50, 50, 50, 50)
        self.setBrush(QtGui.QColor('black'))


class Main(QtWidgets.QMainWindow, bomb.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.__ui_thread = UIThread('')
        self.is_exist_bomb(False)

        self.pattern = re.compile('^\d+$')  # 숫자만 넣어야 함

        self.init_set()

        self.pushButton__start.clicked.connect(self.slot_start)
        self.pushButton__cancle.clicked.connect(self.slot_cancel)
        self.pushButton__pause.clicked.connect(self.slot_pause)

        self.__ui_thread.signals.progressBar_update.connect(self.slot_update_progressbar)
        self.__ui_thread.signals.time_update.connect(self.slot_update_time)
        self.__ui_thread.signals.message.connect(self.slot_msg)

    def slot_msg(self, msg):
        # end
        if msg == '결국 폭탄이 터졌습니다!!!!':
            self.lineEdit__input_text.setText(msg)
            self.scene.removeItem(self.bb)
            self.is_input_err(False)
        # elif msg == '숫자만 입력해야해요,, 안그러면 폭탄이 고장나요':
        #     self.lineEdit__input_text.setText(msg)
        #     self.lineEdit__input_text.setReadOnly(True)
        #     self.is_input_err()

        if self.__ui_thread.isRunning():
            self.slot_start()

    def is_input_err(self, check=True):
        if check is False:
            self.pushButton__start.setEnabled(False)
            self.pushButton__pause.setEnabled(False)
            self.pushButton__cancle.setEnabled(False)
        else:
            pass

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

        if not self.pattern.match(in_sec):
            self.lineEdit__input_text.setText('숫자만 입력해야해요,, 안그러면 폭탄이 고장나요')
            self.lineEdit__input_text.setReadOnly(True)
            self.pushButton__pause.setEnabled(False)
            raise ValueError('숫자 입력!')

        if not self.__ui_thread.isRunning():
            self.__ui_thread.is_start = True
            self.__ui_thread.is_cancel = False
            self.__ui_thread.is_pause = False

            self.__ui_thread.input_num = in_sec
            if len(self.lineEdit__input_text.text()):
                if 1 > (int(in_sec)/60) > 0:
                    self.lineEdit__input_text.setText(
                        f'폭탄이 {int(in_sec)%60:0.0f}초 만에 터질겁니다!!!으아아!')
                else:
                    self.lineEdit__input_text.setText(
                        # TODO 분으로 넘어갈 때, 분/ 초로 나눌 수 있도록
                        f'폭탄이 {int(in_sec)/60:0.0f}분 {int(in_sec)%60:0.0f}초 만에 터질겁니다!!!으아아!')
                self.lineEdit__input_text.setReadOnly(True)

                self.__ui_thread.start()
                self.__ui_thread.daemon = True
            else:
                # print('err')
                self.lineEdit__input_text.setPlaceholderText(
                    '입력해주세요. 폭탄을 몇 초 후에 터뜨릴까요? ex)120')

        else:
            if self.__ui_thread.is_pause:
                self.__ui_thread.resume()
                self.__ui_thread.is_pause = False

    def slot_cancel(self):
        self.pushButton__cancle.setEnabled(False)
        self.pushButton__start.setEnabled(False)
        self.pushButton__pause.setEnabled(False)

        self.__ui_thread.is_start = False
        self.__ui_thread.is_cancel = True
        self.lineEdit__input_text.setReadOnly(True)
        self.lineEdit__input_text.setText('폭탄을 철거합니다')
        self.scene.removeItem(self.bb)
        self.progressBar.setValue(0)
        self.lcdNumber.display('00:00')

    def slot_pause(self):
        self.pushButton__pause.setEnabled(False)
        self.pushButton__start.setEnabled(True)
        self.pushButton__cancle.setEnabled(True)

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


