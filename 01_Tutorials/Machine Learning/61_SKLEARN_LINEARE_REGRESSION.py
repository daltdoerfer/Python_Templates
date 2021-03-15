from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import numpy as np
'''
###############################################################
 Load Dataset
 ##############################################################
'''

dataset = load_boston()

#print(dataset)
x = dataset.data
y = dataset.target


'''
###############################################################
 Split Data in Train and Testset
###############################################################
'''
np.random.seed(42) # Spezifische Random Verteilung bei Permutation

#x = dataset.data[:, 6]# Alle Zeilen jedoch nur Feature von  1.Spalte (Alter)
x = dataset.data # Alle Zeilen
y = dataset.target # 1-D Vektor

num_samples = len(x) # Oder: x.shape(0)
indizes = np.random.permutation(len(x))
test_size = 100

# Diese Daten gehen ins Trainingsset
x_train = x[indizes[:-test_size]] # Nimmt alle  Werte die den vertauschten Indizes hinterlegt sind. Alle bis auf die letzen 100 [:-100]
y_train = y[indizes[:-test_size]]

print(x_train.shape)
print(x_train)

# Diese Daten gehen ins Testset
x_test = x[indizes[-test_size:]] # Nimmt alle  Werte die den vertauschten Indizes hinterlegt sind. Alle bis auf die letzen 100 [:-100]
y_test = y[indizes[-test_size:]]

'''
###############################################################
 SKLEARN LINEARE REGRESSION
###############################################################
'''

regr = LinearRegression()
regr.fit(x_train, y_train)


print("Coeffs: ", regr.coef_) # Entspricht den Steigungen als Vektor im mehrdimensionalen Raum
print("Intercepts :", regr.intercept_) # Entspricht dem Vector C im mehrdimenstionalen Raum
print("R2 :", regr.score(x_test, y_test)) # Entspricht Score
