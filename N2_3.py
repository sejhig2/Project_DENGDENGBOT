import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import N3_4
import Auth_SQL

N2_3UI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/N2_3.ui")[0]
class N2_3Dialog(QDialog,N2_3UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        #라벨에 텍스트 입력 받기
        Auth_SQL.cur.execute("SELECT name FROM family where id = 'n2_1' ")
        text_edit2_1 = Auth_SQL.cur.fetchone()[0]
        self.label_1.setText(text_edit2_1)

        Auth_SQL.cur.execute("SELECT name FROM family where id = 'n2_2' ")
        text_edit2_2 = Auth_SQL.cur.fetchone()[0]
        self.label_2.setText(text_edit2_2)

        Auth_SQL.cur.execute("SELECT name FROM family where id = 'n2_3' ")
        text_edit2_3 = Auth_SQL.cur.fetchone()[0]
        self.label_3.setText(text_edit2_3)

        Auth_SQL.cur.execute("SELECT name FROM family where id = 'n2_4' ")
        text_edit2_4 = Auth_SQL.cur.fetchone()[0]
        self.label_4.setText(text_edit2_4)



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



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     N2_3D = N2_3Dialog()
#     N2_3D.show()
#     app.exec_()