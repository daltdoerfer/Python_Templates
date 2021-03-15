# Dieses Tutorial beinhaltet das einfügen von:
# Progressbar auf Allgemeinem Timer Event
# https://www.youtube.com/watch?v=3uJpHA4l9zg

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

        #################################
        # Progressbar
        #################################
        self.pb1 = QProgressBar(self)
        self.pb1.move(50, 50)

        # Timer
        self.timer = QBasicTimer()
        self.i = 0
        self.timer.start(100, self) # Integer (100) für Ende der Zählung

        #################################
        # Calendar
        #################################
        self.ca1 = QCalendarWidget(self.calendar_function)
        self.ca1.move(200, 200)

        #################################
        # Allgmeine Fenster Config (Hauptfenster)
        #################################
        self.setGeometry(50, 50, 1000, 500)
        self.setWindowTitle("My First GUI")
        self.setWindowIcon(QIcon("icon.png"))
        self.show()

    def timerEvent(self, e): # Diese Funktion läuft jeden Iterationsschritt durch
        if self.i >= 100: # Stoppe den timer wenn gewünschte Zahl erreicht
            self.timer.stop()
        self.i = self.i + 1  # Index Hochzählen
        self.pb1.setValue(self.i) # Den Wert der PRogressbar aktualisieren

    def calendar_function(self, date):
        print(date.toString())

app = QApplication(sys.argv) # Neue Default-Application anlegen
w = Fenster() # Einfaches Fenster bauen -> Neue Instanz w
sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird