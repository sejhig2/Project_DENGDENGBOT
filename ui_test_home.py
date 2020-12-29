# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_homewvMyXV.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(2, -1, 1278, 718))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn119 = QPushButton(self.layoutWidget)
        self.btn119.setObjectName(u"btn119")
        self.btn119.setMinimumSize(QSize(635, 355))

        self.gridLayout.addWidget(self.btn119, 0, 0, 1, 1)

        self.btn_flove = QPushButton(self.layoutWidget)
        self.btn_flove.setObjectName(u"btn_flove")
        self.btn_flove.setMinimumSize(QSize(635, 355))

        self.gridLayout.addWidget(self.btn_flove, 0, 1, 1, 1)

        self.btn_fun = QPushButton(self.layoutWidget)
        self.btn_fun.setObjectName(u"btn_fun")
        self.btn_fun.setMinimumSize(QSize(635, 355))

        self.gridLayout.addWidget(self.btn_fun, 1, 0, 1, 1)

        self.btn_200years = QPushButton(self.layoutWidget)
        self.btn_200years.setObjectName(u"btn_200years")
        self.btn_200years.setMinimumSize(QSize(635, 355))

        self.gridLayout.addWidget(self.btn_200years, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn119.setText(QCoreApplication.translate("MainWindow", u"btn119", None))
        self.btn_flove.setText(QCoreApplication.translate("MainWindow", u"btn_flove", None))
        self.btn_fun.setText(QCoreApplication.translate("MainWindow", u"btn_fun", None))
        self.btn_200years.setText(QCoreApplication.translate("MainWindow", u"btn_200years", None))
    # retranslateUi

