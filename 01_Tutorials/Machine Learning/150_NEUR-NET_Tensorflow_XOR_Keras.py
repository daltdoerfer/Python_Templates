import numpy as np

from tensorflow.keras.models import *
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import *
from tensorflow.keras.losses import *
from tensorflow.keras.utils import *

# XOR Dataset: A ^ BaseException
# A, B sind binäre Werte
# XOR(A, B) = A^B
def XOR(A, B):
	if (A == 1 and B == 0) or (A == 0 and B == 1):
		return 1
	else: 
		return 0

# Datenpunkte zur Logik
x = np.array([[0, 0],[0 ,1],[1, 0],[1, 1]])
y = np.array([[0],[1],[1],[0]])

model = Sequential() # Sequenzielles Modell

# Erstellen und Verbinden der NN-Layer
# Input Layer hat 2 Eingänge: A oder B -> input_dim = x.shape[1]
# Input to first Hidden Layer
model.add(Dense(8, input_dim = x.shape[1]))# Input Layer wird erstellt und verbunden mit Hidden Layer: 2x8 Weights an 8 Biases
model.add(Activation("tanh")) # Hinzufügen der Aktivierungsfunktion als Tangenshyperbolicus -> Wertebereich von [-1, +1] Achtung Nichtlinear

# Hidden to Hidden Layer (Anzahl der Hidden Layer zur Optimierung erhöhen)
model.add(Dense(4))
model.add(Activation("tanh")) # Hinzufügen der Aktivierungsfunktion als Tangenshyperbolicus -> Wertebereich von [-1, +1] Achtung Nichtlinear

# Output Layer
model.add(Dense(y.shape[1])) # Ausgang Deklarieren
model.add(Activation("sigmoid")) # Mapped auf das (Grenz-)Intervall (0 , 1) sprich 0 und 1 sind als Grenzwert nicht enthalten. Beispiel 0,75 -> zu 75% Wahrscheinlichkeit Wert 1
model.summary()


# Model Training
sgd = SGD(lr=0.1) # Optimizer (lr -> Lernrate: Mit werden rumspielen(lr zu hoch -> man schießt direkt über das Optimim hinaus; lr zu klein -> es passiert einfach nichts)
model.compile(loss="binary_crossentropy", optimizer=sgd, metrics=["accuracy"]) # Optimizer arbeitet mit loss-Funktion. Mithilfe der Fehlerfunktion berechnet der Optimizer die Gradienten in die Richtung in die die Fehler kleienr werden -> Gradientenabstieg
model.fit(x, y, epochs=200) # Training des Neurnalen Netzwerkes -> eigentlich auch aufteilen zwischen Trainings und Testset

# Predictions ausgeben
#y_pred = model.predict(x) # Ursprüngliche Funktion gibt Werte zwischen 0 und 1 aus. Wir wollen aber wissen ob True oder nicht
y_pred = model.predict(x > 0.5) # Numpy ausdruck -> TRUE wenn > 0.5 sonst FALSE
print(y_pred)