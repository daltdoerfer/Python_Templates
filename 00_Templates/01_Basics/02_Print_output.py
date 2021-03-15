
###################################################
# Doku am Beispiel Type Annotation
###################################################

def print_message(message: str): # Gibt an Dasss der Intput Message ein String sein sollte.
    print(message)               # Achtung: Python wird auch andere Datentypen weiter ausführen
    # Quasi nur Doku für einen selber


#################################################
# Split and Join mit Delimiter
#################################################
sentence = "ich bin der Satz"
print(sentence.split(" ")) # Split zerlegt hier an leerzeichen -> Zeige mir alle der Elemente
print(len(sentence.split(" "))) # Split zerlegt hier an leerzeichen -> Zeige mir anzahl der Elemente

sentence_list = ["ich", "bin", "ein", "Satz"]
print(" ".join(sentence_list)) # Kombiniert einen die einzelnen Elemente der Liste mit Leerzeichen als Delimiter Trennzeichen

for c in "Hallo":
    print(c) # Jeden Buchstaben in Hallo einzeln ausgeben

#################################################
# Ausgabe in anderen Datentypen
#################################################

print(b"hallo Welt") # Ausgabe und interne Speicherung der Werte als Byte Array (ASCII Codierung)
print("hallo Welt".encode()) # Macht das gleiche wie oben