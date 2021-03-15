import numpy as np


# Listen zusammenschneiden (Slice) Syntax: liste[Start:Stop]
einkaufs_liste = ['milch', 'salz', 'eier', 'äpfel']

list_sliced = einkaufs_liste[1:3] # Nimmt die ersten 3 Werte aus der Liste: einkaufs_liste
print(list_sliced)

#Beispiel an Matrix
my_array = np.arange(4).reshape(2,2) # Return evenly spaced values within a given interval.
print(my_array)

print(my_array[1:2]) # Gibt 2. Spalte aus ^= my_array[1]
x_cooridnates = my_array[:,0] # Alles von der 0. Spalte ausgeben
y_cooridnates = my_array[:,1] # Alles von der 1. Spalte ausgeben
""" Info x_cooridnates = my_array[:,0] zeigt auch auf das im Speicher hinterlegt Array von my_array.
 Sprich wenn ich x_cooridnates ändern, würde würde sich auch my_array ändern
  mit x_cooridnates = my_array[:,0].copy würde man eine Kopie erstellen ohne das original zu verändern."""
print(x_cooridnates)
print(y_cooridnates)


# Bestimmte Bereiche aus Matrix nehmen
random_matr = np.random.randint(10, size=(6,6)) # Erzeugt Random integers zwischen 0 und 9 in 6x6 Matrix  https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.randint.html
print("Original Dataset")
print(random_matr)

matr_sliced = random_matr[:,:2] # Nimmt alle Zeilen und ausgewählte Spalten von Index 0 bis 1 (exclusive 2)
print(matr_sliced)

matr_sliced_2 = random_matr[:-4,:] # Nimmt alle Zeilen bis auf die letzten 4  und alle Spalten
print(matr_sliced_2)

matr_sliced_3 = random_matr[:,-2:] # Nimmt alle Zeilen (:,...) aber nur die letzten 2 Spalten [...,-2:}
print(matr_sliced_3)