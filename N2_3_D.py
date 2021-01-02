import sys
#import Auth_SQL
from PyQt5.QtWidgets import *
from PyQt5 import uic
import inlove



N2_3_DUI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/N2_3_D.ui")[0]
class N2_3_DDialog(QDialog, N2_3_DUI):
    def __init__(self,value, parent=None):
        super().__init__(parent)
        self.setupUi(self)


        # #label_a 수정
        # Auth_SQL.cur.execute("SELECT name FROM family where id = 'n2_3_D' ")
        # text_edit_a = Auth_SQL.cur.fetchone()[0]
        # self.label_a.setText(text_edit_a)
        #
        # # label_b 수정
        # Auth_SQL.cur.execute("SELECT position FROM family where id = 'n2_3_D' ")
        # text_edit_b = Auth_SQL.cur.fetchone()[0]
        # self.label_b.setText(text_edit_b)
        #
        # # label_c 수정
        # Auth_SQL.cur.execute("SELECT birthday FROM family where id = 'n2_3_D'; ")
        # text_edit_c = Auth_SQL.cur.fetchone()[0]
        # self.label_c.setText(text_edit_c)
        #
        # # label_d 수정
        # Auth_SQL.cur.execute("SELECT special FROM family where id = 'n2_3_D'; ")
        # text_edit_d = Auth_SQL.cur.fetchone()[0]
        # self.label_d.setText(text_edit_d)
        #
        # # label_e 수정
        # Auth_SQL.cur.execute("SELECT tel FROM family where id = 'n2_3_D'; ")
        # text_edit_e = Auth_SQL.cur.fetchone()[0]
        # self.label_e.setText(text_edit_e)


    def nachHause_click_open(self):
        self.inLoveopen = inlove.InLove()
        self.inLoveopen.show()
        self.close()




# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     N3_4D = N3_4Dialog()
#     N3_4D.show()
#     app.exec_()