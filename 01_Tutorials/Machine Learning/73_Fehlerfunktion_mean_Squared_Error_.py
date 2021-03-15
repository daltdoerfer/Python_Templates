# Mean Squared Error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
import numpy.linalg

dataset = load_boston()
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

from sklearn.model_selection import train_test_split


x= dataset.data[:,:]
y= dataset.target

#Automatischer Split der Datensätze in Training und Test
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.3) # Train = 70%, Test = 30%

# Wiederholung -> Basiert auf MeanSquared Error
from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(x_train, y_train)
score = regr.score(x_test, y_test)

print("Score: ", score)

# Ausgabe des MEANSquaredErrors
mse_error = 0.0 # Initialisierung Fehlerwert
for i in range(len(x_test)):
    y_pred = regr.predict([x_test[i]])
    err = (y_test[i] - y_pred)**2 # Fehlerfunktion bestraft abweichung quadratisch
    mse_error += err

print("MSE: ", mse_error / len(x_test))

from sklearn.metrics import mean_squared_error
y_pred = regr.predict(x_test)
print("MSE (über SKlearn Funktion): ", mean_squared_error(y_test, y_pred))

