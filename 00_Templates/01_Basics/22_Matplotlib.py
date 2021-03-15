# Die Basics für Matplotlib Grafiken
# https://www.data-blogger.com/2017/11/15/python-matplotlib-pyplot-a-perfect-combination/
# https://matplotlib.org/gallery.html Übersicht aller Funktionen


# in Terminal: pip install  matplotlib
import matplotlib.pyplot as plt
import numpy as np
data = [1, 0, 7, 8, 10]

data_y = [1, 0, 7, 8, 10]
data_x = [0, 1, 2, 3, 4] # Entspricht range(len(data))

x1=0
y1=3

x2=5
y2=3

#plt.plot(data)
plt.plot(data, c='r') # plot -> Punkte werden mit Linien dargestellt (rot)
plt.plot((x1,x2),(y1,y2), c='y') # Plot einer Geraden (gelb)

# plt.scatter(data_x,data_y) # Punktewolke
plt.scatter(range(len(data)),data, c ='b') #Scatter -> Punkte (blau)


plt.xlabel('x-Werte')
plt.ylabel('y-Werte')

# Achsen-Bereiche manuell festlegen
# Syntax: plt.axis([xmin, xmax, ymin, ymax])
#plt.axis([0, 5, 0, 20])

plt.show()
plt.savefig('fig.png')

# Quadratische Funktion mit 20 Einträgen

x = np.arange(20) # Erstellt Array von 0 bis 19
y = x**2 # x^2
print(x)
print(y)
plt.scatter(x,y, c="blue")



plt.show()

