# https://www.udemy.com/course/deep-learning-grundlagen-neuronale-netzwerke-mit-tensorflow/learn/lecture/11780118#overview

from typing import List
from typing import Tuple

import tensorflow as tf
import numpy as np

def get_dataset() -> Tuple[np.ndarray, np.ndarray]:
    ''' XOR Dataset. '''
    x = np.array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype=np.float32)
    y = np.array([[0], [1], [1], [0]], dtype=np.float32)
    return x, y

def dense(W: tf.Variable, b: tf.Variable, x: tf.Tensor) -> tf.Tensor:  # W = Weights , b = bias, x = Input für Layer

    # tf.linalg.matmul(x, W) -> Matrixmultiplikation von x-Datenpunkt mit Gewichten W.
    # W ist eine (n x m) Matrix mit n: Anz. Features; m: Anz Neuronen
    # x ist ein (1 x n) Vektor
    # ist ein (1 x m) Vektor
    # Output = W*x+b
    return tf.math.add(tf.linalg.matmul(x, W), b)  # dazu addieren wir noch das Bias-Neuron b . matmul -> Matrix Multiplikation


class Model:
    def __init__(self, optimizer, loss, metric, units_list) -> None:

        # Model Parameters
        self.optimizer = optimizer
        self.loss = loss
        self.metric = metric
        self.units_list = units_list

        # Weights (Wichtig für interne Bezeichnung (name=) muss Name eindeutig sein und darf nicht doppelt Vorkommen)
        W1_shape = [self.units_list[0], self.units_list[1]]  # Matrix W1 soll vom Input Layer zum Hidden Layer gehen
        self.W1 = tf.Variable(tf.random.truncated_normal(shape=W1_shape, stddev=0.1), name="W1")  # Variable deklarieren für Weights mit Normalverteilung mit Standardabweichung (stddev)und interner Bezeichnung W1

        W2_shape = [self.units_list[1], self.units_list[2]]  # Matrix W1 soll vom Hidden Layer zum Output Layer gehen
        self.W2 = tf.Variable(tf.random.truncated_normal(shape=W2_shape, stddev=0.1), name="W2") # Variable deklarieren für Weights mit Normalverteilung mit Standardabweichung (stddev)und interner Bezeichnung W2
        # Biases
        b1_shape = [self.units_list[1]]  # Erstes Bias neuron wird auf jeden Neuron im Hidden Layer draufaddiert
        self.b1 = tf.Variable(tf.constant(0.0, shape=b1_shape), name="b1")  # 0.0 Initialwert mit Name "b1" .

        b2_shape = [self.units_list[2]]  # Zweites Bias neuron wird auf jeden Neuron im Output Layer draufaddiert
        self.b2 = tf.Variable(tf.constant(0.0, shape=b2_shape), name="b2")

        # Trainable Parameters
        self.variables = [self.W1, self.W2, self.b1, self.b2]

    def _update_weights(self, x: np.ndarray, y: np.ndarray) -> tf.Tensor:
        with tf.GradientTape() as tape:  # Ich erstelle in einem Kontext eine Variable tape von GradientTape Klassee
            y_pred = self.predict(x)  # Von was sollen die Gradienten berechnet werden
            loss_value = self.loss(y, y_pred)  # -> Gradienten werden basierend auf Fehlerwert berechnet

        gradients = tape.gradient(loss_value, self.variables)  # gradient(target, sources) ->Target: Loss-Wert UND Sources: alle Trainierbaren gewichte -> [self.W1, self.W2, self.b1, self.b2]
        self.optimizer.apply_gradients(zip(gradients, self.variables))  # Gradienten Anwenden
        return loss_value


    def fit(self, x: np.ndarray, y: np.ndarray, epochs: int = 1) -> None: # Früher Train
        for epoch in range(1, epochs + 1):  # Über Alle Epochen iterieren
            # Loss Value
            loss_value = self._update_weights(x, y).numpy()  # x,y entsprechen hierbei x_train und y-Train. WICHTIG: Muss Als Numpy Tensor vorliegen um aus C++ Backend wieder ein numpy Array zu erhalten
            # Metric value
            y_pred = self.predict(x)  # Prediction berechnen
            self.metric.reset_states()  # für jede Epoche soll die Metric der letzten Epoche resettet werden
            self.metric.update_state(y, y_pred)  # -> Metrik neu Berechnen
            metric_value = self.metric.result().numpy()  # Wert als Numpy Float bekommen
            print(f"Epoch: {epoch} - Loss: {loss_value} - Metric: {metric_value}")

    def predict(self, x: np.ndarray) -> tf.Tensor:
        # Info: Output des Letzten Layers geht als Input in den nächsten rein
        input_layer = x
        hidden_layer = dense(self.W1, self.b1, input_layer)  # Dense Layer: Hidden Layer mit Input Layer Verbinden -> Siehe dense Funktion oben
        hidden_layer_activation = tf.nn.tanh(hidden_layer)  # Aktivierungsfunktion im Hidden Layer (Vordefiniert im unterpaket NN von Tensorflow
        output_layer = dense(self.W2, self.b2, hidden_layer_activation)
        output_layer_activation = tf.nn.sigmoid(output_layer)  # Finale Aktivierungsfunktion
        return output_layer_activation

    def evaluate(self, x: np.ndarray, y: np.ndarray) -> List[float]: # Metrik (Genauigkeitswert) und Fehlerwert berechnen

        y_pred = self.predict(x) # Prediction berechnen

        #Loss Value
        loss_value = self.loss(y, y_pred).numpy

        # Metric value
        self.metric.reset_states()  # für jede Epoche soll die Metric der letzten Epoche resettet werden
        self.metric.update_state(y, y_pred)  # -> Metrik neu Berechnen
        metric_value = self.metric.result().numpy()  # Wert als Numpy Float bekommen
        return[loss_value, metric_value]


if __name__ == "__main__":
    x, y = get_dataset()

    num_features = 2  # Input Dimension
    num_targets = 1  # Output Dimension
    units_list = [num_features, 6, num_targets]  # Wieviele Neuronen haben wir im [Input-Layer, Hidden-Layer, Output-Layer]

    learning_rate = 0.5
    optimizer = tf.optimizers.Adam(learning_rate=learning_rate)  # Beispiel Adam Optimizer
    loss = tf.keras.losses.MeanSquaredError()  # Fehlerfunktion
    metric = tf.keras.metrics.BinaryAccuracy()  # Metric (Optional) -> Genauigkeit

    model = Model(optimizer, loss, metric, units_list)
    model.fit(x, y, epochs=100)
