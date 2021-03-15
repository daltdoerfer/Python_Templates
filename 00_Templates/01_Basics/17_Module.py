# Module laden und eigene erstellen
# https://stackoverflow.com/questions/4534438/typeerror-module-object-is-not-callable

# import os # Falls Modul woanders liegt außerhalb des selben Ordners kann so der Pfad angepasst werden

import numpy as np
import Modul
# Alternativen zum Importieren

# from numpy import * # nicht zu empfehlen, da wirklich alle Numpy Funktionen geladen werden
# print(mean([1,2]))
#
# from numpy import mean,median # Lädt nur die gewünschten Funktionen von Numpy -> Es muss kein np. vor Funktion gesetzt werden
# print(median([1,2,3]))



print(np.mean([1,2]))

Modul.func(1,2,3)

val, a,b = Modul.func_3(3, 2)
print(val, a, b)