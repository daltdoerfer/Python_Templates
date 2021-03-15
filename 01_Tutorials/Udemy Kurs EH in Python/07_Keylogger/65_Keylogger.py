"""
Linux:
    apt-get update
    apt-get install python3-pip
    pip3 install keyboard

"""
import keyboard

# Tastenanschläge aufnehmen.
keyevents = keyboard.record(until="esc") # Aufnahme stoppt bei rücken der ESC Taste

for keyevent in keyevents: # Zeile für Zeile Ausgeben
    print(keyevent)

# Interpretierte Tastenanschläge ausgeben -> Funktioniert eher schlecht als recht
keys = keyboard.get_typed_strings(keyevents, allow_backspace = True) # Type Generator Object -> Generator Ist wie eine Liste die generiert wird wenn wir darauf zugreifen

for key in keys:
    print(key)
