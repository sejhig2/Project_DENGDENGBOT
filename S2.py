import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import S3_2

S2UI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/S2.ui")[0]
class S2Dialog(QDialog,S2UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def S3_2_click_open(self):
        self.s3_2open = S3_2.S3_2Dialog(self)
        self.s3_2open.show()
        self.close()