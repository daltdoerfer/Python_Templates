PY2EXE_V1.6

Aufgabe des Programmes: Erstellen einer .exe aus einer .py Datei mithilfe des Moduls Pyinstaller


Eine übersicht über Pyinstaller bekommen man über den Konsolenbefehl
>> pyinstaller -h

Manuelle Bedienung:
Folgender Konsolen-Befehl, kann ausgeführt werden, um eine Exe zu erstellen
>> <Pfad zur Src-Datei> pyinstaller --onefile -w <Src-Dateiname>


TODO:
.ico muss in gleichem Ordner liegen wie die Exe, sonst findet dieser die Datei nicht -> Pfadangabe nochmals überprüfen, ob ganzer Pfad angegeben werden kann