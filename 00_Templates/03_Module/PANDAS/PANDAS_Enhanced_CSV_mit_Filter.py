import pandas as pd

#################################################
# CSV Datei Einlesen
#################################################
df = pd.read_csv('students_from_excel.csv', delimiter=";") # Delimiter auswählen (Komma als default)

print(df)
print("\n")

#################################################
# Filtern nach mehreren Strings
#################################################
logic = (df["subject"] == "Mathe") | (df["subject"] == "Informatik")
print(logic)
print("\n")

filt = df[(df["subject"] == "Mathe") | (df["subject"] == "Informatik")]  # Or Operator in Pandas Code um mehrere Filter miteinander zu kombinieren
print(filt)
print("\n")

#################################################
# Filtern nach Zahlen mit Veroderung
#################################################
filt = df[(df["semester"] < 5) | (df["semester"] > 2)]
print(filt)
print("\n")

#################################################
# Mehrere Filter überalgern
#################################################
cs_students = df[df["subject"] == "Informatik"]  # 1. Filter
filter = cs_students[cs_students["semester"] == 4]  # 2. Filter auf den ersten filter anwenden
print(filter)