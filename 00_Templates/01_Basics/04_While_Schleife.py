# While Schleife https://www.youtube.com/watch?v=VQ5285w8o0I

zahl_input = 0
ergebnis = 25
weiterspielen = True
zufallszahl = 14

while weiterspielen:

    zahl_input = int(input('Geben sie eine Zahl ein!\n'))
    print("Die eingegebene Zahl ist :", zahl_input)

    if zahl_input < 10:
        print("Zu niedrig") # Anweisung in IF-Bedingung muss eingeschoben sein
    elif zahl_input >= 10 and zahl_input < 20: # Elseif -> elif
        if zahl_input == zufallszahl:
            print("Gewonnen!")
            break  # Ende der while Schleife wie wenn while False
            # continue  # würde wieder in den nächsten Iterationsschritt der Schleife springen
    else:
        print("Zu hoch")

    weiterspielen = int(input('Weiterspielen (0 oder 1) ?\n'))