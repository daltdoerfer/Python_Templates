import sqlite3 # Datenbankspaket zum auslesen der Datenbank
import pandas as pd
from get_firefox_path import get_firefox_path

path = get_firefox_path("places.sqlite")
conn = sqlite3.connect(path)

##############################################################
# Lesezeichen gespeichert in moz_bookmarks UND  moz_places
# Spalte fk -> Foreign Key eines Bookmarks aus mobz_bookmarks
# gibt den Index in moz_places an in dem die URL Liegt
##############################################################
bookmarks = pd.read_sql("SELECT * FROM moz_bookmarks", conn) # Liste moz_bookmarks in Dataframe packen
print(bookmarks.head())

places = pd.read_sql("SELECT * FROM moz_places", conn)  # Liste moz_places in Dataframe packen
print(places.head())

# Filtering nach ID
for key, bookmark in bookmarks[bookmarks["fk"] > 0 ].iterrows(): # Bestimmte Werte aus mehreren Spalten ausgeben. key -> Indizes und bookmark alle restlichen Infos
    title = str(bookmark["title"]) # Gesetze Bookmark-Titel (meine Bezeichnung)
    fk = int(bookmark["fk"]) # Foreign Key aus  mobz_bookmarks als ganze Zahl (int)
    #print(fk)
    #filt = places[places["id"] == fk] # Filtert moz_places-Spalte ID nach werten die dem foreign Key entsprechen
    #print(filt)
    url = places[places["id"] == fk].iloc[0]["url"] # Filtert moz_places-Spalte ID nach werten die dem foreign Key entsprechen. iloc[0] Transformiert die Spalte der Überschriften als Zeilen und nimmt davon den Inhalt der Zeile URL
    print(title + ": \n" + url) # Achtung Fehler wenn in Zeile 21 kein str() steht -> https://careerkarma.com/blog/python-typeerror-unsupported-operand-types-for-nonetype-and-str/


