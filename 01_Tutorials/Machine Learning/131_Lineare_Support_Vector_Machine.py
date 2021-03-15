# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotting import *

# Sklearn Methoden
from sklearn.datasets import load_digits
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

np.random.seed(42)

# Toy Dataset
def generate_dataset():
    num_p = 50
    cov1 = np.array([[1, 0],
                     [0, 2]])
    cov2 = np.array([[2, 0],
                     [0, 1]])
    data1 = np.random.multivariate_normal(np.array([0, 0]), cov1, num_p) # Erzeugt x,y Pärchen um Mittelwert [0,0] mit Cov1
    data2 = np.random.multivariate_normal(np.array([2, 2]), cov2, num_p)
    data = np.concatenate((data1, data2), axis=0) # Verkettet beide Arrays
    classes = np.array([-1 for i in range(num_p)] + [1 for i in range(num_p)])
    return data, classes

x, y = generate_dataset()

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.3) # Datensatz aufteilen in Train und Test

# Definition: Lineare Separierbarkeit -> Wenn sich keine Punkte aus 2 Datensätzen überschneiden
# Plot des Datensatzes -> Nicht linear separierbar -> Lineares Modell findet keine optimale Lösung: Dazu aber mehr in folgenden Kapiteln
plt.scatter(x_train[:,0], x_train[:,1], c=y_train)
plt.show()



clf = LinearSVC()# SCV-> Support Vector Machine für Klassifikation (SVC)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
weights = clf.coef_[0] # Gewichte
bias = clf.intercept_ # Bias für Gerade
score = clf.score(x_test, y_test)

# Werte die die Gerade beschreiben
print(weights)
print(bias)

#Performance
print("Score: ", score)
print("Confusion Matrix:\n ", confusion_matrix(y_test, y_pred)) # Hauptachse der Confusionmatrix zeigt die Anzahl der richtigen Zuordnung der Punkte an. Die restlichen Punkte sind die Punkte die nicht richtig lagen
# Wenn Datensatz linear separierbar, dann gibt es in der Confusion Matrix NUR Werte auf der 1. Hauptachse

fig, ax = plt.subplots(1, 1)
plt.scatter(x_test[:,0], x_test[:,1], c=y_test)
plot_contours(ax, clf, x_test[:,0], x_test[:,1], cmap=plt.cm.coolwarm, alpha=0.4)
plt.show()