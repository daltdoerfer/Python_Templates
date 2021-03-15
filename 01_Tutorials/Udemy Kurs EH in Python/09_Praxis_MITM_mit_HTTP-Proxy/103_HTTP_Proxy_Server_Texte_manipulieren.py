# Dieses Skript Tauscht den HTML Code zwischen Orignal Anfrage und Proxy Abfrage aus
# Skript in Kombination mit Firefox verwenden
# Wir müssen jedoch noch die Proxy Einstellungen im Browser anpassen: Manuell Proxy Config "127.0.0.1", 7654
# damit unsere Anfrage auf unseren Proxy Server umgeleitet wird
from http.server import HTTPServer, BaseHTTPRequestHandler

from socketserver import ThreadingMixIn # Für Verbesserung der Perfomance

import requests
import random

# Vererbung:Nimm gesamten Rahmen von BaseHTTPReqestHandler aber tausche ein paar Sachen aus
class MyRequestHandler(BaseHTTPRequestHandler):
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