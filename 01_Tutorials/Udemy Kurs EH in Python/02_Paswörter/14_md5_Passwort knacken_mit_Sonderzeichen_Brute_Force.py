# In dieser Lektion werden wir ein Dictionary auf ein md5 Passwort starten incl. Sonderzeichen
# Wichtig: Im Dictionary sind Wörter OHNE Sonderzeichen daher müssen diese noch Kombiniert werden
# md5 ist eine kryptografische Hashfunktion die allerding nicht mehr aktuell ist
# https://de.wikipedia.org/wiki/Message-Digest_Algorithm_5

import hashlib

password_hash = "1e3bf495a62012e7caf5fdd25624605f"  # z.B. Hacker hat ein Hash entwendet und will wissen was versteckt sich dahinter

extra_chars = '!$%&/()=?' # Achtung: Es gibt noch viele weitere Sonderzeichen

#######################################################################
# Dictionary einlesen
# Wir lesen die Datei Zeile für Zeile ein und entfernen unerwünschte Zeichen
#######################################################################
with open("../data/dictionary.txt", "r") as file: # Eine Ebene von hier hoch und dann in data/ usw. rein

    for line in file: # Für jede Zeile in meiner Datei
        word = line.strip() # Der Strip Befehl entfernt z.B.: Leerzeichen oder Zeilenumbrüche vom Anfang UND Ende des Strings

        # Wörter mit Sonderzeichen Kombinieren
        for char in extra_chars:
            word_ext = word + char # Quasi Extra Term hinzufügen

            hash_hex = hashlib.md5(word_ext.encode()).hexdigest() # Jeweiliges Wort auf Byte Ebene Encoden und in Hex ausgeben
            if hash_hex == password_hash:  # Erinnerung password_hash = "1e3bf495a62012e7caf5fdd25624605f"
                print(word + char)
                break # Breche ab wenn gefunden

print("Programm fertig")


