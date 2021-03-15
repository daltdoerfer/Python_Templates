import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def loadCSV(filename):
    f = open(filename)
    data = np.loadtxt(f, delimiter=',')
    X = data[:, 1:]
    y = data[:, 0]
    return X, y

def error(w, X, y):
    N = y.shape[0]
    assert X.shape[0] == N
    wrong = 0.0
    for i in range(N):
        prediction = np.dot(w, X[i, :])
        if prediction * y[i] <= 0.0:
            wrong += 1
    return wrong / N

X, y = loadCSV("banana.csv")
N = X.shape[0]
X_train = X[0:N//2, :]
y_train = y[0:N//2]
X_test = X[N//2:N, :]
y_test = y[N//2:N]

ks = [1, 3, 5, 7, 9, 19, 29, 49, 99, 199, 299, 499, 999]

for k in ks:
    model = KNeighborsClassifier(k)
    model.fit(X_train, y_train)
    print("[" + str(k) + "-NN]  training error:" + str(1 - model.score(X_train, y_train)) + "  test error: " + str(1 - model.score(X_test, y_test)))


#matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00'])

# mesh resolution
h = 0.05

for k in ks:
    model = KNeighborsClassifier(k)
    model.fit(X_train, y_train)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
    y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])

    # put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # range and decoration
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("k = " + str(k))

plt.show()