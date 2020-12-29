import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import N1
import SK1


homeUI = uic.loadUiType("H:\das Projekt auf V3.6\GUI\Inlove.ui")[0]
class InLove(QDialog, homeUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #@pyqtSlot
    def N1_click_open(self):
        self.n1open = N1.N1Dialog(self)
        self.n1open.show()
        self.close()

    def SK1_click_open(self):
        self.sk1open = SK1.SK1Dialog(self)
        self.sk1open.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    homeD = InLove()
    homeD.show()
    app.exec_()