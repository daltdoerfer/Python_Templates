'''
Kombination aus Ridge und Lasso Regression -> ElasticNET Regression
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html?highlight=elasticnet#sklearn.linear_model.ElasticNet
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

# Hauptfunktion

from sklearn.linear_model import ElasticNet

alphas = [1, 2, 5, 10]
l1_ratios = [0.25, 0.5, 0.75, 1.0] # Bezieht sich auf die Lasso Regression -> 0.25 heisst zu 0.25 wird die Lasso Regression miteinbezogen

for alpha in alphas:
    for l1_ratio in l1_ratios:
        regr = ElasticNet(alpha = alpha, l1_ratio = l1_ratio)
        regr.fit(x_train, y_train)
        print("Alpha, L1-Ratio: ", alpha, l1_ratio)
        print("Score: ", regr.score(x_test, y_test))

''' Interpretation der Ergebnisse: 
Bester Score bei erster Iteration -> 0.25 % Lass, 0.75 Ridge Regression 
 -> Ridge Regression besser geeignet -> Features hängen wohl miteinander zusammen, da Lasso Regression ja versucht überflüssige Features zu entfernen

'''

# Nochmal mit bestem gefundenem Ergbnis laufen lassen
regr = ElasticNet(alpha=1.0, l1_ratio=0.25)
regr.fit(x_train, y_train)

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