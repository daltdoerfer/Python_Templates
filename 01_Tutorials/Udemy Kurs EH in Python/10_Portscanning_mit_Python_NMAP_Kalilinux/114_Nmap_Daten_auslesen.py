from bs4 import BeautifulSoup

with open("nmap.xml", "r") as file:
    content = file.read()
    #print(content)

    print("Nmap Befehl + Datum:")
    print("-----------------------------")
    doc = BeautifulSoup(content, "html.parser")

    nmaprun = doc.select("nmaprun")[0] # Element 0 aus Liste
    print(nmaprun.attrs["args"]) # Gibt das Attribut args für verwendeten NMap Befehl aus
    print(nmaprun.attrs["startstr"]) # Gib Attribut für Datum aus

    print("-----------------------------")

    # Alle interessanten Hostelemente ausgeben
    hosts = doc.select("host[endtime]") # Suche alle Elemente des Typs host mit existierendem Attribut endtime
    print("Anzahl Geräte gefunden: " + str(len(hosts))) # Anzahl exisitierender Hostelemente
    print("\n")
    for host in hosts:

        #############################
        # MAC_Address Informationen
        #############################
        mac = host.select("address[addrtype='mac']")

        if len(mac):
            vendor = mac[0].attrs["vendor"]
            mac_address = mac[0].attrs["addr"]
            print("Hersteller: " + vendor + " \nMAC-Adresse: " + str(mac_address))
        else:
            print("Mac-Adresse nicht gefunden")

        #############################
        # IP Informationen
        #############################
        ipv4 = host.select("address[addrtype='ipv4']")
        if len(ipv4):
            ip = ipv4[0].attrs["addr"]
            print("IPv4: " + str(ip))
        else:
            print("Keine IPv4 gefunden")

        ipv6 = host.select("address[addrtype='ipv6']")
        if len(ipv6):
            ip = ipv6[0].attrs["addr"]
            print("IPv6: " + str(ip))
        else:
            print("Keine IPv6 gefunden")



        #############################
        # OS Informationen
        #############################
        os = host.select("osclass[osfamily]")

        osfamily = os[0].attrs["osfamily"]
        accuracy  = os[0].attrs["accuracy"]
        print("OS: zu  " + accuracy + "% " + osfamily)

        # Ports Used
        port_used = host.select("portused[state]")
        portid = port_used[0].attrs["portid"]
        protokoll = port_used[0].attrs["proto"]
        state = port_used[0].attrs["state"]
        print("Port-ID: " + portid + " / Status: "+ state +" / Protokoll: " + protokoll + "\n")


