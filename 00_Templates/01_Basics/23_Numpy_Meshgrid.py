# https://www.python-kurs.eu/matplotlib_konturdiagramme.php
# Ein Maschengitter (Meshgrid) ist ein rechteckiges Gitter (Datengitter), was aus zwei eindimensionalen Arrays erzeugt wird, d.h. den x-Werten und den y-Werten. Im weiteren Verlauf dieses Kapitels werden wir nochmals auf die Funktion meshgrid und ihre Alternativen zurückkommen.

import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(-3.0, 3.0, 100)
ylist = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(xlist, ylist)

print(xlist)
print(ylist)
print(X)
print(Y)

# Nun berechnen wir die Funktionswerte zu den Wertepaaren des Maschengitters:
Z = np.sqrt(X**2 + Y**2)
print(Z)

# Erzeugung des Konturplots
plt.figure()
cp = plt.contour(X, Y, Z)
plt.clabel(cp, inline=True, fontsize=10)
plt.title('Konturplot')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.show()

# Erzeugung eines gefüllten Konturplots
plt.figure(2)
cp = plt.contourf(X, Y, Z)
plt.colorbar(cp)
plt.title('Gefüllter Konturplot')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.show()