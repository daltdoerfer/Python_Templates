# Dieses Tutorial beschreib den Minimalaufbau einer GUI mit PyQ
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore

class Fenster(QWidget): # Erben von QWidget
    def __init__(self):
        super().__init__()
        self.initMe()

        # method for widgets

    def initMe(self):

        QToolTip.setFont(QFont('Arial', 14))

        self.setToolTip('This is my <b>Window</b>')  # Tooltip-Schrift per HTML Code formatierbar

        self.setGeometry(50, 50, 1000, 500) #Fenstergröße -> setGeometry(pos_start_x,pos_start_y, pixel_size_x, pixel_size_y) Info: Startposition beginnt nicht bei Titelbalken sonder beim internen Kasten
        self.setWindowTitle("My first GUI") #Fenstertitel
        self.setWindowIcon(QIcon("icon.png"))


        button = QPushButton('Drück mich', self) # Button erstellen
        button.move(50, 50) # Position des Buttons innerhalb des Fensters
        button.setGeometry(200, 150, 100, 40) # setting geometry of button. setGeometry(pos_start_x,pos_start_y, pixel_size_x, pixel_size_y)
        button.setToolTip('This is my <b>Button</b>') # Tooltip-Schrift per HTML Code formatierbar


        # Button_2 Anlegen
        button_2 = QPushButton('Exit', self)  # Button erstellen
        button_2.move(75, 75)  # Position des Buttons innerhalb des Fensters
        button_2.setGeometry(300, 200, 100, 40)  # setting geometry of button. setGeometry(pos_start_x,pos_start_y, pixel_size_x, pixel_size_y)
        button_2.setToolTip('<b>Exit Window</b>')  # Tooltip-Schrift per HTML Code formatierbar


        # Hier wird Button mit Funktion verknüpft (Wichtig die Funktion OHNE Klammern verwenden "()"
        # Alternative Events zu clicked(down+up): pressed(nur down) + released(nur up)
        button.clicked.connect(self.function_button_pressed) #EVENT: Button bei drücken mit der Funktion function_button_pressed verknüpfen
        # button.clicked.connet(QtCore.QCoreApplication.instance().quit) # Alternatives Event zum schließen der Applikation




        self.show()  # Fenster anzeigen

    def function_button_pressed(self):
        print("Button gedrückt")


app = QApplication(sys.argv) # Neue Default-Application anlegen
w = Fenster() # Einfaches Fenster bauen -> Neue Instanz w
sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird