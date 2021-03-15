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
        self.label = QLabel("CONVERTS .PY INTO .EXE", self)
        self.label.setGeometry(10, -20, 250, 100)
        self.label.setFont(QFont('Arial', 12, QFont.Bold))

        self.label2 = QLabel("Link 1", self)
        self.label2.setText(f"<a href= 'file:///{os.getcwd()}/dist'>Wo ist meine Exe ?</a>")  # Link in HTML Format
        self.label2.setOpenExternalLinks(True)  # Links nicht erlaubt -> clicked Funktion wird aufgerufen
        self.label2.setGeometry(125, 150, 150, 20)

        #################################
        # File Dialoge (Upload/Datei einlesen etc.)
        #################################
        self.btn1 = QPushButton("Load Py-File", self)
        self.btn1.setGeometry(15, 50, 85, 25)
        self.btn1.clicked.connect(self.function_file_dialogue)

        #################################
        # Start Conversion Button
        #################################
        self.btn2 = QPushButton("Start", self)
        #self.btn2.move(150, 80)
        self.btn2.setGeometry(110, 50, 120, 75)
        self.btn2.setEnabled(False)
        self.btn2.clicked.connect(self.function_start_conversion)

        #################################
        # Load Icon for ExE
        #################################
        self.btn3 = QPushButton("Load EXE-Icon", self)
        self.btn3.setGeometry(15, 80, 85, 25)
        self.btn3.setEnabled(False)
        self.btn3.clicked.connect(self.function_icon_dialogue)

        #################################
        # Checkbox einfügen
        #################################
        self.cb1 = QCheckBox("Use Icon", self)
        self.cb1.move(20, 110)
        self.cb1.stateChanged.connect(self.activate_load_Button)

        self.cb2 = QCheckBox("Disable CMD-Window", self)
        self.cb2.move(20, 130)
        self.cb2.stateChanged.connect(self.activate_load_Button)

        #################################
        # Connections der Signale hinter den Funktionen, da sonst die Funtkion schon beim Setup getriggert wird
        #################################
        self.flag_load_file = 0

        #################################
        # Allgmeine Fenster Config (Hauptfenster)
        #################################
        self.setGeometry(50, 50, 250, 170)
        self.setWindowTitle("Py2exe")
        self.setWindowIcon(QIcon("Py2exe.ico"))
        self.show()

    def activate_load_Button(self): # Aktiviert den Load Icon Button wenn Checkbox aktiviert

        cb1_check = self.cb1.checkState()  # for un-checked state
                                           #2 for checked state
        if cb1_check == 2:
            self.btn3.setEnabled(True) # Button aktivieren

        elif cb1_check == 0:
            self.btn3.setEnabled(False)


    def function_file_dialogue(self):
        fd = QFileDialog() # Abfrage mit Button -> wenn ok -> rückgabe in "font" ist aktuelle Schriftart
        start_path = os.getcwd() # Aktuellen Pfad verwenden
        self.fileName = fd.getOpenFileName(self, 'Datei öffnen', start_path, 'Python-Formate (*.py)') # getOpenFileName(self, <Anzeige>, <Startpfad>, <Dateiauswahl>
        self.flag_load_file = 1 # Setzt Flag, dass File ausgewählt wurde

        if self.flag_load_file == 1:
            self.btn2.setEnabled(True)

    def function_icon_dialogue(self):
        fd = QFileDialog() # Abfrage mit Button -> wenn ok -> rückgabe in "font" ist aktuelle Schriftart
        start_path = os.getcwd() # Aktuellen Pfad verwenden
        self.iconName = fd.getOpenFileName(self, 'Datei öffnen', start_path, 'Icon (*.ico)') # getOpenFileName(self, <Anzeige>, <Startpfad>, <Dateiauswahl>
        self.flag_icon_file = 1
        #print(self.iconName[0])

    def function_start_conversion(self):

        if self.flag_load_file: # Wenn Datei ausgewählt wurde wird funktion freigeschaltet

            if self.fileName[0]:

                print("Start Conversion")
                print(self.fileName)

                # Gesamtpfad splitten in Pfad und Dateinamen
                dir_path, filename = os.path.split(self.fileName[0])
                print(f"Directory of source file: {dir_path}, Filename: {filename}")

                # Optionale Agrgumente
                # Prüft ob Checkbox 2 aktiv ->
                cb2_check = self.cb2.checkState()
                if cb2_check == 2:
                    self.flag_cb2_active = 1

                # Optinen mithilfe von Bitmasks übergeben
                opt_arg = 0
                opt_arg = self.flag_icon_file | opt_arg  # Wenn Icon geladen -> 0000 0001
                opt_arg = self.flag_cb2_active << 1 | opt_arg   # -> 0000 0010

                if opt_arg == 0: # Wenn kein Argument aktiv
                    arg = ""
                    arg_2 = ""

                if opt_arg & 0b000001: # Wenn Icon geladen wurde
                    ico_path, ico_name = os.path.split(self.iconName[0])
                    arg = f" --icon {ico_name}" # Icon Pfad wird an arg übergeben

                if opt_arg & 0b0000010: # Wenn CMD Window deaktiviert werden soll für die EXE
                    arg_2 = f" -w"

                # Ausführung der Command Lines zur erzeugung der EXE File
                command_1 = fr'start cmd /k cd {dir_path}'
                command_2 = fr'pyinstaller --onefile{arg}{arg_2} {filename}'
                print(command_2)
                os.system(command_1)
                os.system(command_2)

        else:
            print("Keine Python Datei ausgewählt")

app = QApplication(sys.argv) # Neue Default-Application anlegen
w = Fenster() # Einfaches Fenster bauen -> Neue Instanz w
sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird