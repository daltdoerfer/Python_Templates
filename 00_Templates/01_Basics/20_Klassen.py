# Erstellen von  Klassen

class Vektor3d:

    x = 0 # 3 Eigenschaften für Vektor3d mit Default Wert
    y = 0
    z = 0

    def __init__(self, x=0, y=0, z=0):
        # Wichtig: init Funktion muss bei jeder Klasse deklariert werden und (self) muss auch mindestens vorhanden sein
        # __init__ -> versteckte Build-Funktion zu Objekten (Konstruktor); self bezieht sich auf aktuelle Instanz des Objektes
        self.x = x
        self.y = y
        self.z = z

    def printCoordinates(self): # Funktion deklarieren
        print('X: ', self.x)
        print('Y: ', self.y)
        print('Z: ', self.z)

null_vektor = Vektor3d(0, 0, 0) # Unser nullvektor ist eine Instanz der Klasse Vektor3d
null_vektor.printCoordinates() # Unser nullvektor kann die vorher definierte Funktion aufrufen

v1 = Vektor3d(1, 2, 3)
v1.printCoordinates()