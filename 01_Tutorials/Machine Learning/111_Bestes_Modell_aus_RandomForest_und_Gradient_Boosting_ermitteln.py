# Suche nach Bestern Methode aus KNN, Random Forest oder Gradient Boosting
#https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html

# import warnings filter
from warnings import simplefilter

# ignore all Warnings
simplefilter(action='ignore', category=UserWarning)


import numpy as np
np.random.seed(42)
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

dataset = load_wine()
x = dataset.data
y = dataset.target
'''
print(x.shape, y.shape)
print(f"target names: {dataset.target_names}")
print(f"DESCR:\n{dataset.DESCR}")
df = pd.DataFrame(x, columns=dataset.feature_names)
df["y"] = y
df.head()
'''

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

## KNeighborsClassifier
parameters = {'n_neighbors': [3, 5, 7, 9, 11],
              'weights': ['uniform', 'distance'],
              'p': [1, 2]}
neigh = KNeighborsClassifier()

clf = GridSearchCV(neigh, parameters, cv=3) # Ermittlung des besten Modells mit Grid Search ausgeführt
clf.fit(x_train, y_train)

print("Best params KNN:")
print(clf.best_params_)
print(clf.best_score_)

## DecisionTreeClassifier (nur ein einziger Baum)
parameters = {"criterion": ["gini", "entropy"],
              "max_depth": [None, 3, 5, 7, 8, 9, 10, 11, 12],
              "max_features": [None, "auto", "sqrt", "log2"]} # max_features: None -> Alle Features werden genommen. Die anderen Möglichkeiten reduzieren den Feature-raum

dec_tree = DecisionTreeClassifier()

clf = GridSearchCV(dec_tree, parameters, cv=3) # Ermittlung des besten Modells mit Grid Search ausgeführt
clf.fit(x_train, y_train)

print("Best params Decision Tree:")
print(clf.best_params_)
print(clf.best_score_)

## RandomForestClassifier

from sklearn.ensemble import RandomForestClassifier

parameters = {"n_estimators": range(2, 20), # Wichtister Parameter des RandomForest: n_estimators -> Wie viele Bäume will man ausprobieren
            "criterion": ["gini", "entropy"],
            "max_depth": [None, 3, 5, 7, 8, 9, 10, 11, 12],
            "max_features": [None, "auto", "sqrt", "log2"]}
random_forest = RandomForestClassifier()

clf = GridSearchCV(random_forest, parameters, cv=3, n_jobs=-1) # Ermittlung des besten Modells mit Grid Search ausgeführt
clf.fit(x_train, y_train)

print(f"Best params RandomForest: {clf.best_params_}")
print(f"Score: {clf.best_score_}")


## Gradient Boosting Classifier: Grid Search CV
# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html
# Kann länger dauern, da die Bäume sequenziell abgearbeitet werden

from sklearn.ensemble import GradientBoostingClassifier
parameters = {
            "loss": ["deviance", "exponential"],
            "n_estimators": [10, 20, 40], # Wichtister Parameter des RandomForest: n_estimators -> Wie viele Bäume will man ausprobieren
            "criterion": ["mse", "mae"],
            "max_depth": [None, 3, 4, 8]}

clf = GradientBoostingClassifier()

grid_cv = GridSearchCV(clf, parameters, cv=10, n_jobs=-1) # Ermittlung des besten Modells mit Grid Search ausgeführt
grid_cv.fit(x_train, y_train)

print(f"Best params GradientBoosting: {grid_cv.best_params_}")
print(f"Score: {grid_cv.best_score_}")



############# Bestes Modell aus den Verschiedenen Methoden auf Test-Set prüfen###############

# KNNeigbors: Train Best Model
neigh = KNeighborsClassifier(n_neighbors=5, p=1, weights="distance") # Modell mit besten ermittelten Parametern ausführen
neigh.fit(x_train, y_train)
score = neigh.score(x_test, y_test)
print("Test score: ", score)

# Decisiontree Classifier: Train Best Model
dt = DecisionTreeClassifier(criterion="gini", max_depth=11, max_features="auto")
dt.fit(x_train, y_train)
score = dt.score(x_test, y_test)
print("Test score: ", score)

# RandomForest Classifier: Train Best Model
random_forest = RandomForestClassifier(criterion= 'gini', max_depth= None, max_features='auto', n_estimators=10) # Verwendung der besten ermittelten Parameter von oben
random_forest.fit(x_train, y_train)
score = random_forest.score(x_test, y_test)
print("Test score: ", score)


# GradientBoosting Classifier: Train Best Model
clf = GradientBoostingClassifier(criterion='mae', loss="deviance", max_depth=8, n_estimators=10) # Verwendung der besten ermittelten Parameter von oben
clf.fit(x_train, y_train)
score = clf.score(x_test, y_test) # Im letzten SChritt mit Testset validieren
print(f"Test Score: {score}")