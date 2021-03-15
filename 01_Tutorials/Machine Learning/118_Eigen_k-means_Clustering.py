# Unsupervised Learning k-means Clustering
# https://www.udemy.com/course/machine-learning-grundlagen-mit-python-inkl-ai-einfuhrung/learn/lecture/11566166#overview
# https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
# Wichtigste Parameter:
# n_clusters -> wieviele Centroids bzw. Cluster wir bilden wollen
# tol -> Toleranz
# max_iter -> Maximale Anzahle iterationen
# init -> Methode der Initialisierung der Cluster
# Attribute:
# cluster_center -> wo center liegt
# labels -> Zu welchem Cluster wurde Punkt zugeordnet
# inertia -> Quadratische Distanz zum zugehörigen Clustercenter

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from plotting import plot # Benötigt Datei plotting.py im selben Ordner

# Dataset for Classification
np.random.seed(42)
dataset = load_iris()
x = dataset.data[:, :2]
y = dataset.target # y-Werte sind normalerweise im Unsupervised Learning nicht gegeben bzw

colors = ["red", "green", "blue"]

#Plot der Daten
for idx, point in enumerate(x):
    plt.scatter(point[0], point[1], color=colors[y[idx]])
plt.show()

class KMeans:
    def __init__(self, n_clusters: int = 8, max_iter: int = 3_000): # Defaultwerte int = 8 ; 3000 == 3_000 -> Besser Übersicht mit "_"
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids_ = None

    def fit(self, x: np.ndarray): # y wird nicht entgegengenommen, da nichts gemacht wird in Unsupervised Learning
        rand_idxs = np.random.permutation(len(x))[:self.n_clusters] # Anzahl-"n_clusters" zufällige indizes aus der Gesamtmenge nehmen. [:self.n_clusters] sagt aus das Index 1 bis n_clusters-1 Einträge verwendet werden
        self.centroids_ = x[rand_idxs]
        for _ in range(self.max_iter):
            # Welcher Punkt gehört zu welchem Zentrum bzw. Cluster. Für jeden Cluster wird leere Liste angelegt und die Punkte die am nächjsten sind darin abgespeichert
            self.assignement = {
                i: [] for i in range(self.n_clusters) # Dictionary: Anzahl "n_clusters" jeweils leere Liste anlegen
            }
            # Step 1: Assignement
            for xi in x:
                distance_to_centroids = np.array(
                    [np.linalg.norm(xi - centroid) for centroid in self.centroids_] # List Comprehension. Wird für jeden Punkt betrachtet -> for xi in x:
                )
                closest_centroid_idx = np.argmin(distance_to_centroids) # Herausfinden des Index im Array. np.argmin() -> Returns the indices of the minimum values along an axis.
                self.assignement[closest_centroid_idx].append(xi) # Zuweisung in Dictionary -> xi (Punkt) Anhängen

            # Step 2: Update
            for cluster_idx in range(self.n_clusters): # für jeden Cluster
                if len(self.assignement[cluster_idx]) > 0: # Wenn diesem Cluster etwas zugewiesen wurde, dann soll dieser verschoben werden, sonst nicht
                    self.centroids_[cluster_idx] = np.mean(self.assignement[cluster_idx], axis=0) # Mittelwert -> Zentrum der Punkte ermitteln. Axis=0 -> Vertikale


    def predict(self, x: np.ndarray): # Predict Funktion kommt nach der Fit Funktion. -> Neue Punkte
        y_pred = np.zeros(shape=(len(x),))
        for idx, xi in enumerate(x):
            distance_to_centroids = np.array(
                [np.linalg.norm(xi - centroid) for centroid in self.centroids_] # List Comprehension. Wird für jeden Punkt betrachtet -> for xi in x:
            )
            closest_centroid_idx = np.argmin(distance_to_centroids)  # Herausfinden des Index im Array. np.argmin() -> Returns the indices of the minimum values along an axis.
            y_pred[idx] = closest_centroid_idx
        return y_pred

    def score(self, x: np.ndarray): # y wird nicht entgegengenommen, da nichts gemacht wird in Unsupervised Learning
            pass

kmeans = KMeans(n_clusters = 3, max_iter= 1_000)
kmeans.fit(x)
y_pred = kmeans.predict(x).astype(int) # y_Pred als Integerwerte ausgeben, da sonst Probleme mit Farben

print(kmeans.centroids_)
print(y_pred)


#Plot der Daten nach Clustering (Farben können tauschen im Vergleich zum ersten Plot da zufällig)
for idx, point in enumerate(x):
    plt.scatter(point[0], point[1], color=colors[y_pred[idx]], marker="o")
for centroid in kmeans.centroids_:
    plt.scatter(centroid[0], centroid[1], color="black", marker="*", s=200)
plt.show()

plot(x, y, y_pred, kmeans.centroids_, kmeans)