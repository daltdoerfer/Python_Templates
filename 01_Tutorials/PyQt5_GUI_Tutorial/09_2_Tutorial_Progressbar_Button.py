# Dieses Tutorial beinhaltet das einfügen von:
# Progressbar mit ButtonS und (Multi-)Threading (Programm muss weiterlaufen und lagert andere Prozesse aus)
# https://riptutorial.com/pyqt5/example/29500/basic-pyqt-progress-bar

import sys
import time

from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

TIME_LIMIT = 100 # Ausgelagertes TIME Limit, da mehrere Klassen darauf zugreifen

class External(QThread):
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(int)

    def run(self):
        count = 0
        while count < TIME_LIMIT:
            count += 1
            time.sleep(1)
            self.countChanged.emit(count)


class Fenster(QDialog):  # Wichtig für Status und Menübar von QMainWindow erben
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        #################################
        # Progressbar
        #################################
        self.pb1 = QProgressBar(self)
        self.pb1.setGeometry(0, 0, 300, 25)
        self.pb1.move(50, 50)
        self.pb1.setMaximum(100)

        self.bt1 = QPushButton("Start", self)
        self.bt1.move(50, 75)
        self.bt1.clicked.connect(self.onButtonClick)

        #################################
        # Allgmeine Fenster Config (Hauptfenster)
        #################################
        self.setGeometry(50, 50, 1000, 500)
        self.setWindowTitle("My First GUI")
        self.setWindowIcon(QIcon("icon.png"))
        self.show()

    def onButtonClick(self):
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

    def onCountChanged(self, value):
        self.pb1.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Neue Default-Application anlegen
    w = Fenster()  # Einfaches Fenster bauen -> Neue Instanz w
    sys.exit(app.exec_())  # Beendet Python Skript wenn Fenster geschlossen wird