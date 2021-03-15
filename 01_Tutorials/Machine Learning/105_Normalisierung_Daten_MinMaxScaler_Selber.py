# Standardisierungsfunktion selber Programmieren
# Imports
import numpy as np
import matplotlib.pyplot as plt

class MinMaxScaler:
    def __init__(self):
        self.max=[] #MaxListe
        self.min=[] #MinListe

    def fit(self ,x):
        self.max = np.max(x, axis=0)
        self.min = np.min(x, axis=0)

    def transform(self ,x):
        # Beispiel
        # x=10
        # min = 5, max = 15
        # (10-5)/(15-5)= 0.5
        x_tranform = (x - self.min) / (self.max - self.min)
        return x_tranform

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

# Skaliervorgang
scaler = MinMaxScaler()
scaler.fit(x_train) # Wichtig Fit nur auf Trainingsset ausführen !!!
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test) # Testset wird auch Transformiert, jedoch ohne in Fit eingeflossen zu sein

# Plot Rescaled Daten
plt.figure(2)
plt.scatter(x_test[:,0], x_test[:,1])
plt.show()

print(np.mean(x_test, axis=0))
print(np.std(x_test, axis=0))