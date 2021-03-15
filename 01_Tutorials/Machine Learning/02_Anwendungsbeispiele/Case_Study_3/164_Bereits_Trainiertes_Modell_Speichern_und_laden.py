# Viele Datensätze unter
# https://www.kaggle.com/
# https://www.kaggle.com/datasets

# Wenn Strings in Datensätze vorhanden sind müssen diese mit dem OneHot oder Ordinal Encoder Preprocessed werden Siehe Case_Study_2

import os # Benötigt für Zugriff auf Pfad im OS
import numpy as np
import pandas as pd


#################################################################
# ----------------------Dataset import---------------------------
#################################################################
DATA_PATH = os.path.abspath(r"E:\Benutzer\Dropbox\Dropbox\Projekte\Programmierprojekte\Python\Udemy Kurs Machine Learning\Zusammenfassende Anwendungsbeispiele\Case_Study_3\employee_data.csv") # Über das "r" am Anfang werden die Backslashes richtig geparsed

df = pd.read_csv(DATA_PATH) # df -> Dataframe

print(df.head()) # Vergleich vorher
df = df.drop("Unnamed: 0", axis=1) # Zeilenbereiche löschen drop("label der Zeile oder Spalte", axis=0 -> Zeilen oder axis=1 ->Spalten )
df = df.drop("id", axis=1)
print(df.head())  # Vergleich nachher

data = df.to_numpy()
x = data[:, :-1]
y = data[:, -1]

# Definiton Welche Spalten Numerisch und welche "Strings" sind -> für Ordninal oder OneHot Encoder notwendig
categorical_features = [0]
numerical_features = [1, 2, 3]

print(f"x-shape {x.shape}")
print(f"y-shape {y.shape}")

#################################################################
# ----------------------SKLEAN Imports---------------------------
#################################################################

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
#from sklearn.model_selection import GridSearchCV

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

regr = RandomForestRegressor(n_estimators=100)

# Pipeline -> Mehrere Verarbeitungsschritte hintereinander definieren. Output von Step 1 ist Input für Step 2 (Ähnlich Kiras bei NN mit Layern)
# https://www.statworx.com/de/blog/pipelines-mit-sklearn/
numeric_transformer = Pipeline(steps=[('scaler', StandardScaler())]) # Tupel aus Namen und exisiterenden Objekt (kann auch ein Konstruktor sein)


categorical_transformer = Pipeline(steps=[('ordinal', OrdinalEncoder())])

preprocessor_ordinal = ColumnTransformer(
    transformers=[('numeric', numeric_transformer, numerical_features), # Tupel aus (Name, Tranformobjekt, Definition aus welcher Spalten in den Transformer gehen sollen)
                  ('categorical', categorical_transformer, categorical_features)])


# Machine Learning Teil
pipe_ordinal = Pipeline(steps=[                                                   # Weitere Pipeline Aufgabe
                                ('preprocessor_ordinal', preprocessor_ordinal),
                                ('regressor', regr)                               # Call des RandomForestRegressors
                              ]
                       )

pipe_ordinal.fit(x_train, y_train)
score = pipe_ordinal.score(x_test, y_test)

print(f"Score: {score}")

#################################################################
# ----Classifier oder Regressoren Speicher/laden in/aus Binary---
#################################################################

import pickle # Kann alle Serialisierbaren Objekte in Python als binäre Datei abspeichern

pickle.dump(regr, open("model.pkl", "wb")) # unsere Regressor Speichern -> in Datei "model.pkl" als Binärcode  (WriteBinary = wb)
regr = pickle.load(open("model.pkl", "rb")) # Regressor laden aus Binary

x_sample = np.array([0, 40, 10, 10]) #
y_pred = regr.predict([x_sample]) #

print(f"Pred: {y_pred}")
