# https://www.youtube.com/watch?v=LaoU_o50u9k
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QWidget
from PyQt5 import uic
import sys
import os

class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()

        #######################################################
        # Load your UI
        ########################################################
        filename = "QWidget_Button.ui"
        uic.loadUi(filename, self)

        #######################################################
        #           Connect Buttons, Text, Widgets etc.
        ########################################################
        # self.textedit = self.findChild(QTextEdit, ) # Textedit in ui finden
        self.button = self.findChild(QPushButton, "pushButton") # Button in ui finden (Mit NAmen)
        #self.button.clicked.connect(self.clickedBtn)

        self.show()

#######################################################
#                   Main Function
########################################################
if __name__ == "__main__":

    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()



