# Dieses Tutorial beinhaltet Box Layout

import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class Fenster(QWidget): # Wichtig für Status und Menübar von QMainWindow erben
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):

        grid = QGridLayout()
        namen = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        positions = [(i, j) for i in range(3) for j in range(3)]  # Liste aus Tupeln mit Positionen im Grid
        print(positions)


        for pos, name in zip(positions, namen):  # Wird zu Doppeltupel ((Pos_X,Pos_Y),"Name")
            button = QPushButton(name)
            print(pos)
            print(*pos)
            grid.addWidget(button, *pos)  # Argument unpacking *pos ->

        self.setLayout(grid) # Verknüpft GridLayOut mit Fenster
        self.setGeometry(50, 50, 1000, 500)
        self.setWindowTitle("My First GUI")
        self.show()

app = QApplication(sys.argv) # Neue Default-Application anlegen
w = Fenster() # Einfaches Fenster bauen -> Neue Instanz w
sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird