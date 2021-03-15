
""" Algorithmus übersicht (Pseudocode)
 (1) Funktion für Nearest Neighbour:
     knn (k=3, dataset, new_point) , mit k=3 nächsten Nachbarn aus dataset mit Newpoint -> Winner
 (2) neigh_distances = euclid(dataset) , Funktion mit Abstand auf dataset angewandt
 (3) sorted_neigh_distances = neigh_dist_sort() , Funktion die die Nachbarn sortiert.
 (4) k_nn = sorted_neigh_distances [0....k-1] , Teileliste der wirklich nächsten Nachbarn
 (5) class = winner(k_nn) , Entscheidung der klasse
"""

#------------------Erzeugung eines normalverteilten 2-D Dataset für 3 verschiedene "Klassen"--------------------------
import numpy as np

def generate_dataset():
    cov = np.array([[1,0], [0,1]]) # Kovarianz-Matrix (Beschreibt lineare Abhängigkeit der einzelnen Variablen X, Y) https://studyflix.de/statistik/kovarianz-1547
    print("Covarianzmatrix:")
    print(cov)

    # Draw random samples from a multivariate normal distribution.  https://numpy.org/doc/stable/reference/random/generated/numpy.random.multivariate_normal.html
    # numpy.random.multivariate_normal(mean, cov, size=None, check_valid='warn', tol=1e-8)
    data1 = np.random.multivariate_normal(np.array([0,0]), cov, 10)
    data2 = np.random.multivariate_normal(np.array([-10, 4]), cov, 16)
    data3 = np.random.multivariate_normal(np.array([10, 10]), cov, 13)
    print("Data1:")
    print(data1)

    data = np.concatenate((data1, data2, data3), axis = 0) # Join a sequence of arrays along an existing axis.
    classes = np.array([0 for i in range(10)] + [1 for i in range(16)] + [2 for i in range(13)]) # Zuweisung an jeweilige Klasse. Wir deklarieren ja selber dass data1 nur 10 Einträge hat deswegen wird dazu Klasse 0 zugewiesen
    return data, classes

dataset, classes = generate_dataset() # Erzeugte Dataset und Classes mit obiger Funktion

print("Dimensionen")
print(dataset.shape) # Zeigt Dimensionen
print(classes.shape) # Zeigt Dimensionen

print("Sample: x[0], y[0]")
print(dataset[0])
print(classes[0])


import matplotlib.pyplot as plt

def plot_knn(dataset, classes, sample, voted_class, neighbours):
    colors = ["red", "blue", "green"]
    for index, point in enumerate(dataset): # Erstellt eine Liste mit Spalte 1: Counter Vektor -> index und Spalte 2: als Vektor pointer beinhaltet Daten aus Dataset
        #print(index)
        #print(classes[index])
        #print(point[0])
        #print(point[1])
        plt.scatter(point[0], point[1], color=colors[classes[index]])
    plt.scatter(sample[0], sample[1], color="yellow") # zusätzlich unser Sample Point plotten

    for neigh in neighbours: # Nachbarn nochmals hervorheben
        cl = neigh[1] # Klasse
        p = neigh[2] # Dataset Werte (x,y)
        plt.scatter(p[0], p[1], color=colors[cl], s=50)
        plt.plot((p[0], sample[0]),(p[1], sample[1]), color="cyan")
    plt.show()



#------------------Hauptalgorithmus Neares Neigbour--------------------------
def distance(p1,p2): # Hilfsfunktion, welche die Distanz ausgibt
    distance = np.linalg.norm(p1-p2) # Berechnung euklidische Distanz (Beispiel: Satz des Pythagoras in 2-D Raum)
    return distance

def vote(neighbours, num_classes): # Funktion entscheidet am Ende zu welcher Klasse unser Punkt gehört
    # [Distance, class, x1] [1.7, 2, x2] [2.4, 0, x3]
    votes = [0 for i  in range(num_classes)] # erstellt Leere Liste [ 0 0 0 ]
    for neigh in neighbours: # Durchläuft alle Einträge von Neighborss
        cl = neigh[1] # Extrahiert den Klassenwert
        votes[cl] += 1 # Dokumentiert häufigkeit des Auftretens ins votes-Liste
    voted_class = np.argmax(votes) # Gibt Indexstelle des Maximums aus Liste aus
    return  voted_class


def KNN(dataset, classes, K, sample): # Dataset sind unsere Random Werte, Classes ist unsere Klassenvektor entsprechend den Bekannten Daten, K ist Anzahl der Nachbarn, sample ist Beispielpunkt

    num_samples = dataset.shape[0]
    num_features = dataset.shape[1]
    # List with distances from sample to dataset
    #Step0 distances = [0.0 for i in range(num_samples)] # -> List Comprehension. Beispiel leere Liste Alternativ: for loop mit distances.append(0.0)
    #Step1 distances = [distance(sample) for i in range(num_samples)] -> List Comprehension. sample besteht aus 2 Werten (x,y) und dataset[i] sind jeweils x,y-Werte
    #Step2 distances = [(distance(sample, dataset[i]), classes[i], dataset[i]) for i in range(num_samples)] # gibt zusätzlich Distanz, Klasse und Dataset als Tupel aus
    #Step3:
    distances = sorted([(distance(sample, dataset[i]), classes[i], dataset[i]) for i in range(num_samples)]) # Gibt nach distances sortierte Werte aus (kleinste zuerst)

    print("Liste mit Abständen, Klasse und Datset als Tupel")
    print(distances)

    # Wir wollen nur die K nächsten nachbarn
    neighbours = distances[:K] # Neighbours Liste sieht wie folgt aus [distance_min, class_distance_min, dataset_distance_min)
                                                                    # [distance_2nd, class_distance_2nd, dataset_distance_2nd)
                                                                    # [distance_3rd, class_distance_3rd, dataset_distance_3rd)
    print("K nächste Nachbarn als Liste mit Abständen, Klasse und Datset als Tupel")
    print(neighbours)

    voted_class = vote(neighbours, num_classes)

    return voted_class, neighbours


#----------------------------------- Eigentlicher Code---------------------------------
K = 3
num_classes = 3 # Anzahl existierender Klassen
sample = np.array([0, 6])
voted_class, neighbours = KNN(dataset, classes, K, sample)
print(neighbours)

plot_knn(dataset, classes, sample, voted_class, neighbours) # Erstellung der Plots aus obiger Funktion