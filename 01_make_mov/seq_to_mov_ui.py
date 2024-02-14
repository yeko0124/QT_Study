# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seq_to_mov.ui'
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
        MainWindow.resize(803, 347)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame__img_show = QFrame(self.centralwidget)
        self.frame__img_show.setObjectName(u"frame__img_show")
        self.frame__img_show.setGeometry(QRect(529, 74, 251, 161))
        self.frame__img_show.setFrameShape(QFrame.StyledPanel)
        self.frame__img_show.setFrameShadow(QFrame.Raised)
        self.label__img_show = QLabel(self.frame__img_show)
        self.label__img_show.setObjectName(u"label__img_show")
        self.label__img_show.setGeometry(QRect(20, 20, 211, 121))
        font = QFont()
        font.setPointSize(12)
        self.label__img_show.setFont(font)
        self.label__img_show.setFrameShape(QFrame.Box)
        self.label__img_show.setFrameShadow(QFrame.Raised)
        self.label__img_show.setScaledContents(False)
        self.label__img_show.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 491, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit__dirpath = QLineEdit(self.layoutWidget)
        self.lineEdit__dirpath.setObjectName(u"lineEdit__dirpath")

        self.horizontalLayout.addWidget(self.lineEdit__dirpath)

        self.pushButton__open_dir = QPushButton(self.layoutWidget)
        self.pushButton__open_dir.setObjectName(u"pushButton__open_dir")

        self.horizontalLayout.addWidget(self.pushButton__open_dir)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(19, 50, 491, 231))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.listWidget__seq_grp_lst = QListWidget(self.layoutWidget1)
        self.listWidget__seq_grp_lst.setObjectName(u"listWidget__seq_grp_lst")

        self.verticalLayout.addWidget(self.listWidget__seq_grp_lst)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.listWidget__seq_detail_lst = QListWidget(self.layoutWidget1)
        self.listWidget__seq_detail_lst.setObjectName(u"listWidget__seq_detail_lst")

        self.verticalLayout_2.addWidget(self.listWidget__seq_detail_lst)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit__select_grp = QLineEdit(self.layoutWidget1)
        self.lineEdit__select_grp.setObjectName(u"lineEdit__select_grp")
        self.lineEdit__select_grp.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit__select_grp)

        self.pushButton__convert = QPushButton(self.layoutWidget1)
        self.pushButton__convert.setObjectName(u"pushButton__convert")

        self.horizontalLayout_3.addWidget(self.pushButton__convert)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 803, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sequence Manager", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label__img_show.setText(QCoreApplication.translate("MainWindow", u"PREVIEW", None))
        self.pushButton__open_dir.setText(QCoreApplication.translate("MainWindow", u"Open Dir", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Seq Group List", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Seq Detail List", None))
        self.pushButton__convert.setText(QCoreApplication.translate("MainWindow", u"convert to mov", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

