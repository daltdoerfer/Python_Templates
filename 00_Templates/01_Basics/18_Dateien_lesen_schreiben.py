# Dateien lesen und schreiben

text='Ich gehen heute nach Hause, yippie'
text2 = 'Ich gehe morgen auch nach Hause!'
data = [1,3,5,7,9,11]

# w = schreiben, r = lesen, a=append

#---------------Schreiben---------------------
with open('geschichte.txt', 'w') as f: # f for File
    f.write(text + str('!') + '\n') # Zeilenumbruch muss hier deklariert werden. Im text wird dieser nur mitgeschriben
    f.write(text2 + '\n')

#---------------Einlesen----------------------
    # f.readline()  # Liest Zeile für Zeile
    # f.readlines() # Liest alles ein

# Möglichkeit 1
text_neu = "" # String zum einlesen anlegen
with open('geschichte.txt', 'r') as f:

    for line in f:
        text_neu += line
print(text_neu)

# Möglichkeit 1
text_neu2 = "" # String zum einlesen anlegen
with open('geschichte.txt', 'r') as f:

        text_neu2 = f.readlines() # Rückgabe als Liste (Achtung '\n' vorhanden in Liste)
print(text_neu2)

# Möglichkeit 3
text_neu3 = "" # String zum einlesen anlegen
with open('geschichte.txt', 'r') as f:

        text_neu3 += f.readline() # Rückgabe als Liste (Achtung '\n' vorhanden in Liste)
print(text_neu3)

#---------------Appendix-----------------------

with open('data.txt', 'a') as f:
    for val in data: # Jeden Eintrag aus Data durchgehen
        f.write(str(val)+ ', ') # Mit ', ' Jeden Eintrag auseinderhalten

##########################################################################################
# Beispiel 2:
# Aus https://www.udemy.com/course/ethical-hacking-mit-python/learn/lecture/8104862#overview
########################
with open("../Tutorial/data/dictionary.txt", "r") as file: # Eine Ebene von hier hoch und dann wieder in data/ usw. rein
    for line in file: # Für jede Zeile in meiner Datei
        word = line.strip() # Der Strip Befehl entfernt z.B.: Leerzeichen oder Zeilenumbrüche vom Anfang UND Ende des Strings
        print(word)
        break # Nach erster Zeile Abbrechen