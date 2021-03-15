# Listen in Python
# a = a + b ode a+= b ?
# extend oder append https://www.python-kurs.eu/python3_listen.php
# insert, pop, count, iterieren?

einkaufs_liste = ['milch', 'salz', 'eier', 'äpfel']
zusatz_liste = ['backpulver','motoröl']
zusatz_liste2 = 'brot'

# a = a + b <=> a += b
#einkaufs_liste = einkaufs_liste + zusatz_liste # Alte liste wird komplett überschrieben und gelöscht
#einkaufs_liste += zusatz_liste # Entspricht Extend

einkaufs_liste.extend(zusatz_liste) # Liste per Extend in die Liste anhängen -> Entspricht "=+"
print(einkaufs_liste)

einkaufs_liste.append(zusatz_liste2) # Wenn eine Liste mit Append hinzugefügt wird wird diese wie folgt hinzugefügt [a, b, c, [d, e]] --> Daher lieber extend verwenden. Außer bei einzelnen Werten
print(einkaufs_liste)

einkaufs_liste.pop() # Zugriff auf letztes Element wenn pop() leer bleibt wird letztes Element gelöscht. (Returnwert "a" des aktuellen a=<Liste>.pop() ist immer der Wert der gelöscht wurde)
print(einkaufs_liste)

print(einkaufs_liste.count('milch')) # Schauen wie oft Milch in einer Liste auftaucht


for i in range(len(einkaufs_liste)): # Range darf nicht länger als Liste selbst sein daher -> len() verwenden
    print(einkaufs_liste[i])

for val in einkaufs_liste: # Macht das selbe wie oben, Python weiß selber wie lange die Liste ist
    print(val)

