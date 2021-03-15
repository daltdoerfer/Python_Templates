# Dieses Tutorial beinhaltet das einfügen von:
# Font Dialoge
# File Dialoge
# https://www.youtube.com/watch?v=ykUhAp8yTFE

import sys
import time

from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Fenster(QTabWidget): # Wichtig für Status und Menübar von QMainWindow erben
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):

        #################################
        # Mehrere Tabs erstellen
        #################################
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.addTab(self.tab1, "Tab Nr.1")
        self.addTab(self.tab2, "Tab Nr.2")
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

    def function_1(self):
        text, ok = QInputDialog.getText(self, "Wie ist dein Name", "Gibt deinen Namen ein: ")  # Abfrage mit Button -> wenn ok -> rückgabe in "font" ist aktuelle Schriftart

        if ok:  # Wenn der user auf OK klickt dann wird die schriftart des Buttons verändert
            print(text)


app = QApplication(sys.argv) # Neue Default-Application anlegen
w = Fenster() # Einfaches Fenster bauen -> Neue Instanz w
sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird