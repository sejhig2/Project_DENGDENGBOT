import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import inlove

M1UI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/M1.ui")[0]
class M1Dialog(QDialog,M1UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def nachHause_click_open(self):
        self.inLoveopen = inlove.InLove()
        self.inLoveopen.show()
        self.close()