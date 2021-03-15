# Skript in Kombination mit Google Chrome verwenden
# Wir müssen jedoch noch die Proxy Einstellungen im Browser anpassen: Manuell Proxy Config "127.0.0.1", 7654
# damit unsere Anfrage auf unseren Proxy Server umgeleitet wird
from http.server import HTTPServer, BaseHTTPRequestHandler

# Vererbung:Nimm gesamten Rahmen von BaseHTTPReqestHandler aber tausche ein paar Sachen aus
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path) # Anfragepfad herausfinden


address = ("127.0.0.1", 7654) # IP Adresse (entsprechend dem Computer auf dem der Server läuft) und Port

server = HTTPServer(address, MyRequestHandler) # HTTP Server Adresse zuweisen, und verhalte dich entsprechend MyRequestHandler
server.serve_forever() # Server Starten und halte diesen am laufen