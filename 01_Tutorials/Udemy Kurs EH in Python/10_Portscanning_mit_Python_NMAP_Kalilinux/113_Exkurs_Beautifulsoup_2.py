from bs4 import BeautifulSoup

doc = """
<article from="2018-02-02">
    <heading>Große Feier in Berlin</heading>
    <content author="Max Müller">
    
    </content>
</article>
<article from="2018-02-03">
    <heading></heading>
    <content author="Monika Mustermann">
        
    </content>
</article>
"""

d = BeautifulSoup(doc, "html.parser") # Dokument einlesen

print(d.select("article")) # Anzeigen der Liste von Vorhandenen Artikeln
article = d.select("article")[0] # Zugriff auf erstes Element des Artikel

attr = article.attrs["from"] # Greife auf das Attribut "from" zu: '2018-02-02'
print(attr)

uberschrift = article.select("heading")[0] # # Zugriff auf erstes Element von Heading
print(uberschrift)

text = article.select("heading")[0].text # # Zugriff auf Text des ersten Element von Heading -> 'Große Feier in Berlin'
print(text)


attr_specified = d.select("article[from='2018-02-03']") # Suche alle Elemente des Typs article mit spezifischem Attribut
print(attr_specified)
