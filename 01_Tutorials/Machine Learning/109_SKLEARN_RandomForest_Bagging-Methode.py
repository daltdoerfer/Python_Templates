# https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sklearn Methoden
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# CrossValidation mit KFold und GridSearch
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import GridSearchCV



# Dataset for Classification
dataset = load_wine()
x = dataset.data
y = dataset.target

print(x.shape, y.shape)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

## KNeighborsClassifier.
parameters = {'n_neighbors': [3, 5, 7, 9, 11],
              'weights': ['uniform', 'distance'],
              'p': [1, 2]}
neigh = KNeighborsClassifier()

clf = GridSearchCV(neigh, parameters, cv=3) # Ermittlung des besten Modells mit Grid Search ausgeführt
clf.fit(x_train, y_train)

print("Best params:")
print(clf.best_params_)
print(clf.best_score_)

neigh = KNeighborsClassifier(n_neighbors=5, p=1, weights="distance") # Modell mit besten ermittelten Parametern ausführen
neigh.fit(x_train, y_train)
score = neigh.score(x_test, y_test)
print("Test score: ", score)

## DecisionTreeClassifier
parameters = {"criterion": ["gini", "entropy"], # Ein Maß dafür wie sinnvoll eine tiefere  Verzweigung im Baum wäre
              "max_depth": [None, 3, 5, 7, 8, 9, 10, 11, 12],
              "max_features": [None, "auto", "sqrt", "log2"]} # max_features: None -> Alle Features werden genommen. Die anderen Möglichkeiten reduzieren den Feature-raum

dec_tree = DecisionTreeClassifier()

clf = GridSearchCV(dec_tree, parameters, cv=3) # Ermittlung des besten Modells mit Grid Search ausgeführt
clf.fit(x_train, y_train)

print("Best params:")
print(clf.best_params_)
print(clf.best_score_)

dt = DecisionTreeClassifier(criterion="gini", max_depth=11, max_features="auto")
dt.fit(x_train, y_train)
score = dt.score(x_test, y_test)
print("Test score: ", score)

## RandomForestClassifier:
# Trees können gleichzeitig berechnet werden

from sklearn.ensemble import RandomForestClassifier

parameters = {"n_estimators": range(2, 20), # Wichtister Parameter des RandomForest: n_estimators -> Wie viele Bäume will man ausprobieren
            "criterion": ["gini", "entropy"],
            "max_depth": [None, 3, 5, 7, 8, 9, 10, 11, 12],
            "max_features": [None, "auto", "sqrt", "log2"]}
random_forest = RandomForestClassifier()

clf = GridSearchCV(random_forest, parameters, cv=3, n_jobs=-1) # # Ermittlung des besten Modells mit Grid Search ausgeführt
clf.fit(x_train, y_train)

print("Best params:")
print(clf.best_params_)
print(clf.best_score_)

random_forest = RandomForestClassifier(criterion= 'gini', max_depth= None, max_features='auto', n_estimators=10) # Verwendung der besten ermittelten Parameter von oben
random_forest.fit(x_train, y_train)
score = random_forest.score(x_test, y_test)
print("Test score: ", score)