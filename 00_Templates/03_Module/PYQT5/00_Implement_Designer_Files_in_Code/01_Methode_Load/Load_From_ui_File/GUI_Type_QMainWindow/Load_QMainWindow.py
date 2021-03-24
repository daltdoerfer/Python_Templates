# https://www.youtube.com/watch?v=LaoU_o50u9k
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QWidget
from PyQt5 import uic
import sys
import os

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #######################################################
        #                   Load your UI
        ########################################################
        filename = "QMainWindow_Button.ui"
        uic.loadUi(filename, self)


        #######################################################
        #           Connect Buttons, Text, Widgets etc.
        ########################################################
        # self.textedit = self.findChild(QTextEdit, ) # Textedit in ui-File finden
        self.button = self.findChild(QPushButton, "pushButton") # Button in ui-File finden (Mit NAaen)
        self.button.clicked.connect(self.clickedBtn)

        self.show()


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
    UIWindow = UI()
    app.exec_()



