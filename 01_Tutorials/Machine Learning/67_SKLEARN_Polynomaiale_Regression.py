# Polynomiale Regression Transformation der Datenpunkte auf das gewünschte Polynom mit Linearer Regression -> Entspricht der Polynomialen Regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

#Vergleich mit einfachem Linearen Modell nach Transformation
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Definition der Funktion die wir "nicht kennen" und über Polynomielle Regression approximieren wollen
def f(x):
    return np.sin(x)*x**2
x = np.linspace(0,10, 100) # Teilt den Bereich zwischen 0 und 10 in 100 Teile
y= f(x)

# Datensatz zur oberen Funktion Funktion
x_data = np.expand_dims(np.random.randint(0,10,100), axis=1) # Muss für die verwendung in Numpy extended werden auf Achse 1
x_data = np.sort(x_data, axis=0) # Muss für die verwendung in Numpy zusätzlich sortiert werden
y_data = f(x_data)

fig= plt.figure(figsize=(12,10))

plt.plot(x,y, color="cornflowerblue", linewidth=2, label="ground truth")
plt.scatter(x_data, y_data, color="navy", s=30, marker="o", label="training Points")

colors = ["blue", "red", "green", "yellow", "purple"]
for count, degree in enumerate([1,2,3,4,6]): # Verschiedene Grade für die Tranformation
    # Non Linear Transformation
    model = PolynomialFeatures(degree)
    model.fit(x_data, y_data)
    x_trans_data = model.transform(x_data)
    # Lineare Regression für Transformierte Daten aus Datensatz
    linear = LinearRegression()
    linear.fit(x_trans_data, y_data)
    y_pred = linear.predict(x_trans_data)
    print("Score: ", linear.score(x_trans_data, y_data), "for degree :", degree)
    # Plot Predictions
    plt.plot(x_data, y_pred, color=colors[count], linewidth=2, label="degree%d" % degree) # Hier wird nicht x_trans_data geplottet, da dieser Wert NUR für Transformation gebraucht wird -> Fließt somit in y_pred ein

plt.legend()
plt.show()

