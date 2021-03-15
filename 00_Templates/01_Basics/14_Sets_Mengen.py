# Sets (Mengen)

familie_mutter = {'angelika','petra','horst'} # Deklaration einer Menge
familie_vater =  {'dieter','anne','lothar', 'horst'}

print('dieter' in familie_mutter) # Befindet sich dieter in der Menge "familie_mutter"
print('dieter' in familie_vater)

familie = familie_mutter | familie_vater # Vereinigung von Mengen
print(familie)

namens_test = familie_mutter & familie_vater # Zeigt die gemeinsame Menge von den Sets an
print(namens_test)

namens_test2 = familie_mutter - familie_vater # Wir löschen aus Menge A alles was in Menge B ebenfalls vorhanden ist
print(namens_test2)

namens_test3 = familie_mutter ^ familie_vater # XOR -> Alles gemerged was in einer aber nicht in der anderen ist. Wenn 2 mal vorkommt dann fliegn beide raus
print(namens_test3)


#----------------------------- Set Comprehension (äquivalent zu Listen Comprehension nur mit {}  --------------------
familie2 = {person for person in familie_mutter | familie_vater} # Merged familie_mutter und familie_vater. Gleich wie familie = familie_mutter | familie_vater
print('familie2', familie2)

familie3 = {person for person in familie_mutter + familie_vater} # + macht gleiches wie |
print('familie3', familie3)