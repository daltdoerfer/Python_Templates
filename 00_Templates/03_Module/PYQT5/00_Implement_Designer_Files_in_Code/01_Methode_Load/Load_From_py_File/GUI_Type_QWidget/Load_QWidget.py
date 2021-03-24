# https://www.youtube.com/watch?v=eD91nE8q8Nk

from PySide6.QtCore import *
from PySide6.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QWidget
from PyQt5.QtWidgets import *
import sys
import os

import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot


import QWidget_Button

#######################################################
#                   Load your GUI
########################################################
class UI(QWidget, QWidget_Button.Ui_Form):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        self.setupUi(self)

        #######################################################
        #           Connect Buttons, Text, Widgets etc.
        ########################################################
        # Es gibt 2 Möglichkeiten, die beide auf das selbe herauslaufen
        # 1) findChild
        # self.button = self.findChild(QPushButton, "pushButton")  # Button in py-File finden
        # 2) Direktverknüpfung
        # self.pushButton.clicked.connect(self.clickedBtn)

        # Beispiel 2)
        self.pushButton.clicked.connect(self.clickedBtn)


    #######################################################
    #                   Declare Function
    ########################################################
    def clickedBtn(self):
        print("Test")

#######################################################
#                   Main Function
########################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    PyWindow = UI()
    PyWindow.show()
    app.exec_()



