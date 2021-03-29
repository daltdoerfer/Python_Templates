# https://docs.python.org/3/library/importlib.html

import importlib.util
spec = importlib.util.spec_from_file_location("module.name", "./test_modul.py")
foo = importlib.util.module_from_spec(spec)

spec.loader.exec_module(foo) # Lädt das Modul.Macht Methoden Callbar. Führt das Skript jedoch auch von Anfang bis Ende aus

foo.func(2,2) # Ruft die Funktion func aus dem Modul

foo.test_1() # Ruft die Funktion test_1 aus dem Modul auf

