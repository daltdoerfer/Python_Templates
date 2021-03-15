# Erstellen mit Dictionary Comprehension
# List Comprehensions oder Listen-Abstraktionen sind syntaktische Gefüge, die beschreiben, wie vorhandene Listen
# verarbeitet werden sollen, um aus ihnen neue Listen zu erstellen.

studenten = ['jan', 'horst', 'peter']
noten = [1,1,3]

stud_dict = {'jan': 1, 'horst': 1, 'peter': 3}
print(stud_dict)

#stud_dict2 = {key: val for bla in blubb} -> Transformation von zip in Dictionary
stud_dict2 = {key: val for (key, val) in zip(studenten, noten)}
# keys kommen aus Studentenliste
# Vals kommen aus Notenliste

print(stud_dict2)


# Nur zur Anzeige was in zip passiert
neue_liste = list(zip(studenten,noten))
print(neue_liste)