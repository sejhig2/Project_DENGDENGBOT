import sys
import Auth_SQL
from PyQt5.QtWidgets import *
from PyQt5 import uic
import N2_3
import N1_AnameMODIFY,N1_BnameMODIFY, N1_CnameMODIFY

N1UI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/N1.ui")[0]
class N1Dialog(QDialog,N1UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # 조회하기
        Auth_SQL.cur.execute("SELECT name FROM family where id = 'n1_A' ")
        text_edit1 = Auth_SQL.cur.fetchone()[0]
        self.label_1.setText(text_edit1)

        Auth_SQL.cur.execute("SELECT name FROM family where id = 'n1_B' ")
        text_edit2 = Auth_SQL.cur.fetchone()[0]
        self.label_2.setText(text_edit2)

        Auth_SQL.cur.execute("SELECT name FROM family where id = 'n1_C' ")
        text_edit3 = Auth_SQL.cur.fetchone()[0]
        self.label_3.setText(text_edit3)


    #페이지 넘기기
    def n2_1_click_open(self):
        pass
    def n2_2_click_open(self):
        pass

    def n2_3_click_open(self):
        self.N2_3open = N2_3.N2_3Dialog(self)
        self.N2_3open.show()
        self.close()

    # 이름바꾸기 첫번째
    def N1_AnameMODIFY_click_open(self):
        self.n1_AnameMODIFYopen = N1_AnameMODIFY.N1_AnameMODIFY_Dialog(self)
        self.n1_AnameMODIFYopen.show()
        self.close()

    # 이름바꾸기 두번째
    def N1_BnameMODIFY_click_open(self):
        self.n1_BnameMODIFYopen = N1_BnameMODIFY.N1_BnameMODIFY_Dialog(self)
        self.n1_BnameMODIFYopen.show()
        self.close()

    # 이름바꾸기 세번째
    def N1_CnameMODIFY_click_open(self):
        self.n1_CnameMODIFYopen = N1_CnameMODIFY.N1_CnameMODIFY_Dialog(self)
        self.n1_CnameMODIFYopen.show()
        self.close()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     N1D = N1Dialog()
#     N1D.show()
#     app.exec_()