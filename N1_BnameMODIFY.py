import sys
import Auth_SQL
from PyQt5.QtWidgets import *
from PyQt5 import uic
import N1


N1_BnameMODIFYUI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/nameMODIFY_N1_B.ui")[0]
class N1_BnameMODIFY_Dialog(QDialog,N1_BnameMODIFYUI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def nameReturnN1_B(self):
        name_insert_SQL = self.lineEdit_1.text()
        print(name_insert_SQL)
        sql = "UPDATE family SET name = '{0}' where id = 'n1_B' ;".format(name_insert_SQL)
        print(sql)
        Auth_SQL.cur.execute(sql)
        Auth_SQL.conn.commit()
        #Auth_SQL.conn.close() # 이걸 왜 닫으면 안 되는 걸까? 질문하기

        #클릭시 N1화면으로 돌아가기
        self.n1open = N1.N1Dialog(self)
        self.n1open.show()
        self.close()



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     N1D = N1_nameMODIFY_Dialog()
#     N1D.show()
#     app.exec_()