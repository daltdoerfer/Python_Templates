# https://www.tensorflow.org/api_docs/python/tf/keras
# https://www.udemy.com/course/deep-learning-grundlagen-neuronale-netzwerke-mit-tensorflow/learn/lecture/12664672#overview
# https://www.udemy.com/course/deep-learning-grundlagen-neuronale-netzwerke-mit-tensorflow/learn/lecture/23253820#overview

import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import boston_housing
from tensorflow.keras.initializers import Constant
from tensorflow.keras.initializers import RandomUniform
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

# Metric R² implementieren, da nicht in TF vorhanden.
def r_squared(y_true: tf.Tensor, y_pred: tf.Tensor) -> tf.Tensor:

    #Berechnung der R²-Formel in einzelschritten
    error = tf.math.subtract(y_true, y_pred)
    squared_error = tf.math.square(error)
    numerator = tf.math.reduce_sum(squared_error) # Zähler
    y_true_mean = tf.math.reduce_mean(y_true)
    mean_deviation = tf.math.subtract(y_true, y_true_mean)
    squared_mean_deviation = tf.math.square(mean_deviation)
    denominator = tf.reduce_sum(squared_mean_deviation) # Nenner
    r2 = tf.math.subtract(1.0, tf.math.divide(numerator, denominator))
    r2_clipped = tf.clip_by_value(r2, clip_value_min=0.0, clip_value_max=1.0) # Negative Werte werden abgeschnitten
    return r2_clipped

# Model mit bestimmter Anzahl an Layern erzeugen -> Returned wird das Sequential Objekt
def build_model(num_features: int, num_targets: int) -> Sequential:  # Inpput: num_features ; Output num_targets
    init_w = RandomUniform(minval=-1.0, maxval=1.0) # Startwert für Gewicht deklarieeren. Zufallsverteilung zwischen -1 und  1
    init_b = Constant(value=0.0) # Initialisierung bias Neuronen. INFO: Per Default werden bias Neuronen immer mit 0 in keras initialisiert

    # Der Output des ersten Layers ist der Input des folgenden Layers
    model = Sequential() # Objekt der Sequential Klasse erstellen
    # Beim ersten Layer MUSS Input Shape deklariert werden
    model.add(Dense(units=16, kernel_initializer=init_w, bias_initializer=init_b, input_shape=(num_features,))) # Layer hinzufügen -> Erinnerung  Dense Layer: Hidden Layer mit Input Layer Verbinden. Units -> Wieviele Neuronen hat der Hidden Layer, input_shape -> Shape der Eingangsfeatures
    model.add(Activation("relu")) # Aktivierungsfunktion verknüpfen
    model.add(Dense(units=num_targets, kernel_initializer=init_w, bias_initializer=init_b)) # Output Layer verknüppfen
    model.summary() # Ausgabe der Struktur des Netzwerkes. Erinnerung Activation Funktionen haben 0 Parameter. Die Anzahl der Parameter ergibt sich aus (Anz Input* Anz Neuronen)+ Anz Bias Einträge

    return model

if __name__ == "__main__":

    # Test Train Split
    (x_train, y_train), (x_test, y_test) = boston_housing.load_data() # Lädt Datensatz aus Inet herunter

    # Umformatierung der Datentypen nach Float32
    x_train = x_train.astype(np.float32)
    y_train = y_train.astype(np.float32)
    y_train = np.reshape(y_train, newshape=(-1, 1)) # Zwingt das Format in eine Spalte  -> Keras erwartet Shape.(X, 1)

    x_test = x_test.astype(np.float32)
    y_test = y_test.astype(np.float32)
    y_test = np.reshape(y_test, newshape=(-1, 1)) # Zwingt das Format in eine Spalte  -> Keras erwartet Shape.(X, 1)

    print(f"x_train shape: {x_train.shape}")
    print(f"y_train shape: {y_train.shape}")
    print(f"x_test shape: {x_test.shape}")
    print(f"y_test shape: {y_test.shape}")

    num_features = x_train.shape[1]
    num_targets = y_train.shape[1]


    # Schritt 1:  Modell erstellen
    model = build_model(num_features, num_targets)

    # Schritt 2: Das Modell muss kompiliert werden. Hier werden die Gewichte initialisiert. Besteht aus Fehlerfunktion, Optimizer und einer Metric
    model.compile(
        loss="mse", # Mean-Squared-Error. Übergabe als String (nur wenn in TF existent. Dabei werden immer Defaultwert genommen) oder alternativ als Funktionsaufruf: tf.keras.losses.MeanSquaredError
        optimizer="Adam", # Übergabe als String (nur wenn in TF existent. Dabei werden immer Defaultwert genommen) oder alternativ als Funktionsaufruf:  tf.keras.optimizers.Adam
        metrics=[r_squared] # (OPTIONAL) Wichtig: nicht die Funktion aufrufen, sondern das Funktionsobjekt übergben. Wichtig TF erwartet hier immer eine Liste
    )

    # Schritt 3: Training ausführen
    model.fit(
        x=x_train,
        y=y_train,
        epochs=5_000,                    # (OPTIONAL) Wieviele Epochen sollen trainiert werden. Default = 11
        batch_size=128,                  # (OPTIONAL) Number of samples per batch of computation. If unspecified, batch_size will default to 32. Do not specify the batch_size if your data is in the form of a dataset, generators, or keras.utils.Sequence instances (since they generate batches)
        verbose=1,                       # (OPTIONAL) Wenn Verbose =1, dann wird der Output jede Epoche ausgegeben
        validation_data=(x_test, y_test) # (OPTIONAL) Validation Daten
    )

    # Schritt 4 Testing (Optional). Die Evaluate Funktion returned einen Losswert und einen Metric-Wert
    scores = model.evaluate(
        x=x_test,
        y=y_test,
        verbose=0      # (OPTIONAL) Wenn Verbose =1, dann wird der Output ausgegeben
    )
    print(scores)
