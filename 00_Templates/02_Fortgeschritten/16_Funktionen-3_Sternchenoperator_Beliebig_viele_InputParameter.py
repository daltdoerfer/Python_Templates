# https://www.youtube.com/watch?v=iGxZYMpn954&list=PL_tdPUem3eE8NYCIDrQpcqZaLRWtnLj-w&index=4
# Mehrere Parameter gleichzeitig in eine Funktion schicken, obwohl nur ein Eingangsargument

#------------------------------------------------ Fall 1: ohne Sternchenoperator --------------------------------------------------
def echo(a):
    print('Fall 1')
    print('Test', a)

# echo(4,5,6) # So gehts nicht bei obiger Funktion ohne Sternchen
echo((4,5,6)) # Doppelklammer geht

#------------------------------------------------ Fall 2: mit Sternchenoperator --------------------------------------------------
def echo_2(*a): # * für alle positional Parameters
    print('Fall 2')
    print('Test', a)

echo_2(4,5,6) # Parameter werden in Tupel geschrieben
echo_2((4,5,6))

#------------------------------------------------ Fall 3: Named-Arguments/Keyword-Arguments mit Sternchenoperator --------------------------------------------------
def echo_3(*args, **kwargs): # Doppelstern für Keyword-Arguments -> Damit können neben mehreren Zahlen auch Strings eingelesen werden
    print('Fall 3')
    print(args)
    print(kwargs)

echo_3(4,5,6, c='ein String') # Damit können neben mehreren Zahlen auch Strings eingelesen werden

#------------------------------------------------ Fall 4: Named-Arguments/Keyword-Arguments mit Sternchenoperator --------------------------------------------------
def echo_4(a,*args,c,**kwargs): # Doppelstern für Keyword-Arguments -> Damit können neben mehreren Zahlen auch Strings eingelesen werden

    print('Fall 4')
    print(a) # nur erste Zahl
    print(args) # alle restlichen zahlen oder String ohne Keyword werden auf args gesetzt
    print(c) # nur erster String
    print(kwargs)

echo_4(4,5,6, 'o', c='ein String', keyword='noch ein String') # Damit können neben mehreren Zahlen auch Strings eingelesen werden
