# Standardisierungsfunktion selber Programmieren
# Imports
import numpy as np
import matplotlib.pyplot as plt

class StandardScaler:
    def __init__(self):
        self.mean = [] #Liste
        self.std = [] #Liste

    def fit(self ,x):
        self.mean = np.mean(x, axis=0) # Mittelwert von jedem Feature abspeichern
        self.std = np.std(x, axis=0)

    def transform(self ,x):
        x_transform = (x - self.mean) / self.std
        return x_transform

from sklearn import datasets
from sklearn.model_selection import train_test_split

boston = datasets.load_boston()
x, y = boston.data[:, 1:3], boston.target

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.3)

# Plot Original Daten
plt.scatter(x_test[:, 0], x_test[:, 1])
#plt.show()

print(np.mean(x_test, axis=0))
print(np.std(x_test, axis=0))


# StandardRescaling
scaler = StandardScaler()
scaler.fit(x_train) # Wichtig Fit nur auf Trainingsset ausführen !!!
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test) # Testset wird auch Transformiert, jedoch ohne in Fit eingeflossen zu sein


# Plot Rescaled Daten
plt.figure(2)
plt.scatter(x_test[:,0], x_test[:,1])
plt.show()

print(np.mean(x_test, axis=0))
print(np.std(x_test, axis=0))