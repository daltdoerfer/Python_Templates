# Gradient Descent(Gradienten - Abstieg):
# https://www.udemy.com/course/machine-learning-grundlagen-mit-python-inkl-ai-einfuhrung/learn/lecture/10415950#overview

# Rosenbrock Funktion (3-D Fläche im Raum mit
def f(x0, x1):
    return 100 * (x0 ** 2 - x1) ** 2 + (x0 - 1) ** 2

def f_prime_x0(x0, x1): # Ableitung nach x0
    return 2 * (200 * x0 * (x0 ** 2 - x1) + x0 - 1)

def f_prime_x1(x0, x1): #Ableitung nach x1
    return -200 * (x0 ** 2 - x1)

# Globales Minimum bei x = (1, 1)
print("Minimum: ", f(1, 1))
print("Starte bei: ", f(-1, -1))

# Plot
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7, 7))
ax = fig.gca(projection='3d')

s = 0.3
X = np.arange(-2, 2. + s, s)
Y = np.arange(-2, 3. + s, s)

# Create the mesh grid(s) for all X/Y combos.
X, Y = np.meshgrid(X, Y)
# Rosenbrock function w/ two parameters using numpy Arrays
Z = f(X, Y)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, alpha=0.8)
# Global minimum
ax.scatter(1, 1, f(1, 1), color="red", marker="*", s=200)
# Starting point
ax.scatter(-1, -1, f(-1, -1), color="green", marker="o", s=200)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()


''' Berechnung 1'''
eta = 1 / 1000 # Learning Rate/Lernrate. Entspricht der Schrittweite-> daher klein genug wählen

x0 = -1 # Startpunkt x
x1 = -1 # Startpunkt y
y = f(x0, x1)

#Stop Kriterien
stop_conv = 1e-6
stop_div = 1e+6
stop_iter = 1e4
it = 0

downhill_points = []

while y > stop_conv and y < stop_div and it < stop_iter: # Iteration solang bis eines der Stop-Kriterien erreicht wurden
    x0 = x0 - eta * f_prime_x0(x0, x1) # Neuer Wert = Alter Wert - Lernrate * Gradientenfunktion
    x1 = x1 - eta * f_prime_x1(x0, x1)

    it += 1
    fx = f(x0, x1) # Berechnung neuer Funktionswert
    if it % 100 == 0: # Alle 100 Iterationen aktuelle Werte für Plot speichern
        downhill_points.append([x0, x1])

print("Solution: ", fx)
print("X0 = ", x0)
print("X1 = ", x1)



from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7, 7))
ax = fig.gca(projection='3d')

eps = 0
s = 0.3
X = np.arange(-2, 2. + s, s)
Y = np.arange(-2, 3. + s, s)

# Create the mesh grid(s) for all X/Y combos.
X, Y = np.meshgrid(X, Y)
# Rosenbrock function w/ two parameters using numpy Arrays
Z = f(X, Y)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, alpha=0.5)
# Global minimum
ax.scatter(1, 1, f(1, 1) + eps, color="red", marker="*", s=100)
# Starting point
ax.scatter(-1, -1, f(-1, -1) + eps, color="green", marker="o", s=100)

# Plot Updated Points
for (x0, x1) in downhill_points:
    ax.scatter(x0, x1, f(x0, x1) + eps, color="green", marker="o", s=50)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

''' Berechnung 2: Test mit verschiedenen Lernraten'''

for eta in [1e-7, 1e-6, 1e-5, 1e-4, 1e-3]:
    x0 = -1
    x1 = -1
    y = f(x0, x0)

    stop_conv = 1e-6
    stop_div = 1e+6
    stop_iter = 1e4
    it = 0

    while y > stop_conv and y < stop_div and it < stop_iter:
        x0 = x0 - eta * f_prime_x0(x0, x1)
        x1 = x1 - eta * f_prime_x1(x0, x1)

        it += 1
        fx = f(x0, x1)

    print("Eta = ", format(eta, 'e'))
    print("Solution: ", fx)
    print("X0 = ", x0)
    print("X1 = ", x1, "\n")