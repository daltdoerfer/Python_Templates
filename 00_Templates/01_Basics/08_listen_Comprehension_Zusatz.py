# https://www.youtube.com/watch?v=UZgm_-rOuhE&list=PL_tdPUem3eE8NYCIDrQpcqZaLRWtnLj-w&index=9
import math
import numpy as np
# Beispiel 1
b = []
for i in range(18):
    b.append(i)
print(b)

# Beispiel 2
b = [math.log(i) for i in range(1,10)] #bei 1 Starten da log(0) nicht definiert.
print(b)

# Beispiel 3 doppelte Schleife in 3 Varianten
a = [i*j for i in range(10) for j in range(10)] #
print(a)

b = [[i*j for i in range(10)] for j in range(10)] # Matrixähnlich
print(b)
print(np.array(b)) # Array aus Liste erstellen

c = [[i*j] for i in range(3) for j in range(3)] #
print(c)
print(np.array(c)) # Array aus Liste erstellen

#https://www.youtube.com/watch?v=U48aPgJrL20&list=PL_tdPUem3eE8NYCIDrQpcqZaLRWtnLj-w&index=10
# Beispiel 4: if else -> Nur Gerade Zahlen verwenden (aus Beispiel 3b)

b = [[i*j if i*j % 2 == 0 else i*j*2 for i in range(10)] for j in range(10)]
print(b)
print(np.array(b)) # Array aus Liste erstellen

# Beispiel 5 für einfache If Abfrage mit Vector
c = [i**2 for i in range(20) if i% 2 == 0] # Wichtig: nur bei einfacher if Abfrage steht if hinten in der eckigen Klammer !.
print(c)
c = [i**2 if i% 2 == 0 else -1 for i in range(20) ] # So sieht mit if UND else aus
print(c)

#Erläuterung inline if else
a = None
s = 'hier kommt ein '+(a if a != None else '')+' string'
print(s)

# Einfacher Filter
l = [4,6,8,5,3,6,9,4,2]
nl = [x for x in l if x > 3]
print(nl)


