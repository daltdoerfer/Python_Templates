# https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/
# https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file

import os
import sys
import fileinput

# Pfad namen erstellen (sauberer Weg mit r vor String)

path_dir: str = r"C:\02_Projekte\DAIMLER\UWK\001_GIT\eATS\eats20_sw\Funct_tl\L2\L2_shared"
ext: str = r"L2Config_template_e1.c" # Pfad mit r vor dem eigentlich String erlaub Sonderzeichen wie \ die
                                                                        # sonst mit \\ geschrieben werden müssten zu vernachlässigen
                                                                        # Achtung es darf kein \ am Ende des Strings stehen

# Zusammenführung von Pfaden -> Fügt beide Strings elegant und ohne Fehler zusammen
path_ext = os.sep.join([path_dir, ext])
print(path_ext)


string_dict = {'string1': 'setMonPfcStepInitL2_MTSP(1, 5, progStart);',
               'string2': 'setMonPfcStepInitL2_MTSP(1, 5, progStop);',
               'string3': 'setMonPfcStepL2_MTSP(1, 5, progStart);',
               'string4': 'setMonPfcStepL2_MTSP(1, 5, progStop);'}

zeilen_liste = []


# ----------------------------------------------------
# Folgender CODE ermittelt lediglich die Zeilenzahl
#-----------------------------------------------------
# Durch Values Iterieren
for (k, v) in string_dict.items():

    # opening a text file
    file1 = open(path_ext, "r")

    # setting flag and index to 0
    flag = 0
    index = 0

    print('key: ', k)
    print('value: ', v)

    # Loop through the file line by line
    for line in file1:
        index += 1

        # checking string is present in line or not
        if v in line:
            flag = 1
            break

        # checking condition for string found or not
    if flag == 0:
        print('String', v, 'Not Found')
    else:
        print('String', v, 'Found In Line', index)



    zeilen_liste.append(index)

    # closing text file
    file1.close()

print(zeilen_liste)

# ----------------------------------------------------
# Folgender CODE Erstellt Kopie der Originaldatei mit Replacements
#-----------------------------------------------------
# Read in the file
with open(path_ext, 'r') as file:

    filedata = file.read()

    # Durch Values Iterieren
    for (k, v) in string_dict.items():


        # Replace the target string
        filedata = filedata.replace(v, '/*' + v + '*/')

# Write the file out again
with open(path_ext, 'w') as file:
  file.write(filedata)
