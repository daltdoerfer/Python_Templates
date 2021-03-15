# Dieses Tutorial beinhaltet das einfügen von:
# Input Dialoge
# Font Dialoge
# File Dialoge siehe https://pythonspot.com/pyqt5-file-dialog/
# Color Diagloge
# https://www.youtube.com/watch?v=VvHePllETng

import sys
import time

from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Fenster(QWidget): # Wichtig für Status und Menübar von QMainWindow erben
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):

        #Label für späteres Bild
        self.label = QLabel("CONVERTS PYTHON TO .EXE", self)
        self.label.setGeometry(10, -20, 250, 100)
        self.label.setFont(QFont('Arial', 12, QFont.Bold))

        #################################
        # File Dialoge (Upload/Datei einlesen etc.)
        #################################
        self.btn1 = QPushButton("Load File", self)
        self.btn1.move(50, 80)
        self.btn1.clicked.connect(self.function_file_dialogue)

        #################################
        # Start Conversion Button
        #################################
        self.btn2 = QPushButton("Start", self)
        self.btn2.move(150, 80)
        self.btn2.clicked.connect(self.function_start_conversion)

        #################################
        # Connections der Signale hinter den Funktionen, da sonst die Funtkion schon beim Setup getriggert wird
        #################################

        #################################
        # Allgmeine Fenster Config (Hauptfenster)
        #################################
        self.setGeometry(50, 50, 300, 150)
        self.setWindowTitle("Py2exe")
        self.setWindowIcon(QIcon("Py2exe.png"))
        self.show()


    def function_file_dialogue(self):
        fd = QFileDialog() # Abfrage mit Button -> wenn ok -> rückgabe in "font" ist aktuelle Schriftart
        start_path = r"C:\Users"
        self.fileName = fd.getOpenFileName(self, 'Datei öffnen', start_path, 'Python-Formate (*.py)') # getOpenFileName(self, <Anzeige>, <Startpfad>, <Dateiauswahl>
        #print(fileName) # FileName -> Tupel
        #if self.fileName:
            #print(self.fileName)

    def function_start_conversion(self):
        if self.fileName:
            print(self.fileName)


app = QApplication(sys.argv) # Neue Default-Application anlegen
w = Fenster() # Einfaches Fenster bauen -> Neue Instanz w
sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird