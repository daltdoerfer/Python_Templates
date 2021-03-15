# Code soll folgende CMD Line ausführen
# <Pfad zur Src-Datei> pyinstaller --onefile -w <Src-Dateiname>

import os
import tkinter as tk
import sys

opt_arg = 0

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=350, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Upgrade PIP', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 80, window=label1)


dir_path = os.path.dirname(os.path.realpath(__file__))
print("Directory of source file: ", dir_path)

#user_paths = os.environ['PYTHONPATH'].split(os.pathsep) # Aktuelle Working Dir ausgeben
#print(user_paths[0])
filename = 'test.py'

# Optionale Agrgumente
if opt_arg == 1:
    arg = "-w"
else:
    arg = ""

def generate_EXE():
    package = 'numpy'
    command_1 = fr'start cmd /k cd {dir_path}'
    command_2 = fr'pyinstaller --onefile {arg} {filename}'
    print(command_1)
    os.system(command_1)
    os.system(command_2)

generate_EXE()

'''
button1 = tk.Button(text='      Upgrade PIP     ', command=generate_EXE, bg='green', fg='white',
                    font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=button1)

root.mainloop()'''