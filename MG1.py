import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import G2
import M1

MG1UI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/MG1.ui")[0]
class MG1Dialog(QDialog,MG1UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def run_fun(self):
        self.g2open = G2.G2Dialog(self)
        self.g2open.show()
        self.close()

    def M2_click_open(self):
        self.m1open = M1.M1Dialog(self)
        self.m1open.show()
        self.close()

