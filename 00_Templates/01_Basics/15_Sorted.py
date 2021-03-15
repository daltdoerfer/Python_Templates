# Sortieren von Datensätzen in Python
# pip install random2

import random

data = [random.randint(0, 100) for _ in range(10)] # Liste mit 10 zufälligen Werten zwischen 0 und 100
print(data)

# sorted: neue Liste wird erstellt returned sorted() .Funktioniert auf alles iterierbare
# sort: in-place sortierung der aktuellen variablen .sort()  . Negativbeispiel name.sort() # Geht mit .sort nicht

data.sort()
print(data)

data.sort(reverse=True) # Auflsistung größte zuerst
print(data)


data = [random.randint(0, 100) for _ in range(10)] # Liste mit 10 zufälligen Werten zwischen 0 und 100
print(data)

data2 = sorted(data, reverse=True) # Müssen sorted(data) einer neuen Variablen zuweisen
print(data2)

name = 'jan'
name_sorted= sorted(name) # Geht bei Strings, Tupel, Dictionarys
print(name_sorted)
