# Supervised Leanring Sklearn-Package
#Load Iris Dataset https://scikit-learn.org/stable/datasets/index.html
import numpy as np
from sklearn import datasets

# Load Dataset witth first 2 Features
iris = datasets.load_iris() # Lädt Dictionary mit vielen Werten darunter auch die Arrays "data" und "target"
x = iris.data[:,:2] # Nimmt alle Zeilen und ausgewählte Spalten von Index 0 bis 1 (exclusive 2)
y = iris.target

print(x)
print("\n")
print(y)


# Dataset Variables
num_samples = x.shape[0] # Anzahl Zeilen
num_features = x.shape[1] # Anzahl spalten
num_classes = 3 # kommt aus Anzahl der Klassendefinition in y = iris.target
test_size =  20
train_size = num_samples - test_size


print(num_samples)

# Split Data in Train and Testset
indizes = np.random.permutation(num_samples) # Permutation vertauscht Werte -> gibt Array der größe "num_samples" mit vertauschten Indizes zurück. https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.permutation.html
print(indizes)

# Diese Daten gehen ins Trainingsset
x_train = x[indizes[:-20]] # Nimmt alle  Werte die den vertauschten Indizes hinterlegt sind. Jedoch nur die ersten 130 der 150 Werte, da [:-20]
y_train = y[indizes[:-20]]

# Diese Daten gehen ins Testset
x_test = x[indizes[-20:]]
y_test = y[indizes[-20:]]

# Training Size
print(x_train.shape)
print(y_train.shape)

# Testing Size
print(x_test.shape)
print(y_test.shape)