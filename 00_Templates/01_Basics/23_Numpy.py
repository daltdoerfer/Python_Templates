# Basics für Numerical-Pyton (Numpy)  Listen und Funktionen https://www.youtube.com/watch?v=Ti-uDPHG6OM
# Terminal: pip install numpy
# https://numpy.org/doc/stable/reference/

import numpy as np
from numpy.linalg import eigvals

data = [1.0, 2.0, 3.0]
print(data)

data2 = np.asarray(data, dtype=np.float64) # Convert the input to an array.
print(data2)
print(data2.shape) # Dimension angeben
print(data2.dtype) # Datentyp angeben
data2 = data2.astype(np.int8) # Datentyp ändern
print(data2.dtype) # Datentyp angeben

data3 = np.array([1.0, 2.0, 3.0], dtype=np.float64)
print('Example 3')
print(data3)
print(np.max(data)) # Max wert aus Array anzeigen
print(np.min(data)) # Min wert aus Array anzeigen
print(np.argmax(data)) # Index von Max wert aus Array anzeigen
print(np.argmin(data)) # Index von Min wert aus Array anzeigen

data4 = np.zeros(shape=(10), dtype=np.float64)
print(data4)

data5 = np.full(4,255.0, dtype=np.float64) # Erzeugt Array mit 4 Einträgen welche jeweils auf 255.0 gesetzt werden
#print('Example 5')
print(data5)

matrix = np.zeros(shape=(3, 3), dtype=np.int8) # Erzeugt 3x3 Matrix mit int8 Datentyp einträgen (Wert überall 0)
#matrix = np.ones(shape=(3, 3), dtype=np.int8) # Erzeugt 3x3 Matrix mit int8 Datentyp einträgen (Wert überall 0)
print(matrix)

liste_von_matrix = matrix.reshape(9) # 3x3 Matrix wird in 1D-Array umgewandelt
print(liste_von_matrix)

liste_von_matrix_2 = matrix.reshape(9,1) # 3x3 Matrix wird in 2D-Array ("[[ ]]" ) umgewandelt mit Dimension reshape(<Zeilenzahl>,<Reihenzahl>)
print(liste_von_matrix_2)

print(matrix.shape) # Größe einer Matrix (Dimension) ausgeben
print(matrix.dtype) # Datentyp einer Matrix ausgeben

matrix_2 = np.array([[1,2,3], [7, 1, 9], [4, 5, 3]], dtype=np.int8)
matrix_transpose = np.transpose(matrix_2)
print(matrix_transpose)

matrix_invers = np.invert(matrix_2)
print(matrix_invers)

# Eigenwert mit Linalg bestimmen
EW = np.linalg.eigvals(matrix_2)
print('Example Eigenwert')
print(EW)

EW, EV = np.linalg.eig(matrix_2)
print(EW)
print(EV)

# Matrix Multiplikation
matrix_3 = np.array([[2,1], [3, 4]], dtype=np.int8)
matrix_4 = np.array([[2,1], [1, 1]], dtype=np.int8)
print(np.dot(matrix_3, matrix_4)) # Normale Matrixmultiplikation

# Matrix Punktweise Multiplikation
print(matrix_3 * matrix_4)


# Quadratische Funktion mit 20 Einträgen
x = np.arange(20) # Erstellt Array von 0 bis 19
y = x**2 # x^2


# Linspace Beispiel: Erzeugt Array mit gleich aufgeteilten Werten in einem Bereich
my_array = np.linspace(start=0.0, stop=20 , num=130)
print(my_array)

# Beispiel Indizes Random Permutation: Permutation vertauscht Werte -> gibt Array der größe "num_samples" mit vertauschten Indizes zurück. https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.permutation.html
num_samples = 10
indizes = np.random.permutation(num_samples)
print(indizes)

# Beispiel Summensymbol
y_true = [1, 2, 3, 4]
y_pred = [1.1, 2.1, 3.1, 4.1]

def mse(y_true, y_pred):  # Mean Squared Error
    n = len(y_true)
    return (1/n)*np.sum((y_true[i]-y_pred[i])**2 for i in range(n))

def mae(y_true, y_pred):  # Mean Absolute Error
    n = len(y_true)
    return (1/n)*np.sum(np.abs(y_true[i] - y_pred[i]) for i in range(n)) # Bald muss np.sum(np.fromiter()) anstelle von np.sum() verwendet werden

error1 = mse(y_true, y_pred)
error2 = mae(y_true, y_pred)

print(error1)
print(error2)