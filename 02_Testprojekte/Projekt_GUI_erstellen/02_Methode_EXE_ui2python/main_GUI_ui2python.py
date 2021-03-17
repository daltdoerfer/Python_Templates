#PyQt5 Designer um GUI zu erstellen
#Folgender Code wandelt erstellte GUI von .ui zu .py um.

#Code soll folgende CMD Line ausführen
#pyuic5 –x "filename".ui –o "filename".py

import os
import tkinter as tk
import sys
from datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("%Y%d%m_%H%M%S_")
#print(date_time)

dir_path = os.path.dirname(os.path.realpath(__file__))
print("Directory of source file: ", dir_path)

src_filename = 'UI2PY_1_Button' # Hier muss noch geladen werden
tgt_filename = 'new_GUI'
#tgt_filename = f'{date_time}_new_gui.py' # Name des neu erstellten Zielfiles

def generate_py_GUI():
    command_1 = fr'start cmd /k cd {dir_path}'
    command_2 = f'pyuic5 -x {src_filename}.ui > {date_time}{tgt_filename}.py'
    print(command_1) # CMD Line 1 ausführen
    print(command_2) # CMD Line 2 ausführen
    os.system(command_1)
    os.system(command_2)

generate_py_GUI()
