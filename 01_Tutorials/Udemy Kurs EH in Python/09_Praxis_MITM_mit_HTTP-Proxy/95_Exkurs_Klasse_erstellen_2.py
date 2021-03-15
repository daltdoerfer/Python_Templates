# Die Folgende Möglichkeit ermöglicht die Klasse noch kompakter zu schreiben als in Kapitel 93

class Hacker: # Konvention -> Klasse wird Groß geschrieben
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        print(self.firstname + " " + self.lastname)

hacker1 = Hacker("Max, Müller") # Instanz(Objekt) der Klasse erzeugen
# Durch Obige zuweisung, lassen sich die unteren beiden Zeilen einsparen
#hacker1.firstname = 'Max' # Neue Eigenschaft firstname deklarieren auf dieses Objekt
#hacker1.lastname = 'Müller' # Neue Eigenschaft lastnaem deklarieren auf dieses Objekt

print(hacker1) # Objekt anzeigen
print(hacker1.firstname)
print(hacker1.lastname)
print("\n")

hacker1.get_name() # Interne Funktion des Objektes aufrufen
