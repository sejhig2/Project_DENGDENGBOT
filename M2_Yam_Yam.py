import sys
#import Auth_SQL
from PyQt5.QtWidgets import *
from PyQt5 import uic
import inlove
import Auth_SQL
import webbrowser



M2_Yam_YamUI = uic.loadUiType("C:/DengDengE/M2_Yam_Yam.ui")[0]
class M2_Yam_YamDialog(QDialog, M2_Yam_YamUI):
    def __init__(self, parent=None): #value 는 어떤 역할을 하는거지?
        super().__init__(parent)
        self.setupUi(self)


    def nachHause_click_open(self):
        self.inLoveopen = inlove.InLove()
        self.inLoveopen.show()
        self.close()

    #농사 정보 버튼 페이지 1
    def link1_1(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link1_1'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link1_2(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link1_2'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    # 농사 정보 버튼 페이지 2
    def link2_1(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_1'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_2(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_2'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_3(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_3'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_4(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_4'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_5(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_5'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_6(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_6'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_7(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_7'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_8(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_8'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_9(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_9'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_10(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_10'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_11(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_11'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_12(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_12'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_13(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_13'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_14(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_14'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_15(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_15'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_16(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_16'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_17(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_17'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_18(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_18'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_19(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_19'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

    def link2_20(self):
        Auth_SQL.cur.execute("SELECT url FROM nongsaro where ob_name = 'link2_20'; ")
        url = Auth_SQL.cur.fetchone()[0]
        webbrowser.open(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    homeD = M2_Yam_YamDialog()
    homeD.show()
    app.exec_()

