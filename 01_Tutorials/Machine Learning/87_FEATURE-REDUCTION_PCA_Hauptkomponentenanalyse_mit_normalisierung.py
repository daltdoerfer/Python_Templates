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

n_components = 3 # Herunterbrechen der Infomation auf 3 Dimensionen (Features)
pca = PCA(n_components=n_components, copy=True) # copy=True sagt ob Eingangsdatensatz x überschrieben wird oder nicht
pca.fit(x)

transformed_x = pca.transform(x)

# PCA Variables and Data

print("Components:\n", pca.components_)
print(pca.components_.shape) # Hauptkomponentend die wir behalten haben. Aangezeigt werden die Eigenvektoren des Optimierungsproblems mit den höchsten Werten
print("Explained Variance ", pca.explained_variance_) # Zugehörigen Eigenwerte zu den obigen Eigenvektoren. Anzahl Eigenwerte entpsricht der Anzahl der Wunschdimensionen -> sprich n_components. Die Höhe der Eigenwerte sagen etwas über die übriggebliebene Varianz aus. Remember: Varianz sollte so hoch wie möglich sein.
print("Explained Variance Ratio", pca.explained_variance_ratio_) # Diese Werte beschreiben wieviel welcher Eigenwert an Informationsgehalt des übrig gebliebenene Datensatzes behält. Der erste Eigenwert pca.explained_variance beschreibt den Informationsgehalt in Prozent
print("Sum of Explained Variance Ratio", sum(pca.explained_variance_ratio_)) # Dieser Wert gibt den gesamtprozensatz an, wieviel Informationen mit den übrig gebliebenene Dimensionen beschrieben werden.

# Plot the new 2-D Data
colors = ["red", "blue"]
for index, point in enumerate(transformed_x):
    plt.scatter(point[0], point[1], color=colors[y[index]])
plt.show()