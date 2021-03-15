# https://docs.python.org/3/library/datetime.html
import datetime

print(datetime.time) # Nur Zeit
print(datetime.date) # Nur Datum

print(datetime.datetime) # Datum mit Zeitangabe

###################################################
# Urhzeit formatieren
###################################################
# Hinweis Paket aufrufen
#       Hauptpaket.Unterpaket.Methode()
#       datetime.datetime.fromtimestamp()

datum = datetime.datetime.fromtimestamp(123224.2132) # Unix Timestamp als Zahl ohne Anführungszeichen
print(datum.hour)
print(datum.day)


###################################################
# Urhzeit formatieren
###################################################
datum = datetime.datetime.fromtimestamp(123224.2132) # Unix Timestamp als Zahl ohne Anführungszeichen
datestr = datum.strftime("%d.%m.%Y. %H:%M:%S")
print(datestr)