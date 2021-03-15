#!/usr/bin/python3
# Shebang:

# ACHTUNG Crypt läuft nicht auf Windows
# Linux Benutzerinformationen mit Gecryptetem PW erhalten
# # cat /etc/shadow -> Anzeigen der Gecrypteten PW´s
# Aufsschlüsselung
# PW: test_dummy:$6$.Uc8mzzsy5S40Rhi$96L/FJHcm/i7qQaOQ6MVTq4rOqEBKgNCYB/GSl45ZJWGKZf/NXFkY/Pq230hmQUhetAC..iXd.11lvPgKRvhX0:18662:0:99999:7:::
# USER:     test_dummy
# CRYPT:    $6 -> sha512
# SALT:     $.Uc8mzzsy5S40Rhi
# PW HASH:  $96L/FJHcm/i7qQaOQ6MVTq4rOqEBKgNCYB/GSl45ZJWGKZf/NXFkY/Pq230hmQUhetAC
# PW INFO:  ..iXd.11lvPgKRvhX0:18662:0:99999:7:::


#########################################################################################################
# PASSWORT Hash und SALT Extrahieren -> In diesem Fall ist bekannt wo und wie lang das SALT ist
#########################################################################################################
entry = "test_dummy:$6$.Uc8mzzsy5S40Rhi$96L/FJHcm/i7qQaOQ6MVTq4rOqEBKgNCYB/GSl45ZJWGKZf/NXFkY/Pq230hmQUhetAC..iXd.11lvPgKRvhX0:18662:0:99999:7:::"  # Komplett Passwort HASH
password_hash = entry[11:117]
salt = entry[11:31]
print(f"Total Hash: {entry}")
print(f"Salt: {salt}")
print(f"PW Hash: {password_hash}")


import crypt
''' Beispiel der Verwendung
hash = crypt.crypt("HalloWelt", "$vOY41SSwhOryPuKM") # Verschlüsseln über Crypt mit Übergabe unserer SALT (Sonst kommt immer ein anderes Hash heraus)
'''

hash = crypt.crypt(password_hash, salt) # Verschlüsseln über Crypt mit Übergabe unserer SALT (Sonst kommt immer ein anderes Hash heraus)
print(hash)

extra_chars = '!§$%&/()=?' # Achtung: Es gibt noch viele weitere Sonderzeichen

#######################################################################
# Dictionary einlesen
# Wir lesen die Datei Zeile für Zeile ein und entfernen unerwünschte Zeichen
#######################################################################
with open("/root/bin/password-crack-dictionary.txt") as file:  # Eine Ebene von hier hoch und dann in data/ usw. rein

    for line in file:  # Für jede Zeile in meiner Datei
        word = line.strip()  # Der Strip Befehl entfernt z.B.: Leerzeichen oder Zeilenumbrüche vom Anfang UND Ende des Strings

        # Wörter ohne Sonderzeichen
        hash_hex = crypt.crypt(word, salt) # Jeweiliges Wort auf Byte Ebene Encoden und in Hex ausgeben
        if hash_hex == password_hash:  # Erinnerung password_hash = "1e3bf495a62012e7caf5fdd25624605f"
            print(f"PW lautet:{word}")
            break # Breche ab wenn gefunden


        '''
        # Wörter mit Sonderzeichen Kombinieren
        for char_1 in extra_chars:
            for char_2 in extra_chars:

                word_ext = word + char_1 + char_2  # Quasi Extra Term hinzufügen

                hash_hex = crypt.crypt(word_ext, salt) # Jeweiliges Wort auf Byte Ebene Encoden und in Hex ausgeben
                if hash_hex == password_hash:  # Erinnerung password_hash = "1e3bf495a62012e7caf5fdd25624605f"
                    print(word + char_1 + char_2)
                    break # Breche ab wenn gefunden
        '''

print("Programm fertig")