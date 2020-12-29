import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import N2_3

N1UI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/N1.ui")[0]
class N1Dialog(QDialog,N1UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def n2_1_click_open(self):
        pass
    def n2_2_click_open(self):
        pass

    def n2_3_click_open(self):
        self.N2_3open = N2_3.N2_3Dialog(self)
        self.N2_3open.show()
        self.close()



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     N1D = N1Dialog()
#     N1D.show()
#     app.exec_()