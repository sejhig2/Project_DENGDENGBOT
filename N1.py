import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import N2_3
import N1_1nameMODIFY

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

    def N1_1nameMODIFY_click_open(self):
        self.n1_nameMODIFYopen = N1_1nameMODIFY.N1_nameMODIFY_Dialog(self)
        self.n1_nameMODIFYopen.show()
        self.close()

    def N1_2nameMODIFY_click_open(self):
        pass

    def N1_3nameMODIFY_click_open(self):
        pass

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     N1D = N1Dialog()
#     N1D.show()
#     app.exec_()