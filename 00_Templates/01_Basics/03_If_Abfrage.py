# https://www.youtube.com/watch?v=OmXOfKGd3Vs

zahl_input = 0
zahl_input = int(input('Geben sie eine Zahl ein!\n'))
print("Die eingegebene Zahl ist :", zahl_input)

if zahl_input < 10:
    print("Fall 1") # Anweisung in IF-Bedingung muss eingeschoben sein
elif zahl_input >= 10 and zahl_input < 20: # Elseif -> elif
    print("Fall 2")
else:
    print("Fall 3")