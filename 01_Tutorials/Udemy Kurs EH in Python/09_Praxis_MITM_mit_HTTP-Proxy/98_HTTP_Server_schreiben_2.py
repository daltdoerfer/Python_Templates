# Skript in Kombination mit Firefox verwenden
# Wir müssen jedoch noch die Proxy Einstellungen im Browser anpassen: Manuell Proxy Config "127.0.0.1", 7654
# damit unsere Anfrage auf unseren Proxy Server umgeleitet wird
from http.server import HTTPServer, BaseHTTPRequestHandler

import requests

# Vererbung:Nimm gesamten Rahmen von BaseHTTPReqestHandler aber tausche ein paar Sachen aus
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        print(self.path) # Anfragepfad herausfinden, woher die Anfrage kommt
        res = requests.get(self.path) # Herunterladen des angefragten Pfades
        print(res)
        self.send_response(res.status_code) # Weiterleiten den Angefragten Pfades vom Broswser

        # Headers 1 zu 1 an Browser weiterleiten
        #print(res.headers) # res.headers ist ein Dictionary
        for key, value in res.headers.items(): # Auflösung Dictionary
            print("key: " + key)
            print("value: " + value)
            self.send_header(key, value)
        self.end_headers()

        # Informationen an unseren Browser schicken. Geht nur in Byteform -> Daher wird Str encoded in Bytes
        self.wfile.write("Hallo Welt".encode()) # Weiterleiten des res.content


address = ("127.0.0.1", 7654) # IP Adresse (entsprechend dem Computer auf dem der Server läuft) und Port -> http://127.0.0.1:7654

server = HTTPServer(address, MyRequestHandler) # HTTP Server Adresse zuweisen, und verhalte dich entsprechend MyRequestHandler
server.serve_forever() # Server Starten und halte diesen am laufen