# Diese Datei beschäftigt sich mit dem Nachbau der Funktionen in Tensorflow: ONEHOT aka To-Categorical, Softmax Funktion und Cross Entroppy
# https://www.udemy.com/course/deep-learning-grundlagen-neuronale-netzwerke-mit-tensorflow/learn/lecture/11768720#overview und folgende
#
# To-Categorical (Tensforflow) oder ONEHOT sind Synonyme.
import numpy as np
from typing import Tuple

def get_dataset() -> Tuple[np.ndarray, np.ndarray]:
    '''OR Dataset.'''
    x = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
    y = np.array([[0],[1],[1],[1]])
    return x, y

# Kageorisierung bzw. ONEHOT Vektor zu Datensatz bestimmen
def to_categorical(y: np.ndarray, num_classes: int) -> np.ndarray:
    y_categorical = np.zeros(shape=(len(y), num_classes))
    for i, yi in enumerate(y):
        y_categorical[i, yi] = 1 # yi ist immer Wert aus y-Array
    return y_categorical

# Softmax Formel für Wahrscheinlichkeit berechnen
def softmax(y_pred: np.ndarray) -> np.ndarray:
    probabilities = np.zeros_like(y_pred) # Zeros like -> Macht Zeros in entsprechendem Format wie y_pred ist
    for i in range(len(y_pred)): # Für jeden Eintrag des Eingehenden Vektors
        exps = np.exp(y_pred[i])
        probabilities[i] = exps / np.sum(exps)
    return probabilities

# Vergleich Wahrscheinlichkeitsverteilungen wie ähnlich diese sind. Fehlerwert wird kleiner je ähnlicher sich diese sind
def cross_entropy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    num_samples = y_true.shape[0]
    loss = -np.sum(y_true* np.log(y_pred)) / num_samples
    return loss

if __name__ == "__main__":
    x, y = get_dataset() # Datensatz erzeugen
    #print(y.shape)
    print(y)

    # ONEHOT Vektor erzeugen
    y_true = to_categorical(y, num_classes=2)
    #print(y_true.shape)
    print(y_true)

    # Ausgedachte Werte
    y_logits = np.array([[10.8, -3.3], [12.2, 11.8], [1.1, -4.0], [7.05, 3.95]]) # Rohe Werte vor Umformung in Wahrscheinlichkeit

    # Wahrscheinlicheiten berechnen
    y_pred = softmax(y_logits)
    #print(y_prob.shape)
    print(y_pred)

    loss = cross_entropy(y_true, y_pred)
    print(loss)