import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import uic
import N2_3
import N1_1nameMODIFY
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='projekt2', charset='utf8')
N1UI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/N1.ui")[0]
class N1Dialog(QDialog,N1UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # SQL 커서 생성
        cur = conn.cursor()
        # 조회하기
        cur.execute("SELECT name FROM family where id = 'n11' ")
        text_edit1 = cur.fetchone()[0]
        self.label_1.setText(text_edit1)

        cur.execute("SELECT name FROM family where id = 'n12' ")
        text_edit2 = cur.fetchone()[0]
        self.label_2.setText(text_edit2)

        cur.execute("SELECT name FROM family where id = 'n13' ")
        text_edit3 = cur.fetchone()[0]
        self.label_3.setText(text_edit3)



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