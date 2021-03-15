'''
exifread -> Metadaten auslesen
'''

import exifread

pos_information = {} # Dictionary
with open("images/img-1.jpg", "rb") as file: # Bild als binärcode leaen -> rb
    tags = exifread.process_file(file)
    for key, value in tags.items():
        print(str(key) + ": " + str(value))

        if str(key) ==  "Image DateTime" or str(key) ==  "GPS GPSLatitudeRef" or str(key) ==  "GPS GPSLatitude" or str(key) ==  "GPS GPSLongitudeRef" or str(key) ==  "GPS GPSLongitude": # Filtern
            pos_information[key] = str(value) # zu Dictionary hinzufügen

    print("Ermittelte Metadaten: ", pos_information)