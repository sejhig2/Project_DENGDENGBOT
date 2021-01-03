import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import inlove
import os

G2UI = uic.loadUiType("C:/DengDengE/G2.ui")[0]
class G2Dialog(QDialog,G2UI):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def nachHause_click_open(self):
        self.inLoveopen = inlove.InLove()
        self.inLoveopen.show()
        self.close()

    def run_PIKA(self):
        playPIKA = os.system("H:/game/pika.exe")

    def run_GOSTOP(self):
        os.system("H:/game/월드컵gostop.exe")


    def run_SUPER(self):
        os.system("H:/game/슈퍼마리오/실행기.exe")

    def run_BUBBLE(self):
        os.system("H:/game/bubblebobble.exe")