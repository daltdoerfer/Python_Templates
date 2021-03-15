# Dieses Tutorial beinhaltet das einfügen von:
# Input Dialoge
# Font Dialoge
# File Dialoge siehe https://pythonspot.com/pyqt5-file-dialog/
# Color Diagloge
# https://www.youtube.com/watch?v=VvHePllETng

import sys
import time
import os
import tkinter as tk

from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Fenster(QWidget): # Wichtig für Status und Menübar von QMainWindow erben
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):

        #################################
        # Labels
        #################################
        #Label -> Überschrift
        self.label = QLabel("CONVERTS PYTHON TO .EXE", self)
        self.label.setGeometry(10, -20, 250, 100)
        self.label.setFont(QFont('Arial', 12, QFont.Bold))


        #################################
        # File Dialoge (Upload/Datei einlesen etc.)
        #################################
        self.btn1 = QPushButton("Load File", self)
        self.btn1.move(20, 50)
        self.btn1.clicked.connect(self.function_file_dialogue)

        #################################
        # Start Conversion Button
        #################################
        self.btn2 = QPushButton("Start", self)
        self.btn2.move(150, 80)
        self.btn2.clicked.connect(self.function_start_conversion)

        #################################
        # Load Icon for ExE
        #################################
        self.btn3 = QPushButton("Load Icon", self)
        self.btn3.move(20, 100)
        self.btn3.setEnabled(False)
        self.btn3.clicked.connect(self.function_icon_dialogue)

        #################################
        # Connections der Signale hinter den Funktionen, da sonst die Funtkion schon beim Setup getriggert wird
        #################################
        self.flag_load_file = 0
        #################################
        # Allgmeine Fenster Config (Hauptfenster)
        #################################
        self.setGeometry(50, 50, 300, 150)
        self.setWindowTitle("Py2exe")
        self.setWindowIcon(QIcon("Py2exe.ico"))
        self.show()


    def function_file_dialogue(self):
        fd = QFileDialog() # Abfrage mit Button -> wenn ok -> rückgabe in "font" ist aktuelle Schriftart
        start_path = os.getcwd() # Aktuellen Pfad verwenden
        self.fileName = fd.getOpenFileName(self, 'Datei öffnen', start_path, 'Python-Formate (*.py)') # getOpenFileName(self, <Anzeige>, <Startpfad>, <Dateiauswahl>
        self.flag_load_file = 1 # Setzt Flag, dass File ausgewählt wurde

    def function_icon_dialogue(self):
        fd = QFileDialog() # Abfrage mit Button -> wenn ok -> rückgabe in "font" ist aktuelle Schriftart
        start_path = os.getcwd() # Aktuellen Pfad verwenden
        self.iconName = fd.getOpenFileName(self, 'Datei öffnen', start_path, 'Icon (*.ico)') # getOpenFileName(self, <Anzeige>, <Startpfad>, <Dateiauswahl>


    def function_start_conversion(self):

        if self.flag_load_file: # Wenn Datei ausgewählt wurde

            if self.fileName[0]:

                print("Start Conversion")
                print(self.fileName)

                # Einzeln Ausgeben
                dir_path, filename = os.path.split(self.fileName[0])  # Angabe zur Datei splitten in Pfad und Dateinamen
                print(f"Directory of source file: {dir_path}, Filename: {filename}")

                opt_arg = 1
                # Optionale Agrgumente
                if opt_arg == 1:
                    arg = f"--icon {self.iconName[0]}"
                else:
                    arg = ""

                # Ausführung der Command Lines zur erzeugung der EXE File
                command_1 = fr'start cmd /k cd {dir_path}'
                command_2 = fr'pyinstaller --onefile {arg} -w {filename}'
                print(command_2)
                os.system(command_1)
                os.system(command_2)

        else:
            print("Keine Python Datei ausgewählt")

app = QApplication(sys.argv) # Neue Default-Application anlegen
w = Fenster() # Einfaches Fenster bauen -> Neue Instanz w
sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird