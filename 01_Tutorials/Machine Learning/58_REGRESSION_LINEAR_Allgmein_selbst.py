import pandas as pd #(Pandas ist so etwas wie excel in Pyhton)
from sklearn.datasets import load_boston
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg

'''
###############################################################
 Load Dataset
 ##############################################################
'''

dataset = load_boston()

#print(dataset)
x = dataset.data
y = dataset.target

df = pd.DataFrame(dataset.data, columns = dataset.feature_names)
print(df.head)

'''
###############################################################
 Split Data in Train and Testset
###############################################################
'''
np.random.seed(42) # Spezifische Random Verteilung bei Permutation

#x = dataset.data[:, 6]# Alle Zeilen jedoch nur Feature von  1.Spalte (Alter)
x = dataset.data  # Alle Zeilen
y = dataset.target # 1-D Vektor

num_samples = len(x) # Oder: x.shape(0)
indizes = np.random.permutation(len(x))
test_size = 100

# Diese Daten gehen ins Trainingsset
x_train = x[indizes[:-test_size]] # Nimmt alle  Werte die den vertauschten Indizes hinterlegt sind. Alle bis auf die letzen 100 [:-100]
y_train = y[indizes[:-test_size]]

print(x_train.shape)
print(x_train)

# Diese Daten gehen ins Testset
x_test = x[indizes[-test_size:]] # Nimmt alle  Werte die den vertauschten Indizes hinterlegt sind. Alle bis auf die letzen 100 [:-100]
y_test = y[indizes[-test_size:]]

'''
###############################################################
Berechnung der mehrdimensionalen Linearen Regression
Formeln
beta = (X_Transp * X)^(-1) *X_Trans * y
y_dach= X * beta
###############################################################
'''

class LinearRegression:
    def __init__(self, use_intercept=True):
        self.beta = None
        self.use_intercept = use_intercept

    def add_intercept(self, x):
        intercepts = np.ones(x.shape[0]) # Erstellt X 1er Eintäge wobei X die Anzahl der Zeilen unseres Datensets ist
        x = np.column_stack((intercepts, x)) # Nimmt Vektor "intercepts" und fügt den Vektor "X" in Weiterer Spalte hinzu
        return x

    def fit(self, x, y): # Wird nur im Training verwendet
        if self.use_intercept == True:
            x = self.add_intercept(x) #Self, da Klassenmethode

        # Compute the closed Form bzw. inner Form. Bemerkung: Bei großen Datensätzen mit vielen Features dauert die Berechnung eventuell ewig daher wird alterniv ein iterativer Optimierer angestrebt anstatt die optimal Berechnung hier
        inner = np.dot(x.T, x) # Matrixprodukt (skalar) aus x_Transponiert und x
        inv = numpy.linalg.inv(inner) # Erzeugt die Inverse von X
        self.beta = np.dot(np.dot(inv, x.T), y)

    def predict(self, x):  # Wird sowohl im Training als auch im Testing verwendet
        if x.shape[1] < self.beta.shape[0] and self.use_intercept == True:
            x = self.add_intercept(x) #Self, da Klassenmethode
        predictions = np.array([np.dot(x_i, self.beta) for x_i in x])
        return predictions

    # Berechnung der Streuung des Regressionsmodells
    def compute_r2(self, y, y_mean, y_pred):
        frac1 = sum([(y[i] - y_pred[i])**2 for i in range(y.shape[0])])
        frac2 = sum([(y[i] - y_mean)**2 for i in range(y.shape[0])])
        r2 = 1 - (frac1/frac2)
        return r2

    def score(self, x, y):
        y_pred = self.predict(x)
        y_mean = np.mean(y)
        score = self.compute_r2(y, y_mean, y_pred)
        return score


regr = LinearRegression(use_intercept=True)
regr.fit(x_train, y_train)

print("Coeffs: ", regr.beta[1:]) # Entspricht den Steigungen als Vektor im mehrdimensionalen Raum
print("Intercepts :", regr.beta[0]) # Entspricht dem Vector C im mehrdimenstionalen Raum
print("R2 :", regr.score(x_test, y_test)) # Entspricht Score

'''
###############################################################
# Residual Plot (Restwert) -> Wie gut funktioniert das Modell ?
###############################################################
'''
train_pred = regr.predict(x_train)
test_pred = regr.predict(x_test)

min_val = min(min(train_pred), min(test_pred))
max_val = max(max(train_pred), max(test_pred))

# Beispiel Restwert: y_pred = 10, y = 12 -> 10-12 = -2 Restwert
#
plt.scatter(train_pred, train_pred - y_train, color="blue", s=40)
plt.scatter(test_pred, test_pred - y_test, color="red", s=40)
plt.hlines(y=0, xmin=min_val, xmax=max_val) # Horizontale Gerade
plt.show()