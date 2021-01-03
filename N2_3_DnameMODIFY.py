import sys
import Auth_SQL
from PyQt5.QtWidgets import *
from PyQt5 import uic
import N2_3


N2_3_DnameMODIFYUI = uic.loadUiType("C:/DengDengE/nameMODIFY_N2_3_D.ui")[0]
class N2_3_DnameMODIFY_Dialog(QDialog,N2_3_DnameMODIFYUI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    #N2_3페이지의 네번째이름 바꾸기
    def nameReturnN2_3_D(self):
        name_insert_SQL = self.lineEdit_1.text()
        sql = "UPDATE family SET name = '{0}' where id = 'n2_3_D' ;".format(name_insert_SQL)
        print(sql)
        Auth_SQL.cur.execute(sql)
        Auth_SQL.conn.commit()

        self.n2_3open = N2_3.N2_3Dialog(self)
        self.n2_3open.show()
        self.close()



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     N1D = N1_1nameMODIFY_Dialog()
#     N1D.show()
#     app.exec_()