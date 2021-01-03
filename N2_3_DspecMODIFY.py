import sys
#import Auth_SQL
from PyQt5.QtWidgets import *
from PyQt5 import uic
import N2_3_D
import Auth_SQL


N2_3_DsepcMODIFYUI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/N2_3_DspecMODIFY.ui")[0]
class N2_3_DspecMODIFY_Dialog(QDialog,N2_3_DsepcMODIFYUI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    #N2_3_D 페이지로 돌아가기
    def n2_3_Dclick_open(self):

        #돌아가는 버튼 누르면 text 입력한 것 MySQL로 업로드
        name_insert_SQL = self.lineEdit_1.text()
        sql_1 = "UPDATE family SET name = '{0}' where id = 'n2_3_D' ;".format(name_insert_SQL)
        Auth_SQL.cur.execute(sql_1)
        Auth_SQL.conn.commit()

        posi_insert_SQL = self.lineEdit_2.text()
        sql_2 = "UPDATE family SET position = '{0}' where id = 'n2_3_D' ;".format(posi_insert_SQL)
        Auth_SQL.cur.execute(sql_2)
        Auth_SQL.conn.commit()

        birth_insert_SQL = self.lineEdit_3.text()
        sql_3 = "UPDATE family SET birthday = '{0}' where id = 'n2_3_D' ;".format(birth_insert_SQL)
        Auth_SQL.cur.execute(sql_3)
        Auth_SQL.conn.commit()

        speic_insert_SQL = self.lineEdit_4.text()
        sql_4 = "UPDATE family SET special = '{0}' where id = 'n2_3_D' ;".format(speic_insert_SQL)
        Auth_SQL.cur.execute(sql_4)
        Auth_SQL.conn.commit()

        tel_insert_SQL = self.lineEdit_5.text()
        sql_5 = "UPDATE family SET tel = '{0}' where id = 'n2_3_D' ;".format(tel_insert_SQL)
        Auth_SQL.cur.execute(sql_5)
        Auth_SQL.conn.commit()

        #text edit 박스에 기록한 글자 업로드하기
        memo_insert_SQL = self.textEdit_m.toPlainText()
        sql_m = "UPDATE family SET memo = '{0}' where id = 'n2_3_D' ;".format(memo_insert_SQL)
        Auth_SQL.cur.execute(sql_m)
        Auth_SQL.conn.commit()



        self.n2_3_Dopen = N2_3_D.N2_3_DDialog(self)
        self.n2_3_Dopen.show()
        self.close()



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     N1D = N1_1nameMODIFY_Dialog()
#     N1D.show()
#     app.exec_()