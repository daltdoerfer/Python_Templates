# Ziel dieser Case Study ist die Datenverarbeitung von Excel mit dem OneHot Encoder
# Außerdem soll hier klar gemacht werden, wann man den Ordinal- und One_hot-Encoder verwendet wird

# Adult Datensatz in XCEL Datei mit verschiedenen Features in Spaleten i bis j
# Basierend auf Features sollen wir eine Klassifikation durchführen mit dem Ziel herauszufinden,
# ob die jeweilige Person weniger als 50.000 Dollar verdient oder mehr als 50.000

# Features sind:
# Workclass (Arbeitsgebiet)
# education
# Maritial Status (Verheitratet)
# Occupation (Beruf)
# Relationship Familienstatus
# Rasse
# Geschlecht
# Geburtsland
# Klasse <50.000 Dollar oder > 50.000 Dollar pro Jahr -> Bildet unseren y-Wert siehe Zeile 6

import os # Benötigt für Zugriff auf Pfad im OS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import set_config

set_config(display="diagram")
np.random.seed(0)


# Laden des Datasets in Pandas
DATA_PATH = os.path.abspath(r"E:\Benutzer\Dropbox\Dropbox\Projekte\Programmierprojekte\Python\Udemy Kurs Machine Learning\Zusammenfassende Anwendungsbeispiele\Case_Study_2\adult.xlsx") # Über das "r" am Anfang werden die Backslashes richtig geparsed

df = pd.read_excel(DATA_PATH) # Excel in Pandas einlesen


print(f"Columnnames: {df.columns}") # Spaltenheader ausgeben. Spalte Income ist y-Wert und Rest sind unsere x-Werte
print(f"Data Types: {df.dtypes}") # Datentypen der Spalten ausgeben

print(f"Shape:\n {df.shape}") # Dimensionen der Excel ausgeben

for col_name in df.columns:
    print(f"{col_name} - Number of Categories: {len(df[col_name].value_counts())}") # Wie viele unterschiedliche Werte gibt es in der jeweiligen Spalte -> value_counts()

data = df.to_numpy()

x = data[:, :-1] # Alle Daten bis auf die letzte Spalte (x-Werte), da
y = data[:, -1] # Nur letzte Spalte stellt y-Wert dar  (siehe Zeile 6)
print(f"x-Shape: {x.shape}")
print(f"y-Shape: {y.shape}")



# Definiton Welche Spalten Numerisch und welche "Strings" sind -> für Ordninal oder OneHot Encoder notwendig
categorical_features = [1, 2, 3, 4, 5, 6, 7, 9] # Spalten mit String Informationen
numerical_features = [0, 8] # Spalten mit Zahlen-Informationen


# Problem y-Daten liegen bisher als String vor
def one_hot(y):
    return np.array([0 if val=="<=50K" else 1 for val in y], dtype=np.int32) # Prüft alle Werte in y und erzeugt einen Array mit Wert 0 bei Stringwert "<50k" und sonst 1

print(y)
y = one_hot(y)
print(y)

#### Helper
def print_grid_cv_results(grid_result):
    print(
        f"Best model score: {grid_result.best_score_} "
        f"Best model params: {grid_result.best_params_} "
    )
    means = grid_result.cv_results_["mean_test_score"]
    stds = grid_result.cv_results_["std_test_score"]
    params = grid_result.cv_results_["params"]

    for mean, std, param in zip(means, stds, params):
        mean = round(mean, 4)
        std = round(std, 4)
        print(f"{mean} (+/- {2 * std}) with: {param}")

# SKLEAN Imports
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# Classifier and Params deklarieren
# (Wichtig: Um nur einer bestimmter Task in Pipeline, die params zu übergeben, muss der Name des Pipelineobjekts wie folgt vor die eigentlichen Parameterdictionarys gestellt werden
# "Name__Dictionary":[1,2,3]
params = {"classifier__n_estimators": [50, 100, 200], # vgl. Zeile 148
          "classifier__max_depth": [None, 100, 200] # vgl. Zeile 148
          }

clf = RandomForestClassifier()

#############################################################
# ---------------- Preprocessing Teil 2 ---------------
# Problematik: Viele x-Werte in unserer Tabelle sind String-Werte
# Lösung: Verwendung von Ordinal Encoder oder OneHot Encoder
# Zweck: StandardScaler auf numerische Daten anwenden und
#        Ordinal Encoder auf Kategorische Daten anwenden
#############################################################

#############################################################
# OneHot Encoder:  der OneHot Encoder erstellt ein Array für jede Kategorie mit Werten von 0 und 1
#                    z.B Zeile Gender:    -> Male   [1, 0, 0]
#                                         -> Female [0, 1, 0]
# gäbe es noch divers würde dies wie folgt aussehen [0, 0, 1]
# Links: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html
#        https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html
#############################################################


# Pipeline -> Mehrere Verarbeitungsschritte hintereinander definieren. Output von Step 1 ist Input für Step 2 (Ähnlich Kiras bei NN mit Layern)
# https://www.statworx.com/de/blog/pipelines-mit-sklearn/
numeric_transformer = Pipeline(
                                steps=[ ('scaler',StandardScaler()) ] # Tupel aus Namen und exisiterenden Objekt (kann auch ein Konstruktor sein)
                              )

categorical_transformer = Pipeline(
                                    steps=[ ('onehot', OneHotEncoder(handle_unknown="ignore",sparse=False)) ] # Sparse=False Ergebnis der Transformation lässt keine Spalten aus
                                  )

preprocessor_onehot = ColumnTransformer(
                                          transformers=[ ('numeric', numeric_transformer, numerical_features), # Tupel aus (Name, Tranformobjekt, Definition aus welcher Spalten in den Transformer gehen sollen)
                                                         ('categorical', categorical_transformer, categorical_features) ]
                                         )

print(preprocessor_onehot)

preprocessor_onehot.fit(x_train)
x_train_onehot = preprocessor_onehot.transform(x_train)
x_test_onehot = preprocessor_onehot.transform(x_test)

print(f"onehot Data VOR Transformation: {x_train}")
print(f"onehot Data NACH Transformation: {x_train_onehot}")

print(f"Shape of onehot data: {x_train_onehot.shape}")
print(f"Shape of onehot data: {x_test_onehot.shape}")

# Machine Learning Teil
pipe_onehot = Pipeline(steps=[                                                    # Weitere Pipeline Aufgabe
                                ('preprocessor_onehot', preprocessor_onehot),
                                ('classifier', clf)                               # Call des RandomForestClassifiers
                              ]
                        )

grid_onehot = GridSearchCV(pipe_onehot, params, cv=3)
grid_results_onehot = grid_onehot.fit(x_train, y_train)
print_grid_cv_results(grid_results_onehot)


#############################################################
# Tensorflow Model
#############################################################

from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD

y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

# Funktion für unser Modelerstellung
def build_model(input_dim, output_dim):
    model = Sequential()
    model.add(Dense(units=128, input_dim=input_dim))
    model.add(Activation("relu"))
    model.add(Dense(units=64))
    model.add(Activation("relu"))
    model.add(Dense(units=output_dim))
    model.add(Activation("sigmoid"))

    return model

#############################################################
# Neural Network with OneHot Features
#############################################################
model = build_model(input_dim = x_test_onehot.shape[1],
                    output_dim=y_train.shape[1])

model.compile(loss="binary_crossentropy",
              optimizer=SGD(learning_rate=0.001),
              metrics=["binary_accuracy"])

history_onehot = model.fit(x=x_train_onehot,
                           y=y_train,
                           epochs=20,
                           validation_data=(x_test_onehot, y_test))

# Plot der Accuracy im Laufe der Epchen des Neuronalen Netzwerks
val_binary_accuracy = history_onehot.history["val_binary_accuracy"]
plt.plot(range(len(val_binary_accuracy)), val_binary_accuracy)
plt.show()

#################################################################################
# Prediction für Datenpunkte ermitteln
# Pass in user-Data
#################################################################################
pipe_onehot.fit(x_train, y_train)
score = pipe_onehot.score(x_test, y_test)
print(f"Score: {score}")

# Manuelles Hinzufügen der nochmals 1. Zeile aus unserer Excel
x_sample = [25, "Private", "11th", "Never-married", "Machine-op-inspct", "Own-child", "Black", "Male", 40, "United-States"]
y_sample = 0

y_pred_sample = pipe_onehot.predict([x_sample]) # Voraussage wie Ergebnis wohl mit neuem Datenpunkt sein wird
print(f"Pred: {y_pred_sample}") # Entspricht wie voraussgesagt dem y_sample = 0