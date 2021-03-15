# https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html
# Standardabweichung wird in diesem vereinfachten Code Konstant auf 2 gesetzt. Man will nur den Mittelwert erlenen
# Wichtige Parameter des Gaussian mixture Models:
# n_components -> Wie viele Cluster will ich bilden
# covariance_type -> Wie soll covarianz berechnet werden (full ist der Komplizierteste)
# max_iter -> Wieviele Update-Schritte sollen ausgeführt werden
# Attributes:
# means_
# covariances_
# converge_ -> schauen ob Expectation/Maximazation Algorithmus konvergiert oder doch besser mehr Iterationen sinnvoll sind

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import multivariate_normal

np.random.seed(42)

n_points = 100


# Toy Dataset
def generate_dataset():
    data = np.concatenate((
        np.random.normal(1, 2, n_points), #Mittelwert = 1, std = 2
        np.random.normal(8, 2, n_points) #Mittelwert = 8, std = 2
        ))
    classes = [0 for i in range(n_points)] + [1 for i in range(n_points)]
    return data, classes


x, y = generate_dataset()

plt.scatter(x, [0 for i in range(2 * n_points)], c=y)
plt.show()


class GaussianMixtureModel:
    def __init__(self, n_cluster, max_iter=100): # n_cluster: wie viele Normalverteilungen wollen wir erlernen
        self.n_cluster = n_cluster
        self.max_iter = max_iter

    def prob(self, point, gaussian):
        prob = norm.pdf(point, gaussian[0], gaussian[1]) # Wahrscheinlichkeitsdichtefunktion
        return prob

    def fit(self, x):
        N = x.shape[0]
        # Init our model
        self.gaussians = [[] for _ in range(self.n_cluster)]
        self.cluster_probs = np.zeros((N, self.n_cluster))
        for c in range(self.n_cluster):
            mean = np.random.choice(x)
            std = 2.0
            prob = 1 / self.n_cluster
            self.gaussians[c] = [mean, std, prob]

        # Start training
        for _ in range(self.max_iter):
            # Step 1: Expectation - > Berechnung der Wahrscheinlichtkeiten für die einzelnen Datenpunkte
            for i, point in enumerate(x):
                for c in range(self.n_cluster): # Für jedes CLuster
                    #z.B: 3 Cluster
                    #i=0
                    #c0: 0.7, c1:0.2, c2:0.1 -> Wahrscheinlichkeite zu 70% zu Cluster usw.
                    self.cluster_probs[i][c] = self.gaussians[c][2] * self.prob(point, self.gaussians[c]) # Wie ist Wahrscheinlichkeit das Datenpunkt vom aktuellen Cluster erstellt wurde (prob-Methode), Hier werden die Wahrscheinlichkeiten jedes Datenpunktes für z.B. 3 Cluster aka c0,c1,c2 gespeicher
                self.cluster_probs[i] /= np.sum(self.cluster_probs[i]) # Normierung der Warhscheinlichkeiten

                # Step 2: Maximization
            for c in range(self.n_cluster):
                # Cluster mean
                # Bsp:
                # Datenpunkte:                2     ,3     ,1
                # Wahrscheinlichkeiten: c0:  0.5   0.6    0.2
                # Gewichtung in average:  2*0.5 + 3*0.6+1*0.2 = 3 -> Anschließend wird gemittelt 3/3 = 1
                self.gaussians[c][0] = np.average(x, weights=self.cluster_probs[:, c]) #
                # Cluster std
                self.gaussians[c][1] = 2.0 # Standardabweichung wird in diesem vereinfachten Code Konstant auf 2 gesetzt. Man will nur den Mittelwert erlenen
                # Cluster prob
                self.gaussians[c][2] = np.mean(self.cluster_probs[:, c])
        return self.gaussians


n_cluster = 2
max_iter = 200

gmm = GaussianMixtureModel(n_cluster=n_cluster, max_iter=max_iter)
gaussians = gmm.fit(x)
means = [gaussians[0][0], gaussians[1][0]]

print("True Mean 1: ", 1)
print("True Mean 2: ", 8)

print("Estimate Mean 1: ", means[0])
print("Estimate Mean 2: ", means[1])

#Bemekrung im Plot ist die Farbverteilung (auch wieder) Random
y1 = [norm.pdf(xi, 1, 2) for xi in np.arange(-5, 15, 0.01)]
plt.scatter(np.arange(-5, 15, 0.01), y1, color="lightblue")

y2 = [norm.pdf(xi, 8, 2) for xi in np.arange(-5, 15, 0.01)]
plt.scatter(np.arange(-5, 15, 0.01), y2, color="orange")
plt.title("True")
plt.show()

y1 = [norm.pdf(xi, means[0], 2) for xi in np.arange(-5, 15, 0.01)]
plt.scatter(np.arange(-5, 15, 0.01), y1, color="lightblue")

y2 = [norm.pdf(xi, means[1], 2) for xi in np.arange(-5, 15, 0.01)]
plt.scatter(np.arange(-5, 15, 0.01), y2, color="orange")
plt.title("Estimate")
plt.show()