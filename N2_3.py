import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import N2_3_AnameMODIFY,N2_3_BnameMODIFY,N2_3_CnameMODIFY,N2_3_DnameMODIFY
import Auth_SQL
import N2_3_D

N2_3UI = uic.loadUiType("C:/DengDengE/N2_3.ui")[0]
class N2_3Dialog(QDialog,N2_3UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # #라벨에 텍스트 입력 받기

        Auth_SQL.cur.execute("SELECT name FROM family where id = 'n2_3_A' ")
        text_edit2_3_A = Auth_SQL.cur.fetchone()[0]
        self.label_1.setText(text_edit2_3_A)

        Auth_SQL.cur.execute("SELECT name FROM family where id = 'n2_3_B' ")
        text_edit2_3_B = Auth_SQL.cur.fetchone()[0]
        self.label_2.setText(text_edit2_3_B)

        Auth_SQL.cur.execute("SELECT name FROM family where id = 'n2_3_C' ")
        text_edit2_3_C = Auth_SQL.cur.fetchone()[0]
        self.label_3.setText(text_edit2_3_C)

        Auth_SQL.cur.execute("SELECT name FROM family where id = 'n2_3_D' ")
        text_edit2_3_D = Auth_SQL.cur.fetchone()[0]
        self.label_4.setText(text_edit2_3_D)



    def n2_3_Aclick_open(self):
        pass
        # self.n2_3_Aopen = N2_3_A.N2_3_ADialog(self)
        # self.n2_3_Aopen.show()
        # self.close()
    def n2_3_Bclick_open(self):
        pass
        # self.n2_3_Bopen = N2_3_B.N2_3_BDialog(self)
        # self.n2_3_Bopen.show()
        # self.close()
    def n2_3_Cclick_open(self):
        pass
        # self.n2_3_Copen = N2_3_C.N2_3_CDialog(self)
        # self.n2_3_Copen.show()
        # self.close()
    def n2_3_Dclick_open(self):
        self.n2_3_Dopen = N2_3_D.N2_3_DDialog(self)
        self.n2_3_Dopen.show()
        self.close()

    #이름 바꾸기 1,2,3,4
    def N2_3_AnameMODIFY_click_open(self):
        self.n2_3_AnameMODIFYopen = N2_3_AnameMODIFY.N2_3_AnameMODIFY_Dialog(self)
        self.n2_3_AnameMODIFYopen.show()
        self.close()

    def N2_3_BnameMODIFY_click_open(self):
        self.n2_3_BnameMODIFYopen = N2_3_BnameMODIFY.N2_3_BnameMODIFY_Dialog(self)
        self.n2_3_BnameMODIFYopen.show()
        self.close()

    def N2_3_CnameMODIFY_click_open(self):
        self.n2_3_CnameMODIFYopen = N2_3_CnameMODIFY.N2_3_CnameMODIFY_Dialog(self)
        self.n2_3_CnameMODIFYopen.show()
        self.close()

    def N2_3_DnameMODIFY_click_open(self):
        self.n2_3_DnameMODIFYopen = N2_3_DnameMODIFY.N2_3_DnameMODIFY_Dialog(self)
        self.n2_3_DnameMODIFYopen.show()
        self.close()




# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     N2_3D = N2_3Dialog()
#     N2_3D.show()
#     app.exec_()