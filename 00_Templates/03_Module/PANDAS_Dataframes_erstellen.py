import pandas as pd #(Pandas ist so etwas wie excel in Pyhton)
import numpy as np

###################################################
# Beispiel 1: DataFrage Manuell erstellen
###################################################
df = pd.DataFrame({'Days':['Monday', 'Tuesday','Wednesday','Thursday','Friday'],
                    'Months':['Jan', 'Feb', 'Mar', 'May', 'nan'], # Alle Zeilen müssen gleich groß sein
                     'Zahl':['1', '2', '3', np.nan, np.nan]
                   })
print(df)

###################################################
# Beispiel 2: aus HTML im Internet auslesen
###################################################
files = pd.read_html('https://accessibility.psu.edu/tableshtml') # Html Table format
print(files)

###################################################
# Beispiel 3: Aus Datensatz laden und Spalten Zuweisen
###################################################
from sklearn.datasets import load_boston
dataset = load_boston()

print("Feature_Names")
print(dataset.feature_names)
print("Data")
print(dataset.data)

df = pd.DataFrame(dataset.data, columns=dataset.feature_names) # Erzeugt eine Tabelle mit Daten in Entsprehcenden Spalten
print(df)
all_features = df.columns.values.tolist()
num_features_total = dataset.data.shape[1] # alternativ: len(all_features)