import sys
import Auth_SQL
from PyQt5.QtWidgets import *
from PyQt5 import uic
import N2_3
import N1_1nameMODIFY,N1_2nameMODIFY, N1_3nameMODIFY

N1UI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/N1.ui")[0]
class N1Dialog(QDialog,N1UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)



        # 조회하기
        Auth_SQL.cur.execute("SELECT name FROM family where id = 'n1_1' ")
        text_edit1 = Auth_SQL.cur.fetchone()[0]
        self.label_1.setText(text_edit1)

        Auth_SQL.cur.execute("SELECT name FROM family where id = 'n1_2' ")
        text_edit2 = Auth_SQL.cur.fetchone()[0]
        self.label_2.setText(text_edit2)

        Auth_SQL.cur.execute("SELECT name FROM family where id = 'n1_3' ")
        text_edit3 = Auth_SQL.cur.fetchone()[0]
        self.label_3.setText(text_edit3)



    def n2_1_click_open(self):
        pass
    def n2_2_click_open(self):
        pass

    def n2_3_click_open(self):
        self.N2_3open = N2_3.N2_3Dialog(self)
        self.N2_3open.show()
    #Auth_SQL.conn.close() # SQL 닫으면 안 된다. 3시간 뺑이쳤다.
        self.close()

    def N1_1nameMODIFY_click_open(self):
        self.n1_1nameMODIFYopen = N1_1nameMODIFY.N1_1nameMODIFY_Dialog(self)
        self.n1_1nameMODIFYopen.show()
        self.close()

    def N1_2nameMODIFY_click_open(self):
        self.n1_2nameMODIFYopen = N1_2nameMODIFY.N1_2nameMODIFY_Dialog(self)
        self.n1_2nameMODIFYopen.show()
        self.close()

    def N1_3nameMODIFY_click_open(self):
        self.n1_3nameMODIFYopen = N1_3nameMODIFY.N1_3nameMODIFY_Dialog(self)
        self.n1_3nameMODIFYopen.show()
        self.close()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     N1D = N1Dialog()
#     N1D.show()
#     app.exec_()