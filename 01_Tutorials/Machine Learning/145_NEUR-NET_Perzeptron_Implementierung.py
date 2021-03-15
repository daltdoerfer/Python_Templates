'Bias Neuron (==Intercept bei linearer Regression) aus einfachheitsgründen nicht implementiert'

import random
random.seed(42)
import numpy as np
np.random.seed(42)

import pandas as od
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

def get_dataset():
    """"OR Dataset welchges die OR Logig beschreibt."""
    x = np.array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype=np.float32)
    y = np.array([0, 1, 1, 1], dtype=np.float32)
    return x, y

''' Formeln für das Perzeptron:
Aktivierungsfunktion:
    theta_s = {1, wenn s > 0
               0, sonst

Delta-Regel (Gewicht-Updat) -> Basiert auf dem Gradientenverfahren indem man versucht den Fehler über die Ableitung "delta_w_i" und Lambda zu minimieren
    delta_w_i = (y_i - y_hat_i)*x_i
    w_i = w_i + Lambda*delta_w_i
'''

#--------------Definition der Klassen---------------------------
class Perceptron():
    def __init__(self, epochs: int, learning_rate: float):
        self.epochs = epochs                    # Bei Neuronalen Netzwerken wird immer der Parameter "epochs" angebeben -> Wie oft will man über den Datensatz iterieren.
        self.learning_rate = learning_rate      # Lernerate enspricht Lambda (siehe Delta Regel). Gibt an wie Stark die Gewichte angepasst werden. Wie stark man in Richtung des Gradienten geht
        self.w: np.ndarray = None

    def fit(self, x, y):
        N, dim = x.shape
        # Init Model
        self.w = np.random.uniform(-1, 1, (dim, 1)) # Zufällige Initialisierung der Gewichte. Zufallsverteilung zwischen -1 bis 1 (normalerweise Nullzentriert). Ausgabe als Array mit Dimensionen x = dim; y = 1
        # Training
        error = 0.0
        for epoch in range(self.epochs): # Pro Iteration über Datensatz (Epoche) will ich einen Index Generieren und einen Datenpunkt aus dem Datensatz nehmen dazu die Prediction bestimmen. Wenn Prediction nicht mit Ergebnis übereinstimmt, wird Gewichtung angepasst
            choice = np.random.choice(N) # Index Generieren
            x_i = x[choice]
            y_i = y[choice]
            y_hat = self.predict(x_i) # Prediction y_hat für diesen Datenpunkt bestimmen

            # We made misclassification
            if y_hat != y_i: # Wenn Prediction ungleich unserem wahren Wert ist, dann werden Gewichte angepasst
                self._update_weights(x_i, y_i, y_hat)

    # Aktivierungsfunktion (wir in predict-Funktion aufgerufen)
    def _activation(self, signal):
        if signal > 0:
            return 1
        else:
            return 0

    # Update der Gewichtungen -> siehe Delta-Regel oben
    def _update_weights(self, x, y, y_hat):
        for i in range(self.w.shape[0]): # Für alle Weights in einem Schritt
            delta_w_i = self.learning_rate * (y - y_hat) * x[i] # Gradient aus wahrem Ergebnis zu Predict-Ergebnis
            self.w[i] = self.w[i] + delta_w_i

    def score(self, x, y):
        y_pred = np.array([self.predict(x_i) for x_i in x])
        n = y.shape[0]
        acc = np.sum([y_p == y_i for y_p, y_i in zip(y_pred, y) if y_p == y_i]) / n
        return acc

    def predict(self, x):
        y_pred = self._activation(np.dot(self.w.T, x)) # np.dot(self.w.T, x) ist äquivalent zu Berechnung der linearen Regression -> Diese Funktion geht nochmal durch Aktivierungsfunktion 1 oder 0
        return y_pred

#--------------Durchführung der Berechnung------------------------------
x,y = get_dataset()

p = Perceptron(epochs=10, learning_rate=0.5)
p.fit(x,y)
acc = p.score(x, y)

print(f"Acc: {acc}") # Score
print(f"W:\n {p.w}") # Weights