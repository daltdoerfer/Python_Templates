# Polynomiale Regression mit vorheriger Transformation der Datenpunkte -> Notwendig um aus Linearer Regression eine Polynomielle Regression zu machen -> Siehe Lektion 67
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

dataset = load_boston()
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

# Automatisiertes Splitten der Train und Testdaten
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

x= dataset.data[:,:2]  #Nimmt alle Zeilen und ausgewählte Spalten von Index 0 bis 1 (exclusive 2)
y= dataset.target

#Automatischer Split der Datensätze in Training und Test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3) # Train = 70%, Test = 30%

# Transformation von unsere Eingangsdaten x1 und x2
deg = 4 # Grad 2 Transformation von unseren Datenpunkten (Eingang siehe dataset.data[:,:2] -> X1 & X2) -> Kombinationen siehe  print(pf.get_feature_names()) in Zeile 30
        # Wichtig -> Dieser Parameter kann verstellt werden. Mit der Score überprüfung am Ende kann geschaut werden, ob diese veränderung positiven Einfluss hat
pf = PolynomialFeatures(degree=deg)
pf.fit(x_train)

x_trans_train = pf.fit_transform(x_train) # Nur die X Werte werden Transformiert y bleiben gleich
x_trans_test = pf.fit_transform(x_test)

print(pf.n_input_features_) # Wieviel x-Werte gab es
print(pf.n_output_features_) # Wieviele Transformierte x-Werte gibt es nun

print(pf.get_feature_names()) # Zeigt alle Transformationskombinationen an

#Vergleich mit einfachem Linearen Modell nach Transformation
from sklearn.linear_model import LinearRegression
linear = LinearRegression()
linear.fit(x_trans_train, y_train)

score = linear.score(x_trans_test, y_test)
print(score)

# Residual Plot (Restwert)
train_pred = linear.predict(x_trans_train)
test_pred = linear.predict(x_trans_test)

min_val = min(min(train_pred), min(test_pred))
max_val = max(max(train_pred), max(test_pred))

plt.scatter(train_pred, train_pred - y_train, color="blue", s=40)
plt.scatter(test_pred, test_pred - y_test, color="red", s=40)
plt.hlines(y=0, xmin=min_val, xmax=max_val)
plt.xlabel("Predicted Value")
plt.ylabel("Residual: Pred - True")
plt.show()

# Kommentar