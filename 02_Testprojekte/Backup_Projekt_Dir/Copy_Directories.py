import os
import shutil
from datetime import datetime

# L2cc
src = fr"C:\02_Projekte\DAIMLER\UWK\001_GIT\eATS\eats20_sw\Funct_tl\L2\L2cc"
dst_dir = fr"C:\02_Projekte\DAIMLER\UWK\002_Aufgaben\eATS\01_UWK_Modekonzept_L2cc\02_Modell_Backup"

now = datetime.now()  # current date and time
date_time = now.strftime("%Y%d%m")
#print("date: ", date_time)

new_folder = fr"{date_time}_VXX_Kommentar"

dst = os.sep.join([dst_dir, new_folder])
print(dst)


# Prüfen of Pfad oder File existieren
if not os.path.exists(dst):
    print(rf"Copy wird in neues DIR erstellt: {dst}")
    os.makedirs(dst)
    #shutil.copytree(src, dst)

    # Files aus folgender Liste
    file_list = ["L2cc_e1.dd", "L2cc_e1.mdl"]

    for file in file_list:
        src_file = os.sep.join([src, file])
        shutil.copyfile(src_file, dst)


else:
    print("ERROR: Pfad exisitert bereits")






# L2mi