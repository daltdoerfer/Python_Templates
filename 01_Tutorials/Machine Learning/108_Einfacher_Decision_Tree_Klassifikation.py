# Hinleitung auf Thema Decision Tees
# Anmerkung: hier wird einzelner Baum verwendet. Normalerweise wird Kombination von Mehreren Bäumen Verwendet nicht nur einer
# https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
'''Hyperparameter:
 criteriuon -> Was für Fragen soll der Baum stellen (ja nein ?). Das Beste wäre wenn man mit einer Frage den Datensatz in 50:50 Split aufteilen
 max_depth -> Maximale Fragentiefe, wie viele Verzweigungsebenen es geben soll
 min_samples_split -> Am ende wie viele Datenpunkte dürfen übrig bleiben bevor noch einmal gesplittet wird
 min_samples_leaf -> Ende des Baumes (Blatt): Wie viele Datenpunkte müssen mindestens vorliegen bis Ende das Baumes erreicht.
 max_features -> Wie viele Features schaut man sich generell bei verzweigung anschauen will
'''

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

print("Samples: ", len(x))
print(x.shape, y.shape)

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df.head()

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# 2 * 7 * 3 * 4 = 168
parameters = {"criterion": ["gini", "entropy"], # Ein Maß dafür wie sinnvoll eine tiefere  Verzweigung im Baum wäre
              "max_depth": [None, 1, 2, 3, 4, 5, 10]}
dt = DecisionTreeClassifier()

# Bestes Modell über Grid Serach bestimmen
clf = GridSearchCV(dt, parameters, cv=3, n_jobs=-1)
clf.fit(x_train, y_train)

print("Best params: ")
print(clf.best_params_)
print(clf.best_score_)

dt = DecisionTreeClassifier(criterion="entropy", max_depth=10)
dt.fit(x_train, y_train)
score = dt.score(x_test, y_test) # Als letzten Schritt auf Testset Validieren
print(score)