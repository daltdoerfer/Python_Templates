# Dieses Tutorial beinhaltet das einfügen von:
# Beinhaltet Drag n Drop möglichkeiten
# Dazu wird ein Klasse Button erstellt welche die Dropevents enthält, diese erbt von QPushButton und wird später in unsere Klasse Fenster implementiert
# https://www.youtube.com/watch?v=DaIfM0jkbIk

import sys
import time

from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Button(QPushButton): # Wir brauchen einen Button der von QPusbutton erbt, dieser wird später ins Fenster gebracht
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        # Welche Formate dürfen gezogen werden
        # Nur eine der folgenden Zeilen darf aktiv sein
        if event.mimeData().hasFormat("text/plain"): # Standard Text
        #if event.mimeData().hasFormat("text/html"): # Html Format
        #if event.mimeData().hasFormat("text/uri-l"): # Link-liste
        #if event.mimeData().hasFormat("image/*") # Bilder
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event): # Was soll passieren bei Drag n Drop
        self.setText(event.mimeData().text()) # Der Texte der auf den Button gesetzt wird soll auf den Button geschrieben werden

class Fenster(QWidget): # Wichtig für Status und Menübar von QMainWindow erben
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):

        #################################
        # Drag N Drop
        #################################
        edit = QLineEdit('Drop on me', self)
        edit.setDragEnabled(True) # Text soll ziehbar sein
        edit.move(100, 100)
        btn = Button("Drop it on me", self) # Dieser Button kommt aus der Extra Klasse oben

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
        pass


app = QApplication(sys.argv) # Neue Default-Application anlegen
w = Fenster() # Einfaches Fenster bauen -> Neue Instanz w
sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird