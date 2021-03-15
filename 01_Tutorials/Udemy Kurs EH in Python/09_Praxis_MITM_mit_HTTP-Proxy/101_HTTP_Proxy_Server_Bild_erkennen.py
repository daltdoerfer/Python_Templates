# Skript in Kombination mit Firefox verwenden
# Wir müssen jedoch noch die Proxy Einstellungen im Browser anpassen: Manuell Proxy Config "127.0.0.1", 7654
# damit unsere Anfrage auf unseren Proxy Server umgeleitet wird
from http.server import HTTPServer, BaseHTTPRequestHandler

from socketserver import ThreadingMixIn # Für Verbesserung der Perfomance

import requests

# Vererbung:Nimm gesamten Rahmen von BaseHTTPReqestHandler aber tausche ein paar Sachen aus
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "https://iot-daltdoer.000webhostapp.com/humidity.png": # Nur wenn folgende Seite aufgerufen wird passiert das untere, sonst wird die normale Seite aufgerufen

            # Für speziellen Text:
            #self.send_response(200)
            #self.send_header("Content-Type", "text/plain") # Text
            #self.end_headers()
            #self.wfile.write("Katzenbild".encode()) #Text

            # Für anderes Bild
            self.send_response(200)
            self.send_header("Content-Type", "image/jpeg") # Text
            self.end_headers()

            with open("Bilder/1.jpg", "rb") as file:
                self.wfile.write(file.read()) #Text

        else:
            # Einrücken Notwendig, damit wir kein Memory Leak haben und damit wir in Variable res zusätzliche eigenschaft haben um auf Rohdaten (stream) zugreifen zu können
            with requests.get(self.path, stream=True) as res: # Herunterladen des angefragten Pfades

                self.send_response(res.status_code) # Weiterleiten den Angefragten Pfades vom Broswser
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