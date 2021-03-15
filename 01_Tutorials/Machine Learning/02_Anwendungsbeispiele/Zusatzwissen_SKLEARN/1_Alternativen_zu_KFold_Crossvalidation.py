# Hier werden Alternativen zu KFold vorgestellt ( welches die Datenpunkte in jeweils gleich große Teile splitet)

# LeaveOneOut (Empfehlung nur bei sehr kleinen Datasets)
# Nimmt alle Datenpunkte bis auf einen ins Trainingsset und nur einen ins Test-/Validationset
# Entspricht Kfold(n_splits = n) -> Wobei n_splits die Anzahl der Teilungen und n die Anzahl der Datenpunkte
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html

# StratifiedKFold (nur bei Klassifikationsdatensätze, die Imbalanced sind)
# 100 Datenpunkte, 90 Datenpunkte gehören zu Klasse 1 und 10 zu Klasse 2
# Im schlimmsten Fall kommt es im ValidationFold vor dass kein einziger Datenpunkt zur Klasse 2 gehört
# StratifiedKFold packt prozentual immer die vorliegende kleinere Klasse von der Menge her ins Validationset
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html


# Shuffle Split
# Zufällig zuweisung der Datenpunkte im Validation Set.
# Kann vorkomen, dass manche Datenpunkte nie im Validation-Set landen
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html?highlight=shufflesplit#sklearn.model_selection.ShuffleSplit