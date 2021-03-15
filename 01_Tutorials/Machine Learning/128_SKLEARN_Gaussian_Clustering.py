# https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html
# Standardabweichung wird in diesem vereinfachten Code Konstant auf 2 gesetzt. Man will nur den Mittelwert erlenen
# Wichtige Parameter des Gaussian mixture Models:
# n_components -> Wie viele Cluster will ich bilden
# covariance_type -> Wie soll covarianz berechnet werden (full ist der Komplizierteste)
# max_iter -> Wieviele Update-Schritte sollen ausgeführt werden
# Attributes:
# means_
# covariances_
# converge_ -> schauen ob Expectation/Maximazation Algorithmus konvergiert oder doch besser mehr Iterationen sinnvoll sind

# Imports

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.mixture import GaussianMixture
from plotting import *

np.random.seed(22)

# Toy Dataset
def generate_dataset():
    cov1 = np.array([[1, 0], # Kovarianzmatrix mit nur Werten auf der Hauptdiagonalen
                     [0, 2]])
    cov2 = np.array([[2, 0],
                     [0, 1]])
    data1 = np.random.multivariate_normal(np.array([0, 0]), cov1, 50) # Multivariate Normalverteil -> Keine Standardabweichung sondern Kovarianzmatrix
    data2 = np.random.multivariate_normal(np.array([2, 2]), cov2, 50)
    data = np.concatenate((data1, data2), axis=0)
    classes = np.array([0 for i in range(50)] + [1 for i in range(50)])
    return data, classes

x,y = generate_dataset()

plt.scatter(x[:, 0], x[:, 1], c=y)
plt.show()

n_components = 2
gauss = GaussianMixture(n_components=n_components, covariance_type="diag") # Kovarianztype = Diag nur wenn Kovarianzmatrix Werte auf der Diagnoalen hat
gauss.fit(x)

print("Model converged: ", gauss.converged_) # Modell hört auf zu itereren wenn Mittelwert und Kovarianzen sich nicht großartig weiter verbessert (innerhalb einer Range). Wert gibt TRUE oder FALSE zurück

covs = gauss.covariances_
means = gauss.means_

#print("Cov:\n", covs, "\n") # Kovarianzen in der Originalausgabe
print(np.diag(covs[0]), "\n") # Kovarianzmatrix zur ersten Normalverteilung (Datenwolke 1) -> Vergleiche Z.25
print(np.diag(covs[1]), "\n") # Kovarianzmatrix zur zweiten Normalverteilung (Datenwolke 2) -> Vergleiche Z.27
print("Means:")
print(means[0], "\n") # Vergleiche Mittelwerte aus generierten data1 -> Z:29
print(means[1]) # Vergleiche Mittelwerte aus generierten data2 -> Z:30

# Das Schlechte Ergebis aus oberen Zeilen kann entweder daran liegen, dass wir zu wenige Datenpunkte hatte oder, dass die Kovarianzmethode  covariance_type schlecht gewählt ist

cov1 = np.diag(covs[0])
cov2 = np.diag(covs[1])

plot_results(x, y, gauss.predict(x), means, [cov1, cov2], 0, "Gaussian Mixture") # Plot des Kreises mit Weite = Standardabweichung (bzw Kovarianzmatrix)
