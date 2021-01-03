import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import inlove
import M2_Yam_Yam

M1UI = uic.loadUiType("H:/das Projekt auf V3.6/GUI/M1.ui")[0]
class M1Dialog(QDialog,M1UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def M2_Yam_Yam_click_open(self):
        self.m2_Yam_Yamopen = M2_Yam_Yam.M2_Yam_YamDialog()
        self.m2_Yam_Yamopen.show()
        self.close()


    def nachHause_click_open(self):
        self.inLoveopen = inlove.InLove()
        self.inLoveopen.show()
        self.close()