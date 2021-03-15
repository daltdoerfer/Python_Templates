import os

path = r"C:\Users\James\AppData\Roaming\Mozilla\Firefox\Profiles"

profiles = os.listdir(path) # Speichert die Unterordner in einer Liste
print(profiles) # Alle Profile in Liste anzeigen

for element in profiles:
    if element[0] != ".": # Wenn erstes Zeichen kein Punklt (nicht unsichtbar) -> Gilt nur für MAC
        profile = element # Bei mir 1oplyo9s.default-1477335232207
        break;
print(profile)

# Im unterordner befindet sich places.sqlite. Dieese Datei beinhaltet Browser History, Bookmarks etc.

#
# path_file = os.sep.join([path_dir, ext]) # Fügt beide Strings elegeant und ohne Fehler zusamsmen

