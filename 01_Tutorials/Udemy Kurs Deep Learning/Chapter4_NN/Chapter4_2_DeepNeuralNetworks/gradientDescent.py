import numpy as np

from helper import f # Importiert Rosenbrock Funktion aus help.py
from helper import f_prime_x0 # Importiert Ableitung der Rosenbrock Funktion nach x0
from helper import f_prime_x1 # Importiert Ableitung der Rosenbrock Funktion nach x1
from helper import plot_rosenbrock # Importiert Plot der Rosenbrock Funktion

# Starpunkte generieren (Random Auswahl zwischen -2 und 2. Größere Werte würden bei Rosenbrock-Funktion zu groß werden, daher werden diese hier nicht betrachtet)
x0 = np.random.uniform(-2, 2)
x1 = np.random.uniform(-2, 2)
x_start = (x0, x1)
y_start = f(x0, x1)

print("Global minimum: ", 1, 1) # Da wollen wir hin, wissen wir aber noch nicht
print("X_start = ", x_start)
print("Y_start = ", y_start)
plot_rosenbrock(x_start)

#Hyperparameter: Einzustellende Parameter
learning_rate = 0.005  # [0.001, 0.00001] Lernrate üblicherweise zwischen diesen beiden Werte
num_iterations = 1000  # Epochs: Wie oft will ich ausführen

gradient_steps = []

for it in range(num_iterations):
    x0 = x0 - learning_rate * f_prime_x0(x0, x1) # new = old - learnrate * derivative. Minus weil man in Richtung des Steilsten Abstiegs will.
    x1 = x1 - learning_rate * f_prime_x1(x0, x1)
    y = f(x0, x1)
    if it % 100 == 0: # Alle Hundert Schritte wird ein Ausschnitt gemacht
        print("x0 = ", x0, " x1 = ", x1, " y = ", y)
        gradient_steps.append((x0, x1))

x_end = (x0, x1)
y_end = f(x0, x1)
print("X_end = ", x_end)
print("Y_end = ", y_end)
plot_rosenbrock(x_start=x_start, gradient_steps=gradient_steps)
