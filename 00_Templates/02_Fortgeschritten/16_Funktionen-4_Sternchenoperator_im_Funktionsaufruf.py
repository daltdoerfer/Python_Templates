# Verwendung von Matplotlib

import matplotlib.pyplot as plt
# %matplotlib inline
#%matplotlib --list

def myplot(daten,*args, **kwargs):
    print('Plotte ', daten, args, kwargs) # mit args -> Tupel und kwargs -> Dictionary
    #plt.plot(daten) #Plotte ohne weitere Argumente
    plt.plot(daten,*args, **kwargs) # Funktionseingang wird durchgeroutet auf plotFunktion (Wichtig geht nicht ohne Sternchenoperatoren!!!)
    plt.show()


myplot([5, 7, 2, 5, 34, 63, 23, 66, 65], 'o-', color='red') # Man könnte Colour auch weglassen
plt.show()


def myplot_2(daten,*args, **kwargs):
    print('Plotte ', daten, args, kwargs)
    if 'color' in kwargs:
        plt.plot(daten,*args, **kwargs) # Funktionseingang wird durchgeroutet auf plotFunktion (Wichtig geht nicht ohne Sternchenoperatoren!!!)
    else:
        plt.plot(daten, *args, **kwargs, color='pink')

myplot_2([5, 7, 2, 5, 34, 63, 23, 66, 65],'o-') # Man könnte Colour auch weglassen
plt.show()