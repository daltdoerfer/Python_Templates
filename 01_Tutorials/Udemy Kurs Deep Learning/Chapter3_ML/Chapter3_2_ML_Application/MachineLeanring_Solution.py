import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from tf_utils.dummy_data import regression_data # Importiert aus dem Ordner ..\utils unseren DatenGenerator: dummy_data


def mae(y_true: np.ndarray, y_pred: np.ndarray):
    return np.mean(np.abs(y_true - y_pred)) # Elementweise Subtraktion des Arrays


def mse(y_true: np.ndarray, y_pred: np.ndarray): # Sensibel für große Abweichung der Fehler (da quadratisch mit einfliesst)
    return np.mean(np.square(y_true - y_pred)) # Elementweise Subtraktion des Arrays

# Beispiel mse und mae mit 2 Werten
# y_true = [1, 2]
# y_pred = [1, 2]
# diff = [1-0.5 , 2-3] = [0.5, 1]
# square = diff^2 = [0.25, 1]
# mean = [(0.25+1) /2] = [0.625]


if __name__ == "__main__":
    x, y = regression_data()
    x = x.reshape(-1, 1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    regr = LinearRegression()
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_test)

    r2_score = regr.score(x_test, y_test)
    mae_score = mae(y_test, y_pred)
    mse_score = mse(y_test, y_pred)

    print(f"R2-Score: {r2_score}")
    print(f"MAE: {mae_score}") # Bester Fehlerwert wäre beim MAE 0 , der schlechteste bei unendlich
    print(f"MSE: {mse_score}")  # Bester Fehlerwert wäre beim MAE 0 , der schlechteste bei unendlich

    plt.scatter(x, y)
    plt.plot(x_test, y_pred)
    plt.show()