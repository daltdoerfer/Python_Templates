# Dieses Tutorial beinhaltet das einfügen von:
# Komboboxen, Inputs aller Art
# https://www.youtube.com/watch?v=qdW_XlnOCxM

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
        # ComboBox (Dropdown)
        #################################
        self.cb1 = QComboBox(self) # Durch das self sind die Werte veränderbar
        self.cb1.move(50, 50)

        self.cb1.addItem("#C") # Erstes Element taucht als erstes auf
        self.cb1.addItem("Java")  # Additem wenn nur ein Element
        self.cb1.addItems(["Rust", "Hacken"]) # Liste geht auch -> JEdoch addItems verwenden
        self.cb1.currentIndexChanged.connect(self.clicked) #Element verbinden

        #################################
        # Spinbox (Dropdown)
        #################################
        self.sp1 = QSpinBox(self)
        self.sp1.move(100, 100)
        self.sp1.valueChanged.connect(self.funktion1)

        #################################
        # Slider
        #################################
        self.sl1 = QSlider(self)
        self.sl1.move(150, 100)

        # Trigger-Varianten: Eine von den folgenden 4 Zeilen darf nur aktiv sein
        #self.sl1.valueChanged.connect(self.funktion1) # Jedes Mal wenn verändert wird
        #self.sl1.sliderPressed.connect(self.funktion1) # Veränderung NUR bei Klick auf Slider
        #self.sl1.sliderMoved.connect(self.funktion1) # Entspricht eigentlich valueChanged
        self.sl1.sliderReleased.connect(self.funktion_slider)  # Triggert Funktion nur wenn Maus losgelassen wird

        #Eigenschaften des Sliders
        self.sl1.setMinimum(0)   # Minimaler Value-Wert
        self.sl1.setMaximum(300) # Maximaler Value-Wert
        self.sl1.setMinimumHeight(200) # Minimale Slidergröße
        self.sl1.setMaximumHeight(300) # Minimale Slidergröße
        self.sl1.setValue(50) # Startwert angeben

        #################################
        # Line Edit -> Edit-Fenster für eine Zeile
        #################################
        self.le1 = QLineEdit(self)
        self.le1.move(200, 200)
        self.le1.textChanged.connect(self.funktion_line_edit) # JEdes mal wenn der User etwas ändert wird getriggert
        #Input Maskten -> Lassen nur spezielle Inputs zu
        # WICHTIG: es darf nur eine der Folgenden Zeilen aktiv sein!
        #self.le1.setValidator(QIntValidator()) # Lässt nur int-Zahlen zu
        #self.le1.setValidator(QDoubleValidator())  # Lässt Double-Zahlen zu
        #self.le1.setInputMask("abcde") # Input Mask
        self.le1.setInputMask("99.9999")  # Input Mask aus vorgegeben Zahlen (mit Punkt)

        #Settings Line Edit
        self.le1.setEchoMode(QLineEdit.Password) # Nur Punkte (wie bei Passwortausgabe)
        self.le1.setReadOnly(False)  # TRUE -> nur lesen
                                     # FALSE -> auch schreiben

        #################################
        # Text Edit -> Edit-Fenster für mehrere Zeilen
        #################################
        self.te1 = QTextEdit(self)
        self.te1.move(500, 200)
        self.te1.textChanged.connect(self.funktion_text_edit)  # JEdes mal wenn der User etwas ändert wird getriggert
        # Settings Text Edit
        #self.le1.setEchoMode(QLineEdit.Password)  # Nur Punkte (wie bei Passwortausgabe)
        self.te1.setReadOnly(False)  # TRUE -> nur lesen
                                     # FALSE -> auch schreiben

        #################################
        # Allgmeine Fenster Config (Hauptfenster)
        #################################
        self.setGeometry(50, 50, 1000, 500)
        self.setWindowTitle("My First GUI")
        self.setWindowIcon(QIcon("icon.png"))
        self.show()

    def clicked(self, i): # Rückgabe eines zusätzlichen integers, welches symbol aktiv ist
        print(self.cb1.currentText()) # Aktueller oberster Text
        print(self.cb1.currentIndex()) # Gibt aktuellen Index in der Liste aus (Achtung Index Startet bei 0)

    def funktion1(self): # Rückgabe eines zusätzlichen integers, welches symbol aktiv ist
        print(self.sp1.value()) # Aktuelle Zahl aus Spinbox ausgeben -> Achtung bei zweistelliger Zahl kommt bei eingabe 2x returnwert z.b.: 50 -> 5 und 50

    def funktion_slider(self): # Rückgabe eines zusätzlichen integers, welches symbol aktiv ist
        print(self.sl1.value()) # Aktuelle Zahl aus Slider ausgeben
        print(self.sl1.minimum())  # Gibt das Maximum zurück
        print(self.sl1.maximum()) # Gibt das Maximum zurück

    def funktion_line_edit(self, text): # Rückgabe eines Textes
        print(self.le1.text) # Wenn der Text später aufgerufen werden soll

    def funktion_text_edit(self):
        print(self.te1.toHtml())  # Wenn der Text später aufgerufen werden soll
        print(str(self.te1.toPlainText()))  # PlainText() liegt als Qstring vor und muss in normalem String vorliegen

app = QApplication(sys.argv) # Neue Default-Application anlegen
w = Fenster() # Einfaches Fenster bauen -> Neue Instanz w
sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird