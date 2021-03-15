# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotting import *

# Sklearn Methoden
from sklearn.datasets import load_digits
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

np.random.seed(42)

# Toy Dataset
def generate_dataset():
    num_p = 50
    cov1 = np.array([[1, 0], [0, 2]])
    cov2 = np.array([[2, 0], [0, 1]])
    data1 = np.random.multivariate_normal(np.array([0, 0]), cov1, num_p)
    data2 = np.random.multivariate_normal(np.array([2, 2]), cov2, num_p)
    data = np.concatenate((data1, data2), axis=0)
    classes = np.array([-1 for i in range(num_p)] + [1 for i in range(num_p)])
    return data, classes

#### SVM mit Kernel:
x, y = generate_dataset()
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.3)

plt.scatter(x_train[:,0], x_train[:,1], c=y_train)
plt.show()

''' Kernels:
	- Man verwendet keine Lineare SVM 
	- Man verwendet einen Kernel:
	der Kernel ist dazu da die Features in einen Höherdimensionalen Raum zu bringen,
	wo wir die Daten Linear Separarieren können !
	-> Nichtlineare Transformation
Vorteil: die Rechnungen bleiben auf dem eigentlichen Featureraum 
-> Man spart extreme Rechenleistung mit den Kernels

Es gibt folgende Kernels (komplexität der Kurve erfassen): 
-rbf (radial basis function)
-linear
-poly (mit Grad)
-sigmoid

Ziel der Kernels: man bringt die Daten die in dieser Dimension nicht linear separierbar sind in eine andere Feature Space in dieser die Daten eventuell linear separierbar sind
'''
#kernel = "rbf"
#kernel = "linear"
kernel = "poly"
#kernel = "sigmoid"

clf = SVC(kernel=kernel)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
score = clf.score(x_test, y_test)

print("Score: ", score)
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))

print(x.shape, y.shape)
print(x_test.shape, y_test.shape)

# Testset
fig, ax = plt.subplots(1, 1)
plt.scatter(x_test[:,0], x_test[:,1], c=y_test)
plot_contours(ax, clf, x_test[:,0], x_test[:,1], cmap=plt.cm.coolwarm, alpha=0.4)
plt.show()

# Alle Daten
fig, ax = plt.subplots(1, 1)
plt.scatter(x[:,0], x[:,1], c=y)
plot_contours(ax, clf, x[:,0], x[:,1], cmap=plt.cm.coolwarm, alpha=0.4)
plt.show()