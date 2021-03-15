# Crossvalidation nur Hinleitung zu Random Search und Grid Search
# Stichwort: Crossvalidation, KNeighbors Regressor

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


# Cross Validation mit KFolds (Crossvalidation eigentlich bei Datensätze im höheren 1000er Bereich)
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
print(x_train.shape, x_test.shape)

# 2/3 von den 455 sind dann im Train set und 1/3 von 455 sind in Validationset
kf = KFold(n_splits=3, shuffle=True, random_state=42) # https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html
clf = KNeighborsClassifier(n_neighbors=3) # KNN-Classifier mit Hyperparameter n_neigbours = 3

scores = cross_val_score(clf, x_train, y_train, cv=kf, n_jobs=-1) # https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html
predicitons = cross_val_predict(clf, x_train, y_train, cv=kf, n_jobs=-1) # https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html
mean_score = round(np.mean(scores),4) # Mittewert von scores auf 4. Nachkommastelle gerundet

print("Scores: ", scores) # Zeigt alle Scores der KFold=3 Testsets auf
print("Mean Score: ", mean_score) # Aussage über alle Modelle mit Crossvalidation

plt.plot(range(len(scores)), scores, color="blue")
plt.xlim(0, 2)
plt.ylim(0.75, 1)
plt.axhline(mean_score, linestyle="-", color="red")
plt.show()