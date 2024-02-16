

# [hw-point]
# 시작 버튼 클릭 -> 명령 실행 예약 타이머 시작
# 정지 버튼 클릭 -> 명령 실행 예약 타이머 정지(종료)
# 일시 정지 버튼 클릭 -> 명령 실행 예약 타이머 일시 정지
#
# 타이머 UI
# 시작, 중단, 일시 정지 기능 (예약 타이머)
# 입력한 시간에 도달 -> 특정 명령 실행 (명령은 알아서)
# 명령 실행도 Thread 이용
# 5분을 입력 -> 5분 후에 특정 명령 실행
# -------------

# 응용 -> 나의 것으로 .

"""
<폭탄 설치 게임> feat.지영양
방향키로 돌아다니다가, 스페이스바를 누르면 폭탄을 그 자리에 놓으면, 몇 초 후 터트릴건지 물어봄.
(-> 이건 후디니api로 해볼까. 폭탄이 cube)

폭탄을 설치하면(스페이스바) -> 몇초 후 터트릴건지 타이머 설정(input)
-> 시작버튼누르면 폭탄 타이머 시작
-> 철거버튼 누르면 폭탄 타이머 종료(정지)
-> 일시정지버튼 누르면 폭탄 타이머 일시정지
시간에 도달하면, 폭탄 사라지기
++ 시간 도달 10초 전에 카운트다운 10, 9, 8----0 타이머 셀 수 있도록 하면 재밌을 듯 ++ -> 의미없음 기각.
"""

import sys
import time
import re

from PySide2 import QtCore, QtGui, QtWidgets
from resource.ui import bomb_game_ui as bomb


# 시그널 클래스
class Signals(QtCore.QObject):
    progressBar_update = QtCore.Signal(int)
    time_update = QtCore.Signal(str)
    message = QtCore.Signal(str)


# 스레드 클래스
class UIThread(QtCore.QThread):
    def __init__(self, in_num: str):
        super().__init__()
        self.signals = Signals()
        self.input_num = in_num  # 사용자로부터 인풋값을 받아 타이머로 활용

        self.__is_start = False
        self.__is_cancel = True
        self.__is_pause = False

        self.__condition = QtCore.QWaitCondition()
        self.__mutex = QtCore.QMutex()   # 스레드 기다려

        # self.pattern = re.compile('^\d+$')  # 숫자만 넣어야 함

    def resume(self):
        if self.__is_pause:
            self.__condition.wakeAll()  # 일시 정지일 시, 다시 시작

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
            # 카운트 다운. 60초 -> 1분 -> 나눗셈 후, 나머지와 몫으로 분 초를 계산
            seconds = int(x % 60)
            minutes = int(x / 60)
            res_time = f'{minutes:02}:{seconds:02}'
            ratio = int((int(self.input_num) - x) / int(self.input_num) * 100)
            time.sleep(1)

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


# 폭탄 클래스
class Bomb(QtWidgets.QGraphicsEllipseItem):
    def __init__(self):
        super().__init__()

    def create_bomb(self, pos):
        x, y = pos
        self.setRect(x, y, 50, 50)
        self.setBrush(QtGui.QColor('black'))


class Main(QtWidgets.QMainWindow, bomb.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pixmap_item = None
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.__ui_thread = UIThread('')
        self.is_exist_bomb(False)

        self.pattern = re.compile('^\d+$')  # 숫자만 넣어야 함

        # 초기값 세팅
        self.init_set()

        # 지영 등장
        self.set_user

        self.pushButton__start.clicked.connect(self.slot_start)
        self.pushButton__cancle.clicked.connect(self.slot_cancel)
        self.pushButton__pause.clicked.connect(self.slot_pause)

        # 시그널
        self.__ui_thread.signals.progressBar_update.connect(self.slot_update_progressbar)
        self.__ui_thread.signals.time_update.connect(self.slot_update_time)
        self.__ui_thread.signals.message.connect(self.slot_msg)

    @property
    def set_user(self):
        pixmap = QtGui.QPixmap('/Users/yeko/Desktop/netflix_TD/self_study/qt_study/04_task_execution_app/resource/png/jy.png').scaled(100,150)
        self.pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmap_item)
        self.graphicsView.setScene(self.scene)

    @set_user.setter
    def set_user(self, val: tuple):
        x, y = val
        self.pixmap_item: QtWidgets.QGraphicsPixmapItem
        self.pixmap_item.moveBy(x, y)

    def slot_msg(self, msg):
        # end
        if msg == '결국 폭탄이 터졌습니다!!!!':
            self.lineEdit__input_text.setText(msg)
            self.scene.removeItem(self.bb)
            # self.set_end()
        # elif msg == '숫자만 입력해야해요,, 안그러면 폭탄이 고장나요':
        #     self.lineEdit__input_text.setText(msg)
        #     self.lineEdit__input_text.setReadOnly(True)
        #     self.is_input_err()
        if self.__ui_thread.isRunning():
            self.slot_start()
    #
    # def set_end(self):
    #     self.pushButton__start.setEnabled(False)
    #     self.pushButton__pause.setEnabled(True)
    #     self.pushButton__cancel.setEnabled(False)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if not self.__ui_thread.isRunning():
            # 스레드가 실행될 때는 폭탄을 다시 옮길 수가 없음
            if event.key() == QtCore.Qt.Key_Space:
                # 지영님이 있는 위치값에 폭탄 생성
                self.bb.create_bomb((self.pixmap_item.pos().x(), self.pixmap_item.pos().y()))
                self.scene.addItem(self.bb)
                self.is_exist_bomb()

        # 지영님 위치 이동
        if event.key() == QtCore.Qt.Key_D:  # 우
            self.set_user = (30, 0)

        if event.key() == QtCore.Qt.Key_A:  # 좌
            self.set_user = (-30, 0)

        if event.key() == QtCore.Qt.Key_S:  # 하
            self.set_user = (0, 30)

        if event.key() == QtCore.Qt.Key_W:  # 상
            self.set_user = (0, -30)

    def is_exist_bomb(self, check=True):
        # 폭탄이 생기면 발생하는 함수
        if check:
            self.lineEdit__input_text.setReadOnly(False)
            self.lineEdit__input_text.setText('')
            self.lineEdit__input_text.setPlaceholderText('폭탄을 몇 초 후에 터뜨릴까요? ex)120')
            self.pushButton__start.setEnabled(True)

    @QtCore.Slot(str)
    def slot_update_time(self, val):
        self.lcdNumber.display(val)
        if val == '00:00':
            self.graphicsView.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(255, 50, 10)))
            self.pushButton__pause.setEnabled(False)

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
            raise ValueError(f'\n{in_sec}is not only number.')

        if not self.__ui_thread.isRunning():
            self.__ui_thread.is_start = True
            self.__ui_thread.is_cancel = False
            self.__ui_thread.is_pause = False

            self.__ui_thread.input_num = in_sec
            if len(self.lineEdit__input_text.text()):
                # 60초 이내 (초 단위 알림)
                if 1 > (int(in_sec)/60) > 0:
                    self.lineEdit__input_text.setText(
                        f'폭탄이 {int(in_sec)%60:0.0f}초 만에 터질겁니다!!!으아아!')
                else:
                    # 60초 이후 (분, 초 단위 알림)
                    self.lineEdit__input_text.setText(
                        f'폭탄이 {int(in_sec)/60:0.0f}분 {int(in_sec)%60:0.0f}초 만에 터질겁니다!!!으아아!')
                self.lineEdit__input_text.setReadOnly(True)

                self.__ui_thread.start()
                self.__ui_thread.daemon = True
            else:
                # print('err')
                self.lineEdit__input_text.setPlaceholderText('입력해주세요. 폭탄을 몇 초 후에 터뜨릴까요? ex)120')

        else:
            if self.__ui_thread.is_pause:
                self.__ui_thread.resume()
                self.__ui_thread.is_pause = False

    def slot_cancel(self):
        self.graphicsView.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(255, 255, 200)))
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
        self.graphicsView.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(255, 255, 200)))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    bg = Main()
    bg.show()
    sys.exit(app.exec_())