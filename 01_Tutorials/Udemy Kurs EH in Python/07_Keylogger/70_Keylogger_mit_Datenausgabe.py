import keyboard

keyboard.unhook_all() # Letzten Hook beenden

file = open("./log.txt", "w", encoding="utf-8")
file.write("Log Start: \n")

def on_key(key):
    file.write(str(key.__dict__) + "\n") # Objekteigenschaften ausgeben -> Gibt Informatioen aus z.B. über alle Funktionen die Aufrufbar sind
                                         # Sideinformation: Objekteigenschaften ausgeben -> Gibt Informatioen aus z.B. über alle Funktionen die Aufrufbar sind

    '''
    Problem file.write() sagt zu Python schreibe, WANN du es für richtig hälst
    Lösung -> Alles was in Warteschlange ist, soll sofort geschrieben werden -> file.flush()
    '''
    file.flush()
    #print(key)
    #print(key.time) # Aktuelle Uhrzeit

keyboard.hook(on_key) # Hook starten zum aufnehmen aller kommenden Tastenanschläge

keyboard.wait(hotkey="esc") # Loop beenden mit bestimmter Taste
# keyboard.wait() # Loop läuft ewig weiter





