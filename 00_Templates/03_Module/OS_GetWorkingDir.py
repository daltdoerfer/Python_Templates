############################################################################################################
# Pfade ermitteln, kombinieren, öffnen, Programme ausführen
# Pfade richtig angeben -> siehe Link:
# https://www.btelligent.com/blog/best-practice-arbeiten-in-python-mit-pfaden-teil-1/
#############################################################################################################
import os

# get current working dir -> aktuelles Arbeitsverzeichnis abrufen
path_dir = os.getcwd()  # z.B.: E:\Benutzer\Dropbox\Dropbox\Projekte\Programmierprojekte\Python\Tutorial\Templates
print(path_dir)

# <class 'str'> -> Rückgabety der path_dir Variable
print(type(path_dir))


# Pfad namen erstellen (sauberer Weg mit r vor String)

path_dir: str = r"E:\Benutzer\Dropbox\Dropbox\Projekte\Programmierprojekte\Python\Tutorial\Templates"
ext: str = r"GetWorkingDir_Ex" # Pfad mit r vor dem eigentlich String erlaub Sonderzeichen wie \ die
                                                                        # sonst mit \\ geschrieben werden müssten zu vernachlässigen
                                                                        # Achtung es darf kein \ am Ende des Strings stehen


# Zusammenführung von Pfaden -> Fügt beide Strings elegant und ohne Fehler zusammen
path_ext = os.sep.join([path_dir, ext])
print(path_ext)

# Unterordner des Pfades anzeigen lassen -> Zeigt und speichert die Unterordner in einer Liste
sub_dir = os.listdir(path_dir) #
print(sub_dir)
print(sub_dir[1])

# Prüfen of Pfad oder File existieren
if os.path.isdir(path_ext): # Wenn der Pfad ein existierender PFad ist
    print("Pfad exisitert")
    if os.path.isfile(path_ext + "/" + "Beispiel.txt"): # Wenn auch noch das File Besipiel Text existiert
        print("File exisitert")

# Dateipfad öffnen
os.startfile(path_ext)

# Programm starten
prgm = r"C:\Program Files (x86)\Battle.net\Battle.net.exe"
os.startfile(prgm)