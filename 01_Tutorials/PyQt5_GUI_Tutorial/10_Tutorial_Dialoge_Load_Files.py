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

        #################################
        # Input Dialog
        #################################
        self.btn0 = QPushButton("Input Text", self)
        self.btn0.move(10, 10)
        self.btn0.clicked.connect(self.function_input_dialogue)

        #################################
        # Font Dialoge (Schrift ändern)
        #################################
        self.btn1 = QPushButton("Welche Schriftart", self)
        self.btn1.move(50, 50)
        self.btn1.clicked.connect(self.function_font_dialogue)


        #################################
        # File Dialoge (Upload/Datei einlesen etc.)
        #################################
        self.btn2 = QPushButton("Load File", self)
        self.btn2.move(50, 80)
        self.btn2.clicked.connect(self.function_file_dialogue)

        #Label für späteres Bild
        self.label = QLabel("Ich werde ein Bild", self)
        self.label.move(150, 150)
        self.label.setGeometry(150, 150, 100, 100)


        #################################
        # Color-Dialoge und Frames
        #################################
        self.btn3 = QPushButton("Change Color", self)
        self.btn3.move(50, 110)
        self.btn3.clicked.connect(self.function_change_colour)

        self.frame = QFrame(self) # Default Frame Colour ist durchsichtig
        self.frame.setGeometry(300, 50, 100, 100)
        #################################
        # Connections der Signale hinter den Funktionen, da sonst die Funtkion schon beim Setup getriggert wird
        #################################

        #################################
        # Allgmeine Fenster Config (Hauptfenster)
        #################################
        self.setGeometry(50, 50, 1000, 500)
        self.setWindowTitle("My First GUI")
        self.setWindowIcon(QIcon("icon.png"))
        self.show()

    def function_input_dialogue(self):
        text, ok = QInputDialog.getText(self, "Wie ist dein Name", "Gibt deinen Namen ein: ")  # Abfrage mit Button -> wenn ok -> rückgabe in "font" ist aktuelle Schriftart

        if ok:  # Wenn der user auf OK klickt dann wird die schriftart des Buttons verändert
            print(text)

    # Programmabsturz kann bei dieser Funktion daran liegen, dass nur <Python3.8 supported wird
    def function_font_dialogue(self):
        font, ok = QFontDialog.getFont() # Abfrage mit Button -> wenn ok -> rückgabe in "font" ist aktuelle Schriftart

        if ok: # Wenn der user auf OK klickt dann wird die schriftart des Buttons verändert
            self.bt1.setFont(font)

    def function_file_dialogue(self):
        fd = QFileDialog() # Abfrage mit Button -> wenn ok -> rückgabe in "font" ist aktuelle Schriftart
        start_path = r"C:\03_Programming\Python\02_Tutorials"
        filename = fd.getOpenFileName(self, 'Datei öffnen', start_path, 'Nur Bild-Formate (*.jpg *.png)') # getOpenFileName(self, <Anzeige>, <Startpfad>, <Dateiauswahl>
        #print(filename) # Filename -> Tupel
        self.label.setPixmap(QPixmap(filename[0])) # Bild in Fenster laden

    def function_change_colour(self):
        color = QColorDialog.getColor() # Farbe abfragen
        if color.isValid():
            self.frame.setStyleSheet("QWidget {background-color: %s}" % color.name()) # Framefarbe ändern. Achtung: CSS-Befehl -> Farbe auf Frame Setzen
            self.setStyleSheet("QWidget {background-color: %s}" % color.name())  # Gesamte Hintergrundfarbe ändern

app = QApplication(sys.argv) # Neue Default-Application anlegen
w = Fenster() # Einfaches Fenster bauen -> Neue Instanz w
sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird