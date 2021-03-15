import numpy as np
np.random.seed(42)
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

dataset = load_wine()
x = dataset.data
y = dataset.target

print(f"target names: {dataset.target_names}")
print(f"DESCR:\n{dataset.DESCR}")

df = pd.DataFrame(x, columns=dataset.feature_names)
df["y"] = y
df.head()