import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import N1

N1_nameMODIFYUI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/nameMODIFY_N1_1.ui")[0]
class N1_nameMODIFY_Dialog(QDialog,N1_nameMODIFYUI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def nameReturnN1_1(self):
        self.n1open = N1.N1Dialog(self.lineEdit_1.text())
        self.n1open.show()
        self.close()



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     N1D = N1_nameMODIFY_Dialog()
#     N1D.show()
#     app.exec_()