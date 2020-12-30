import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import N3_4
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='projekt2', charset='utf8')


N2_3UI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/N2_3.ui")[0]
class N2_3Dialog(QDialog,N2_3UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # SQL 커서 생성
        cur = conn.cursor()
        #라벨에 텍스트 입력 받기
        cur.execute("SELECT name FROM family where id = 'n21' ")
        text_edit21 = cur.fetchone()[0]
        self.label_1.setText(text_edit21)

        cur.execute("SELECT name FROM family where id = 'n22' ")
        text_edit22 = cur.fetchone()[0]
        self.label_2.setText(text_edit22)

        cur.execute("SELECT name FROM family where id = 'n23' ")
        text_edit23 = cur.fetchone()[0]
        self.label_3.setText(text_edit23)

        cur.execute("SELECT name FROM family where id = 'n24' ")
        text_edit24 = cur.fetchone()[0]
        self.label_4.setText(text_edit24)


    def n3_1_click_open(self):
        pass
    def n3_2_click_open(self):
        pass
    def n3_3_click_open(self):
        pass
    def n3_4_click_open(self):
        self.n3_4open = N3_4.N3_4Dialog(self)
        self.n3_4open.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    N2_3D = N2_3Dialog()
    N2_3D.show()
    app.exec_()