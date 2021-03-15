import pandas as pd #(Pandas ist so etwas wie excel in Pyhton)
from sklearn.datasets import load_boston
import numpy as np
import matplotlib.pyplot as plt

'''
###############################################################
 Load Dataset
 ##############################################################
'''
dataset = load_boston()

#print(dataset)
x = dataset.data
y = dataset.target

df = pd.DataFrame(dataset.data, columns = dataset.feature_names)
print(df.head)

'''
###############################################################
Berechnung unserer Linearen Regression 
###############################################################
'''
# Berechnung Steigung (m)
def compute_slope(x, y, x_mean, y_mean):
    frac1 = sum([(x[i] - x_mean)*(y[i] - y_mean) for i in range(len(x))])
    frac2 = sum([(x[i] - x_mean)**2 for i in range(len(x))])
    slope = frac1 / frac2
    return slope

# Compute intercept (b)
def compute_intercept(x_mean, y_mean, slope):
    intercept = y_mean - slope * x_mean
    return intercept

# Berechnung y = m*x+b
def compute_regression(x, slope, intercept):
    regression_line = [slope * x[i] + intercept for i in range(len(x))] # Prediction unseres Modells oder auch y_dach
    return regression_line

# Berechnung der Streuung des Regressionsmodells
def compute_r2(y, y_mean, regression_line):
    frac1 = sum([(y[i] - regression_line[i])**2 for i in range(len(y))])
    frac2 = sum([(y[i] - y_mean)**2 for i in range(len(y))])
    r2 = 1 - (frac1/frac2)
    return r2

'''
###############################################################
 Split Data in Train and Testset
###############################################################
'''
np.random.seed(42) # Spezifische Random Verteilung bei Permutation

x = dataset.data[:, 6]# Alle Zeilen jedoch nur Feature von  1.Spalte (Alter)
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
 Training und Testing
###############################################################
'''
def train_model(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    m = compute_slope(x, y, x_mean, y_mean)
    b = compute_intercept(x_mean, y_mean, m)
    print("Finished Training!")
    print("With Params: ", m, "and b: ", b)
    regression_line = compute_regression(x, m, b)
    r2 = compute_r2(y, y_mean, regression_line)
    print("With R2: ", r2)
    return m, b

def test_model(x, y ,m ,b):
    y_mean = np.mean(y)
    regression_line = compute_regression(x, m, b)
    r2 = compute_r2(y, y_mean, regression_line)
    print("Finished Testing!")
    print("With R2: ", r2)
    return r2

m, b = train_model(x_train, y_train)
r2_test = test_model(x_test, y_test, m , b)

'''
###############################################################
 Start Plotting
###############################################################
'''
LB = int(np.floor(np.min(x))) - 5 # Lower Bound
UB = int(np.floor(np.max(x))) + 5 # Upper Bound

line = [m * i + b for i in range(LB, UB)]
line_2 = [m * i + b for i in [LB, UB]]

print(line)
print(line_2)

plt.scatter(x_test, y_test, color="blue") # Plottet alle Testpunkte
plt.plot([LB, UB], line_2,color="red")
#plt.plot(range(len(line)),line,color="red")
plt.show()