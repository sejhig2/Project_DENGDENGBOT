import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import inlove


N3_4UI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/N3_4.ui")[0]

class N3_4Dialog(QDialog, N3_4UI):
    def __init__(self,value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def nachHause_click_open(self):
        self.inLoveopen = inlove.InLove()
        self.inLoveopen.show()
        self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    N3_4D = N3_4()
    N3_4D.show()
    app.exec_()