import pandas as pd #(Pandas ist so etwas wie excel in Pyhton)
from sklearn.datasets import load_boston

dataset = load_boston()

print(dataset)
x = dataset.data
y = dataset.target

print('Dataset X:', x)
print("\n")
print('Dataset Y:', y)

print(dataset["DESCR"])

df = pd.DataFrame(dataset.data, columns = dataset.feature_names)
print(df.head)