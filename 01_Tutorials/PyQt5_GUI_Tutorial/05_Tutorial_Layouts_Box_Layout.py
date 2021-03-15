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

        # Mehrere Buttons erstellen
        upvote = QPushButton("Upvote me", self)
        abo = QPushButton("Sub me", self)

        #################################################################################
        # Buttons manuell über .move() verschieben ist Blöd daher -> Box Layout
        #################################################################################
        # Horizontales Layout/Anordnung
        h = QHBoxLayout()
        h.addWidget(upvote) # Erzeugt Button (an 1. Stelle von Links)
        h.addStretch(1) # Erzeugt Leere horizontale Box damit die Buttons nach rechts geschoben werden (an 2. Stelle von Links)
        h.addWidget(abo) # Erzeugt Button (an 3. Stelle von Links)

        # Vertikales Layout/Anordung
        v = QVBoxLayout()
        v.addStretch(1) # Erzeugt Leere vertikale Box damit die Buttons nach unten geschoben werden (an 1. Stelle von Oben)
        v.addLayout(h) # Horiozontale Layout verknüpfen mit vertikalem LAyout (an 2. Stelle von Oben)

        self.setLayout(v) # Verknüpft BoxLayOut mit Fenster -> Wichtig h wurde mit v Verknüpft und v wird mit Fenster verknüpft
        self.setGeometry(50,50,1000,500)
        self.setWindowTitle("My First GUI")
        self.show()

app = QApplication(sys.argv) # Neue Default-Application anlegen
w = Fenster() # Einfaches Fenster bauen -> Neue Instanz w
sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird