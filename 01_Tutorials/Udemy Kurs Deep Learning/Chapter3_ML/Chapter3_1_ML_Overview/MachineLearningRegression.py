import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from tf_utils.dummy_data import regression_data # Importiert aus dem Ordner ..\utils unseren DatenGenerator: dummy_data


if __name__ == "__main__":

    x, y = regression_data()

    x = x.reshape(-1, 1) # Macht aus dem Vektor (100, ) den Vektor (100, 1) # https://stackoverflow.com/questions/18691084/what-does-1-mean-in-numpy-reshape

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3) # Train-Test Split der Daten

    regr = LinearRegression()
    regr.fit(x_train, y_train) # Training
    score = regr.score(x_test, y_test)
    print(f"R2-Score: {score}")
    print(f"Coefs: {regr.coef_}") # Ausgabe Steigung
    print(f"Intercept: {regr.intercept_}")  # Ausgabe y-Achsenabschitt

    y_pred = regr.predict(x_test) # Prediction für Testset


    plt.scatter(x, y)
    plt.plot(x_test, y_pred)
    plt.show()