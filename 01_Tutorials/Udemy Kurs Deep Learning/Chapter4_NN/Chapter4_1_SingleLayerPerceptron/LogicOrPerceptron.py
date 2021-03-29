import numpy as np
from typing import Tuple

def get_dataset() -> Tuple[np.ndarray, np.ndarray]:
    '''OR Dataset.'''
    x = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
    y = np.array([[0],[1],[1],[1]])
    return x, y

def accuracy_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    # https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score
    N = y_true.shape[0] # Anzahl Datenpunkte
    accuracy = np.sum(y_true == y_pred) /N # Vergleicht die Beiden Listen y_True mit y_pred und ergibt
    return accuracy

def step_function(input_signal: np.ndarray) -> np.ndarray:

    output_signal = (input_signal > 0.0).astype(np.int_) # Umwandlung von Bool in Integer wenn > 0
    return output_signal



class Perceptron:
    def __init__(self, learning_rate: float, input_dim: int) -> None:
        self.learning_rate = learning_rate
        self.input_dim = input_dim
        self.w = np.random.uniform(-1, 1, size=(self.input_dim, 1)) # Initialisierung der Gewichte gemäß Gleichverteilung im Bereich -1 bis 1

    def _update_weights(self, x: np.ndarray, y: np.ndarray, y_pred: np.ndarray) -> None:

        error = (y - y_pred) # Vektorsubtraktion
        delta = error * x
        for delta_i in delta:
            self.w = self.w + self.learning_rate * delta_i.reshape(-1, 1) # Reshape zwingt w in ein Format (X, 1)

    def train(self, x: np.ndarray, y: np.ndarray, epochs: int = 1):
        for epoch in range(1, epochs + 1): # Über Alle Epochen iterieren
            y_pred = self.predict(x) # Prediction
            self._update_weights(x, y, y_pred)
            accuracy = accuracy_score(y, y_pred)
            print(f"Epoch: {epoch} Accuracy: {accuracy} \n with Values w: {self.w}")

    def predict(self, x: np.ndarray) -> np.ndarray:
        input_signal = np.dot(x, self.w) # Eingangslayer Perzeptron: -> Matrixmultiplikation x mit Weights
        output_signal = step_function(input_signal) # Ausgangslayer Perzepton
        return output_signal

    def evaluate(self, x: np.ndarray, y: np.ndarray): # Metrik
        return accuracy_score()


if __name__ == "__main__":
    x, y = get_dataset()

    input_dim = x.shape[1] # Anzahl an Features, [0] Wäre die Anzhal an samples
    learning_rate = 0.5

    p = Perceptron(learning_rate, input_dim)
    p.train(x, y, epochs = 10)
