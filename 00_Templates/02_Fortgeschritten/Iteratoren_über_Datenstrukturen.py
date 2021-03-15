# https://www.youtube.com/watch?v=h9R1ZhIS7wM&list=PL_tdPUem3eE8NYCIDrQpcqZaLRWtnLj-w&index=12
# Fall man hat eigene Klasse und Datenstruktur geschrieben und man will darüber mit einer Schleife itereiren
# Beschreibung Iterator ist Zeiger auf Datenstruktur
# Möglichkeit zur Implementierung einer Schnittstelle für Datenstruktur (Handhabung einer Datenstruktur)
#
# --------------------------Basic Funktionen Iterator------------------------
for x in ['asdf', 'qwert', 'zxcv']:
    print(x)

for x in 'asdf':
    print(x)

d = {'hallo': 'welt', 'ich': 'da'}
for x in d:
    print(x)  # Ausgabe Keys
    print(d[x])  # Ausgabe Values zu Keys

# ------------------------- Ziel Nachbau der Range Funktion mit Iteratoren (über Klasse)---------------------
# Folgende Funktion soll nachgebaut werden.
y = list(range(2, 20, 3))  # Erstellenn eines Vektors: Start 2 bis (exclusive) 20 mit Stepsize 3
print('Target:', y)

# Nachbau als Klasse
class MyRange:
    def __init__(self, a, b=0, step=1): # b und step sind optionale Parameter mit jeweiligen Default Werten
        if b:
            (b,a) = (a,b)# Dreieckstausch damit wenn nur end gesetzt, dieser als Startwert genommen wird
                         # Grund wenn nur ein Wert in Funktion MyRange(a) gilt dieser Wert als Endwert
                         # Sind jedoch 2 Werte angegeben gilt der erste als Start und der 2. als Endwert
        self.lower = b
        self.upper = a
        self.step = step
        self.current = self.lower # immer aktueller Wert
    def __iter__(self):  # Methode Iterator -> Macht Iterationen möglichen. : Wird einmal am Anfang aufgerufen
        return self  # Gibt Iterator zurück.

    def __next__(self): # Methode: Bei jedem Iterationsschritt aufgerufen
        old = self.current
        if self.current >= self.upper: # Abbruchkriterium für den Iterator (wenn aktuelles Element >= oberer Grenzwert)
            raise StopIteration # Befehl um aus Loop zu gehen. Abbruch
        self.current +=self.step
        return old

for x in MyRange(4,8):
    print(x)

# Manuelle Ausführung der Iteration über das Klassenobjektes
objekt_einer_klasse = MyRange(4,8) # Erstellen eines Klassenobjektes
#print(objekt_einer_klasse)
while(True):
    try:
        print(objekt_einer_klasse.__next__()) # Nächstes Element ausgeben
    except StopIteration:
        break # Aus While schleife gehen