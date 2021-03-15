# Zusätzliche Preprocessing und Normalisation Tools in SKLEARN

######################################################################
# Label Encoder: Preprocessing für die Target Werte (y)
# Nur für Klassifikationsdatensets verwendbar
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html
######################################################################
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

# Für Numerische Zahlen
le.fit([1, 2, 2, 6]) # Target Value y

le.classes_ # Listet alle Uniquen Elemente einmalig auf
le.transform([1, 1, 2, 6]) # Transformiert alle Elemente in eine aufsteigende Zahlenreihenfolge beginnend bei 0
le.inverse_transform([0, 0, 1, 2]) # Transformiert die Information zurück

print(le.classes_)
print(le.transform([1, 1, 2, 6]))
print(le.inverse_transform([0, 0, 1, 2]))


# Für String Werte
le.fit(["paris", "paris", "tokyo", "amsterdam"]) # Listet alle Uniquen Elemente einmalig auf
le.transform(["tokyo", "tokyo", "paris"]) # Transformiert alle Elemente in eine aufsteigende Zahlenreihenfolge beginnend bei 0
le.inverse_transform([2, 2, 1]) # Transformiert die Information zurück

print(list(le.classes_))
print(list(le.transform(["tokyo", "tokyo", "paris"])))
print(list(le.inverse_transform([2, 2, 1])))

#################################################################
# Binarize: Preprocessing für Features (x)
# Basierend auf Threshhold werden Features zu 0 oder 1
# Komplexer Wertebereich vereinfachen
# Wichtig bei Estimator die Boolean Random Variables betrachten (z.B. Bernoulli Verteilung)
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Binarizer.html?highlight=binarizer#sklearn.preprocessing.Binarizer
#################################################################


#################################################################
# OneHot-Encoder (siehe Case Study 2)
# Wird eigentlich in NN verwendet um die y-Daten zu preprocessen (in Kategorien einzuteilen) in Kiras gibt es die Funktion ebenfalls, dort heißt diese to_categorical
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder
from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder(handle_unknown='ignore')
X = [['Male', 1], ['Female', 3], ['Female', 2]]
enc.fit(X)

enc.categories_ # Listet alle Möglichkeiten für Klasse 1 (Gender) auf -> (Male, Female) ; ebenso für Klasse 2 -> (1,2,3)
enc.transform([['Female', 1], ['Male', 4]]).toarray() # Weißt der im enc.categories_ gebildeten Datenstring die Werte als Matrix zu -> F
                                                      #  Categories [Female, Male, 1, 2, 3]
                                                    # [Female,1] -> [     1,    0, 1 ,0, 0] = 1x Female, 1*1 ->
                                                    # [Male, 4]  -> [     0,    1, 0 ,0, 0] = 1x Male, 0*4 ->

enc.inverse_transform([[0, 1, 1, 0, 0], [0, 0, 0, 1, 0]]) # Basierend au enc.categories -> [1*male + 1*1] & [ 1*2]
enc.get_feature_names(['gender', 'group']) # Kategoriezuweisung zu enc.categories dType 1 -> male, female und dtype 2 -> 1,2,3

print(enc.categories_)
print(enc.transform([['Female', 1], ['Male', 4]]).toarray())
print(enc.inverse_transform([[0, 1, 1, 0, 0], [0, 0, 0, 1, 0]]))
print(enc.get_feature_names(['gender', 'group']))

# Side Info:  One can always drop the first column for each feature:
drop_enc = OneHotEncoder(drop='first').fit(X)
drop_enc.categories_

drop_enc.transform([['Female', 1], ['Male', 2]]).toarray()

#################################################################
# Ordinal-Encoder (siehe Case Study 2)
#
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder

from sklearn.preprocessing import OrdinalEncoder
enc = OrdinalEncoder()
X = [['Male', 1], ['Female', 3], ['Female', 2]]
enc.fit(X)

enc.categories_ # Listet alle Möglichkeiten für Klasse 1 (Gender) auf -> (Male, Female) ; ebenso für Klasse 2 -> (1,2,3)
enc.transform([['Female', 3], ['Male', 1]]) # Nimmt die Indizes aus enc.categries -> Female wäre auf Index 0 und 3 auf Index 2 -> [0,2]
enc.inverse_transform([[1, 0], [0, 1]])

print(enc.categories_)
print(enc.transform([['Female', 3], ['Male', 1]]))
print(enc.inverse_transform([[1, 0], [0, 1]]))