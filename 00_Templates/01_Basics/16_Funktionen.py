# Eigene Funktionen erstellen

#---------- Deklarationen der Funktionen------------------
def func(a,b, c=None):
    print('Funktion 1')
    print('A:',a)
    print('B:', b)
    print('C:', c)

def func_2(a=None,b=None,c=None): # Keine Übergabe von Parameten über None
    print('Funktion 2')
    print('A:', a)
    print('B:', b)
    print('C:', c)

def func_3(a,b): # Keine Übergabe von Parameten über None
    print('Funktion 3')
    val = a * b
    return val, a, b # Es können einzelne oder mehrere Werte zurückgegeben werden

def func_4(a,b,reverse=False): # Konkartination zweier Wörter mit +
    print('Funktion 4')
    if not reverse:
        return a+' '+b
    else:
        return b + ' ' + a



#-------- Aufrufe der Funktionen--------------------------

func(1,2)
func_2(c=1) # Nur c deklarieren a und b bleiben auf default = None
# func_2(a=1, 2, c=1) # Diese Funktion funktioniert nicht, da er 2 nicht automatisch als b erkennt

wert1,wert2,wert3 = func_3(3,2)
print(wert1, wert2, wert3)

wert1,wert2,_ = func_3(3,2)
print(wert1, wert2, )

print(func_4('Hallo','Welt',reverse=False))
# print(func_4(a='Hallo',b='Welt')) # Alternativ