# https://www.youtube.com/watch?v=LaoU_o50u9k
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QLineEdit, QWidget
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import os

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #######################################################
        #                   Load your UI
        ########################################################
        filename = "QMainWindow_Convert.ui"
        uic.loadUi(filename, self)


        #######################################################
        #           Connect Buttons, Text, Widgets etc.
        ########################################################
        self.textedit = self.findChild(QLineEdit, "lineEdit") # Textedit in ui-File finden
        # self.textedit.textChanged.connect(self.funktion_line_edit)  # JEdes mal wenn der User etwas ändert wird getriggert

        self.button = self.findChild(QPushButton, "loadBtn") # Button in ui-File finden (Mit NAaen)
        self.button.clicked.connect(self.function_file_dialogue)

        self.button_2 = self.findChild(QPushButton, "exeBtn") # Button in ui-File finden (Mit NAaen)
        self.button_2.setEnabled(False)
        self.button_2.clicked.connect(self.function_start_conversion)

        #######################################################
        #           Initialsisierung
        ########################################################
        self.flag_load_file = 0

        self.show()

    #######################################################
    #                   Declare Function
    ########################################################
    def function_file_dialogue(self):
        print("Test")
        fd = QFileDialog() # Abfrage mit Button -> wenn ok -> rückgabe in "font" ist aktuelle Schriftart
        start_path = os.getcwd() # Aktuellen Pfad verwenden
        self.fileName = fd.getOpenFileName(self, 'Datei öffnen', start_path, 'Designer-Formate (*.ui)') # getOpenFileName(self, <Anzeige>, <Startpfad>, <Dateiauswahl>
        self.textedit.setText(f"{self.fileName[0]}")

        self.flag_load_file = 1
        if self.flag_load_file == 1:
            self.button_2.setEnabled(True)

    def function_start_conversion(self):

        if self.flag_load_file:  # Wenn Datei ausgewählt wurde wird funktion freigeschaltet

            if self.fileName[0]:

                print("Start Conversion")
                print(self.fileName)

                # Gesamtpfad splitten in Pfad und Dateinamen
                dir_path, filename = os.path.split(self.fileName[0])
                print(f"Directory of source file: {dir_path}, Filename: {filename}")


                # Ausführung der Command Lines zur erzeugung der EXE File
                # pyuic5 -x filename.ui > filename.py
                command_1 = fr'start cmd /k cd {dir_path}'
                command_2 = fr'pyuic5 -x {filename} > {filename[:-3]}.py'
                #self.le1.setText(f">> {command_2} ")
                print(command_2)
                os.system(command_1)
                os.system(command_2)

        else:
            print("Keine Designer-Datei ausgewählt")


#######################################################
#                   Main Function
########################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()



