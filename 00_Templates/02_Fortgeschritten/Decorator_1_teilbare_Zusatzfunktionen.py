# https://www.youtube.com/watch?v=45QI-XEeue4&list=PL_tdPUem3eE8NYCIDrQpcqZaLRWtnLj-w&index=7
# Dekorateure sind keine Leute die deine Bude einrichten, sondern ein Sprachkonstrukt welches dir in Python erlaubt zusätzliche
# Funktionalitäten an Funktionen dranzuheften - und das auf eine sehr elegante Art und Weise.

#  Problem: Man hat eine Funktion gebaut für plt.plot
#  man würde diese jetzt aber gerne die gleiche Funktion genauso verwenden
#  nur mit .scatter statt .plot

import matplotlib.pyplot as plt

# def myplot_2(daten,*args, **kwargs):
#     print('Plotte ', daten, args, kwargs)
#     if 'color' in kwargs:
#         plt.plot(daten,*args, **kwargs) # Funktionseingang wird durchgeroutet auf plotFunktion (Wichtig geht nicht ohne Sternchenoperatoren!!!)
#     else:
#         plt.plot(daten, *args, **kwargs, color='pink')
#
# myplot_2([5, 7, 2, 5, 34, 63, 23, 66, 65],'o-') # Man könnte Colour auch weglassen
# plt.show()

#-----------------------------Dekorateure-------------------------------------------

# Dekorator erstellen
def debug_decor(func):
    def decorate(*args, **kwargs): # wir definieren im Dekorator noch eine weitere Funktion mit Positional- und Keyword-Argumenten
        print('debug call', func, args, kwargs)   # Erst festlegen was Dekorator machen soll: Ausgabe Text, Funktion, Positional- und Keyword-Argumenten
        return func(*args, **kwargs) # Eigentliche Funktion aus main loop aufrufen (do_this/do_that) und deren Ergebnis mit returnwert zurückgeben (sonst fehlt das Ergebnis der Funktion!!!
    return decorate # Funktion nochmal zurückgeben damit diese in debug_decor() ebenfalls vorhanden ist


@debug_decor # Aufruf des Dekorators für die Funktion do_this.
#@decorator_2 # Mehrere Dekoratoren können für eine Funktion angwandt werden
def do_this(a,b): # Funktion
    return a+b

@debug_decor # Aufruf des Dekorators für die Funktion do_that.
def do_that(b,a): # Funktion
    return b*a


print(do_this(5,6))
print(do_that(3,3))