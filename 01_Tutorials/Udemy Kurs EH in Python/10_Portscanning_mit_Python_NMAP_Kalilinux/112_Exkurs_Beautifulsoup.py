from bs4 import BeautifulSoup

doc = """
<p>Ich bin ein <strong>Absatz1</strong></p>
<p>Ich bin ein <strong id="important">Absatz</strong></p>
<p>Ich bin ein <strong class="urgent">Absatz2</strong></p>
<strong class="urgent">Fettschrift</strong> 
"""

print(doc)

d = BeautifulSoup(doc, "html.parser")
print(d)

fa = d.find_all("p") # Gibt ganze Zeile aus in der sich Suchanfrage befindet
print(fa)

#Ansteuerung Elemente/Suche Elemente
# Beispiel 1: macht das gleiche wie Find all
sel = d.select("p")
print("Bsp1: " + str(sel))

#Beispiel 2: Sucht nach Elemtenten -> Zeige nur die strong-Elemente wenn sie sich innerhalb eines p-Elementes befindet
sel = d.select("p strong") #
print("Bsp2: " + str(sel))

#Beispiel 3: nach id Filtern -> Suche nach allen Elementen mit important
sel = d.select("#important") #
print("Bsp3: " + str(sel))

#Beispiel 4: nach Klasse Filtern -> Suche nach allen Klassen-Elementen mit urgent
sel = d.select(".urgent") #
print("Bsp4: " + str(sel))