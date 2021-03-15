##########################################################
# Zusammenfassung: Überprüfung folgender Klassifikationsverfahren:
# KNN - KNearest Neighbor
# Random Forest
# Gradient Boosting
# SVM - Support Vector Machine
#
# In diesem File wurde bei allen Verfahren (KNN, Random Forest, Gradient Boosting, SVM)
# jeweils eine Grid Search  mit 3 Folds gemacht (cv=3) -> Veränderbar
#
# Neuronale Netze befinden sich in Case Study 1.1.2, da NN bei Bildern im Vergleich zu anderen am Besten
##########################################################

import numpy as np
np.random.seed(42)
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

#### Helper
def print_grid_cv_results(grid_result):
        print(
                f"Best model score: {grid_result.best_score_} "
                f"Best model params: {grid_result.best_params_} "
        )
        means = grid_result.cv_results_["mean_test_score"]
        stds = grid_result.cv_results_["std_test_score"]
        params = grid_result.cv_results_["params"]

        for mean, std, param in zip(means, stds, params):
                mean = round(mean, 4)
                std = round(std, 4)
                print(f"{mean} (+/- {2 * std}) with: {param}")

#############################################################
# ---- Load MNIST Dataset: Zahlen 0-9 in 8x8 Farbmustern  ---
#############################################################
mnist = load_digits()
x = mnist.data
y = mnist.target

#############################################################
# ------ Splitting der Daten in Trainings und Testset -------
#############################################################
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3) # Bsp: 0.3 => Test: 30% + Train: 70%. (Default=None=0.25)


#############################################################
# ----------- Normalisieren des Datasets --------------------
# Siehe Lektionen: 104, 105, 106
# Übungen: PÜ_4
#############################################################
scaler = StandardScaler() # StandardScaler bei Normalverteilung der Daten besser als andere Scaler
scaler.fit(x)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

#############################################################
# ---------------- KNNeigbors Classifier --------------------
# Siehe Lektionen: 31
# Siehe Programmierübung: PÜ_2, PÜ_4
#############################################################
from sklearn.neighbors import KNeighborsClassifier

#Hyperparameter für Grid Search
params = {"n_neighbors": [i for i in range(2, 22, 2)], # Bis einschließlich 20 Neighbors, was schon viel ist. Stichwort Overfitting
        "weights": ["uniform", "distance"]}

clf = KNeighborsClassifier()

grid = GridSearchCV(clf, params, cv=3)
grid_result = grid.fit(x_train, y_train)

print_grid_cv_results(grid_result)

#############################################################
# ---------------- Random Forest Classifier ---------------
# Siehe Lektionen: 109, 111
#############################################################
from sklearn.ensemble import RandomForestClassifier

#Hyperparameter für Grid Search
params = {"n_estimators": [50*i for i in range(4, 10)], # 6 Möglichkeiten
        "max_depth": [i for i in range(20, 51, 10)] + [None], # 5 Möglichkeiten. None wäre der Defaultfall -> Verzwigt so lange weiter bis min_samples_split oder min_samples_leaf triggern würden
        "criterion": ["gini", "entropy"], # 2 Möglichkeiten
        "min_samples_split": [2, 4], # 2 Möglichkeiten
        "min_samples_leaf": [1, 2]} # 2 Möglichkeiten


clf = RandomForestClassifier()

grid = GridSearchCV(clf, params, cv=3, n_jobs=-1) # 3 Möglichkeiten. -> Möglichkeiten Gesamt 6*5*2*2*2*3 = 720
grid_result = grid.fit(x_train, y_train)

print_grid_cv_results(grid_result)

#############################################################
# --------------- Gradient Boosting Classifier --------------
# Siehe Lektionen: 111
#############################################################
from sklearn.ensemble import GradientBoostingClassifier

#Hyperparameter für Grid Search
params = {"n_estimators": [50*i for i in range(4, 10)], # Wenige Werte in dieser Berechnung, da lange Berechnungszeit, hier kann herum gespielt werden
          "max_depth": [i for i in range(20, 51, 10)] + [None]}

clf = GradientBoostingClassifier()

grid = GridSearchCV(clf, params, cv=3, n_jobs=-1)
grid_result = grid.fit(x_train, y_train)

print_grid_cv_results(grid_result)

#############################################################
#--------------- SVM CLASSIFICATION -------------------------
# Siehe Lektionen: 137, 138
# Siehe Programmierübung: PÜ_7
#############################################################
from sklearn.svm import SVC

#Hyperparameter für Grid Search
params = {"kernel": ["linear", "sigmoid", "rbf", "poly"]} # Info: Hier wurden nur die Kernels getestet. Jedes Kernel hat noch weiter unterparameter -> beachten

clf = SVC()

grid = GridSearchCV(clf, params, cv=3, n_jobs=-1)
grid_result = grid.fit(x_train, y_train)

print_grid_cv_results(grid_result)

#############################################################
# Finale Auswertung des BEST MODEL aller obiger Verfahren:
# Kommentar:
#############################################################
from sklearn.svm import SVC

best_params = {'kernel': 'rbf'} # Erstellung eines Dictionarys der Optimal ermittelten Parameter
best_classifier = SVC

regr = best_classifier(**best_params) # Übergabe eines Dictionarys als Key: Value Paar mit **
regr.fit(x_train, y_train)
y_pred = regr.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)

print(f"Accuracy: {acc}")
print(f"Confusion matrix:\n{cm}")

