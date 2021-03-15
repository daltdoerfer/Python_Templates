# Dieses Tutorial beschreib den Minimalaufbau einer GUI mit PyQ
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv) # Neue Default-Application anlegen

w = QWidget() # Einfaches Fenster bauen -> Neue Instanz w


w.setGeometry(50, 50, 1000, 500) #Fenstergröße -> w.setGeometry(pos_start_x,pos_start_y, pixel_size_x, pixel_size_y) Info: Startposition beginnt nicht bei Titelbalken sonder beim internen Kasten
w.setWindowTitle("My first GUI") #Fenstertitel
w.setWindowIcon(QIcon("icon.png"))

w.show() # Fenster anzeigen

sys.exit(app.exec_()) # Beendet Python Skript wenn Fenster geschlossen wird