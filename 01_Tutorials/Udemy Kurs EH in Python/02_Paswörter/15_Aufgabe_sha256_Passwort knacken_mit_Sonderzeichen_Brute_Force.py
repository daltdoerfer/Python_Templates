# In dieser Lektion werden wir ein Dictionary auf ein md5 Passwort starten incl. Sonderzeichen
# Wichtig: Im Dictionary sind Wörter OHNE Sonderzeichen daher müssen diese noch Kombiniert werden

# Hier wurde hashlib.sha256 anstatt hashlib.md5 verwendet

import hashlib

password_hash = "112aa01926aebb65c5e09cc0a25ce2b5cff2ec5df0e9b123510db6753557e552"  # z.B. Hacker hat ein Hash entwendet und will wissen was versteckt sich dahinter

extra_chars = '!§$%&/()=?' # Achtung: Es gibt noch viele weitere Sonderzeichen

#######################################################################
# Dictionary einlesen
# Wir lesen die Datei Zeile für Zeile ein und entfernen unerwünschte Zeichen
#######################################################################
with open("../data/dictionary.txt", "r") as file:  # Eine Ebene von hier hoch und dann in data/ usw. rein

    for line in file:  # Für jede Zeile in meiner Datei
        word = line.strip()  # Der Strip Befehl entfernt z.B.: Leerzeichen oder Zeilenumbrüche vom Anfang UND Ende des Strings

        # Wörter mit Sonderzeichen Kombinieren
        for char_1 in extra_chars:
            for char_2 in extra_chars:

                word_ext = word + char_1 + char_2  # Quasi Extra Term hinzufügen

                hash_hex = hashlib.sha256(word_ext.encode()).hexdigest() # Jeweiliges Wort auf Byte Ebene Encoden und in Hex ausgeben
                if hash_hex == password_hash:  # Erinnerung password_hash = "1e3bf495a62012e7caf5fdd25624605f"
                    print(word + char_1 + char_2)
                    break # Breche ab wenn gefunden

print("Programm fertig")


