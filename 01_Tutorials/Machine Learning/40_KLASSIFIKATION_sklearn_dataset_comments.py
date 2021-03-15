# Supervised Leanring Sklearn-Package
#Load Iris Dataset https://scikit-learn.org/stable/datasets/index.html
import numpy as np
from sklearn import datasets

# Load Dataset witth first 2 Features
iris = datasets.load_iris() # Lädt Dictionary mit vielen Werten darunter auch die Arrays "data" und "target"
x = iris.data[:, :2] # Nimmt alle Zeilen und ausgewählte Spalten von Index 0 bis 1 (exclusive 2)
y = iris.target

print("Iris Dataset:")
print(iris)
print("X:")
print(x)
print("Y:")
print(y)


# Dataset Variables
num_samples = x.shape[0] # Anzahl Zeilen
num_features = x.shape[1] # Anzahl spalten
num_classes = 3 # kommt aus Anzahl der Klassendefinition in y = iris.target
test_size = 20
train_size = num_samples - test_size

#print(num_samples)

# Split Data in Train and Testset
indizes = np.random.permutation(num_samples) # Permutation vertauscht Werte -> gibt Array der größe "num_samples" mit vertauschten Indizes zurück. https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.permutation.html
#print(indizes)

# Diese Daten gehen ins Trainingsset
x_train = x[indizes[:-20]] # Nimmt alle  Werte die den vertauschten Indizes hinterlegt sind. Alle bis auf die letzen 20 [:-20]
y_train = y[indizes[:-20]]
print("Train X")
print(x_train)
print("Train Y")
print(y_train)


# Diese Daten gehen ins Testset
x_test = x[indizes[-20:]] # Nimmt alle  Werte die den vertauschten Indizes hinterlegt sind. Nur die letzten 20 [-20:]
y_test = y[indizes[-20:]]
print("Test X")
print(x_test)
print("Test Y")
print(y_test)

# Training Size
#print(x_train.shape)
#print(y_train.shape)
# Testing Size
#print(x_test.shape)
#print(y_test.shape)

###########################################################################################################################################
# ------------------------------------------------------------------Modell-----------------------------------------------------------------
###########################################################################################################################################
# https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
from sklearn.neighbors import KNeighborsClassifier

neighbors = [i for i in range (1,11)] # [1,2,3....,10]
weights = ["uniform", "distance"]

# 10 x 2 = 20 Modelle zum testen mit Testdatensatz
for neighbor in neighbors:
    for weight in weights:

        knn = KNeighborsClassifier(n_neighbors=neighbor, weights=weight) # Aufruf des Konstruktors -> knn ist das Objekt
        knn.fit(x_train, y_train) # Trainingsfunktion mit Trainingsinformationen
        score = knn.score(x_test, y_test) # Bewertung für Testdatensatz. -> Genauigkeit (Accurcy). Wert zwischen 0 und 1
        print("Score for Setup: ", neighbor, " N,", weight, " W - Score = ", score)

# Use "best Setup" -> Gewählt aus höchstem Score der obigen Print Werte
best_neighbor = 3
best_weight = "uniform"

knn = KNeighborsClassifier(n_neighbors=best_neighbor, weights=best_weight)
knn.fit(x_train, y_train) # Trainingsfunktion mit Trainingsinformationen

pred = knn.predict(x_test) # Vorhersagen aus den Testparametern
pred_prob = knn.predict_proba(x_test) # Zu wieviel % ist er sich sicher.

print("Predictios vs. Classes")
print("Pred: ", pred)
print("Class:", y_test)
print("\nPredictios Probs:")
print(pred_prob)

###########################################################################################################################################
# ------------------------------------------------------------------Visualisierung-----------------------------------------------------------------
###########################################################################################################################################
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

cmap_light = ListedColormap(['#FFAAAA', '#AAAAFF', '#AAFFAA']) # Farben definieren

def make_meshgrid(x, y):
    x = np.arange(x.min()-1, x.max()+1, 0.05) # Erzeugt Array von min bis max mit Schrittweite 0.05
    y = np.arange(y.min()-1, y.max()+1, 0.05)  # Erzeugt Array von min bis max mit Schrittweite 0.05
    xx, yy = np.meshgrid(x,y) # Bildet Kombination der Wertepaare
                              # xx ist der komplette Vektor x der in y0 Zeilen geschrieben wird
    print("Vector-X")
    print(x)
    print("Vector-Y")
    print(y)
    print("Meshgrid-XX")
    print(xx)
    print("Meshgrid-YY")
    print(yy)

    return xx, yy

def plot_contours(ax, clf, xx, yy, **params):

    print("ravel XX & YY")
    print(xx.ravel()) # np.ravel(x) is equivalent to reshape(-1, order=order) macht aus Matrix einfaches Array.
    print(yy.ravel())
    a= np.c_[xx.ravel(), yy.ravel()] # np.c_ -> arrays will be stacked along their last axis after being upgraded to at least 2-D with 1's post-pended to the shape https://stackoverflow.com/questions/10894323/what-does-the-c-underscore-expression-c-do-exactly
    print(a.shape)
    Z = clf.predict(a) # predict(X) -> Perform classification on samples in X. Ist eine sklearn-Funktion!!!

    #print("Z Pre Shape: ", Z)
    Z = Z.reshape(xx.shape) #
    # print("Z Post Shape: ", Z)
    ax.contourf(xx, yy, Z, **params) #Bedingung Dimension xx und yy müssen gleich sein wie Z -> https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.contourf.html


def plot_knn(x_train, y_train, x_test, y_test): # Plottet die Punkte o für Testing und * für Testpunkte
    colors = ["red", "blue", "green"]
    fig, ax = plt.subplots() # returns plot information

    X0 = x_train[:,0]
    X1 = x_train[:,1]
    xx, yy = make_meshgrid(X0, X1)
    print(xx.shape)
    print(yy.shape)
    plot_contours(ax, knn, xx, yy, cmap=cmap_light, alpha=0.5) # cmap-> farben, alpha -> Transparenz

    for index, point in enumerate(x_train):
            #                                Farbe der Klasse z.B. 3  , Punkt mit Größe 20
            plt.scatter(point[0],point[1], color=colors[y_train[index]], marker="o", s=20.0)
    for index, point in enumerate(x_test):
            plt.scatter(point[0],point[1], color=colors[y_test[index]], marker="*", s=20.0)
    plt.show()

plot_knn(x_train, y_train, x_test, y_test)