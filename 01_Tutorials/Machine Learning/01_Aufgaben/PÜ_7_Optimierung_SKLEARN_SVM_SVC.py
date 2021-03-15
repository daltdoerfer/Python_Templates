# Imports
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotting import *

# Sklearn Methoden
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_digits
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import KFold
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load Dataset

mnist = load_digits()

x = mnist.data.astype(np.float32) # Jede Zeile beinhaltet Informationen zu einer Pixelzahl. 64 Spalten -> 8x8 Grauwert-Pixel pro Zahl
y = mnist.target.astype(np.float32)
print(x.shape)
print(y.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.33)

n_samples, n_features = x.shape
print("Bilder: ", n_samples)
print("Pixel: ", n_features)

# Plot random images: https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.imshow.html
for index, (image, label) in enumerate(zip(x_train[:10], y_train[:10])): # Nimmt die ersten 10 Werte von x_train und y_Test packt diese in eine Liste mit der Iteration (Start bei 0) an erste Zeile
    plt.subplot(2, 5, index + 1)
    plt.axis('off')
    plt.imshow(image.reshape((8, 8)), cmap=plt.cm.gray_r, interpolation='nearest') # Bilder sind 8x8 Pixel groß -> 64 Features -> Jedes Feature beschreibt grauwert
    plt.title('Train: %i' % (label+1))

plt.show()

# Normalisierung der Features mit dem Standardscaler
scaler = StandardScaler()
scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# Aufgabe 1 Trainiere eine SVM mit der GridSearch
# Was fällt dir beim Training auf ?
# Sklearn

parameters = {'kernel': ['rbf', 'poly', 'linear', 'sigmoid'],
              'gamma': [0.01, 0.001]}
svm = SVC()

start_time = time.time()
clf = GridSearchCV(svm, parameters, cv=10, n_jobs=-1)
clf.fit(x_train, y_train)
end_time=time.time()
print("Training done in ", (end_time-start_time), " seconds.")

y_pred = clf.predict(x_test) # Hier würde das beste Modell ausgewählt werden
score = clf.score(x_test, y_test)

# Aufgabe 2: Gebe die Genauigkeit und die Confusion Matrix an.
print("Score: ", score)
print("Confusion Matrix: \n", confusion_matrix(y_test, y_pred)) # Hauptachse der Confusionmatrix zeigt die Anzahl der richtigen Zuordnung der Punkte an. Die restlichen Punkte sind die Punkte die nicht richtig lagen
# Wenn Datensatz linear separierbar, dann gibt es in der Confusion Matrix NUR Werte auf der 1. Hauptachse
# Analyse z.B. bei Klasse 8 (Zeile 8) wurden die Zahlen 1,2,3 und 9 jeweils einmal falsch erkannt



# Aufgabe 3: Anwendung der PCA (Feature Reduction -> Haupkomponentenanalyse)
# Es soll min. 95 % der Varianz behalten werden
# Trainiere anschließened eine SVM mit der GridSearch
# Was fällt beim Training auf

# Daten neu laden
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.33)
# Normalisierung der Features mit dem Standardscaler
scaler = StandardScaler()
scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# PCA Feature Reduction
pca = PCA(n_components=0.95)
pca.fit(x_train) # Nur aus Trainingsdatensatz ermitteln
x_train_transformed = pca.transform(x_train)
x_test_transformed = pca.transform(x_test)

print("Dimensions before: ", x_train.shape[1])
print("Dimensions to keep: ", len(pca.components_))
print("Explained Variance: ", round(sum(pca.explained_variance_ratio_), 8)) # Gerundet auf 8 nachkommstellen

parameters = {'kernel': ['rbf', 'poly', 'linear', 'sigmoid'],
              'gamma': [0.01, 0.001],
              'max_iter': [1000]}
svm = SVC()

start_time = time.time()
clf = GridSearchCV(svm, parameters, cv=10, n_jobs=-1)
clf.fit(x_train, y_train)
end_time=time.time()
print("Training done in ", (end_time-start_time), " seconds.")

y_pred = clf.predict(x_test) # Hier würde das beste Modell ausgewählt werden
score = clf.score(x_test, y_test)
# Beurteilung:
# Aufgabe 2 resultierte in einem Score von 0.97306 bei einer Dauer von fast 4 Sekunden
# Mit der Feature reduction bekamen wir einen Score von 0.97306 bei einer Dauer von 2.4 Sekunden -> Also eine deutlicher Verringerung der Rechenzeit


# Aufgabe 2: Gebe die Genauigkeit und die Confusion Matrix an.
print("Score: ", score)
print("Confusion Matrix: \n", confusion_matrix(y_test, y_pred)) # Hauptachse der Confusionmatrix zeigt die Anzahl der richtigen Zuordnung der Punkte an. Die restlichen Punkte sind die Punkte die nicht richtig lagen
# Wenn Datensatz linear separierbar, dann gibt es in der Confusion Matrix NUR Werte auf der 1. Hauptachse
# Analyse z.B. bei Klasse 8 (Zeile 8) wurden die Zahlen 1,2,3 und 9 jeweils einmal falsch erkannt