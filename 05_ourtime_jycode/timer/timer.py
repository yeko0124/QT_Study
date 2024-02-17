#!/usr/bin/env python
# encoding= = utf - 8

# author : jy
# created date: 2024.02.16
# modified data: 2024.02.16
# description
# Todo : 음악넣기 ,사용자가 자유로운 시간설정, 그에맞춰 디졸브 흐르기
#명령 실행 예약
'''
시작 중지 일시정지
시작 버튼 클릭하면, 명령 실행 예약 타이머 시작
정지 버튼 클릭하면, 명령 실행 예약 타이머 정지
일시 정지 버튼 클릭하면, 명령 실행 예약 타이머 일시 정지 (edited)
'''
import sys
import logging
import typing

import importlib
from datetime import datetime
from PySide2 import QtWidgets, QtCore, QtGui

from PySide2.QtCore import QMutexLocker
from PySide2.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QPropertyAnimation, QByteArray
from PySide2.QtWidgets import QGraphicsOpacityEffect

import time
from resource.ui import timer_ui
from resource.lib import qt_lib
from resource.lib import sys_lib
from resource.algorithm.algo_lib import BitMask

importlib.reload(timer_ui)
importlib.reload(qt_lib)
importlib.reload(sys_lib)


is_logging_active = True


class MessageSig:
    message = ''
    is_err = False


class Signals(QtCore.QObject):
    progress_update = QtCore.Signal(int)
    message = QtCore.Signal(str)


class Constant:
    __slots__ = ()
    START: typing.Final[int] = 1
    PAUSE: typing.Final[int] = 2
    STOP: typing.Final[int] = 4
# Constant = Constant()


class UIThread(QtCore.QThread):
    def __init__(self):
        super().__init__()
        self.__signals = Signals()
        self.__bitfield = BitMask()

        self.__is_start = False
        self.__is_stop = True
        self.__is_pause = False

        self.total_time = 0

        # init
        self.bitfield.activate(Constant.STOP)  # 0000 0100
        self.is_running = False

        # self.__condition = QtCore.QWaitCondition()
        # self.__mutex = QtCore.QMutex()

    @property
    def signals(self):
        return self.__signals

    @property
    def bitfield(self):
        return self.__bitfield

    @property
    def is_stop(self):
        return self.__is_stop

    @is_stop.setter
    def is_stop(self, flag: bool):
        self.__is_stop = flag

    def resume(self):
        self.__condition.wakeAll()

    @property
    def is_pause(self):
        return self.__is_pause

    @is_pause.setter
    def is_pause(self, flag):
        self.__is_pause = flag
        if not flag:
            self.resume()

    def run(self):
        self.is_running = True
        while self.is_running:
            self.__mutex.lock()
            if self.is_pause:
                self.__condition.wait(self.__mutex)
            if not self.is_running:
                break
            self.__mutex.unlock()
            self.update_time()

    def update_time(self):
        while self.is_running and self.total_time > 0:
            self.__mutex.lock()
            if self.is_pause:
                self.__condition.wait(self.__mutex)
            self.total_time -= 1
            self.signals.progress_update.emit(self.total_time)
            self.__mutex.unlock()
            time.sleep(1)  # 1초 대기
        if self.total_time <= 0:
            today = datetime.today()
            f_today = today.strftime("%Y년 %m월 %d일")
            end_time = f"{f_today}, 우린 30초 동안 같이 있었어. - 아비정전"
            self.signals.message.emit(end_time)
            self.is_running = False


class Timer(QtWidgets.QMainWindow, timer_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

        # 초기 상태
        self.init_set()

        # variables
        self.__handler = qt_lib.LogHandler(out_stream=self.lineEdit__status)

        self.__ui_thread = UIThread()
        self.pushButton_start.clicked.connect(self.slot_start)
        self.pushButton_stop.clicked.connect(self.slot_stop)
        self.pushButton_pause.clicked.connect(self.slot_pause)
        self.__ui_thread.signals.progress_update.connect(self.updateLCDNumber)
        self.__ui_thread.signals.message.connect(self.showMessage)
        self.time_update_timer = QtCore.QTimer(self)  # 현재 시간 업데이트를 위한 타이머
        self.time_update_timer.timeout.connect(self.updateCurrentTime)
        self.time_update_timer.start(1000)  # 1초마다 업데이트

        logging.basicConfig(filename='timer.log', level=logging.INFO, format='%(asctime)s - %(message)s')

        # QGraphicsView 및 QGraphicsScene 설정
        self.initGraphics()

        # 애니메이션 관련 속성 초기화
        self.initAnimationProperties()

    def initGraphics(self):
        self.graphicsView = QtWidgets.QGraphicsView(self)
        self.graphicsView.setGeometry(10, 220, 291, 201)  # QGraphicsView의 위치와 크기 설정
        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)

        # 이미지 로드 및 QGraphicsPixmapItem 생성
        self.pixmap1 = QPixmap('/home/rapa/git_workspace/QT_Study/05_ourtime_jycode/timer/resource/png/before.png')
        self.pixmap2 = QPixmap('/home/rapa/git_workspace/QT_Study/05_ourtime_jycode/timer/resource/png/after.png')

        # QGraphicsOpacityEffect 생성 및 item2에 적용
        self.opacityEffect = QGraphicsOpacityEffect()

        self.item1 = QGraphicsPixmapItem(
            self.pixmap1.scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.item2 = QGraphicsPixmapItem(
            self.pixmap2.scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.item2.setOpacity(0)  # 초기 투명도 설정

        # scene에 item1과 item2 추가
        self.scene.addItem(self.item1)
        self.scene.addItem(self.item2)

        # 투명도 효과 및 애니메이션 설정
        self.opacityEffect = QGraphicsOpacityEffect()
        self.item2.setGraphicsEffect(self.opacityEffect)

        self.animation = QPropertyAnimation(self.opacityEffect, QByteArray(b'opacity'))
        self.animation.setDuration(5000)  # 애니메이션 지속 시간 설정 (5초)
        self.animation.setStartValue(0)  # 시작 투명도
        self.animation.setEndValue(1)  # 종료 투명도


    def init_set(self):
        self.pushButton_pause.setEnabled(False)
        self.pushButton_stop.setEnabled(False)
        self.pushButton_start.setEnabled(True)
        self.__ui_thread = UIThread()

    def initAnimationProperties(self):
        self.opacityLevel = 0.0  # 투명도 초기값
        self.animationDuration = 30000  # 애니메이션 지속 시간 (ms)
        self.animationStep = 0.01  # 투명도 변경 단계
        self.animationTimer = QtCore.QTimer(self)  # 애니메이션 타이머
        self.animationTimer.timeout.connect(self.updateOpacity)
        self.timerInterval = self.animationDuration * self.animationStep
        self.animationTimer.setInterval(self.timerInterval)


    def slot_start(self):
        self.pushButton_stop.setEnabled(True)
        self.pushButton_pause.setEnabled(True)
        self.pushButton_start.setEnabled(False)
        self.__ui_thread.is_pause = False
        self.__ui_thread.total_time = 30
        self.startAnimation()

        if not self.__ui_thread.isRunning():
            self.__ui_thread.is_running = True  # 이 부분을 수정하여 적절한 속성을 사용합니다.
            self.__ui_thread.start()
        self.startAnimation()

    def startAnimation(self):
        self.item2.setOpacity(self.opacityLevel)  # 초기 투명도 설정
        self.animationTimer.start(self.animationDuration // (1 / self.animationStep))
        self.opacityLevel = 0.0  # 애니메이션 시작 전 투명도 초기화
        # 애니메이션 설정
        self.animation.setTargetObject(self.opacityEffect)  # 대상 객체를 명시적으로 설정
        self.animation.setStartValue(0)  # 시작 투명도 설정
        self.animation.setEndValue(1)  # 종료 투명도 설정
        self.animation.setDuration(1000)  # 애니메이션 지속 시간 설정 (5초)
        self.animation.start()  # 애니메이션 시작

    def updateOpacity(self):
        self.opacityLevel += self.animationStep
        if self.opacityLevel > 1:
            self.opacityLevel = 1
            self.animationTimer.stop()
        self.item2.setOpacity(self.opacityLevel)
        self.scene.update()


    def emit(self, record):
        msg = self.format(record)
        self.__out_stream.appendPlainText(msg)

    def slot_stop(self):
        self.pushButton_stop.setEnabled(False)
        self.pushButton_pause.setEnabled(False)
        self.pushButton_start.setEnabled(True)

        self.__ui_thread.is_running = False

    def slot_pause(self):
        self.pushButton_stop.setEnabled(True)
        self.pushButton_pause.setEnabled(False)
        self.pushButton_start.setEnabled(True)

        self.__ui_thread.is_pause = True


    def updateCurrentTime(self):
        global is_logging_active  # 전역 변수 사용 선언

        if self.__ui_thread.is_running and not self.__ui_thread.is_pause:
            # 시작 시간을 로그로 기록
            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if is_logging_active:  # 로그 기록이 활성화된 경우에만 로그를 기록
                logging.info(f"우리의 현재 : {start_time}")
        elif self.__ui_thread.total_time <= 0:
            # 종료 시간을 로그로 기록
            end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if is_logging_active:  # 로그 기록이 활성화된 경우에만 로그를 기록
                logging.info(f"우리의 추억: {end_time}")

            # 타이머 종료 시 로그 기록을 비활성화
            is_logging_active = False



    def startCountdown(self):
        self.countdownThread.start()
        logging.info("Countdown started")

    def stopCountdown(self):
        self.countdownThread.terminate()
        logging.info("Countdown ended")

    def updateLCDNumber(self, timeLeft):
        self.lcdNumber.display(timeLeft)

    def showMessage(self, message):
        QtWidgets.QMessageBox.information(self, "메시지", message)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cfc = Timer()
    cfc.show()
    sys.exit(app.exec_())