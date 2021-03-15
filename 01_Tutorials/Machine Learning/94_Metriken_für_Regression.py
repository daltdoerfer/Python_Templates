# Imports (allgemein gültig)
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dataset for Classifications
dataset = load_boston()
x = dataset.data
y = dataset.target

#Automatischer Split der Datensätze in Training und Test
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=23111 ,test_size=0.3) # Train = 70%, Test = 30%

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df.head()

#Lineare Regression
regr = LinearRegression()
regr.fit(x_train, y_train)

y_pred = regr.predict(x_test)
y_true = y_test

def r_squared(y_true, y_pred):  # Mean Squared Error
    n = len(y_true)
    y_true_mean = np.mean(y_true)
    num = np.sum(np.fromiter(((y_true[i] - y_pred[i])**2 for i in range(n)), dtype=float)) # Bald muss np.sum(np.fromiter()) anstelle von np.sum() verwendet werden
    denom = np.sum(np.fromiter(((y_true[i] - y_true_mean)**2 for i in range(n)), dtype=float)) # Bald muss np.sum(np.fromiter()) anstelle von np.sum() verwendet werden
    return 1.0 - (num/denom)


def mape(y_true, y_pred):  # Mean Absolute Percentage Error (Eher Metrik als Error) -> Aussage wie weit liege ich den Prozentual vom Richtigen Ergebnis weg ?
    n = len(y_true)
    frac = np.sum(np.fromiter((np.abs((y_true[i] - y_pred[i])/y_true[i]) for i in range(n)), dtype=float)) # Bald muss np.sum(np.fromiter()) anstelle von np.sum() verwendet werden
    return (100/n)*frac


print("R2: ", r_squared(y_true, y_pred)) # 0,7 ist ok ->  ist Bester Wert
print("MAPE: ", mape(y_true, y_pred)) # 18% ist ok aber nicht gerade gut

# Gleiche Funktionen aus SKLEARN
from sklearn.metrics import r2_score
#from sklearn.metrics import

print("R2: ", r2_score(y_true, y_pred))


