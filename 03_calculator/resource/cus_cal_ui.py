# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cus_cal.ui'
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
        MainWindow.resize(268, 366)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit__res = QLineEdit(self.centralwidget)
        self.lineEdit__res.setObjectName(u"lineEdit__res")
        font = QFont()
        font.setPointSize(70)
        self.lineEdit__res.setFont(font)
        self.lineEdit__res.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit__res.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit__res.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.lineEdit__res)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        font1 = QFont()
        font1.setPointSize(20)
        self.pushButton_1.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton__add = QPushButton(self.centralwidget)
        self.pushButton__add.setObjectName(u"pushButton__add")
        self.pushButton__add.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton__add)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton__sub = QPushButton(self.centralwidget)
        self.pushButton__sub.setObjectName(u"pushButton__sub")
        self.pushButton__sub.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton__sub)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font1)

        self.horizontalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font1)

        self.horizontalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font1)

        self.horizontalLayout_3.addWidget(self.pushButton_9)

        self.pushButton__mul = QPushButton(self.centralwidget)
        self.pushButton__mul.setObjectName(u"pushButton__mul")
        self.pushButton__mul.setFont(font1)

        self.horizontalLayout_3.addWidget(self.pushButton__mul)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton__clear = QPushButton(self.centralwidget)
        self.pushButton__clear.setObjectName(u"pushButton__clear")
        self.pushButton__clear.setFont(font1)

        self.horizontalLayout_4.addWidget(self.pushButton__clear)

        self.pushButton_0 = QPushButton(self.centralwidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setFont(font1)

        self.horizontalLayout_4.addWidget(self.pushButton_0)

        self.pushButton__res = QPushButton(self.centralwidget)
        self.pushButton__res.setObjectName(u"pushButton__res")
        self.pushButton__res.setFont(font1)
        # self.pushButton__res.setStyleSheet("background-color: rgb(200, 80, 70)")

        self.horizontalLayout_4.addWidget(self.pushButton__res)

        self.pushButton__div = QPushButton(self.centralwidget)
        self.pushButton__div.setObjectName(u"pushButton__div")
        self.pushButton__div.setFont(font1)

        self.horizontalLayout_4.addWidget(self.pushButton__div)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 268, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton__add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton__sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton__mul.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton__clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton__res.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton__div.setText(QCoreApplication.translate("MainWindow", u"/", None))
    # retranslateUi

