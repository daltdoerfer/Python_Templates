# Ramdom Search
# -> Zufällige Kombination aus allen möglichen Hyperparametermöglichkeiten erstellen, um bestes Modell zu ermitteln
# Vorteil oft wird zufällig ein gutes Modell gefunden, ohne viel vorwiwssen wie die Hyperparameter aussehen sollen

# Imports
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

# Dataset for Classification
dataset = load_breast_cancer()
x = dataset.data
y = dataset.target

print("Samples: ", len(x))

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df.head()

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.3)
print(x_train.shape, x_test.shape)

# RandomSearch
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint as sp_randint # Statistikpaket -> für zufällige WErte aus Intervall für RandomSearch

# Liste der Möglichen Parameter mit
# sp_randint(1,15) -> Zufällige Zahl zwischen 1 und 15. Intervall sollte jedoch gut überlegt werden
# "weights": ["uniform", "distance"] -> Zufälliger Auswahl zwischen uniform und Distance
# "p": [1, 2] -> Zufälliger Auswahl zwischen p = 1 oder 2
param_dist = {"n_neighbors": sp_randint(1,15), "weights": ["uniform", "distance"], "p": [1, 2]}
n_iter_search = 20 # Es sollen 20 Modelle erstellt werden

neigh = KNeighborsClassifier()

clf = RandomizedSearchCV(neigh, param_distributions=param_dist, n_iter=n_iter_search, cv=3) # CV (Crossvalidation). Bei kleinen Datensätzen CV~ 3. Bei großen Datensätzen (mehrere 1000) CV = 5...10
clf.fit(x_train, y_train)

for key in clf.cv_results_.keys(): # Listet Attribute auf die Aufgerufen werden können
    print(key)

for parameter in  clf.cv_results_["params"]: # Parameterausprägungen der 16 Modelle
    print(parameter)

print("Best params set found: ")
print(clf.best_params_, "\n")

means = clf.cv_results_["mean_test_score"]
stds = clf.cv_results_["std_test_score"]

for mean, std, params, in zip(means, stds, clf.cv_results_["params"]):
    print("%0.3f ((+/-%0.3f for %r" % (mean, std*2, params)) # Mittelwert über 3 folds +-2-fache Standardabweichung. Aussage -> Je höher die Standardabweichung des unverlässlicher ist Mittelwert. Bester Wert ist der Höchste Mittelwert mit möglichst niedrigster Standarabweichung
    # -> %0.3f entspricht Float Zahl mit 3 Nachommastellen


# Der Bisherige Aufwand mit Foldings etc wurde nur verwendet um die optimalen Hyperparameter zu bestimmen
# Jetzt wird das Modell nochmal mit den noch nicht verwendeten Testdatensatz und den Besten Hyperparametenr getestet
neigh = KNeighborsClassifier(n_neighbors=6, p=1, weights="uniform")
neigh.fit(x_train, y_train)
score= neigh.score(x_test, y_test)
print("Score :", score)

# Plot Bestes Modell: {'n_neighbors': 5, 'p': 1, 'weights': 'uniform'}
cv0 = clf.cv_results_["split0_test_score"][8] # Perfomances des Modells Nr 8 (unser besten Modells)
cv1 = clf.cv_results_["split1_test_score"][8] # Split Test Score ist die Auflistung der Einzelscores
cv2 = clf.cv_results_["split2_test_score"][8]

print(clf.cv_results_["split0_test_score"][8]) #Perfomances
print(clf.cv_results_["split1_test_score"][8])
print(clf.cv_results_["split2_test_score"][8])

plt.plot(range(3), [cv0, cv1, cv2], color="blue")
plt.xlim(0, 2)
plt.ylim(0.85, 1.0)
plt.axhline(np.mean([cv0, cv1, cv2]), color="red")
plt.show()