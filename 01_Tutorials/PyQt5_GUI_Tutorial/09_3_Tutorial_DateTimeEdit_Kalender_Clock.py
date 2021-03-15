# Dieses Tutorial beinhaltet das einfügen von:
# Progressbar auf Allgemeinem Timer Event
# https://www.youtube.com/watch?v=3uJpHA4l9zg

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
        # Calendar
        #################################
        self.ca1 = QCalendarWidget(self)
        self.ca1.move(50, 50)
        self.ca1.clicked.connect(self.calendar_function)

        #################################
        # Clock
        #################################
        self.clo1 = QLCDNumber(self)
        self.clo1.move(300, 300)
        self.clo1.display("12:00")
        self.clo1.setGeometry(250, 250,100,100)

        #################################
        # Datetime
        #################################
        self.dt1 = QDateTimeEdit(self)
        self.dt1.move(400, 400)
        # Eine von den 3 Unteren Funktionen darf nur aktiv sein
        #self.dt1.dateChanged.connect(self.calendar_function)
        #self.dt1.timeChanged.connect(self.calendar_function)


        # Setup Aktuelle Zeit
        now = QDateTime() # Element der QdateTime erzeugen
        now.setTime_t(int(time.time())) # Aus import time dem erzeugten QDateTime-element
        self.dt1.setDateTime(now)

        #################################
        # Connections der Signale hinter den Funktionen, da sonst die Funtkion schon beim Setup getriggert wird
        #################################
        self.dt1.dateTimeChanged.connect(self.calendar_function)

        #################################
        # Allgmeine Fenster Config (Hauptfenster)
        #################################
        self.setGeometry(50, 50, 1000, 500)
        self.setWindowTitle("My First GUI")
        self.setWindowIcon(QIcon("icon.png"))
        self.show()

    def calendar_function(self, date):
        print(date.toString())

    def function_2(self, date):
        print(date.toString())

app = QApplication(sys.argv) # Neue Default-Application anlegen
w = Fenster() # Einfaches Fenster bauen -> Neue Instanz w
sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird