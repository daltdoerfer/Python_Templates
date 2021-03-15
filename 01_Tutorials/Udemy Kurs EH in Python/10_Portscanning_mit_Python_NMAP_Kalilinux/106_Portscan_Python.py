#!/usr/bin/python3

import socket

ip = '192.168.0.140' # IP des Portscan geräts
print(f"Socket auf ip: {ip} wird geöffnet.")

# Portscan von Port 1 bis 65535 -> Gesamter Portbereich
for port in range(1, 65536):

    s = socket.socket() # Initialisieren

    # Unterschied:   s.connect() würde bei Fehler einfach beenden
    #                s.connect_ex() gibt als return Fehler zurück, aber arbeitet Weiter
    res = s.connect_ex((ip, port)) # Übergabe eines Tupels aus ip und port an s.connect
    s.close() # Wichtig bei vielen Portscans
    #print("Port " + str(port) + ": " + str(res))
    if res == 0: # Es tritt kein Fehler bei Portaufruf auf -> Port offen
        print("Port " + str(port) + ": " + str(res))

    if port == 65535:
        print("Programm ENDE")
