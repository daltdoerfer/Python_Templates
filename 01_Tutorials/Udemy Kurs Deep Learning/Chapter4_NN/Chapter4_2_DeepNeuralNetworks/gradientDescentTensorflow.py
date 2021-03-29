# Hier Soll die Rosenbrock Funktion (Gradient Descent) über Tensorflow gelöst werden. Ziel: Lokales Minima finden

import tensorflow as tf

from helper import plot_rosenbrock


class Model:
    def __init__(self):

        # tf.Variable() sagen wir Tensorflow, dass beim internen Gradient Descent Verfahren im Training angepasst werden darf.
        # Alles innerhalb der Klammer ist die Initialisierung
        self.x = tf.Variable(tf.random.uniform(minval=-2.0, maxval=2.0, shape=[2]))  #shape=[2] -> Zwei Koordinaten bei Rosenbrock Funktion x = [x0, x1]
        self.learning_rate = 0.001 # Erster Wert  0.0005
        self.optimizer = tf.optimizers.SGD(learning_rate=self.learning_rate) # Tensorflow Berechnet mit dem Optimizer  die Ableitung selber. SGD -> Stochastic Gradient Descent

        # Current_loss wird als Workaround verwendet um die Loss Funktion im späteren Zwischenschritt aufrufen zu können
        self.current_loss_val = self.loss()

    # Unsere abzuleitende Funktion (Rosenbrock Funktion) -> Loss Funktion im NN Jargon
    def loss(self): # Funktion die Mininmiert werden soll. Hier ist das die Rosenbrock Funktion
        self.current_loss_val = 100 * (self.x[0] ** 2 - self.x[1]) ** 2 + (self.x[0] - 1) ** 2 # Die einzelnen Variablen müssen in Vektorform umgeschrieben werden x0 -> x[0] usw.
        return self.current_loss_val

    def fit(self):
        self.optimizer.minimize(self.loss, self.x)  # Man übergibt dem Optimizer in folgender Reihenfolge: 1. loss-Funktiuon; 2. variable die wir anpassen wollen)


model = Model()
gradient_steps = []
x_start = model.x.numpy() # Vor erstem Fit aufruf mit Startwerten berechnet. Das interne x als Numpy Array abspeichern
num_iterations = 5000

for it in range(num_iterations):
    model.fit()

    #Alle 100 Iterationen
    if it % 100 == 0:
        x = model.x.numpy() # Aktuelle Koordinaten: x = [x0, x1] im Numpy Array ausgeben
        y = model.current_loss_val.numpy() # Aktuelle Koordinaten: y im Numpy Array ausgeben
        print("X = ", x, " Y = ", y)
        gradient_steps.append(x)

plot_rosenbrock(x_start=x_start, gradient_steps=gradient_steps)
