import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import S2

SK1UI = uic.loadUiType("C:/DengDengE/SK1.ui")[0]
class SK1Dialog(QDialog,SK1UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def S2_click_open(self):
        self.s2open = S2.S2Dialog(self)
        self.s2open.show()
        self.close()

