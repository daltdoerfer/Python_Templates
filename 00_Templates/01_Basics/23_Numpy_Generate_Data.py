import numpy as np
import matplotlib.pyplot as plt

# Datensatz erzeugen mit
np.random.seed(42)

# Toy Dataset
def generate_dataset():
    num_p = 50 # 50 Datenpunkte erzeugen
    cov1 = np.array([[1, 0], # Kovarianzmatrix mit nur Werten auf der Hauptdiagonalen
                     [0, 2]])
    cov2 = np.array([[2, 0], # Kovarianzmatrix mit nur Werten auf der Hauptdiagonalen
                     [0, 1]])
    data1 = np.random.multivariate_normal(np.array([0, 0]), cov1, num_p) # Multivariate Normalverteil -> Keine Standardabweichung sondern Kovarianzmatrix:  Erzeugt x,y Pärchen um Mittelwert [0,0] mit Cov1
    data2 = np.random.multivariate_normal(np.array([2, 2]), cov2, num_p)
    data = np.concatenate((data1, data2), axis=0) # Verkettet beide Datensätze zu einem langen
    classes = np.array([-1 for i in range(num_p)] + [1 for i in range(num_p)])
    return data, classes

x,y = generate_dataset()

plt.scatter(x[:, 0], x[:, 1], c=y) # c=y Bedeutet das die Datenpunktsfarbe jeweilig von der Klasse abhängig sind
plt.show()


# Normalverteilung Datensatz erzeugen

def generate_dataset_Normalverteilung():
    data = np.concatenate((
        np.random.normal(1, 2, n_points), #Mittelwert = 1, std = 2
        np.random.normal(8, 2, n_points) #Mittelwert = 8, std = 2
        ))
    classes = [0 for i in range(n_points)] + [1 for i in range(n_points)]
    return data, classes

n_points = 100
x, y = generate_dataset_Normalverteilung()

plt.scatter(x, [0 for i in range(2 * n_points)], c=y)
plt.show()