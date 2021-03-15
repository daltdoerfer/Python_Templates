# Feature Reduction (Dimensionality Reduction on Datasets, PCA wäre ebenfalls dies)
# https://scikit-learn.org/stable/modules/feature_selection.html
# Es kann sein dass man Features hat und diese bringen gar nichts,
# da diese keine Informationen die weiterhilft besitzen

# Removing Features with low Variance
# VarianceThreshold -> z.b ich will 90% der Varianz behalten, rest fliegt raus
# Beispiel wir haben 100 Features und in 90% der Fälle sind die Werte immer gleich -> macht höchstwahrscheinlich keinen Sinn

# Univariate feature Selection
# es gibt folgende Methoden:
# SelectKBest -> behält die k höchstgescorten Features (score_funktion muss übergeben werden)
#                                           als Score Funktion gibt es folgende:
#                                           For regression: f_regression, mutual_info_regression
#                                           For classification: chi2, f_classif, mutual_info_classif


# SelectPercentile -> wie bei PCA müssen prozentual die wichtigsten Features angegeben werden
# GenericUnivariateSelect ->

# Beispiel SelectKBest
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2 # -> Statistischer Test https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#sklearn.feature_selection.chi2
X, y = load_iris(return_X_y=True)
print(X.shape)
#(150, 4) # 4 Features im Dataset
X_new = SelectKBest(chi2, k=2).fit_transform(X, y) # es sollen die 2 Wichtigsten behalten werden
print(X_new.shape)
#(150, 2)