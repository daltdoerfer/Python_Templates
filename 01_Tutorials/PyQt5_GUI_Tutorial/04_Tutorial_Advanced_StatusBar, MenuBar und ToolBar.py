# Dieses Tutorial
# https://www.youtube.com/watch?v=pa4XlYyIa2o

import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class Fenster(QMainWindow): # Wichtig für Status und Menübar von QMainWindow erben
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.statusBar().showMessage("Immer noch my first GUI") # Statusbar Unten links im Programm

        #Diese Funktion exitMe bezieht sich auf das Submenü in Zeile 29
        exitMe = QAction(QIcon('icon.png'), '&Exit', self) # self -> Woraus wir exiten wollen
        exitMe.setShortcut('Ctrl+E') # Shortcut für Submenü einfügen
        exitMe.triggered.connect(self.close)
        exitMe.setStatusTip('Beendet das Programm')

        # Menüleiste
        menubar = self.menuBar()
        file = menubar.addMenu('&File') # Das & fügt ein Shortcut für Menüleiste ein (ALT+F)
        file.addAction(exitMe) #  Submenü für File Menu Bar -> exitMe Funktion von oben aufrufen

        toolBar = self.addToolBar('Exit')
        toolBar.addAction(exitMe)

        self.setGeometry(50,50,1000,500)
        self.setWindowTitle("My First GUI")
        self.show()

app = QApplication(sys.argv) # Neue Default-Application anlegen
w = Fenster() # Einfaches Fenster bauen -> Neue Instanz w
sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird