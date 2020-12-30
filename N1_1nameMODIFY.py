import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import uic
import N1

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='projekt2', charset='utf8')

N1_nameMODIFYUI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/nameMODIFY_N1_1.ui")[0]
class N1_nameMODIFY_Dialog(QDialog,N1_nameMODIFYUI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        #SQL 수정



    def nameReturnN1_1(self):
        # self.lineEdit_1.getText()
        # cur = conn.cursor()
        # sql = "UPDATE family SET name = '큰 딸b ' where id = 'n11' ;"
        # title_modi = cur.execute(sql)
        # title_modi
        # # print(title_modi)
        # conn.commit()
        # conn.close()

        self.n1open = N1.N1Dialog(self.lineEdit_1.text())
        self.n1open.show()
        self.close()



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     N1D = N1_nameMODIFY_Dialog()
#     N1D.show()
#     app.exec_()