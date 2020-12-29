import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import N1
homeUI = uic.loadUiType("H:\das Projekt auf V3.6\GUI\Inlove.ui")[0]

class InLove(QDialog, homeUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #@pyqtSlot
    def N1_click_open(self):
        self.N1open = N1(self)
        self.N1open.show()
        self.close()

N1UI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/N1.ui")[0]

class N1(QDialog,N1UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def n2_1(self):
        pass
    def n2_2(self):
        pass
    def n2_3(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    homeD = InLove()
    homeD.show()
    app.exec_()