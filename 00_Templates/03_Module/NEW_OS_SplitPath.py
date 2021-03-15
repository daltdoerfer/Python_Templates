import os

os.path.split

# get current working dir -> aktuelles Arbeitsverzeichnis abrufen
path_dir = os.getcwd()  # z.B.: E:\Benutzer\Dropbox\Dropbox\Projekte\Programmierprojekte\Python\Tutorial\Templates
print(path_dir)

split_path = os.path.split(path_dir)
print(split_path)
print(len(split_path))


################################################################
# Kompletten Pfad in Directory und Filename Trennen
################################################################
dir_file = r"C:\03_Programming\Python\01_Testprojekte\Projekt Generate Exe\Test.py"
print(dir_file)

# Als Tuple ausgeben
split_path = os.path.split(dir_file)
print(split_path)

# Einzeln Ausgeben
dir, name = os.path.split(dir_file)
print(dir)
print(name)