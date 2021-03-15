# Dieses Tutorial beinhaltet das einfügen von:
# Bildern, Checkboxen, Radiobuttons, ToggleButtons
# https://www.youtube.com/watch?v=6qriyonapEE

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

        #########################
        # Qlabel -> Bild eingfügen
        #########################
        w = QLabel("Upvote", self)
        w.setPixmap(QPixmap("icon.png"))
        w.move(50, 50)

        #########################
        # Qlabel -> Link eingfügen
        #########################
        # Link 1: Einfügen setOpenExternalLinks(True)
        l1 = QLabel("Upvote", self)
        l1.setText("<a href= 'https://www.google.com'> Link 1: Zu Google</a>")  # Link in HTML Format
        l1.setOpenExternalLinks(True)  # Links erlauben -> clicked Funktion wird nicht aufgerufen
        l1.linkActivated.connect(self.clicked)
        l1.move(100, 50)

        # Link 2: Einfügen setOpenExternalLinks(False)
        l2 = QLabel("Downvote", self)
        l2.setText("<a href= 'https://www.google.com'> Link 2: Zu Google</a>")  # Link in HTML Format
        l2.setOpenExternalLinks(False)  # Links nicht erlaubt -> clicked Funktion wird aufgerufen
        l2.linkActivated.connect(self.clicked)
        l2.move(100, 70)

        # Link 3: Mouseover (Hovered) wird aktiviert wenn man das erste mal über den Link fährt
        l2 = QLabel("Downvote 2", self)
        l2.setText(f"<a href= 'https://www.google.com'> Link 3: Zu Google</a>")  # Link in HTML Format
        l2.setOpenExternalLinks(False)  # Links nicht erlaubt -> clicked Funktion wird aufgerufen
        l2.linkHovered.connect(self.clicked)
        l2.move(100, 90)

        #################################
        # Qlabel -> Checkbox einfügen
        #################################
        cb1 = QCheckBox("Check me", self)
        cb1.move(150, 150)
        cb1.toggle() # ISt die Zeile aktiv ist die Checkbox beim Programmstart bereits gesetzt, sonst ist sie nicht aktiv
        cb1.stateChanged.connect(self.funktion1)

        #################################
        # QPushButton -> Toggle Button
        #################################
        pb1 = QPushButton("Push me", self)
        pb1.setCheckable(True)
        pb1.move(250, 250)
        pb1.toggle() # ISt die Zeile aktiv ist die Checkbox beim Programmstart bereits gesetzt, sonst ist sie nicht aktiv
        pb1.clicked[bool].connect(self.funktion2)

        #################################
        # QPushButton -> Toggle Button
        #################################
        rb1 = QRadioButton("Push me", self)
        rb1.setCheckable(True)
        rb1.move(350, 350)
        #rb1.toggle()  # ISt die Zeile aktiv ist die Checkbox beim Programmstart bereits gesetzt, sonst ist sie nicht aktiv
        rb1.clicked[bool].connect(self.funktion2)

        #################################
        # Allgmeine Fenster Config
        #################################
        self.setGeometry(50, 50, 1000, 500)
        self.setWindowTitle("My First GUI")
        self.setWindowIcon(QIcon("icon.png"))
        self.show()

    def clicked(self):
        print("clicked")

    def funktion1(self):
        print("Funktion 1 aktiv")

    def funktion2(self, active): # Bool für aktiv oder nicht. -> notwendig für PushButton und Radio Button
        if active:
            print("active")
        else:
            print("not active")

app = QApplication(sys.argv) # Neue Default-Application anlegen
w = Fenster() # Einfaches Fenster bauen -> Neue Instanz w
sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird