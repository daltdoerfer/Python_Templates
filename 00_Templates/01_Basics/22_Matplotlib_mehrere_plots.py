# Die Basics für Matplotlib Grafiken
#https://stackoverflow.com/questions/7744697/how-to-show-two-figures-using-matplotlib

# in Terminal: pip install  matplotlib
import matplotlib.pyplot as plt
import numpy as np

f1 = plt.figure(1)

# code for figure 1
x = np.arange(20) # Erstellt Array von 0 bis 19
y = x**2 # x^2
plt.scatter(x,y, c="blue")

# don't write 'plt.show()' here


f2 = plt.figure(2)

# code for figure 2
x = np.arange(20) # Erstellt Array von 0 bis 19
y = x**2 # x^2
plt.scatter(x,y, c="red")


plt.show() # Nur einmal am Ende