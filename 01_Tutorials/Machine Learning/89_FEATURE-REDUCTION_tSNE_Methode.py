# Imports
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict

# Loading the dataset
digits = load_digits(n_class=10)
x = digits.data
y = digits.target
n_samples, n_features = x.shape

print("Samples: ", n_samples)
print("Features: ", n_features)

# PCA Reduction
n_components = 2
pca = PCA(n_components=n_components, copy=True)
pca.fit(x)
transformed_x = pca.transform(x)

# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(transformed_x, y, random_state=42, test_size=0.30)

# Plotting
plt.figure(figsize=(8,8))
colors = {0:"red", 1:"blue", 2:"orange", 3:"yellow", 4:"cyan",
          5:"black", 6:"green", 7:"purple", 8:"pink", 9:"gray"}
labels = [i for i in range(10)]
for index, point in enumerate(x_test):
    plt.scatter(point[0], point[1], color=colors[y_test[index]], label=labels[y_test[index]])
plt.xlabel("x1")
plt.ylabel("x2")
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())
plt.show()

# tSNE Reduction
n_components = 2
tsne = TSNE(n_components=n_components, n_iter=2000)
transformed_x = tsne.fit_transform(x)

# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(transformed_x, y, random_state=42, test_size=0.30)

# Plotting
plt.figure(figsize=(8,8))
colors = {0:"red", 1:"blue", 2:"orange", 3:"yellow", 4:"cyan",
          5:"black", 6:"green", 7:"purple", 8:"pink", 9:"gray"}
labels = [i for i in range(10)]
for index, point in enumerate(x_test):
    plt.scatter(point[0], point[1], color=colors[y_test[index]], label=labels[y_test[index]])
plt.xlabel("x1")
plt.ylabel("x2")
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())
plt.show()