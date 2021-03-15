#
'''
Ridge Regression - erweiterung der Linearen Regression mit Optimierung gegen Overfitting
Prinzipiell versucht die Ridge-Regression-Funktion den Einfluss der unwichtigen Beta-Faktoren in der Linearen Regression zu minimieren
Funktionen
    SSE = Fehlerfunktion (SUM of squared errors)
    beta_ridge =
 https://www.udemy.com/course/machine-learning-grundlagen-mit-python-inkl-ai-einfuhrung/learn/lecture/11587922#overview
'''

import pandas as pd #(Pandas ist so etwas wie excel in Pyhton)
from sklearn.datasets import load_boston
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg


dataset = load_boston()

#print(dataset)
x = dataset.data
y = dataset.target

df = pd.DataFrame(dataset.data, columns = dataset.feature_names)
print(df.head)


from sklearn.model_selection import train_test_split

x= dataset.data[:,:]
y= dataset.target

#Automatischer Split der Datensätze in Training und Test
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.3) # Train = 70%, Test = 30%

'''
###############################################################
Berechnung der mehrdimensionalen Linearen Regression
Formeln
beta = (X_Transp * X)^(-1) *X_Trans * y
y_dach= X * beta
###############################################################
'''

class RidgeRegression:
    def __init__(self, lamb, use_intercept=True):
        self.beta = None
        self.use_intercept = use_intercept
        self.lamb = lamb
        self.n_features = None

    def add_intercept(self, x):
        intercepts = np.ones(x.shape[0]) # Erstellt X 1er Eintäge wobei X die Anzahl der Zeilen unseres Datensets ist
        x = np.column_stack((intercepts, x)) # Nimmt Vektor "intercepts" und fügt den Vektor "X" in Weiterer Spalte hinzu
        return x

    def fit(self, x, y): # Wird nur im Training verwendet
        if self.use_intercept == True:
            x = self.add_intercept(x) #Self, da Klassenmethode
        self.n_features = x.shape[1]
        # Compute Closed Form
        inner_1 = np.dot(x.T, x)
        inner_2 = np.dot(self.lamb, np.identity(self.n_features))
        inner_ges = np.add(inner_1, inner_2)
        inv = np.linalg.inv(inner_ges)
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

'''
Hier die Funktion -> Lambdawerte verändern für 
'''
lambdas = [0.0, 1.0, 10, 100, 1000]

for lamb in lambdas:
    regr = RidgeRegression(lamb = lamb, use_intercept=True)
    regr.fit(x_train, y_train)

    print("Lambda : ", lamb)
    print("Coeffs: ", regr.beta[1:]) # Entspricht den Steigungen als Vektor im mehrdimensionalen Raum
    print("Intercepts :", regr.beta[0]) # Entspricht dem Vector C im mehrdimenstionalen Raum
    print("R2 :", regr.score(x_test, y_test), "\n\n") # Entspricht Score

# Abschließende Bemerkung: in dieser Funktion Verbessert sich nichts -> Siehe R2 Wert wird schlechter bei erhöhung von Lambda


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