# https://www.youtube.com/watch?v=5vyUlKahAlc&list=PL_tdPUem3eE8NYCIDrQpcqZaLRWtnLj-w&index=11
# Erweiterung vcon Listen Comprehension Zusatz

# Einfacher Filter
l = [4,6,8,5,3,6,9,4,2]
nl = [x for x in l if x > 3]
print(nl)
print(tuple(nl)) # Umwandlung in Tupel ()
print(set(nl)) # Umwandlung in Set {}

c = [4,6,2,8,4,6,7,8]
d = [(x,x**x) for x in c] # Schreibt Tupel in eine Liste mit Tupel Inhalt (x,x^x) für aktuelle Iteration
print(d)
e = dict(d) #Umwandlung in Dictionary mit {key: value} -> Wichtig Keys sind unique -> Darf nicht 2x der selbe Key vorkommen
# e = dict([(x,x**x) for x in c])
print(e)