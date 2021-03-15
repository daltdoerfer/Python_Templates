# Kombinatorik: Alle möglichkeiten aus 2 aus 13 Features

import itertools
import random
random.seed(0)

import numpy as np
np.random.seed(0) # Spezifische Random Verteilung bei Permutation
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression


'''
###############################################################
 Load Dataset
 ##############################################################
'''
dataset = load_boston()
df = pd.DataFrame(dataset.data, columns=dataset.feature_names) # Erzeugt eine Tabelle mit Daten in Entsprehcenden Spalten

all_features= df.columns.values.tolist()
num_features_total = dataset.data.shape[1] # alternativ: len(all_features)

print(all_features)
print("Num Features: ", num_features_total)

# Ermittlung aller Kombinationen
total_feature_combs = 0
for num in range(1, num_features_total): # Iteration von 1 bis 13
    current_feature_combs = len([v for v in itertools.combinations(all_features, num)]) #https://docs.python.org/3/library/itertools.html ->  Kombinationstool
    total_feature_combs += current_feature_combs
    print("Combs with", num, "combs")

print("Total:", total_feature_combs)

# Alle Kombinationen ermitteln
best_score = 0.0
for num in range(1, num_features_total+1): # 1 bis inclusive 13 -> Wieviel Feature Pro Iteration genommen werden sollen
    for features in itertools.combinations(all_features, num): # Alle Möglichen Kombinationen mit unterschiedlicher Feature anzahl erstellen -> Beispiel unter Templates/Kombinatorik_Itertools.py
        df_features = pd.DataFrame(df, columns=features)

    x = df_features.to_numpy() # Convert the DataFrame to a NumPy array.
    y = dataset['target'] # Enstpricht y=dataset.target


    num_samples = len(x) # Oder: x.shape(0)
    indizes = np.random.permutation(len(x))
    test_size = 100
    # Diese Daten gehen ins Trainingsset
    x_train = x[indizes[:-test_size]] # Nimmt alle  Werte die den vertauschten Indizes hinterlegt sind. Alle bis auf die letzen 100 [:-100]
    y_train = y[indizes[:-test_size]]
    # Diese Daten gehen ins Testset
    x_test = x[indizes[-test_size:]] # Nimmt alle  Werte die den vertauschten Indizes hinterlegt sind. Alle bis auf die letzen 100 [:-100]
    y_test = y[indizes[-test_size:]]


    # Create Linear Regession Object
    regr = LinearRegression()
    # Train model using the training sets
    regr.fit(x_train, y_train)

    score = regr.score(x_test, y_test)

    if score > best_score: # Immer nur ausgeben wenn aktueller Score besser als bisherig besserer
            best_score = score
            print("R2: ", score)
            print(features)

# Bestes Modell Trainieren
features =  ['CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
df_features = pd.DataFrame(df, columns=features)

x= df_features.to_numpy()
y= dataset.target

test_size = 100

x_train = x[indizes[:-test_size]]  # Nimmt alle  Werte die den vertauschten Indizes hinterlegt sind. Alle bis auf die letzen 100 [:-100]
y_train = y[indizes[:-test_size]]
# Diese Daten gehen ins Testset
x_test = x[indizes[-test_size:]]  # Nimmt alle  Werte die den vertauschten Indizes hinterlegt sind. Alle bis auf die letzen 100 [:-100]
y_test = y[indizes[-test_size:]]

regr = LinearRegression()
regr.fit(x,y)

#Residual Plot (Restwert)
train_pred = regr.predict(x_train)
test_pred = regr.predict(x_test)

min_val = min(min(train_pred), min(test_pred))
max_val = max(max(train_pred), max(test_pred))

plt.scatter(train_pred, train_pred - y_train, color="blue", s=40)
plt.scatter(test_pred, test_pred - y_test, color="red", s=40)
plt.hlines(y = 0, xmin = min_val, xmax= max_val)
plt.xlabel("$\hat{y} (Predicitons)$")
plt.ylabel("Residuals")
plt.show()