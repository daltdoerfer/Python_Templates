### Vererbung in Python: https://www.youtube.com/watch?v=d3Wqi7asNXg  ab Minute 6 weiter

# Erstellung Parent-Klasse: Deklaration Klasse von der geerbt werden soll
class Tier:
    rasse = ""
    geschlecht = ""
    alter = 0

    def __init__(self, rasse, geschlecht, alter):
        self.rasse = rasse
        self.geschlecht = geschlecht
        self.alter = alter

    def printRasse(self):
        print('(Tier) Rasse : ', self.rasse)

# Erstellung der zu erbenden Klasse: Vererbung von Eigenschaften von Klasse Tier auf Klasse Hund
class Hund(Tier):
    tatzen_size = 0
    
    def __init__(self, tatzen_size, rasse, geschlecht, alter):
        super(Hund, self).__init__(rasse, geschlecht, alter)  # Konstruktor von Parent muss erstmal aufgerufen werden -> Verwendung von Superkonstruktor
        'super().__init__(<Elternklaseneigneschaften (Tier)> '  # Ab Python 3 kann super() leer bleiben

        self.tatzen_size = tatzen_size

    def printRasse(self): # Wird diese Funktion aufgerufen wird einmal die Parent Funktion ausgeführt durch das Super und anschließend die lokale Print Fuktion mit "(Hund)"
        super(Hund,self).printRasse()
        print('(Hund) Rasse : ', self.rasse)


###--------------------- Ab hier werden die Objekte angelegt----------------------------

hund_1 = Hund(10, 'Dackel', 'Männlich', 5)
hund_1.printRasse()  # Wir können die Funktion der Elternklasse aufrufen obwohl diese nicht in Klasse Hund vorkommt -> Sie wurde vererbt

