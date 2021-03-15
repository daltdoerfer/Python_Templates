import sqlite3 # Datenbankspaket zum auslesen der Datenbank
import pandas as pd
from get_firefox_path import get_firefox_path
import datetime

path = get_firefox_path("places.sqlite")
conn = sqlite3.connect(path)

##############################################################
# Lesezeichen gespeichert in moz_bookmarks UND  moz_places
# Spalte fk -> Foreign Key eines Bookmarks aus mobz_bookmarks
# gibt den Index in moz_places an in dem die URL Liegt
##############################################################
history = pd.read_sql("SELECT * FROM moz_historyvisits", conn) # Liste moz_bookmarks in Dataframe packen
print(history.head())

places = pd.read_sql("SELECT * FROM moz_places", conn)  # Liste moz_places in Dataframe packen
print(places.head())

# Filtering nach ID
for key, item in history.iterrows(): # Bestimmte Werte aus mehreren Spalten ausgeben. key -> Indizes und item alle restlichen Infos
    place_id = item["place_id"] # id der besuchten Website (meine Bezeichnung)
    visit_date_unix_ms = item["visit_date"] # Datum der besuchten Web ID (meine Bezeichnung) als Unix Time Stamp in Millisekunden seit 1970 siehe Code 57_Unix_Timestamp
    timestamp = datetime.datetime.fromtimestamp(visit_date_unix_ms / 1000000) # Modul datetime Timestamp mit Umrechnung in
    #filt = places[places["id"] == place_id] # Filtert moz_places-Spalte ID nach werten die der place_id entsprechen
    #print(filt)
    url = places[places["id"] == place_id].iloc[0]["url"] # Filtert moz_places-Spalte ID nach werten die dem foreign Key entsprechen. iloc[0] Transformiert die Spalte der Überschriften als Zeilen und nimmt davon den Inhalt der Zeile URL
    print(url) # Achtung Fehler wenn in Zeile 21 kein str() steht -> https://careerkarma.com/blog/python-typeerror-unsupported-operand-types-for-nonetype-and-str/
    print(timestamp.strftime("Datum: %d.%m.%Y %H:%M:%S \n"))
    #print(str(timestamp) + "\n") # Alternative

