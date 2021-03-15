# In anderen Sprachen z.b. C gibt es Aufrufe über
# "Call by Value" dabei wird in einer Funktion eine Kopie des Wertes verwendet -> Originalwert wird nicht überschrieben
# Wobei im Aufruf "Call by Referece" wird mit einem Pointer direkt auf die Variable gezeigt und die kann überschrieben werden

# In Python wird eine Kombination aus Call by Reference und Call By Value Verwendet
# Es wird auf den Pointer gezeigt jedoch wird davon dann eine Kopie erstellt


#------------------------------------------------ Fall 1: Funktioniert wie geplant--------------------------------------------------
def plus1(liste): # Funktion zum Anhänmgen
    liste.append(1)

liste = [4,3,2] #Erzeugen einer Liste
print(liste)
plus1(liste)
print(liste)


#------------------------------------------------ Problem Fall 2: Funktioniert nicht wie geplant. Appendix wird nicht angehängtr
def plus1_2(liste): # Eine Kopie der Liste wird
    liste = [6,7,8] # Problem liegt hier da hier eine neue Zuweisung auf ein neues Objekt stattfindet welches eine ganz andere Adresse (Speicherstelle) hat
    liste.append(1)

liste = [4, 3, 2]  # Erzeugen einer Liste
print(liste)
plus1_2(liste) # Hier wird die alte Speicherstelle übergeben jedoch ändert sich diese in der Funktion
print(liste) # In diesem Aufruf wird auf die alte Speicherstelle geschaut

#------------------------------------------------  Lösung Fall 2: Return Value Verwenden (Beispiel mit mehreren Return Values
def plus1_2(liste): # Eine Kopie der Liste wird
    liste = [6,7,8] # Problem liegt hier da hier eine neue Zuweisung auf ein neues Objekt stattfindet welches eine ganz andere Adresse (Speicherstelle) hat
    liste2 = [9,9,9]
    liste.append(1)
    return (liste, liste2)

liste = [4, 3, 2]  # Erzeugen einer Liste
print(liste)
liste,liste2 = plus1_2(liste) # Hier wird die alte Speicherstelle übergeben jedoch ändert sich diese in der Funktion
print(liste) # In diesem Aufruf wird auf die alte Speicherstelle geschaut
print(liste2) # In diesem Aufruf wird auf die alte Speicherstelle geschaut