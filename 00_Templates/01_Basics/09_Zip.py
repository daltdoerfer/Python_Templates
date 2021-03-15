 # ZIP, praktisches Zusammenführen von Daten in eine Liste oder Tupel.
#Informatuion:
# Runde Klammern('','') -> Tupel
# Eckige Klammern['','','',''] ->  Listen
smaller = [1,2,3,6]
name = ['jan', 'peter', 'horst','python', 'dieser Eintrag sollte nicht auftauchen']

# Ausgabe Möglichkeit 1:
for (val1, val2) in zip(smaller, name): # Zip hört auf wenn die kleinere Liste zu Ende ist
    print(val1, val2)
#       1 jan
#       2 peter
#       3 horst
#       6 python


# Ausgabe Möglichkeit 2:
neue_liste = list(zip(smaller,name))
print(neue_liste)
#       [(1, 'jan'), (2, 'peter'), (3, 'horst'), (6, 'python')]


# Ausgabe als Tupel:
for val in neue_liste:
    print(val)
#       (1, 'jan')
#       (2, 'peter')
#       (3, 'horst')
#       (6, 'python')


# Ausgabe als Liste
for val in neue_liste: # Es wird für Range der neuen Liste jeweils jedes zusammengezippte Element aufgerufen
    print(val[0], val[1])
#       1 jan
#       2 peter
#       3 horst
#       6 python