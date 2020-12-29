import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import G2

MG1UI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/MG1.ui")[0]
class MG1Dialog(QDialog,MG1UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def run_fun(self):
        self.g2open = G2.G2Dialog(self)
        self.g2open.show()
        self.close()
