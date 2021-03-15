# https://en.wikipedia.org/wiki/MNIST_database

import numpy as np

from tensorflow.keras.models import *
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import *
from tensorflow.keras.losses import *
from tensorflow.keras.utils import *

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

dataset = load_digits()
x = dataset.data
y = dataset.target
print(x.shape)
print(y.shape)
print(x[0])
print(y[0])

y = to_categorical(y, num_classes = 10) # der y-Wert kann als Zahl so nicht verwendet werden. Es muss eine Kategorisierung durchgeführt werden (in diesem Fall 10 Klassen weil 10 Zahlen im Dataset dargestellt werden
print(y) # Der Kategorisierte Wert ist eine Matrix. Jede Zeile beschreibt das auftreten der jeweiligen Zahl.

x_train, x_test, y_train, y_test = train_test_split(x,y)

model = Sequential()
model.add(Dense(512, input_dim=x.shape[1])) # Input Layer(64 Neuronen) to first Hidden Layer (512 Neurons). WICHTIG: Erster Hidden Layer braucht immer Verbindung zu Input Layer -> input_dim.
model.add(Activation("relu"))
model.add(Dense(256))
model.add(Activation("relu"))
model.add(Dense(y.shape[1])) # Last Hidden Layer (256 Neurons) to Output Layer (10Neurons, da 10 Zahlen aus dem Datatset dargestellt werden könnnen)
model.add(Activation("softmax")) # Softmax-Layer wird verwendet wenn Klassifikationsproblem vorliegt mit mehr als 2 Klassen (Ausgabe von Wahrscheinlichkeitswerten für jede mögliche Klasse -> Die höchste gewinnt)

# Model Training
sdg = SGD(lr=0.001) # Optimizer (lr -> Lernrate: Mit werden rumspielen(lr zu hoch -> man schießt direkt über das Optimim hinaus; lr zu klein -> es passiert einfach nichts)
model.compile(loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"]) # Optimizer (sgd stochastic Gradient Descent) arbeitet mit loss-Funktion. Mithilfe der Fehlerfunktion berechnet der Optimizer die Gradienten in die Richtung in die die Fehler kleiner werden -> Gradientenabstieg
model.fit(x=x_train, y=y_train, epochs=15, validation_data=(x_test, y_test)) # WICHTIG: Normalerweise müsste für die Validation das Trainingsset nochmal in ein Train_set und validation_set geteilt werden (darauf wird hier verzichtet)