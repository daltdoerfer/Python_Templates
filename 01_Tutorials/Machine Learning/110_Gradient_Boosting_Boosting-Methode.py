# Gradient Boosting ist das Iterative Verbessern
#https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html

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
print(x.shape, y.shape)
print(f"target names: {dataset.target_names}")
print(f"DESCR:\n{dataset.DESCR}")

df = pd.DataFrame(x, columns=dataset.feature_names)
df["y"] = y
df.head()

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)


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

print(f"Best params: {grid_cv.best_params_}")
print(f"Score: {grid_cv.best_score_}")

## GradientBoosting Classifier: Train Best Model

clf = GradientBoostingClassifier(criterion='mae', loss="deviance", max_depth=8, n_estimators=10) # Verwendung der besten ermittelten Parameter von oben
clf.fit(x_train, y_train)
score = clf.score(x_test, y_test) # Im letzten SChritt mit Testset validieren
print(f"Test Score: {score}")