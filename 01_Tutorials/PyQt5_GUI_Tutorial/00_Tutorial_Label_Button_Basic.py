# Aufbau ohne Objektorientierte Klassendefinition
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore

def gedrueckt():
    print("Button Clicked")

def window():
    app = QApplication(sys.argv) # Neue Default-Application anlegen
    win = QMainWindow()  # Einfaches Fenster bauen -> Neue Instanz w
    win.setGeometry(200, 200, 300, 300) # setGeometry(pos_start_x,pos_start_y, pixel_size_x, pixel_size_y)
    win.setWindowTitle("Das ist der Titel")

    label = QtWidgets.QLabel(win)
    label.setText("Labelname")
    label.move(50, 50)


    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click Me")
    b1.clicked.connect(gedrueckt) # Funktionsbinding

    b2 = QtWidgets.QPushButton(win)
    b2.setText("Click Me 2")
    b2.clicked.connect(gedrueckt) # Funktionsbinding
    b2.setGeometry(200, 150, 100, 40)

    win.show() # Fenster anzeigen
    sys.exit(app.exec_())  # Beendet Python Skript wenn Fenster geschlossen wird


window()
