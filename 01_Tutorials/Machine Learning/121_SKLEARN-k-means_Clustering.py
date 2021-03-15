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
from sklearn.cluster import KMeans

# Dataset for Classification
np.random.seed(42)
dataset = load_iris()
x = dataset.data[:, :2]
y = dataset.target # y-Werte sind normalerweise im Unsupervised Learning nicht gegeben bzw


kmeans = KMeans(n_clusters=3, max_iter=1_000)

kmeans.fit(x)
y_pred = kmeans.predict(x).astype(int) # y_Pred als Integerwerte ausgeben, da sonst Probleme mit Farben

print(kmeans.cluster_centers_)
print(y_pred)

plot(x, y, y_pred, kmeans.cluster_centers_, kmeans)

#Objective: [0, inf)  Der Wert 0 wäre der Beste Wert und der Schlechteste wäre unendlich
#Score: (-inf, 0] Score ist das negative Objective. Also wäre der Wert -unendlich am schlechtesten und 0 am bestem

score = kmeans.score(x, y)

print(f"Score: {score}") # Wert -36 wäre z.B besser als -37. Bester Wert wäre 0

# Abschlussnotiz: Je mehr Cluster desto besser der Score.
# Achtung: jedoch will man nicht unendliche Cluster haben.
# Beim Clustering will man noch nicht bekannte Informationen aus den Feature Daten gewinnen.
# z.B. Wie viele Cluster sind sinnvoll.
# Beispiel: Netflix Filmempfehlung: Welche User haben ähnliches Sehverhalten von Filmen.
# Jedoch sehen Horrorfans jedoch nicht nur Horrorfilme. Es sollen vorschläge anhand des Sehverhaltens änhlicher leute erstellt werden