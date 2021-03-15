# For Schleife (einfaches Iterieren)

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

print(range(3))
for i in range(3):

    print(i)
    zahl_input = int(input('Geben sie eine Zahl ein!\n'))

    if zahl_input < 10:
        print("Fall 1") # Anweisung in IF-Bedingung muss eingeschoben sein
    elif zahl_input >= 10 and zahl_input < 20: # Elseif -> elif
        print("Fall 2")
    else:
        print("Fall 3")

einkaufs_liste = ['Apfel','Birne','Gemüse']

for item in einkaufs_liste: # Python erkennt die Größe der Liste selber
    print(item)

