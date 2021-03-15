# https://www.youtube.com/watch?v=-fzj_nCrh8I&list=PL_tdPUem3eE8NYCIDrQpcqZaLRWtnLj-w&index=6
# Callbacks werden oft bei GUI-Prorammierung verwendet

#-----------------------------------Normaler Callback-------------------------------------
def quadriereplus1(x):
    return (x*x)+1

func = quadriereplus1 # !!!!Kein Funktionsaufruf sondern Funktionsübergabe (Callback-Funktion)
print(func) # Speicherstelle der Funktion

a = func(6)
print(a)

# Map Funktion: map(fcn, *iterable)
b = map(func, [5,6,7,8]) # Wendet Callback Funktion auf jedes Iterable-element (in diesem Fall Listenelement) an

print(b)
print(list(b))

#-----------------------------------Lambda Callback-------------------------------------
# Eine Lambda Funktion ist eine Funktion ohne Namen. Diese wird häufig bei einzeiligen Callback Funktionen verwendet, die nur einmalig ausgeführt werden
print(list(map(lambda x:(x*x)+1,[5,6,7,8]))) # quasi ein Inline Callback

#Alternativ
func_2 = lambda x: x*x+1
print(list(map(func_2,[5,6,7,8]))) # quasi ein Inline Callback