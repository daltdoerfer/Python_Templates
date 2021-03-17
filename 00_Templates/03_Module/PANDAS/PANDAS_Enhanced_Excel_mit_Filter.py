import pandas as pd

#################################################
# Excel Datei Einlesen
#################################################
df = pd.read_excel('./Students_from_excel.xls')

#################################################
# Filtern nach Mathe und Informatik
#################################################
logic = (df["subject"] == "Mathe") | (df["subject"] == "Informatik")
print(logic)

filt = df[(df["subject"] == "Mathe") | (df["subject"] == "Informatik")]  # Or Operator in Pandas Code um mehrere Filter miteinander zu kombinieren
print(filt)

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