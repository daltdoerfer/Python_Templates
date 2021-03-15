##########################################################
# Zusammenfassung: Überprüfung aller Regressionsverfahren:
# Lineare Regression
# KNN-Regressor
# Random-Forest Regressor
# Gradient Boosting Regressor
#
# Kommentar:  In diesem File wurde bei allen Verfahren (KNN, Random Forest, Gradient Boosting, SVM)
# Jeweils eine Grid Search  mit 3 Folds gemacht (cv=3) -> Veränderbar
#
# Neuronaler Netze nicht betrachtet , da bisher kein beispiel Vorlag für Regression
##########################################################
import numpy as np
np.random.seed(42)
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import make_scorer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import StandardScaler

#### Helper
def print_grid_cv_results(grid_result):
        print(
                f"Best model score: {grid_result.best_score_} "
                f"Best model params: {grid_result.best_params_} "
        )
        means = grid_result.cv_results_["mean_test_score"]
        stds = grid_result.cv_results_["std_test_score"]
        params = grid_result.cv_results_["params"]

        for mean, std, param in zip(means, stds, params):
                mean = round(mean, 4)
                std = round(std, 4)
                print(f"{mean} (+/- {2 * std}) with: {param}")


#############################################################
#--------------- LOAD DATASET -------------------------
#############################################################
cal_housing = fetch_california_housing()
x = cal_housing.data
y = cal_housing.target

#############################################################
# ------ Splitting der Daten in Trainings und Testset -------
#############################################################
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

#############################################################
# ----------- Normalisieren des Datasets --------------------
# Siehe Lektionen: 104, 105, 106
# Übungen: PÜ_4
#############################################################
scaler = StandardScaler() # StandardScaler bei Normalverteilung der Daten besser als andere Scaler
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

#############################################################
# ---------------------- Metriken ---------------------------
# Siehe Lektionen: 92,93,94
# Übungen: PÜ_4
# Kommentar: R²-Score als Metrik zur Argumentation welches Modell am Besten.
#            Überlegung am Anfang der Aufgabe welche Metrik sinnvoll.
#            r², mae, mse etc.
#############################################################
scoring_metrics = {'r2_score': make_scorer(r2_score)} #

#############################################################
# ---------------------- Lineare Regression------------------
# Siehe Lektionen: 54,58,61,62,66 + 97 (CrossValidation)
# Kommentar: Keine Grid-Search möglich, da keine Hyperparameter bei LinRegr
#            Verwendung von Cross Validation anstatt Grid-Search
#            R² ist default Metric bei LinRegr.
#############################################################
from sklearn.linear_model import LinearRegression

regr = LinearRegression()
cv_results = cross_validate(regr, x_train, y_train, cv=3,
                            scoring=scoring_metrics) # https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html

test_r2_score = cv_results['test_r2_score']

print(f"Mean R2: {np.mean(test_r2_score)}")

#############################################################
# ---------------- KNNeigbors Regressor ---------------
# Siehe Lektionen: 68
# Siehe Programmierübung:
#############################################################
from sklearn.neighbors import KNeighborsRegressor

params = { "n_neighbors": [i for i in range(2, 24, 2)],
           "weights": ["uniform", "distance"]
         }

regr = KNeighborsRegressor()

grid = GridSearchCV(regr, params, cv=3, n_jobs=-1)
grid_result = grid.fit(x_train, y_train)

print_grid_cv_results(grid_result)

#############################################################
# ---------------- Random Forest Regressor ---------------
# Siehe Lektionen:
#############################################################
from sklearn.ensemble import RandomForestRegressor

params = {"n_estimators": [50*i for i in range(4, 10)],            # Alternativ Random-Search
          "max_depth": [i for i in range(20, 51, 10)] + [None]
         }

regr = RandomForestRegressor()

grid = GridSearchCV(regr, params, cv=3, n_jobs=-1)
grid_result = grid.fit(x_train, y_train)

print_grid_cv_results(grid_result)

#############################################################
# ---------------- GRADIENT BOOSTING REGRESSOR ---------------
# Siehe Lektionen:
# Kommentar: Random Search bei Lernrate bietet sich an,
#            bzw. größerer Bereich bei Grid Search
#############################################################

from sklearn.ensemble import GradientBoostingRegressor

params = {"n_estimators": [50*i for i in range(4, 10)],
          "max_depth": [i for i in range(20, 51, 10)] + [None]
         }

regr = GradientBoostingRegressor()

grid = GridSearchCV(regr, params, cv=3, n_jobs=-1)
grid_result = grid.fit(x_train, y_train)

print_grid_cv_results(grid_result)

#############################################################
# ---------------- SVM REGRESSOR ---------------
# Siehe Lektionen: 139
# Kommentar:
#############################################################
from sklearn.svm import SVR

params = {
        "kernel": ["linear", "sigmoid", "rbf", "poly"]
}

regr = SVR()

grid = GridSearchCV(regr, params, cv=3, n_jobs=-1)
grid_result = grid.fit(x_train, y_train)

print_grid_cv_results(grid_result)


#############################################################
# Finale Auswertung des BEST MODEL aller obiger Verfahren:
# Kommentar: Es werden zusätzlich 2 weitere Metriken angeschaut (mse, mae)
#############################################################

best_params = {'max_depth': 50, 'n_estimators': 400} # Erstellung eines Dictionarys der Optimal ermittelten Parameter
best_regressor = RandomForestRegressor

regr = best_regressor(**best_params) # Übergabe eines Dictionarys als Key: Value Paar mit **
regr.fit(x_train, y_train)
y_pred = regr.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse}")
print(f"MAE: {mae}")
print(f"R2: {r2}")

#### Residual Plot of Best Model (Punkte auf Nulllinie wäre Optimal)
def plot_residuals(regr, x_train, y_train, x_test, y_test):
        y_pred_train = regr.predict(x_train)
        y_pred_test = regr.predict(x_test)

        min_val = min(np.min(y_pred_train), np.min(y_pred_test))
        max_val = max(np.max(y_pred_train), np.max(y_pred_test))

        plt.scatter(y_pred_train, y_pred_train - y_train, color="blue")
        plt.scatter(y_pred_test, y_pred_test - y_test, color="red")
        plt.hlines(y=0, xmin=min_val, xmax=max_val)
        plt.legend(["Train", "Test"])
        plt.show()

plot_residuals(regr, x_train, y_train, x_test, y_test)