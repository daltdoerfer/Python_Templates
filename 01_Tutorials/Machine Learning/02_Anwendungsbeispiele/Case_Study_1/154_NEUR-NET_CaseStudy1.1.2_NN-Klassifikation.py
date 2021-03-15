import numpy as np

from tensorflow.keras.models import *
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import *
from tensorflow.keras.losses import *
from tensorflow.keras.utils import *

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.utils.multiclass import type_of_target

#############################################################
# ---- Load MNIST Dataset: Zahlen 0-9 in 8x8 Farbmustern  ---
# https://en.wikipedia.org/wiki/MNIST_database
#############################################################
dataset = load_digits()
x = dataset.data
y = dataset.target
print(x.shape)
print(y.shape)
print(x[0])
print(y[0])

#############################################################
# ------ Vorkategorisierung -------
#############################################################
y = to_categorical(y, num_classes = 10) # der y-Wert kann als Zahl so nicht verwendet werden. Es muss eine Kategorisierung durchgeführt werden (in diesem Fall 10 Klassen weil 10 Zahlen im Dataset dargestellt werden
print(y) # Der Kategorisierte Wert ist eine Matrix. Jede Zeile beschreibt das auftreten der jeweiligen Zahl.

#############################################################
# Splitting der Daten in Trainings-,Test-, und Validationset
#############################################################
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25) # Bsp: 0.3 => Test: 30% + Train: 70%. (Default=None=0.25)
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.25) # Nochmal 25% der Trainingspunkte gehen ins Validation set

''' Normalisierung macht zumindest in diesem Beispiel das Ergebnis schlechter
#############################################################
# ----------- Normalisieren des Datasets --------------------
# Siehe Lektionen: 104, 105, 106
# Übungen: PÜ_4
#############################################################
scaler = StandardScaler() # StandardScaler bei Normalverteilung der Daten besser als andere Scaler
scaler.fit(x)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
'''

#############################################################
#----- Neuronales Netzwerk Klassifikation (Tensorflow)-------
# Siehe Lektionen: 151, 92 (Metriken)
# Anleitung:
# Anfangslayer + Verscheidene Layer mit Neuronen-Anzahl aufspannen + Activation Function
# Modell Trainieren mit verschiedenen Lernraten (lr -> Achtung teils sehr sensibel)
# Verschiedene model.compile Parameter testen (loss; optimizer; metrics)
# https://www.tensorflow.org/api_docs/python/tf/keras/Model
#############################################################

model = Sequential()
model.add(Dense(512, input_dim=x.shape[1])) # Input Layer(64 Neuronen) to first Hidden Layer (512 Neurons). WICHTIG: Erster Hidden Layer braucht immer Verbindung zu Input Layer -> input_dim.
model.add(Activation("relu"))
model.add(Dense(256))
model.add(Activation("relu"))
model.add(Dense(y.shape[1])) # Last Hidden Layer (256 Neurons) to Output Layer (10Neurons, da 10 Zahlen aus dem Datatset dargestellt werden könnnen)
model.add(Activation("softmax")) # Softmax wird verwendet wenn Klassifikationsproblem vorliegt mit mehr als 2 Klassen (Ausgabe von Wahrscheinlichkeitswerten für jede mögliche Klasse -> Die höchste gewinnt)

# Model Training
sdg = SGD(lr=0.001) # Optimizer (lr -> Lernrate: Mit werden rumspielen(lr zu hoch -> man schießt direkt über das Optimim hinaus; lr zu klein -> es passiert einfach nichts)
model.compile(loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"]) # Optimizer (sgd stochastic Gradient Descent) arbeitet mit loss-Funktion. Mithilfe der Fehlerfunktion berechnet der Optimizer die Gradienten in die Richtung in die die Fehler kleiner werden -> Gradientenabstieg
model.fit(x=x_train, y=y_train, epochs=15, validation_data=(x_val, y_val)) # WICHTIG: Normalerweise wird für die Validierung das Trainingsset nochmal in ein Train_set und validation_set geteilt



#############################################################
# Finale Auswertung:
# Kommentar:
#############################################################

# Ausführen des gelernten Modells auf Testset
# (Rückgabewert ist eine Wahrscheinlichkeitstabelle, welche Ausgibt,
# wie Wahrscheinlich welches Ergebnis der jeweiligen Klasse eintritt
y_pred = model.predict(x_test, batch_size=None, verbose=0, steps=None,
                       callbacks=None, max_queue_size=10,
                       workers=1, use_multiprocessing=False)

print(type_of_target(y_test))
print(type_of_target(y_pred))

''' confusion_matrix und accuracy Score kann aufgrund verschiedener ausgabetypen nicht berechnet werden
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)

print(f"Accuracy: {acc}")
print(f"Confusion matrix:\n{cm}")
'''