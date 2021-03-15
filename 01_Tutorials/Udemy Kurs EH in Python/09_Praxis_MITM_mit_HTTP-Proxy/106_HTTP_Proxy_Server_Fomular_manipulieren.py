# Dieses Skript Tauscht den HTML Code zwischen Orignal Anfrage und Proxy Abfrage aus
# Skript in Kombination mit Firefox verwenden
# Wir müssen jedoch noch die Proxy Einstellungen im Browser anpassen: Manuell Proxy Config "127.0.0.1", 7654
# damit unsere Anfrage auf unseren Proxy Server umgeleitet wird
from http.server import HTTPServer, BaseHTTPRequestHandler

from socketserver import ThreadingMixIn # Für Verbesserung der Perfomance

import requests
import random
import urllib

# Vererbung:Nimm gesamten Rahmen von BaseHTTPReqestHandler aber tausche ein paar Sachen aus
class MyRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        print(self.path)
        print(self.headers) # Header wenn der Browser dem Proxy Daten schickt
        if self.headers["content-type"] == "application/x-www-form-urlencoded": # Wenne es sich um Typ Formular handelt
            length = int(self.headers["content-length"]) # Länge des Formularinhalts als integer ermitteln
            print(length)
            read_form_raw = str(self.rfile.read(length), "utf-8") # Formulardaten lesen (raw)
            data = urllib.parse.parse_qs(read_form_raw) # Raw Formular zerlegen in strukturierte Form (dict) umwandeln


            # Hier werden die Formulardaten manipuliert
            if "content" in data: # Gibt es den Eintrag Content im Formular
                if type(data["content"]) == list: # Ist dieser eintrag eine Liste ?
                    if len(data["content"]) == 1:
                        data["content"][0] = data["content"][0].replace("top, flop") # Wort "top" durch "flop" ersetzen
                    print(data)
            # Hier könnte der Proxy Server auch wieder top durch flop ersetzen damit der Angegriffene garnichts merkt

            # Schicke Post Requests an Server mit Formulardaten data ,welche wir gerade eben auzsgelesen haben
            with requests.post(self.path, data=data, stream=True) as res:

                self.send_response(res.status_code) # ABSOLUT NOTWENDIGE ZEILE. Statuscode muss immer an Browser mitgeteilt werden. Weiterleiten den Angefragten Pfades vom Broswser
                # Headers 1 zu 1 an Browser weiterleiten
                #print(res.headers) # res.headers ist ein Dictionary
                for key, value in res.headers.items(): # Auflösung Dictionary
                    self.send_header(key, value)
                self.end_headers()

                # Informationen an unseren Browser schicken. Geht nur in Byteform -> Daher wird Str encoded in Bytes
                self.wfile.write(res.raw.read()) # Gibt die Rohdaten die von der Seite gesendet wurden weiter an Browser

    def do_GET(self):

        if self.path[-4:] == ".jpg": # Nur wenn folgende Dateiendeung

            # Für anderes Bild
            self.send_response(200)
            self.send_header("Content-Type", "image/jpeg") # Text
            self.end_headers()

            images = ["./Bilder/1.jpg", "./Bilder/2.jpg"]

            with open(random.choice(images), "rb") as file:
                self.wfile.write(file.read()) # Text

        else:
            # Einrücken Notwendig, damit wir kein Memory Leak haben und damit wir in Variable res zusätzliche eigenschaft haben um auf Rohdaten (stream) zugreifen zu können
            with requests.get(self.path, stream=True) as res: # Herunterladen des angefragten Pfades

                self.send_response(res.status_code) # Weiterleiten den Angefragten Pfades vom Broswser

                print(res.headers) # res Headers -> Original Server Headers an Proxy  die (als Dictionary)
                if "text/html" in res.headers["content-type"]: # Wenn es sich um html Datei handelt
                    self.send_header("Content-Type", "text/html") # Bezieht sich auf die Headers die unser Proxy an den Browser schickt.
                    print(res.content) # Enthält Originalinhalt was Server geantwortet hat
                    content = str(res.content, "utf-8") # Interne Übergabe als String mit utf-8 Format
                    content = content.replace("Bilder", "Katzenbilder") # Ersetzt in HTML das Wort Bilder durch Katzenbilder
                    #self.wfile.write(res.content, encode()) # Senden des Originalinhaltes
                    self.wfile.write(content, encode()) # Senden unserer Message

                else:
                    # Headers 1 zu 1 an Browser weiterleiten
                    #print(res.headers) # res.headers ist ein Dictionary
                    for key, value in res.headers.items(): # Auflösung Dictionary
                        self.send_header(key, value)
                    self.end_headers()

                    # Informationen an unseren Browser schicken. Geht nur in Byteform -> Daher wird Str encoded in Bytes
                    self.wfile.write(res.raw.read()) # Gibt die Rohdaten die von der Seite gesendet wurden weiter an Browser

# Optimierung -> Kombination aus ThreadMixIn, HTTPServer (Mehrfachvererbung)
class ThreadingHTTPServer(ThreadingMixIn, HTTPServer): #
    pass

address = ("127.0.0.1", 7654) # IP Adresse (entsprechend dem Computer auf dem der Server läuft) und Port -> http://127.0.0.1:7654

server = ThreadingHTTPServer(address, MyRequestHandler) # ThreadingHTTP Server Adresse zuweisen, und verhalte dich entsprechend MyRequestHandler
server.serve_forever() # Server Starten und halte diesen am laufen