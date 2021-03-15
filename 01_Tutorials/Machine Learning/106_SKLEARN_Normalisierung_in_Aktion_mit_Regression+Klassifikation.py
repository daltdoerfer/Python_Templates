# Erklärung der Verwendeten Scaler und weiter auf:
# https://scikit-learn.org/stable/modules/preprocessing.html

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

def regr_method(i): #Switch Statement aufbauen
    switcher={
        0: 'KNeigborsRegressor',
        1: 'LinearRegression'
    }
    return switcher.get(i,)

methode = 1 # Wähle zwischen 0 (KNeigborsRegressor) und 1 (LineareRegression)
print(regr_method(methode)) # Aktuellen Switch Zustand abfragen
print(type(regr_method(methode))) # Datentyp ausgeben

boston = datasets.load_boston()
x, y = boston.data, boston.target
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.3)


if regr_method(methode) in 'KNeigborsRegressor': # Abfrag mit "in"
    print("Methode: ", methode," KNeighbors aktiv")
    regr = KNeighborsRegressor(n_neighbors=3)
elif regr_method(methode) == 'LinearRegression': # Abfrage mit ==
    print("Methode: ", methode, " Lineare Regression aktiv")
    regr = LinearRegression()

regr.fit(x_train, y_train)

print("Ohne!")
print("R2: ", regr.score(x_test, y_test))

boston = datasets.load_boston()
x, y = boston.data, boston.target
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.3)

scaler = StandardScaler() # Bei Normalverteilung der Daten besser
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

if regr_method(methode) in 'KNeigborsRegressor': # Abfrag mit "in"
    regr = KNeighborsRegressor(n_neighbors=3)
elif regr_method(methode) == 'LinearRegression': # Abfrage mit ==
    regr = LinearRegression()

regr.fit(x_train, y_train)

print("StandarsScaler!")
print("R2: ", regr.score(x_test, y_test))

boston = datasets.load_boston()
x, y = boston.data, boston.target
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.3)

scaler = MinMaxScaler() # Bei Gleichverteilung der Daten besser
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

if regr_method(methode) in 'KNeigborsRegressor': # Abfrag mit "in"
    regr = KNeighborsRegressor(n_neighbors=3)
elif regr_method(methode) == 'LinearRegression': # Abfrage mit ==
    regr = LinearRegression()

regr.fit(x_train, y_train)

print("MinMaxScaler!")
print("R2: ", regr.score(x_test, y_test))

# Ergebnis: die auswahl der Normalisierungsmethode hat auf die LineareRegression kaum auswirkung, da diese sehr einfach gestrickt ist.
# Auf KNeigbors hat es jedoch eine Auswirkung -> Standardscaler am Besten!!!
# Resumee: Keine Allgemeine aussage welche besser
# MinMaxScaler() -> Bei Gleichverteilung der Daten besser
# StandardScaler() -> Bei Normalverteilung der Daten besser