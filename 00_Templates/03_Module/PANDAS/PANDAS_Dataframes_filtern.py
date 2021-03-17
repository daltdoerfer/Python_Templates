import pandas as pd #(Pandas ist so etwas wie excel in Pyhton)
import numpy as np

###################################################
# DataFrage Manuell erstellen
###################################################
df = pd.DataFrame({'Days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                   'Months': ['Jan', 'Feb', 'Mar', 'May', 'nan'], # Alle Zeilen müssen gleich groß sein
                   'Zahl': ['1', '2', '3', np.nan, np.nan],
                   'Tage': ['5', '1', '2', '5', '4']
                   })
print(df)
print("Header:")
print(df.head) # Nur die ersten Zeilen Ausgeben
print("\n")
###################################################
# Auf einzelne Spalten Zugreifen
###################################################
print("Spalte Days ausgeben:")
print(df["Days"]) # Einzelne Spalten ausgeben
print("\n")

###################################################
# In jeder Zeile mehrere Spaltenwerte ausgeben
###################################################
# key -> Interne Numerierung in Pandas, startet von 0;
# item -> Restliche Informatiuon
for key, item in df.iterrows(): # Es wird über Zeilen Iteriert:
    print(item["Days"] + " " + item["Months"]) # Zugriff auf die direkten Spaltenwerte

print("\n")

###################################################
# Spalten Filtern
###################################################
# Nach String filtern
logik = df["Days"] == 'Monday' # Bool-logik der Filterung anzeigen für ganze Spalte
print(logik)
print("\n")
filt = df[df["Days"] == 'Monday'] # Es werden nur noch die Filterungen angezeigt
print(filt)
print("\n")

# Nach Zahlen filtern
filt = df[df["Tage"] >= str(2)] # Es werden in 'Tagen' nach Werten >= 2 Gesucht. Zahl muss als String vorliegen
print(filt)
print("\n")

print(filt.head()) # Die ersten Zeilen der gefilterten Daten anzeigen
print("\n")