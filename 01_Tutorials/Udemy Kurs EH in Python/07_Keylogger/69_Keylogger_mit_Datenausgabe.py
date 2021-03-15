"""
Linux:
    apt-get update
    apt-get install python3-pip
    pip3 install keyboard

"""
import keyboard

with open("./log.txt", "w", encoding="utf-8") as file:
    print(file)
    file.write("Log Start: \n")

keyboard.unhook_all() # Letzten Hook beenden

def on_key(key):
    print(key)
keyboard.hook(on_key) # Hook starten - Problem Skript arbeitet einmal durch und gut -> File wird vor Regisrierung schon wieder geschlossen -> Das liegt an dem "with Open"