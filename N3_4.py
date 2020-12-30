import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import inlove
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='projekt2', charset='utf8')
N3_4UI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/N3_4.ui")[0]

class N3_4Dialog(QDialog, N3_4UI):
    def __init__(self,value, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        #self.label_12.setText("안녕하세요.")

        #sql data 가져오기
        cur = conn.cursor()
        #label_a 수정
        cur.execute("SELECT name FROM family where id = 'n23' ")
        text_edit_a = cur.fetchone()[0]
        self.label_a.setText(text_edit_a)

        # label_b 수정
        cur.execute("SELECT position FROM family where id = 'n23' ")
        text_edit_b = cur.fetchone()[0]
        self.label_b.setText(text_edit_b)

        # label_c 수정
        cur.execute("SELECT birthday FROM family where id = 'n23' ")
        text_edit_c = cur.fetchone()[0]
        self.label_c.setText(text_edit_c)

        # label_d 수정
        cur.execute("SELECT special FROM family where id = 'n23' ")
        text_edit_d = cur.fetchone()[0]
        self.label_d.setText(text_edit_d)

        # label_e 수정
        cur.execute("SELECT tel FROM family where id = 'n23' ")
        text_edit_e = cur.fetchone()[0]
        self.label_e.setText(text_edit_e)


    def nachHause_click_open(self):
        self.inLoveopen = inlove.InLove()
        self.inLoveopen.show()
        self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    N3_4D = N3_4()
    N3_4D.show()
    app.exec_()