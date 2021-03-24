# https://www.learnpyqt.com/blog/pyqt6-vs-pyside6/

import sys
from PyQt6 import QtWidgets

from QMainWindow_Button import Ui_MainWindow

#######################################################
#                   Load your GUI
########################################################
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()