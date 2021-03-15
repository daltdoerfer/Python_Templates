# Polynomiale Regression mit vorheriger Transformation der Datenpunkte -> Notwendig um aus Linearer Regression eine Polynomielle Regression zu machen -> Siehe Lektion 67
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

dataset = load_boston()
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

x= dataset.data[:,:2]  #Nimmt alle Zeilen und ausgewählte Spalten von Index 0 bis 1 (exclusive 2)
y= dataset.target

#Automatischer Split der Datensätze in Training und Test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3) # Train = 70%, Test = 30%

from sklearn.neighbors import KNeighborsRegressor

for i in range(2, 30): # Für verschiedene Nachbar-Anzahlen die Genauigkeit überprüfen
    knn = KNeighborsRegressor(n_neighbors=i) # i Nachbarn bestimmen
    # y=1, y=2, y=3,
    knn.fit(x_train, y_train)
    print("Score: ", knn.score(x_test, y_test), " i=",i)