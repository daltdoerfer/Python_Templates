# Doku places.sqlite https://developer.mozilla.org/en-US/docs/Mozilla/Tech/Places/Database
# z.B: Bookmarks in moz_boookmarks
import os
import sqlite3 # Datenbankspaket zum auslesen der Datenbank
import pandas as pd
from get_firefox_path import get_firefox_path
# Alternativ: import get_firefox_path as gfp # -> Hier nüsste jedoch der Aufruf der Funktions wie folgt lauten gfd.get_firefox_path()



##############################################################################
# Funktionsaufruf
##############################################################################
path = get_firefox_path("places.sqlite")
#os.startfile('C:\\Users\\James/AppData/Roaming/Mozilla/Firefox/Profiles') # Öffnen zum betrachten

conn = sqlite3.connect(path)
print(conn)

# Ausgabe in Pandas
df = pd.read_sql("SELECT * FROM moz_bookmarks", conn)
print(df)


