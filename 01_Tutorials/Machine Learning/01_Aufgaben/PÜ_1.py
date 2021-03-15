#https://www.udemy.com/course/machine-learning-grundlagen-mit-python-inkl-ai-einfuhrung/learn/quiz/4411854#overview

import numpy as np
import matplotlib.pyplot as plt

y = np.random.randint(low=1, high=30, size = 30)
x = range(len(y)) # Erzeugt liste mit Indizes passend zur länge von x
print(y)
print(x)

# plt.scatter(data_x,data_y) # Punktewolke
plt.scatter(x,y, c ='b') #Scatter -> Punkte (blau)

y_mean = np.mean(y)
print(y_mean)
print(np.max(x))
print(np.min(x))

plt.plot((np.min(x),np.max(x)),(y_mean,y_mean), c='y') # Plot einer Geraden (gelb): plt.plot((x1,x2),(y1,y2), c='y')

plt.xlabel('x-Werte')
plt.ylabel('y-Werte')

plt.show()