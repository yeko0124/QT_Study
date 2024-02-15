# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bomb_game.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(691, 283)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setFrameShadow(QFrame.Plain)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_3.addWidget(self.graphicsView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        font = QFont()
        font.setPointSize(30)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_3.addWidget(self.lcdNumber)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton__cancle = QPushButton(self.centralwidget)
        self.pushButton__cancle.setObjectName(u"pushButton__cancle")

        self.horizontalLayout.addWidget(self.pushButton__cancle)

        self.pushButton__pause = QPushButton(self.centralwidget)
        self.pushButton__pause.setObjectName(u"pushButton__pause")
        self.pushButton__pause.setCheckable(False)

        self.horizontalLayout.addWidget(self.pushButton__pause)

        self.pushButton__start = QPushButton(self.centralwidget)
        self.pushButton__start.setObjectName(u"pushButton__start")

        self.horizontalLayout.addWidget(self.pushButton__start)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit__input_text = QLineEdit(self.centralwidget)
        self.lineEdit__input_text.setObjectName(u"lineEdit__input_text")
        self.lineEdit__input_text.setAlignment(Qt.AlignCenter)
        self.lineEdit__input_text.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit__input_text)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 691, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"How to Play", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" SpaceBar: \ud3ed\ud0c4\uc124\uce58", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" \ubc29\ud5a5\ud0a4: \uce90\ub9ad\ud130 \ubc29\ud5a5", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"------------------", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\ud3ed\ud0c4\uc124\uce58 \ud6c4, \ud0c0\uc774\uba38 \uc124\uc815", None))
        self.pushButton__cancle.setText(QCoreApplication.translate("MainWindow", u"\ucca0\uac70", None))
        self.pushButton__pause.setText(QCoreApplication.translate("MainWindow", u"\uc815\uc9c0", None))
        self.pushButton__start.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.label_5.setText("")
        self.lineEdit__input_text.setText("")
        self.lineEdit__input_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ud3ed\ud0c4\uc744 \uc124\uce58\ud558\uae30 \uc804\uc785\ub2c8\ub2e4.", None))
    # retranslateUi

