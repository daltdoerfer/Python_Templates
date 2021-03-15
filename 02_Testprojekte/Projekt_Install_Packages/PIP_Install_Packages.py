import os
import tkinter as tk
import sys


root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=350, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Upgrade PIP', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 80, window=label1)

pydir = os.path.dirname(sys.executable)
print("Directory of installed Python: ", pydir)

#user_paths = os.environ['PYTHONPATH'].split(os.pathsep) # Aktuelle Working Dir ausgeben
#print(user_paths[0])

def installPackage():
    package = 'numpy'
    command = f'start cmd /k {pydir}\\python.exe python -m pip install {package}'
    print(command)
    #os.system(command)



button1 = tk.Button(text='      Upgrade PIP     ', command=installPackage, bg='green', fg='white',
                    font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=button1)

root.mainloop()