# Bezieht sich auf Lektion 87_PCA_Hauptkomponentenanalyse
# Load Dataset
from sklearn.datasets import load_breast_cancer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = load_breast_cancer()
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

dataset.target_names
df.head()


x = dataset.data
y = dataset.target
print("Dimensions of Dataset x:", x.shape[0], "y: ", x.shape[1])

# (Pseudo-)Whitening the Data. Datensatz normalisieren
# -> Wird in späterem Kapitel nochmals erörtert
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler() # Objekt erstellen
scaler.fit(x) # Mittelwert und Varianz bestimmen jedes Features bestimmen
x = scaler.transform(x) # Transformation der x-Date auf Basis von Mittelwert und Varianz

print("Mean:\n", scaler.mean_)
print("Var: \n", scaler.var_) # Der Unterstrich bedeuted -> private Membervariable
print("Samples seen: ", scaler.n_samples_seen_)

# Import PCA from Sklearn
from sklearn.decomposition import PCA

# Aufgabe 1: Bestimme auf wie viele Dimensionen die PCA "mappen" soll, damit min. 90% der Varianz der Daten erhalten bleibt.
for i in range(1,50,1):

    n_components = i # Herunterbrechen der Infomation auf 3 Dimensionen (Features)
    pca = PCA(n_components=n_components, copy=True) # copy=True sagt ob Eingangsdatensatz x überschrieben wird oder nicht
    pca.fit(x)

    transformed_x = pca.transform(x)

    explained_variance_ratio = sum(pca.explained_variance_ratio_)
    if explained_variance_ratio >= 0.9:
        break
    else:
        best_explained_variance_ratio = explained_variance_ratio
        print("Sum of Explained Variance Ratio: ", round(explained_variance_ratio, 6), "\t with:", n_components, " components")

# Aufgabe 2: Wende das gefundene Setup der PCA auf den Datensatz an
n_components = 7 # Herunterbrechen der Infomation auf 3 Dimensionen (Features)
pca = PCA(n_components=n_components, copy=True) # copy=True sagt ob Eingangsdatensatz x überschrieben wird oder nicht
pca.fit(x)
transformed_x = pca.transform(x)

# PCA Variables and Data
print("Components:\n", pca.components_)
print(pca.components_.shape) # Hauptkomponentend die wir behalten haben. Aangezeigt werden die Eigenvektoren des Optimierungsproblems mit den höchsten Werten
print("Explained Variance ", pca.explained_variance_) # Zugehörigen Eigenwerte zu den obigen Eigenvektoren. Anzahl Eigenwerte entpsricht der Anzahl der Wunschdimensionen -> sprich n_components. Die Höhe der Eigenwerte sagen etwas über die übriggebliebene Varianz aus. Remember: Varianz sollte so hoch wie möglich sein.
print("Explained Variance Ratio", pca.explained_variance_ratio_) # Diese Werte beschreiben wieviel welcher Eigenwert an Informationsgehalt des übrig gebliebenene Datensatzes behält. Der erste Eigenwert pca.explained_variance beschreibt den Informationsgehalt in Prozent
print("Sum of Explained Variance Ratio", sum(pca.explained_variance_ratio_)) # Dieser Wert gibt den gesamtprozensatz an, wieviel Informationen mit den übrig gebliebenene Dimensionen beschrieben werden.


# Aufgabe 3: Splitte das (transformierte) Dataset in ein Trainings und Testset
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(transformed_x, y, random_state=42, test_size=0.30)

# Aufgabe 4: Wende das KNN Verfahren auf das (PCA-transformierte) Dataset an
from sklearn.neighbors import KNeighborsClassifier

best_score = 0.0

for i in range (1,11):
    n_neighbors = i
    knn = KNeighborsClassifier(n_neighbors=n_neighbors) # Aufruf des Konstruktors -> knn ist das Objekt
    knn.fit(x_train, y_train) # Trainingsfunktion mit Trainingsinformationen
    score = knn.score(x_test, y_test) # Bewertung für Testdatensatz. -> Genauigkeit (Accurcy). Wert zwischen 0 und 1

    if score > best_score:
        best_score = score
        print("Score:", score, "with ", n_neighbors, "neighbors.")

# Aufgabe 5: Wende das KNN ohne Whitening und one PCA an
dataset = load_breast_cancer()
x = dataset.data
y = dataset.target
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.30)


best_score_without_whitening = 0.0

for i in range (1,11):
    n_neighbors = i
    knn = KNeighborsClassifier(n_neighbors=n_neighbors) # Aufruf des Konstruktors -> knn ist das Objekt
    knn.fit(x_train, y_train) # Trainingsfunktion mit Trainingsinformationen
    score = knn.score(x_test, y_test) # Bewertung für Testdatensatz. -> Genauigkeit (Accurcy). Wert zwischen 0 und 1

    if score > best_score_without_whitening:
        best_score_without_whitening = score
        print("Score:", score, "with ", n_neighbors, "neighbors.")

# Aufgabe 5: Suche dir ein weiteres Matrix Decomposition aus der sklearn.decomposition Klasse aus und wende dies auf das Dataset an
from sklearn.decomposition import TruncatedSVD
dataset = load_breast_cancer()
x = dataset.data
y = dataset.target

best_score = 0.0

for i in range (1,30):
    n_components = i
    svd = TruncatedSVD(n_components=n_components) #
    svd.fit(x) #
    transformed_x = svd.transform(x)

    # Train Test Split
    x_train, x_test, y_train, y_test = train_test_split(transformed_x, y, random_state=42, test_size=0.30)

    for j in range(1,15):
        # KNN
        n_neighbors = j
        neigh = KNeighborsClassifier(n_neighbors=n_neighbors)  # Aufruf des Konstruktors -> knn ist das Objekt
        neigh.fit(x_train, y_train)  # Trainingsfunktion mit Trainingsinformationen
        score = neigh.score(x_test, y_test)  # Bewertung für Testdatensatz. -> Genauigkeit (Accurcy). Wert zwischen 0 und 1

        if score > best_score:
            best_score = score
            print("Score:", score, "\twith:\t ", n_neighbors, "\tneighbors and\t", n_components, "components")

