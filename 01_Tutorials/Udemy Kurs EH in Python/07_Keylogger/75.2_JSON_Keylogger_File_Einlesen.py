import json
import datetime
import glob # module to get a list of files for wildcards:


path = "./*.txt" # Wildcard File einlesen
for filename in glob.glob(path):
    print("File :", filename)
    with open(filename, 'r') as file:
        for line in file:
            #print(line) # Vergleich kein Python Objekt sondern reiner Text
            data = json.loads(line) # Wandle JSON-Text in Python Dictionary Objekt um

            #print(data) # Zeigt alle Daten im Dicionary
            #print(data["event_type"]) # Zeigt nur ob Taste gedrück oder losgelassen wurde


            # Herausfinden welche Tasten herunter gedrückt wurden
            if data["event_type"] == "down":

                # Zeit des Tastenanschlags auslesen
                datum = datetime.datetime.fromtimestamp(data["time"]) # Unix Timestamp als Zahl ohne Anführungszeichen
                date_str = datum.strftime("%d.%m.%Y. %H:%M:%S")

                print(data["name"] +"\t" + date_str )


