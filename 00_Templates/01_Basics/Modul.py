def func(a,b, c=None):
    print('Funktion 1')
    print('A:',a)
    print('B:', b)
    print('C:', c)

def func_3(a, b):  # Keine Übergabe von Parameten über None
    print('Funktion 3')
    val = a * b
    return val, a, b  # Es können einzelne oder mehrere Werte zurückgegeben werden