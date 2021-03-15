
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def generate_dataset():
    var = 3
    mean = 1.5
    data = np.random.normal(mean, var, 10) # Letzter Wert -> Anzahl Samples/Punkte
    return data

data = generate_dataset()

plt.scatter(data, [0 for i in range(len(data))])
plt.show()


#Schätzung Mittelwert
def estimate_mean(data):
    mean = np.mean(data)
    return mean

def estimate_std(data):
    std = np.std(data)
    return std

mean = estimate_mean(data)
std = estimate_std(data)

print(f"Mean: {mean}")
print(f"Std: {std}")

# Probabilty Density Funktion -> Dichtefunktionen bestimmen
real_pdf = [norm.pdf(x, 1.5, 3) for x in np.arange(-9, 11, 0.01)] # Dichtefunktion auf Basis unsereres erstellten Datensatzes mit bekanntem mean und std
estimate_pdf = [norm.pdf(x, mean, std) for x in np.arange(-9, 11, 0.01)] # Dichtefunktion auf Basis der aus dem Datensatz ermittelten Daten

plt.scatter(np.arange(-9, 11, 0.01), real_pdf, color="red", s=4)
plt.scatter(np.arange(-9, 11, 0.01), estimate_pdf, color="blue", s=4)
plt.legend(["Y", "$\hat{Y}"])
plt.show()


for num_samples in range(10, 11000, 1000):
    data = np.random.normal(1.5, 3, num_samples)  # Letzter Wert -> Anzahl Samples/Punkte
    mean = estimate_mean(data)
    std = estimate_std(data)
    real_pdf = [norm.pdf(x, 1.5, 3) for x in np.arange(-9, 11, 0.01)]  # Dichtefunktion auf Basis unsereres erstellten Datensatzes mit bekanntem mean und std
    estimate_pdf = [norm.pdf(x, mean, std) for x in np.arange(-9, 11, 0.01)]  # Dichtefunktion auf Basis der aus dem Datensatz ermittelten Daten

    plt.scatter(np.arange(-9, 11, 0.01), real_pdf, color="red", s=4)
    plt.scatter(np.arange(-9, 11, 0.01), estimate_pdf, color="blue", s=4)
    plt.legend(["Y", "$\hat{Y}"])
    plt.title("Num Samples = " + str(num_samples))
    plt.show()

