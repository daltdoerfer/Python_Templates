# In dieser Lektion werden wir ein Dictionary auf ein md5 Passwort starten
# md5 ist eine kryptografische Hashfunktion die allerding nicht mehr aktuell ist
# https://de.wikipedia.org/wiki/Message-Digest_Algorithm_5

import hashlib

# Wir wollen quasi aus der Hashfunktion ein Passwort ermitteln
# Zuerst schauen wir uns an, wie wir einen md5 - Hash berechnen können. Das geht mit dem Python - Modul `hashlib` (https://docs.python.org/3.6/library/hashlib.html):

password_hash = "9e083ec666c9f3db044bb7c381640227" # z.B. Hacker hat ein Hash entwendet und will wissen was versteckt sich dahinter



hash_byte = hashlib.md5("Hallo Welt".encode()) # md5 Summe eines Stringsberechnet der vorher auf byte-Ebene encoded wurde. Strings können intern nicht verwendet werden
print(f"Beispiel: md5 Bytecode von Hallo Welt: {hash_byte}")

hash_bit = hashlib.md5("Hallo Welt".encode()).digest()
print(f"Beispiel: md5 Binär von Hallo Welt: {hash_bit}")

hash_hex = hashlib.md5("Hallo Welt".encode()).hexdigest()
print(f"Beispiel: md5 Hexcode von Hallo Welt: {hash_hex}")


#######################################################################
# Zusammenfassung in eine Zeile im Zielformat
#######################################################################
o = hashlib.md5("Hallo Welt".encode()).hexdigest() # md5 Summe eines Stringsberechnet der vorher auf byte-Ebene encoded wurde. Strings können intern nicht verwendet werden
print(f"Beispiel: md5 Hex-Hashcode von Hallo Welt: {o}")

#######################################################################
# Dictionary einlesen
# Wir lesen die Datei Zeile für Zeile ein und entfernen unerwünschte Zeichen
#######################################################################
with open("../data/dictionary.txt", "r") as file: # Eine Ebene von hier hoch und dann in data/ usw. rein
    for line in file: # Für jede Zeile in meiner Datei
        word = line.strip() # Der Strip Befehl entfernt z.B.: Leerzeichen oder Zeilenumbrüche vom Anfang UND Ende des Strings
        print(word)
        print(hashlib.md5(word.encode()).hexdigest()) # Jeweiliges Wort auf Byte Ebene Encoden und in Hex ausgeben)
        break # Beendet Testausgabe nach einem Durchlauf

    # Neuen durchlauf ohne print Ausgabe Starten
    for line in file: # Für jede Zeile in meiner Datei
        word = line.strip() # Der Strip Befehl entfernt z.B.: Leerzeichen oder Zeilenumbrüche vom Anfang UND Ende des Strings

        hash_hex = hashlib.md5(word.encode()).hexdigest() # Jeweiliges Wort auf Byte Ebene Encoden und in Hex ausgeben

        if hash_hex == password_hash:  # Erinnerung password_hash = "9e083ec666c9f3db044bb7c381640227"
            print(word)
            break # Breche ab wenn gefunden

print("Programm fertig")


