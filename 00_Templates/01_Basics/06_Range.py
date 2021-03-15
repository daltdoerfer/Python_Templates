# Range Anweisungen

# range(start, stop, step)
# range(0,3,1) -> 0, 1, 2
# range(3) -> Beginnt bei 0 bis 2

#Beispiel 1:
for i in range(10, 21, 2): # Man muss Stop + 1 eingeben um bis Stop zu gehen
    print(i) # 10, 12, 14, 16, 18, 20


#Beispiel 2:
my_list = []

for i in range(10):
    my_list.append(i)

print(my_list)