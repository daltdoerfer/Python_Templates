class Hacker: # Konvention -> Klasse wird Groß geschrieben
    def get_name(self):
        print(self.firstname + " " + self.lastname)

hacker1 = Hacker() # Objekt der Klasse erzeugen
hacker1.firstname = 'Max' # Neue Eigenschaft firstname deklarieren auf dieses Objekt
hacker1.lastname = 'Müller' # Neue Eigenschaft lastnaem deklarieren auf dieses Objekt

print(hacker1) # Objekt anzeigen
print(hacker1.firstname)
print(hacker1.lastname)
print("\n")

hacker1.get_name() # Interne Funktion des Objektes aufrufen

class Company:
    def get_name(self):
        print(self.name)

company1 = Company()  # Objekt einer 2. Klasse erzeugen
company1.name = "Hacking GmbH"

company1.get_name()

# Liste mit beiden Objekten erstellen
participants = [hacker1,
                company1
                ]

for participant in participants: # Objekte in der Liste durchgehen
    participant.get_name() # Beide Klassen haben die Funktion Namens get_name -> Python weiß aus dem Objekttyp, zu welcher Klasse diese Funktion gehört
    print(participant) # Ausgabe der Objekttypes