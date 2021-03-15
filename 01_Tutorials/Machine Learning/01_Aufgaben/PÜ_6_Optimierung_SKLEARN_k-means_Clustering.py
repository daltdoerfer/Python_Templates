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

# Übersicht Metriken https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
# Hier verwendete Metrik -> Clustering metrics -> Silhouette metric : https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
#from plotting import plot # Benötigt Datei plotting.py im selben Ordner
from sklearn.cluster import KMeans
from sklearn.metrics.cluster  import silhouette_score

# Dataset for Classification
np.random.seed(42)
dataset = load_iris()
x = dataset.data[:, :2]
y = dataset.target # y-Werte sind normalerweise im Unsupervised Learning nicht gegeben bzw

scores = []
s_scores = []

for n_cluster in range(2,8,1):
    max_iteration = 10_000

    kmeans = KMeans(n_clusters=n_cluster, max_iter=max_iteration, n_jobs=-1)
    kmeans.fit(x)
    y_pred = kmeans.predict(x)#.astype(int) # y_Pred als Integerwerte ausgeben, da sonst Probleme mit Farben
    s_scores.append(silhouette_score(x,y_pred)) # Bester Wert wäre 1. Schlechtester Wert wäre 0. NEgative Werte sagen aus dass zu falschem Cluster zugeordnet wurde
    scores.append(kmeans.score(x))


#plot(x, y, y_pred, kmeans.cluster_centers_, kmeans)

#Objective: [0, inf)  Der Wert 0 wäre der Beste Wert und der Schlechteste wäre unendlich
#Score: (-inf, 0] Score ist das negative Objective. Also wäre der Wert -unendlich am schlechtesten und 0 am bestem

print(f"Scores: {scores}") # Wert -36 wäre z.B besser als -37. Bester Wert wäre 0
print(f"Silhouette_score: {s_scores}")

# Abschlussnotiz: Je mehr Cluster desto besser der Score.
# Achtung: jedoch will man nicht unendliche Cluster haben.
# Beim Clustering will man noch nicht bekannte Informationen aus den Feature Daten gewinnen.
# z.B. Wie viele Cluster sind sinnvoll.
# Beispiel: Netflix Filmempfehlung: Welche User haben ähnliches Sehverhalten von Filmen.
# Jedoch sehen Horrorfans jedoch nicht nur Horrorfilme. Es sollen vorschläge anhand des Sehverhaltens änhlicher leute erstellt werden