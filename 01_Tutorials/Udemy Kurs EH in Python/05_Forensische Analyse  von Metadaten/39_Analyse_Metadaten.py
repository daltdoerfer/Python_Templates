'''
In diesem Code wird zunächst mithilfe des Python Pakets "Requests" eine HTML-Homepage
abgerufen, gespeichert, und processed um Metadaten aus Bildern gezielt zu extrahieren

 Packages:
 Requests: https://requests.readthedocs.io/en/master/
 BS4 BeautifulSoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/
 exifread -> Metadaten auslesen
'''

import requests
import urllib
from bs4 import BeautifulSoup


url = "http://python.vic-tim.de/images/" # Adresse unserer Zielhomepage

response = requests.get(url) # HTML einlesen
print(response) # 200 Heisst alles in Ordnung, 404 -> Not found
print(response.status_code)
print(response.text) # Komplette HTML in Textform ausgeben

found_images = [] # Leere Liste
if response.status_code == 200: # Nur beginnen wenn abfrage erfolgreich

    doc = BeautifulSoup(response.text, "html.parser") # Dokument erstellen in welches die HTML seite geschrieen wird

    # Beispiel etwas finden -> mehr dazu siehe die Doku von BS4
    # print(doc.title) # Nach Title Suchen
    # print(doc.find_all('img')) # gibt alle <img>´s aus

    images = doc.find_all('img')

    for img in images:
        #print(type(img))  # Typinformationen des Bildes
        #print(img)  # Alle Infos aus Img Zeilen ausgeben
        #print(img.attrs)  # Gibt Eigenschaften des Html Elementes aus
        #print(img.attrs["src"])  # Die Quelle des Bildes auf der HTML seite als relative Pfadangabe
        path = urllib.parse.urljoin(url, img.attrs["src"])  # Erzeugt den kommpletten Pfad der Bilder auf der jeweiligen Homepage
        print(path)
        found_images.append(path) # Liste mit Pfad-Bildern

#####################################################################################
# Neuen Pfad erstellen
#####################################################################################
import os
if not os.path.exists("images"):  # Nur wenn Ordner noch nicht exisitiert
    os.mkdir("images")  # Images Ordner erstellen

#####################################################################################
# Bilder Herunterladen
#####################################################################################

for found_image in found_images:
    # print(found_image.split("/")) # Unseren aktuellen Pfad an jedem "/" Zerteilen
    filename = found_image.split("/")[-1]  # Auf letzten Eintrag des zerteilten Pfades zugreifen -> Dateiname
    response = requests.get(found_image)  # Alle Bilder herunterladen

    with open("./images/" + filename, "wb") as file:  # Neues File öffnen und Bild darunter als binärecode abspeichern (kein Text sondern Bild daher binär)
        file.write(response.content) # Schreibt den Content des Bildes in das offene File

    print(response)
    #print(len(response.text)) # Zeigt an wie lang bild ist (als Binärdaten)
    print(len(response.content)) # Zeigt an wie lang bild ist (als Bytecontent)
    print(response.content[:100]) # Zeigt die ersten 100 Byte des Bildes an