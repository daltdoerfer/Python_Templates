'''
Dieses Tutorial beschreib den Minimalaufbau einer GUI mit PyQ
Folgende Aspekte werden in diesem Tutorial beschrieben:
1) Wie verbinde ich Widget mit einem Fenster oder einem Button mit Funktionen
2) Wie verbinde ich Buttons mit Funktionen/Events
3) Wie erstelle und verbinde ich Events
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QObject, pyqtSignal

#################################################
#            Eigene Events Erstellen (Zeile 19,39,40,74)
##################################################
class Neues_Event(QObject): # Schließ mich
    schliess_mich_Event = pyqtSignal() # Signal erstellen, welches global aktiv wird

#################################################
#  KeyPressEvent (Bereits in QPushButton Existent)
##################################################
class MyButton(QPushButton): # Erbt von QPushButton
    def keyPressEvent(self, QkeyEvent):
        if QkeyEvent.key() == Qt.Key_Escape:  # Wenn ESC-Taste Gedrückt wird
            self.close()  # Button schließen, da sich self auf den QPushButton bezieht

class Fenster(QWidget): # Erben von QWidget
    def __init__(self):
        super().__init__()
        self.initMe()

        # method for widgets

    def initMe(self):

        # Event Erstellen und Verknüpfen
        self.sig = Neues_Event() # Event Objekt anlegen
        self.sig.schliess_mich_Event.connect(self.close) # Event Objekt verknüpfen -> self.close Befehl, welches das Fenster schließt


        QToolTip.setFont(QFont('Arial', 14))

        # button = MyButton('Drück mich', self) # Button erstellen (Mit eigener Eigenschaft siehe class MyButton(QPushButton):
        button = QPushButton('Drück mich', self)  # Button erstellen (Standard)
        button.move(50, 50) # Position des Buttons innerhalb des Fensters
        button.setGeometry(200, 150, 100, 40) # setting geometry of button. setGeometry(pos_start_x,pos_start_y, pixel_size_x, pixel_size_y)
        button.setToolTip('This is my <b>Button</b>') # Tooltip-Schrift per HTML Code formatierbar

        # Hier wird Button mit Funktion verknüpft (Wichtig die Funktion OHNE Klammern verwenden "()"
        # Alternative Events zu clicked(down+up): pressed(nur down) + released(nur up)
        button.clicked.connect(self.function_button_pressed) #EVENT: Button bei drücken mit der Funktion function_button_pressed verknüpfen
        # button.clicked.connet(QtCore.QCoreApplication.instance().quit) # Alternatives Event zum schließen der Applikation

        self.setToolTip('This is my <b>Window</b>')  # Tooltip-Schrift per HTML Code formatierbar

        self.setGeometry(50, 50, 1000, 500) #Fenstergröße -> setGeometry(pos_start_x,pos_start_y, pixel_size_x, pixel_size_y) Info: Startposition beginnt nicht bei Titelbalken sonder beim internen Kasten
        self.setWindowTitle("My first GUI") #Fenstertitel
        self.setWindowIcon(QIcon("icon.png"))

        self.show()  # Fenster anzeigen

    def function_button_pressed(self):

        sender = self.sender() # Man bekommt eine Instanz des Buttons und kann damit machen was man will
        sender.move(100,100) # Beispiel Button nach klicken Verschieben
        #print(sender.text() +" " + "Button gedrückt")

    #Events erzeugen mit keyPressEvent, welches immer für das Gesamte Fenster Gilt
    def keyPressEvent(self, QKeyEvent): # Keypressevent gilt für ALLE Keys (nicht nur Maus)
        if QKeyEvent.key() == Qt.Key_W: # Wenn Key-Taste W Gedrückt wird
            #self.close() # Fenster schließen
            self.sig.schliess_mich_Event.emit() # Event/Signal Triggern. Emit-Methode -> Sendet Signal los. In Zeile



app = QApplication(sys.argv) # Neue Default-Application anlegen
w = Fenster() # Einfaches Fenster bauen -> Neue Instanz w
sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird