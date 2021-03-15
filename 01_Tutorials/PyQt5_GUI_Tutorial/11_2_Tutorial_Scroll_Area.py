# Dieses Tutorial beinhaltet das einfügen von:
# Font Dialoge
# File Dialoge
# https://www.youtube.com/watch?v=DaIfM0jkbIk

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
        # Scroll Area erstellen
        #################################
        #  innerhalb des Hauptfensters (Lvl2)
        box = QVBoxLayout(self) # BoxLayout für MainFenster
        self.setLayout(box)

        #  innerhalb des Hauptfensters (lvl3)
        scroll = QScrollArea(self) # Innerhalb des BoxLayouts haben wir eine Scrollarea erstellt, in welcher gescrollt werden kann
        box.addWidget(scroll) # Scrollobjekt wird dem Boxobjekt zugewiesen
        scroll.setWidgetResizable(True) # Veränderbare Größe (geht auch ohne diese Zeile)

        # Subwidget erstellen (lvl4)
        scrollContent = QWidget(scroll) # Neuer Inhalt -> Soll sich im Scrollfenster befinden, daher auf SCroll bezogen
        scrollLayout = QVBoxLayout(scrollContent) # Dieser neue Inhalt brauche jedoch immernoch ein Layout
        scrollContent.setLayout(scrollLayout)  # Wir brauchen ein Layout für die Scrollarea

        # Liste befüllen mit Buttons  (in ScrollLayout)
        for i in range(0, 100):
            scrollLayout.addWidget(QPushButton(f"Nr. {i}"))

        scroll.setWidget(scrollContent) # Das was wir scrollen wollen muss hier gesettet werden

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