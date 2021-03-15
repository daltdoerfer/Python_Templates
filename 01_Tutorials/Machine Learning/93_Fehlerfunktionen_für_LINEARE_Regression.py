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
x= dataset.data
y= dataset.target

#Automatischer Split der Datensätze in Training und Test
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=23111 ,test_size=0.3) # Train = 70%, Test = 30%

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df.head()

# Lineare Regression
regr = LinearRegression()
regr.fit(x_train, y_train)

y_pred = regr.predict(x_test)
y_true = y_test

def mse(y_true, y_pred):  # Mean Squared Error
    n = len(y_true)
    return (1/n)*np.sum((y_true[i]- y_pred[i])**2 for i in range(n)) # Bald muss np.sum(np.fromiter()) anstelle von np.sum() verwendet werden

def mae(y_true, y_pred):  # Mean Absolute Error
    n = len(y_true)
    return (1 / n) * np.sum(np.abs(y_true[i] - y_pred[i]) for i in range(n)) # Bald muss np.sum(np.fromiter()) anstelle von np.sum() verwendet werden

print("MSE: ", mse(y_true, y_pred))
print("MAE: ", mae(y_true, y_pred))

# Gleiche Funktionen aus SKLEARN
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
print("MSE: ", mean_absolute_error(y_true, y_pred)) # Bei Outlier Punkten fällt MSE viel mehr ins Gewicht da Fehler quadratisch mit einfließt
print("MAE: ", mean_squared_error(y_true, y_pred)) # Bei Outlier Punkten fällt MSE weniger ins Gewicht da Fehler NICHT quadratisch mit einfließt
