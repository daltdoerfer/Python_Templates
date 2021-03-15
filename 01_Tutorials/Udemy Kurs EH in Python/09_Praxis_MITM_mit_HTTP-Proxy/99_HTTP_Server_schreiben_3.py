# Skript in Kombination mit Firefox verwenden
# Wir müssen jedoch noch die Proxy Einstellungen im Browser anpassen: Manuell Proxy Config "127.0.0.1", 7654 (Port freigeben unter about:config -> Network.security.ports.banned)
# damit unsere Anfrage auf unseren Proxy Server umgeleitet wird
from http.server import HTTPServer, BaseHTTPRequestHandler

import requests

# Vererbung:Nimm gesamten Rahmen von BaseHTTPReqestHandler aber tausche ein paar Sachen aus
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        print(self.path) # Anfragepfad herausfinden, woher die Anfrage kommt

        # Einrücken Notwendig, damit wir kein Memory Leak haben und damit wir in Variable res zusätzliche eigenschaft haben um auf Rohdaten (stream) zugreifen zu können
        with requests.get(self.path, stream=True) as res: # Herunterladen des angefragten Pfades
            print(res)
            self.send_response(res.status_code) # Weiterleiten den Angefragten Pfades vom Broswser

            # Headers 1 zu 1 an Browser weiterleiten
            #print(res.headers) # res.headers ist ein Dictionary
            for key, value in res.headers.items(): # Auflösung Dictionary
                print("key: " + key)
                print("value: " + value)
                self.send_header(key, value)

            self.end_headers()

            #print(res.raw.read()) # Rohdaten als Bytestring ausgeben
            self.wfile.write(res.raw.read()) # Gibt die Rohdaten die von der Seite gesendet wurden weiter an Browser


address = ("127.0.0.1", 7654) # IP Adresse (entsprechend dem Computer auf dem der Server läuft) und Port -> http://127.0.0.1:7654
                               # Test auf https://iot-daltdoer.000webhostapp.com/humidity.png
server = HTTPServer(address, MyRequestHandler) # HTTP Server Adresse zuweisen, und verhalte dich entsprechend MyRequestHandler
server.serve_forever() # Server Starten und halte diesen am laufen