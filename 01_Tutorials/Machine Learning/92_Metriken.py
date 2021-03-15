# https://www.udemy.com/course/machine-learning-grundlagen-mit-python-inkl-ai-einfuhrung/learn/lecture/9364146#overview

# Übersicht Metriken https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics

# Load Dataset

import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

# Dataset for Classification
dataset = load_breast_cancer()
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

x = dataset.data
y = dataset.target
print("Dimensions of Dataset x:", x.shape[0], "y: ", x.shape[1])

# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=23111, test_size=0.30)

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df.head()

# KNN Classifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(x_train, y_train)

y_pred = neigh.predict(x_test)
y_true = y_test

''' 
Verwendung von Metriken

True positive = TP -> Ergebnis stimmt mit Prognose
False positive = FP
True negative = TN -> Ergebnis stimmt mit Prognose
False negative = FN

accuracy = (TP+TN)/N -> Hauptachse aller wahren Werte / Summe aller Werte.
'''
def accuracy(y_true, y_pred):
    n = len(y_true)
    true_predictions = [True for i in range(n) if y_true[i] == y_pred[i]] # Liste erstellen mit Wert 1 wenn Metrik-Ergebnis True Positive
    sum_true_predictions = sum(true_predictions)
    return (sum_true_predictions / n)

print("Acc: ", accuracy(y_true,y_pred))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)
print("Metrik aus SKLEARN Confusion Matrix: \n")
print(cm) # Ergebnis ganz gut da TRUE Positive (links oben) und True Negative (rechts unten) hohe Werte im Vergleich zum Rest